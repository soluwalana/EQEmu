"""Band 0. Obtain a count of an item. A drop in another zone is Travel, not Zone."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient4.world import World, Mob
    from eqclient4.loop import Loop

from eqclient4.action import Action
from eqclient4.actions.grind import LevelHoldAction
from eqclient4.actions.kill import Kill
from eqclient4.actions.pickup import Pickup

# from eqclient4.actions.shop import ShopOffer, choose_offer
# from eqclient4.actions.talk import Talk, append_soulbind, hail_name
# from eqclient4.actions.trade import Trade
from eqclient4.actions.travel import Travel
from eqclient4.actions.zone import Zone
from eqclient4.camps import grind_zones
from eqclient4.data.ground import GroundSpot, ground_at, nearest_spawn
from eqclient4.data.items import ItemStats
from eqclient4.data.locations import SpawnPoint
from eqclient4.data.merchants import Seller
from eqclient4.data.recipes import Recipe
from eqclient4.log import log
from eqclient4.nav.navmesh import load_nav
from eqclient4.utils import normalize_name


@dataclass
class FetchRequest:
    item_id: int
    count: int
    copper: int | None


class Fetch(LevelHoldAction):

    def __init__(self, world: World, loop: Loop, request: FetchRequest) -> None:
        super().__init__(world, loop)

        if not request.item_id and not request.copper:
            log.error(f"Fetch request is empty")
            self.crash()
            return

        self.priority = 0
        self.durable = True
        self.request = request
        self.item: ItemStats | None = None

        # In case it was sold out we will need to try again with the next merchant
        # If we exhaust all merchants we will need to wait until it is restocked
        # and restart the fetch process
        self.merchant: Seller | None = None
        self.merchant_history: list[Seller] = []
        self.purchase_cost: int | None = None

        # All of the in zone locations for mobs that drop this item
        # we will cycle through the campsites until we have the item
        # that we need
        self.mobs: list[Mob] = []
        self.mob_locations: list[SpawnPoint] | None = None
        self.mob_locations_index: int = 0

        # Cycle through the ground locations until we have the item that we need
        self.ground_locations: list[GroundSpot] = []
        self.ground_locations_index: int = 0

        # Recipe to try to craft
        self.recipe: Recipe | None = None

    def resolve_course(self) -> None:
        if not self.request.item_id:
            log.info(f"Not fetching an item")
            return

        if not self._world.zone:
            log.error(f"Not zoned in yet to fetch {self.request.item_id}")
            return

        self.item = self._world.item_book.get(self.request.item_id)
        if not self.item:
            log.error(f"Item {self.request.item_id} not found in item book")
            self.crash()
            return

        # Preferences for fetching an item
        # 1. Pick it up from the ground in the same zone
        # 2. Buy it from a merchant in the same zone
        # 3. Loot it from a mob in the same zone
        # 4. Craft it

        zone_ground_spots = []
        possible_ground_locations = self._world.ground_book.spots.get(self.request.item_id, ())
        if possible_ground_locations:
            for loc in possible_ground_locations:
                if loc.zone_id != self._world.zone_id:
                    continue

                zone_ground_spots.append(
                    GroundSpot(
                        zone_id=loc.zone_id,
                        x=loc.x,
                        y=loc.y,
                        z=loc.z,
                    )
                )

        if zone_ground_spots:
            self.ground_locations = zone_ground_spots
            self.ground_locations_index = 0
            return

        merchants = self._world.merchants.best(self.request.item_id, self._world.zone)
        if merchants:
            self.merchant = merchants[0]
            self.purchase_cost = merchants[1]
            return

        mob_locations = self._world.item_locations.points(self.request.item_id)
        if mob_locations:
            self.mob_locations = mob_locations
            self.mob_locations_index = 0
            return

        recipe = self._world.recipes.for_item(self.request.item_id)
        if recipe:
            self.recipe = recipe
            return

        log.error(f"No way to fetch {self.request.item_id}")
        self.crash()
        return

    def opcodes(self) -> tuple[str, ...]:
        return ()

    def suspend(self) -> None:
        self.active_path = None
        self.suspended = True

    def satisfied(self) -> bool:
        return self.copper_fetched and self.items_fetched

    @property
    def copper_fetched(self) -> bool:
        if not self.request.copper:
            return True

        if self._world.character.total_copper >= self.request.copper:
            return True

        return False

    @property
    def items_fetched(self) -> bool:
        if not self.request.item_id:
            return True

        number_held = self._world.inventory.held(self.request.item_id)
        if number_held >= self.request.count:
            return True
        return False

    def step(self) -> None:
        self.suspended = False

        if self.satisfied():
            self.complete = True
            return

        # Priority 0: Fetch the item, if there is one
        if self.ground_locations:
            self.ground_fetch()
            return

        if self.merchant:
            self.merchant_fetch()
            return

        if self.mob_locations:
            self.mob_elimination()
            return

        if self.recipe:
            self.craft_item()
            return

        # Priority 1: Fetch the copper, if there is any
        if self.request.copper:
            self.grind_copper()
            return

    def ground_fetch(self) -> None:
        # if self.ground_locations_index >= len(self.ground_locations):
        #     self.ground_locations_index = 0
        #     return

        # ground_location = self.ground_locations[self.ground_locations_index]
        # self.ground_locations_index += 1
        # self.pickup(ground_location)
        return

    def merchant_fetch(self) -> None:
        return

    def mob_elimination(self) -> None:
        return

    def craft_item(self) -> None:
        return

    def grind_copper(self) -> None:
        return

    def report(self) -> str:
        res = f"{super().report()}"
        if self.request.item_id:
            res += f"item={self.item.name} count={self.request.count} held={self._world.inventory.held(self.request.item_id)}"
        if self.request.copper:
            res += f"copper={self.request.copper} / {self._world.character.total_copper}"
        return res

    # def _seek(self, loop: Loop, world: World) -> None:
    #     """Walk to a ground spawn of this item. Roam the zone until one is in view."""
    #     points = ground_at(self.item_id, world.zone_id, str(world.zone or ""))
    #     if points:
    #         here = (world.x, world.y, world.z)
    #         point = min(
    #             points, key=lambda spot: (spot[0] - here[0]) ** 2 + (spot[1] - here[1]) ** 2
    #         )
    #         seen = nearest_spawn(world.ground, point)
    #         if seen is not None:
    #             pickup = Pickup(seen.id, (seen.x, seen.y, seen.z))
    #             pickup.item_id = self.item_id
    #             yield_to(self, loop, world, pickup, f"pickup:{seen.id}")
    #             return
    #         walk(self, loop, world, point, "run")
    #         return
    #     mesh = load_nav(str(world.zone or ""))
    #     spot = None if mesh is None else mesh.unvisited(world.position)
    #     if spot is not None:
    #         walk(self, loop, world, spot, "run")

    # def _chain(
    #     self,
    #     loop: Loop,
    #     world: World,
    #     quest: list[Action] | tuple[Action, ...] | Action,
    #     source: str,
    # ) -> None:
    #     rows = list(quest) if isinstance(quest, (list, tuple)) else [quest]
    #     pushed = False
    #     for index, action in enumerate(rows):
    #         if yield_to(self, loop, world, action, action.source or f"{source}:{index}"):
    #             pushed = True
    #     if pushed:
    #         self.yielding = True

    # def _drop(self, drop: FetchDrop) -> None:
    #     zone = drop.zone
    #     if drop.above_level:
    #         camp = drop.camp
    #         level = drop.level
    #         yield_to(
    #             self,
    #             loop,
    #             world,
    #             Kill(camp=camp, level=level),
    #             f"kill:camp:{self.item_id}",
    #         )
    #         return
    #     if zone and zone != world.zone:
    #         yield_to(self, loop, world, Travel(zone), f"travel:{zone}")
    #         return
    #     queue = loop.queue
    #     for spawn_id in drop.spawns:
    #         if queue is not None and any(
    #             isinstance(action, Kill) and action.spawn_id == spawn_id for action in queue
    #         ):
    #             continue
    #         yield_to(self, loop, world, Kill(spawn_id=spawn_id), f"kill:{spawn_id}")

    # def _earn(self) -> None:
    #     if in_tutorial(world):
    #         return
    #     level = max(int(world.level or 1), 1)
    #     zones = grind_zones(level)
    #     here = (world.zone or "").lower()
    #     if here not in zones:
    #         if not zones:
    #             return
    #         zone = zones[0]
    #         source = f"{self.source}#gold:travel:{zone}"
    #         if _open(loop, source):
    #             self.yielding = True
    #             return
    #         yield_to(self, loop, world, Travel(zone), source)
    #         return
    #     target = level + 1
    #     source = f"{self.source}#gold:kill:{here}:{target}"
    #     if _open(loop, source):
    #         self.yielding = True
    #         return
    #     yield_to(self, loop, world, Kill(camp=here, level=target), source)

    # def _shop(self) -> bool:
    #     offer = choose_offer(world, self.item_id, _merchant_book())
    #     if offer is not None:
    #         self._visit(loop, world, offer)
    #         return True
    #     later = world.later_shops.get(self.item_id)
    #     if later is None:
    #         return False
    #     if later.copper and _copper(world.coin) < later.copper:
    #         self.copper = later.copper
    #         self._earn(loop, world)
    #         return True
    #     hold_for_level(self, loop, world, later.blocked_zone)
    #     return True

    # def _visit(self, offer: ShopOffer) -> None:
    #     if offer.copper and _copper(world.coin) < offer.copper:
    #         self.copper = offer.copper
    #         self._earn(loop, world)
    #         return
    #     self._buy(loop, world, FetchMerchant(npc=offer.npc_id, zone=offer.zone))

    # def _buy(self, seller: FetchMerchant) -> None:
    #     """Walk to the merchant who stocks this, then buy it from the live spawn."""
    #     if seller.zone and not _here(world, seller.zone):
    #         source = f"{self.source}#travel"
    #         if _open(loop, source):
    #             self.priority = 0
    #             self.yielding = True
    #             return
    #         if yield_to(self, loop, world, Travel(seller.zone), source):
    #             self.priority = 0
    #         return
    #     spawn = _spawned(world, seller)
    #     if not spawn:
    #         return
    #     source = f"trade:{self.item_id}"
    #     if _open(loop, source):
    #         self.priority = 0
    #         self.yielding = True
    #         return
    #     opened = Trade(spawn, self.item_id)
    #     opened.merchant_zone = seller.zone
    #     if yield_to(self, loop, world, opened, source):
    #         self.priority = 0

    # def _near_level(self, drop: FetchDrop) -> bool:
    #     """A drop from a camp at this level is farmed. A camp above us is bought when it is sold."""
    #     if drop.above_level:
    #         return False
    #     level = int(world.level or 1)
    #     if drop.level is None:
    #         return True
    #     return drop.level <= level + 2

    # def _spawned(self, merchant: FetchMerchant) -> int:
    #     book = _merchant_book()
    #     if book is None:
    #         return 0
    #     row = book.by_npc.get(merchant.npc)
    #     if not row:
    #         return 0
    #     name = normalize_name(str(row.get("name") or ""))
    #     if not name:
    #         return 0
    #     for mob in world.mobs.values():
    #         if mob.dead:
    #             continue
    #         if normalize_name(mob.spoken_name()) == name:
    #             return int(mob.id)
    #     return 0

    # def _here(self, zone: str) -> bool:
    #     return not zone or zone == world.zone
