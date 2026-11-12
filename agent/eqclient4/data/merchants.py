"""Merchant stock, cached beside the quest graph.

One row per NPC that sells: npc id, the zone id he stands in, and the item
ids on his list. The other direction is item id to the NPCs who sell it and
the copper price from the items table. A campaign leaf with nowhere else to
get an item buys it here.
"""

from __future__ import annotations

import json
import os
from collections import defaultdict
from collections.abc import Iterable, Iterator
from dataclasses import dataclass, field
from pathlib import Path

from eqclient4.data.cache_builders.common import peq_path
from eqclient4.data.catalog import _table, _tuple
from eqclient4.log import log
from eqclient4.utils import normalize_name

DEFAULT_MERCHANTS = str(Path.home() / ".eqclient" / "merchants.jsonl")
# items.price. merchantlist.item is column 2, alt_currency_cost is column 7.
_PRICE = 49
_ALT_CURRENCY = 7


@dataclass(frozen=True)
class Seller:
    npc_id: int
    zone_id: int
    zone: str
    name: str


def zone_aliases(zone: str) -> frozenset[str]:
    """The zone we are standing in.

    freportw (9) and freeportwest (383) are both titled West Freeport and are
    still different zones. The same split is qeynos/qeynos2 and
    commons/ecommons/commonlands/oldcommons. A merchant in one is not stocked
    in the other.
    """
    home = (zone or "").lower()
    if not home:
        return frozenset()
    return frozenset({home})


@dataclass
class MerchantBook:
    """npc id → stock, and item id → sellers plus one copper cost."""

    by_npc: dict[int, dict] = field(default_factory=dict)
    by_item: dict[int, dict] = field(default_factory=dict)
    by_zone: dict[str, tuple[int, ...]] = field(default_factory=dict)
    _names: set[str] = field(default_factory=set)
    _names_in: dict[str, set[str]] = field(default_factory=dict)
    _indexed: bool = False

    def index(self) -> None:
        """Zone → sellers, and normalized name → that zone. in_zone no longer walks every NPC."""
        zones: dict[str, list[int]] = defaultdict(list)
        names: set[str] = set()
        names_in: dict[str, set[str]] = defaultdict(set)
        for npc_id, row in self.by_npc.items():
            zone = str(row.get("where") or "").lower()
            zones[zone].append(int(npc_id))
            folded = normalize_name(str(row.get("name") or ""))
            if folded:
                names.add(folded)
                names_in[zone].add(folded)
        self.by_zone = {zone: tuple(npc_ids) for zone, npc_ids in zones.items()}
        self._names = names
        self._names_in = dict(names_in)
        self._indexed = True

    def sells(self, item_id: int) -> bool:
        return item_id in self.by_item

    def cost(self, item_id: int) -> int:
        row = self.by_item.get(item_id) or {}
        return int(row.get("cost") or 0)

    def best(self, item_id: int, here: str = "") -> tuple[Seller, int] | None:
        """A seller in this zone when one is stocked here, otherwise the nearest zone id."""
        row = self.by_item.get(item_id)
        if not row:
            return None
        sellers = [self._seller(npc_id) for npc_id in row.get("npcs") or ()]
        stocked = [seller for seller in sellers if seller is not None]
        if not sellers:
            return None
        here = (here or "").lower()
        aliases = zone_aliases(here)
        local = [seller for seller in stocked if seller.zone in aliases or seller.zone == here]
        pool = local or stocked
        pool.sort(key=lambda seller: (seller.zone_id or 10**9, seller.zone, seller.npc_id))
        return pool[0], int(row.get("cost") or 0)

    def in_zone(self, zone: str) -> list[Seller]:
        """Every cached seller whose zone short name is `zone`."""
        aliases = zone_aliases(zone)
        if not aliases:
            return []
        if self._indexed:
            npc_ids = [npc_id for alias in aliases for npc_id in self.by_zone.get(alias, ())]
        else:
            npc_ids = [
                npc_id
                for npc_id, row in self.by_npc.items()
                if str(row.get("where") or "").lower() in aliases
            ]
        found = [seller for npc_id in npc_ids if (seller := self._seller(npc_id)) is not None]
        found.sort(key=lambda seller: (seller.name.lower(), seller.npc_id))
        return found

    def names_in(self, zone: str) -> set[str]:
        """Normalized merchant names for matching live spawns in `zone`."""
        if self._indexed:
            found: set[str] = set()
            for alias in zone_aliases(zone):
                found.update(self._names_in.get(alias, ()))
            return found
        return {normalize_name(seller.name) for seller in self.in_zone(zone) if seller.name}

    def is_merchant_name(self, name: str, zone: str = "") -> bool:
        """True when `name` is a known seller, optionally restricted to `zone`."""
        folded = normalize_name(name)
        if not folded:
            return False
        if self._indexed:
            if zone:
                return folded in self.names_in(zone)
            return folded in self._names
        if zone:
            return folded in self.names_in(zone)
        for row in self.by_npc.values():
            if normalize_name(str(row.get("name") or "")) == folded:
                return True
        return False

    def _seller(self, npc_id: int) -> Seller | None:
        row = self.by_npc.get(int(npc_id))
        if not row:
            return None
        return Seller(
            int(npc_id),
            int(row.get("zone") or 0),
            str(row.get("where") or ""),
            str(row.get("name") or ""),
        )


