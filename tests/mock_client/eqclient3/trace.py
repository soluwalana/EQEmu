"""One line per bus opcode, and one line per handler that runs for it.

The live client appends to ~/.eqclient/logs/<character>/bus.log. EQEMU_BUS_LOG
overrides the path. EQEMU_BUS_LOG=off leaves the file alone. With no character
name the line still goes to ~/.eqclient/bus-v3.log.
"""

from __future__ import annotations

import os
from datetime import datetime
from pathlib import Path
from typing import TextIO

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
