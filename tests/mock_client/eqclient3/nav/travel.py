"""Zone-to-zone transit graph. Built once from the offline peq dump, then saved.

Each transit records:
  - where the door/point is in the source zone (x, y, z, heading)
  - destination zone (short name + id) and land coords when known
  - requirements: key item, lockpick skill, expansion / content flags

Runtime pathfinding reads only the saved zone graph — never MariaDB or the dump.
"""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.quests.graph import QuestGraph

import json
import os
import re
from collections import defaultdict, deque
from dataclasses import asdict, dataclass, field
from pathlib import Path
from eqclient3.log import log
from eqclient3.data.cache_builders.common import peq_path as builder_peq_path
from eqclient3.nav.zones import remember, zone_id_of, zone_name_of

def peq_path(peq: str | Path | None = None) -> Path:
    """Offline dump path from the data builder."""
    return builder_peq_path(peq)
_ROW = re.compile('\\(([^)]*)\\)')
DEFAULT_ZONE_GRAPH = str(Path.home() / '.eqclient' / 'zone_graph.jsonl')

def zoneflag_key(zone_id: int) -> str:
    """Journal / graph flag name for a character zone flag (HasZoneFlag)."""
    return f'zoneflag:{int(zone_id)}'

@dataclass(frozen=True)
class TransitNeed:
    """Gates that must be satisfied before the agent can use this transit."""
    key_item: int = 0
    lockpick: int = 0
    min_expansion: int = -1
    max_expansion: int = -1
    content_flags: str = ''
    content_flags_disabled: str = ''
    zone_flag: int = 0

    def empty(self) -> bool:
        return not self.key_item and (not self.lockpick) and (self.min_expansion < 0) and (self.max_expansion < 0) and (not self.content_flags) and (not self.content_flags_disabled) and (not self.zone_flag)

    def to_dict(self) -> dict:
        row = {k: v for k, v in asdict(self).items() if v not in (0, -1, '')}
        return row

@dataclass(frozen=True)
class Transit:
    """One door, stone, or zone_point that leaves `zone` for `dest`."""
    zone: str
    door_id: int
    dest: str
    dest_id: int = 0
    via: str = 'door'
    name: str = ''
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    heading: float = 0.0
    dest_x: float = 0.0
    dest_y: float = 0.0
    dest_z: float = 0.0
    dest_heading: float = 0.0
    need: TransitNeed = field(default_factory=TransitNeed)

    def to_edge(self) -> dict:
        row: dict = {'kind': 'edge', 'rel': 'travel', 'from': self.zone, 'to': self.dest, 'door': self.door_id, 'dest_id': self.dest_id, 'via': self.via, 'x': self.x, 'y': self.y, 'z': self.z, 'heading': self.heading}
        if self.name:
            row['name'] = self.name
        if self.dest_x or self.dest_y or self.dest_z:
            row['dest_x'] = self.dest_x
            row['dest_y'] = self.dest_y
            row['dest_z'] = self.dest_z
            row['dest_heading'] = self.dest_heading
        need = self.need.to_dict()
        if need:
            row['need'] = need
        return row

    @classmethod
    def from_edge(cls, row: dict) -> Transit:
        need_raw = row.get('need') or {}
        need = TransitNeed(key_item=int(need_raw.get('key_item') or row.get('key_item') or 0), lockpick=int(need_raw.get('lockpick') or row.get('lockpick') or 0), min_expansion=int(need_raw.get('min_expansion') if need_raw.get('min_expansion') is not None else -1), max_expansion=int(need_raw.get('max_expansion') if need_raw.get('max_expansion') is not None else -1), content_flags=str(need_raw.get('content_flags') or ''), content_flags_disabled=str(need_raw.get('content_flags_disabled') or ''), zone_flag=int(need_raw.get('zone_flag') or row.get('zone_flag') or 0))
        return cls(zone=str(row.get('from') or row.get('zone') or '').lower(), door_id=int(row.get('door') or 0), dest=str(row.get('to') or '').lower(), dest_id=int(row.get('dest_id') or 0), via=str(row.get('via') or 'door'), name=str(row.get('name') or ''), x=float(row.get('x') or 0), y=float(row.get('y') or 0), z=float(row.get('z') or 0), heading=float(row.get('heading') or 0), dest_x=float(row.get('dest_x') or 0), dest_y=float(row.get('dest_y') or 0), dest_z=float(row.get('dest_z') or 0), dest_heading=float(row.get('dest_heading') or 0), need=need)

