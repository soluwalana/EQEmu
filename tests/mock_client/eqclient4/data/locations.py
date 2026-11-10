"""Spawn points for an item, indexed by item id.

The loader maps `item_locations.eqm` and reads one item's slice. The jsonl is
parsed only when that file is missing or older.
"""

from __future__ import annotations

import json
import mmap
import os
import struct
from array import array
from dataclasses import dataclass, field
from pathlib import Path

from eqclient4.data.mapped import (
    IdIndex,
    StringTable,
    eqm_path,
    eqm_ready,
    read_header,
    read_string,
    write_eqm,
)
from eqclient4.log import log

DEFAULT_LOCATIONS = str(Path.home() / ".eqclient" / "item_locations.jsonl")
_KIND = b"LOC\x00"
_RECORD = struct.Struct("<IHHfffIIf")


@dataclass(frozen=True)
class SpawnPoint:
    zone: str
    x: float
    y: float
    z: float
    npc_id: int
    name: str
    level: int
    chance: float

    def row(self) -> dict:
        return {
            "zone": self.zone,
            "x": self.x,
            "y": self.y,
            "z": self.z,
            "npc_id": self.npc_id,
            "name": self.name,
            "npc_level": self.level,
            "chance": self.chance,
        }


@dataclass
class LocationBook:
    """item id → the spawn points that drop it. A lookup does not scan the file."""

    by_item: dict[int, tuple[SpawnPoint, ...]] = field(default_factory=dict)

    def points(self, item_id: int) -> list[SpawnPoint]:
        return [point for point in self.by_item.get(int(item_id), ())]


class MappedLocations:
    """item id → spawn points, read from a mapped record file."""

    def __init__(self, path: Path) -> None:
        self._fh = open(path, "rb")
        try:
            self._mm = mmap.mmap(self._fh.fileno(), 0, access=mmap.ACCESS_READ)
            slots = read_header(self._mm, _KIND)
        except Exception:
            self._fh.close()
            raise
        (
            n_index,
            _n_records,
            self._n_zones,
            self._strings,
            _strings_len,
            self._zones,
            index_off,
            self._records,
        ) = slots
        self.by_item = IdIndex(self._mm, index_off, n_index)

    def _text(self, rel: int) -> str:
        return read_string(self._mm, self._strings, rel)

    def points(self, item_id: int) -> list[SpawnPoint]:
        span = self.by_item.span(int(item_id))
        if span is None:
            return []
        start, count = span
        found: list[SpawnPoint] = []
        for index in range(count):
            _item, zone_i, level, x, y, z, npc, name_off, chance = _RECORD.unpack_from(
                self._mm, self._records + (start + index) * _RECORD.size
            )
            zone = ""
            if zone_i < self._n_zones:
                rel = struct.unpack_from("<I", self._mm, self._zones + zone_i * 4)[0]
                zone = self._text(rel)
            found.append(
                SpawnPoint(
                    zone=zone,
                    x=x,
                    y=y,
                    z=z,
                    npc_id=npc,
                    name=self._text(name_off),
                    level=level,
                    chance=chance,
                )
            )
        return found


def read_locations(path: str | None = None) -> MappedLocations | LocationBook:
    """Map the `.eqm` sibling. Build it from the jsonl when it is missing or older."""
    source = Path(path or os.environ.get("EQEMU_ITEM_LOCATIONS", DEFAULT_LOCATIONS))
    mapped = eqm_path(source)
    if eqm_ready(source, mapped):
        try:
            return MappedLocations(mapped)
        except ValueError:
            log.error("location cache %s failed to open", mapped, exc_info=True)

    if not source.is_file():
        raise Exception("Failed to generate an item location cache file")

    _compile_locations(source, mapped)
    return MappedLocations(mapped)


_book: LocationBook | MappedLocations | None = None


def ensure_locations(
    path: str | None = None,
    rebuild: bool = False,
) -> LocationBook | MappedLocations:
    """Load item_locations.jsonl, or build once from the jsonl."""
    global _book
    if _book is not None:
        return _book

    path = path or os.environ.get("EQEMU_ITEM_LOCATIONS", DEFAULT_LOCATIONS)
    file = Path(path)
    if file.is_file() and not rebuild:
        _book = read_locations(path)
        return _book
    _book = read_locations(path)
    return _book


def _compile_locations(source: Path, dest: Path) -> None:
    print(f"caches: building {dest.name} from {source.name}", flush=True)
    strings = StringTable()
    zones: dict[str, int] = {}
    zone_at: list[int] = []
    raw = bytearray()
    ids = array("I")
    seen = 0
    with source.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            row = json.loads(line)
            item_id = int(row.get("item_id") or row.get("item") or 0)
            if item_id <= 0:
                continue
            zone = str(row.get("zone") or "").lower()
            zone_i = zones.get(zone)
            if zone_i is None:
                if len(zones) >= 65535:
                    raise ValueError("too many zones for the location cache")
                zone_i = len(zones)
                zones[zone] = zone_i
                zone_at.append(strings.add(zone))
            level = int(row.get("npc_level") or row.get("level") or 0)
            raw += _RECORD.pack(
                item_id,
                zone_i,
                max(0, min(65535, level)),
                float(row.get("x") or 0),
                float(row.get("y") or 0),
                float(row.get("z") or 0),
                int(row.get("npc_id") or 0),
                strings.add(str(row.get("name") or "")),
                float(row.get("chance") or 0),
            )
            ids.append(item_id)
            seen += 1
            if seen % 1000000 == 0:
                print(f"caches: {source.name} {seen} rows", flush=True)
    order = sorted(range(seen), key=ids.__getitem__)
    index = bytearray()
    records = bytearray()
    cursor = 0
    while cursor < seen:
        item_id = ids[order[cursor]]
        end = cursor + 1
        while end < seen and ids[order[end]] == item_id:
            end += 1
        index += struct.pack("<III", item_id, cursor, end - cursor)
        for slot in order[cursor:end]:
            at = slot * _RECORD.size
            records += raw[at : at + _RECORD.size]
        cursor = end
    zone_blob = b"".join(struct.pack("<I", off) for off in zone_at)
    strings_off = 64 + len(zone_blob)
    index_off = strings_off + len(strings.buf)
    records_off = index_off + len(index)
    n_index = len(index) // 12
    write_eqm(
        dest,
        _KIND,
        (
            n_index,
            seen,
            len(zone_at),
            strings_off,
            len(strings.buf),
            64,
            index_off,
            records_off,
        ),
        [zone_blob, strings.buf, index, records],
    )
    print(f"caches: {dest.name} {seen} rows, {n_index} items", flush=True)
