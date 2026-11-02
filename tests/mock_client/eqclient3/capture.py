"""Raw bus bytes, separate from the journal.

The file is on by default, beside the bus text log:
~/.eqclient/logs/<character>/bus.sqlite3 next to bus.log.
EQEMU_CAPTURE overrides that path. EQEMU_CAPTURE=off leaves the file alone.
A test run writes nothing unless EQEMU_CAPTURE names a path.
"""

from __future__ import annotations

import os
import sqlite3
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Literal

from eqclient3.log import log

Direction = Literal["send", "recv"]

_SCHEMA = """
CREATE TABLE IF NOT EXISTS packets (
    TimeSeen TEXT NOT NULL,
    Character TEXT NOT NULL,
    Op_Code TEXT NOT NULL,
    Direction TEXT NOT NULL,
    Bytes BLOB NOT NULL
);
CREATE INDEX IF NOT EXISTS packets_character_time ON packets (Character, TimeSeen);
CREATE INDEX IF NOT EXISTS packets_opcode ON packets (Op_Code);
CREATE INDEX IF NOT EXISTS packets_character_opcode_time ON packets (Character, Op_Code, TimeSeen);
"""


@dataclass(frozen=True)
class Packet:
    time_seen: str
    character: str
    opcode: str
    direction: Direction
    payload: bytes


class Capture:

    def __init__(self, path: str | os.PathLike[str], character: str) -> None:
        self.character = character
        self.path = Path(path)
        if str(self.path) != ":memory:":
            self.path.parent.mkdir(parents=True, exist_ok=True)
        self._db = sqlite3.connect(self.path, timeout=5.0)
        if str(self.path) != ":memory:":
            self._db.execute("PRAGMA journal_mode=WAL")
        self._db.executescript(_SCHEMA)
        self._db.commit()
        self._pending: list[tuple[str, str, str, str, bytes]] = []

    def record(self, direction: Direction, opcode: str, payload: object) -> None:
        """Queue one raw body. A value that is not bytes is not a bus payload."""
        body = _raw(payload)
        if body is None or not opcode:
            return
        seen = datetime.now().isoformat(timespec="microseconds")
        self._pending.append((seen, self.character, opcode, direction, body))

    def commit(self) -> None:
        if not self._pending:
            return
        self._db.executemany(
            "INSERT INTO packets (TimeSeen, Character, Op_Code, Direction, Bytes) VALUES (?, ?, ?, ?, ?)",
            self._pending,
        )
        self._db.commit()
        self._pending.clear()

    def packets(self, opcode: str = "") -> list[Packet]:
        """Rows for this character, oldest first. An opcode limits the list to that code."""
        if opcode:
            rows = self._db.execute(
                "SELECT TimeSeen, Character, Op_Code, Direction, Bytes FROM packets WHERE Character = ? AND Op_Code = ? ORDER BY TimeSeen, rowid",
                (self.character, opcode),
            )
        else:
            rows = self._db.execute(
                "SELECT TimeSeen, Character, Op_Code, Direction, Bytes FROM packets WHERE Character = ? ORDER BY TimeSeen, rowid",
                (self.character,),
            )
        found: list[Packet] = []
        for seen, character, code, direction, body in rows:
            way = _direction(direction)
            if way is None:
                continue
            found.append(Packet(str(seen), str(character), str(code), way, bytes(body)))
        return found

    def close(self) -> None:
        self.commit()
        self._db.close()


def capture_path(character: str) -> Path:
    """Default file sits in the same directory as bus.log."""
    raw = os.environ.get("EQEMU_CAPTURE", "").strip()
    if raw and raw not in ("0", "off"):
        return Path(raw)
    bus = os.environ.get("EQEMU_BUS_LOG", "").strip()
    if bus and bus not in ("0", "off"):
        return Path(bus).with_name("bus.sqlite3")
    return Path.home() / ".eqclient" / "logs" / character / "bus.sqlite3"


def open_capture(character: str) -> Capture | None:
    """Open the capture. It is on unless EQEMU_CAPTURE=off, the name is empty, or this is a test."""
    if not character:
        return None
    raw = os.environ.get("EQEMU_CAPTURE", "").strip()
    if raw in ("0", "off"):
        return None
    if os.environ.get("PYTEST_CURRENT_TEST") and not raw:
        return None
    path = capture_path(character)
    log.info("bus capture %s", path)
    return Capture(path, character)


def _direction(value: object) -> Direction | None:
    if value == "send":
        return "send"
    if value == "recv":
        return "recv"
    return None


def _raw(payload: object) -> bytes | None:
    if isinstance(payload, (bytes, bytearray)):
        return bytes(payload)
    return None
