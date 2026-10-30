"""Band 210. Request, move the item onto the cursor, accept, then wait for the close.

A buy uses the merchant window slot, not a bag index.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import World


from eqclient3.action import Action
from eqclient3.structs import OP_MoveItem, OP_ShopPlayerBuy, OP_ShopRequest, OP_TradeAcceptClick, OP_TradeRequest
from eqclient3.actions.support import CURSOR_SLOT, bag_slot, merchant_offer, take_refusal


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

    def opcodes(self) -> tuple[object, ...]:
        return ("OP_TradeRequest", "OP_FinishTrade", "OP_SimpleMessage")

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
            self.complete = True
            return
        self.suspended = False
        offer = merchant_offer(self, int(self.item))
        if offer is not None:
            slot, price = offer
            if not self.requested:
                loop.send("OP_ShopRequest", OP_ShopRequest(int(self.partner), int(world.self_id or 0), 1).serialize())
                self.requested = True
                return
            loop.send(
                "OP_ShopPlayerBuy",
                OP_ShopPlayerBuy(int(self.partner), int(world.self_id or 0), int(slot), quantity=1, price=int(price)).serialize(),
            )
            self.accepted = True
            self.wait("TRADE")
            return
        if not self.requested:
            loop.send("OP_TradeRequest", OP_TradeRequest(int(self.partner), int(world.self_id or 0)).serialize())
            self.requested = True
            return
        if world.cursor != int(self.item):
            src = bag_slot(world, int(self.item))
            if src is None:
                return
            loop.send("OP_MoveItem", OP_MoveItem(int(src), CURSOR_SLOT).serialize())
            return
        loop.send("OP_TradeAcceptClick", OP_TradeAcceptClick().serialize())
        self.accepted = True
        self.wait("TRADE")
