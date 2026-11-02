"""Band 0. Walk to a ground spawn and click it. The bag or a cleared drop finishes it."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import World

from eqclient3.action import Action
from eqclient3.structs import OP_ClickObject
from eqclient3.actions.support import INTERACT, walk, yards


class Pickup(Action):

    def __init__(self, drop_id: int, point: tuple[float, float, float]) -> None:
        super().__init__()
        self.priority = 0
        self.drop_id = int(drop_id)
        self.point = point
        self.active_path = None
        self.clicked = False
        self.item_id = 0

    def opcodes(self) -> tuple[str, ...]:
        return ()

    def suspend(self) -> None:
        self.active_path = None
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        self.suspended = False
        gone = self.drop_id not in (world.ground or {})
        held = bool(self.item_id) and world.held(self.item_id) > 0
        if gone or held:
            self.complete = True
            return
        if yards(world, self.point) > INTERACT:
            walk(self, loop, world, self.point, "run")
            return
        if not self.clicked:
            loop.send(
                "OP_ClickObject",
                OP_ClickObject(int(self.drop_id), int(world.self_id or 0)).serialize(),
            )
            self.clicked = True
            self.waited = 0
            return
        self.waited += 1
        if self.waited < 20:
            return
        row = world.ground.get(self.drop_id)
        if row is not None:
            row.used = True
        self.complete = True
