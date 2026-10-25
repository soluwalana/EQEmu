"""Walk maps/nav/<zone>.nav. Coordinates in the file are Detour (x, z, y); EQ is (x, y, z)."""

from __future__ import annotations

import heapq
import math
import os
import struct
import zlib
from dataclasses import dataclass, field
from pathlib import Path

from eqclient.opcodes import repo_root

_HEADER = 100
_POLY = 32


def maps_root() -> Path | None:
    raw = os.environ.get("EQEMU_MAPS", "")
    candidates = []
    if raw:
        candidates.append(Path(raw))
    candidates.append(repo_root() / "maps")
    candidates.append(repo_root().parent / "maps")
    for path in candidates:
        if path.is_dir():
            return path
    return None


@dataclass
class _Poly:
    tile: int
    index: int
    center: tuple[float, float, float]
    verts: list[tuple[float, float, float]]
    neighbors: list[tuple[int, int]] = field(default_factory=list)


@dataclass
class NavMesh:
    zone: str
    version: int
    polys: list[_Poly]
    visited: set[tuple[int, int]] = field(default_factory=set)

    def nearest(self, point: tuple[float, float, float]) -> _Poly | None:
        inside = [poly for poly in self.polys if _contains(poly, point[0], point[1])]
        if inside:
            return min(inside, key=lambda poly: abs(poly.center[2] - point[2]))
        if not self.polys:
            return None
        return min(self.polys, key=lambda poly: _horiz(poly.center, point) + abs(poly.center[2] - point[2]) * 0.01)

    def path(self, start: tuple[float, float, float], goal: tuple[float, float, float]) -> list[tuple[float, float, float]]:
        begin = self.nearest(start)
        end = self.nearest(goal)
        if begin is None or end is None:
            return [start, goal]
        self.visited.add((begin.tile, begin.index))
        if (begin.tile, begin.index) == (end.tile, end.index):
            return [start, goal]
        chain = _astar(self.polys, begin, end)
        if len(chain) < 2:
            return [start, goal]
        return [poly.center for poly in chain]

    def unvisited(self, start: tuple[float, float, float]) -> tuple[float, float, float] | None:
        begin = self.nearest(start)
        if begin is None:
            return None
        self.visited.add((begin.tile, begin.index))
        fresh = [poly for poly in self.polys if (poly.tile, poly.index) not in self.visited]
        if not fresh:
            return None
        return min(fresh, key=lambda poly: _horiz(poly.center, start)).center


def load_nav(zone: str, root: Path | None = None) -> NavMesh | None:
    base = root or maps_root()
    if base is None or not zone:
        return None
    path = base / "nav" / f"{zone}.nav"
    if not path.is_file():
        return None
    blob = path.read_bytes()
    if blob[:9] != b"EQNAVMESH":
        raise ValueError(f"{path} is not an EQNAVMESH")
    version = struct.unpack_from("<I", blob, 9)[0]
    if version != 2:
        raise ValueError(f"{path} nav version {version}")
    data_size, buffer_size = struct.unpack_from("<II", blob, 13)
    inflated = zlib.decompress(blob[21 : 21 + data_size])
    if len(inflated) != buffer_size and buffer_size:
        inflated = inflated[:buffer_size]
    polys, portals = _tiles(inflated)
    _link_portals(polys, portals)
    return NavMesh(zone, version, polys)


def _tiles(buf: bytes) -> tuple[list[_Poly], list[tuple[tuple[int, int], tuple[float, float, float]]]]:
    if len(buf) < 32:
        return [], []
    count = struct.unpack_from("<I", buf)[0]
    offset = 4 + 28  # tile count, then dtNavMeshParams
    polys: list[_Poly] = []
    portals: list[tuple[tuple[int, int], tuple[float, float, float]]] = []
    for tile_index in range(count):
        if offset + 8 > len(buf):
            break
        _tile_ref, size = struct.unpack_from("<II", buf, offset)
        offset += 8
        tile = buf[offset : offset + size]
        offset += size
        tile_polys, tile_portals = _tile_polys(tile_index, tile)
        polys.extend(tile_polys)
        portals.extend(tile_portals)
    return polys, portals


