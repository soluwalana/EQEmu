"""Ground-spawn points for an item, read once from the local peq dump.

A fetch with no merchant and no loot drop walks to one of these points and
clicks the live object the server places there.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from dataclasses import dataclass

from eqclient4.data.cache_builders.common import lines, peq_path
from eqclient4.data.catalog import _table, _tuple
from eqclient4.world import GroundSpawn

_NEAR = 40.0


@dataclass(frozen=True)
class GroundSpot:
    zone_id: int
    x: float
    y: float
    z: float


@dataclass
class GroundSpawnBook:
    spots: dict[int, tuple[GroundSpot, ...]]
    zones: dict[int, str]


_book: GroundSpawnBook | None = None


def ensure_ground_spawns() -> GroundSpawnBook:
    global _book
    if _book:
        return _book

    path = peq_path()
    if not path.is_file():
        raise FileNotFoundError(f"PEQ file not found: {path}")

    spots, zones = read_ground(lines(path))
    _book = GroundSpawnBook(spots=spots, zones=zones)
    return _book


def ground_at(item_id: int, zone_id: int, zone: str) -> tuple[tuple[float, float, float], ...]:
    """Points in this zone where the item sits on the ground. Empty when the dump has none."""
    spots, names = _book()
    here = (zone or "").lower()
    found: list[tuple[float, float, float]] = []
    for spot in spots.get(item_id, ()):
        if zone_id and spot.zone_id == zone_id:
            found.append((spot.x, spot.y, spot.z))
            continue
        if here and names.get(spot.zone_id) == here:
            found.append((spot.x, spot.y, spot.z))
    return tuple(found)


def nearest_spawn(
    world_ground: Mapping[int, GroundSpawn],
    point: tuple[float, float, float],
) -> GroundSpawn | None:
    """The unused ground object sitting on this point, or None."""
    best: GroundSpawn | None = None
    best_d = _NEAR * _NEAR
    for row in world_ground.values():
        if row.used:
            continue
        dist = (row.x - point[0]) ** 2 + (row.y - point[1]) ** 2
        if dist < best_d:
            best = row
            best_d = dist
    return best


def read_ground(rows: Iterable[str]) -> tuple[dict[int, tuple[GroundSpot, ...]], dict[int, str]]:
    spots: dict[int, list[GroundSpot]] = {}
    names: dict[int, str] = {}
    mode = ""
    for raw in rows:
        line = raw.strip()
        if line.startswith("INSERT INTO `"):
            mode = _table(line)
            continue
        if not line.startswith("("):
            continue
        if mode == "zone":
            _take_zone(line, names)
        elif mode == "ground_spawns":
            _take_ground(line, spots)
    frozen = {item_id: tuple(points) for item_id, points in spots.items()}
    return frozen, names


def _take_zone(line: str, names: dict[int, str]) -> None:
    fields = _tuple(line)
    if len(fields) < 14 or not fields[0]:
        return
    short = fields[0].lower()
    if fields[1].isdigit():
        names[int(fields[1])] = short
    number = fields[13].lstrip("-")
    if number.isdigit():
        names[int(fields[13])] = short


def _take_ground(line: str, spots: dict[int, list[GroundSpot]]) -> None:
    fields = _tuple(line)
    if len(fields) < 11 or not fields[1].isdigit() or not fields[10].isdigit():
        return
    item_id = int(fields[10])
    if item_id <= 0:
        return
    max_x, max_y, max_z = _float(fields[3]), _float(fields[4]), _float(fields[5])
    min_x, min_y = _float(fields[6]), _float(fields[7])
    spots.setdefault(item_id, []).append(
        GroundSpot(
            int(fields[1]),
            (min_x + max_x) / 2.0,
            (min_y + max_y) / 2.0,
            max_z,
        )
    )


def _float(text: str) -> float:
    try:
        return float(text)
    except ValueError:
        return 0.0