@dataclass(frozen=True)
class TravelLeg:
    """One hop on a planned path (door id + dest). Location comes from ZoneGraph.transit_at."""
    zone: str
    door_id: int
    dest: str
    dest_id: int = 0
    kind: str = 'door'

@dataclass
class ZoneGraph:
    """Connectivity: zone short↔id, doors index, and full transit records."""
    zones: dict[str, int] = field(default_factory=dict)
    flagged: dict[str, int] = field(default_factory=dict)
    doors: dict[str, dict[int, list[int]]] = field(default_factory=dict)
    edges: list[dict] = field(default_factory=list)
    transits: list[Transit] = field(default_factory=list)
    _at: dict[tuple[str, int], Transit] = field(default_factory=dict)
    _from: dict[str, tuple[Transit, ...]] = field(default_factory=dict)
    _by_id: dict[int, str] = field(default_factory=dict)
    _indexed: bool = False

    def index(self) -> None:
        """(zone, door) → transit, and zone → the doors that leave it."""
        at: dict[tuple[str, int], Transit] = {}
        grouped: dict[str, list[Transit]] = {}
        for transit in self.transits:
            grouped.setdefault(transit.zone, []).append(transit)
            at.setdefault((transit.zone, int(transit.door_id)), transit)
        self._at = at
        self._from = {zone: tuple(rows) for zone, rows in grouped.items()}
        self._by_id = {zone_id: name for name, zone_id in self.zones.items() if zone_id}
        self._indexed = True

    def remember_all(self) -> None:
        for name, zone_id in self.zones.items():
            if name and zone_id:
                remember(name, zone_id)

    def transit_at(self, zone: str, door_id: int) -> Transit | None:
        home = (zone or '').lower()
        door = int(door_id)
        if self._indexed:
            return self._at.get((home, door))
        for transit in self.transits:
            if transit.zone == home and transit.door_id == door:
                return transit
        return None

    def transits_from(self, zone: str) -> list[Transit]:
        home = (zone or '').lower()
        if self._indexed:
            return list(self._from.get(home, ()))
        return [t for t in self.transits if t.zone == home]

    def apply_to_quest_graph(self, graph: QuestGraph) -> None:
        if graph is None:
            return
        for zone, by_door in self.doors.items():
            home = graph.doors.setdefault(zone, {})
            for door_id, destinations in by_door.items():
                known = home.setdefault(int(door_id), [])
                for dest_id in destinations:
                    if dest_id not in known:
                        known.append(dest_id)
        seen = {(e.get('from'), e.get('to'), e.get('rel'), e.get('door'), e.get('via')) for e in graph.edges}
        for edge in self.edges:
            key = (edge.get('from'), edge.get('to'), edge.get('rel'), edge.get('door'), edge.get('via'))
            if key in seen:
                continue
            seen.add(key)
            graph.edges.append(dict(edge))
        for name, zone_id in self.flagged.items():
            flag = zoneflag_key(zone_id)
            edge = {'kind': 'edge', 'rel': 'needs', 'from': f'zone:{name}', 'to': f'flag:{flag}', 'flag': flag, 'at': 'set', 'zone': name}
            key = (edge['from'], edge['to'], edge['rel'], None, None)
            if key in seen:
                continue
            seen.add(key)
            graph.edges.append(edge)

def can_transit(transit: Transit, *, inventory_ids: set[int] | None = None, lockpick_skill: int=0, expansion: int=-1, flags: dict[str, int] | None = None, door_ids: set[int] | None = None) -> bool:
    """True when key / lockpick / expansion / zone-flag gates on the transit are met.

    When `door_ids` is set (live OP_Doors for the current zone), door/stone hops whose
    id is absent are rejected — peq may list Luclin stones the Titanium zone never spawned.
    """
    need = transit.need
    if need.key_item and (not inventory_ids or need.key_item not in inventory_ids):
        return False
    if need.lockpick and lockpick_skill < need.lockpick:
        return False
    if need.min_expansion >= 0 and expansion >= 0 and (expansion < need.min_expansion):
        return False
    if need.max_expansion >= 0 and expansion >= 0 and (expansion > need.max_expansion):
        return False
    if need.zone_flag:
        key = zoneflag_key(need.zone_flag)
        if not flags or key not in flags:
            return False
    if door_ids is not None and transit.door_id and (transit.via in {'door', 'stone'}) and (transit.door_id not in door_ids):
        return False
    return True

