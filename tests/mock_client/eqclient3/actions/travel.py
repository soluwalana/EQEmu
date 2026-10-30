"""Band 0. Walk to the next zoneline. Completes when the world zone is the destination."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import World


from eqclient3.action import Action
from eqclient3.actions.support import next_zoneline, walk


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
        if world.zone == self.destination:
            self.complete = True
            return
        self.suspended = False
        point = next_zoneline(world, self.destination)
        if point is None:
            return
        if not self.active_path:
            walk(self, loop, world, point, "run")
            return
        self.suspended = False
        world.movement.advance(loop, world, self.active_path)
