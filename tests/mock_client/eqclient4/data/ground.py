"""Ground-spawn points for an item, read once from the local peq dump.

A fetch with no merchant and no loot drop walks to one of these points and
clicks the live object the server places there.
"""

import json
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from pathlib import Path

from eqclient4.data.cache_builders.common import lines, peq_path
from eqclient4.data.catalog import _table, _tuple

_NEAR = 40.0

DEFAULT_LOCATIONS = str(Path.home() / ".eqclient" / "gs_cache.jsonl")


@dataclass
class GroundSpawn:
    zone_id: int  # fields[1]
    x: float  # calculated
    y: float  # calculated

    max_x: float  # fields[3]
    max_y: float  # fields[4]
    max_z: float  # fields[5]
    min_x: float  # fields[6]
    min_y: float  # fields[7]

    item_id: int  # fields[10]
    respawn_time: int  # fields[13]


@dataclass
class LiveGroundSpawn(GroundSpawn):
    instance_id: int
    observed_x: float
    observed_y: float
    observed_z: float
    observed_time: int


class GroundSpawnBook:
    """Database of ground spawns for items in zones."""

    def __init__(self) -> None:
        self.spots: dict[int, tuple[GroundSpawn, ...]] = {}
        self.zones: dict[int, str] = {}
        self.zone_spawns: dict[int, list[GroundSpawn]] = {}

        path = peq_path()
        if not path.is_file():
            raise FileNotFoundError(f"PEQ file not found: {path}")

        if Path(DEFAULT_LOCATIONS).is_file():
            with open(DEFAULT_LOCATIONS, "r") as f:
                data = json.load(f)
                self.spots = data["spots"]
                self.zones = data["zones"]
                self.zone_spawns = data["zone_spawns"]
                return

        if not Path(DEFAULT_LOCATIONS).is_file():
            self._read_ground(lines(path))
            with open(DEFAULT_LOCATIONS, "w") as f:
                json.dump(
                    {
                        "spots": self.spots,
                        "zones": self.zones,
                        "zone_spawns": self.zone_spawns,
                    },
                    f,
                )
                return

    def _read_ground(self, rows: Iterable[str]) -> None:
        spots: dict[int, list[GroundSpawn]] = {}
        names: dict[int, str] = {}
        zone_spawns: dict[int, list[GroundSpawn]] = {}

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
                _take_ground(line, spots, zone_spawns)
        frozen = {item_id: tuple(points) for item_id, points in spots.items()}

        self.spots = frozen
        self.zones = names
        self.zone_spawns = zone_spawns

    def spawns_at_coordinates(self, x: float, y: float, z: float) -> list[GroundSpawn]:
        """Spawns at this coordinates."""
        possible = []
        for spawns in self.spots.values():
            for spawn in spawns:
                if (
                    spawn.min_x <= x <= spawn.max_x
                    and spawn.min_y <= y <= spawn.max_y
                    and spawn.max_z == z
                ):
                    possible.append(spawn)
        return possible

    def nearest_spawn(
        self,
        zone_id: int,
        point: tuple[float, float, float],
    ) -> GroundSpawn | None:
        """The unused ground object sitting on this point, or None."""
        best: GroundSpawn | None = None
        best_d = float("inf")
        for gs in self.zone_spawns.get(zone_id, []):
            dist = (gs.x - point[0]) ** 2 + (gs.y - point[1]) ** 2
            if dist < best_d:
                best = gs
                best_d = dist
        return best


_book: GroundSpawnBook | None = None


def ensure_ground_spawns() -> GroundSpawnBook:
    global _book
    if _book:
        return _book

    _book = GroundSpawnBook()
    return _book


def ground_at(item_id: int, zone_id: int, zone: str) -> tuple[tuple[float, float, float], ...]:
    """Points in this zone where the item sits on the ground. Empty when the dump has none."""
    book = ensure_ground_spawns()
    here = (zone or "").lower()
    found: list[tuple[float, float, float]] = []
    for spot in book.spots.get(item_id, ()):
        if zone_id and spot.zone_id == zone_id:
            found.append((spot.x, spot.y, spot.max_z))
            continue
        if here and book.zones.get(spot.zone_id) == here:
            found.append((spot.x, spot.y, spot.max_z))
    return tuple(found)


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


def _take_ground(
    line: str, spots: dict[int, list[GroundSpawn]], zone_spawns: dict[int, list[GroundSpawn]]
) -> None:
    fields = _tuple(line)
    if len(fields) < 14 or not fields[1].isdigit() or not fields[10].isdigit():
        print(f"Invalid ground spawn line: {line}")
        return

    zone_id = int(fields[1])

    max_x = float(fields[3])
    max_y = float(fields[4])
    max_z = float(fields[5])
    min_x = float(fields[6])
    min_y = float(fields[7])
    item_id = int(fields[10])
    respawn_time = int(fields[13])

    if item_id <= 0:
        print(f"Invalid item ID: {item_id}")
        return

    spawn = GroundSpawn(
        zone_id,
        (min_x + max_x) / 2.0,
        (min_y + max_y) / 2.0,
        min_x,
        min_y,
        max_x,
        max_y,
        max_z,
        item_id,
        respawn_time,
    )
    spots.setdefault(item_id, []).append(spawn)
    zone_spawns.setdefault(zone_id, []).append(spawn)
