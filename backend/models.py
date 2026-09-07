from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Literal
from uuid import uuid4

from pydantic import BaseModel, Field, model_validator


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()


def new_id(prefix: str) -> str:
    return f"{prefix}-{uuid4().hex[:8].upper()}"


class MissionCreate(BaseModel):
    prompt: str | None = None
    goal: str | None = None
    objective: str | None = None
    mission: str | None = None

    @model_validator(mode="after")
    def require_text(self) -> "MissionCreate":
        if not self.text:
            raise ValueError("One of prompt, goal, objective or mission is required")
        return self

    @property
    def text(self) -> str:
        return next((v.strip() for v in (self.prompt, self.goal, self.objective, self.mission) if v and v.strip()), "")


class Artifact(BaseModel):
    path: str
    name: str | None = None
    summary: str = ""
    diff: str = ""
    content: str = ""


class AgentRecord(BaseModel):
    id: str = Field(default_factory=lambda: new_id("A"))
    mission_id: str
    parent_id: str | None = None
    rank: Literal["CEO", "DIRECTOR", "MANAGER", "SUBMANAGER", "WORKER", "REVIEWER"] = "WORKER"
    branch: str = "runtime"
    name: str
    role: str = "worker"
    mission: str
    definition_of_done: list[str] = Field(default_factory=list)
    skills: list[str] = Field(default_factory=list)
    tools: list[str] = Field(default_factory=list)
    state: str = "created"
    progress: float = 0.0
    confidence: float = 0.0
    status_message: str = "Created"
    job_id: str | None = None
    created_at: str = Field(default_factory=utcnow)
    updated_at: str = Field(default_factory=utcnow)


class JobRecord(BaseModel):
    id: str = Field(default_factory=lambda: new_id("J"))
    mission_id: str
    manager_id: str | None = None
    assignee: str = "Unassigned"
    title: str
    description: str
    branch: str = "runtime"
    status: str = "queued"
    progress: float = 0.0
    attempts: int = 0
    max_attempts: int = 2
    recovery_count: int = 0
    definition_of_done: list[str] = Field(default_factory=list)
    files_hint: list[str] = Field(default_factory=list)
    depends_on: list[str] = Field(default_factory=list)
    files: list[Artifact] = Field(default_factory=list)
    failure_reason: str = ""
    output: str = ""
    evidence: list[str] = Field(default_factory=list)
    tool_events: list[dict[str, Any]] = Field(default_factory=list)
    created_at: str = Field(default_factory=utcnow)
    updated_at: str = Field(default_factory=utcnow)


class MissionRecord(BaseModel):
    id: str = Field(default_factory=lambda: new_id("M"))
    title: str
    objective: str
    status: str = "starting"
    progress: float = 0.0
    loop: int = 1
    created_at: str = Field(default_factory=utcnow)
    updated_at: str = Field(default_factory=utcnow)


class EventEnvelope(BaseModel):
    type: str
    ts: str = Field(default_factory=utcnow)
    mission_id: str | None = None
    payload: dict[str, Any] = Field(default_factory=dict)