def _tile_polys(
    tile_index: int, tile: bytes
) -> tuple[list[_Poly], list[tuple[tuple[int, int], tuple[float, float, float]]]]:
    if len(tile) < _HEADER:
        return [], []
    magic, version, _x, _y, _layer, _user, poly_count, vert_count = struct.unpack_from("<8i", tile)
    if magic != 0x444E4156 or version != 7 or poly_count <= 0 or vert_count <= 0:
        return [], []
    vert_at = _HEADER
    poly_at = vert_at + vert_count * 12
    if poly_at + poly_count * _POLY > len(tile):
        return [], []
    verts = []
    for index in range(vert_count):
        dx, dy, dz = struct.unpack_from("<fff", tile, vert_at + index * 12)
        verts.append((dx, dz, dy))  # detour (x, up, z) -> EQ (x, y, z)
    found: list[_Poly] = []
    raw_neis: list[list[int]] = []
    portals: list[tuple[tuple[int, int], tuple[float, float, float]]] = []
    for index in range(poly_count):
        start = poly_at + index * _POLY
        # firstLink uint32, 6 verts, 6 neis, flags, vertCount, area
        values = struct.unpack_from("<I6H6HHBB", tile, start)
        indexes = values[1:7]
        neis = values[7:13]
        vert_count = values[14]
        area_type = values[15]
        if area_type >> 6:
            raw_neis.append([])
            found.append(_Poly(tile_index, index, (0.0, 0.0, 0.0), []))
            continue
        poly_verts = [verts[indexes[i]] for i in range(min(vert_count, 6)) if indexes[i] < len(verts)]
        if not poly_verts:
            raw_neis.append([])
            found.append(_Poly(tile_index, index, (0.0, 0.0, 0.0), []))
            continue
        center = (
            sum(point[0] for point in poly_verts) / len(poly_verts),
            sum(point[1] for point in poly_verts) / len(poly_verts),
            sum(point[2] for point in poly_verts) / len(poly_verts),
        )
        found.append(_Poly(tile_index, index, center, poly_verts))
        edge_neis = list(neis[:vert_count])
        raw_neis.append(edge_neis)
        for edge, nei in enumerate(edge_neis):
            if not nei & 0x8000 or edge + 1 > len(poly_verts):
                continue
            a = poly_verts[edge]
            b = poly_verts[(edge + 1) % len(poly_verts)]
            mid = ((a[0] + b[0]) * 0.5, (a[1] + b[1]) * 0.5, (a[2] + b[2]) * 0.5)
            portals.append(((tile_index, index), mid))
    by_index = {poly.index: poly for poly in found}
    for poly, neis in zip(found, raw_neis):
        for nei in neis:
            if not nei or nei & 0x8000:
                continue
            other = by_index.get(nei - 1)
            if other is not None and other.verts:
                poly.neighbors.append((other.tile, other.index))
    kept = [poly for poly in found if poly.verts]
    kept_ids = {(poly.tile, poly.index) for poly in kept}
    return kept, [portal for portal in portals if portal[0] in kept_ids]


def _link_portals(polys: list[_Poly], portals: list[tuple[tuple[int, int], tuple[float, float, float]]]) -> None:
    """External edges that share a midpoint connect one tile to the next."""
    buckets: dict[tuple[int, int, int], list[tuple[int, int]]] = {}
    for poly_id, mid in portals:
        key = (round(mid[0]), round(mid[1]), round(mid[2]))
        buckets.setdefault(key, []).append(poly_id)
    lookup = {(poly.tile, poly.index): poly for poly in polys}
    for group in buckets.values():
        unique = list(dict.fromkeys(group))
        for left in unique:
            poly = lookup.get(left)
            if poly is None:
                continue
            for right in unique:
                if right != left and right not in poly.neighbors:
                    poly.neighbors.append(right)


def _astar(polys: list[_Poly], start: _Poly, goal: _Poly) -> list[_Poly]:
    lookup = {(poly.tile, poly.index): poly for poly in polys}
    goal_id = (goal.tile, goal.index)
    start_id = (start.tile, start.index)
    open_heap = [(0.0, start_id)]
    came: dict[tuple[int, int], tuple[int, int] | None] = {start_id: None}
    cost = {start_id: 0.0}
    while open_heap:
        _score, current = heapq.heappop(open_heap)
        if current == goal_id:
            chain = []
            while current is not None:
                chain.append(lookup[current])
                current = came[current]
            chain.reverse()
            return chain
        poly = lookup[current]
        for neighbor in poly.neighbors:
            other = lookup.get(neighbor)
            if other is None:
                continue
            step = cost[current] + _horiz(poly.center, other.center)
            if step < cost.get(neighbor, 1e18):
                cost[neighbor] = step
                came[neighbor] = current
                heapq.heappush(open_heap, (step + _horiz(other.center, goal.center), neighbor))
    return [start]


def _contains(poly: _Poly, x: float, y: float) -> bool:
    inside = False
    points = poly.verts
    count = len(points)
    j = count - 1
    for i in range(count):
        yi, yj = points[i][1], points[j][1]
        xi, xj = points[i][0], points[j][0]
        if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi + 1e-12) + xi):
            inside = not inside
        j = i
    return inside


def _horiz(a: tuple[float, float, float], b: tuple[float, float, float]) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])
