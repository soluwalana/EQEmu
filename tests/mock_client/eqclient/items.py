"""Inventory learned from OP_ItemPacket, and which ground models belong to an item."""

from __future__ import annotations

from dataclasses import dataclass

from eqclient.packets import HELD_ITEM_TYPES, ITEM_LOOT, parse_item_packet

CURSOR = 30
PRIMARY = 13
TRADE = 3000
GENERAL = range(22, 30)


@dataclass
class Held:
    item_id: int
    slot: int
    stack: int
    name: str
    idfile: str
    slots: int = 0
    classes: int = 0
    races: int = 0
    ac: int = 0
    damage: int = 0
    req_level: int = 0
    size: int = 0
    bag_slots: int = 0
    bag_size: int = 0


class Inventory:
    def __init__(self) -> None:
        self.slots: dict[int, Held] = {}
        self.idfile: dict[int, str] = {}
        self.fetched: set[int] = set()
        # Loot-window lines. They are still on the corpse until OP_LootItem takes them.
        self.corpse_slots: dict[int, Held] = {}

    def on_packet(self, payload: bytes, needed: set[int] | None = None) -> Held | None:
        parsed = parse_item_packet(payload)
        if parsed is None:
            return None
        (
            kind,
            slot,
            name,
            idfile,
            item_id,
            stack,
            slot_bits,
            classes,
            races,
            ac,
            damage,
            req_level,
            size,
            bag_slots,
            bag_size,
        ) = parsed
        if idfile:
            self.idfile[item_id] = idfile
        held = Held(
            item_id,
            slot,
            stack,
            name,
            idfile,
            _worn_bits(slot_bits),
            classes,
            races,
            ac,
            damage,
            req_level,
            size,
            bag_slots,
            bag_size,
        )
        if kind == ITEM_LOOT:
            self.corpse_slots[slot] = held
            return held
        if kind not in HELD_ITEM_TYPES:
            return None
        self.slots[slot] = held
        if needed and item_id in needed:
            self.fetched.add(item_id)
        return held

    def clear_corpse(self) -> None:
        self.corpse_slots.clear()

    def clear(self) -> None:
        """Death took what we were holding. Models we have already seen stay known."""
        self.slots.clear()
        self.corpse_slots.clear()

    def count(self, item_id: int) -> int:
        return sum(held.stack for held in self.slots.values() if held.item_id == item_id)

    def slot_of(self, item_id: int) -> int | None:
        for slot, held in self.slots.items():
            if held.item_id == item_id:
                return slot
        return None

    def cursor(self) -> Held | None:
        return self.slots.get(CURSOR)

    def cursor_blocks(self, needed: set[int]) -> bool:
        held = self.cursor()
        return held is not None and held.item_id not in needed

    def note_move(self, from_slot: int, to_slot: int) -> None:
        held = self.slots.pop(from_slot, None)
        if held is None:
            return
        held.slot = to_slot
        self.slots[to_slot] = held

    def empty_general(self) -> int | None:
        for slot in GENERAL:
            if slot not in self.slots:
                return slot
        return None


# Charm through ammo. Bits 21 and 22 are swapped on the Titanium item string.
WORN = range(22)
TRAIN_SKILLS = (0, 1, 36, 28, 15, 33, 19, 34, 10, 30, 23, 20, 11, 7)


def _worn_bits(raw: int) -> int:
    bit21 = (raw >> 21) & 1
    bit22 = (raw >> 22) & 1
    raw &= ~((1 << 21) | (1 << 22))
    return raw | (bit22 << 21) | (bit21 << 22)


def _allowed(mask: int, index: int) -> bool:
    if index <= 0:
        return True
    if mask in (0, 0xFFFF, 0x7FFF, 0xFFFFFFFF):
        return mask != 0
    return bool(mask & (1 << (index - 1)))


def fits(held: Held, class_id: int, race_id: int, level: int) -> bool:
    """The item can be worn by this character in at least one equipment slot."""
    if held.req_level and level < held.req_level:
        return False
    if not _allowed(held.classes, class_id) or not _allowed(held.races, race_id):
        return False
    return any(held.slots & (1 << slot) for slot in WORN)


