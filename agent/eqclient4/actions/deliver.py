"""Band 210. Hand the item to the npc. A missing item completes it. Never appends Fetch."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient4.loop import Loop
    from eqclient4.world import World

from eqclient4.action import Action
from eqclient4.actions.talk import Talk
from eqclient4.log import log


class Deliver(Action):
    def __init__(self, item: int, npc: int | str) -> None:
        super().__init__()
        self.priority = 210
        self.durable = True
        self.item = item
        self.npc = npc
        self.handed = False

    def step(self, loop: Loop, world: World) -> None:
        self.suspended = False

        item_id = int(self.item)

        # Don't have the item so can't deliver it
        if self._world.inventory.held(item_id) <= 0:
            log.error(f"Not holding item {item_id} to deliver to {self.npc}")
            self.complete = True
            return

        if not self.handed:
            npc = int(self.npc) if isinstance(self.npc, int) else 0
            talk = Talk(npc, "hail", str(item_id))
            talk.source = f"hand:{item_id}:{self.npc}"
            self.yield_to(talk)
            self.handed = True
            return
        self.complete = True
