"""Live inventory view built entirely on eqclient4's existing packet structs.

Use OP_CharInventory as an authoritative snapshot. ItemPacket corrects a slot;
MoveItem predicts a move when the caller chooses to apply it. There is no
network/acknowledgment policy in this module.

InventorySlot is the wire-address type, *not* eqclient4.journal.InventorySlot.
Item instances are the existing eqclient4.structs.items.Item objects.
"""

from copy import copy
from dataclasses import dataclass, field
from struct import unpack_from
from typing import Iterator

from eqclient4.structs.items import (
    Item,
    OP_CancelTrade,
    OP_CharInventory,
    OP_DeleteItem,
    OP_FinishTrade,
    OP_ItemPacket,
    OP_MoveItem,
)
from eqclient4.structs.constants import CURSOR_SLOT, GENERAL_SLOTS
from eqclient4.structs.wire import EQStruct, InventorySlot

_WORN = (
    "Charm",
    "Left Ear",
    "Head",
    "Face",
    "Right Ear",
    "Neck",
    "Shoulders",
    "Arms",
    "Back",
    "Left Wrist",
    "Right Wrist",
    "Ranged",
    "Hands",
    "Primary",
    "Secondary",
    "Left Finger",
    "Right Finger",
    "Chest",
    "Legs",
    "Feet",
    "Waist",
    "Power Source",
    "Ammo",
)
_BANK_SLOTS = 24
_SHARED_BANK_SLOTS = 2

POSSESSIONS_ADDRESS = 0
BANK_ADDRESS = 1
SHARED_BANK_ADDRESS = 2
TRADE_ADDRESS = 3
WORLD_CONTAINER_ADDRESS = 4
LIMBO_ADDRESS = 5


def _item_address(item: Item) -> InventorySlot:
    """Read the existing serialized Item header, retaining its inventory type.

    Item.slot only contains a client-style integer. Its RoF2 item-header
    `_wire_prefix` retains: type:u8 at +25, main/sub/aug:i16 at +26/+28/+30.
    """
    header = item._wire_prefix
    if len(header) >= 32:
        main, sub, aug = unpack_from("<hhh", header, 26)
        return InventorySlot(header[25], 0, main, sub, aug, 0)
    return InventorySlot.for_client(0, item.slot)


def _child_address(parent: InventorySlot, item: Item, child: Item) -> InventorySlot:
    index = child._entry_index
    if index < 0:
        raise ValueError(f"Negative item child index: {index}")
    if parent.aug_index != -1:
        raise ValueError("InventorySlot cannot represent nested augmentation sockets")
    if item.bag_slots > 0:
        if parent.sub_index != -1:
            raise ValueError("InventorySlot cannot represent bags nested within bags")
        return InventorySlot(parent.type, 0, parent.main_slot, index, -1, 0)
    return InventorySlot(parent.type, 0, parent.main_slot, parent.sub_index, index, 0)


def _format_item(item: Item, show_ids: bool) -> str:
    label = item.name
    if show_ids:
        label += f" [#{item.item_id}]"
    if item.stack > 1:
        label += f" x{item.stack}"
    return label


def _format_address(address: InventorySlot) -> str:
    number = address.main_slot
    if address.type == 0:
        if 0 <= number < len(_WORN):
            result = _WORN[number]
        elif number in GENERAL_SLOTS:
            result = f"General {number - GENERAL_SLOTS.start + 1}"
        elif number == CURSOR_SLOT:
            result = "Cursor"
        else:
            result = f"Possessions {number}"
    else:
        label = {1: "Bank", 2: "Shared Bank", 3: "Trade"}.get(address.type, f"Type {address.type}")
        result = f"{label} {number + 1}"
    if address.sub_index >= 0:
        result += f" / Cell {address.sub_index + 1}"
    if address.aug_index >= 0:
        result += f" / Aug {address.aug_index + 1}"
    return result


