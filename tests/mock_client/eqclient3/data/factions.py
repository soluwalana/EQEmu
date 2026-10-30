"""Kill→faction hits and NPC primary faction, cached beside the quest graph.

npc_types.npc_faction_id → npc_faction_entries (faction_id, value). A positive
value is what killing that NPC awards. Primary standing gates resolve through
npc_faction.primaryfaction for the quest NPC, then the same hit list.
"""

from __future__ import annotations

import json
import os
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

from eqclient3.data.cache_builders.common import peq_path
from eqclient3.data.catalog import _table, _tuple

DEFAULT_FACTIONS = str(Path.home() / ".eqclient" / "faction_hits.jsonl")
_NPC_FACTION_ID = 22
_PRIMARY = 2


@dataclass(frozen=True)
class FactionHit:
    """One NPC that awards `value` toward `faction_id` when killed."""

    faction_id: int
    value: int
    npc_id: int
    name: str
    zone: str
    zone_id: int = 0


@dataclass
class FactionBook:
    """faction_id → kill sources; npc name → primary faction id."""

    by_faction: dict[int, list[FactionHit]] = field(default_factory=dict)
    primary_of: dict[str, int] = field(default_factory=dict)  # normalized name → primaryfaction
    primary_at: dict[str, int] = field(default_factory=dict)  # "zone/name" → primaryfaction
    _densest: dict[int, str] = field(default_factory=dict)

    def index(self) -> None:
        """Remember the densest farm zone for each faction so later lookups do not rescan the hits."""
        self._densest = {int(faction_id): self._densest_zone(int(faction_id)) for faction_id in self.by_faction}

    def densest_zone(self, faction_id: int) -> str:
        faction_id = int(faction_id)
        if faction_id in self._densest:
            return self._densest[faction_id]
        return self._densest_zone(faction_id)

    def _densest_zone(self, faction_id: int) -> str:
        """Zone with the most distinct +faction kill NPCs (empty when unknown)."""
        hits = self.by_faction.get(int(faction_id)) or ()
        if not hits:
            return ""
        counts: dict[str, int] = defaultdict(int)
        for hit in hits:
            if hit.zone:
                counts[hit.zone] += 1
        if not counts:
            return ""
        # Tie-break: more total value, then lower zone id, then name.
        value_sum: dict[str, int] = defaultdict(int)
        zone_id: dict[str, int] = {}
        for hit in hits:
            if not hit.zone:
                continue
            value_sum[hit.zone] += hit.value
            zone_id.setdefault(hit.zone, hit.zone_id or 10**9)
        return max(
            counts,
            key=lambda zone: (counts[zone], value_sum[zone], -(zone_id.get(zone) or 10**9), zone),
        )

    def farm(self, faction_id: int, here: str = "") -> FactionHit | None:
        """Kill target in the zone with the most +faction NPCs (densest farm)."""
        hits = self.by_faction.get(int(faction_id)) or ()
        if not hits:
            return None
        densest = self.densest_zone(faction_id)
        here = (here or "").lower()
        # Stay only when already in the densest zone; otherwise travel there.
        target_zone = densest if densest else here
        pool = [hit for hit in hits if hit.zone == target_zone] or list(hits)
        pool.sort(key=lambda hit: (-hit.value, hit.name))
        return pool[0]

    def farm_names(self, faction_id: int, zone: str = "") -> set[str]:
        """Normalized NPC names that award this faction in `zone` (or densest zone)."""
        hits = self.by_faction.get(int(faction_id)) or ()
        if not hits:
            return set()
        where = (zone or "").lower() or self.densest_zone(faction_id)
        return {_norm(hit.name) for hit in hits if hit.zone == where and hit.name}

    def primary(self, zone: str, npc: str) -> int:
        """Primary faction id for a quest NPC, or 0 when unknown."""
        who = _norm(npc)
        if not who:
            return 0
        place = f"{(zone or '').lower()}/{who}".strip("/")
        if place in self.primary_at:
            return int(self.primary_at[place])
        return int(self.primary_of.get(who) or 0)


def factions_from_lines(lines) -> FactionBook:
    """Positive kill hits and NPC primary factions from a peq dump."""
    mode = ""
    # npc_faction_id → [(faction_id, value), ...]
    entries: dict[int, list[tuple[int, int]]] = defaultdict(list)
    # npc_faction.id → primaryfaction
    primary: dict[int, int] = {}
    names: dict[int, str] = {}
    npc_faction_of: dict[int, int] = {}
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
        if mode == "npc_faction_entries":
            _take_entry_hit(fields, entries)
        elif mode == "npc_faction":
            _take_primary(fields, primary)
        elif mode == "npc_types":
            _take_npc(fields, names, npc_faction_of)
        elif mode == "spawnentry":
            _take_spawn_group(fields, groups)
        elif mode == "spawn2":
            _take_spawn_zone(fields, group_zones)
        elif mode == "zone":
            _take_zone_id(fields, zone_ids)

    book = FactionBook()
    buckets: dict[int, list[FactionHit]] = defaultdict(list)
    for npc_id, nf_id in npc_faction_of.items():
        name = names.get(npc_id, "")
        if not name:
            continue
        key = _norm(name)
        prim = int(primary.get(nf_id) or 0)
        if prim and key:
            book.primary_of.setdefault(key, prim)
        zones = {zone for group in groups.get(npc_id, ()) for zone in group_zones.get(group, ())}
        if not zones:
            # Still record primary for named NPCs with no spawn2 (quest summons).
            continue
        zone_id, where = _pick_zone(zones, zone_ids)
        if prim and key:
            book.primary_at[f"{where}/{key}"] = prim
        for faction_id, value in entries.get(nf_id, ()):
            if value <= 0:
                continue
            buckets[faction_id].append(
                FactionHit(faction_id, value, npc_id, name, where, zone_id)
            )
    for faction_id, hits in buckets.items():
        # Dedupe (npc, zone) keeping the largest value.
        best: dict[tuple[int, str], FactionHit] = {}
        for hit in hits:
            key = (hit.npc_id, hit.zone)
            prior = best.get(key)
            if prior is None or hit.value > prior.value:
                best[key] = hit
        book.by_faction[faction_id] = sorted(
            best.values(),
            key=lambda hit: (-hit.value, hit.zone, hit.name),
        )
    return book


