"""Band 0. Camp until the world reaches a level, at whichever open XP camp we are in."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import World

from eqclient3.action import Action
from eqclient3.actions.kill import Kill
from eqclient3.actions.support import next_zoneline, walk, yield_to
from eqclient3.camps import grind_zones


class Grind(Action):
    def __init__(self, level: int) -> None:
        super().__init__()
        self.priority = 0
        self.durable = True
        self.level = int(level)
        self.camp = ""
        self.active_path = None

    def opcodes(self) -> tuple[str, ...]:
        return ()

    def suspend(self) -> None:
        self.active_path = None
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        target = int(self.level or 0)
        if int(world.level or 0) >= target:
            self.complete = True
            return
        self.suspended = False
        zones = grind_zones(int(world.level or 1))
        if not zones:
            return
        here = (world.zone or "").lower()
        if here in zones:
            self.camp = here
            self.active_path = None
            source = f"{self.source}#kill:{here}"
            if _open(loop, source):
                self.yielding = True
                return
            yield_to(self, loop, world, Kill(camp=here, level=target), source)
            return
        zone = zones[0]
        if self.camp != zone:
            self.camp = zone
            self.active_path = None
        point = next_zoneline(world, zone)
        if point is None:
            return
        if not self.active_path:
            walk(self, loop, world, point, "run")
            return
        world.movement.advance(loop, world, self.active_path)


def _open(loop: Loop, source: str) -> bool:
    queue = loop.queue
    if queue is None:
        return False
    for queued in queue:
        if queued.source == source and not queued.complete:
            return True
    return False