def equip_move(
    inventory: Inventory,
    class_id: int,
    race_id: int,
    level: int,
    protect: set[int],
) -> tuple[int, int] | None:
    """Move a bag or cursor item into a worn slot when it fits and is an upgrade."""
    for slot, held in list(inventory.slots.items()):
        if slot in WORN or held.item_id in protect or held.bag_slots:
            continue
        if not fits(held, class_id, race_id, level):
            continue
        dest = _upgrade_slot(inventory, held)
        if dest is not None:
            return slot, dest
    return None


def _upgrade_slot(inventory: Inventory, held: Held) -> int | None:
    choices = [slot for slot in WORN if held.slots & (1 << slot)]
    best: int | None = None
    best_gain = 0
    for slot in choices:
        current = inventory.slots.get(slot)
        gain = _gain(held, current)
        if gain > best_gain:
            best = slot
            best_gain = gain
    return best


def _gain(held: Held, current: Held | None) -> int:
    if current is None:
        return max(held.ac, held.damage, 1)
    return max(0, held.ac - current.ac) + max(0, held.damage - current.damage)


# General slot 22 holds contents 251-260. Each later bag is ten slots on. Cursor contents start at 331.
GENERAL_BAGS_BEGIN = 251
BAG_SLOT_COUNT = 10
CURSOR_BAG_BEGIN = 331


def content_slot(parent: int, index: int) -> int:
    """Server slot id for one pocket inside a bag."""
    if parent == CURSOR:
        return CURSOR_BAG_BEGIN + index
    return GENERAL_BAGS_BEGIN + (parent - GENERAL.start) * BAG_SLOT_COUNT + index


def stack_totals(slots: dict[int, Held]) -> dict[int, int]:
    totals: dict[int, int] = {}
    for held in slots.values():
        totals[held.item_id] = totals.get(held.item_id, 0) + max(held.stack, 1)
    return totals


def missing_entries(before: dict[int, int], after: dict[int, int], expected: list[Held]) -> int:
    """How many corpse lines have not shown up in inventory, bags included."""
    groups: dict[int, list[int]] = {}
    for held in expected:
        groups.setdefault(held.item_id, []).append(max(held.stack, 1))
    missing = 0
    for item_id, stacks in groups.items():
        gained = after.get(item_id, 0) - before.get(item_id, 0)
        for stack in stacks:
            if gained >= stack:
                gained -= stack
            else:
                missing += 1
    return missing


def empty_in_bag(inventory: Inventory, held: Held) -> int | None:
    """A free pocket whose bag is large enough. Bags themselves stay out of bags."""
    if held.bag_slots:
        return None
    for parent in GENERAL:
        bag = inventory.slots.get(parent)
        if bag is None or bag.bag_slots <= 0 or held.size > bag.bag_size:
            continue
        for index in range(min(bag.bag_slots, BAG_SLOT_COUNT)):
            slot = content_slot(parent, index)
            if slot not in inventory.slots:
                return slot
    return None


def _general_for_bag(inventory: Inventory, bag: Held) -> int | None:
    for slot in GENERAL:
        if slot in inventory.slots:
            continue
        if bag.slots == 0 or bag.slots & (1 << slot):
            return slot
    return None


def stow_move(inventory: Inventory) -> tuple[int, int] | None:
    """One move that puts a bag into a general slot, or a loose item into a bag."""
    cursor = inventory.cursor()
    if cursor is not None and cursor.bag_slots:
        dest = _general_for_bag(inventory, cursor)
        if dest is not None:
            return CURSOR, dest
    if cursor is not None and not cursor.bag_slots:
        dest = empty_in_bag(inventory, cursor)
        if dest is None:
            dest = inventory.empty_general()
        if dest is not None:
            return CURSOR, dest
    for slot in GENERAL:
        held = inventory.slots.get(slot)
        if held is None or held.bag_slots:
            continue
        dest = empty_in_bag(inventory, held)
        if dest is not None:
            return slot, dest
    return None


def can_receive(inventory: Inventory) -> bool:
    """True when another loot item can land, after bags have been used for room."""
    if inventory.cursor() is None:
        return True
    if inventory.empty_general() is not None:
        return True
    cursor = inventory.cursor()
    if cursor is not None and not cursor.bag_slots and empty_in_bag(inventory, cursor) is not None:
        return True
    for slot in GENERAL:
        held = inventory.slots.get(slot)
        if held is not None and not held.bag_slots and empty_in_bag(inventory, held) is not None:
            return True
    return False
