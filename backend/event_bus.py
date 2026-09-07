from __future__ import annotations

import asyncio
from collections.abc import AsyncIterator

from .db import Database
from .models import EventEnvelope


class EventBus:
    def __init__(self, db: Database):
        self.db = db
        self._subs: set[asyncio.Queue[dict]] = set()
        self._lock = asyncio.Lock()

    async def publish(self, event_type: str, payload: dict, mission_id: str | None = None) -> dict:
        event = EventEnvelope(type=event_type, mission_id=mission_id, payload=payload)
        seq = await self.db.append_event(event)
        data = event.model_dump()
        data["seq"] = seq
        async with self._lock:
            subscribers = list(self._subs)
        for queue in subscribers:
            try:
                queue.put_nowait(data)
            except asyncio.QueueFull:
                try:
                    queue.get_nowait()
                except asyncio.QueueEmpty:
                    pass
                try:
                    queue.put_nowait(data)
                except asyncio.QueueFull:
                    pass
        return data

    async def subscribe(self) -> AsyncIterator[dict]:
        queue: asyncio.Queue[dict] = asyncio.Queue(maxsize=512)
        async with self._lock:
            self._subs.add(queue)
        try:
            while True:
                yield await queue.get()
        finally:
            async with self._lock:
                self._subs.discard(queue)
