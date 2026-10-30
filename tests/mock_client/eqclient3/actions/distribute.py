"""Band 220. Empty the worn slots, then one give. The bag leaving the item finishes it."""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import World

from eqclient3.action import Action
from eqclient3.actions.support import (
    delete_slot,
    item_of,
    send_command,
    set_worn,
    worn_map,
)


class Distribute(Action):

    def __init__(self, item: int, bot: str, slots: Sequence[int]) -> None:
        super().__init__()
        self.priority = 220
        self.durable = True
        self.item = item
        self.bot = bot
        self.slots = list(slots)
        self.removed: set[int] = set()
        self.gave = False

    def opcodes(self) -> tuple[str, ...]:
        return ("OP_ItemPacket", "OP_DeleteItem")

    def suspend(self) -> None:
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        self._inbox(loop, world)
        item_id = int(self.item if isinstance(self.item, int) else self.item.item_id or 0)
        if item_id and world.held(item_id) <= 0 and (self.gave or self.removed):
            slot = self.slots[-1] if self.slots else 0
            set_worn(loop, world, self.bot, int(slot), item_id)
            self.complete = True
            return
        self.suspended = False
        worn = worn_map(loop, world, self.bot)
        for slot in self.slots:
            if int(slot) in self.removed:
                continue
            if int(worn.get(int(slot), 0) or 0) == 0:
                continue
            send_command(loop, f"^inventoryremove {int(slot)} byname {self.bot}")
            return
        send_command(loop, f"^inventorygive byname {self.bot}")
        self.gave = True

    def _inbox(self, loop: Loop, world: World) -> None:
        deleted = self.consume("OP_DeleteItem")
        if deleted is not None:
            slot = delete_slot(deleted)
            if slot in self.slots or slot < 0:
                if slot >= 0:
                    self.removed.add(int(slot))
                    set_worn(loop, world, self.bot, int(slot), 0)
        item = self.consume("OP_ItemPacket")
        if item is None:
            return
        parsed = item_of(item)
        if parsed is None:
            return
        item_id = int(self.item if isinstance(self.item, int) else self.item.item_id or 0)
        if int(parsed.item_id or 0) == item_id and int(parsed.slot) < 0:
            return
