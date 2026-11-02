"""Band 220. Empty the worn slots, then one give. The bag leaving the item finishes it.

A piece the player can wear is taken back. A give is sent once, and the bot's
acceptance finishes it.
"""

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
    line_of,
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
        self.recalled = False

    def __setstate__(self, state: dict[str, object]) -> None:
        self.__dict__.update(state)
        if "gave" not in self.__dict__:
            self.gave = False
        if "recalled" not in self.__dict__:
            self.recalled = False
        if "removed" not in self.__dict__:
            self.removed = set()

    def opcodes(self) -> tuple[str, ...]:
        return ("OP_ItemPacket", "OP_DeleteItem", "OP_ChannelMessage", "OP_SpecialMesg", "OP_SimpleMessage")

    def suspend(self) -> None:
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        self._inbox(loop, world)
        item_id = int(self.item if isinstance(self.item, int) else 0)
        heard = self._heard()
        if item_id and self._reclaim(loop, world, item_id, heard):
            return
        if "have accepted" in heard:
            slot = self.slots[-1] if self.slots else 0
            set_worn(loop, world, self.bot, int(slot), item_id)
            self.complete = True
            return
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
        if self.gave:
            return
        send_command(loop, f"^inventorygive byname {self.bot}")
        self.gave = True

    def _reclaim(self, loop: Loop, world: World, item_id: int, heard: str) -> bool:
        """The player can use this. One remove brings it back off the companion."""
        from eqclient3.inventory.assign import player_upgrade_slot

        who = str(loop.character or "")
        slot = player_upgrade_slot(world, loop.journal, who, item_id)
        if slot is None:
            return False
        if "have returned" in heard or "unequipped" in heard:
            self.complete = True
            return True
        if self.recalled:
            return True
        send_command(loop, f"^inventoryremove {int(slot)} byname {self.bot}")
        self.recalled = True
        return True

    def _heard(self) -> str:
        spoken: list[str] = []
        for opcode in ("OP_ChannelMessage", "OP_SpecialMesg", "OP_SimpleMessage"):
            while True:
                message = self.consume(opcode)
                if message is None:
                    break
                _speaker, text = line_of(message.payload)
                if text:
                    spoken.append(text)
        return " ".join(spoken).lower()

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
