"""Line of sight against maps/base/<zone>.map. A missing file means the shot is clear."""

from __future__ import annotations

import math
import struct
import zlib
from collections.abc import Callable
from dataclasses import dataclass, field

from eqclient4.nav.navmesh import maps_root

# zone/aggro.cpp: CheckLosFN; zone/common.h: HEAD_POSITION, SEE_POSITION.
_DEFAULT_SIZE = 6.0
_HEAD_POSITION = 0.9
_SEE_POSITION = 0.5


_CELL = 32.0
Triangle = tuple[tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]
Point = tuple[float, float, float]


_RAY_CACHE = 4096


@dataclass
class ZoneMap:
    triangles: list[Triangle]
    _grid: dict[tuple[int, int], list[int]] = field(default_factory=dict)
    _wide: list[int] = field(default_factory=list)
    _indexed: bool = False
    _rays: dict[tuple[Point, Point], bool] = field(default_factory=dict)

    def clear(
        self,
        start: Point,
        end: Point,
        watcher_size: float = _DEFAULT_SIZE,
        target_size: float = _DEFAULT_SIZE,
    ) -> bool:
        """Server CheckLosFN: one exact ray from the watcher's head to the target."""
        origin = (
            start[0], start[1], start[2] + (watcher_size or _DEFAULT_SIZE) / 2 * _HEAD_POSITION
        )
        target = (
            end[0], end[1], end[2] + (target_size or _DEFAULT_SIZE) / 2 * _SEE_POSITION
        )
        # Cache the actual elevated endpoints, not 8-yard cells. Adjacent
        # positions (or differently sized entities) may be on opposite sides
        # of the same wall.
        key = (origin, target)
        found = self._rays.get(key)
        if found is not None:
            return found
        result = self._ray_clear(origin, target)
        if len(self._rays) >= _RAY_CACHE:
            self._rays.clear()
        self._rays[key] = result
        return result

    def ground(self, point: Point, max_delta: float | None = None) -> float | None:
        """Collision surface at XY, optionally bounded around a planned elevation.

        Without a bound, preserve the existing ground lookup for other callers.
        Navigation supplies the intended route Z and a narrow tolerance; a
        distant floor or ceiling in a stacked room is not a valid correction.
        """
        if max_delta is not None:
            closest = None
            for triangle in self._candidates(point):
                height = _surface_z(triangle, point)
                if height is None or abs(height - point[2]) > max_delta:
                    continue
                if closest is None or (abs(height - point[2]), height) < (
                    abs(closest - point[2]),
                    closest,
                ):
                    closest = height
            return closest
        below = None
        above = None
        limit = point[2] + 2.0
        for triangle in self._candidates(point):
            height = _surface_z(triangle, point)
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

    def _ray_clear(self, origin: Point, target: Point) -> bool:
        """True when the finite, normalized server ray has no triangle hit."""
        distance = math.dist(origin, target)
        # raycast_mesh.cpp's segment/AABB test skips zero-length/tiny rays.
        if distance <= 1e-5:
            return True
        direction = (
            (target[0] - origin[0]) / distance,
            (target[1] - origin[1]) / distance,
            (target[2] - origin[2]) / distance,
        )
        self._ensure_grid()
        seen: set[int] = set()
        for index in self._wide:
            if _hits(origin, direction, distance, self.triangles[index]):
                return False
        for key in _cells_crossed(origin, target):
            for index in self._grid.get(key, ()):
                if index in seen:
                    continue
                seen.add(index)
                if _hits(origin, direction, distance, self.triangles[index]):
                    return False
        return True

    def _candidates(self, point: Point) -> list[Triangle]:
        self._ensure_grid()
        cx = math.floor(point[0] / _CELL)
        cy = math.floor(point[1] / _CELL)
        found: list[Triangle] = [self.triangles[index] for index in self._wide]
        for ix in (cx - 1, cx, cx + 1):
            for iy in (cy - 1, cy, cy + 1):
                for index in self._grid.get((ix, iy), ()):
                    found.append(self.triangles[index])
        return found

    def _ensure_grid(self) -> None:
        if self._indexed:
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
        self._indexed = True


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
    if len(data) < 4:
        return None
    version = struct.unpack_from("<I", data)[0]
    if version == 0x01000000:
        # Map::LoadV1 reads the face list; the legacy quadtree is not used.
        if len(data) < 14:
            return None
        count, _, _ = struct.unpack_from("<IHI", data, 4)
        if len(data) < 14 + count * 52:
            raise ValueError(f"Truncated V1 map: {path}")
        triangles: list[Triangle] = []
        for offset in range(14, 14 + count * 52, 52):
            ax, ay, az, bx, by, bz, cx, cy, cz = struct.unpack_from("<9f", data, offset)
            triangles.append(((ax, ay, az), (bx, by, bz), (cx, cy, cz)))
        return ZoneMap(triangles)
    if version != 0x02000000 or len(data) < 12:
        return None
    data_size, buffer_size = struct.unpack_from("<II", data, 4)
    if len(data) < 12 + data_size:
        raise ValueError(f"Truncated V2 map: {path}")
    inflated = zlib.decompress(data[12 : 12 + data_size])
    if len(inflated) != buffer_size or len(inflated) < 40:
        raise ValueError(f"Invalid V2 map buffer: {path}")
    return ZoneMap(_triangles(inflated))


