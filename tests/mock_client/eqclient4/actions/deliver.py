"""Band 210. Hand the item to the npc. A missing item completes it. Never appends Fetch."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient4.loop import Loop
    from eqclient4.world import World


from eqclient4.action import Action
from eqclient4.actions.support import yield_to
from eqclient4.actions.talk import Talk


class Deliver(Action):
    def __init__(self, item: int, npc: int | str) -> None:
        super().__init__()
        self.priority = 210
        self.durable = True
        self.item = item
        self.npc = npc
        self.handed = False

    def opcodes(self) -> tuple[str, ...]:
        return ()

    def suspend(self) -> None:
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        self.suspended = False
        item_id = int(self.item)
        if world.held(item_id) <= 0:
            self.complete = True
            return
        if not self.handed:
            npc = int(self.npc) if isinstance(self.npc, int) else 0
            talk = Talk(npc, "hail", str(item_id))
            yield_to(self, loop, world, talk, f"hand:{item_id}:{self.npc}")
            self.handed = True
            return
        self.complete = True
