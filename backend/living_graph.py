from __future__ import annotations

from collections import defaultdict
from pathlib import PurePosixPath
from typing import Any


BRANCH_LABELS = {
    "architecture": "Architecture",
    "frontend": "Frontend",
    "backend": "Backend",
    "runtime": "Runtime",
    "knowledge": "Knowledge",
    "research": "Research",
    "tools": "Tools",
    "tooling": "Tools",
    "infrastructure": "Tools & Infra",
    "infra": "Tools & Infra",
    "qa": "QA",
    "testing": "QA",
    "design": "Design",
    "data": "Data",
    "security": "Security",
    "docs": "Knowledge",
}


def canonical_branch(value: str | None) -> str:
    raw = (value or "").strip().lower().replace("_", "-")
    if not raw:
        return "project"
    aliases = {
        "ui": "frontend",
        "web": "frontend",
        "client": "frontend",
        "server": "backend",
        "api": "backend",
        "test": "qa",
        "tests": "qa",
        "review": "qa",
        "documentation": "knowledge",
        "memory": "knowledge",
        "rag": "knowledge",
        "devops": "infrastructure",
        "ops": "infrastructure",
    }
    return aliases.get(raw, raw)


def branch_label(branch: str) -> str:
    key = canonical_branch(branch)
    return BRANCH_LABELS.get(key, key.replace("-", " ").title())


def infer_branch_for_path(path: str) -> str:
    p = str(PurePosixPath(path)).lower()
    parts = set(PurePosixPath(p).parts)
    if any(token in p for token in ("test", "spec", "playwright", "cypress")):
        return "qa"
    if any(token in parts for token in ("frontend", "client", "ui", "components", "pages", "views")) or any(token in p for token in (".css", ".scss", ".tsx", ".jsx")):
        return "frontend"
    if any(token in parts for token in ("backend", "server", "api", "routes", "controllers")):
        return "backend"
    if any(token in parts for token in ("runtime", "workers", "orchestrator", "agents")):
        return "runtime"
    if any(token in parts for token in ("docs", "knowledge", "memory", "embeddings")) or p.endswith((".md", ".rst")):
        return "knowledge"
    if any(token in parts for token in ("scripts", "tools", "infra", ".github")) or p.endswith((".sh", ".command", ".yml", ".yaml")):
        return "tools"
    if any(token in parts for token in ("data", "db", "database", "migrations")):
        return "data"
    return "project"


def _job_file_paths(job: dict[str, Any]) -> list[str]:
    paths: list[str] = []
    for item in job.get("files") or []:
        if isinstance(item, dict) and item.get("path"):
            paths.append(str(item["path"]))
    for item in job.get("files_hint") or []:
        if isinstance(item, str) and item:
            paths.append(item)
    return paths