def _rotate(point: Point, rx: float, ry: float, rz: float) -> Point:
    """Map::RotateVertex, in X/Y/Z order. Angles are radians."""
    x, y, z = point
    if rx:
        c, s = math.cos(rx), math.sin(rx)
        y, z = c * y - s * z, s * y + c * z
    if ry:
        c, s = math.cos(ry), math.sin(ry)
        x, z = c * x + s * z, -s * x + c * z
    if rz:
        c, s = math.cos(rz), math.sin(rz)
        x, y = c * x - s * y, s * x + c * y
    return x, y, z


def _scale(point: Point, scale: Point) -> Point:
    return point[0] * scale[0], point[1] * scale[1], point[2] * scale[2]


def _translate(point: Point, offset: Point) -> Point:
    return point[0] + offset[0], point[1] + offset[1], point[2] + offset[2]


def _triangles(buf: bytes) -> list[Triangle]:
    """Match zone/map.cpp Map::LoadV2, including models and terrain.

    Base mesh and terrain are already in EQ coordinates; model placements
    alone swap X/Y after their transforms, just as on the server.
    """
    (
        vert_count, ind_count, nc_vert_count, nc_ind_count, model_count,
        plac_count, group_count, tile_count, quads, unit,
    ) = struct.unpack_from("<9If", buf)
    offset = 40

    def read(fmt: str) -> tuple:
        nonlocal offset
        result = struct.unpack_from(fmt, buf, offset)
        offset += struct.calcsize(fmt)
        return result

    def name() -> bytes:
        nonlocal offset
        end = buf.index(b"\0", offset)
        value = buf[offset:end]
        offset = end + 1
        return value

    def vertices(count: int) -> list[Point]:
        nonlocal offset
        end = offset + 12 * count
        if end > len(buf):
            raise ValueError("Truncated map vertices")
        result = [(x, y, z) for x, y, z in struct.iter_unpack("<fff", memoryview(buf)[offset:end])]
        offset = end
        return result

    def faces(verts: list[Point], indices: tuple[int, ...]) -> list[Triangle]:
        if len(indices) % 3:
            raise ValueError("Invalid map triangle indices")
        try:
            return [
                (verts[indices[i]], verts[indices[i + 1]], verts[indices[i + 2]])
                for i in range(0, len(indices), 3)
            ]
        except IndexError as exc:
            raise ValueError("Map triangle references a missing vertex") from exc

    verts = vertices(vert_count)
    indices = read(f"<{ind_count}I")
    triangles = faces(verts, indices)
    # Non-collidable base geometry is not added to the server raycast mesh.
    offset += nc_vert_count * 12 + nc_ind_count * 4
    if offset > len(buf):
        raise ValueError("Truncated non-collidable map geometry")

    models: dict[bytes, tuple[list[Point], list[tuple[int, int, int]]]] = {}
    for _ in range(model_count):
        model_name = name()
        vc, pc = read("<II")
        model_verts = vertices(vc)
        polys = []
        for _ in range(pc):
            a, b, c, visible = read("<IIIB")
            if visible:
                polys.append((a, b, c))
        models[model_name] = model_verts, polys

    def append_model(model_name: bytes, transform: Callable[[Point], Point]) -> None:
        model = models.get(model_name)
        if model is None:
            return
        model_verts, polys = model
        transformed = []
        for vertex in model_verts:
            x, y, z = transform(vertex)
            transformed.append((y, x, z))
        try:
            triangles.extend((transformed[a], transformed[b], transformed[c]) for a, b, c in polys)
        except IndexError as exc:
            raise ValueError("Map model references a missing vertex") from exc

    for _ in range(plac_count):
        model_name = name()
        position = read("<fff")
        rotation = read("<fff")  # individual placements already use radians
        scale = read("<fff")
        append_model(
            model_name, lambda v: _translate(_scale(_rotate(v, *rotation), scale), position)
        )

    # Grouped model rotations are stored in degrees. The order and signs here
    # deliberately follow LoadV2, rather than a conventional Euler transform.
    radians = 3.14159 / 180.0
    for _ in range(group_count):
        position = read("<fff")
        gx, gy, gz = read("<fff")
        gx, gy, gz = gx * radians, gy * radians, gz * radians
        scale = read("<fff")
        tile = read("<fff")
        (count,) = read("<I")
        for _ in range(count):
            model_name = name()
            local_pos = read("<fff")
            rx, ry, rz = read("<fff")
            rx, ry, rz = rx * radians, ry * radians, rz * radians
            local_scale = read("<fff")
            correction = _rotate(local_pos, gx, 0, 0)
            negative = (-correction[0], -correction[1], -correction[2])

            def transform(v: Point) -> Point:
                v = _translate(_scale(v, local_scale), local_pos)
                v = _rotate(v, gx, gy, 0)
                v = _translate(v, negative)
                v = _rotate(v, rx, -ry, rz)
                v = _translate(v, correction)
                v = _rotate(v, 0, 0, gz)
                v = _scale(v, scale)
                return _translate(_translate(v, tile), position)

            append_model(model_name, transform)

    for _ in range(tile_count):
        flat, x, y = read("<Bff")
        if flat:
            (z,) = read("<f")
            span = quads * unit
            a, b = (x, y, z), (x + span, y, z)
            c, d = (x + span, y + span, z), (x, y + span, z)
            triangles.extend(((d, b, c), (d, a, b)))
            continue
        flags = read(f"<{quads * quads}B")
        heights = read(f"<{(quads + 1) ** 2}f")
        for quad, flag in enumerate(flags):
            if flag & 1:  # terrain hole, no collision
                continue
            row, col = divmod(quad, quads)
            i = quad + row
            ax, ay = x + row * unit, y + col * unit
            a = (ax, ay, heights[i])
            b = (ax + unit, ay, heights[i + quads + 1])
            c = (ax + unit, ay + unit, heights[i + quads + 2])
            d = (ax, ay + unit, heights[i + 1])
            triangles.extend(((d, b, c), (d, a, b)))
    return triangles


