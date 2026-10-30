"""Stride state for one character.

Movement is not an action. It does not append actions. It does not import
eqclient or eqclient2. The world owns one Movement. The bus calls handle
on that object. Callers use world.movement. They do not import this module
to keep a position.

The loop calls hold_if_idle once per pulse after the action step. If nobody
called advance during that pulse, hold_if_idle queues one hold OP_ClientUpdate
from the committed position (anim 0, no horizontal step). If advance ran,
hold_if_idle sends nothing.

``plan`` does not send OP_Consider and does not write a position. ``advance``
is the only move-packet builder. A closed door on the stride gets one
OP_ClickDoor before the step through it. The next stride through that door
waits until OP_MoveDoor. A call whose active action is named Reclaim does
not send OP_Consider.

A step lands on the zone-map floor under its feet. A navmesh center is one
height for the whole polygon, and in tutorialb that center is under the
collision floor, so the body never leaves the spawn. The height change is
capped the way v1 and v2 cap it. OP_FloatListThing is the current position,
sent before OP_ClientUpdate. Spawn id 0 is this client: a nonzero id that is
not the player's is a boat update and the player stays put. The zone does not
echo our own update, so a stride that times out with no refusal takes the
point it asked for.
"""
from __future__ import annotations

import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterator
    from eqclient3.action import Action
    from eqclient3.loop import Loop
    from eqclient3.nav.water import WaterMap
    from eqclient3.world import Door, Mob, World

import math
import struct
import time
from dataclasses import dataclass
from eqclient3.struct_helpers import eq_heading
from eqclient3.structs import EQStruct, OP_ClickDoor, OP_ClientUpdate, OP_Consider, OP_FindPersonReply, OP_FloatListThing, OP_MobUpdate, OP_MoveDoor, OP_NewZone, OPERATIONS
from eqclient3.nav.navmesh import load_nav
from eqclient3.nav.path import NEARBY_YARDS, STRIDE, Path, along, doors_on_stride, find as path_find, is_nearby, iter_mobs, mob_id, mob_point, route, track as path_track, water_of
log = logging.getLogger('eqclient3.movement')
LOG_PACKETS = False
STRIDE_TIMEOUT = 3
STRIDE_MOB_RADIUS = 2.0
_COMMIT_TOLERANCE = 0.35
OPCODES = ('OP_ClientUpdate', 'OP_MobUpdate', 'OP_NewZone', 'OP_MoveDoor', 'OP_FindPersonReply')

@dataclass
class MovementAnnotatedMob:
    """A mob already on the current stride. Values are copied off the Mob."""
    mob: object
    distance: object = None
    direction: object = None
    consider: object = None
    targeted: bool = False

