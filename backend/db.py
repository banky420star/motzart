from __future__ import annotations

import asyncio
import json
import sqlite3
from pathlib import Path
from typing import Any

from .models import AgentRecord, EventEnvelope, JobRecord, MissionRecord, utcnow


class Database:
    def __init__(self, path: Path):
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.lock = asyncio.Lock()
        self._init_schema()

    def _init_schema(self) -> None:
        self.conn.executescript(
            """
            PRAGMA journal_mode=WAL;
            CREATE TABLE IF NOT EXISTS missions (
              id TEXT PRIMARY KEY, created_at TEXT NOT NULL, updated_at TEXT NOT NULL, payload TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS agents (
              id TEXT PRIMARY KEY, mission_id TEXT NOT NULL, created_at TEXT NOT NULL, updated_at TEXT NOT NULL, payload TEXT NOT NULL
            );
            CREATE INDEX IF NOT EXISTS idx_agents_mission ON agents(mission_id);
            CREATE TABLE IF NOT EXISTS jobs (
              id TEXT PRIMARY KEY, mission_id TEXT NOT NULL, created_at TEXT NOT NULL, updated_at TEXT NOT NULL, signature TEXT NOT NULL, payload TEXT NOT NULL
            );
            CREATE UNIQUE INDEX IF NOT EXISTS idx_jobs_mission_signature ON jobs(mission_id, signature);
            CREATE INDEX IF NOT EXISTS idx_jobs_mission ON jobs(mission_id);
            CREATE TABLE IF NOT EXISTS events (
              seq INTEGER PRIMARY KEY AUTOINCREMENT, mission_id TEXT, ts TEXT NOT NULL, type TEXT NOT NULL, payload TEXT NOT NULL
            );
            CREATE INDEX IF NOT EXISTS idx_events_mission_seq ON events(mission_id, seq);
            CREATE TABLE IF NOT EXISTS memories (
              id INTEGER PRIMARY KEY AUTOINCREMENT, mission_id TEXT, branch TEXT, title TEXT, payload TEXT NOT NULL, created_at TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS settings (
              key TEXT PRIMARY KEY, value TEXT NOT NULL, updated_at TEXT NOT NULL
            );
            """
        )
        self.conn.commit()

    @staticmethod
    def signature(title: str, description: str, branch: str) -> str:
        raw = " ".join(f"{branch} {title} {description}".lower().split())
        for token in ("implement", "create", "build", "execute", "perform", "repair", "fix", "update", "task", "job"):
            raw = raw.replace(token, "")
        return " ".join(raw.split())[:320]

    async def save_mission(self, mission: MissionRecord) -> None:
        mission.updated_at = utcnow()
        data = mission.model_dump_json()
        async with self.lock:
            self.conn.execute(
                "INSERT INTO missions(id,created_at,updated_at,payload) VALUES(?,?,?,?) "
                "ON CONFLICT(id) DO UPDATE SET updated_at=excluded.updated_at,payload=excluded.payload",
                (mission.id, mission.created_at, mission.updated_at, data),
            )
            self.conn.commit()

    async def save_agent(self, agent: AgentRecord) -> None:
        agent.updated_at = utcnow()
        async with self.lock:
            self.conn.execute(
                "INSERT INTO agents(id,mission_id,created_at,updated_at,payload) VALUES(?,?,?,?,?) "
                "ON CONFLICT(id) DO UPDATE SET updated_at=excluded.updated_at,payload=excluded.payload",
                (agent.id, agent.mission_id, agent.created_at, agent.updated_at, agent.model_dump_json()),
            )
            self.conn.commit()

    async def save_job(self, job: JobRecord) -> bool:
        job.updated_at = utcnow()
        sig = self.signature(job.title, job.description, job.branch)
        async with self.lock:
            existing = self.conn.execute(
                "SELECT id FROM jobs WHERE mission_id=? AND signature=? AND id<>?",
                (job.mission_id, sig, job.id),
            ).fetchone()
            if existing:
                return False
            self.conn.execute(
                "INSERT INTO jobs(id,mission_id,created_at,updated_at,signature,payload) VALUES(?,?,?,?,?,?) "
                "ON CONFLICT(id) DO UPDATE SET updated_at=excluded.updated_at,signature=excluded.signature,payload=excluded.payload",
                (job.id, job.mission_id, job.created_at, job.updated_at, sig, job.model_dump_json()),
            )
            self.conn.commit()
            return True

    async def append_event(self, event: EventEnvelope) -> int:
        async with self.lock:
            cur = self.conn.execute(
                "INSERT INTO events(mission_id,ts,type,payload) VALUES(?,?,?,?)",
                (event.mission_id, event.ts, event.type, event.model_dump_json()),
            )
            self.conn.commit()
            return int(cur.lastrowid)

    async def add_memory(self, mission_id: str, branch: str, title: str, payload: dict[str, Any]) -> None:
        async with self.lock:
            self.conn.execute(
                "INSERT INTO memories(mission_id,branch,title,payload,created_at) VALUES(?,?,?,?,?)",
                (mission_id, branch, title, json.dumps(payload), utcnow()),
            )
            self.conn.commit()

    async def latest_mission(self) -> MissionRecord | None:
        async with self.lock:
            row = self.conn.execute("SELECT payload FROM missions ORDER BY created_at DESC LIMIT 1").fetchone()
        return MissionRecord.model_validate_json(row["payload"]) if row else None

    async def get_mission(self, mission_id: str) -> MissionRecord | None:
        async with self.lock:
            row = self.conn.execute("SELECT payload FROM missions WHERE id=?", (mission_id,)).fetchone()
        return MissionRecord.model_validate_json(row["payload"]) if row else None

    async def list_missions(self, limit: int = 30) -> list[MissionRecord]:
        async with self.lock:
            rows = self.conn.execute("SELECT payload FROM missions ORDER BY created_at DESC LIMIT ?", (limit,)).fetchall()
        return [MissionRecord.model_validate_json(r["payload"]) for r in rows]

    async def agents_for(self, mission_id: str) -> list[AgentRecord]:
        async with self.lock:
            rows = self.conn.execute("SELECT payload FROM agents WHERE mission_id=? ORDER BY created_at", (mission_id,)).fetchall()
        return [AgentRecord.model_validate_json(r["payload"]) for r in rows]

    async def jobs_for(self, mission_id: str) -> list[JobRecord]:
        async with self.lock:
            rows = self.conn.execute("SELECT payload FROM jobs WHERE mission_id=? ORDER BY created_at", (mission_id,)).fetchall()
        return [JobRecord.model_validate_json(r["payload"]) for r in rows]

    async def events_for(self, mission_id: str | None = None, limit: int = 200) -> list[dict[str, Any]]:
        async with self.lock:
            if mission_id:
                rows = self.conn.execute(
                    "SELECT seq,payload FROM events WHERE mission_id=? ORDER BY seq DESC LIMIT ?", (mission_id, limit)
                ).fetchall()
            else:
                rows = self.conn.execute("SELECT seq,payload FROM events ORDER BY seq DESC LIMIT ?", (limit,)).fetchall()
        out = []
        for row in rows:
            item = json.loads(row["payload"])
            item["seq"] = row["seq"]
            out.append(item)
        return out

    async def memories(self, mission_id: str | None = None, limit: int = 200) -> list[dict[str, Any]]:
        async with self.lock:
            if mission_id:
                rows = self.conn.execute(
                    "SELECT * FROM memories WHERE mission_id=? ORDER BY id DESC LIMIT ?", (mission_id, limit)
                ).fetchall()
            else:
                rows = self.conn.execute("SELECT * FROM memories ORDER BY id DESC LIMIT ?", (limit,)).fetchall()
        return [
            {"id": r["id"], "mission_id": r["mission_id"], "branch": r["branch"], "title": r["title"], "created_at": r["created_at"], **json.loads(r["payload"])}
            for r in rows
        ]

    async def snapshot(self, mission_id: str | None = None) -> dict[str, Any] | None:
        mission = await (self.get_mission(mission_id) if mission_id else self.latest_mission())
        if not mission:
            return None
        agents = await self.agents_for(mission.id)
        jobs = await self.jobs_for(mission.id)
        payload = mission.model_dump()
        payload["agents"] = [a.model_dump() for a in agents]
        payload["jobs"] = [j.model_dump() for j in jobs]
        payload["event_count"] = len(await self.events_for(mission.id, 5000))
        return payload

    async def set_setting(self, key: str, value: Any) -> None:
        async with self.lock:
            self.conn.execute(
                "INSERT INTO settings(key,value,updated_at) VALUES(?,?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value,updated_at=excluded.updated_at",
                (key, json.dumps(value), utcnow()),
            )
            self.conn.commit()

    async def get_settings(self) -> dict[str, Any]:
        async with self.lock:
            rows = self.conn.execute("SELECT key,value FROM settings ORDER BY key").fetchall()
        out: dict[str, Any] = {}
        for row in rows:
            try:
                out[row["key"]] = json.loads(row["value"])
            except Exception:
                out[row["key"]] = row["value"]
        return out
