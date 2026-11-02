"""Band 0. Walk to the next zoneline. Completes when the world zone is the destination."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import World


from eqclient3.action import Action
from eqclient3.actions.level_gate import hold_for_level
from eqclient3.actions.support import (
    exit_kind,
    forget,
    in_tutorial,
    next_zoneline,
    painted_line,
    session_open,
    walk,
    zone_id,
    zone_packet,
)
from eqclient3.log import log


class Travel(Action):
    def __init__(self, destination: str) -> None:
        super().__init__()
        self.priority = 0
        self.durable = True
        self.destination = destination
        self.active_path = None

    def opcodes(self) -> tuple[str, ...]:
        return ("OP_NewZone",)

    def suspend(self) -> None:
        self.active_path = None
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        if in_tutorial(world) and "#gold:" in (self.source or ""):
            forget(loop, world, self)
            return
        if world.zone == self.destination:
            self.complete = True
            return
        if hold_for_level(self, loop, world, self.destination):
            return
        self.suspended = False
        point = next_zoneline(world, self.destination)
        if point is None:
            return
        if exit_kind(world, self.destination) == "point":
            painted = painted_line(world, point)
            if painted is not None:
                point = painted
            if self._crossing(loop, world, point):
                return
        self._drop_stale_path(point)
        if not self.active_path:
            walk(self, loop, world, point, "run")
            return
        self.suspended = False
        world.movement.advance(loop, world, self.active_path)

    def _drop_stale_path(self, point: tuple[float, float, float]) -> None:
        path = self.active_path
        if path is None:
            return
        dest = path.destination
        if (dest[0] - point[0]) ** 2 + (dest[1] - point[1]) ** 2 > 400.0:
            self.active_path = None

    def _crossing(self, loop: Loop, world: World, point: tuple[float, float, float]) -> bool:
        """A zone point zones when we ask from the painted line. Doors do not."""
        if self.waiting_for("ZONE"):
            if world.zone == self.destination or self.consume("OP_NewZone"):
                self.complete = True
                return True
            self.waited += 1
            if self.waited < 40:
                return True
            self.unwait("ZONE")
            self.waited = 0
        here = world.position
        if (here[0] - point[0]) ** 2 + (here[1] - point[1]) ** 2 > 625.0:
            return False
        if not session_open(loop):
            return True
        dest_id = zone_id(self.destination)
        if not dest_id:
            return False
        log.info(
            "zone line %s -> %s (%s) at (%.0f, %.0f, %.0f)",
            world.zone,
            self.destination,
            dest_id,
            here[0],
            here[1],
            here[2],
        )
        loop.send("OP_ZoneChange", zone_packet(self.destination, dest_id, here[0], here[1], here[2]))
        self.wait("ZONE")
        self.waited = 0
        self.active_path = None
        return True
