from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


def _bool(name: str, default: bool) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


@dataclass(slots=True)
class Settings:
    root: Path
    host: str
    port: int
    ollama_url: str
    manager_model: str
    worker_model: str
    qa_model: str
    max_concurrency: int
    max_retries: int
    allow_writes: bool
    auto_execute: bool
    workspace: Path
    data_dir: Path

    @classmethod
    def load(cls) -> "Settings":
        root = Path(__file__).resolve().parents[1]
        workspace_env = os.getenv("MOZART_WORKSPACE", "./workspace")
        data_env = os.getenv("MOZART_DATA_DIR", "./data")
        workspace = Path(workspace_env).expanduser()
        data_dir = Path(data_env).expanduser()
        if not workspace.is_absolute():
            workspace = (root / workspace).resolve()
        if not data_dir.is_absolute():
            data_dir = (root / data_dir).resolve()
        workspace.mkdir(parents=True, exist_ok=True)
        data_dir.mkdir(parents=True, exist_ok=True)
        return cls(
            root=root,
            host=os.getenv("MOZART_HOST", "0.0.0.0"),
            port=int(os.getenv("MOZART_PORT", "8765")),
            ollama_url=os.getenv("MOZART_OLLAMA_URL", "http://127.0.0.1:11434").rstrip("/"),
            manager_model=os.getenv("MOZART_MANAGER_MODEL", "qwen3:8b"),
            worker_model=os.getenv("MOZART_WORKER_MODEL", "qwen3:4b"),
            qa_model=os.getenv("MOZART_QA_MODEL", "qwen3:8b"),
            max_concurrency=max(1, int(os.getenv("MOZART_MAX_CONCURRENCY", "2"))),
            max_retries=max(0, int(os.getenv("MOZART_MAX_RETRIES", "2"))),
            allow_writes=_bool("MOZART_ALLOW_WRITES", True),
            auto_execute=_bool("MOZART_AUTO_EXECUTE", True),
            workspace=workspace,
            data_dir=data_dir,
        )
