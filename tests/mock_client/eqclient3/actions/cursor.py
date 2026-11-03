"""Band 350. A fresh move is sent once. The token, the real item, or a delete finishes it.

A move the server accepts has no reply. Silence lands it. A reply that puts the
item back on the source, or deletes the destination, refuses that slot.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.action import Message
    from eqclient3.loop import Loop
    from eqclient3.world import World

from eqclient3.action import Action
from eqclient3.structs import OP_MoveItem
from eqclient3.actions.support import CURSOR_SLOT, TOKEN, delete_slot, item_of


class Cursor(Action):

    def __init__(self, slot: int, move: tuple[int, int] | None = None) -> None:
        super().__init__()
        self.priority = 350
        self.durable = True
        self.slot = int(slot)
        self.move = move
        self.sent = False
        self.outstanding = True
        self.limit = 10

    def opcodes(self) -> tuple[str, ...]:
        return ("OP_ItemPacket", "OP_DeleteItem")

    def suspend(self) -> None:
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        if self.move and not self.sent:
            # A loot packet already in the mailbox is the item arriving, not a refusal.
            while self.consume("OP_ItemPacket") is not None:
                pass
            while self.consume("OP_DeleteItem") is not None:
                pass

            world.cursor_move = self.move
            loop.send("OP_MoveItem", OP_MoveItem(self.move[0], self.move[1]).serialize())
            self.sent = True
            self.outstanding = True
            self.wait("CURSOR")
            self.suspended = False
            return

        message = self.consume("OP_ItemPacket") or self.consume("OP_DeleteItem")
        if self.sent and message is not None and self._returned(world, message):
            self._reject(world)
            return

        if self.waiting_for("CURSOR") and message is None:
            self.waited += 1
            if self.limit is None or self.waited < self.limit:
                return

            self.waited = 0
            if self.sent:
                self._accept(world)
                return

            self._retry(loop, world)
            return

        if message is not None and self._finishes(message):
            self._write(world, message)
            self.unwait("CURSOR")
            self.waited = 0
            self.outstanding = False
            self.complete = True
            return

        self.wait("CURSOR")
        self.suspended = False

    def _finishes(self, message: Message) -> bool:
        if message.opcode == "OP_DeleteItem":
            return delete_slot(message) == self.slot
        item = item_of(message)
        if item is None:
            return False
        slot = int(item.slot)
        item_id = int(item.item_id or 0)
        if item_id == TOKEN:
            return False
        return slot == self.slot

    def _write(self, world: World, message: Message) -> None:
        bags = world.bags
        if message.opcode == "OP_DeleteItem":
            bags.pop(self.slot, None)
            if world.cursor == TOKEN:
                world.cursor = None
            return
        item = item_of(message)
        if item is None:
            return
        item_id = item.item_id
        if item_id and item_id != TOKEN:
            bags[self.slot] = item_id
        if world.cursor == TOKEN:
            world.cursor = None

    def _returned(self, world: World, message: Message) -> bool:
        """The server did not take the move. The source still has the item, or the destination was cleared."""
        move = self.move or world.cursor_move
        if not move:
            return False
        src, dest = int(move[0]), int(move[1])
        if message.opcode == "OP_DeleteItem":
            return delete_slot(message) == dest
        item = item_of(message)
        if item is None:
            return False
        item_id = int(item.item_id or 0)
        if item_id in (0, TOKEN):
            return False
        return int(item.slot) == src

    def _reject(self, world: World) -> None:
        """The server did not confirm the move. The destination stays empty and is not tried again."""
        move = self.move or world.cursor_move
        if move:
            world.refused_slots.add(int(move[1]))

        self.unwait("CURSOR")
        self.outstanding = False
        self.complete = True

    def _accept(self, world: World) -> None:
        """A sent move that the server did not refuse landed. Record it and stop."""
        move = self.move or world.cursor_move
        if not move:
            return
        src, dest = move
        bags = world.bags
        item_id = world.cursor if src == CURSOR_SLOT else bags.get(src)
        if item_id and item_id != TOKEN:
            bags[dest] = item_id
        if src == CURSOR_SLOT or world.cursor == item_id:
            world.cursor = None
            bags.pop(CURSOR_SLOT, None)
        if src != dest:
            bags.pop(src, None)
        self.unwait("CURSOR")
        self.outstanding = False
        self.complete = True

    def _retry(self, loop: Loop, world: World) -> None:
        move = world.cursor_move
        if not move:
            return
        src, dest = (int(move[0]), int(move[1]))
        loop.send("OP_MoveItem", OP_MoveItem(int(src), int(dest)).serialize())
        self.outstanding = True
        self.wait("CURSOR")
        self.suspended = False


def cursor_slot() -> int:
    return CURSOR_SLOT