class Movement:
    """Position, the stride in flight, and the packets that move us."""

    def __init__(self, world: World | None = None) -> None:
        self.world = world
        self.position: tuple = (0.0, 0.0, 0.0)
        self.heading: int = 0
        self.asked: tuple | None = None
        self.asked_tick: int = 0
        self.anim: int = 0
        self.committed: bool = True
        self.refused: bool = False
        self.sequence: int = 0
        self.caller_mode: str = 'run'
        self.advanced: bool = False
        self.path: Path | None = None
        self.clicked: set = set()
        self.open_ids: set = set()
        self.find_mob: Mob | None = None
        self._nav = None
        self._nav_zone = None

    @property
    def stride_committed(self) -> bool:
        return self.committed

    def opcodes(self) -> tuple[str, ...]:
        """Opcodes the bus should deliver to handle()."""
        return OPCODES

    def bind(self, world: World) -> None:
        """Remember the sheet plan() reads for doors, water, mobs, and the zone."""
        self.world = world

    def reset(self, origin: tuple[float, float, float]=(0.0, 0.0, 0.0)) -> None:
        """Clear stride state. A new session calls this. OP_NewZone clears a zone entry."""
        point = (float(origin[0]), float(origin[1]), float(origin[2]))
        self.position = point
        self.heading = 0
        self.asked = None
        self.asked_tick = 0
        self.anim = 0
        self.committed = True
        self.refused = False
        self.sequence = 0
        self.caller_mode = 'run'
        self.advanced = False
        self.path = None
        self.clicked = set()
        self.open_ids = set()
        self.find_mob = None

    def snap(self, world: World, point: tuple[float, float, float]) -> None:
        """The server moved us inside this zone. Drop the stride and take the point."""
        if world is not None:
            self.bind(world)
        self.asked = None
        self.asked_tick = 0
        self.anim = 0
        self.committed = True
        self.refused = False
        self.path = None
        self.position = (float(point[0]), float(point[1]), float(point[2]))
        _write_world(world, self.position)

    def handle(self, opcode: str, payload: object, world: World | None = None) -> None:
        """Bus entry. Our position, a zone entry, an opened door, or find waypoints."""
        if world is not None:
            self.bind(world)
        world = world if world is not None else self.world
        row = payload
        if isinstance(payload, (bytes, bytearray)):
            kind = OPERATIONS.get(opcode)
            if kind is None:
                return
            try:
                row = kind.deserialize(bytes(payload))
            except (ValueError, struct.error):
                return
        if not isinstance(row, EQStruct):
            return
        if isinstance(row, (OP_ClientUpdate, OP_MobUpdate)):
            self._on_position(row, world)
        elif isinstance(row, OP_NewZone):
            self._on_new_zone(row, world)
        elif isinstance(row, OP_MoveDoor):
            self._on_move_door(row, world)
        elif isinstance(row, OP_FindPersonReply):
            self._on_find_reply(row)

    def plan(self, destination: tuple[float, float, float] | str | Mob, mode: str | None = None, world: World | None = None, loop: Loop | None = None) -> Path:
        """Return a Path. Does not send OP_Consider and does not write a position.

        ``loop`` is accepted and ignored so a distance read cannot send.
        ``mode`` is run, los, walk, creep, hold, or swim. Swim keeps the stride
        of the last mode (run, until one was planned) and changes only z.
        """
        del loop
        if world is not None:
            self.bind(world)
        world = self.world
        mode = mode or 'run'
        if mode not in STRIDE and mode != 'swim':
            mode = 'run'
        base = self.caller_mode if mode == 'swim' else mode
        if base not in STRIDE:
            base = 'run'
        length, anim = STRIDE[base]
        if mode != 'swim':
            self.caller_mode = mode
        origin = self.position
        zone = world.zone or '' if world is not None else ''
        water = water_of(world, zone)
        built = route(origin, destination, zone=zone, doors=world.doors if world is not None else None, water=water, length=length, mode=mode)
        built.stride_length = length
        built.anim = anim
        built.mode = mode
        if mode == 'swim':
            target_z = _surface_z(origin, built.destination, water)
            built.z_only = True
            built.swim_z = target_z
            built.next_point = _z_step(origin, target_z, length)
            built.in_water = built.in_water or _liquid(water, built.next_point) or _liquid(water, built.destination)
        kept = self._keep_find_path(built)
        if kept is not None:
            return kept
        self.path = built
        return built

    def advance(self, loop: Loop, world: World, path: Path, sender: Action | None = None) -> None:
        """One stride. The only builder of OP_ClientUpdate and the only door click.

        While the last stride is not committed and the short timeout has not
        fired, the same asked point is sent again. A closed door on the stride
        is clicked once. The stride that would pass that door waits for OP_MoveDoor.
        """
        self.advanced = True
        if world is not None:
            self.bind(world)
        world = world if world is not None else self.world
        self.path = path
        self._drop_find(world, path)
        
        self._send_considers(loop, world, sender)
        here = self.position
        tick = _loop_tick(loop)
        doors = self._click_doors(world, path)
        if self.asked is not None and (not self.committed):
            if tick - self.asked_tick < STRIDE_TIMEOUT:
                self._click_if_needed(loop, self._blocking(here, self.asked, doors))
                self._emit(loop, world, self.asked, self.anim, 'stride')
                return
            self._settle_timeout(world)
            here = self.position
        nxt = self._aim(path, here)
        blocking = self._blocking(here, nxt, doors)
        if blocking:
            self._click_if_needed(loop, blocking)
            spot = (float(blocking.x), float(blocking.y), float(blocking.z))
            if _horiz(here, spot) > 1.0 and _door_on(here, nxt, blocking):
                nxt = self._on_floor(here, spot)
            else:
                return
        self._start_stride(loop, world, here, nxt, int(path.anim or 0), tick)

    def hold_if_idle(self, loop: Loop, world: World | None = None) -> None:
        """One hold update when this pulse did not call advance."""
        if world is not None:
            self.bind(world)
        world = self.world
        if self.advanced:
            self.advanced = False
            return
        self._emit(loop, world, self.position, 0, 'hold')

    def visible_mobs(self, world: World | None = None, loop: Loop | None = None) -> list[Mob]:
        """Mobs in line of sight from the committed position. Does not send OP_Consider."""
        del loop
        if world is not None:
            self.bind(world)
        world = world if world is not None else self.world
        origin = self.position
        seen = []
        for mob in iter_mobs(world):
            if _is_self(world, mob):
                continue
            if _can_see(world, origin, mob):
                seen.append(mob)
        return seen

    def mobs_on_path(self, mobs: list[Mob], loop: Loop | None = None) -> list[MovementAnnotatedMob] | None:
        """Mobs on the current stride, or None. Does not send OP_Consider.

        Each result is a MovementAnnotatedMob. distance, direction, consider, and
        targeted are the values already on the Mob.
        """
        del loop
        if not mobs:
            return None
        here = self.position
        end = self.asked
        if end is None and self.path is not None:
            end = self.path.next_point
        if end is None:
            return None
        found = []
        for mob in mobs:
            if not _mob_on_stride(here, end, mob):
                continue
            found.append(MovementAnnotatedMob(mob=mob, distance=mob.distance, direction=mob.direction, consider=mob.consider, targeted=bool(mob.targeted)))
        return found or None

    def find(self, loop: Loop, world: World, mob: Mob) -> bool:
        """OP_FindPersonRequest when the mob is not nearby and the mesh has no route."""
        if world is not None:
            self.bind(world)
        sent = path_find(loop, world, mob, origin=self.position)
        if sent:
            self.find_mob = mob
        return sent

    def track(self, loop: Loop, world: World, mob: Mob) -> bool:
        """OP_Track then OP_TrackTarget. Does not create a Mob."""
        if world is not None:
            self.bind(world)
        return bool(path_track(loop, world, mob, origin=self.position))

    def _settle_timeout(self, world: World) -> None:
        """The zone does not echo our ClientUpdate. Take the asked point unless it refused us."""
        asked = self.asked
        refused = self.refused
        self.refused = False
        self.committed = True
        self.asked = None
        if refused or asked is None:
            return
        if _horiz(self.position, asked) <= 0.4 and abs(self.position[2] - asked[2]) <= 0.4:
            return
        self.position = (float(asked[0]), float(asked[1]), float(asked[2]))
        _write_world(world, self.position)

    def _keep_find_path(self, built: Path) -> Path | None:
        current = self.path
        if current is None or not current.find_waypoints:
            return None
        if not _same(current.destination, built.destination):
            return None
        if not _same(current.origin, self.position, tol=1.0):
            return None
        return current

    def _drop_find(self, world: World, path: Path) -> None:
        mob = self.find_mob
        if mob is None or not path.find_waypoints:
            return
        origin = self.position
        if not (is_nearby(world, mob, origin) or _can_see(world, origin, mob)):
            return
        path.find_waypoints = False
        zone = world.zone or '' if world is not None else ''
        fresh = route(origin, path.destination, zone=zone, doors=world.doors if world is not None else None, water=water_of(world, zone), length=path.stride_length, mode=path.mode)
        path.points = fresh.points
        path.door = fresh.door
        path.in_water = fresh.in_water
        path.fallback = fresh.fallback
        path.next_point = fresh.next_point
        path.origin = origin

    def _aim(self, path: Path, here: tuple[float, float, float]) -> tuple[float, float, float]:
        if path.z_only:
            target = path.swim_z if path.swim_z is not None else path.destination[2]
            return _z_step(here, target, path.stride_length)
        nxt = along(here, path.points, path.stride_length)
        return self._on_floor(here, nxt)

    def _on_floor(self, here: tuple[float, float, float], step: tuple[float, float, float]) -> tuple[float, float, float]:
        """Keep the step on the floor. A stride climbs a ramp; it does not teleport in Z."""
        target_z = step[2]
        ground = self._ground(step[0], step[1], here[2])
        if ground is not None:
            target_z = ground
        else:
            mesh = self._mesh()
            if mesh is not None:
                poly = mesh.nearest((step[0], step[1], here[2]))
                if poly is not None and _horiz((step[0], step[1], 0.0), (poly.center[0], poly.center[1], 0.0)) <= 18.0:
                    target_z = poly.center[2]
        gap = target_z - here[2]
        travel = max(_horiz(here, step), 0.5)
        budget = min(10.0, max(2.0, travel * 1.5))
        if abs(gap) > budget:
            target_z = here[2] + (budget if gap > 0 else -budget)
        return (float(step[0]), float(step[1]), float(target_z))

    def _ground(self, x: float, y: float, z: float) -> float | None:
        """Collision floor at this step. None when the zone has no map."""
        world = self.world
        zone = world.zone or '' if world is not None else ''
        if not zone:
            return None
        from eqclient3.nav.maps import load_map
        zone_map = load_map(zone)
        if zone_map is None:
            return None
        return zone_map.ground(x, y, z)

    def _mesh(self):
        world = self.world
        zone = world.zone or '' if world is not None else ''
        if not zone:
            return None
        if self._nav is not None and self._nav_zone == zone:
            return self._nav
        try:
            mesh = load_nav(zone)
        except (OSError, ValueError):
            mesh = None
        self._nav = mesh
        self._nav_zone = zone
        return mesh

    def _start_stride(self, loop: Loop, world: World, here: tuple[float, float, float], nxt: tuple[float, float, float], anim: int, tick: int) -> None:
        self._emit(loop, world, nxt, anim, 'stride')
        self.asked = nxt
        self.asked_tick = tick
        self.anim = anim
        self.committed = False
        self.refused = False
        if _horiz(here, nxt) > 0.05 or abs(nxt[2] - here[2]) > 0.05:
            self.heading = eq_heading(here[0], here[1], nxt[0], nxt[1])

    def _emit(self, loop: Loop, world: World, point: tuple[float, float, float], anim: int, label: str) -> None:
        self.sequence = (self.sequence + 1) & 65535
        here = self.position
        # 0 is this client. A nonzero id that is not GetID() updates a boat and the player stays put.
        spawn = 0
        stamp = int(time.time() * 1000) & 4294967295
        if LOG_PACKETS:
            log.info(
                'move %s OP_FloatListThing OP_ClientUpdate (%.1f, %.1f, %.1f) -> (%.1f, %.1f, %.1f) seq=%s anim=%s',
                label,
                here[0],
                here[1],
                here[2],
                point[0],
                point[1],
                point[2],
                self.sequence,
                anim,
            )
        loop.send('OP_FloatListThing', OP_FloatListThing(here[0], here[1], here[2], stamp).serialize())
        loop.send(
            'OP_ClientUpdate',
            OP_ClientUpdate(
                spawn,
                point[0],
                point[1],
                point[2],
                self.sequence,
                self.heading,
                anim,
                point[0] - here[0],
                point[1] - here[1],
            ).serialize(),
        )

    def _click_if_needed(self, loop: Loop, door: Door) -> None:
        if not door:
            return
        ident = door.id
        if ident in self.clicked or ident in self.open_ids:
            return
        if door.opened:
            return
        self.clicked.add(ident)
        loop.send('OP_ClickDoor', OP_ClickDoor(ident).serialize())

    def _click_doors(self, world: World, path: Path) -> list[Door]:
        doors = list(_iter_doors(world.doors if world is not None else None))
        extra = path.door
        if extra is not None:
            doors.append(extra)
        return doors

    def _blocking(self, here: tuple[float, float, float], nxt: tuple[float, float, float], doors: dict[int, Door] | list[Door]) -> Door | None:
        for door in doors_on_stride(here, nxt, doors):
            if door.id in self.open_ids:
                continue
            if door.opened:
                continue
            return door
        for door in doors:
            if door.opened:
                continue
            if door.id in self.open_ids:
                continue
            spot = (float(door.x), float(door.y), float(door.z))
            if _horiz(here, spot) <= 1.5 and abs(here[2] - spot[2]) <= 20.0 and (_horiz(here, nxt) > 1.0):
                return door
        return None

    def _send_considers(self, loop: Loop, world: World, sender: Action | None = None) -> None:
        if _is_reclaim(loop, sender):
            return
        origin = self.position
        for mob in _consider_mobs(world, origin):
            if not _can_see(world, origin, mob):
                continue
            if not _needs_consider(mob, world):
                continue
            spawn = int(world.self_id or 0)
            loop.send('OP_Consider', OP_Consider(spawn, mob_id(mob)).serialize())
            _remember_consider(mob, world)

    def _on_position(self, row: OP_ClientUpdate | OP_MobUpdate, world: World) -> None:
        spawn_id = int(row.spawn_id)
        x, y, z = float(row.x), float(row.y), float(row.z)
        heading = row.heading if isinstance(row, OP_ClientUpdate) and not row.server else None
        if not _is_our_spawn(world, spawn_id):
            return
        point = (x, y, z)
        if self.asked is not None and (not self.committed):
            if _same(point, self.asked, tol=_COMMIT_TOLERANCE):
                self.committed = True
                self.refused = False
            elif _horiz(point, self.position) <= 0.8 and (_horiz(self.position, self.asked) > 0.4 or abs(self.position[2] - self.asked[2]) > 0.4):
                self.refused = True
        self.position = point
        if heading is not None:
            self.heading = heading
        _write_world(world, point)

    def _on_new_zone(self, row: OP_NewZone, world: World) -> None:
        _short = row.short_name
        safe = (float(row.x), float(row.y), float(row.z))
        self.asked = None
        self.asked_tick = 0
        self.anim = 0
        self.committed = True
        self.refused = False
        self.position = safe
        self.path = None
        self.clicked = set()
        self.open_ids = set()
        self.find_mob = None
        _write_world(world, safe)
        if world is not None and _short:
            world.zone = _short

    def _on_move_door(self, row: OP_MoveDoor, world: World) -> None:
        door_id = row.door_id
        self.open_ids.add(door_id)
        self.clicked.discard(door_id)
        for door in _iter_doors(world.doors if world else None):
            if door.id == door_id:
                door.opened = True

    def _on_find_reply(self, row: OP_FindPersonReply) -> None:
        points = list(row.points)
        path = self.path
        if path is None or not points:
            return
        path.points = points
        path.find_waypoints = True
        path.next_point = points[0]
        path.fallback = False