def merchants_from_lines(lines: Iterable[str]) -> MerchantBook:
    """NPC stock and item prices from a peq dump. No live query."""
    mode = ""
    prices: dict[int, int] = {}
    stock: dict[int, set[int]] = defaultdict(set)
    names: dict[int, str] = {}
    merchant_of: dict[int, int] = {}
    groups: dict[int, set[int]] = defaultdict(set)
    group_zones: dict[int, set[str]] = defaultdict(set)
    zone_ids: dict[str, int] = {}
    for raw in lines:
        line = raw.strip()
        if line.startswith("INSERT INTO `"):
            mode = _table(line)
            continue
        if not line.startswith("("):
            continue
        fields = _tuple(line)
        if mode == "items":
            _take_price(fields, prices)
        elif mode == "merchantlist":
            _take_stock(fields, stock)
        elif mode == "npc_types":
            _take_npc(fields, names, merchant_of)
        elif mode == "spawnentry":
            _take_entry(fields, groups)
        elif mode == "spawn2":
            _take_spawn(fields, group_zones)
        elif mode == "zone":
            _take_zone_id(fields, zone_ids)
    book = MerchantBook()
    sellers_of: dict[int, list[int]] = defaultdict(list)
    for npc_id, merchant_id in merchant_of.items():
        items = stock.get(merchant_id)
        if not items:
            continue
        zones = {zone for group in groups.get(npc_id, ()) for zone in group_zones.get(group, ())}
        if not zones:
            continue
        zone_id, where = _pick_zone(zones, zone_ids)
        item_ids = tuple(sorted(items))
        book.by_npc[npc_id] = {
            "zone": zone_id,
            "where": where,
            "name": names.get(npc_id, ""),
            "items": list(item_ids),
        }
        for item_id in item_ids:
            sellers_of[item_id].append(npc_id)
    for item_id, npc_ids in sellers_of.items():
        book.by_item[item_id] = {
            "npcs": sorted(set(npc_ids)),
            "cost": int(prices.get(item_id, 0)),
        }
    book.index()
    return book


def _take_price(fields: list[str], prices: dict[int, int]) -> None:
    if len(fields) <= _PRICE or not fields[0].isdigit():
        return
    raw = fields[_PRICE]
    prices[int(fields[0])] = int(raw) if raw.lstrip("-").isdigit() else 0


def _take_stock(fields: list[str], stock: dict[int, set[int]]) -> None:
    if (
        len(fields) < 3
        or not fields[0].lstrip("-").isdigit()
        or not fields[2].lstrip("-").isdigit()
    ):
        return
    merchant_id = int(fields[0])
    item_id = int(fields[2])
    if merchant_id <= 0 or item_id <= 0:
        return
    if (
        len(fields) > _ALT_CURRENCY
        and fields[_ALT_CURRENCY].lstrip("-").isdigit()
        and int(fields[_ALT_CURRENCY]) > 0
    ):
        return
    stock[merchant_id].add(item_id)


