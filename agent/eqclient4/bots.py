"""Minimal EQEmu bot identity and equipment eligibility."""

import re
from collections.abc import Iterator

from eqclient4.data.items import ItemBook
from eqclient4.log import log
from eqclient4.structs.constants import (
    CAN_EQUIP,
    CANNOT_EQUIP,
    CANNOT_EQUIP_CONFLICT,
    CANNOT_EQUIP_LEVEL,
    CLASS_ID_TO_NAME,
    CLASS_NAME_TO_ID,
    DEITY_ID_TO_BIT,
    HEALER_CLASSES,
    RACE_ID_TO_BIT,
    RACE_ID_TO_NAME,
    RACE_NAME_TO_ID,
    TANK_CLASSES,
    WORN_SLOTS,
    WORN_SLOTS_BY_NAME,
    combination_valid,
)
from eqclient4.structs.items import Item
from eqclient4.structs.messages import OP_ChannelMessage, OP_SpecialMesg
from eqclient4.structs.wire import EQStruct, InventorySlot, ItemLink, MessagePart

_CURSOR = InventorySlot.for_client(0, 33)
_SLOT_LINE = re.compile(r"\bSlot\s+(\d+)\s+\([^)]+\)\s*\|\s*(.*)", re.IGNORECASE)
_SLOT_SECTION = re.compile(r"\(Slot\s*(\d+)\s*\)")
# 1, 4 and 35 are the EQ 2H slashing, 2H blunt, and 2H piercing item types.
_TWO_HAND_TYPES = {1, 4, 35}


class Bot:

    def __init__(
        self,
        item_book: ItemBook,
        owner: str,
        name: str,
        race: int,
        class_id: int,
        gender: int,
        created: bool = False,
    ):
        self.owner: str = owner
        self.name: str = name
        self.race: int = race
        self.class_id: int = class_id
        self.gender: int = gender
        self.level: int = 0
        self.hp: int = 0
        self.max_hp: int = 0
        self.mana: int = 0
        self.max_mana: int = 0
        self.id: int = 0
        self.alive: bool = False
        self.created: bool = created
        self.inventory: BotInventory = BotInventory(self, item_book)


class BotInventory:

    def __init__(self, bot: Bot, item_book: ItemBook):
        self.bot = bot
        self.item_book = item_book

        self.slots: dict[InventorySlot, Item] = {}
        self.loaded: bool = False
        self._expecting_listing: dict[int, bool] | None = None
        self.failures: list[str] = []

    def items(self) -> Iterator[tuple[InventorySlot, Item]]:
        for slot in range(23):
            address = InventorySlot.for_client(0, slot)
            item = self.slots.get(address)
            if item is not None:
                yield address, item

    def render(self, show_empty: bool = True, show_ids: bool = True) -> str:
        lines = [f"BOT INVENTORY: {self.bot.name}", "=" * 56]
        for slot, label in WORN_SLOTS.items():
            item = self.slots.get(InventorySlot.for_client(0, slot))
            if item is None and not show_empty:
                continue
            description = "(empty)" if item is None else item.name
            if item and show_ids and item.item_id:
                description += f" [#{item.item_id}]"
            lines.append(f"{label:<16} ({slot:02d}) {description}")
        return "\n".join(lines)

    def list_inventory(self) -> list[EQStruct]:
        """Request an authoritative worn snapshot; call apply on response messages."""
        self._expecting_listing = {s: True for s in WORN_SLOTS.keys()}
        self._expecting_listing[WORN_SLOTS_BY_NAME["Secondary"]] = False
        return [OP_ChannelMessage(text=f"^inventorylist byname {self.bot.name}")]

    def can_equip(self, item: Item, replace: bool = False) -> int:
        """Check intrinsic character restrictions; slot occupancy is inventory state."""
        if item.item_class != 0 or item.slots == 0:
            return CANNOT_EQUIP

        if not 1 <= self.bot.class_id <= 16:
            return CANNOT_EQUIP

        if self.bot.class_id not in item.classes:
            return CANNOT_EQUIP

        race_bit = RACE_ID_TO_BIT.get(self.bot.race, 0)
        if not race_bit or not (item.races & race_bit):
            return CANNOT_EQUIP

        if self.bot.level < item.required_level:
            return CANNOT_EQUIP_LEVEL

        if all(self._slot_available(item, i, replace) == -1 for i in range(23)):
            return CANNOT_EQUIP_CONFLICT

        return CAN_EQUIP

    def _slot_available(self, item: Item, slot: int, replace: bool) -> int:
        if not 0 <= slot <= 22 or not (item.slots & (1 << slot)):
            return -1

        if not replace and InventorySlot.for_client(0, slot) in self.slots:
            return -1

        if slot == 14 and item.item_type not in _TWO_HAND_TYPES:
            primary = self.slots.get(InventorySlot.for_client(0, 13))
            if primary and primary.item_id and primary.item_type in _TWO_HAND_TYPES:
                return -1

        if slot == 13 and item.item_type in _TWO_HAND_TYPES:
            if InventorySlot.for_client(0, 14) in self.slots and not replace:
                return -1

        return slot

    def first_available_slot(self, item: Item) -> int:
        """Return the first available slot with replacement enabled."""
        for i in range(23):
            available_slot = self._slot_available(item, i, True)
            if available_slot == -1:
                continue
            return available_slot
        return -1

    def equip(self, item: Item) -> list[EQStruct]:
        """Give cursor item to bot; does not update slots or player's cursor.

        The item must actually reside in possessions cursor slot 33. The caller
        passes the same Item instance currently indexed by CharacterInventory.
        """
        if not item.address or item.address != _CURSOR:
            raise ValueError("Item must be in Possessions cursor slot 33")

        equippable = self.can_equip(item, replace=True)

        if equippable != CAN_EQUIP:
            raise ValueError(f"{item.name} cannot equip on {self.bot.name} - {equippable}")

        available_slot = self.first_available_slot(item)

        return [
            OP_ChannelMessage(
                target=self.bot.name,
                sender=self.bot.owner,
                text=f"^inventorygive byname {self.bot.name} {available_slot}",
            )
        ]

    def apply(self, packet: EQStruct) -> bool:
        """Apply server text responses. Return True if worn state changed.

        OP_SimpleMessage string_id requires external string-table resolution;
        its substitution texts are parsed when they contain inventory lines.
        """

        parts: tuple[MessagePart, ...]
        match packet:
            case OP_SpecialMesg():
                parts = packet.message_parts
            case _:
                return False

        item_links: list[ItemLink] = [t for t in parts if isinstance(t, ItemLink)]
        strs: list[str] = [t for t in parts if isinstance(t, str)]

        normalized = " ".join(strs).lower()
        if any(
            word in normalized
            for word in ("cannot", "unable", "failed", "refused", "invalid", "not allowed")
        ):
            self.failures.append(normalized)
            return False

        match = _SLOT_LINE.search(packet.message)
        if match and self._expecting_listing:

            slot = int(match.group(1))
            if not 0 <= slot <= 22:
                self._log_failure(f"Received listing message with invalid slot: {slot}")
                return False

            self._expecting_listing[slot] = False
            if all(not e for e in self._expecting_listing.values()):
                self._expecting_listing = None
                self.loaded = True

            address = InventorySlot.for_client(0, slot)
            if len(item_links) == 0:
                self.slots.pop(address, None)
                return True

            item_link = item_links[0]
            item = self.item_book.get(item_link.item_id)
            if not item:
                self._log_failure(
                    f"Received listing message with unknown item: {item_link.item_id}"
                )
                return False

            self.slots[address] = item
            return True

        if self.bot.name.lower() not in normalized:
            return False

        if "i have accepted" in normalized:
            if len(item_links) == 0:
                self._log_failure(
                    f"Received accepted message with {len(item_links)} items: {item_links}"
                )
                return False

            # first item weapon
            item_link = item_links[0]
            item = self.item_book.get(item_link.item_id)
            if not item:
                self._log_failure(
                    f"Received accepted message with unknown item: {item_link.item_id}"
                )
                return False

            available_slot = self.first_available_slot(item)
            if available_slot == -1:
                self._log_failure(f"{item.name} cannot equip on {self.bot.name}")
                return False

            address = InventorySlot.for_client(0, available_slot)
            self.slots[address] = item
            if available_slot == 13 and item.item_type in _TWO_HAND_TYPES:
                self.slots.pop(InventorySlot.for_client(0, 14), None)

            return True

        if "i have unequipped" in normalized:
            if len(item_links) == 0:
                self._log_failure(
                    f"Received unequipped message with {len(item_links)} items: {item_links}"
                )
                return False

            item_link = item_links[0]
            item = self.item_book.get(item_link.item_id)
            if not item:
                self._log_failure(
                    f"Received unequipped message with unknown item: {item_link.item_id}"
                )
                return False

            match = _SLOT_SECTION.search(packet.message)
            if not match:
                self._log_failure(
                    f"Received unequipped message without slot section: {packet.message}"
                )
                return False

            slot = int(match.group(1))
            if not 0 <= slot <= 22:
                self._log_failure(f"Received unequipped message with invalid slot: {slot}")
                return False

            address = InventorySlot.for_client(0, slot)
            old = self.slots.pop(address, None)
            if not old or old != item:
                self._log_failure(
                    f"Received unequipped message with mismatched item: {item_link.item_id}"
                )
            return True

        return False

    def _log_failure(self, message: str) -> None:
        log.error(message)
        self.failures.append(message)
