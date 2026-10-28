"""Mob drop chances, cached beside the quest graph.

One row per NPC that drops something: npc id, the zone he stands in, and each
item with the percent chance a kill yields it. The other direction is item id
to those NPCs and the same percent. A campaign leaf whose quest graph never
mentions the item kills the spawned mob with the highest chance.

The percent is the chance of at least one copy, following the server's loot
roll: the loot-table probability, then either an independent chance or one
weighted pick from the list, repeated for the table multiplier.
"""

from __future__ import annotations

import json
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

from eqclient.catalog import _table, _tuple

DEFAULT_DROPS = str(Path.home() / ".eqclient" / "drops.jsonl")
_VERSION = 2
# lootdrop_entries: chance 4, multiplier 8, npc_min_level 9, npc_max_level 10.
# loottable_entries: multiplier 2, droplimit 3, mindrop 4, probability 5.
_CHANCE = 4
_ENTRY_MULT = 8
_NPC_MIN = 9
_NPC_MAX = 10
_TABLE_MULT = 2
_DROP_LIMIT = 3
_MIN_DROP = 4
_PROBABILITY = 5
_LOOTTABLE = 17


@dataclass(frozen=True)
class Dropper:
    npc_id: int
    zone_id: int
    zone: str
    name: str
    level: int = 0
    chance: float = 0.0


@dataclass
class DropBook:
    """npc id → drop chances, and item id → the NPCs who drop it and how often."""

    by_npc: dict[int, dict] = field(default_factory=dict)
    by_item: dict[int, dict] = field(default_factory=dict)

    def drops(self, item_id: int) -> bool:
        return item_id in self.by_item

    def chance(self, item_id: int, npc_id: int) -> float:
        for stored_id, pct in _pairs((self.by_item.get(item_id) or {}).get("npcs")):
            if stored_id == npc_id:
                return pct
        return 0.0

    def best(self, item_id: int, here: str = "") -> Dropper | None:
        """The spawned mob with the highest chance. Ties stay in this zone, then the lower level."""
        row = self.by_item.get(item_id)
        if not row:
            return None
        killers = [self._dropper(npc_id, pct) for npc_id, pct in _pairs(row.get("npcs"))]
        killers = [killer for killer in killers if killer is not None and killer.chance > 0]
        if not killers:
            return None
        here = (here or "").lower()

        def rank(killer: Dropper) -> tuple:
            local = 0 if killer.zone == here else 1
            return (-killer.chance, local, killer.level or 10**9, killer.zone_id or 10**9, killer.npc_id)

        killers.sort(key=rank)
        return killers[0]

    def _dropper(self, npc_id: int, chance: float) -> Dropper | None:
        row = self.by_npc.get(int(npc_id))
        if not row:
            return None
        return Dropper(
            int(npc_id),
            int(row.get("zone") or 0),
            str(row.get("where") or ""),
            str(row.get("name") or ""),
            int(row.get("level") or 0),
            float(chance),
        )