def adjacency(graph: ZoneGraph, *, inventory_ids: set[int] | None = None, lockpick_skill: int=0, expansion: int=-1, flags: dict[str, int] | None = None, door_ids: set[int] | None = None) -> dict[str, list[tuple[int, str, int]]]:
    """zone short → list of (door_id, dest_short, dest_zone_id), gated by transit needs when known."""
    links: dict[str, list[tuple[int, str, int]]] = defaultdict(list)
    zone_names = graph.zones or {}
    transits = graph.transits
    if transits:
        for transit in transits:
            if not can_transit(transit, inventory_ids=inventory_ids, lockpick_skill=lockpick_skill, expansion=expansion, flags=flags, door_ids=door_ids):
                continue
            dest = transit.dest or _name_of(transit.dest_id, zone_names) or zone_name_of(transit.dest_id) or f'zone{transit.dest_id}'
            links[transit.zone].append((transit.door_id, dest, transit.dest_id))
        return links
    doors = graph.doors or {}
    for zone, by_door in doors.items():
        home = (zone or '').lower()
        for door_id, destinations in by_door.items():
            for dest_id in destinations:
                dest_id = int(dest_id)
                dest = _name_of(dest_id, zone_names) or zone_name_of(dest_id) or f'zone{dest_id}'
                links[home].append((int(door_id), dest, dest_id))
    for edge in graph.edges or ():
        if edge.get('rel') != 'travel':
            continue
        transit = Transit.from_edge(edge)
        if not can_transit(transit, inventory_ids=inventory_ids, lockpick_skill=lockpick_skill, expansion=expansion, flags=flags, door_ids=door_ids):
            continue
        home = transit.zone
        dest = transit.dest
        if not home or not dest:
            continue
        dest_id = transit.dest_id or int(zone_names.get(dest) or zone_id_of(dest) or 0)
        links[home].append((transit.door_id, dest, dest_id))
    return links

def path(graph: ZoneGraph, here: str, dest: str, *, inventory_ids: set[int] | None = None, lockpick_skill: int=0, expansion: int=-1, flags: dict[str, int] | None = None, door_ids: set[int] | None = None) -> list[TravelLeg]:
    """BFS shortest path. Empty if already there or unreachable under the given gates."""
    start = (here or '').lower()
    goal = (dest or '').lower()
    if not start or not goal or start == goal:
        return []
    zone_names = graph.zones or {}
    goal_id = int(zone_names.get(goal) or zone_id_of(goal) or 0)
    links = adjacency(graph, inventory_ids=inventory_ids, lockpick_skill=lockpick_skill, expansion=expansion, flags=flags, door_ids=door_ids)
    queue: deque[str] = deque([start])
    prev: dict[str, tuple[str, int, str, int]] = {}
    seen = {start}
    while queue:
        cur = queue.popleft()
        for door_id, nxt, dest_id in links.get(cur, ()):
            key = nxt if not str(nxt).startswith('zone') else _name_of(dest_id, zone_names) or zone_name_of(dest_id) or nxt
            if key in seen:
                continue
            seen.add(key)
            prev[key] = (cur, door_id, key, dest_id)
            if key == goal or (dest_id and goal_id and (dest_id == goal_id)):
                return _rebuild(prev, start, key)
            queue.append(key)
    return []

def first_leg(graph: ZoneGraph, here: str, dest: str, **kwargs: object) -> TravelLeg | None:
    legs = path(graph, here, dest, **kwargs)
    return legs[0] if legs else None

