"""Band 0. Open the merchant and sell one stack. The window slot is the bag slot."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import World

from eqclient3.action import Action
from eqclient3.structs import OP_ShopPlayerSell, OP_ShopRequest
from eqclient3.actions.support import (
    INTERACT,
    bag_slot,
    yield_to,
    take_refusal,
    walk,
    yards,
)
from eqclient3.actions.zone import Zone


class Sell(Action):

    def __init__(self, item_ids: list[int]) -> None:
        super().__init__()
        self.priority = 0
        self.durable = True
        self.item_ids = [int(item) for item in item_ids]
        self.active_path = None
        self.window = False
        self.merchant_id = 0
        self.slots: dict[int, tuple[int, int]] = {}
        self.merchant_zone = ""
        self.merchant_point: tuple[float, float, float] | None = None

    def opcodes(self) -> tuple[str, ...]:
        return ("OP_ItemPacket", "OP_DeleteItem", "OP_SimpleMessage")

    def suspend(self) -> None:
        self.active_path = None
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        self.suspended = False
        if take_refusal(self):
            self.complete = True
            return
        self.consume("OP_ItemPacket")
        self.consume("OP_DeleteItem")
        if not any((world.held(item_id) > 0 for item_id in self.item_ids)):
            self.complete = True
            return
        zone = self.merchant_zone
        if zone and zone != world.zone:
            yield_to(self, loop, world, Zone(zone), f"zone:{zone}")
            return
        point = self.merchant_point
        if point is not None and yards(world, point) > INTERACT:
            walk(self, loop, world, point, "run")
            return
        npc = int(self.merchant_id or 0)
        if not self.window:
            loop.send(
                "OP_ShopRequest",
                OP_ShopRequest(int(npc), int(world.self_id or 0), 1).serialize(),
            )
            self.window = True
            return
        for item_id in self.item_ids:
            slot = bag_slot(world, item_id)
            if slot is None:
                continue
            loop.send(
                "OP_ShopPlayerSell",
                OP_ShopPlayerSell(int(npc), int(slot), 1).serialize(),
            )
            return