def drops_from_lines(lines) -> DropBook:
    """Drop chances from a peq dump. No live query."""
    mode = ""
    lists: dict[int, list[tuple]] = defaultdict(list)
    tables: dict[int, list[tuple]] = defaultdict(list)
    names: dict[int, str] = {}
    levels: dict[int, int] = {}
    loot_of: dict[int, int] = {}
    groups: dict[int, set[int]] = defaultdict(set)
    group_zones: dict[int, set[str]] = defaultdict(set)
    zone_ids: dict[str, int] = {}
    for raw in lines:
        line = raw.strip()
        if line.startswith("INSERT INTO `"):
            mode = _table(line)
            continue
        if not line.startswith("("):
            continue
        fields = _tuple(line)
        if mode == "lootdrop_entries":
            _take_drop(fields, lists)
        elif mode == "loottable_entries":
            _take_table(fields, tables)
        elif mode == "npc_types":
            _take_npc(fields, names, levels, loot_of)
        elif mode == "spawnentry":
            _take_entry(fields, groups)
        elif mode == "spawn2":
            _take_spawn(fields, group_zones)
        elif mode == "zone":
            _take_zone_id(fields, zone_ids)
    book = DropBook()
    killers_of: dict[int, list[list]] = defaultdict(list)
    for npc_id, loottable_id in loot_of.items():
        chances = _npc_chances(tables.get(loottable_id, ()), lists, levels.get(npc_id, 0))
        if not chances:
            continue
        zones = {zone for group in groups.get(npc_id, ()) for zone in group_zones.get(group, ())}
        if not zones:
            continue
        zone_id, where = _pick_zone(zones, zone_ids)
        items = [[item_id, chances[item_id]] for item_id in sorted(chances)]
        book.by_npc[npc_id] = {
            "zone": zone_id,
            "where": where,
            "name": names.get(npc_id, ""),
            "level": levels.get(npc_id, 0),
            "items": items,
        }
        for item_id, pct in items:
            killers_of[item_id].append([npc_id, pct])
    for item_id, rows in killers_of.items():
        book.by_item[item_id] = {"npcs": sorted(rows, key=lambda row: row[0])}
    return book


def _npc_chances(rows, lists, npc_level: int) -> dict[int, float]:
    parts: dict[int, list[float]] = defaultdict(list)
    for lootdrop_id, mult, drop_limit, min_drop, probability in rows:
        opened = _open_chance(probability)
        if opened <= 0 or mult <= 0:
            continue
        for item_id, once in _list_chances(lists.get(lootdrop_id, ()), npc_level, drop_limit, min_drop).items():
            parts[item_id].append(_at_least(opened * once, mult))
    found: dict[int, float] = {}
    for item_id, chances in parts.items():
        pct = _percent(_merge(chances))
        if pct > 0:
            found[item_id] = pct
    return found


def _list_chances(entries, npc_level: int, drop_limit: int, min_drop: int) -> dict[int, float]:
    """Chance of each item once this lootdrop has been opened."""
    eligible = [row for row in entries if row[1] > 0 and _fits(npc_level, row[3], row[4])]
    if not eligible:
        return {}
    if drop_limit == 0 and min_drop == 0:
        return _independent(eligible)
    return _weighted(eligible, drop_limit, min_drop)


def _independent(entries) -> dict[int, float]:
    miss: dict[int, float] = defaultdict(lambda: 1.0)
    seen: set[int] = set()
    for item_id, chance, mult, _npc_min, _npc_max in entries:
        if mult <= 0:
            continue
        hit = min(1.0, chance / 100.0)
        miss[item_id] *= (1.0 - hit) ** mult
        seen.add(item_id)
    return {item_id: 1.0 - miss[item_id] for item_id in seen if miss[item_id] < 1.0}


def _weighted(entries, drop_limit: int, min_drop: int) -> dict[int, float]:
    limit = drop_limit
    if len(entries) > 100 and limit == 0:
        limit = 10
    if limit < min_drop:
        limit = min_drop
    if limit <= 0:
        return {}
    weights: dict[int, float] = defaultdict(float)
    roll_t = 0.0
    bypass = False
    no_loot = 1.0
    for item_id, chance, _mult, _npc_min, _npc_max in entries:
        weights[item_id] += chance
        roll_t += chance
        if chance >= 100:
            bypass = True
        else:
            no_loot *= max(0.0, (100.0 - chance) / 100.0)
    if roll_t <= 0:
        return {}
    soft = 1.0 if bypass else max(0.0, 1.0 - no_loot)
    found: dict[int, float] = {}
    for item_id, weight in weights.items():
        chance = _weighted_item(weight / roll_t, limit, min_drop, soft, bypass)
        if chance > 0:
            found[item_id] = chance
    return found


