from __future__ import annotations

from abc import ABC, abstractmethod


class ModelProvider(ABC):
    @abstractmethod
    async def chat(self, model: str, messages: list[dict], *, json_mode: bool = False, temperature: float = 0.2) -> str:
        raise NotImplementedError

    @abstractmethod
    async def list_models(self) -> list[dict]:
        raise NotImplementedError

    @abstractmethod
    async def healthy(self) -> bool:
        raise NotImplementedError
