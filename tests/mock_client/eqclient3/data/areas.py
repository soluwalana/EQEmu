"""Explore boxes from the task table, read once from the local peq dump.

An explore step has no npc. The server credits it when the player stands inside
the box, so the client walks to the center.
"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass

from eqclient3.data.cache_builders.common import lines, peq_path
from eqclient3.data.catalog import _table, _tuple

_EXPLORE = "5"


@dataclass(frozen=True)
class Box:
    task_id: int
    activity_id: int
    min_x: float
    min_y: float
    min_z: float
    max_x: float
    max_y: float
    max_z: float

    def center(self) -> tuple[float, float, float]:
        return (
            (self.min_x + self.max_x) / 2,
            (self.min_y + self.max_y) / 2,
            (self.min_z + self.max_z) / 2,
        )


_boxes: dict[tuple[int, int], Box] | None = None


def box_for(task_id: int, activity_id: int) -> Box | None:
    return _book().get((task_id, activity_id))


def _book() -> dict[tuple[int, int], Box]:
    global _boxes
    if _boxes is not None:
        return _boxes
    path = peq_path()
    if not path.is_file():
        _boxes = {}
        return _boxes
    _boxes = read_areas(lines(path))
    return _boxes


def read_areas(rows: Iterable[str]) -> dict[tuple[int, int], Box]:
    found: dict[tuple[int, int], Box] = {}
    mode = ""
    for raw in rows:
        line = raw.strip()
        if line.startswith("INSERT INTO `"):
            mode = _table(line)
            continue
        if mode != "task_activities" or not line.startswith("("):
            continue
        box = _take(line)
        if box is not None:
            found[(box.task_id, box.activity_id)] = box
    return found


def _take(line: str) -> Box | None:
    fields = _tuple(line)
    if len(fields) < 19 or fields[4] != _EXPLORE:
        return None
    if not fields[0].isdigit() or not fields[1].isdigit():
        return None
    coords = tuple(float(fields[index]) for index in range(13, 19))
    if not any(coords):
        return None
    return Box(int(fields[0]), int(fields[1]), *coords)
