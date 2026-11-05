"""The action superclass. The scheduler and the bus only know this type."""

from collections.abc import Callable
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient4.loop import Loop
    from eqclient4.nav.path import Path
    from eqclient4.world import Mob, World

from eqclient4.nav.travel import ZoneGraph, first_leg
from eqclient4.structs import EQStruct, OP_Consider, OP_TargetMouse


def _consider_id(payload: EQStruct) -> int:
    if isinstance(payload, OP_Consider):
        return int(payload.target_id)
    return 0


class Action:
    def __init__(self, world: World, loop: Loop) -> None:
        self.source = ""
        self.priority = 0
        self.insert = 0
        self.level: int | None = None
        self.started = 0.0
        self._world: World = world
        self._loop: Loop = loop
        self.corpse_id: int | None = None
        self.where: tuple[float, float, float] | None = None
        self.partner = 0
        self.merchant_id = 0
        self.merchant_zone = ""
        self.merchant_point: tuple[float, float, float] | None = None
        self.count = 0
        self.zone = ""
        self.durable = False
        self.complete = False
        self.suspended = True
        self.yielding = False
        self.messages: list[EQStruct] = []
        self.waiting: list[str] = []
        self.target_id = 0
        self.item_id = 0
        self.spawn_id: int | None = None
        self.task_text = ""
        self.name = ""
        self.description = ""
        self.active_path: Path | None = None
        self.active_path_dest: tuple[float, float, float] | Mob | None = None
        self._gem_recast: dict[int, int] = {}
        self.limit: int | None = None
        self.consider_sent = False
        self.target_sent = False
        self.mob_targeted = 0
        self.waited = 0
        self.zoneline: tuple[float, float, float] | None = None
        self.zoneline_dest: str | None = None

    def _hear(self) -> None:
        return

    def step(self) -> None:
        if not self.target_id:
            return

        mob = self._world.mobs.find_mob(self.target_id)
        if not mob:
            return

        if self.mob_targeted != self.target_id:
            self.wait("TARGET")

        if not self.can_see_mob(mob):
            return

        if mob.is_treasure and float(mob.distance) > 25:
            self.move_closer(mob)
            return

        if not self.target_sent:
            self._loop.send(
                "OP_TargetMouse", OP_TargetMouse(int(self.target_id) & 65535).serialize()
            )
            self.target_sent = True
            return

        if not self.consider_sent:
            spawn = int(self._world.self_id or 0)
            self._loop.send(
                "OP_Consider",
                OP_Consider(spawn, int(mob.id)).serialize(),
            )
            self.consider_sent = True
            return

        message = self.consume(
            "OP_Consider",
            lambda message: _consider_id(message) == int(self.target_id),
        )
        if message:
            mob.targeted = True
            self.mob_targeted = self.target_id
            self.unwait("TARGET")
            self.consider_sent = False
            self.target_sent = False
            return

    def can_see_mob(self, mob: Mob) -> bool:
        if self._world.line_of_sight(mob):
            return True
        self.move_closer(mob)
        return False

    def wait(self, kind: str) -> None:
        pending = self._pending()
        if kind not in pending:
            pending.append(kind)

    def unwait(self, kind: str) -> None:
        pending = self._pending()
        if kind in pending:
            pending.remove(kind)

    def waiting_for(self, kind: str) -> bool:
        return kind in self._pending()

    def wait_label(self) -> str:
        return ",".join(self._pending())

    def _pending(self) -> list[str]:
        pending = self.waiting
        if isinstance(pending, list):
            return pending
        if isinstance(pending, str) and pending:
            self.waiting = [pending]
            return self.waiting
        self.waiting = []
        return self.waiting

    def consume(
        self, opcode: str, match: Callable[[EQStruct], bool] | None = None
    ) -> EQStruct | None:
        for index, message in enumerate(self.messages):
            if message.opcode != opcode:
                continue
            if match and not match(message):
                continue
            return self.messages.pop(index)
        return None

    @property
    def completed(self) -> bool:
        return self.complete

    def add_message(self, payload: EQStruct) -> None:
        self.messages.append(payload)

    def suspend(self) -> None:
        self.suspended = True

    def opcodes(self) -> tuple[str, ...]:
        return ("OP_Consider",)

    @staticmethod
    def key(action: Action) -> tuple[object, ...]:
        # Within one band, smaller runs first. Newest insert is the default.
        return (-action.insert,)

    def forget(self) -> None:
        self._loop.queue.remove(self.insert)
        self._loop.journal.clear_source(self.source)

    def yield_to(self, new: Action, source: str = "") -> bool:
        """Queue the next piece of work. Same-band handoff waits until the next pulse."""
        if source:
            new.source = source

        if not self._loop.queue.append(new):
            return False

        self.yielding = True
        return True

    def move_closer(self, dest: tuple[float, float, float] | Mob, mode: str = "run") -> None:
        if not self.active_path or self.active_path_dest != dest:
            self.active_path = self._world.movement.plan(dest, mode)
            self.active_path_dest = dest
        self._world.movement.advance(self._loop, self.active_path)

    def next_zoneline(self, destination: str) -> tuple[float, float, float] | None:
        """Where to walk to leave this zone toward `destination`.

        A saved zoneline wins. Otherwise the zone graph's next transit. A zone
        with no graph hop, such as tutorialb, walks to the one scripted exit door.
        """

        # Cached
        if destination == self.zoneline_dest:
            return self.zoneline

        self.zoneline_dest = destination

        here = (self._world.zone or "").lower()
        dest = (destination or "").lower()
        leg = first_leg(self._world.zone_graph, here, dest)
        if leg:
            spot = self._transit_point(leg.zone, leg.door_id, leg.dest)
            if spot:
                self.zoneline = spot
                return spot

        self.zoneline = self._script_exit(here, dest)
        return self.zoneline

    def _transit_point(
        self,
        zone: str,
        door_id: int,
        dest: str = "",
    ) -> tuple[float, float, float] | None:
        transit = self._world.zone_graph.transit_at(zone, door_id)
        if transit and (transit.x or transit.y or transit.z):
            return (transit.x, transit.y, transit.z)

        arrived = self._return_landing(zone, dest)
        if arrived:
            return arrived

        return self._door_point(door_id)

    def _return_landing(self, here: str, dest: str) -> tuple[float, float, float] | None:
        """A zone point stored with no origin. The reverse hop's landing is that point."""
        home = (here or "").lower()
        target = (dest or "").lower()
        if not home or not target:
            return None

        for transit in self._world.zone_graph.transits_from(target):
            if transit.dest != home:
                continue
            if transit.dest_x or transit.dest_y or transit.dest_z:
                return (transit.dest_x, transit.dest_y, transit.dest_z)

        return None

    def _script_exit(self, here: str, destination: str) -> tuple[float, float, float] | None:
        """The live door a quest script uses to leave, when the zone graph has no hop."""
        exits = self._world.exit_doors.get(here, {})
        if not exits:
            return None

        dest_id = self._world.zone_graph.zones.get(destination, 0)

        chosen = 0
        if dest_id:
            for door_id, targets in exits.items():
                if dest_id in targets:
                    chosen = door_id
                    break

        if not chosen and len(exits) == 1:
            chosen = next(iter(exits))

        if not chosen:
            return None

        return self._door_point(chosen)

    def _door_point(self, door_id: int) -> tuple[float, float, float] | None:
        door = self._world.doors.get(door_id)
        if door is None and door_id < 256:
            for live in self._world.doors.values():
                if live.id % 256 == door_id:
                    door = live
                    break

        if door is None:
            return None

        return (door.x, door.y, door.z)

    def exit_kind(self, destination: str) -> str:
        """How the next hop leaves: door, stone, or point. Empty when the graph has no hop."""
        graph = self._world.zone_graph

        leg = first_leg(graph, (self._world.zone or "").lower(), (destination or "").lower())
        if not leg:
            return ""
        transit = graph.transit_at(leg.zone, leg.door_id)
        if not transit:
            return ""
        return transit.via

    def painted_line(self, anchor: tuple[float, float, float]) -> tuple[float, float, float] | None:
        """A watermap zone-line sample near a zone point. Outdoor lines are volumes, not the row."""
        if not self._world.zone:
            return None
        water = self._world.get_water_map(self._world.zone)
        if not water:
            return None
        if water.in_zone_line(anchor[0], anchor[1], anchor[2]):
            return anchor
        here = self._world.position
        return water.nearest_zone_line(here[0], here[1], here[2], anchor=anchor, reach=300, step=10)