def _weighted_item(p_target: float, slots: int, min_drop: int, soft: float, bypass: bool) -> float:
    """Chance this weighted row is picked at least once across the drop slots."""
    if slots <= 0 or p_target <= 0:
        return 0.0
    if slots == 1:
        attempt = 1.0 if (min_drop >= 1 or bypass) else soft
        return attempt * p_target
    states = {(0, False): 1.0}
    need = min_drop
    for _slot in range(slots):
        nxt: dict[tuple[int, bool], float] = defaultdict(float)
        for (succ, got), mass in states.items():
            attempt = 1.0 if (succ < need or bypass) else soft
            if attempt < 1.0:
                nxt[(succ, got)] += mass * (1.0 - attempt)
            if attempt > 0:
                nxt[(min(succ + 1, need), True)] += mass * attempt * p_target
                nxt[(min(succ + 1, need), got)] += mass * attempt * (1.0 - p_target)
        states = nxt
    return sum(mass for (_succ, got), mass in states.items() if got)


def _open_chance(probability: float) -> float:
    if probability <= 0:
        return 0.0
    if probability >= 100:
        return 1.0
    return probability / 100.0


def _at_least(chance: float, times: int) -> float:
    if times <= 0 or chance <= 0:
        return 0.0
    if chance >= 1:
        return 1.0
    return 1.0 - (1.0 - chance) ** times


def _merge(chances) -> float:
    miss = 1.0
    for chance in chances:
        miss *= 1.0 - min(1.0, max(0.0, chance))
    return 1.0 - miss


def _percent(chance: float) -> float:
    return round(max(0.0, min(1.0, chance)) * 100.0, 4)


def _fits(npc_level: int, npc_min: int, npc_max: int) -> bool:
    if npc_level and npc_min and npc_level < npc_min:
        return False
    if npc_level and npc_max and npc_level > npc_max:
        return False
    return True


def _take_drop(fields: list[str], lists: dict[int, list[tuple]]) -> None:
    if len(fields) <= _CHANCE or not fields[0].isdigit() or not fields[1].lstrip("-").isdigit():
        return
    item_id = int(fields[1])
    if item_id <= 0:
        return
    lists[int(fields[0])].append(
        (
            item_id,
            _float(fields[_CHANCE]),
            _count(fields, _ENTRY_MULT, 1),
            _int(fields, _NPC_MIN),
            _int(fields, _NPC_MAX),
        )
    )


def _take_table(fields: list[str], tables: dict[int, list[tuple]]) -> None:
    if len(fields) < 2 or not fields[0].isdigit() or not fields[1].isdigit():
        return
    probability = _float(fields[_PROBABILITY]) if len(fields) > _PROBABILITY else 100.0
    tables[int(fields[0])].append(
        (
            int(fields[1]),
            _count(fields, _TABLE_MULT, 1),
            _int(fields, _DROP_LIMIT),
            _int(fields, _MIN_DROP),
            probability,
        )
    )


def _take_npc(fields: list[str], names: dict[int, str], levels: dict[int, int], loot_of: dict[int, int]) -> None:
    if len(fields) <= _LOOTTABLE or not fields[0].isdigit():
        return
    loottable_id = int(fields[_LOOTTABLE]) if fields[_LOOTTABLE].lstrip("-").isdigit() else 0
    if loottable_id <= 0:
        return
    npc_id = int(fields[0])
    names[npc_id] = fields[1].replace("_", " ").lstrip("#")
    levels[npc_id] = _int(fields, 3)
    loot_of[npc_id] = loottable_id


def _take_entry(fields: list[str], groups: dict[int, set[int]]) -> None:
    if len(fields) < 2 or not fields[0].isdigit() or not fields[1].isdigit():
        return
    groups[int(fields[1])].add(int(fields[0]))


def _take_spawn(fields: list[str], group_zones: dict[int, set[str]]) -> None:
    if len(fields) < 3 or not fields[1].isdigit() or not fields[2]:
        return
    group_zones[int(fields[1])].add(fields[2].lower())


def _take_zone_id(fields: list[str], zone_ids: dict[str, int]) -> None:
    if not fields or not fields[0]:
        return
    if len(fields) > 13 and fields[13].lstrip("-").isdigit() and int(fields[13]) > 0:
        zone_ids[fields[0].lower()] = int(fields[13])


