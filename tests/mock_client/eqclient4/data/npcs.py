import json
import os
from dataclasses import dataclass, field
from pathlib import Path

DEFAULT_NPCS = str(Path.home() / ".eqclient" / "npc_types.jsonl")


@dataclass
class NPC:
    id: int
    name: str = ""
    lastname: str = ""
    race_id: int = 0
    class_id: int = 0
    level: int = 0
    bodytype: int = 0
    npc_faction_id: int = 0
    spawngroups: list[int] = field(default_factory=list)
    zones: list[str] = field(default_factory=list)


_npcs: dict[int, NPC] = {}


def ensure_npcs(path: str | None = None) -> dict[int, NPC]:
    global _npcs
    if _npcs:
        return _npcs

    path = path or os.environ.get("EQEMU_NPCS", DEFAULT_NPCS)
    file = Path(path)
    if not file.is_file():
        raise FileNotFoundError(f"NPC types file not found: {path}")

    npcs: dict[int, NPC] = {}

    with open(file, "r") as f:
        for line in f:

            try:
                data = json.loads(line)
            except json.JSONDecodeError:
                continue
            npc = NPC(**data)
            npcs[npc.id] = npc

    _npcs = npcs
    return _npcs
