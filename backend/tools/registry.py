from __future__ import annotations

from .workspace import Workspace


class ToolRegistry:
    def __init__(self, workspace: Workspace):
        self.workspace = workspace

    def capabilities(self) -> dict:
        return {
            "workspace": {
                "inventory": True,
                "read": True,
                "write": self.workspace.allow_writes,
                "delete": False,
                "root": str(self.workspace.root),
            },
            "safety": {
                "path_traversal": "blocked",
                "credential_overwrite": "blocked",
                "destructive_delete": "not exposed",
            },
            "autonomous_worker": {
                "isolated_workspace": True,
                "list_files": True,
                "read_file": True,
                "search_text": True,
                "replace_text": self.workspace.allow_writes,
                "write_file": self.workspace.allow_writes,
                "safe_terminal": True,
                "diff": True,
                "delete": False,
            },
        }
