"""Item combat stats from peq, cached beside the quest graph.

Packet AC/damage often lands as 0 on Titanium ItemPackets. Equip/upgrade scoring
reads this cache so Gloomiron Greaves beat Stitched Burlap Pants using real AC,
aagi/astr/…, hp, and mana.
"""

from __future__ import annotations

import json
import os
from dataclasses import asdict, dataclass, field
from pathlib import Path

from eqclient.catalog import _table, _tuple

DEFAULT_ITEMS = str(Path.home() / ".eqclient" / "items.jsonl")

# peq `items` column indices (create_tables_content.sql).
_COL_ID = 0
_COL_NAME = 2
_COL_AAGI = 3
_COL_AC = 4
_COL_ACHA = 6
_COL_ADEX = 7
_COL_AINT = 8
_COL_ASTA = 10
_COL_ASTR = 11
_COL_AWIS = 28
_COL_BAGSLOTS = 30
_COL_CLASSES = 44
_COL_DAMAGE = 51
_COL_DELAY = 54
_COL_HP = 77
_COL_ITEMTYPE = 82
_COL_MANA = 90
_COL_RACES = 102
_COL_REQLEVEL = 106
_COL_SIZE = 109
_COL_SLOTS = 112


@dataclass(frozen=True)
class ItemStats:
    item_id: int
    name: str = ""
    ac: int = 0
    damage: int = 0
    delay: int = 0
    astr: int = 0
    asta: int = 0
    aagi: int = 0
    adex: int = 0
    awis: int = 0
    aint: int = 0
    acha: int = 0
    hp: int = 0
    mana: int = 0
    reqlevel: int = 0
    slots: int = 0
    classes: int = 0
    races: int = 0
    bagslots: int = 0
    itemtype: int = 0
    size: int = 0


@dataclass
class ItemBook:
    """item id → combat / wear stats from peq."""

    by_id: dict[int, ItemStats] = field(default_factory=dict)

    def get(self, item_id: int) -> ItemStats | None:
        return self.by_id.get(int(item_id))

    def enrich(self, held) -> None:
        """Overlay peq cache fields on a Held (packet AC/slots are often wrong)."""
        row = self.get(held.item_id)
        if row is None:
            return
        if row.name and (not held.name or held.name.endswith("*")):
            held.name = row.name
        # Prefer peq combat/wear fields — Titanium ItemPackets routinely zero or skew these.
        if row.ac:
            held.ac = row.ac
        if row.damage:
            held.damage = row.damage
        if row.reqlevel:
            held.req_level = row.reqlevel
        if row.slots:
            held.slots = row.slots
        if row.classes:
            held.classes = row.classes
        if row.races:
            held.races = row.races
        if row.bagslots:
            held.bag_slots = row.bagslots
        if row.size:
            held.size = row.size
        if row.itemtype:
            held.item_type = row.itemtype
        held.astr = row.astr
        held.asta = row.asta
        held.aagi = row.aagi
        held.adex = row.adex
        held.awis = row.awis
        held.aint = row.aint
        held.acha = row.acha
        held.hp = row.hp
        held.mana = row.mana
        held.delay = row.delay


def _int(fields: list[str], index: int) -> int:
    if index >= len(fields):
        return 0
    raw = fields[index]
    if not raw or not raw.lstrip("-").isdigit():
        return 0
    return int(raw)


def items_from_lines(lines) -> ItemBook:
    mode = ""
    book = ItemBook()
    for raw in lines:
        line = raw.strip()
        if line.startswith("INSERT INTO `"):
            mode = _table(line)
            continue
        if mode != "items" or not line.startswith("("):
            continue
        fields = _tuple(line)
        if len(fields) <= _COL_SLOTS or not fields[_COL_ID].isdigit():
            continue
        item_id = int(fields[_COL_ID])
        if item_id <= 0:
            continue
        book.by_id[item_id] = ItemStats(
            item_id=item_id,
            name=fields[_COL_NAME],
            ac=_int(fields, _COL_AC),
            damage=_int(fields, _COL_DAMAGE),
            delay=_int(fields, _COL_DELAY),
            astr=_int(fields, _COL_ASTR),
            asta=_int(fields, _COL_ASTA),
            aagi=_int(fields, _COL_AAGI),
            adex=_int(fields, _COL_ADEX),
            awis=_int(fields, _COL_AWIS),
            aint=_int(fields, _COL_AINT),
            acha=_int(fields, _COL_ACHA),
            hp=_int(fields, _COL_HP),
            mana=_int(fields, _COL_MANA),
            reqlevel=_int(fields, _COL_REQLEVEL),
            slots=_int(fields, _COL_SLOTS),
            classes=_int(fields, _COL_CLASSES),
            races=_int(fields, _COL_RACES),
            bagslots=_int(fields, _COL_BAGSLOTS),
            itemtype=_int(fields, _COL_ITEMTYPE),
            size=_int(fields, _COL_SIZE),
        )
    return book


def build_items(peq: str | Path) -> ItemBook:
    path = Path(peq)
    with open(path, encoding="latin1", errors="replace") as handle:
        return items_from_lines(handle)


def write_items(book: ItemBook, path: str) -> None:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    lines = []
    for item_id, row in sorted(book.by_id.items()):
        payload = {"kind": "item", **asdict(row)}
        # Compact key name for the jsonl schema used elsewhere.
        payload["item"] = payload.pop("item_id")
        lines.append(json.dumps(payload, separators=(",", ":")))
    destination.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")


def read_items(path: str) -> ItemBook:
    book = ItemBook()
    file = Path(path)
    if not file.is_file():
        return book
    for line in file.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        if row.get("kind") not in (None, "item"):
            continue
        item_id = int(row.get("item") or row.get("item_id") or 0)
        if item_id <= 0:
            continue
        book.by_id[item_id] = ItemStats(
            item_id=item_id,
            name=str(row.get("name") or ""),
            ac=int(row.get("ac") or 0),
            damage=int(row.get("damage") or 0),
            delay=int(row.get("delay") or 0),
            astr=int(row.get("astr") or 0),
            asta=int(row.get("asta") or 0),
            aagi=int(row.get("aagi") or 0),
            adex=int(row.get("adex") or 0),
            awis=int(row.get("awis") or 0),
            aint=int(row.get("aint") or 0),
            acha=int(row.get("acha") or 0),
            hp=int(row.get("hp") or 0),
            mana=int(row.get("mana") or 0),
            reqlevel=int(row.get("reqlevel") or 0),
            slots=int(row.get("slots") or 0),
            classes=int(row.get("classes") or 0),
            races=int(row.get("races") or 0),
            bagslots=int(row.get("bagslots") or 0),
            itemtype=int(row.get("itemtype") or 0),
            size=int(row.get("size") or 0),
        )
    return book


def ensure_items(
    path: str | None = None,
    peq: str | Path | None = None,
    *,
    rebuild: bool = False,
) -> ItemBook:
    """Build/load via cache_builders. Prefer read_items at runtime."""
    from eqclient.cache_builders.items import ensure_items as _ensure

    return _ensure(path, peq, rebuild=rebuild)