def _z_step(here: tuple[float, float, float], target_z: float, length: float) -> tuple[float, float, float]:
    gap = float(target_z) - here[2]
    if abs(gap) <= length:
        nz = float(target_z)
    else:
        nz = here[2] + (length if gap > 0.0 else -length)
    return (here[0], here[1], nz)

def _surface_z(here: tuple[float, float, float], destination: tuple[float, float, float] | str | Mob, water: WaterMap) -> float:
    if water is not None:
        try:
            surf = water.surface_z(here[0], here[1])
        except (TypeError, ValueError):
            surf = None
        if surf is not None:
            return float(surf)
    return float(destination[2])

def _liquid(water: WaterMap, point: tuple[float, float, float]) -> bool:
    if water is None or point is None:
        return False
    try:
        return bool(water.in_liquid(point[0], point[1], point[2]))
    except (TypeError, ValueError):
        return False

def _door_on(here: tuple[float, float, float], nxt: tuple[float, float, float], door: Door) -> bool:
    return bool(doors_on_stride(here, nxt, [door]))

def _is_reclaim(loop: Loop, sender: Action) -> bool:
    current = loop.active if loop is not None else None
    for obj in (sender, current):
        if obj is not None and type(obj).__name__ == 'Reclaim':
            return True
    return False

