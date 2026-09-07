from __future__ import annotations


def built_in_skills() -> list[dict]:
    return [
        {"id": "ce-plan", "name": "Plan", "description": "Decompose outcomes into unique subsystem-specific contracts."},
        {"id": "ce-work", "name": "Build", "description": "Execute bounded implementation jobs against the workspace."},
        {"id": "qa", "name": "QA", "description": "Review artifacts against explicit success criteria and reject weak work."},
        {"id": "research", "name": "Research", "description": "Inspect codebase context before implementation."},
        {"id": "ce-review", "name": "Review", "description": "Merge accepted results and surface remaining gaps."},
    ]