def build_zone_graph(peq: str | Path, quest_doors: dict[str, dict[int, list[int]]] | None = None) -> ZoneGraph:
    """Offline dump → zones, door/point transits with coords + requirements."""
    peq = Path(peq)
    graph = ZoneGraph()
    if not peq.is_file():
        return graph
    text = peq.read_text(encoding='latin1', errors='replace')
    graph.zones, graph.flagged = _parse_zones(text)
    for name, zone_id in graph.zones.items():
        remember(name, zone_id)
    for transit in _parse_doors(text, graph.zones, graph.flagged):
        _add_transit(graph, transit)
    for transit in _parse_zone_points(text, graph.zones, graph.flagged):
        _add_transit(graph, transit)
    if quest_doors:
        for zone, by_door in quest_doors.items():
            home = (zone or '').lower()
            for door_id, destinations in by_door.items():
                for dest_id in destinations:
                    dest_id = int(dest_id)
                    dest = _name_of(dest_id, graph.zones) or zone_name_of(dest_id) or f'zone{dest_id}'
                    need = TransitNeed(zone_flag=dest_id) if dest in graph.flagged or dest_id in graph.flagged.values() else TransitNeed()
                    _add_transit(graph, Transit(zone=home, door_id=int(door_id), dest=dest, dest_id=dest_id, via='script', need=need))
    return graph

def bake_from_dump(path: str | Path) -> list[dict]:
    """Compat: travel edge dicts for quest-graph bake."""
    return list(build_zone_graph(path).edges)

def write_zone_graph(graph: ZoneGraph, path: str) -> None:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []
    for name, zone_id in sorted(graph.zones.items(), key=lambda pair: (pair[1], pair[0])):
        row: dict = {'kind': 'zone', 'name': name, 'id': int(zone_id)}
        if name in graph.flagged:
            row['flag_needed'] = 1
        lines.append(json.dumps(row, ensure_ascii=True))
    for transit in graph.transits:
        lines.append(json.dumps(transit.to_edge(), ensure_ascii=True))
    destination.write_text('\n'.join(lines) + ('\n' if lines else ''), encoding='utf-8')

def read_zone_graph(path: str) -> ZoneGraph:
    graph = ZoneGraph()
    file = Path(path)
    if not file.is_file():
        graph.index()
        return graph
    for line in file.read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        kind = row.get('kind', '')
        if kind == 'zone':
            name = str(row.get('name') or '').lower()
            zone_id = int(row.get('id') or 0)
            if name and zone_id:
                graph.zones[name] = zone_id
                if row.get('flag_needed') in (1, '1', True):
                    graph.flagged[name] = zone_id
            continue
        if kind == 'edge' or row.get('rel') == 'travel':
            _add_transit(graph, Transit.from_edge(row))
            continue
        if kind == 'door' and 'to' in row:
            zone = str(row.get('zone') or '').lower()
            door_id = int(row.get('door') or 0)
            for dest_id in row.get('to') or []:
                dest_id = int(dest_id)
                dest = _name_of(dest_id, graph.zones) or zone_name_of(dest_id) or f'zone{dest_id}'
                need = TransitNeed(zone_flag=dest_id) if dest in graph.flagged else TransitNeed()
                _add_transit(graph, Transit(zone=zone, door_id=door_id, dest=dest, dest_id=dest_id, via='door', need=need))
            continue
    graph.remember_all()
    graph.index()
    return graph

def ensure_zone_graph(path: str | None = None, peq: str | Path | None = None, quest_doors: dict[str, dict[int, list[int]]] | None = None, *, rebuild: bool=False) -> ZoneGraph:
    """Load zone_graph.jsonl, or build once from the peq dump."""
    path = path or os.environ.get('EQEMU_ZONE_GRAPH', DEFAULT_ZONE_GRAPH)
    file = Path(path)
    if file.is_file() and (not rebuild):
        return read_zone_graph(path)
    dump = peq_path(peq)
    graph = build_zone_graph(dump, quest_doors) if dump.is_file() else ZoneGraph()
    if graph.zones or graph.transits:
        write_zone_graph(graph, path)
    return graph

def _name_of(zone_id: int, zones: dict[str, int]) -> str:
    for name, found in zones.items():
        if found == zone_id:
            return name
    return ''

