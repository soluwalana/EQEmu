"""PEQ item definitions cached as eqclient4.structs.Item objects.

The cache stores item definitions, not inventory/wire instances.
Unknown instance-specific integer fields are initialized to -1.
"""

from __future__ import annotations

import json
import os
from collections.abc import Iterable
from dataclasses import dataclass, field
from pathlib import Path

from eqclient4.data.cache_builders.common import peq_path
from eqclient4.data.catalog import _table, _tuple
from eqclient4.structs import Item

DEFAULT_ITEMS = str(Path.home() / ".eqclient" / "items.jsonl")

# Item attribute -> zero-based column index in the supplied PEQ items schema.
_OFFSETS: dict[str, int] = {
    "name": 2,
    "id_file": 80,
    "slots": 112,
    "_classes": 44,
    "races": 102,
    "ac": 4,
    "damage": 51,
    "required_level": 106,
    "size": 109,
    "bag_slots": 30,
    "bag_size": 29,
    "item_type": 82,
    "scroll_effect": 159,
    "price": 49,
    "lore_group": 88,
    "weight": 120,
    "stack_size": 140,
    "bag_type": 31,
    "bag_weight_reduction": 32,
    "delay": 54,
    "range": 103,
    "magic": 89,
    "elemental_damage_type": 60,
    "elemental_damage": 61,
    "strength": 11,
    "stamina": 10,
    "agility": 3,
    "dexterity": 7,
    "wisdom": 28,
    "intelligence": 8,
    "charisma": 6,
    "hp": 77,
    "mana": 90,
    "endurance": 62,
    "resist_magic": 96,
    "resist_fire": 73,
    "resist_cold": 50,
    "resist_poison": 100,
    "resist_disease": 57,
    "resist_corruption": 171,
    "deity": 53,
    "recommended_level": 104,
    "attack": 12,
    "haste": 75,
    "damage_shield": 52,
    "shielding": 108,
    "avoidance": 27,
    "accuracy": 5,
    "item_class": 81,
    "click_effect": 113,
    "proc_effect": 145,
    "worn_effect": 150,
    "focus_effect": 72,
    "bard_effect": 249,
    "aug_type": 26,
    "aug_restrict": 13,
    "no_drop": 97,
    "no_transfer": 141,
    "item_id": 0,
}

_INSTANCE_DEFAULTS = {"kind": -1, "slot": -1, "stack": -1, "charges": -1}


def _type_cast(key: str, value: str) -> int | str | bool:
    if key in {"name", "id_file"}:
        return str(value)

    if key == "no_drop":
        return int(value) == 0  # PEQ nodrop=0 means NO DROP.

    if key == "no_transfer":
        return int(value) != 0

    return int(value)


def _from_peq(values: list[str]) -> Item:
    payload = {key: _type_cast(key, values[offset]) for key, offset in _OFFSETS.items()}
    return Item(**_INSTANCE_DEFAULTS, **payload)  # type: ignore[arg-type]


@dataclass
class ItemBook:
    """Item ID -> item definition from PEQ."""

    by_id: dict[int, Item] = field(default_factory=dict)
    _by_name: dict[str, int] | None = field(default=None, repr=False)

    def get(self, item_id: int) -> Item | None:
        return self.by_id.get(int(item_id))

    def id_named(self, name: str) -> int:
        key = " ".join((name or "").casefold().split())
        if not key:
            return 0
        if self._by_name is None:
            self._by_name = {}
            for item in self.by_id.values():
                normalized = " ".join(item.name.casefold().split())
                self._by_name.setdefault(normalized, item.item_id)
        return self._by_name.get(key, 0)


def items_from_lines(lines: Iterable[str]) -> ItemBook:
    book = ItemBook()
    mode = ""
    minimum_fields = max(_OFFSETS.values()) + 1
    for raw in lines:
        line = raw.strip()
        if line.startswith("INSERT INTO `"):
            mode = _table(line).lower()
            continue
        if mode != "items" or not line.startswith("("):
            continue
        values = _tuple(line)
        if len(values) < minimum_fields:
            raise ValueError(
                f"Item row has {len(values)} fields; expected at least {minimum_fields}"
            )
        item = _from_peq(values)
        if item.item_id > 0:
            book.by_id[item.item_id] = item
    return book


def build_items(peq: str | Path) -> ItemBook:
    with open(peq, encoding="latin1", errors="replace") as handle:
        return items_from_lines(handle)


def write_items(book: ItemBook, path: str) -> None:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8") as output:
        for _, item in sorted(book.by_id.items()):
            payload = {**_INSTANCE_DEFAULTS}
            payload.update({key: getattr(item, key) for key in _OFFSETS})
            output.write(json.dumps(payload, separators=(",", ":"), ensure_ascii=True) + "\n")


def read_items(path: str) -> ItemBook:
    book = ItemBook()
    file = Path(path)
    if not file.is_file():
        return book
    with file.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            data = json.loads(line)
            classes = data.pop("classes")
            item = Item(**data)
            item.classes = classes
            book.by_id[item.item_id] = item
    return book


def ensure_items(
    path: str | None = None,
    peq: str | Path | None = None,
    rebuild: bool = False,
) -> ItemBook:
    """Load items.jsonl, or build once from the PEQ dump."""
    path = path or os.environ.get("EQEMU_ITEMS", DEFAULT_ITEMS)
    if Path(path).is_file() and not rebuild:
        return read_items(path)

    dump = peq_path(peq)
    if not dump.is_file():
        raise FileNotFoundError(f"PEQ dump file not found: {dump}")

    book = build_items(dump)
    write_items(book, path)
    return book