def _take_entry_hit(fields: list[str], entries: dict[int, list[tuple[int, int]]]) -> None:
    if len(fields) < 3:
        return
    if not fields[0].isdigit() or not fields[1].isdigit():
        return
    raw = fields[2]
    if not raw.lstrip("-").isdigit():
        return
    value = int(raw)
    if value == 0:
        return
    entries[int(fields[0])].append((int(fields[1]), value))


def _take_primary(fields: list[str], primary: dict[int, int]) -> None:
    if len(fields) <= _PRIMARY or not fields[0].isdigit():
        return
    raw = fields[_PRIMARY]
    if not raw.lstrip("-").isdigit():
        return
    primary[int(fields[0])] = int(raw)


def _take_npc(fields: list[str], names: dict[int, str], npc_faction_of: dict[int, int]) -> None:
    if len(fields) <= _NPC_FACTION_ID or not fields[0].isdigit():
        return
    nf = fields[_NPC_FACTION_ID]
    if not nf.lstrip("-").isdigit() or int(nf) <= 0:
        return
    npc_id = int(fields[0])
    names[npc_id] = fields[1].replace("_", " ").lstrip("#")
    npc_faction_of[npc_id] = int(nf)


def _take_spawn_group(fields: list[str], groups: dict[int, set[int]]) -> None:
    if len(fields) < 2 or not fields[0].isdigit() or not fields[1].isdigit():
        return
    groups[int(fields[1])].add(int(fields[0]))


def _take_spawn_zone(fields: list[str], group_zones: dict[int, set[str]]) -> None:
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


def _norm(name: str) -> str:
    return " ".join((name or "").lower().replace("_", " ").replace("#", " ").split())


def build_factions(peq: str | Path) -> FactionBook:
    return factions_from_lines(_lines(str(peq)))


def write_factions(book: FactionBook, path: str) -> None:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []
    for key, faction_id in sorted(book.primary_of.items()):
        lines.append(json.dumps({"kind": "primary", "name": key, "faction": faction_id}, ensure_ascii=True))
    for key, faction_id in sorted(book.primary_at.items()):
        lines.append(json.dumps({"kind": "primary_at", "at": key, "faction": faction_id}, ensure_ascii=True))
    for faction_id, hits in sorted(book.by_faction.items()):
        for hit in hits:
            lines.append(
                json.dumps(
                    {
                        "kind": "hit",
                        "faction": hit.faction_id,
                        "value": hit.value,
                        "npc": hit.npc_id,
                        "name": hit.name,
                        "zone": hit.zone,
                        "zone_id": hit.zone_id,
                    },
                    ensure_ascii=True,
                )
            )
    destination.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")


def read_factions(path: str) -> FactionBook:
    book = FactionBook()
    file = Path(path)
    if not file.is_file():
        book.index()
        return book
    buckets: dict[int, list[FactionHit]] = defaultdict(list)
    for line in file.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        kind = row.get("kind")
        if kind == "primary":
            name = _norm(str(row.get("name") or ""))
            faction_id = int(row.get("faction") or 0)
            if name and faction_id:
                book.primary_of[name] = faction_id
        elif kind == "primary_at":
            at = str(row.get("at") or "")
            faction_id = int(row.get("faction") or 0)
            if at and faction_id:
                book.primary_at[at] = faction_id
        elif kind == "hit":
            faction_id = int(row.get("faction") or 0)
            value = int(row.get("value") or 0)
            if faction_id and value > 0:
                buckets[faction_id].append(
                    FactionHit(
                        faction_id,
                        value,
                        int(row.get("npc") or 0),
                        str(row.get("name") or ""),
                        str(row.get("zone") or ""),
                        int(row.get("zone_id") or 0),
                    )
                )
    book.by_faction = dict(buckets)
    book.index()
    return book


def ensure_factions(
    path: str | None = None,
    peq: str | Path | None = None,
    *,
    rebuild: bool = False,
) -> FactionBook:
    """Load faction_hits.jsonl, or build once from the peq dump."""
    path = path or os.environ.get("EQEMU_FACTIONS", DEFAULT_FACTIONS)
    file = Path(path)
    if file.is_file() and not rebuild:
        return read_factions(path)
    dump = peq_path(peq)
    book = build_factions(dump) if dump.is_file() else FactionBook()
    if book.by_faction or book.primary_of:
        write_factions(book, path)
    return book


def _lines(path: str):
    with open(path, encoding="latin1", errors="replace") as handle:
        yield from handle
