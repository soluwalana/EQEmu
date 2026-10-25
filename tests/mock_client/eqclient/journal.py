"""SQLite memory of quest triggers this character has already fired.

A script can hail, then ask for a keyword, then take an item. The task packets
remember kills and deliveries. They do not remember which line was said, so the
next session would hail again and never reach the later trigger.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path


class Journal:
    def __init__(self, path: str) -> None:
        if path != ":memory:":
            Path(path).parent.mkdir(parents=True, exist_ok=True)
        self._db = sqlite3.connect(path, timeout=5.0)
        if path != ":memory:":
            self._db.execute("PRAGMA journal_mode=WAL")
        self._db.execute(
            """
            CREATE TABLE IF NOT EXISTS events (
                character TEXT NOT NULL,
                zone TEXT NOT NULL,
                npc TEXT NOT NULL,
                kind TEXT NOT NULL,
                detail TEXT NOT NULL,
                created TEXT NOT NULL DEFAULT (datetime('now')),
                PRIMARY KEY (character, zone, npc, kind, detail)
            )
            """
        )
        self._db.commit()

    def record(self, character: str, zone: str, npc: str, kind: str, detail: str) -> None:
        self._db.execute(
            "INSERT OR IGNORE INTO events (character, zone, npc, kind, detail) VALUES (?, ?, ?, ?, ?)",
            (character, zone, npc, kind, detail),
        )
        self._db.commit()

    def has(self, character: str, zone: str, npc: str, kind: str, detail: str) -> bool:
        row = self._db.execute(
            "SELECT 1 FROM events WHERE character = ? AND zone = ? AND npc = ? AND kind = ? AND detail = ?",
            (character, zone, npc, kind, detail),
        ).fetchone()
        return row is not None

    def triggers(self, character: str, zone: str, npc: str) -> list[tuple[str, str]]:
        """Kind and detail, in the order they were first recorded."""
        rows = self._db.execute(
            "SELECT kind, detail FROM events WHERE character = ? AND zone = ? AND npc = ? ORDER BY rowid",
            (character, zone, npc),
        ).fetchall()
        return [(kind, detail) for kind, detail in rows]

    def said(self, character: str, zone: str) -> set[tuple[str, str]]:
        rows = self._db.execute(
            "SELECT npc, detail FROM events WHERE character = ? AND zone = ? AND kind = 'say'",
            (character, zone),
        ).fetchall()
        return {(npc, detail) for npc, detail in rows}

    def handed(self, character: str, zone: str) -> set[tuple[str, str]]:
        rows = self._db.execute(
            "SELECT npc, detail FROM events WHERE character = ? AND zone = ? AND kind = 'handin'",
            (character, zone),
        ).fetchall()
        return {(npc, detail) for npc, detail in rows}

    def close(self) -> None:
        self._db.close()
