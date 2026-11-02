"""Band 210. Request, put the item in the trade window, accept, then wait for the close.

The pickup and the window move are each sent once. Silence means the server took
the move. Accepting while the window is empty closes it and leaves the item behind.
A buy uses the merchant window slot, not a bag index.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import World


from eqclient3.action import Action
from eqclient3.structs import (
    OP_MoveItem,
    OP_ShopPlayerBuy,
    OP_ShopRequest,
    OP_TradeAcceptClick,
    OP_TradeRequest,
)
from eqclient3.actions.support import (
    CURSOR_SLOT,
    TOKEN,
    bag_slot,
    item_of,
    merchant_offer,
    take_refusal,
)

_QUIET = 10
# common/patches/rof2_limits.h:50 typeTrade. Slot 0 is server trade slot 3000.
_TRADE_TYPE = 3


class Trade(Action):
    def __init__(self, partner: int, item: int) -> None:
        super().__init__()
        self.priority = 210
        self.durable = True
        self.partner = partner
        self.item = item
        self.requested = False
        self.accepted = False
        self.merchant_id = int(partner or 0)
        self.slots: dict[int, tuple[int, int]] = {}
        self.merchant_zone = ""
        self.merchant_point: tuple[float, float, float] | None = None
        self.sent_move = False
        self.move_from: int | None = None
        self.sent_offer = False
        self.offered = False

    def __setstate__(self, state: dict[str, object]) -> None:
        self.__dict__.update(state)
        if "sent_move" not in self.__dict__:
            self.sent_move = False
        if "move_from" not in self.__dict__:
            self.move_from = None
        if "sent_offer" not in self.__dict__:
            self.sent_offer = False
        if "offered" not in self.__dict__:
            self.offered = False

    def opcodes(self) -> tuple[str, ...]:
        return ("OP_TradeRequest", "OP_FinishTrade", "OP_SimpleMessage", "OP_ItemPacket", "OP_DeleteItem")

    def suspend(self) -> None:
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        if self.waiting_for("TRADE") and not self.messages:
            return
        if take_refusal(self):
            self.unwait("TRADE")
            self.complete = True
            return
        if self.consume("OP_FinishTrade"):
            self.unwait("TRADE")
            if world.held(int(self.item)) > 0:
                self._reset()
                return
            self.complete = True
            return
        if self.accepted:
            self.wait("TRADE")
            return
        self.suspended = False
        offer = merchant_offer(self, int(self.item))
        if offer is not None:
            slot, price = offer
            if not self.requested:
                loop.send(
                    "OP_ShopRequest",
                    OP_ShopRequest(int(self.partner), int(world.self_id or 0), 1).serialize(),
                )
                self.requested = True
                return
            loop.send(
                "OP_ShopPlayerBuy",
                OP_ShopPlayerBuy(
                    int(self.partner),
                    int(world.self_id or 0),
                    int(slot),
                    quantity=1,
                    price=int(price),
                ).serialize(),
            )
            self.accepted = True
            self.wait("TRADE")
            return
        if not self.requested:
            loop.send(
                "OP_TradeRequest",
                OP_TradeRequest(int(self.partner), int(world.self_id or 0)).serialize(),
            )
            self.requested = True
            return
        if world.cursor != int(self.item) and not self.offered:
            if not self._hold_cursor(loop, world):
                return
        if not self.offered:
            if not self._offer(loop, world):
                return
        self.unwait("MOVE")
        loop.send("OP_TradeAcceptClick", OP_TradeAcceptClick().serialize())
        self.accepted = True
        self.wait("TRADE")

    def _reset(self) -> None:
        """The window closed with the item still held. Ask again."""
        self.accepted = False
        self.requested = False
        self.sent_move = False
        self.move_from = None
        self.sent_offer = False
        self.offered = False
        self.waited = 0

    def _offer(self, loop: Loop, world: World) -> bool:
        """Move the cursor item into the first trade cell. A stack count would kick."""
        if not self.sent_offer:
            loop.send("OP_MoveItem", OP_MoveItem(CURSOR_SLOT, 0, to_type=_TRADE_TYPE).serialize())
            self.sent_offer = True
            self.wait("MOVE")
            self.waited = 0
            return False
        self.waited += 1
        if self.waited < _QUIET:
            return False
        world.cursor = None
        world.bags.pop(CURSOR_SLOT, None)
        self.offered = True
        self.unwait("MOVE")
        return True

    def _hold_cursor(self, loop: Loop, world: World) -> bool:
        """Send one pickup. Silence lands it. The item returning to the bag sends it again."""
        if self._returned():
            self.sent_move = False
            self.unwait("MOVE")
            self.waited = 0
            return False
        if not self.sent_move:
            src = bag_slot(world, int(self.item))
            if src is None:
                if world.bags.get(CURSOR_SLOT) == int(self.item) or world.cursor == int(self.item):
                    world.cursor = int(self.item)
                    return True
                self.complete = True
                return False
            loop.send("OP_MoveItem", OP_MoveItem(int(src), CURSOR_SLOT).serialize())
            self.sent_move = True
            self.move_from = int(src)
            self.wait("MOVE")
            self.waited = 0
            return False
        self.waited += 1
        if self.waited < _QUIET:
            return False
        self._land(world)
        return True

    def _returned(self) -> bool:
        """The server answered by putting the item back where the pickup started."""
        returned = False
        while self.consume("OP_DeleteItem") is not None:
            pass
        while True:
            message = self.consume("OP_ItemPacket")
            if message is None:
                return returned
            item = item_of(message)
            if item is None or int(item.item_id) in (0, TOKEN):
                continue
            src = self.move_from
            if src is not None and int(item.slot) == src and int(item.item_id) == int(self.item):
                returned = True

    def _land(self, world: World) -> None:
        item = int(self.item)
        src = self.move_from
        if src is not None and world.bags.get(src) == item:
            world.bags.pop(src)
        world.bags[CURSOR_SLOT] = item
        world.cursor = item
        self.unwait("MOVE")