def _consider_mobs(world: World, origin: tuple[float, float, float]) -> list[object]:
    del origin
    if not world:
        return []
    return [mob for mob in world.nearby(NEARBY_YARDS) if not _is_self(world, mob)]

def _needs_consider(mob: Mob, world: World) -> bool:
    amount, maxed, changed = _faction(world, mob.faction_id)
    sent = mob._consider_sent or mob.faction_last_considered is not None
    if not sent:
        return True
    if maxed in ('positive', 'negative'):
        return False
    if changed and (not mob._consider_change_sent):
        return True
    return amount != mob.faction_last_considered

def _remember_consider(mob: Mob, world: World) -> None:
    amount, _maxed, changed = _faction(world, int(mob.faction_id or 0))
    mob.faction_last_considered = amount
    mob._consider_sent = True
    mob._consider_change_sent = bool(changed)

def _faction(world: World, faction_id: int) -> tuple[object, ...]:
    raw = None
    factions = world.factions
    if isinstance(factions, dict):
        raw = factions.get(faction_id)
    amount = None
    maxed = None
    changed = False
    if raw is None:
        return (amount, maxed, changed)
    if isinstance(raw, bool):
        return (amount, None, raw)
    if isinstance(raw, (int, float)) and (not isinstance(raw, bool)):
        return (int(raw), None, False)
    if isinstance(raw, str):
        text = raw.lower()
        if 'positive' in text:
            return (None, 'positive', False)
        if 'negative' in text:
            return (None, 'negative', False)
        if text == 'changed':
            return (None, None, True)
        return (None, None, False)
    if isinstance(raw, dict):
        amount = raw.get('amount')
        maxed = raw.get('maxed')
        changed = bool(raw.get('changed'))
    else:
        amount = raw.amount
        maxed = raw.maxed
        changed = bool(raw.changed)
    if isinstance(maxed, bool):
        maxed = 'positive' if maxed else None
    if isinstance(maxed, str):
        maxed = maxed.lower()
        if maxed in ('maxed_positive', 'best', '+'):
            maxed = 'positive'
        elif maxed in ('maxed_negative', 'worst', '-'):
            maxed = 'negative'
    return (amount, maxed, changed)