@dataclass(frozen=True)
class InventoryEvent:
    action: str
    message: str
    source: InventorySlot | None = None
    destination: InventorySlot | None = None
    changed: bool = False

    def __str__(self) -> str:
        return f"{self.action}: {self.message}"


@dataclass
class CharacterInventory:
    """Stateful collection of the *existing* Item objects indexed by InventorySlot.

    All `slots` keys are canonical InventorySlot values. A bag and its contents
    are individually indexed, while `Item.children` remains a linked hierarchy.
    A move changes the index but intentionally does not rewrite an Item's original
    received packet header; the mapping key is the current location.
    """

    slots: dict[InventorySlot, Item] = field(default_factory=dict)
    changes: list[InventoryEvent] = field(default_factory=list)

    @classmethod
    def from_packet(cls, packet: OP_CharInventory) -> CharacterInventory:
        inventory = cls()
        inventory.load(packet)
        return inventory

    @classmethod
    def from_payload(cls, payload: bytes) -> CharacterInventory:
        return cls.from_packet(OP_CharInventory.deserialize(payload))

    @staticmethod
    def address(kind: int, slot: int) -> InventorySlot:
        """Build a typed address using native RoF2 slot numbers (cursor=33)."""
        return InventorySlot.for_client(kind, slot)

    @staticmethod
    def cell(parent: InventorySlot, index: int) -> InventorySlot:
        """Build the address for a zero-based bag cell (any inventory type)."""
        if parent.sub_index != -1 or parent.aug_index != -1 or index < 0:
            raise ValueError("Expected a top-level bag and nonnegative cell index")
        return InventorySlot(parent.type, 0, parent.main_slot, index, -1, 0)

    def get(self, address: InventorySlot) -> Item | None:
        return self.slots.get(address)

    def __getitem__(self, address: InventorySlot) -> Item:
        return self.slots[address]

    def items(self) -> Iterator[tuple[InventorySlot, Item]]:
        yield from sorted(
            self.slots.items(),
            key=lambda row: (
                row[0].type,
                row[0].main_slot,
                row[0].sub_index,
                row[0].aug_index,
            ),
        )

    def _event(
        self,
        action: str,
        message: str,
        source: InventorySlot | None = None,
        destination: InventorySlot | None = None,
        changed: bool = False,
    ) -> InventoryEvent:
        event = InventoryEvent(action, message, source, destination, changed)
        self.changes.append(event)
        return event

    def _descendant_keys(self, address: InventorySlot) -> list[InventorySlot]:
        if address.aug_index >= 0:
            return []
        if address.sub_index >= 0:
            return [
                other
                for other in self.slots
                if other.type == address.type
                and other.main_slot == address.main_slot
                and other.sub_index == address.sub_index
                and other.aug_index >= 0
            ]
        return [
            other
            for other in self.slots
            if other.type == address.type
            and other.main_slot == address.main_slot
            and other != address
        ]

    def _take(self, address: InventorySlot) -> dict[InventorySlot, Item]:
        """Take one item and its descendants from the index as one unit."""
        result: dict[InventorySlot, Item] = {}
        for key in (address, *self._descendant_keys(address)):
            item = self.slots.pop(key, None)
            if item is not None:
                result[key] = item
        return result

    def _index(self, address: InventorySlot, item: Item) -> None:
        if address in self.slots:
            raise ValueError(f"Duplicate inventory item at {_format_address(address)}")
        self.slots[address] = item
        for child in item.children:
            self._index(_child_address(address, item, child), child)

    def _upsert(self, address: InventorySlot, item: Item) -> None:
        """Apply an item update, retaining bag contents if omitted by update."""
        old = self.slots.get(address)
        if old is not None and (old.item_id != item.item_id or item.children):
            self._take(address)
        else:
            self.slots.pop(address, None)
        self._index(address, item)
        self._relink()

    def _relink(self) -> None:
        """Make Item.children agree with the address index after a mutation."""
        # Note: many ItemPacket updates omit nested children. Preserve already
        # indexed children and relink them to the newly received parent Item.
        for address, item in list(self.slots.items()):
            if address.aug_index >= 0:
                item.children = []
                continue
            if item.bag_slots > 0 and address.sub_index == -1:
                children = sorted(
                    (
                        (key.sub_index, child)
                        for key, child in self.slots.items()
                        if key.type == address.type
                        and key.main_slot == address.main_slot
                        and key.sub_index >= 0
                        and key.aug_index == -1
                    ),
                )
            else:
                children = sorted(
                    (
                        (key.aug_index, child)
                        for key, child in self.slots.items()
                        if key.type == address.type
                        and key.main_slot == address.main_slot
                        and key.sub_index == address.sub_index
                        and key.aug_index >= 0
                    ),
                )
            item.children = [child for _, child in children]
            for index, child in children:
                child._entry_index = index

    def load(self, packet: OP_CharInventory) -> InventoryEvent:
        """Replace all state from an authoritative OP_CharInventory snapshot."""
        self.slots.clear()
        for item in packet.items:
            self._index(_item_address(item), item)
        self._relink()
        return self._event("snapshot", f"Loaded {len(self.slots)} items", changed=True)

    def apply(self, packet: EQStruct) -> InventoryEvent:
        """Apply one packet *now*; scheduling/connection checks belong to caller."""
        match packet:
            case OP_CharInventory():
                return self.load(packet)
            case OP_ItemPacket():
                return self._received_item(packet.item)
            case OP_MoveItem():
                return self._move(packet)
            case OP_DeleteItem():
                return self._delete(packet)
            case OP_FinishTrade():
                return self.clear_trade("trade-cleared")
            case OP_CancelTrade():
                return self.clear_trade("trade-cancelled")
            case _:
                return self._event("ignored", f"{type(packet).__name__} is not an inventory update")

    def clear_trade(self) -> None:
        for slot in list(self.slots):
            if slot.type == 3:
                del self.slots[slot]

    def clear_trade(self, action: str) -> InventoryEvent:
        removed = [(address, item) for address, item in self.slots.items() if address.type == 3]

        for address, _ in removed:
            del self.slots[address]

        if removed:
            self._relink()

        description = (
            ", ".join(
                f"{_format_item(item, True)} from {_format_address(address)}"
                for address, item in removed
            )
            or "Trade window already empty"
        )

        return self._event(
            action,
            description,
            source=removed[0][0] if len(removed) == 1 else None,
            changed=bool(removed),
        )

    def _received_item(self, item: Item) -> InventoryEvent:
        valid_destinations = (
            POSSESSIONS_ADDRESS,
            BANK_ADDRESS,
            SHARED_BANK_ADDRESS,
            TRADE_ADDRESS,
            LIMBO_ADDRESS,
        )
        if not item.address or item.address.type not in valid_destinations:
            return self._event(
                "ignored", f"{item.name}: non-inventory ItemPacket kind={item.kind:#x}"
            )

        address = item.address
        previous = self.get(address)
        self._upsert(address, item)
        action = "updated" if previous else "received"
        return self._event(
            "item",
            f"{action} {_format_item(item, True)} at {_format_address(address)}",
            destination=address,
            changed=True,
        )

    @staticmethod
    def _packet_address(packet: OP_MoveItem | OP_DeleteItem, side: str) -> InventorySlot:
        raw = getattr(packet, f"{side}_address", None)
        if raw:
            return raw
        return InventorySlot.for_client(
            getattr(packet, f"{side}_type"),
            getattr(packet, f"{side}_slot"),
        )

    def _delete(self, packet: OP_DeleteItem) -> InventoryEvent:
        address = self._packet_address(packet, "from")
        item = self.get(address)
        if item is None:
            return self._event("unresolved", f"Unknown {_format_address(address)}", source=address)
        count = packet.count or 0
        if 0 < count < item.stack:
            item.stack -= count
            return self._event(
                "consumed",
                f"{count} x {item.name} at {_format_address(address)}",
                source=address,
                changed=True,
            )
        self._take(address)
        self._relink()
        return self._event(
            "deleted",
            f"{_format_item(item, True)} at {_format_address(address)}",
            source=address,
            changed=True,
        )

    @staticmethod
    def _rebase(source: InventorySlot, target: InventorySlot, key: InventorySlot) -> InventorySlot:
        """Move the complete bag/augment subtree to a different parent slot."""
        if key == source:
            return target
        # Direct augmentation children occupy the source's own subslot;
        # descendants of a bag occupy their own distinct cell indices.
        sub = target.sub_index if key.sub_index == source.sub_index else key.sub_index
        return InventorySlot(target.type, 0, target.main_slot, sub, key.aug_index, 0)

    def _place(
        self, source: InventorySlot, target: InventorySlot, tree: dict[InventorySlot, Item]
    ) -> None:
        for address, item in tree.items():
            self.slots[self._rebase(source, target, address)] = item

    def _move(self, packet: OP_MoveItem) -> InventoryEvent:
        source = self._packet_address(packet, "from")
        destination = self._packet_address(packet, "to")
        if source == destination:
            return self._event(
                "unchanged", "Source and destination are identical", source, destination
            )

        item = self.get(source)
        if item is None:
            return self._event(
                "unresolved", f"Unknown {_format_address(source)}", source, destination
            )

        # Received a delete from server
        if destination.type == -1 and destination.main_slot == -1:
            self._take(source)
            self._relink()

            return self._event(
                "removed",
                f"{_format_item(item, True)} from {_format_address(source)}",
                source=source,
                changed=True,
            )

        other = self.get(destination)
        count = packet.count
        if count < 0 or (count > 0 and count > item.stack):
            return self._event("unresolved", f"Invalid stack count {count}", source, destination)
        if source.type == destination.type and source.main_slot == destination.main_slot:
            # Disallow moving an item into its own descendant (or vice versa).
            if source.sub_index == -1 or destination.sub_index == -1:
                return self._event(
                    "unresolved", "Overlapping source/destination subtree", source, destination
                )
        if count > 0 and other is not None and other.item_id != item.item_id:
            return self._event(
                "unresolved", "Cannot stack different item types", source, destination
            )
        if count > 0 and item.bag_slots:
            return self._event("unresolved", "Cannot split a container", source, destination)

        if count > 0 and count < item.stack:
            if other is None:
                cloned = copy(item)
                cloned.children = []
                cloned.stack = count
                self.slots[destination] = cloned
            else:
                other.stack += count
            item.stack -= count
            self._relink()
            return self._event(
                "split",
                f"{count} x {item.name}: {_format_address(source)} -> {_format_address(destination)}",
                source,
                destination,
                True,
            )

        if count > 0 and other is not None:
            other.stack += count
            self._take(source)
            self._relink()
            return self._event(
                "merged",
                f"{count} x {item.name}: {_format_address(source)} -> {_format_address(destination)}",
                source,
                destination,
                True,
            )

        moving = self._take(source)
        displaced = self._take(destination) if other is not None else {}
        self._place(source, destination, moving)
        if displaced:
            self._place(destination, source, displaced)
        self._relink()
        return self._event(
            "swapped" if displaced else "moved",
            f"{_format_item(item, True)}: {_format_address(source)} -> {_format_address(destination)}",
            source,
            destination,
            True,
        )

    def _render_descendants(
        self,
        lines: list[str],
        parent: InventorySlot,
        item: Item,
        prefix: str,
        shown: set[InventorySlot],
        show_empty: bool,
        show_ids: bool,
    ) -> None:
        if item.bag_slots and parent.sub_index == -1 and parent.aug_index == -1:
            # Display the capacity, including empty cells.
            children = [(index, self.cell(parent, index)) for index in range(item.bag_slots)]
            for index, address in children:
                child = self.get(address)
                shown.add(address)
                if child is None and not show_empty:
                    continue

                lines.append(
                    f"{prefix}|-- ({index + 1:02d} | {_slot_id(address)}) "
                    + (_format_item(child, show_ids) if child else "(empty)")
                )
                if child:
                    self._render_descendants(
                        lines, address, child, prefix + "|   ", shown, show_empty, show_ids
                    )
        else:
            # Existing Item.children augments map to aug_index on the same slot.
            augments = sorted(
                (
                    addr
                    for addr in self.slots
                    if addr.type == parent.type
                    and addr.main_slot == parent.main_slot
                    and addr.sub_index == parent.sub_index
                    and addr.aug_index >= 0
                ),
                key=lambda a: a.aug_index,
            )
            for address in augments:
                child = self.slots[address]
                shown.add(address)
                lines.append(
                    f"{prefix}`-- [Aug {address.aug_index + 1}] {_format_item(child, show_ids)}"
                )

    def render(
        self,
        *,
        show_empty: bool = True,
        show_ids: bool = True,
        show_bank_empty: bool = False,
        expand_bags: bool = True,
    ) -> str:
        lines = ["CHARACTER INVENTORY", "=" * 62]
        shown: set[InventorySlot] = set()

        def show(address: InventorySlot, label: str) -> None:
            shown.add(address)
            item = self.get(address)
            if not item and not show_empty:
                return

            lines.append(
                f"{label:<22} [{_slot_id(address)}] "
                + (_format_item(item, show_ids) if item else "(empty)")
            )
            if item and expand_bags:
                self._render_descendants(lines, address, item, "  ", shown, show_empty, show_ids)

        lines.extend(("", "[WORN]"))
        for index, name in enumerate(_WORN):
            show(self.address(0, index), f"{name} ({index:02d})")
        lines.extend(("", "[GENERAL]"))
        for index in GENERAL_SLOTS:
            show(
                self.address(0, index),
                f"General {index - GENERAL_SLOTS.start + 1} ({index})",
            )
        show(self.address(0, CURSOR_SLOT), f"Cursor ({CURSOR_SLOT})")

        for kind, name, capacity in (
            (1, "BANK", _BANK_SLOTS),
            (2, "SHARED BANK", _SHARED_BANK_SLOTS),
        ):
            lines.extend(("", f"[{name}]"))
            before = len(lines)
            for index in range(capacity):
                address = self.address(kind, index)
                if self.get(address) is not None or show_bank_empty:
                    show(address, f"Slot {index + 1} ({index})")
            if before == len(lines):
                lines.append("  (empty or not yet loaded)")

        extras = [(key, item) for key, item in self.items() if key not in shown]
        if extras:
            lines.extend(("", "[OTHER / UNATTACHED]"))
            for address, item in extras:
                lines.append(f"{_format_address(address):<22} {_format_item(item, show_ids)}")
        return "\n".join(lines)

    def render_change(self, event: InventoryEvent) -> str:
        lines = [str(event)]
        seen: set[InventorySlot] = set()
        for address in (event.source, event.destination):
            if address is None or address in seen:
                continue
            seen.add(address)
            item = self.get(address)
            lines.append(
                f"  {_format_address(address):<26}"
                + (_format_item(item, True) if item else "(empty)")
            )
            if item:
                self._render_descendants(lines, address, item, "    ", set(), False, True)
        return "\n".join(lines)

    def __str__(self) -> str:
        return self.render()


def _slot_id(address: InventorySlot) -> str:
    if address.type == 0:
        return str(address.client_slot)

    kind = {
        1: "B",
        2: "SB",
        3: "T",
    }.get(address.type, f"T{address.type}")

    if address.sub_index >= 0:
        return f"{kind}:{address.main_slot}:{address.sub_index}"

    return f"{kind}:{address.main_slot}"
