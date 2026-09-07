from __future__ import annotations


class PluginRegistry:
    def __init__(self):
        self.providers: dict[str, object] = {}

    def register(self, name: str, provider: object) -> None:
        self.providers[name] = provider

    def list(self) -> list[str]:
        return sorted(self.providers)