def _can_see(world: World, origin: tuple[float, float, float], mob: Mob) -> bool:
    del origin
    if not world:
        return False
    return world.line_of_sight(mob)

def _is_self(world: World, mob: Mob) -> bool:
    self_id = world.self_id if world else 0
    if not self_id:
        return False
    return mob_id(mob) == self_id

def _mob_on_stride(here: tuple[float, float, float], end: tuple[float, float, float], mob: Mob) -> bool:
    point = mob_point(mob)
    if point is None:
        return False
    if abs(point[2] - here[2]) > 20.0 and abs(point[2] - end[2]) > 20.0:
        return False
    dx, dy = (end[0] - here[0], end[1] - here[1])
    length = dx * dx + dy * dy
    if length <= 1e-06:
        return False
    tee = ((point[0] - here[0]) * dx + (point[1] - here[1]) * dy) / length
    if tee <= 0.0 or tee > 1.0:
        return False
    along_yards = math.sqrt(tee * tee * length)
    if along_yards < 1.0:
        return False
    nearest = (here[0] + tee * dx, here[1] + tee * dy)
    return math.hypot(point[0] - nearest[0], point[1] - nearest[1]) <= STRIDE_MOB_RADIUS

def _is_our_spawn(world: World, spawn_id: int) -> bool:
    spawn_id = int(spawn_id)
    self_id = world.self_id if world else 0
    if spawn_id == 0:
        return True
    return bool(self_id) and spawn_id == self_id

def _write_world(world: World, point: tuple[float, float, float]) -> None:
    if world is None:
        return
    world.position = (float(point[0]), float(point[1]), float(point[2]))

def _loop_tick(loop: Loop) -> int:
    if loop is None:
        return 0
    return int(loop.tick)

def _iter_doors(doors: dict[int, Door] | list[Door]) -> Iterator[object]:
    if not doors:
        return
    if isinstance(doors, dict):
        yield from doors.values()
        return
    yield from doors

def _horiz(a: tuple[float, float, float], b: tuple[float, float, float]) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])

def _same(a: tuple[float, float, float], b: tuple[float, float, float], tol: float=0.05) -> bool:
    if a is None or b is None:
        return False
    return abs(a[0] - b[0]) <= tol and abs(a[1] - b[1]) <= tol and (abs(a[2] - b[2]) <= tol)

def pack_server_position(spawn_id: int, x: float, y: float, z: float) -> bytes:
    """Titanium server position, so a test can commit a stride."""
    return OP_MobUpdate(int(spawn_id), float(x), float(y), float(z)).serialize()