def _add_transit(graph: ZoneGraph, transit: Transit) -> None:
    if not transit.zone or not transit.dest:
        return
    dest_id = transit.dest_id or graph.zones.get(transit.dest) or 0
    if dest_id and transit.dest_id != dest_id:
        transit = Transit(zone=transit.zone, door_id=transit.door_id, dest=transit.dest, dest_id=dest_id, via=transit.via, name=transit.name, x=transit.x, y=transit.y, z=transit.z, heading=transit.heading, dest_x=transit.dest_x, dest_y=transit.dest_y, dest_z=transit.dest_z, dest_heading=transit.dest_heading, need=transit.need)
    key = (transit.zone, transit.door_id, transit.dest, transit.via, transit.dest_id)
    for existing in graph.transits:
        if (existing.zone, existing.door_id, existing.dest, existing.via, existing.dest_id) == key:
            return
    graph.transits.append(transit)
    graph.edges.append(transit.to_edge())
    if dest_id:
        known = graph.doors.setdefault(transit.zone, {}).setdefault(transit.door_id, [])
        if dest_id not in known:
            known.append(dest_id)

def _parse_zones(text: str) -> tuple[dict[str, int], dict[str, int]]:
    """Return (short→id, short→id for zones with numeric flag_needed)."""
    found: dict[str, int] = {}
    flagged: dict[str, int] = {}
    mode = ''
    for line in text.splitlines():
        if 'INSERT INTO `zone`' in line and 'zone_points' not in line and ('zone_flags' not in line):
            mode = 'zone'
            continue
        if line.startswith('INSERT INTO `'):
            mode = ''
            continue
        if mode != 'zone':
            continue
        for match in _ROW.finditer(line):
            parts = _split_sql_row(match.group(1))
            if len(parts) < 14:
                continue
            name = _unquote(parts[0]).lower()
            try:
                zone_id = int(parts[13])
            except ValueError:
                log.error("zone row failed to parse", exc_info=True)
                continue
            if name and zone_id > 0:
                found[name] = zone_id
                if len(parts) > 53:
                    raw = _unquote(parts[53]).strip()
                    if raw in {'1', 'true', 'True'}:
                        flagged[name] = zone_id
    return (found, flagged)

def _dest_zone_flag(dest: str, dest_id: int, flagged: dict[str, int]) -> int:
    if dest in flagged:
        return flagged[dest]
    if dest_id and dest_id in flagged.values():
        return dest_id
    return 0

def _parse_doors(text: str, zones: dict[str, int], flagged: dict[str, int] | None = None) -> list[Transit]:
    """doors columns: doorid, zone, name, pos_y/x/z, heading, lockpick, keyitem, dest_zone, dest xyz, expansions."""
    flagged = flagged or {}
    found: list[Transit] = []
    mode = ''
    for line in text.splitlines():
        if 'INSERT INTO `doors`' in line:
            mode = 'doors'
            continue
        if line.startswith('INSERT INTO `'):
            mode = ''
            continue
        if mode != 'doors':
            continue
        for match in _ROW.finditer(line):
            parts = _split_sql_row(match.group(1))
            if len(parts) < 25:
                continue
            try:
                door_id = int(parts[1])
            except ValueError:
                log.error("door row failed to parse", exc_info=True)
                continue
            zone = _unquote(parts[2]).lower()
            dest_zone = _unquote(parts[19]).lower()
            if not zone or not dest_zone or dest_zone in {'none', 'same'}:
                continue
            name = _unquote(parts[4])
            try:
                pos_y, pos_x, pos_z = (float(parts[5]), float(parts[6]), float(parts[7]))
                heading = float(parts[8])
                lockpick = int(parts[11] or 0)
                key_item = int(parts[12] or 0)
                dest_x, dest_y, dest_z = (float(parts[21]), float(parts[22]), float(parts[23]))
                dest_heading = float(parts[24])
            except ValueError:
                log.error("door coordinates failed to parse", exc_info=True)
                continue
            min_exp = max_exp = -1
            flags = flags_off = ''
            if len(parts) > 33:
                try:
                    min_exp = int(parts[32])
                    max_exp = int(parts[33])
                except ValueError:
                    log.error("door expansion flags failed to parse", exc_info=True)
            if len(parts) > 35:
                flags = _unquote(parts[34]) if parts[34].upper() != 'NULL' else ''
                flags_off = _unquote(parts[35]) if parts[35].upper() != 'NULL' else ''
            via = 'stone' if 'tele' in name.lower() or name.lower().startswith('pok') else 'door'
            dest_id = zones.get(dest_zone) or zone_id_of(dest_zone) or 0
            found.append(Transit(zone=zone, door_id=door_id, dest=dest_zone, dest_id=dest_id, via=via, name=name, x=pos_x, y=pos_y, z=pos_z, heading=heading, dest_x=dest_x, dest_y=dest_y, dest_z=dest_z, dest_heading=dest_heading, need=TransitNeed(key_item=key_item, lockpick=lockpick, min_expansion=min_exp, max_expansion=max_exp, content_flags=flags, content_flags_disabled=flags_off, zone_flag=_dest_zone_flag(dest_zone, dest_id, flagged))))
    return found

