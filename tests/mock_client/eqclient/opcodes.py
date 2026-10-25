"""Load EQEmu opcode conf files. Values are the little-endian wire numbers."""

from __future__ import annotations

import re
from pathlib import Path

_HEX = re.compile(r"0x([0-9a-fA-F]+)")


def repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def load_opcodes(path: Path) -> dict[str, int]:
    """Parse the same way OpcodeManager::LoadOpcodesFile does: sscanf 0x%hx."""
    opcodes: dict[str, int] = {}
    text = path.read_text(encoding="utf-8", errors="replace")
    for raw in text.splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line.startswith("OP_") or "=" not in line:
            continue
        name, value = line.split("=", 1)
        match = _HEX.search(value)
        if match is None:
            continue
        opcodes[name.strip()] = int(match.group(1), 16)
    return opcodes


def titanium_opcodes() -> dict[str, int]:
    return load_opcodes(repo_root() / "utils" / "patches" / "patch_Titanium.conf")


def login_opcodes() -> dict[str, int]:
    return load_opcodes(repo_root() / "loginserver" / "login_util" / "login_opcodes.conf")


def require(opcodes: dict[str, int], name: str) -> int:
    try:
        return opcodes[name]
    except KeyError as exc:
        raise KeyError(f"{name} is missing from the opcode file") from exc
