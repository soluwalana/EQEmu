"""Walk maps/nav/<zone>.nav. Coordinates in the file are Detour (x, z, y); EQ is (x, y, z)."""
from __future__ import annotations
import heapq
import math
import os
import struct
import zlib
from dataclasses import dataclass, field
from pathlib import Path
from eqclient3.nav.explore import cell_of
_HEADER = 100
_POLY = 32
_SURFACE = 40.0

def _repo_root() -> Path:
    """EQEmu checkout. navmesh.py lives in tests/mock_client/eqclient3/nav/."""
    return Path(__file__).resolve().parents[4]

def maps_root() -> Path | None:
    raw = os.environ.get('EQEMU_MAPS', '')
    candidates = []
    if raw:
        candidates.append(Path(raw))
    root = _repo_root()
    candidates.append(root / 'maps')
    candidates.append(root.parent / 'maps')
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
    _components: list[set[tuple[int, int]]] | None = None
    _owner: dict[tuple[int, int], set[tuple[int, int]]] | None = None
    _by_id: dict[tuple[int, int], _Poly] | None = None

    def nearest(self, point: tuple[float, float, float]) -> _Poly | None:
        inside = [poly for poly in self.polys if _contains(poly, point[0], point[1])]
        if inside:
            return min(inside, key=lambda poly: abs(poly.center[2] - point[2]))
        if not self.polys:
            return None
        return min(self.polys, key=lambda poly: _horiz(poly.center, point) + abs(poly.center[2] - point[2]) * 0.01)

    def path(self, start: tuple[float, float, float], goal: tuple[float, float, float], avoid: set[tuple[int, int]] | None = None) -> list[tuple[float, float, float]]:
        begin, end = self._ends(start, goal)
        if begin is None or end is None:
            return [start, goal]
        self.visited.add((begin.tile, begin.index))
        if (begin.tile, begin.index) == (end.tile, end.index):
            return [start, goal]
        chain = _astar(self.polys, begin, end, avoid) if avoid else []
        if not _reaches(chain, end):
            chain = _astar(self.polys, begin, end)
        if not _reaches(chain, end):
            return [start, goal]
        return [poly.center for poly in chain]

    def reaches(self, start: tuple[float, float, float], goal: tuple[float, float, float]) -> bool:
        """True when a polygon chain reaches the goal polygon.

        ``path`` returns ``[start, goal]`` both for a shared polygon and when
        A* has no route. Only the shared polygon, or a real chain, is success.
        The two-point list from a failed search does not count.
        """
        begin, end = self._ends(start, goal)
        if begin is None or end is None:
            return False
        if (begin.tile, begin.index) == (end.tile, end.index):
            return True
        return _reaches(_astar(self.polys, begin, end), end)

    def _ends(self, start: tuple[float, float, float], goal: tuple[float, float, float]) -> tuple[_Poly | None, _Poly | None]:
        """Polygons to search. A zone point on a disconnected pocket is walked
        from the nearest polygon on the connected surface, within ``_SURFACE``.

        That projection is a real polygon chain. It is not the two-point fallback.
        """
        begin = self.nearest(start)
        end = self.nearest(goal)
        if begin is None or end is None or self._joined(begin, end):
            return (begin, end)
        surface = self._surface()
        if not surface:
            return (begin, end)
        onto_start = self._closest(start, surface)
        onto_goal = self._closest(goal, surface)
        if onto_start is None or onto_goal is None:
            return (begin, end)
        if _horiz(onto_start.center, start) > _SURFACE or _horiz(onto_goal.center, goal) > _SURFACE:
            return (begin, end)
        return (onto_start, onto_goal)

    def _parts(self) -> list[set[tuple[int, int]]]:
        cached = self._components
        if cached is not None:
            return cached
        lookup = self._index()
        seen: set[tuple[int, int]] = set()
        parts: list[set[tuple[int, int]]] = []
        owner: dict[tuple[int, int], set[tuple[int, int]]] = {}
        for poly in self.polys:
            pid = (poly.tile, poly.index)
            if pid in seen:
                continue
            group: set[tuple[int, int]] = set()
            stack = [pid]
            while stack:
                cur = stack.pop()
                if cur in group or cur not in lookup:
                    continue
                group.add(cur)
                seen.add(cur)
                stack.extend(lookup[cur].neighbors)
            parts.append(group)
            for item in group:
                owner[item] = group
        parts.sort(key=len, reverse=True)
        self._components = parts
        self._owner = owner
        return parts

    def _joined(self, left: _Poly, right: _Poly) -> bool:
        self._parts()
        return self._owner.get((left.tile, left.index)) is self._owner.get((right.tile, right.index))

    def _surface(self) -> set[tuple[int, int]]:
        parts = self._parts()
        return parts[0] if parts else set()

    def _closest(self, point: tuple[float, float, float], group: set[tuple[int, int]]) -> _Poly | None:
        lookup = self._index()
        best = None
        best_d = 1e+18
        for pid in group:
            poly = lookup.get(pid)
            if poly is None:
                continue
            dist = _horiz(poly.center, point)
            if dist < best_d:
                best = poly
                best_d = dist
        return best

    def unvisited(self, start: tuple[float, float, float], avoid: set[tuple[int, int]] | None = None) -> tuple[float, float, float] | None:
        begin = self.nearest(start)
        if begin is None:
            return None
        self.visited.add((begin.tile, begin.index))
        avoid = avoid or set()
        fresh = [poly for poly in self.polys if (poly.tile, poly.index) not in self.visited and cell_of(poly.center[0], poly.center[1]) not in avoid]
        if not fresh:
            fresh = [poly for poly in self.polys if (poly.tile, poly.index) not in self.visited]
        if not fresh:
            return None
        farther = [poly for poly in fresh if _horiz(poly.center, start) > 2.0]
        pool = farther or fresh
        return min(pool, key=lambda poly: _horiz(poly.center, start)).center

    def locate(self, point: tuple[float, float, float]) -> tuple[int, int] | None:
        poly = self.nearest(point)
        if poly is None or not poly.verts:
            return None
        return (poly.tile, poly.index)

    def center(self, poly_id: tuple[int, int]) -> tuple[float, float, float] | None:
        poly = self._index().get(poly_id)
        if poly is None or not poly.verts:
            return None
        return poly.center

    def links(self, poly_id: tuple[int, int]) -> list[tuple[tuple[int, int], tuple[float, float, float]]]:
        poly = self._index().get(poly_id)
        if poly is None:
            return []
        found = []
        for neighbor in poly.neighbors:
            other = self._index().get(neighbor)
            if other is not None and other.verts:
                found.append((neighbor, other.center))
        return found

    def _index(self) -> dict[tuple[int, int], _Poly]:
        cached = self._by_id
        if cached is None:
            cached = {(poly.tile, poly.index): poly for poly in self.polys}
            self._by_id = cached
        return cached

_LOADED: dict[str, NavMesh | None] = {}

def load_nav(zone: str, root: Path | None = None) -> NavMesh | None:
    key = (zone or '').lower()
    if root is None and key in _LOADED:
        return _LOADED[key]
    mesh = _read_nav(key, root)
    if root is None:
        _LOADED[key] = mesh
    return mesh

def _read_nav(zone: str, root: Path | None) -> NavMesh | None:
    base = root or maps_root()
    if base is None or not zone:
        return None
    path = base / 'nav' / f'{zone}.nav'
    if not path.is_file():
        return None
    blob = path.read_bytes()
    if blob[:9] != b'EQNAVMESH':
        raise ValueError(f'{path} is not an EQNAVMESH')
    version = struct.unpack_from('<I', blob, 9)[0]
    if version != 2:
        raise ValueError(f'{path} nav version {version}')
    data_size, buffer_size = struct.unpack_from('<II', blob, 13)
    inflated = zlib.decompress(blob[21:21 + data_size])
    if len(inflated) != buffer_size and buffer_size:
        inflated = inflated[:buffer_size]
    polys, portals = _tiles(inflated)
    _link_portals(polys, portals)
    return NavMesh(zone, version, polys)

def _tiles(buf: bytes) -> tuple[list[_Poly], list[tuple[tuple[int, int], tuple[float, float, float]]]]:
    if len(buf) < 32:
        return ([], [])
    count = struct.unpack_from('<I', buf)[0]
    offset = 4 + 28
    polys: list[_Poly] = []
    portals: list[tuple[tuple[int, int], tuple[float, float, float]]] = []
    for tile_index in range(count):
        if offset + 8 > len(buf):
            break
        _tile_ref, size = struct.unpack_from('<II', buf, offset)
        offset += 8
        tile = buf[offset:offset + size]
        offset += size
        tile_polys, tile_portals = _tile_polys(tile_index, tile)
        polys.extend(tile_polys)
        portals.extend(tile_portals)
    return (polys, portals)

