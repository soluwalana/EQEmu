import logging
import os
import sqlite3
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Literal, TextIO

log = logging.getLogger("eqclient3")

_LEVELS = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
}


def configure() -> None:
    """Apply LOG_LEVEL and a timestamp to every line, and the character log file."""
    level = _LEVELS.get(os.environ.get("LOG_LEVEL", "INFO").strip().upper(), logging.INFO)
    log.setLevel(level)
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        stream=sys.stderr,
    )
    _character_file(level)


def _character_file(level: int) -> None:
    """Append the same lines to the character log. Tests and a nameless run skip this."""
    if os.environ.get("PYTEST_CURRENT_TEST"):
        return
    name = os.environ.get("EQEMU_CHAR", "").strip()
    if not name:
        return
    path = Path.home() / ".eqclient" / "logs" / name / "agent.log"
    path.parent.mkdir(parents=True, exist_ok=True)
    for handler in log.handlers:
        if isinstance(handler, logging.FileHandler) and Path(handler.baseFilename) == path:
            return
    handle = logging.FileHandler(path, encoding="utf-8")
    handle.setLevel(level)
    handle.setFormatter(logging.Formatter("%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S"))
    log.addHandler(handle)


configure()


def write(message: str, stream: TextIO | None = None) -> None:
    """Write one line. Embedded newlines become spaces."""
    target = sys.stderr if stream is None else stream
    line = " ".join(str(message).splitlines())
    target.write(line + "\n")
    target.flush()


_handle: TextIO | None = None
_opened: str | None = None


def _destination() -> str | None:
    raw = os.environ.get("EQEMU_BUS_LOG")
    if raw in ("0", "off"):
        return None
    if raw:
        return raw
    if os.environ.get("PYTEST_CURRENT_TEST"):
        return None
    name = os.environ.get("EQEMU_CHAR", "").strip()
    if not name:
        return str(Path.home() / ".eqclient" / "bus-v3.log")
    return str(Path.home() / ".eqclient" / "logs" / name / "bus.log")


def _file() -> TextIO | None:
    global _handle, _opened
    path = _destination()
    if path is None:
        return None
    if _handle is not None and _opened == path:
        return _handle
    if _handle is not None:
        _handle.close()
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    _handle = open(path, "a", encoding="utf-8", buffering=1)
    _opened = path
    return _handle


def _write(kind: str, text: str) -> None:
    handle = _file()
    if handle is None:
        return
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    handle.write(f"{stamp} {kind} {text}\n")


def note_comms(name: str, opcode: str, payload: object, sent: bool = False) -> None:
    size = len(payload) if isinstance(payload, (bytes, bytearray)) else 0
    _write(name, f"{opcode} bytes={size} sent={sent}")


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


class EmptyCapture:

    def record(self, direction: Direction, opcode: str, payload: object) -> None:
        pass

    def commit(self) -> None:
        pass

    def packets(self, opcode: str = "") -> list[Packet]:
        return []

    def close(self) -> None:
        pass


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

    def record(self, direction: Direction, opcode: str, payload: bytes) -> None:
        """Queue one raw body. A value that is not bytes is not a bus payload."""

        seen = datetime.now().isoformat(timespec="microseconds")
        self._pending.append((seen, self.character, opcode, direction, payload))

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


def open_capture(character: str) -> Capture | EmptyCapture:
    """Open the capture. It is on unless EQEMU_CAPTURE=off, the name is empty, or this is a test."""
    raw = os.environ.get("EQEMU_CAPTURE", "").strip()
    if raw in ("0", "off"):
        return EmptyCapture()
    if os.environ.get("PYTEST_CURRENT_TEST") and not raw:
        return EmptyCapture()
    path = capture_path(character)
    log.info("bus capture %s", path)
    return Capture(path, character)


def _direction(value: object) -> Direction | None:
    if value == "send":
        return "send"
    if value == "recv":
        return "recv"
    return None
