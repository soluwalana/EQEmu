"""Band 0. Obtain a count of an item. A drop in another zone is Travel, not Zone."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import World

from eqclient3.action import Action
from eqclient3.actions.kill import Kill
from eqclient3.actions.level_gate import hold_for_level
from eqclient3.actions.shop import ShopOffer, choose_offer
from eqclient3.actions.pickup import Pickup
from eqclient3.actions.support import (
    FetchDrop,
    FetchMerchant,
    fetch_plan,
    forget,
    has_soulbind,
    in_tutorial,
    yield_to,
    walk,
)
from eqclient3.actions.talk import Talk, append_soulbind, hail_name
from eqclient3.actions.trade import Trade
from eqclient3.actions.travel import Travel
from eqclient3.actions.zone import Zone
from eqclient3.camps import grind_zones
from eqclient3.data.merchants import MerchantBook, _norm_name, read_merchants

# Worn before a camp. A shop window is 210. The camp and its road are 0.
GEAR_BAND = 50


class Fetch(Action):

    def __init__(self, item_id: int, count: int, task_text: str, copper: int = 0) -> None:
        super().__init__()
        self.priority = 0
        self.durable = True
        self.item_id = item_id
        self.count = count
        self.task_text = task_text
        self.copper = copper
        self.active_path = None

    def __setstate__(self, state: dict[str, object]) -> None:
        self.__dict__.update(state)
        if "copper" in self.__dict__:
            return
        paid = state.get("gold")
        self.copper = paid if isinstance(paid, int) else 0

    def opcodes(self) -> tuple[str, ...]:
        return ()

    def suspend(self) -> None:
        self.active_path = None
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        self.suspended = False
        source = str(self.source or "")
        if _is_gear(source, str(self.task_text)):
            self.priority = GEAR_BAND
        if in_tutorial(world) and self.task_text.startswith("gear "):
            forget(loop, world, self)
            return
        if self.item_id == 0 and self.copper:
            if _copper(world.coin) < self.copper:
                self._earn(loop, world)
                return
            self.complete = True
            return
        if self.copper and _copper(world.coin) < self.copper:
            if in_tutorial(world):
                return
            self._earn(loop, world)
            return
        if self.item_id == 0:
            if hail_name(self.task_text):
                yield_to(
                    self,
                    loop,
                    world,
                    Talk(0, "hail", self.task_text),
                    f"hail:{hail_name(self.task_text).lower()}",
                )
                self.complete = True
                return
        if world.held(self.item_id) >= self.count:
            self.complete = True
            return
        plan = fetch_plan(world, self.item_id)
        drop = plan.drop
        if drop is not None and (not has_soulbind(loop, world)):
            if append_soulbind(self, loop, world):
                return
        quest = plan.quest
        if quest:
            self._chain(loop, world, quest, f"quest:{self.item_id}")
            return
        merchant = plan.merchant
        if merchant is not None and _here(world, merchant.zone):
            price = item_cost(self.item_id)
            if price and _copper(world.coin) < price:
                self.copper = price
                if in_tutorial(world):
                    return
                self._earn(loop, world)
                return
            opened = Trade(merchant.npc, self.item_id)
            opened.merchant_zone = str(merchant.zone or "")
            if yield_to(self, loop, world, opened, f"trade:{self.item_id}"):
                return
            return
        ground = plan.ground
        if ground is not None and _here(world, ground.zone):
            yield_to(
                self,
                loop,
                world,
                Pickup(ground.drop_id, ground.point),
                f"pickup:{ground.drop_id}",
            )
            return
        if drop is not None and _near_level(drop, world):
            self._drop(loop, world, drop)
            return
        vendor_zone = plan.vendor_zone or plan.station_zone
        if vendor_zone and vendor_zone != world.zone:
            if in_tutorial(world):
                return
            yield_to(self, loop, world, Zone(vendor_zone), f"{self.source}#zone:{vendor_zone}")
            return
        station = plan.station or world.station
        if station is None:
            if self._shop(loop, world):
                return
            if drop is not None:
                self._drop(loop, world, drop)
            return
        walk(self, loop, world, station, "run")

    def _chain(
        self,
        loop: Loop,
        world: World,
        quest: list[Action] | tuple[Action, ...] | Action,
        source: str,
    ) -> None:
        rows = list(quest) if isinstance(quest, (list, tuple)) else [quest]
        pushed = False
        for index, action in enumerate(rows):
            if yield_to(self, loop, world, action, action.source or f"{source}:{index}"):
                pushed = True
        if pushed:
            self.yielding = True

    def _drop(self, loop: Loop, world: World, drop: FetchDrop) -> None:
        zone = drop.zone
        if drop.above_level:
            camp = drop.camp
            level = drop.level
            yield_to(
                self,
                loop,
                world,
                Kill(camp=camp, level=level),
                f"kill:camp:{self.item_id}",
            )
            return
        if zone and zone != world.zone:
            yield_to(self, loop, world, Travel(zone), f"travel:{zone}")
            return
        queue = loop.queue
        for spawn_id in drop.spawns:
            if queue is not None and any(isinstance(action, Kill) and action.spawn_id == spawn_id for action in queue):
                continue
            yield_to(self, loop, world, Kill(spawn_id=spawn_id), f"kill:{spawn_id}")

    def _earn(self, loop: Loop, world: World) -> None:
        if in_tutorial(world):
            return
        level = max(int(world.level or 1), 1)
        zones = grind_zones(level)
        here = (world.zone or "").lower()
        if here not in zones:
            if not zones:
                return
            zone = zones[0]
            source = f"{self.source}#gold:travel:{zone}"
            if _open(loop, source):
                self.yielding = True
                return
            yield_to(self, loop, world, Travel(zone), source)
            return
        target = level + 1
        source = f"{self.source}#gold:kill:{here}:{target}"
        if _open(loop, source):
            self.yielding = True
            return
        yield_to(self, loop, world, Kill(camp=here, level=target), source)

    def _shop(self, loop: Loop, world: World) -> bool:
        offer = choose_offer(world, self.item_id, _merchant_book())
        if offer is not None:
            self._visit(loop, world, offer)
            return True
        later = world.later_shops.get(self.item_id)
        if later is None:
            return False
        if later.copper and _copper(world.coin) < later.copper:
            self.copper = later.copper
            self._earn(loop, world)
            return True
        hold_for_level(self, loop, world, later.blocked_zone)
        return True

    def _visit(self, loop: Loop, world: World, offer: ShopOffer) -> None:
        if offer.copper and _copper(world.coin) < offer.copper:
            self.copper = offer.copper
            self._earn(loop, world)
            return
        self._buy(loop, world, FetchMerchant(npc=offer.npc_id, zone=offer.zone))

    def _buy(self, loop: Loop, world: World, seller: FetchMerchant) -> None:
        """Walk to the merchant who stocks this, then buy it from the live spawn."""
        if seller.zone and not _here(world, seller.zone):
            source = f"{self.source}#travel"
            if _open(loop, source):
                self.priority = 0
                self.yielding = True
                return
            if yield_to(self, loop, world, Travel(seller.zone), source):
                self.priority = 0
            return
        spawn = _spawned(world, seller)
        if not spawn:
            return
        source = f"trade:{self.item_id}"
        if _open(loop, source):
            self.priority = 0
            self.yielding = True
            return
        opened = Trade(spawn, self.item_id)
        opened.merchant_zone = seller.zone
        if yield_to(self, loop, world, opened, source):
            self.priority = 0


def _is_gear(source: str, task_text: str) -> bool:
    return task_text.startswith("gear ") or source.startswith("gear:")


def _near_level(drop: FetchDrop, world: World) -> bool:
    """A drop from a camp at this level is farmed. A camp above us is bought when it is sold."""
    if drop.above_level:
        return False
    level = int(world.level or 1)
    if drop.level is None:
        return True
    return drop.level <= level + 2


def _spawned(world: World, merchant: FetchMerchant) -> int:
    book = _merchant_book()
    if book is None:
        return 0
    row = book.by_npc.get(merchant.npc)
    if not row:
        return 0
    name = _norm_name(str(row.get("name") or ""))
    if not name:
        return 0
    for mob in world.mobs.values():
        if mob.dead:
            continue
        if _norm_name(mob.spoken_name()) == name:
            return int(mob.id)
    return 0


def _here(world: World, zone: str) -> bool:
    return not zone or zone == world.zone


def _copper(coin: tuple[int, int, int, int] | None) -> int:
    if coin is None:
        return 0
    platinum, gold, silver, copper = coin
    return platinum * 1000 + gold * 100 + silver * 10 + copper


def _open(loop: Loop, source: str) -> bool:
    queue = loop.queue
    if queue is None:
        return False
    for queued in queue:
        if queued.source == source and not queued.complete:
            return True
    return False


_book: MerchantBook | None = None
_loaded = False


def item_cost(item_id: int) -> int:
    """Copper price from the merchant book, or 0 when the item is not sold."""
    if item_id <= 0:
        return 0
    book = _merchant_book()
    if book is None:
        return 0
    return book.cost(item_id)


def _merchant_book() -> MerchantBook | None:
    global _book, _loaded
    if _loaded:
        return _book
    _loaded = True
    path = Path.home() / ".eqclient" / "merchants.jsonl"
    if not path.is_file():
        return None
    _book = read_merchants(str(path))
    return _book
