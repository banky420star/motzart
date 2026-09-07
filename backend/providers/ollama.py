from __future__ import annotations

import os

import httpx

from .base import ModelProvider


class OllamaProvider(ModelProvider):
    def __init__(self, base_url: str, timeout: float = 180.0):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    async def healthy(self) -> bool:
        try:
            async with httpx.AsyncClient(timeout=3.0) as client:
                res = await client.get(f"{self.base_url}/api/tags")
                return res.is_success
        except Exception:
            return False

    async def list_models(self) -> list[dict]:
        try:
            async with httpx.AsyncClient(timeout=5.0) as client:
                res = await client.get(f"{self.base_url}/api/tags")
                res.raise_for_status()
                data = res.json()
                return data.get("models", [])
        except Exception:
            return []

    async def chat(self, model: str, messages: list[dict], *, json_mode: bool = False, temperature: float = 0.2) -> str:
        num_ctx = max(4096, min(int(os.getenv("MOZART_OLLAMA_NUM_CTX", "8192")), 32768))
        payload = {
            "model": model,
            "messages": messages,
            "stream": False,
            "options": {"temperature": temperature, "num_ctx": num_ctx},
        }
        # Qwen3's reasoning mode is excellent for deep analysis but wasteful for
        # the tiny structured tool decisions Mozart makes dozens of times per
        # mission. Disable hidden thinking by default so local turns stay short.
        if os.getenv("MOZART_OLLAMA_THINK", "0").strip().lower() not in {"1", "true", "yes", "on"}:
            payload["think"] = False
        if json_mode:
            payload["format"] = "json"
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            res = await client.post(f"{self.base_url}/api/chat", json=payload)
            res.raise_for_status()
            data = res.json()
            return (data.get("message") or {}).get("content", "")
