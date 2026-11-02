"""Sell disposable stacks once the bags are full.

The camp is 0 and gear is 50. A sell queued because nothing else fits has to
run, or the bags stay full and the task stalls. The window slot is the bag
slot. One sale is in flight until the inventory packet or a short wait.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import Mob, World

from eqclient3.action import Action
from eqclient3.data.merchants import MerchantBook, ensure_merchants
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

SELL_BAND = 60
_RETRY = 10
_book: MerchantBook | None = None


class Sell(Action):

    def __init__(self, item_ids: list[int], keep: dict[int, int] | None = None) -> None:
        super().__init__()
        self.priority = SELL_BAND
        self.durable = True
        self.item_ids = [int(item) for item in item_ids]
        self.keep = dict(keep or {})
        self.active_path = None
        self.window = False
        self.merchant_id = 0
        self.slots: dict[int, tuple[int, int]] = {}
        self.merchant_zone = ""
        self.merchant_point: tuple[float, float, float] | None = None

    def __setstate__(self, state: dict[str, object]) -> None:
        self.__dict__.update(state)
        if "keep" not in self.__dict__:
            self.keep = {}
        self.priority = SELL_BAND

    def opcodes(self) -> tuple[str, ...]:
        return ("OP_ItemPacket", "OP_DeleteItem", "OP_SimpleMessage")

    def suspend(self) -> None:
        self.active_path = None
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        self.priority = SELL_BAND
        self.suspended = False
        if take_refusal(self):
            self.complete = True
            return
        if self.consume("OP_ItemPacket") or self.consume("OP_DeleteItem"):
            self.waited = 0
        if not any((world.held(item_id) > self.keep.get(item_id, 0) for item_id in self.item_ids)):
            self.complete = True
            return
        self._aim(world)
        zone = self.merchant_zone
        if zone and zone != world.zone:
            yield_to(self, loop, world, Zone(zone), f"zone:{zone}")
            return
        if not self.merchant_id:
            return
        point = self.merchant_point
        if point is not None and yards(world, point) > INTERACT:
            self.window = False
            self.waited = 0
            walk(self, loop, world, point, "run")
            return
        if not self.window:
            loop.send(
                "OP_ShopRequest",
                OP_ShopRequest(int(self.merchant_id), int(world.self_id or 0), 1).serialize(),
            )
            self.window = True
            return
        if self.waited:
            self.waited += 1
            if self.waited < _RETRY:
                return
            self.waited = 0
        for item_id in self.item_ids:
            if world.held(item_id) <= self.keep.get(item_id, 0):
                continue
            slot = bag_slot(world, item_id)
            if slot is None:
                continue
            loop.send(
                "OP_ShopPlayerSell",
                OP_ShopPlayerSell(int(self.merchant_id), int(slot), 1).serialize(),
            )
            self.waited = 1
            return

    def _aim(self, world: World) -> None:
        """Fill a missing seller from a live merchant in this zone."""
        if self.merchant_id:
            mob = world.mobs.get(self.merchant_id)
            if mob is not None:
                self.merchant_point = mob.position
                if not self.merchant_zone:
                    self.merchant_zone = str(world.zone or "")
            return
        seller = _nearest_seller(world)
        if seller is None:
            return
        self.merchant_id = int(seller.id)
        self.merchant_zone = str(world.zone or "")
        self.merchant_point = seller.position


def _nearest_seller(world: World) -> Mob | None:
    book = _merchants()
    zone = str(world.zone or "")
    chosen: Mob | None = None
    distance = 0.0
    for mob in world.mobs.values():
        if mob.dead:
            continue
        if not book.is_merchant_name(mob.spoken_name(), zone) and not book.is_merchant_name(mob.name, zone):
            continue
        if chosen is None or mob.distance < distance:
            chosen = mob
            distance = mob.distance
    return chosen


def _merchants() -> MerchantBook:
    global _book
    if _book is None:
        _book = ensure_merchants()
    return _book
