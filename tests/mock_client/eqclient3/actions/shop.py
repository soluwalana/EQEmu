"""Which merchant can sell this item to this character.

A seller is usable when the standing is not hostile and every zone on the walk
is open at this level. A walk through a higher zone is remembered and tried
again after the level comes up. The nearest usable seller is the shortest walk.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.world import World

from eqclient3.camps import zone_reachable
from eqclient3.data.factions import ensure_factions
from eqclient3.data.merchants import MerchantBook, Seller
from eqclient3.log import log
from eqclient3.nav.travel import ensure_zone_graph, path

# Below this the merchant will not trade. Unknown standing is not a refusal.
INDIFFERENT = 0


@dataclass(frozen=True)
class ShopOffer:
    npc_id: int
    name: str
    zone: str
    copper: int
    hops: int
    blocked_zone: str = ""


def choose_offer(world: World, item_id: int, book: MerchantBook | None) -> ShopOffer | None:
    """Nearest seller this level can walk to. A level-gated walk is stored for later."""
    if book is None or item_id <= 0:
        return None
    row = book.by_item.get(item_id) or {}
    npc_ids = row.get("npcs") or ()
    copper = int(row.get("cost") or 0)
    here = str(world.zone or "")
    level = int(world.level or 1)
    open_offers: list[ShopOffer] = []
    blocked: list[ShopOffer] = []
    for npc_id in npc_ids:
        seller = book._seller(int(npc_id))
        if seller is None or not seller.zone:
            continue
        if not _standing_allows(world, seller):
            continue
        hops = _hops(here, seller.zone)
        gate = _blocked_zone(here, seller.zone, level)
        if hops < 0 and not gate:
            continue
        offer = ShopOffer(seller.npc_id, seller.name, seller.zone, copper, max(hops, 0), gate)
        if gate:
            blocked.append(offer)
        else:
            open_offers.append(offer)
    if open_offers:
        open_offers.sort(key=lambda offer: (offer.hops, offer.npc_id))
        return open_offers[0]
    if blocked:
        blocked.sort(key=lambda offer: (offer.blocked_zone, offer.hops, offer.npc_id))
        world.later_shops[item_id] = blocked[0]
    return None


def _standing_allows(world: World, seller: Seller) -> bool:
    try:
        book = ensure_factions()
    except (OSError, ValueError):
        log.error("faction book failed to load", exc_info=True)
        return True
    faction_id = book.primary(seller.zone, seller.name)
    if not faction_id:
        return True
    standing = world.faction(faction_id)
    if standing.amount is None:
        return True
    return standing.amount >= INDIFFERENT


def _hops(here: str, dest: str) -> int:
    home = (here or "").lower()
    goal = (dest or "").lower()
    if not goal:
        return -1
    if home == goal:
        return 0
    graph = ensure_zone_graph()
    if graph is None:
        return 1
    legs = path(graph, home, goal)
    if not legs:
        return -1
    return len(legs)


def _blocked_zone(here: str, dest: str, level: int) -> str:
    """A zone on the walk whose floor is above `level`. Empty when the walk is open."""
    home = (here or "").lower()
    goal = (dest or "").lower()
    if not goal:
        return ""
    zones = [goal]
    graph = ensure_zone_graph()
    if graph is not None and home and home != goal:
        legs = path(graph, home, goal)
        if legs:
            zones = [leg.dest for leg in legs]
    for zone in zones:
        if zone_reachable(zone, level).startswith("level:"):
            return zone
    return ""
