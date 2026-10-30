"""Line of sight against maps/base/<zone>.map. A missing file means the shot is clear."""

from __future__ import annotations

import math
import struct
import zlib
from dataclasses import dataclass

from eqclient3.nav.navmesh import maps_root

_EYE = 2.7  # (default size 6 / 2) * 0.9, where this character looks from
_SEE = 1.5  # (default size 6 / 2) * 0.5, where the other character is seen
_PEEK = 1.5  # yards offset when sampling alternate headings
_LOS_HEADINGS = 8  # compass peeks around watcher and target


_CELL = 32.0

@dataclass
class ZoneMap:
    triangles: list[tuple[tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]]
    _grid: dict[tuple[int, int], list[int]] | None = None
    _wide: list[int] | None = None

    def clear(
        self,
        start: tuple[float, float, float],
        end: tuple[float, float, float],
        *,
        headings: int = _LOS_HEADINGS,
        peek: float = _PEEK,
    ) -> bool:
        """True when any sampled eye-to-target ray is unblocked.

        Direct center-to-center first; if that clips geometry, try evenly spaced
        heading offsets around the watcher and around the target so a thin wall
        or corner does not hide an otherwise visible NPC.
        """
        if self._ray_clear(start, end):
            return True
        n = max(1, int(headings))
        if n <= 1 or peek <= 0:
            return False
        for i in range(n):
            angle = (2.0 * math.pi * i) / n
            dx = math.cos(angle) * peek
            dy = math.sin(angle) * peek
            if self._ray_clear((start[0] + dx, start[1] + dy, start[2]), end):
                return True
            if self._ray_clear(start, (end[0] + dx, end[1] + dy, end[2])):
                return True
        return False

    def ground(self, x: float, y: float, z: float) -> float | None:
        """Walkable surface at this XY.

        The highest face at or just above ``z``. A point under the floor takes
        the next face above it. A ceiling far overhead is not the floor.
        """
        below = None
        above = None
        limit = z + 2.0
        for triangle in self._candidates(x, y):
            height = _surface_z(triangle, x, y)
            if height is None:
                continue
            if height <= limit:
                if below is None or height > below:
                    below = height
            elif above is None or height < above:
                above = height
        if below is not None:
            return below
        return above

    def _ray_clear(self, start: tuple[float, float, float], end: tuple[float, float, float]) -> bool:
        """True when no collidable triangle sits between the two eye points."""
        origin = (start[0], start[1], start[2] + _EYE)
        target = (end[0], end[1], end[2] + _SEE)
        self._ensure_grid()
        seen: set[int] = set()
        for index in self._wide or []:
            if _hits(origin, target, self.triangles[index]):
                return False
        for key in _cells_crossed(origin[0], origin[1], target[0], target[1], _CELL):
            for index in self._grid.get(key, ()):
                if index in seen:
                    continue
                seen.add(index)
                if _hits(origin, target, self.triangles[index]):
                    return False
        return True

    def _candidates(self, x: float, y: float) -> list:
        self._ensure_grid()
        cx = math.floor(x / _CELL)
        cy = math.floor(y / _CELL)
        found = [self.triangles[index] for index in self._wide]
        for ix in (cx - 1, cx, cx + 1):
            for iy in (cy - 1, cy, cy + 1):
                for index in self._grid.get((ix, iy), ()):
                    found.append(self.triangles[index])
        return found

    def _ensure_grid(self) -> None:
        if self._grid is not None:
            return
        grid: dict[tuple[int, int], list[int]] = {}
        wide: list[int] = []
        span = _CELL * 4.0
        for index, triangle in enumerate(self.triangles):
            xs = (triangle[0][0], triangle[1][0], triangle[2][0])
            ys = (triangle[0][1], triangle[1][1], triangle[2][1])
            minx, maxx = min(xs), max(xs)
            miny, maxy = min(ys), max(ys)
            if maxx - minx > span or maxy - miny > span:
                wide.append(index)
                continue
            x0 = math.floor(minx / _CELL)
            x1 = math.floor(maxx / _CELL)
            y0 = math.floor(miny / _CELL)
            y1 = math.floor(maxy / _CELL)
            for ix in range(x0, x1 + 1):
                for iy in range(y0, y1 + 1):
                    grid.setdefault((ix, iy), []).append(index)
        self._grid = grid
        self._wide = wide


_LOADED: dict[str, ZoneMap | None] = {}

def load_map(zone: str) -> ZoneMap | None:
    key = (zone or "").lower()
    if key in _LOADED:
        return _LOADED[key]
    zone_map = _read_map(key)
    _LOADED[key] = zone_map
    return zone_map

