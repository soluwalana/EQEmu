"""Spawn points for an item. Built from the content dump, read by the item grind."""

from __future__ import annotations

import json
import os
from collections import defaultdict
from pathlib import Path

from eqclient4.data.cache_builders.common import peq_path
from eqclient4.data.catalog import _tuple
from eqclient4.data.drops import _lines, drops_from_lines
from eqclient4.log import log

OUT = Path(
    os.environ.get("EQEMU_ITEM_LOCATIONS", Path.home() / ".eqclient" / "item_locations.jsonl")
)


def spawn_xyz(fields: list[str]) -> tuple[str, float, float, float] | None:
    """spawn2 is id, spawngroupID, zone, version, x, y, z. Version is not a coordinate."""
    if len(fields) < 7:
        return None
    try:
        return fields[2].lower(), float(fields[4]), float(fields[5]), float(fields[6])
    except ValueError:
        log.error("spawn coordinates failed to parse", exc_info=True)
        return None


def _points(path: Path) -> dict[int, list[tuple[str, float, float, float]]]:
    """spawngroup -> spawn2 points. Zone is the short name; x, y, z follow version."""
    found: dict[int, list[tuple[str, float, float, float]]] = defaultdict(list)
    mode = ""
    for raw in _lines(str(path)):
        line = raw.strip()
        if line.startswith("INSERT INTO `"):
            mode = line.split("`", 2)[1]
            continue
        if mode != "spawn2" or not line.startswith("("):
            continue
        fields = _tuple(line)
        if len(fields) < 7 or not fields[1].isdigit():
            continue
        point = spawn_xyz(fields)
        if point is None:
            continue
        found[int(fields[1])].append(point)
    return found


def build_item_locations(root: Path | None = None) -> int:
    dump = peq_path(root)
    book = drops_from_lines(_lines(str(dump)))
    groups: dict[int, set[int]] = defaultdict(set)
    mode = ""
    for raw in _lines(str(dump)):
        line = raw.strip()
        if line.startswith("INSERT INTO `"):
            mode = line.split("`", 2)[1]
            continue
        if mode != "spawnentry" or not line.startswith("("):
            continue
        fields = _tuple(line)
        if len(fields) < 2 or not fields[0].isdigit() or not fields[1].isdigit():
            continue
        groups[int(fields[1])].add(int(fields[0]))
    points = _points(dump)
    written = 0
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8") as handle:
        for npc_id, row in sorted(book.by_npc.items()):
            for group in groups.get(npc_id, ()):
                for zone, x, y, z in points.get(group, ()):
                    for item_id, chance in row.get("items") or ():
                        handle.write(
                            json.dumps(
                                {
                                    "item_id": int(item_id),
                                    "zone": zone,
                                    "x": x,
                                    "y": y,
                                    "z": z,
                                    "npc_id": npc_id,
                                    "name": row.get("name") or "",
                                    "npc_level": int(row.get("level") or 0),
                                    "chance": float(chance),
                                },
                                separators=(",", ":"),
                            )
                            + "\n"
                        )
                        written += 1
    return written


def main() -> None:
    count = build_item_locations()
    print(f"item locations: {count} rows → {OUT}", flush=True)