def _pick_zone(zones: set[str], zone_ids: dict[str, int]) -> tuple[int, str]:
    ranked = sorted((zone_ids.get(zone, 10**9), zone) for zone in zones)
    zone_id, zone = ranked[0]
    return (0 if zone_id >= 10**9 else zone_id), zone


def _int(fields: list[str], index: int) -> int:
    if index >= len(fields):
        return 0
    raw = fields[index]
    return int(raw) if raw.lstrip("-").isdigit() else 0


def _count(fields: list[str], index: int, default: int) -> int:
    """A missing multiplier defaults to one roll. An explicit zero never rolls."""
    if index >= len(fields) or fields[index] == "":
        return default
    raw = fields[index]
    return int(raw) if raw.lstrip("-").isdigit() else default


def _float(raw: str) -> float:
    try:
        return float(raw)
    except ValueError:
        return 0.0


def _pairs(raw) -> list[tuple[int, float]]:
    found: list[tuple[int, float]] = []
    for entry in raw or ():
        if isinstance(entry, (list, tuple)) and entry:
            pct = float(entry[1]) if len(entry) > 1 else 100.0
            found.append((int(entry[0]), pct))
        else:
            found.append((int(entry), 100.0))
    return found


def build_drops(peq: str | Path) -> DropBook:
    return drops_from_lines(_lines(str(peq)))


def write_drops(book: DropBook, path: str) -> None:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    lines = [json.dumps({"kind": "meta", "version": _VERSION}, ensure_ascii=True)]
    for npc_id, row in sorted(book.by_npc.items()):
        lines.append(
            json.dumps(
                {
                    "kind": "drop",
                    "npc": npc_id,
                    "zone": int(row.get("zone") or 0),
                    "where": row.get("where") or "",
                    "name": row.get("name") or "",
                    "level": int(row.get("level") or 0),
                    "items": [[int(item_id), float(pct)] for item_id, pct in _pairs(row.get("items"))],
                },
                ensure_ascii=True,
            )
        )
    for item_id, row in sorted(book.by_item.items()):
        lines.append(
            json.dumps(
                {
                    "kind": "item",
                    "item": item_id,
                    "npcs": [[int(npc_id), float(pct)] for npc_id, pct in _pairs(row.get("npcs"))],
                },
                ensure_ascii=True,
            )
        )
    destination.write_text("\n".join(lines) + "\n", encoding="utf-8")


def read_drops(path: str) -> DropBook:
    book = DropBook()
    file = Path(path)
    if not file.is_file():
        return book
    for line in file.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        if row.get("kind") == "drop":
            npc_id = int(row.get("npc") or 0)
            if npc_id:
                book.by_npc[npc_id] = {
                    "zone": int(row.get("zone") or 0),
                    "where": str(row.get("where") or ""),
                    "name": str(row.get("name") or ""),
                    "level": int(row.get("level") or 0),
                    "items": [[item_id, pct] for item_id, pct in _pairs(row.get("items"))],
                }
        elif row.get("kind") == "item":
            item_id = int(row.get("item") or 0)
            if item_id:
                book.by_item[item_id] = {"npcs": [[npc_id, pct] for npc_id, pct in _pairs(row.get("npcs"))]}
    return book


def _version_ok(path: str) -> bool:
    file = Path(path)
    if not file.is_file():
        return False
    first = ""
    for line in file.read_text(encoding="utf-8").splitlines():
        if line.strip():
            first = line
            break
    if not first:
        return False
    try:
        row = json.loads(first)
    except json.JSONDecodeError:
        return False
    return row.get("kind") == "meta" and int(row.get("version") or 0) >= _VERSION


def ensure_drops(
    path: str | None = None,
    peq: str | None = None,
    *,
    rebuild: bool = False,
) -> DropBook:
    """Build/load via cache_builders. Prefer read_drops at runtime."""
    from eqclient.cache_builders.drops import ensure_drops as _ensure

    return _ensure(path, peq, rebuild=rebuild)


def _lines(path: str):
    with open(path, encoding="latin1", errors="replace") as handle:
        yield from handle