def build_living_graph(
    *,
    project: dict[str, Any],
    mission: dict[str, Any] | None,
    files: list[str],
    events: list[dict[str, Any]] | None = None,
    memory: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    mission = mission or {}
    agents = list(mission.get("agents") or [])
    jobs = list(mission.get("jobs") or [])
    events = list(events or [])
    memory = list(memory or [])

    stats: dict[str, dict[str, Any]] = defaultdict(lambda: {
        "agents": [],
        "jobs": [],
        "files": [],
        "active_jobs": 0,
        "blocked_jobs": 0,
        "completed_jobs": 0,
        "progress_total": 0.0,
    })

    for agent in agents:
        branch = canonical_branch(agent.get("branch"))
        stats[branch]["agents"].append(agent)

    claimed_files: dict[str, str] = {}
    for job in jobs:
        branch = canonical_branch(job.get("branch"))
        bucket = stats[branch]
        bucket["jobs"].append(job)
        status = str(job.get("status") or "queued").lower()
        if status in {"running", "assigned", "review", "retrying"}:
            bucket["active_jobs"] += 1
        if status in {"blocked", "failed", "rejected"}:
            bucket["blocked_jobs"] += 1
        if status == "completed":
            bucket["completed_jobs"] += 1
        bucket["progress_total"] += float(job.get("progress") or 0.0)
        for path in _job_file_paths(job):
            claimed_files[path] = branch

    for path in files:
        branch = claimed_files.get(path) or infer_branch_for_path(path)
        stats[branch]["files"].append(path)

    branch_nodes: list[dict[str, Any]] = []
    for branch, bucket in stats.items():
        meaningful = bucket["agents"] or bucket["jobs"] or bucket["files"]
        if not meaningful:
            continue
        job_count = len(bucket["jobs"])
        avg_progress = bucket["progress_total"] / job_count if job_count else 0.0
        # Review/QA work is usually transient biological activity, not a
        # permanent organ. It remains visible while active/blocked so the user
        # can inspect it, then disappears unless it creates durable structure.
        ephemeral = branch == "qa" and not bucket["files"]
        if ephemeral and not bucket["active_jobs"] and not bucket["blocked_jobs"]:
            continue
        branch_nodes.append({
            "id": f"branch:{branch}",
            "type": "branch",
            "branch": branch,
            "label": branch_label(branch),
            "agent_count": len(bucket["agents"]),
            "job_count": job_count,
            "active_jobs": bucket["active_jobs"],
            "blocked_jobs": bucket["blocked_jobs"],
            "completed_jobs": bucket["completed_jobs"],
            "file_count": len(bucket["files"]),
            "progress": avg_progress,
            "ephemeral": ephemeral,
            "persistent": not ephemeral,
            "agents": bucket["agents"],
            "jobs": bucket["jobs"],
            "files": bucket["files"][:80],
            "weight": max(1.0, len(bucket["agents"]) * 1.3 + job_count * 1.5 + min(12, len(bucket["files"])) * 0.28),
        })

    branch_nodes.sort(key=lambda item: (-int(item["active_jobs"]), -int(item["job_count"]), str(item["label"])))

    file_nodes: list[dict[str, Any]] = []
    for branch, bucket in stats.items():
        for index, path in enumerate(bucket["files"][:40]):
            file_nodes.append({
                "id": f"file:{path}",
                "type": "file",
                "path": path,
                "label": PurePosixPath(path).name,
                "branch": branch,
                "parent": f"branch:{branch}",
                "ordinal": index,
            })

    work_cells: list[dict[str, Any]] = []
    for job in jobs:
        status = str(job.get("status") or "queued").lower()
        branch = canonical_branch(job.get("branch"))
        work_cells.append({
            "id": str(job.get("id") or ""),
            "type": "work",
            "branch": branch,
            "target": f"branch:{branch}",
            "title": str(job.get("title") or "Work"),
            "description": str(job.get("description") or ""),
            "assignee": str(job.get("assignee") or "Unassigned"),
            "status": status,
            "progress": float(job.get("progress") or 0.0),
            "attempts": int(job.get("attempts") or 0),
            "failure_reason": str(job.get("failure_reason") or ""),
            "output": str(job.get("output") or ""),
            "evidence": list(job.get("evidence") or []),
            "tool_events": list(job.get("tool_events") or []),
            "files": _job_file_paths(job),
            "updated_at": job.get("updated_at"),
        })

    project_progress = float(project.get("stage_progress") or 0.0)
    mission_progress = float(mission.get("progress") or 0.0)
    if mission_progress > 1:
        mission_progress /= 100.0
    progress = max(project_progress, mission_progress)

    return {
        "project": project,
        "mission": {
            "id": mission.get("id"),
            "title": mission.get("title"),
            "objective": mission.get("objective"),
            "status": mission.get("status") or project.get("status") or "seed",
            "progress": mission_progress,
        },
        "stage": project.get("stage") or "seed",
        "progress": progress,
        "core": {
            "id": "core",
            "type": "core",
            "label": "Mozart",
            "stage": project.get("stage") or "seed",
            "status": mission.get("status") or project.get("status") or "seed",
            "progress": progress,
            "agent_count": len(agents),
            "job_count": len(jobs),
            "file_count": len(files),
            "memory_count": len(memory),
        },
        "branches": branch_nodes,
        "files": file_nodes,
        "work": work_cells,
        "events": events[:100],
        "memory": memory[:100],
    }