def _cells_crossed(start: Point, end: Point) -> list[tuple[int, int]]:
    """Grid cells the segment passes through."""
    x0, y0 = start[0], start[1]
    x1, y1 = end[0], end[1]
    cell = _CELL
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
    while cx != ex or cy != ey:
        # Include both side cells at a corner; a face touching exactly that
        # corner can be indexed in either one. Do not step an axis past its end.
        tx = t_max_x if cx != ex else math.inf
        ty = t_max_y if cy != ey else math.inf
        if math.isclose(tx, ty, rel_tol=0.0, abs_tol=1e-12):
            cells.extend(((cx + step_x, cy), (cx, cy + step_y)))
            cx += step_x
            cy += step_y
            t_max_x += t_dx
            t_max_y += t_dy
        elif tx < ty:
            cx += step_x
            t_max_x += t_dx
        else:
            cy += step_y
            t_max_y += t_dy
        cells.append((cx, cy))
    return cells


def _hits(start: Point, direction: Point, distance: float, triangle: Triangle) -> bool:
    """Möller–Trumbore with the server's normalized ray and determinant epsilon."""
    (ax, ay, az), (bx, by, bz), (cx, cy, cz) = triangle
    edge1 = (bx - ax, by - ay, bz - az)
    edge2 = (cx - ax, cy - ay, cz - az)
    p = _cross(direction, edge2)
    det = _dot(edge1, p)
    if abs(det) < 1e-5:
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
    return 0.0 < t <= distance


def _surface_z(triangle: Triangle, point: Point) -> float | None:
    """Height of the face at this XY, or None when the point is outside it."""
    x, y = point[0], point[1]
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


def _dot(a: Point, b: Point) -> float:
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def _cross(a: Point, b: Point) -> Point:
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )
