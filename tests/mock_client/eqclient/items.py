"""Inventory learned from OP_ItemPacket, and which ground models belong to an item."""

from __future__ import annotations

from dataclasses import dataclass

from eqclient.packets import HELD_ITEM_TYPES, ITEM_LOOT, parse_inventory, parse_item_packet

CURSOR = 30
PRIMARY = 13
SECONDARY = 14
TRADE = 3000
GENERAL = range(22, 30)
# Classic vendor backpack — fills empty general slots when the agent can buy.
BACKPACK_ITEM = 17005
GENERAL_BAG_WANT = 8
# Server SwapItemResync plants this then DeleteItem/real item. Treat as empty.
RESYNC_TOKEN_ID = 22292  # Copper Coin

# Titanium possessions 0–21 (charm → ammo).
WORN_NAMES = (
    "charm",
    "ear1",
    "head",
    "face",
    "ear2",
    "neck",
    "shoulders",
    "arms",
    "back",
    "wrist1",
    "wrist2",
    "range",
    "hands",
    "primary",
    "secondary",
    "finger1",
    "finger2",
    "chest",
    "legs",
    "feet",
    "waist",
    "ammo",
)


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
    item_type: int = 0
    scroll_spell: int = 0
    # Filled from ~/.eqclient/items.jsonl when the ItemPacket omits them.
    astr: int = 0
    asta: int = 0
    aagi: int = 0
    adex: int = 0
    awis: int = 0
    aint: int = 0
    acha: int = 0
    hp: int = 0
    mana: int = 0
    delay: int = 0


class Inventory:
    def __init__(self) -> None:
        self.slots: dict[int, Held] = {}
        self.idfile: dict[int, str] = {}
        self.fetched: set[int] = set()
        self.failed_tomes: set[int] = set()
        self.failed_scrolls: set[int] = set()
        self.scribed: set[int] = set()
        self.book: dict[int, int] = {}
        self.memorized: dict[int, int] = {}
        self.spell_names: dict[int, str] = {}
        # Loot-window lines. They are still on the corpse until OP_LootItem takes them.
        self.corpse_slots: dict[int, Held] = {}

    def load_inventory(self, payload: bytes, needed: set[int] | None = None) -> list[Held]:
        """Everything the login inventory packet listed."""
        return [held for parsed in parse_inventory(payload) if (held := self._hold(parsed, needed)) is not None]

    def on_packet(self, payload: bytes, needed: set[int] | None = None) -> Held | None:
        parsed = parse_item_packet(payload)
        if parsed is None:
            return None
        return self._hold(parsed, needed)

    def _hold(self, parsed, needed: set[int] | None) -> Held | None:
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
            item_type,
            scroll_spell,
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
            item_type,
            scroll_spell,
        )
        if scroll_spell > 0:
            self.spell_names[scroll_spell] = name
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

    def scroll(self) -> Held | None:
        """A spell scroll whose spell is not in the book yet."""
        for held in self.slots.values():
            if held.scroll_spell <= 0 or held.item_type != 20:
                continue
            if held.scroll_spell in self.failed_scrolls or held.scroll_spell in self.scribed:
                continue
            lowered = held.name.lower()
            if lowered.startswith("tome of ") or lowered.startswith("skill:"):
                continue
            return held
        return None

    def tome(self) -> Held | None:
        """A skill tome still in a bag. Right-clicking it is what learns the ability."""
        for held in self.slots.values():
            if held.slot in self.failed_tomes:
                continue
            if held.name.startswith("Tome of ") or held.name.startswith("Skill: "):
                return held
        return None

    def cursor_blocks(self, needed: set[int]) -> bool:
        held = self.cursor()
        return held is not None and held.item_id not in needed

    def note_move(self, from_slot: int, to_slot: int) -> None:
        """Apply a Titanium-style swap locally (displaced item returns to from_slot)."""
        moving = self.slots.pop(from_slot, None)
        if moving is None:
            return
        displaced = self.slots.pop(to_slot, None)
        moving.slot = to_slot
        self.slots[to_slot] = moving
        if displaced is not None:
            displaced.slot = from_slot
            self.slots[from_slot] = displaced

    def empty_general(self) -> int | None:
        empties = self.empty_generals()
        return empties[0] if empties else None

    def empty_generals(self) -> list[int]:
        """Every free general slot (drops leftover SwapItemResync Copper Coin tokens)."""
        out: list[int] = []
        for slot in GENERAL:
            held = self.slots.get(slot)
            if held is None:
                out.append(slot)
                continue
            if held.item_id == RESYNC_TOKEN_ID:
                self.slots.pop(slot, None)
                out.append(slot)
        return out


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
    score=None,
) -> tuple[int, int] | None:
    """Move a bag or cursor item into a worn slot when it fits and is an upgrade."""
    for slot, held in list(inventory.slots.items()):
        if slot in WORN or held.item_id in protect or held.bag_slots:
            continue
        if not fits(held, class_id, race_id, level):
            continue
        dest = _upgrade_slot(inventory, held, score)
        if dest is not None:
            return slot, dest
    return None


def _upgrade_slot(inventory: Inventory, held: Held, score=None) -> int | None:
    choices = [slot for slot in WORN if held.slots & (1 << slot)]
    primary = inventory.slots.get(PRIMARY)
    # 2H primary occupies the offhand — never "upgrade" into secondary under it.
    if primary is not None and (primary.slots & 0x2000):
        choices = [slot for slot in choices if slot != SECONDARY]
    best: int | None = None
    best_gain = 0
    for slot in choices:
        current = inventory.slots.get(slot)
        gain = _gain(held, current, score)
        if gain > best_gain:
            best = slot
            best_gain = gain
    return best


_STARTER_JUNK = (
    "burlap",
    "patched",
    "tattered",
    "ruined",
    "training",
    "cloth cap",
    "cloth shirt",
    "cloth pants",
    "cloth sleeves",
    "cloth wrist",
    "worn cloth",
)


def held_stats_tip(held: Held) -> str:
    """Compact non-zero stats for inventory dumps."""
    parts: list[str] = []
    for label, value in (
        ("ac", held.ac),
        ("dmg", held.damage),
        ("delay", getattr(held, "delay", 0)),
        ("str", getattr(held, "astr", 0)),
        ("sta", getattr(held, "asta", 0)),
        ("agi", getattr(held, "aagi", 0)),
        ("dex", getattr(held, "adex", 0)),
        ("wis", getattr(held, "awis", 0)),
        ("int", getattr(held, "aint", 0)),
        ("cha", getattr(held, "acha", 0)),
        ("hp", getattr(held, "hp", 0)),
        ("mana", getattr(held, "mana", 0)),
        ("bag", held.bag_slots),
    ):
        if value:
            parts.append(f"{label}={value}")
    return ", ".join(parts)


def is_wearable_gear(held: Held) -> bool:
    """Armor/weapon — include items whose AC/damage failed to parse from the packet."""
    if held.bag_slots:
        return False
    if held.ac > 0 or held.damage > 0:
        return True
    return any(held.slots & (1 << slot) for slot in WORN)


def _gain(held: Held, current: Held | None, score=None) -> int:
    if score is not None:
        gain = score(held) - (score(current) if current is not None else 0)
        if gain > 0:
            return gain
    if current is None:
        return max(held.ac, held.damage, 1) if is_wearable_gear(held) else 0
    numeric = max(0, held.ac - current.ac) + max(0, held.damage - current.damage)
    if numeric:
        return numeric
    # Packet AC often lands as 0 — still swap starter junk for real named gear.
    cur_n = (current.name or "").lower()
    new_n = (held.name or "").lower()
    if (
        is_wearable_gear(held)
        and any(tip in cur_n for tip in _STARTER_JUNK)
        and not any(tip in new_n for tip in _STARTER_JUNK)
    ):
        return 1
    return 0


# General slot 22 holds contents 251-260. Each later bag is ten slots on. Cursor contents start at 331.
GENERAL_BAGS_BEGIN = 251
BAG_SLOT_COUNT = 10
CURSOR_BAG_BEGIN = 331


def server_slot(slot: int) -> int:
    """Titanium slot as the server stores it.

    A right-click is not translated on the way in, so the click has to name the
    server slot. Cursor 30 is server 33. A bag pocket is 200 wide on the server
    and 10 wide here.
    """
    if slot <= 20:
        return slot
    if slot == 21:
        return slot + 1
    if 22 <= slot <= 29:
        return slot + 1
    if slot == 30:
        return slot + 3
    if GENERAL_BAGS_BEGIN <= slot < CURSOR_BAG_BEGIN:
        bag = (slot - GENERAL_BAGS_BEGIN) // BAG_SLOT_COUNT
        index = (slot - GENERAL_BAGS_BEGIN) % BAG_SLOT_COUNT
        return 4010 + bag * 200 + index
    return slot


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
    pockets = empty_bag_pockets(inventory, held)
    return pockets[0] if pockets else None


def empty_bag_pockets(inventory: Inventory, held: Held) -> list[int]:
    """All free bag pockets that can hold this item.

    Only use bag_slots from the item packet — guessing pockets for Backpack* with
    bag_slots=0 sent MoveItem into invalid bag indices and desynced inventory.
    """
    if held.bag_slots:
        return []
    out: list[int] = []
    for parent in GENERAL:
        bag = inventory.slots.get(parent)
        if bag is None or bag.bag_slots <= 0:
            continue
        if bag.bag_size > 0 and held.size > bag.bag_size:
            continue
        for index in range(min(bag.bag_slots, BAG_SLOT_COUNT)):
            slot = content_slot(parent, index)
            pocket = inventory.slots.get(slot)
            if pocket is None:
                out.append(slot)
                continue
            if pocket.item_id == RESYNC_TOKEN_ID:
                inventory.slots.pop(slot, None)
                out.append(slot)
    return out


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
        return has_loot_room(inventory)
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


def worn_bags(inventory: Inventory) -> int:
    """How many general slots already hold a bag."""
    return sum(
        1
        for slot in GENERAL
        if (held := inventory.slots.get(slot)) is not None
        and (held.bag_slots > 0 or "backpack" in (held.name or "").lower())
    )


def bags_short(inventory: Inventory) -> int:
    """How many general slots still lack a bag (empty or occupied by non-bags)."""
    return max(0, GENERAL_BAG_WANT - worn_bags(inventory))


def bags_buyable(inventory: Inventory) -> int:
    """Backpacks we can actually buy right now — needs an empty general slot each."""
    empty = sum(1 for slot in GENERAL if slot not in inventory.slots)
    return min(bags_short(inventory), empty)


def has_loot_room(inventory: Inventory) -> bool:
    """True when one more non-bag item can land with an empty cursor."""
    if inventory.cursor() is not None:
        return False
    if inventory.empty_general() is not None:
        return True
    probe = Held(0, 0, 1, "", "", size=0)
    return empty_in_bag(inventory, probe) is not None


def is_vendor_trash(held: Held, protect: set[int] | None = None) -> bool:
    """Junk that should be sold when bags fill — not gear, bags, food, or quest pieces."""
    protect = protect or set()
    if held.item_id <= 0 or held.item_id in protect:
        return False
    if held.bag_slots or held.ac or held.damage or held.scroll_spell:
        return False
    if held.item_type in (20,):  # spell scroll / tome type
        return False
    name = (held.name or "").lower()
    if any(
        word in name
        for word in (
            "bread",
            "cake",
            "muffin",
            "pie",
            "meat",
            "cheese",
            "stew",
            "ration",
            "water",
            "drink",
            "ale",
            "wine",
            "milk",
            "cider",
            "tea",
            "mushroom",
            "tome",
            "book",
            "spell",
            "backpack",
            " bag",
        )
    ):
        return False
    if is_coin_item(held):
        return False
    return True


def trash_slots(inventory: Inventory, protect: set[int] | None = None) -> list[int]:
    """Inventory slots holding vendor trash (bag pockets first, then general junk)."""
    protect = protect or set()
    bag_pockets: list[int] = []
    general_junk: list[int] = []
    for slot, held in inventory.slots.items():
        if slot < GENERAL.start or slot == CURSOR:
            continue
        if not is_vendor_trash(held, protect):
            continue
        if slot in GENERAL:
            general_junk.append(slot)
        else:
            bag_pockets.append(slot)
    return bag_pockets + general_junk


def loot_picks(
    slots: list[tuple[int, int, int]],
    held: dict[int, int],
    need: dict[int, int],
) -> list[int]:
    """Corpse slots to take. Each slot is (slot, item id, stack). Stop once the shortfall is covered.

    A slot is one server loot, so a stack larger than the gap is still taken whole.
    """
    gained: dict[int, int] = {}
    chosen: list[int] = []
    for slot, item_id, stack in slots:
        if item_id <= 0:
            continue
        gap = int(need.get(item_id, 0)) - int(held.get(item_id, 0)) - gained.get(item_id, 0)
        if gap <= 0:
            continue
        chosen.append(slot)
        gained[item_id] = gained.get(item_id, 0) + max(1, int(stack or 1))
    return chosen


def is_coin_item(held: Held) -> bool:
    """Loose coin piles on a corpse (not worn gear)."""
    if held.bag_slots or held.ac or held.damage:
        return False
    name = (held.name or "").lower()
    return any(tip in name for tip in ("coin", "platinum", "gold piece", "silver", "copper"))


def coin_loot_slots(corpse_slots: dict[int, Held]) -> list[int]:
    return [slot for slot, held in corpse_slots.items() if is_coin_item(held)]


def upgrade_loot_slots(
    corpse_slots: dict[int, Held],
    inventory: Inventory,
    class_id: int,
    race_id: int,
    level: int,
    protect: set[int] | None = None,
    score=None,
) -> list[int]:
    """Corpse slots whose armor/weapon is wearable and better than what is equipped."""
    protect = protect or set()
    chosen: list[int] = []
    for slot, held in corpse_slots.items():
        if held.item_id in protect or held.bag_slots:
            continue
        if is_coin_item(held):
            continue
        if held.ac <= 0 and held.damage <= 0:
            continue
        if not fits(held, class_id, race_id, level):
            continue
        if _upgrade_slot(inventory, held, score) is not None:
            chosen.append(slot)
    return chosen


def bot_usable_loot_slots(
    corpse_slots: dict[int, Held],
    class_ids: list[int],
    race_id: int,
    level: int,
    protect: set[int] | None = None,
    skip_slots: set[int] | None = None,
) -> list[int]:
    """Corpse slots with armor/weapon a party bot class can wear (not already picked)."""
    protect = protect or set()
    skip_slots = skip_slots or set()
    chosen: list[int] = []
    for slot, held in corpse_slots.items():
        if slot in skip_slots or held.item_id in protect or held.bag_slots:
            continue
        if is_coin_item(held):
            continue
        if held.ac <= 0 and held.damage <= 0:
            continue
        if any(fits(held, class_id, race_id, level) for class_id in class_ids):
            chosen.append(slot)
    return chosen
