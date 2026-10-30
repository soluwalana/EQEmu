"""One line per bus opcode, and one line per handler that runs for it.

The live client appends to ~/.eqclient/bus-v3.log. EQEMU_BUS_LOG overrides the
path. EQEMU_BUS_LOG=off leaves the file alone.
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
    return str(Path.home() / ".eqclient" / "bus-v3.log")


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


def note_opcode(opcode: str, payload: object, sent: bool = False) -> None:
    size = len(payload) if isinstance(payload, (bytes, bytearray)) else 0
    _write("opcode", f"{opcode} bytes={size} sent={sent}")


def note_handler(name: str, opcode: str) -> None:
    _write("handler", f"{name} {opcode}")