def _read_map(zone: str) -> ZoneMap | None:
    root = maps_root()
    if root is None or not zone:
        return None
    path = root / "base" / f"{zone}.map"
    if not path.is_file():
        return None
    data = path.read_bytes()
    if len(data) < 16:
        return None
    version = struct.unpack_from("<I", data)[0]
    if version != 0x02000000:
        return None
    data_size, _buffer_size = struct.unpack_from("<II", data, 4)
    inflated = zlib.decompress(data[12 : 12 + data_size])
    if len(inflated) < 40:
        return None
    return ZoneMap(_triangles(inflated))


def _triangles(buf: bytes) -> list[object]:
    counts = struct.unpack_from("<9I", buf)
    vert_count, ind_count = counts[0], counts[1]
    offset = 36 + 4  # nine uint32 counts and the units-per-vertex float
    verts = []
    for _ in range(vert_count):
        verts.append(struct.unpack_from("<fff", buf, offset))
        offset += 12
    indices = []
    for _ in range(ind_count):
        indices.append(struct.unpack_from("<I", buf, offset)[0])
        offset += 4
    triangles = []
    for index in range(0, len(indices) - 2, 3):
        a, b, c = indices[index], indices[index + 1], indices[index + 2]
        if a >= len(verts) or b >= len(verts) or c >= len(verts):
            continue
        triangles.append((verts[a], verts[b], verts[c]))
    return triangles


def _cells_crossed(x0: float, y0: float, x1: float, y1: float, cell: float) -> list[tuple[int, int]]:
    """Grid cells the segment passes through."""
    cx = math.floor(x0 / cell)
    cy = math.floor(y0 / cell)
    ex = math.floor(x1 / cell)
    ey = math.floor(y1 / cell)
    cells = [(cx, cy)]
    if cx == ex and cy == ey:
        return cells
    dx = x1 - x0
    dy = y1 - y0
    step_x = 1 if dx >= 0.0 else -1
    step_y = 1 if dy >= 0.0 else -1
    if dx == 0.0:
        t_max_x = math.inf
        t_dx = math.inf
    else:
        edge = (math.floor(x0 / cell) + (1 if step_x > 0 else 0)) * cell
        t_max_x = (edge - x0) / dx
        t_dx = abs(cell / dx)
    if dy == 0.0:
        t_max_y = math.inf
        t_dy = math.inf
    else:
        edge = (math.floor(y0 / cell) + (1 if step_y > 0 else 0)) * cell
        t_max_y = (edge - y0) / dy
        t_dy = abs(cell / dy)
    for _ in range(4096):
        if t_max_x < t_max_y:
            cx += step_x
            t_max_x += t_dx
        else:
            cy += step_y
            t_max_y += t_dy
        cells.append((cx, cy))
        if cx == ex and cy == ey:
            break
    return cells


def _hits(start: tuple[float, float, float], end: tuple[float, float, float], triangle: tuple[tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]) -> bool:
    """Möller–Trumbore. A hit between the eyes blocks the shot."""
    (ax, ay, az), (bx, by, bz), (cx, cy, cz) = triangle
    edge1 = (bx - ax, by - ay, bz - az)
    edge2 = (cx - ax, cy - ay, cz - az)
    direction = (end[0] - start[0], end[1] - start[1], end[2] - start[2])
    p = _cross(direction, edge2)
    det = _dot(edge1, p)
    if abs(det) < 1e-8:
        return False
    inverse = 1.0 / det
    tvec = (start[0] - ax, start[1] - ay, start[2] - az)
    u = _dot(tvec, p) * inverse
    if u < 0.0 or u > 1.0:
        return False
    q = _cross(tvec, edge1)
    v = _dot(direction, q) * inverse
    if v < 0.0 or u + v > 1.0:
        return False
    t = _dot(edge2, q) * inverse
    return 0.02 < t < 0.98


def _surface_z(triangle: tuple[tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]], x: float, y: float) -> float | None:
    """Height of the face at this XY, or None when the point is outside it."""
    (ax, ay, az), (bx, by, bz), (cx, cy, cz) = triangle
    den = (by - cy) * (ax - cx) + (cx - bx) * (ay - cy)
    if abs(den) < 1e-8:
        return None
    w1 = ((by - cy) * (x - cx) + (cx - bx) * (y - cy)) / den
    w2 = ((cy - ay) * (x - cx) + (ax - cx) * (y - cy)) / den
    w3 = 1.0 - w1 - w2
    if w1 < -1e-3 or w2 < -1e-3 or w3 < -1e-3:
        return None
    return w1 * az + w2 * bz + w3 * cz


def _dot(a: tuple[float, float, float], b: tuple[float, float, float]) -> float:
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def _cross(a: tuple[float, float, float], b: tuple[float, float, float]) -> tuple[float, float, float]:
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )
