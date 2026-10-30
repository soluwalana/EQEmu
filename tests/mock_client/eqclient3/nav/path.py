"""Mesh step, a door on that step, and water.

Unstick stays off. ``route`` walks the destination it was given. A walk that
does not advance is the same destination again, not a new one. The two-point
list ``NavMesh.path`` returns when A* has no route is ``Path.fallback`` and
does not count as reaching the goal polygon. Use ``NavMesh.reaches``.

``find`` and ``track`` send through ``loop.send``. They do not write a Mob
and they do not build a MovementAnnotatedMob.
"""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterator
    from eqclient3.loop import Loop
    from eqclient3.nav.water import WaterMap
    from eqclient3.nav.travel import Transit, ZoneGraph
    from eqclient3.world import Door, Mob, World

import math
from dataclasses import dataclass, field
from pathlib import Path as GraphFile
from eqclient3.nav.navmesh import load_nav
from eqclient3.structs import OP_FindPersonReply, OP_FindPersonRequest, OP_Track, OP_TrackTarget
from eqclient3.nav.travel import DEFAULT_ZONE_GRAPH, first_leg, read_zone_graph
from eqclient3.nav.water import load_water
_V1_STEP = 14.0
_V1_LOS = 19.6
STRIDE = {'run': (_V1_STEP * 0.75, 20), 'los': (_V1_LOS * 0.75, 20), 'walk': (_V1_STEP / 3.0 * 0.75, 12), 'creep': (_V1_STEP / 6.0 * 0.75, 12), 'hold': (0.0, 0)}
NEARBY_YARDS = 200.0
DOOR_REACH = 15.0
TRACK_SKILL = 53
_ZONE_POINT_REACH = 12.0

@dataclass
class Path:
    """One planned walk. ``distance`` is yards from the committed position."""
    distance: float
    points: list = field(default_factory=list)
    door: object | None = None
    in_water: bool = False
    mode: str = 'run'
    destination: tuple = (0.0, 0.0, 0.0)
    next_point: tuple = (0.0, 0.0, 0.0)
    origin: tuple = (0.0, 0.0, 0.0)
    stride_length: float = 0.0
    anim: int = 0
    z_only: bool = False
    swim_z: float | None = None
    find_waypoints: bool = False
    fallback: bool = False

def route(origin: tuple[float, float, float], destination: tuple[float, float, float] | str | Mob, *, zone: str='', doors: dict[int, Door] | list[Door] | None = None, water: WaterMap | None = None, length: float=10.5, mode: str='run') -> Path:
    """Next mesh point, a door on this stride or a zoneline, and water.

    ``length`` is the caller's stride. Swim is applied by movement: this
    function still reports the door and whether the point is in water.
    """
    origin = _xyz(origin)
    goal, zoneline = _goal(destination, zone, origin)
    points, fallback = _polyline(origin, goal, zone)
    nxt = along(origin, points, length)
    live = doors_on_stride(origin, nxt, doors)
    door = live[0] if live else zoneline
    if live:
        nxt = _door_xyz(live[0])
    wet = _in_liquid(water, nxt) or _in_liquid(water, goal)
    return Path(distance=_length(origin, points, goal), points=points, door=door, in_water=wet, mode=mode, destination=goal, next_point=nxt, origin=origin, stride_length=float(length), fallback=fallback)

def along(origin: tuple[float, float, float], points: list[tuple[float, float, float]], length: float) -> tuple[float, float, float]:
    """Walk up to ``length`` horizontal yards along ``points``."""
    origin = _xyz(origin)
    if length <= 0.0 or not points:
        return origin
    prev = origin
    left = float(length)
    for point in points:
        point = _xyz(point)
        span = _horiz(prev, point)
        if span <= 1e-06:
            prev = point
            continue
        if span + 1e-09 >= left:
            scale = left / span
            # Z is the waypoint, not a blend between centers. A blend sits
            # between floors and the zone leaves the client where it was.
            return (prev[0] + (point[0] - prev[0]) * scale, prev[1] + (point[1] - prev[1]) * scale, point[2])
        left -= span
        prev = point
    return _xyz(points[-1])

def doors_on_stride(origin: tuple[float, float, float], end: tuple[float, float, float], doors: dict[int, Door] | list[Door], reach: float=DOOR_REACH) -> list:
    """Closed doors whose position lies on the segment, nearest first."""
    origin = _xyz(origin)
    end = _xyz(end)
    hits = []
    for door in iter_doors(doors):
        if door.opened:
            continue
        try:
            dz = abs(float(door.z) - origin[2])
        except (TypeError, ValueError):
            continue
        if dz > 20.0:
            continue
        xy = (float(door.x), float(door.y))
        tee = _segment_t(xy, origin, end)
        if tee is None or tee <= 0.0 or tee > 1.0:
            continue
        if _segment_distance(xy, origin, end) > reach:
            continue
        hits.append((tee, door))
    hits.sort(key=lambda item: item[0])
    return [door for _tee, door in hits]

def find(loop: Loop, world: World, mob: Mob, origin: tuple[float, float, float] | None = None) -> bool:
    """OP_FindPersonRequest when the mob is not nearby and the mesh has no route."""
    origin = _xyz(origin) if origin is not None else _world_origin(world)
    if is_nearby(world, mob, origin):
        return False
    if mesh_reaches(world.zone or '', origin, mob_point(mob)):
        return False
    loop.send('OP_FindPersonRequest', OP_FindPersonRequest(mob_id(mob), origin[0], origin[1], origin[2]).serialize())
    return True

def track(loop: Loop, world: World, mob: Mob, origin: tuple[float, float, float] | None = None) -> bool:
    """OP_Track then OP_TrackTarget when the skill is known and the mob is outside nearby.

    The track list itself is the mob handler's write. This does not create a
    Mob and it does not build a MovementAnnotatedMob.
    """
    if not track_known(world):
        return False
    origin = _xyz(origin) if origin is not None else _world_origin(world)
    if is_nearby(world, mob, origin):
        return False
    loop.send('OP_Track', OP_Track().serialize())
    loop.send('OP_TrackTarget', OP_TrackTarget(mob_id(mob)).serialize())
    return True

def find_waypoints(payload: bytes) -> list[tuple[float, float, float]]:
    """Points from OP_FindPersonReply. The first 12 bytes are the destination."""
    if not payload or len(payload) < 24:
        return []
    return OP_FindPersonReply.deserialize(payload).points

def mesh_reaches(zone: str, origin: tuple[float, float, float], goal: tuple[float, float, float]) -> bool:
    if not zone or goal is None:
        return False
    try:
        mesh = load_nav(zone)
    except (OSError, ValueError):
        return False
    if mesh is None:
        return False
    return bool(mesh.reaches(_xyz(origin), _xyz(goal)))

def iter_doors(doors: dict[int, Door] | list[Door]) -> Iterator[object]:
    if not doors:
        return
    if isinstance(doors, dict):
        yield from doors.values()
        return
    yield from doors

def iter_mobs(world: World) -> list[Mob]:
    mobs = world.mobs if world is not None else None
    if isinstance(mobs, dict):
        return list(mobs.values())
    if isinstance(mobs, (list, tuple)):
        return list(mobs)
    return []

def mob_id(mob: Mob) -> int:
    return int(mob.id)

def mob_point(mob: Mob) -> tuple[float, float, float] | None:
    if mob is None:
        return None
    try:
        pos = mob.position
    except AttributeError:
        pos = None
    if isinstance(pos, (tuple, list)) and len(pos) >= 3:
        return _xyz(pos)
    return (float(mob.x), float(mob.y), float(mob.z))

def is_nearby(world: World, mob: Mob, origin: tuple[float, float, float], yards: float=NEARBY_YARDS) -> bool:
    if world is not None and callable(world.nearby):
        wanted = mob_id(mob)
        for other in world.nearby(yards):
            if other is mob or mob_id(other) == wanted:
                return True
        return False
    return _range_of(origin, mob) <= yards

def track_known(world: World) -> bool:
    if world is None:
        return False
    return world.skills.get(TRACK_SKILL, 0) > 0

def _goal(destination: tuple[float, float, float] | str | Mob, zone: str, origin: tuple[float, float, float]) -> tuple[tuple[float, float, float], Transit | None]:
    if isinstance(destination, str):
        transit = _transit_toward(zone, destination.strip().lower())
        if transit is None:
            return (origin, None)
        return ((float(transit.x), float(transit.y), float(transit.z)), transit)
    point = _point(destination)
    if point is None:
        point = origin
    transit = _transit_at_point(zone, point)
    return (point, transit)

def _point(destination: tuple[float, float, float] | str | Mob) -> tuple[float, float, float] | None:
    if destination is None or isinstance(destination, str):
        return None
    if isinstance(destination, (tuple, list)) and len(destination) >= 3:
        return _xyz(destination)
    return mob_point(destination)

def _polyline(origin: tuple[float, float, float], goal: tuple[float, float, float], zone: str) -> tuple[list[tuple[float, float, float]], bool]:
    mesh = None
    if zone:
        try:
            mesh = load_nav(zone)
        except (OSError, ValueError):
            mesh = None
    if mesh is None:
        return (_trim(origin, [origin, goal], goal), False)
    points = mesh.path(origin, goal)
    begin = mesh.nearest(origin)
    end = mesh.nearest(goal)
    fallback = False
    if begin is not None and end is not None and ((begin.tile, begin.index) != (end.tile, end.index)) and (len(points) == 2) and _same(points[0], origin) and _same(points[1], goal):
        fallback = True
    return (_trim(origin, points, goal), fallback)

def _trim(origin: tuple[float, float, float], points: list[tuple[float, float, float]], goal: tuple[float, float, float]) -> list[tuple[float, float, float]]:
    pts = [_xyz(point) for point in points]
    while pts and _horiz(origin, pts[0]) <= 1.0:
        pts.pop(0)
    while len(pts) > 1 and _behind(origin, pts[0], pts[1]):
        pts.pop(0)
    if not pts:
        return [goal]
    if _horiz(pts[-1], goal) > 1.0:
        pts.append(goal)
    return pts

def _length(origin: tuple[float, float, float], points: list[tuple[float, float, float]], goal: tuple[float, float, float]) -> float:
    total = 0.0
    prev = origin
    chain = list(points)
    if not chain or _horiz(chain[-1], goal) > 0.5:
        chain.append(goal)
    for point in chain:
        total += _horiz(prev, point)
        prev = point
    return total

def _transit_toward(zone: str, dest: str) -> Transit | None:
    graph = _graph()
    if graph is None or not zone or (not dest):
        return None
    leg = first_leg(graph, zone, dest)
    if leg is None:
        return None
    return graph.transit_at(zone, leg.door_id)

def _transit_at_point(zone: str, point: tuple[float, float, float]) -> Transit | None:
    graph = _graph()
    if graph is None or not zone:
        return None
    best = None
    best_d = _ZONE_POINT_REACH
    for transit in graph.transits_from(zone):
        if (transit.via or '') not in ('point', 'door', 'stone'):
            continue
        dist = _horiz(point, (transit.x, transit.y, transit.z))
        if dist <= best_d:
            best, best_d = (transit, dist)
    return best
_GRAPH = None
_GRAPH_TRIED = False

def _graph() -> ZoneGraph | None:
    global _GRAPH, _GRAPH_TRIED
    if _GRAPH_TRIED:
        return _GRAPH
    _GRAPH_TRIED = True
    try:
        file = GraphFile(DEFAULT_ZONE_GRAPH)
        if file.is_file():
            _GRAPH = read_zone_graph(str(file))
    except (OSError, ValueError, ImportError):
        _GRAPH = None
    return _GRAPH

def _world_origin(world: World) -> tuple[float, float, float]:
    pos = world.position if world is not None else None
    if isinstance(pos, (tuple, list)) and len(pos) >= 3:
        return _xyz(pos)
    return (0.0, 0.0, 0.0)

def _range_of(origin: tuple[float, float, float], mob: Mob) -> float:
    point = mob_point(mob)
    if point is not None:
        return _horiz(origin, point)
    raw = mob.distance
    try:
        return float(raw)
    except (TypeError, ValueError):
        return 1e+18

def _in_liquid(water: WaterMap, point: tuple[float, float, float]) -> bool:
    if water is None or point is None:
        return False
    try:
        return bool(water.in_liquid(point[0], point[1], point[2]))
    except (TypeError, ValueError):
        return False

def _door_xyz(door: Door) -> tuple[float, float, float]:
    return (float(door.x), float(door.y), float(door.z))

def _xyz(point: tuple[float, float, float]) -> tuple[float, float, float]:
    return (float(point[0]), float(point[1]), float(point[2]))

def _horiz(a: tuple[float, float, float], b: tuple[float, float, float]) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])

def _same(a: tuple[float, float, float], b: tuple[float, float, float], tol: float=0.05) -> bool:
    return abs(a[0] - b[0]) <= tol and abs(a[1] - b[1]) <= tol and (abs(a[2] - b[2]) <= tol)

def _behind(here: tuple[float, float, float], point: tuple[float, float, float], nxt: tuple[float, float, float]) -> bool:
    vx, vy = (point[0] - here[0], point[1] - here[1])
    gx, gy = (nxt[0] - here[0], nxt[1] - here[1])
    if gx * gx + gy * gy < 1.0:
        return False
    return vx * gx + vy * gy < 0.0

def _segment_t(point: tuple[float, float, float], start: tuple[float, float, float], end: tuple[float, float, float]) -> float | None:
    dx, dy = (end[0] - start[0], end[1] - start[1])
    length = dx * dx + dy * dy
    if length <= 1e-06:
        return None
    return ((point[0] - start[0]) * dx + (point[1] - start[1]) * dy) / length

def _segment_distance(point: tuple[float, float, float], start: tuple[float, float, float], end: tuple[float, float, float]) -> float:
    dx, dy = (end[0] - start[0], end[1] - start[1])
    length = dx * dx + dy * dy
    if length <= 1e-06:
        return math.hypot(point[0] - start[0], point[1] - start[1])
    tee = max(0.0, min(1.0, ((point[0] - start[0]) * dx + (point[1] - start[1]) * dy) / length))
    nearest = (start[0] + tee * dx, start[1] + tee * dy)
    return math.hypot(point[0] - nearest[0], point[1] - nearest[1])

def water_of(world: World, zone: str='') -> WaterMap | None:
    """World-supplied map, else the zone file. A missing file is no water."""
    if world is not None and world.water_map is not None:
        return world.water_map
    zone = zone or (world.zone if world is not None else '') or ''
    if not zone:
        return None
    try:
        return load_water(zone)
    except (OSError, ValueError):
        return None
