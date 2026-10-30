"""Trade requests are acked when a Trade is open, and cancelled when it is not.

A shop close completes that Trade. The deeds line is messages.py, not this packet.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.action import Action

from eqclient3.handlers.common import queue_of
from eqclient3.structs import (
    EQStruct,
    OP_CancelTrade,
    OP_ShopRequest,
    OP_TradeRequest,
    OP_TradeRequestAck,
)
from eqclient3.handler import Handler

CLOSE = 0


class TradeHandler(Handler):
    opcodes = ("OP_TradeRequest", "OP_ShopRequest")

    def on(self, opcode: str, payload: EQStruct) -> None:
        del opcode
        if isinstance(payload, OP_TradeRequest):
            self.request(payload)
        elif isinstance(payload, OP_ShopRequest):
            self.shop(payload)

    def request(self, row: OP_TradeRequest) -> None:
        to_id, from_id = row.to_id, row.from_id
        loop = self.loop
        trade = self.open_trade()
        if trade:
            loop.send("OP_TradeRequestAck", OP_TradeRequestAck(from_id, to_id).serialize())
            return
        loop.send("OP_CancelTrade", OP_CancelTrade(from_id, 1).serialize())

    def shop(self, row: OP_ShopRequest) -> None:
        npc, command = row.npc_id, row.command
        shops = self.open_shops()
        if command == CLOSE:
            for action in shops:
                if type(action).__name__ == "Trade":
                    action.complete = True
            return
        world = self.world
        zone = str(world.zone or "")
        point = self.merchant_point(npc)
        for action in shops:
            action.merchant_id = npc
            action.merchant_zone = zone
            action.merchant_point = point

    def merchant_point(self, npc: int) -> tuple[float, float, float]:
        world = self.world
        mobs = world.mobs
        mob = mobs.get(npc) if mobs else None
        if mob:
            return mob.position
        return (world.x, world.y, world.z)

    def open_shops(self) -> list[Action]:
        opened = []
        for action in queue_of(self.loop):
            if action.complete:
                continue
            if type(action).__name__ in ("Trade", "Sell"):
                opened.append(action)
        return opened

    def open_trade(self) -> Action | None:
        for action in self.open_shops():
            if type(action).__name__ == "Trade":
                return action
        return None