def _tile_polys(tile_index: int, tile: bytes) -> tuple[list[_Poly], list[tuple[tuple[int, int], tuple[float, float, float]]]]:
    if len(tile) < _HEADER:
        return ([], [])
    magic, version, _x, _y, _layer, _user, poly_count, vert_count = struct.unpack_from('<8i', tile)
    if magic != 1145979222 or version != 7 or poly_count <= 0 or (vert_count <= 0):
        return ([], [])
    vert_at = _HEADER
    poly_at = vert_at + vert_count * 12
    if poly_at + poly_count * _POLY > len(tile):
        return ([], [])
    verts = []
    for index in range(vert_count):
        dx, dy, dz = struct.unpack_from('<fff', tile, vert_at + index * 12)
        verts.append((dx, dz, dy))
    found: list[_Poly] = []
    raw_neis: list[list[int]] = []
    portals: list[tuple[tuple[int, int], tuple[float, float, float]]] = []
    for index in range(poly_count):
        start = poly_at + index * _POLY
        values = struct.unpack_from('<I6H6HHBB', tile, start)
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
        center = (sum((point[0] for point in poly_verts)) / len(poly_verts), sum((point[1] for point in poly_verts)) / len(poly_verts), sum((point[2] for point in poly_verts)) / len(poly_verts))
        found.append(_Poly(tile_index, index, center, poly_verts))
        edge_neis = list(neis[:vert_count])
        raw_neis.append(edge_neis)
        for edge, nei in enumerate(edge_neis):
            if not nei & 32768 or edge + 1 > len(poly_verts):
                continue
            a = poly_verts[edge]
            b = poly_verts[(edge + 1) % len(poly_verts)]
            mid = ((a[0] + b[0]) * 0.5, (a[1] + b[1]) * 0.5, (a[2] + b[2]) * 0.5)
            portals.append(((tile_index, index), mid))
    by_index = {poly.index: poly for poly in found}
    for poly, neis in zip(found, raw_neis):
        for nei in neis:
            if not nei or nei & 32768:
                continue
            other = by_index.get(nei - 1)
            if other is not None and other.verts:
                poly.neighbors.append((other.tile, other.index))
    kept = [poly for poly in found if poly.verts]
    kept_ids = {(poly.tile, poly.index) for poly in kept}
    return (kept, [portal for portal in portals if portal[0] in kept_ids])

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

def _reaches(chain: list[_Poly], goal: _Poly) -> bool:
    return len(chain) >= 2 and chain[-1].tile == goal.tile and (chain[-1].index == goal.index)

def _astar(polys: list[_Poly], start: _Poly, goal: _Poly, avoid: set[tuple[int, int]] | None = None) -> list[_Poly]:
    lookup = {(poly.tile, poly.index): poly for poly in polys}
    goal_id = (goal.tile, goal.index)
    start_id = (start.tile, start.index)
    blocked = avoid or set()
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
            if neighbor != goal_id and cell_of(other.center[0], other.center[1]) in blocked:
                continue
            step = cost[current] + _horiz(poly.center, other.center)
            if step < cost.get(neighbor, 1e+18):
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
        yi, yj = (points[i][1], points[j][1])
        xi, xj = (points[i][0], points[j][0])
        if (yi > y) != (yj > y) and x < (xj - xi) * (y - yi) / (yj - yi + 1e-12) + xi:
            inside = not inside
        j = i
    return inside

def _horiz(a: tuple[float, float, float], b: tuple[float, float, float]) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])