def _take_npc(fields: list[str], names: dict[int, str], merchant_of: dict[int, int]) -> None:
    if len(fields) <= 18 or not fields[0].isdigit():
        return
    merchant_id = int(fields[18]) if fields[18].lstrip("-").isdigit() else 0
    if merchant_id <= 0:
        return
    npc_id = int(fields[0])
    names[npc_id] = fields[1].replace("_", " ").lstrip("#")
    merchant_of[npc_id] = merchant_id


def _take_entry(fields: list[str], groups: dict[int, set[int]]) -> None:
    if len(fields) < 2 or not fields[0].isdigit() or not fields[1].isdigit():
        return
    groups[int(fields[1])].add(int(fields[0]))


def _take_spawn(fields: list[str], group_zones: dict[int, set[str]]) -> None:
    if len(fields) < 3 or not fields[1].isdigit() or not fields[2]:
        return
    group_zones[int(fields[1])].add(fields[2].lower())


def _take_zone_id(fields: list[str], zone_ids: dict[str, int]) -> None:
    if not fields or not fields[0]:
        return
    if len(fields) > 13 and fields[13].lstrip("-").isdigit() and int(fields[13]) > 0:
        zone_ids[fields[0].lower()] = int(fields[13])


def _pick_zone(zones: set[str], zone_ids: dict[str, int]) -> tuple[int, str]:
    ranked = sorted((zone_ids.get(zone, 10**9), zone) for zone in zones)
    zone_id, zone = ranked[0]
    return (0 if zone_id >= 10**9 else zone_id), zone


def build_merchants(peq: str | Path) -> MerchantBook:
    return merchants_from_lines(_lines(str(peq)))


def write_merchants(book: MerchantBook, path: str) -> None:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []
    for npc_id, row in sorted(book.by_npc.items()):
        lines.append(
            json.dumps(
                {
                    "kind": "merchant",
                    "npc": npc_id,
                    "zone": int(row.get("zone") or 0),
                    "where": row.get("where") or "",
                    "name": row.get("name") or "",
                    "items": list(row.get("items") or ()),
                },
                ensure_ascii=True,
            )
        )
    for item_id, row in sorted(book.by_item.items()):
        lines.append(
            json.dumps(
                {
                    "kind": "item",
                    "item": item_id,
                    "npcs": list(row.get("npcs") or ()),
                    "cost": int(row.get("cost") or 0),
                },
                ensure_ascii=True,
            )
        )
    destination.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")


def read_merchants(path: str) -> MerchantBook:
    book = MerchantBook()
    file = Path(path)
    if not file.is_file():
        log.error(f"merchants file not found: {path}")
        raise FileNotFoundError(f"merchants file not found: {path}")

    for line in file.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        if row.get("kind") == "merchant":
            npc_id = int(row.get("npc") or 0)
            if npc_id:
                book.by_npc[npc_id] = {
                    "zone": int(row.get("zone") or 0),
                    "where": str(row.get("where") or ""),
                    "name": str(row.get("name") or ""),
                    "items": [int(item_id) for item_id in row.get("items") or ()],
                }
        elif row.get("kind") == "item":
            item_id = int(row.get("item") or 0)
            if item_id:
                book.by_item[item_id] = {
                    "npcs": [int(npc_id) for npc_id in row.get("npcs") or ()],
                    "cost": int(row.get("cost") or 0),
                }
    book.index()
    return book


def ensure_merchants(
    path: str | None = None,
    peq: str | Path | None = None,
    rebuild: bool = False,
) -> MerchantBook:
    """Load merchants.jsonl, or build once from the peq dump."""
    path = path or os.environ.get("EQEMU_MERCHANTS", DEFAULT_MERCHANTS)
    file = Path(path)
    if file.is_file() and not rebuild:
        return read_merchants(path)
    dump = peq_path(peq)
    if not dump.is_file():
        log.error(f"peq dump file not found: {dump}")
        raise FileNotFoundError(f"peq dump file not found: {dump}")

    book = build_merchants(dump)
    write_merchants(book, path)
    return book


def _lines(path: str) -> Iterator[str]:
    with open(path, encoding="latin1", errors="replace") as handle:
        yield from handle