def _parse_zone_points(text: str, zones: dict[str, int], flagged: dict[str, int] | None = None) -> list[Transit]:
    flagged = flagged or {}
    found: list[Transit] = []
    mode = ''
    for line in text.splitlines():
        if 'INSERT INTO `zone_points`' in line:
            mode = 'points'
            continue
        if line.startswith('INSERT INTO `'):
            mode = ''
            continue
        if mode != 'points':
            continue
        for match in _ROW.finditer(line):
            parts = _split_sql_row(match.group(1))
            if len(parts) < 14:
                continue
            zone = _unquote(parts[1]).lower()
            try:
                number = int(parts[3])
                y, x, z = (float(parts[4]), float(parts[5]), float(parts[6]))
                heading = float(parts[7])
                dest_y, dest_x, dest_z = (float(parts[8]), float(parts[9]), float(parts[10]))
                dest_heading = float(parts[11])
                dest_id = int(parts[13])
            except ValueError:
                log.error("zone point failed to parse", exc_info=True)
                continue
            if not zone or dest_id <= 0:
                continue
            if abs(x) >= 999999 or abs(y) >= 999999:
                x = y = 0.0
            dest = _name_of(dest_id, zones) or zone_name_of(dest_id) or f'zone{dest_id}'
            min_exp = max_exp = -1
            flags = flags_off = ''
            if len(parts) > 20:
                try:
                    min_exp = int(parts[18])
                    max_exp = int(parts[19])
                except ValueError:
                    log.error("zone point expansion flags failed to parse", exc_info=True)
                if len(parts) > 21:
                    flags = _unquote(parts[20]) if parts[20].upper() != 'NULL' else ''
                    flags_off = _unquote(parts[21]) if parts[21].upper() != 'NULL' else ''
            found.append(Transit(zone=zone, door_id=number, dest=dest, dest_id=dest_id, via='point', name=f'zone_point_{number}', x=x, y=y, z=z, heading=heading, dest_x=dest_x, dest_y=dest_y, dest_z=dest_z, dest_heading=dest_heading, need=TransitNeed(min_expansion=min_exp, max_expansion=max_exp, content_flags=flags, content_flags_disabled=flags_off, zone_flag=_dest_zone_flag(dest, dest_id, flagged))))
    return found

def _rebuild(prev: dict[str, tuple[str, int, str, int]], start: str, goal: str) -> list[TravelLeg]:
    legs: list[TravelLeg] = []
    cur = goal
    while cur != start:
        parent, door_id, dest, dest_id = prev[cur]
        legs.append(TravelLeg(zone=parent, door_id=door_id, dest=dest, dest_id=dest_id))
        cur = parent
    legs.reverse()
    return legs

def _unquote(raw: str) -> str:
    text = raw.strip()
    if len(text) >= 2 and text[0] == text[-1] and (text[0] in {"'", '"'}):
        return text[1:-1]
    return text

def _split_sql_row(body: str) -> list[str]:
    parts: list[str] = []
    buf: list[str] = []
    in_str = False
    quote = ''
    i = 0
    while i < len(body):
        ch = body[i]
        if in_str:
            buf.append(ch)
            if ch == quote:
                in_str = False
            i += 1
            continue
        if ch in {"'", '"'}:
            in_str = True
            quote = ch
            buf.append(ch)
            i += 1
            continue
        if ch == ',':
            parts.append(''.join(buf).strip())
            buf = []
            i += 1
            continue
        buf.append(ch)
        i += 1
    if buf:
        parts.append(''.join(buf).strip())
    return parts
