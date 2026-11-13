import struct
from collections.abc import Generator
from dataclasses import dataclass, field

from eqclient4.structs.wire import (
    EQStruct,
    InventorySlot,
    TypelessInventorySlot,
    advance,
    cstring,
    exact,
    i32,
    need,
    pack_names,
    put_cstr,
    read_u32,
    two_names,
    u32,
)

# common/patches/rof2_structs.h:4977 ItemQuaternaryBodyStruct, packed.
_QUATERNARY = 171

ITEM_MERCHANT = 0x64  # 100
ITEM_LOOT = 0x66  # 102
ITEM_TRADE = 0x67  # 103
ITEM_INVENTORY = 0x69  # 105
ITEM_SUMMON = 0x6A  # 106


# Replacement for _pack_item_body, _read_item, AugmentSocket, the field tables,
# and Item in eqclient4/structs/items.py.
# Assumes existing imports: struct, dataclass, field, EQStruct, InventorySlot,
# advance, cstring, need, put_cstr, read_u32, u32, and ITEM_MERCHANT.

SECTION_SIZES = {
    "header": 77,
    "finish": 26,
    "body": 255,
    "secondary": 74,
    "tertiary": 76,
    "quaternary": 171,
}
ADDRESS_LAYOUT = ("header", "<Bhhh", 25)
AUGMENT_LAYOUT = ("secondary", "<IBB", 12)
NO_RENT_OFFSET = 8
MERCHANT_SLOT_OFFSET = 36
EVOLVING_FLAG_OFFSET = 76
ITEM_MERCHANT = 0x64
ITEM_LOOT = 0x66
ITEM_TRADE = 0x67
ITEM_INVENTORY = 0x69
ITEM_SUMMON = 0x6A


@dataclass(frozen=True)
class AugmentSocket:
    type: int = 0
    visible: int = 0
    unknown: int = 0


ITEM_EFFECT_FIELDS = (
    "click_effect",
    "proc_effect",
    "worn_effect",
    "focus_effect",
    "scroll_effect",
    "bard_effect",
)

# Single source of truth: attribute -> (section, wire format, section-relative offset).
# A section's start (including each variable-position effect) is stored in
# _wire_offsets. All reads and writes use this layout.
ITEM_FIELD_LAYOUT: dict[str, tuple[str, str, int]] = {
    # ItemSerializationHeader (77 bytes)
    "stack": ("header", "<I", 17),
    "price": ("header", "<I", 32),
    "charges": ("header", "<i", 56),
    "attuned": ("header", "<I", 60),
    # ItemBodyStruct (255 bytes)
    "item_id": ("body", "<I", 0),
    "weight": ("body", "<i", 4),
    "no_drop": ("body", "<B", 9),  # Wire 0 = No Drop; 255 = droppable
    "size": ("body", "<B", 11),
    "slots": ("body", "<I", 12),
    "resist_cold": ("body", "<b", 31),
    "resist_disease": ("body", "<b", 32),
    "resist_poison": ("body", "<b", 33),
    "resist_magic": ("body", "<b", 34),
    "resist_fire": ("body", "<b", 35),
    "resist_corruption": ("body", "<b", 36),
    "strength": ("body", "<b", 37),
    "stamina": ("body", "<b", 38),
    "agility": ("body", "<b", 39),
    "dexterity": ("body", "<b", 40),
    "charisma": ("body", "<b", 41),
    "intelligence": ("body", "<b", 42),
    "wisdom": ("body", "<b", 43),
    "hp": ("body", "<i", 44),
    "mana": ("body", "<i", 48),
    "endurance": ("body", "<I", 52),
    "ac": ("body", "<i", 56),
    "_classes": ("body", "<I", 72),
    "races": ("body", "<I", 76),
    "deity": ("body", "<I", 80),
    "magic": ("body", "<B", 116),
    "required_level": ("body", "<I", 121),
    "recommended_level": ("body", "<I", 125),
    "delay": ("body", "<B", 142),
    "elemental_damage_type": ("body", "<B", 143),
    "elemental_damage": ("body", "<B", 144),
    "range": ("body", "<B", 145),
    "damage": ("body", "<I", 146),
    "prestige": ("body", "<I", 154),
    "item_type": ("body", "<B", 158),
    "shielding": ("body", "<i", 187),
    "avoidance": ("body", "<i", 211),
    "accuracy": ("body", "<i", 215),
    # ItemSecondaryBodyStruct (74 bytes)
    "aug_type": ("secondary", "<I", 0),
    "aug_restrict2": ("secondary", "<i", 4),
    "aug_restrict": ("secondary", "<I", 8),
    "bag_type": ("secondary", "<B", 68),
    "bag_slots": ("secondary", "<B", 69),
    "bag_size": ("secondary", "<B", 70),
    "bag_weight_reduction": ("secondary", "<B", 71),
    # ItemTertiaryBodyStruct (76 bytes)
    "lore_group": ("tertiary", "<i", 0),
    "attack": ("tertiary", "<i", 15),
    "haste": ("tertiary", "<i", 19),
    "damage_shield": ("tertiary", "<i", 23),
    "stack_size": ("tertiary", "<I", 50),
    "no_transfer": ("tertiary", "<B", 54),
    "item_class": ("finish", "<B", 25),
    # Six effects, each at an independently located offset, owing to C-strings
    **{name: (f"effect:{name}", "<i", 0) for name in ITEM_EFFECT_FIELDS},
}


@dataclass
class Item(EQStruct):
    kind: int
    slot: int
    name: str
    id_file: str
    item_id: int
    stack: int = 1
    slots: int = 0
    _classes: int = 0
    races: int = 0
    ac: int = 0
    damage: int = 0
    required_level: int = 0
    size: int = 0
    bag_slots: int = 0
    bag_size: int = 0
    item_type: int = 0
    scroll_effect: int = 0
    price: int = 0

    # Flags and inventory metadata
    no_drop: bool = False
    attuned: bool = False
    lore_group: int = 0
    weight: int = 0
    charges: int = 0
    stack_size: int = 0
    bag_type: int = 0
    bag_weight_reduction: int = 0
    no_transfer: bool = False

    # Weapons, statistics and restrictions
    delay: int = 0
    range: int = 0
    magic: int = 0
    elemental_damage_type: int = 0
    elemental_damage: int = 0
    strength: int = 0
    stamina: int = 0
    agility: int = 0
    dexterity: int = 0
    wisdom: int = 0
    intelligence: int = 0
    charisma: int = 0
    hp: int = 0
    mana: int = 0
    endurance: int = 0
    resist_magic: int = 0
    resist_fire: int = 0
    resist_cold: int = 0
    resist_poison: int = 0
    resist_disease: int = 0
    resist_corruption: int = 0
    deity: int = 0
    recommended_level: int = 0
    prestige: int = 0
    attack: int = 0
    haste: int = 0
    damage_shield: int = 0
    shielding: int = 0
    avoidance: int = 0
    accuracy: int = 0
    item_class: int = 0

    # Spell effects (scroll_effect stays in the legacy constructor above)
    click_effect: int = 0
    proc_effect: int = 0
    worn_effect: int = 0
    focus_effect: int = 0
    bard_effect: int = 0

    # Augment compatibility, not installed augment items (those are children)
    aug_type: int = 0
    aug_restrict: int = 0
    aug_restrict2: int = 0
    augment_slots: dict[int, AugmentSocket] = field(default_factory=dict)

    ornament_mainhand: str = ""
    ornament_offhand: str = ""

    address: InventorySlot | None = field(default=None, repr=False, compare=False)
    children: list[Item] = field(default_factory=list, repr=False, compare=False)
    _entry_index: int = field(default=0, repr=False, compare=False)
    _wire_prefix: bytes = field(default=b"", repr=False, compare=False)
    _wire_offsets: dict = field(default_factory=dict, repr=False, compare=False)
    _original_fields: dict = field(default_factory=dict, repr=False, compare=False)

    @property
    def is_lore(self) -> bool:
        return self.lore_group != 0

    @property
    def is_no_drop(self) -> bool:
        return self.no_drop or self.attuned

    @property
    def classes(self) -> list[int]:
        return [class_id for class_id in range(1, 17) if self._classes & (1 << (class_id - 1))]

    @classes.setter
    def classes(self, value: list[int] | int) -> None:
        match value:
            case list():
                for class_id in range(1, 17):
                    if class_id in value:
                        self._classes |= 1 << (class_id - 1)
                    else:
                        self._classes &= ~(1 << (class_id - 1))
            case int():
                self._classes = value
            case _:
                raise ValueError(f"Invalid classes value: {value}")

    @property
    def augments(self) -> dict[int, Item]:
        """Installed augments indexed by socket position."""
        if self.item_class != 0:
            return {}

        return {child._entry_index: child for child in self.children if 0 <= child._entry_index < 6}

    def _effective_address(self) -> InventorySlot:
        if self.address is None:
            return InventorySlot.for_client(9 if self.kind == ITEM_MERCHANT else 0, self.slot)
        original = self._original_fields
        if original and self.slot != original["slot"] and self.address == original["address"]:
            return InventorySlot.for_client(self.address.type, self.slot)
        return self.address

    @staticmethod
    def _wire_value(name: str, value: int | bool, fmt: str) -> int:
        """Map Python field semantics to a representable wire integer."""
        if name == "no_drop":
            return 0 if value else 255
        value = int(value)
        bits = struct.calcsize(fmt) * 8
        value &= (1 << bits) - 1
        if fmt[-1] in "bhi" and value >= (1 << (bits - 1)):
            value -= 1 << bits
        return value

    @staticmethod
    def _python_value(name: str, value: int) -> int | bool:
        if name == "no_drop":
            return value == 0
        if name in {"attuned", "no_transfer"}:
            return bool(value)
        return value

    @staticmethod
    def _pack_item_body(item: Item) -> bytes:
        """Construct a minimal, valid serialized item when there is no raw prefix."""
        buf = {
            "header": bytearray(SECTION_SIZES["header"]),
            "finish": bytearray(SECTION_SIZES["finish"]),
            "body": bytearray(SECTION_SIZES["body"]),
            "secondary": bytearray(SECTION_SIZES["secondary"]),
            "tertiary": bytearray(SECTION_SIZES["tertiary"]),
            **{f"effect:{name}": bytearray(35) for name in ITEM_EFFECT_FIELDS},
        }
        # The RoF2 body uses 255 for the *absence* of No Rent.
        buf["body"][NO_RENT_OFFSET] = 255
        # Server uses merchant_slot=1 for nonmerchant items.
        struct.pack_into("<I", buf["header"], MERCHANT_SLOT_OFFSET, 1)
        address = item._effective_address()
        address_section, address_fmt, address_delta = ADDRESS_LAYOUT
        struct.pack_into(
            address_fmt,
            buf[address_section],
            address_delta,
            address.type & 0xFF,
            address.main_slot,
            address.sub_index,
            address.aug_index,
        )

        for name, (section, fmt, delta) in ITEM_FIELD_LAYOUT.items():
            raw = Item._wire_value(name, getattr(item, name), fmt)
            if name == "stack":
                raw = max(1, raw)
            struct.pack_into(fmt, buf[section], delta, raw)

        if any(not 0 <= i < 6 for i in item.augment_slots):
            raise ValueError("Invalid augment socket index")

        aug_section, aug_fmt, aug_delta = AUGMENT_LAYOUT
        for i in range(6):
            socket = item.augment_slots.get(i, AugmentSocket(type=0, visible=1, unknown=0))
            struct.pack_into(
                aug_fmt,
                buf[aug_section],
                aug_delta + i * struct.calcsize(aug_fmt),
                socket.type,
                socket.visible,
                socket.unknown,
            )

        return b"".join(
            (
                buf["header"],
                put_cstr(item.ornament_mainhand),
                put_cstr(item.ornament_offhand),
                buf["finish"],
                put_cstr(item.name),
                put_cstr(""),
                put_cstr(item.id_file),
                put_cstr(""),
                buf["body"],
                put_cstr(""),
                buf["secondary"],
                put_cstr(""),
                buf["tertiary"],
                *(buf[f"effect:{name}"] for name in ITEM_EFFECT_FIELDS),
                bytes(SECTION_SIZES["quaternary"]),
                u32(0),
            )
        )

    @staticmethod
    def _read_item(data: bytes, offset: int, kind: int) -> tuple[Item, int]:
        """Parse one root item (including children), returning the next position."""
        begin = offset
        offsets: dict[str, int] = {"header": 0}

        offset = advance(data, offset, SECTION_SIZES["header"], "item header")
        if data[begin + offsets["header"] + EVOLVING_FLAG_OFFSET]:
            offset = advance(data, offset, 25, "evolving item")

        ornaments = {}
        for field_name in ("ornament_mainhand", "ornament_offhand"):
            offsets[f"{field_name}_start"] = offset - begin
            value, offset = cstring(data, offset)
            ornaments[field_name] = value
            offsets[f"{field_name}_end"] = offset - begin

        offsets["finish"] = offset - begin
        offset = advance(data, offset, SECTION_SIZES["finish"], "item header finish")

        name_start = offset
        name, offset = cstring(data, offset)

        offsets["name_start"] = name_start - begin
        offsets["name_end"] = offset - begin
        _, offset = cstring(data, offset)  # Lore display string
        id_start = offset
        id_file, offset = cstring(data, offset)

        offsets["id_file_start"] = id_start - begin
        offsets["id_file_end"] = offset - begin
        _, offset = cstring(data, offset)  # Blank field

        offsets["body"] = offset - begin
        offset = advance(data, offset, SECTION_SIZES["body"], "item body")
        _, offset = cstring(data, offset)  # Charm string

        offsets["secondary"] = offset - begin
        offset = advance(data, offset, SECTION_SIZES["secondary"], "item secondary body")
        _, offset = cstring(data, offset)  # Filename

        offsets["tertiary"] = offset - begin
        offset = advance(data, offset, SECTION_SIZES["tertiary"], "item tertiary body")

        for effect_name in ITEM_EFFECT_FIELDS:
            offsets[f"effect:{effect_name}"] = offset - begin
            offset = advance(data, offset, 30, f"{effect_name} header")
            _, offset = cstring(data, offset)  # Variable-length effect name
            offset = advance(data, offset, 4, f"{effect_name} trailer")

        offset = advance(data, offset, SECTION_SIZES["quaternary"], "item quaternary body")
        nested_count = read_u32(data, offset)
        offset = advance(data, offset, 4, "item child count")

        prefix_end = offset

        fields = {
            name: Item._python_value(
                name, struct.unpack_from(fmt, data, begin + offsets[section] + delta)[0]
            )
            for name, (section, fmt, delta) in ITEM_FIELD_LAYOUT.items()
        }

        # The protocol sometimes serializes zero stack quantity for unstackables.
        if not fields["stack"]:
            fields["stack"] = 1

        address_section, address_fmt, address_delta = ADDRESS_LAYOUT
        addr_type, main, sub, aug = struct.unpack_from(
            address_fmt, data, begin + offsets[address_section] + address_delta
        )
        address = InventorySlot(addr_type, 0, main, sub, aug, 0)

        aug_section, aug_fmt, aug_delta = AUGMENT_LAYOUT

        augment_slots = {
            i: socket
            for i in range(6)
            if (
                socket := AugmentSocket(
                    *struct.unpack_from(
                        aug_fmt,
                        data,
                        begin + offsets[aug_section] + aug_delta + i * struct.calcsize(aug_fmt),
                    )
                )
            ).type
            != 0
        }

        item = Item(
            kind=kind,
            slot=address.client_slot,
            name=name,
            id_file=id_file,
            address=address,
            augment_slots=augment_slots,
            ornament_mainhand=ornaments["ornament_mainhand"],
            ornament_offhand=ornaments["ornament_offhand"],
            **fields,  # type: ignore[arg-type]
        )
        item._wire_prefix = bytes(data[begin:prefix_end])
        item._wire_offsets = offsets

        item._original_fields = {}
        for name in (
            *ITEM_FIELD_LAYOUT,
            "slot",
            "address",
            "name",
            "id_file",
            "ornament_mainhand",
            "ornament_offhand",
        ):
            item._original_fields[name] = getattr(item, name)
        item._original_fields["augment_slots"] = dict(item.augment_slots)

        for _ in range(nested_count):
            entry_index = read_u32(data, offset)
            offset = advance(data, offset, 4, "item child index")
            child, offset = Item._read_item(data, offset, kind)
            child._entry_index = entry_index
            item.children.append(child)

        return item, offset

    def _serialize_body(self) -> bytes:
        if not self._wire_prefix:
            data = bytearray(Item._pack_item_body(self))
        else:
            data = bytearray(self._wire_prefix)
            offsets = self._wire_offsets
            original = self._original_fields

            for name, (section, fmt, delta) in ITEM_FIELD_LAYOUT.items():
                if getattr(self, name) != original[name]:
                    struct.pack_into(
                        fmt,
                        data,
                        offsets[section] + delta,
                        Item._wire_value(name, getattr(self, name), fmt),
                    )

            address = self._effective_address()
            if address != original["address"]:
                address_section, address_fmt, address_delta = ADDRESS_LAYOUT
                struct.pack_into(
                    address_fmt,
                    data,
                    offsets[address_section] + address_delta,
                    address.type & 0xFF,
                    address.main_slot,
                    address.sub_index,
                    address.aug_index,
                )

            if any(not 0 <= idx < 6 for idx in self.augment_slots):
                raise ValueError("Invalid augment socket index")

            if self.augment_slots != original["augment_slots"]:
                aug_section, aug_fmt, aug_delta = AUGMENT_LAYOUT

                for idx in range(6):
                    socket = self.augment_slots.get(
                        idx,
                        AugmentSocket(type=0, visible=1, unknown=0),
                    )

                    struct.pack_into(
                        aug_fmt,
                        data,
                        offsets[aug_section] + aug_delta + idx * struct.calcsize(aug_fmt),
                        socket.type,
                        socket.visible,
                        socket.unknown,
                    )

            # Apply variable-length edits in reverse byte order. Static offsets
            # above refer to the *original* data, before these replacements.
            edits = []
            for name in ("name", "id_file", "ornament_mainhand", "ornament_offhand"):
                if getattr(self, name) != original[name]:
                    edits.append(
                        (
                            offsets[f"{name}_start"],
                            offsets[f"{name}_end"],
                            put_cstr(getattr(self, name)),
                        )
                    )

            for start, end, value in sorted(edits, reverse=True):
                data[start:end] = value

        # Direct nested children are serialized after the root's fixed prefix.
        struct.pack_into("<I", data, len(data) - 4, len(self.children))
        for child in self.children:
            data += u32(child._entry_index)
            data += child._serialize_body()
        return bytes(data)

    def serialize(self) -> bytes:
        return u32(self.kind) + self._serialize_body()

    def walk(self) -> Generator[Item]:
        yield self
        for child in self.children:
            yield from child.walk()

    @classmethod
    def deserialize(cls, data: bytes) -> Item:
        need(data, 4, "item packet")
        item, end = cls._read_item(data, 4, read_u32(data))
        if end != len(data):
            raise ValueError(f"Item packet trailing data: {len(data) - end} bytes")
        return item


@dataclass
class OP_CharInventory(EQStruct):
    items: list[Item] = field(default_factory=list)

    @property
    def flat_items(self) -> list[Item]:
        """Compatibility view of the former flattened `items` list."""
        return [item for root in self.items for item in root.walk()]

    def serialize(self) -> bytes:
        # common/patches/rof2.cpp:1075 OP_CharInventory
        out = bytearray(struct.pack("<I", len(self.items)))
        for item in self.items:
            out += item._serialize_body()
        return bytes(out)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_CharInventory:
        need(data, 4, "OP_CharInventory")
        count = read_u32(data)
        offset = 4
        found: list[Item] = []
        for _index in range(count):
            item, offset = Item._read_item(data, offset, ITEM_INVENTORY)
            found.append(item)

        if offset != len(data):
            raise ValueError(f"OP_CharInventory trailing data: {len(data) - offset} bytes")
        return cls(found)


@dataclass
class OP_ItemPacket(EQStruct):
    item: Item

    def serialize(self) -> bytes:
        return self.item.serialize()

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ItemPacket:
        return cls(Item.deserialize(data))


@dataclass
class OP_DeleteItem(EQStruct):
    from_slot: int
    to_slot: int | None = None
    count: int | None = None
    from_type: int = 0
    to_type: int = 0
    # The observed short-form packet contains only a slot uint32.
    short_form: bool = False
    from_address: InventorySlot | None = field(default=None, repr=False, compare=False)
    to_address: InventorySlot | None = field(default=None, repr=False, compare=False)

    def serialize(self) -> bytes:
        if self.short_form:
            return u32(self.from_slot)
        if self.from_address:
            source = self.from_address.preserve_inventory_slot(self.from_type, self.from_slot)
        else:
            source = InventorySlot.for_client(self.from_type, self.from_slot)

        if self.to_address:
            dest = self.to_address.preserve_inventory_slot(self.to_type, self.to_slot or 0)
        else:
            dest = InventorySlot.for_client(self.to_type, self.to_slot or 0)

        return source.pack() + dest.pack() + u32(self.count or 0)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_DeleteItem:
        if len(data) == 4:
            return cls(read_u32(data), short_form=True)
        if len(data) != 28:
            raise ValueError(f"OP_DeleteItem expected 4 or 28 bytes, got {len(data)}")
        source = InventorySlot.unpack(data, 0)
        dest = InventorySlot.unpack(data, 12)
        return cls(
            source.client_slot,
            dest.client_slot,
            read_u32(data, 24),
            source.type,
            dest.type,
            False,
            source,
            dest,
        )


@dataclass
class OP_MoveItem(EQStruct):
    from_slot: int
    to_slot: int
    count: int = 0
    to_type: int = 0
    from_type: int = 0
    from_address: InventorySlot | None = field(default=None, repr=False, compare=False)
    to_address: InventorySlot | None = field(default=None, repr=False, compare=False)

    def serialize(self) -> bytes:
        if self.from_address:
            source = self.from_address.preserve_inventory_slot(self.from_type, self.from_slot)
        else:
            source = InventorySlot.for_client(self.from_type, self.from_slot)
        if self.to_address:
            dest = self.to_address.preserve_inventory_slot(self.to_type, self.to_slot)
        else:
            dest = InventorySlot.for_client(self.to_type, self.to_slot)
        return source.pack() + dest.pack() + u32(self.count)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_MoveItem:
        exact(data, 28, "OP_MoveItem")
        source = InventorySlot.unpack(data, 0)
        dest = InventorySlot.unpack(data, 12)
        return cls(
            source.client_slot,
            dest.client_slot,
            read_u32(data, 24),
            dest.type,
            source.type,
            source,
            dest,
        )


@dataclass
class OP_LootRequest(EQStruct):
    spawn_id: int

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:84 EntityId_Struct
        return struct.pack("<I", self.spawn_id & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_LootRequest:
        need(data, 4, "OP_LootRequest")
        return cls(read_u32(data))


@dataclass
class OP_EndLootRequest(EQStruct):
    spawn_id: int

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:84 EntityId_Struct
        return struct.pack("<I", self.spawn_id & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_EndLootRequest:
        need(data, 4, "OP_EndLootRequest")
        return cls(read_u32(data))


@dataclass
class OP_LootItem(EQStruct):
    corpse_id: int
    player_id: int
    slot: int
    auto_loot: int = 0
    unknown10: int = 0
    unknown16: int = 0

    def serialize(self) -> bytes:
        # common/patches/rof2_structs.h:2058 LootingItem_Struct
        return struct.pack(
            "<IIHHiI",
            self.corpse_id & 0xFFFFFFFF,
            self.player_id & 0xFFFFFFFF,
            self.slot & 0xFFFF,
            self.unknown10 & 0xFFFF,
            i32(self.auto_loot),
            self.unknown16 & 0xFFFFFFFF,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_LootItem:
        exact(data, 20, "OP_LootItem")
        corpse_id, player_id, slot, unknown10, auto_loot, unknown16 = struct.unpack_from(
            "<IIHHiI", data
        )
        return cls(corpse_id, player_id, slot, auto_loot, unknown10, unknown16)


@dataclass
class OP_MoneyOnCorpse(EQStruct):
    response: int = 0
    platinum: int = 0
    gold: int = 0
    silver: int = 0
    copper: int = 0
    unknown01: int = 0x42
    unknown02: int = 0xEF
    unknown03: int = 0
    packet_size: int = field(default=20, repr=False, compare=False)

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:1829 moneyOnCorpseStruct. zone/corpse.cpp:1280 writes 0x42, 0xef.
        if self.packet_size == 0:
            return b""
        if self.packet_size == 1:
            return bytes((self.response & 0xFF,))
        if self.packet_size != 20:
            raise ValueError("OP_MoneyOnCorpse packet_size must be 0, 1 or 20")

        return struct.pack(
            "<BBBBIIII",
            self.response & 0xFF,
            self.unknown01 & 0xFF,
            self.unknown02 & 0xFF,
            self.unknown03 & 0xFF,
            self.platinum & 0xFFFFFFFF,
            self.gold & 0xFFFFFFFF,
            self.silver & 0xFFFFFFFF,
            self.copper & 0xFFFFFFFF,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_MoneyOnCorpse:

        if len(data) == 0:
            return cls(packet_size=0)
        if len(data) == 1:
            return cls(response=data[0], packet_size=1)
        if len(data) != 20:
            raise ValueError(f"OP_MoneyOnCorpse expected 0, 1 or 20 bytes, got {len(data)}")
        a, b, c, d, pp, gp, sp, cp = struct.unpack("<BBBBIIII", data)
        return cls(a, pp, gp, sp, cp, b, c, d, packet_size=20)


@dataclass
class OP_CorpseDrag(EQStruct):
    corpse: str
    dragger: str
    trailing: bytes = b"\x00" * 24
    _raw_names: bytes = field(default=b"", repr=False, compare=False)
    _original_names: tuple[str, str] | None = field(default=None, repr=False, compare=False)

    def serialize(self) -> bytes:
        exact(self.trailing, 24, "OP_CorpseDrag trailing")
        if self._original_names == (self.corpse, self.dragger) and len(self._raw_names) == 128:
            names = self._raw_names
        else:
            names = pack_names(self.corpse, self.dragger, 128)
        return names + self.trailing

    @classmethod
    def deserialize(cls, data: bytes) -> OP_CorpseDrag:
        exact(data, 152, "OP_CorpseDrag")
        corpse, dragger = two_names(data)
        return cls(corpse, dragger, data[128:], data[:128], (corpse, dragger))


@dataclass
class OP_ShopRequest(EQStruct):
    npc_id: int
    player_id: int
    command: int
    rate: float = 0.0
    tab_display: int = 0
    unknown20: int = 0

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:2136 MerchantClick_Struct
        return struct.pack(
            "<IIIfii",
            self.npc_id & 0xFFFFFFFF,
            self.player_id & 0xFFFFFFFF,
            self.command & 0xFFFFFFFF,
            self.rate,
            i32(self.tab_display),
            i32(self.unknown20),
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ShopRequest:
        exact(data, 24, "OP_ShopRequest")
        return cls(*struct.unpack("<IIIfii", data))


@dataclass
class OP_ShopPlayerBuy(EQStruct):
    npc_id: int
    player_id: int
    slot: int
    unknown: int = 0
    quantity: int = 1
    price: int = 0
    unknown20: int = 0
    unknown28: int = 0

    def serialize(self) -> bytes:
        # common/patches/rof2_structs.h:2284 Merchant_Sell_Struct
        return struct.pack(
            "<8I",
            self.npc_id & 0xFFFFFFFF,
            self.player_id & 0xFFFFFFFF,
            self.slot & 0xFFFFFFFF,
            self.unknown & 0xFFFFFFFF,
            self.quantity & 0xFFFFFFFF,
            self.unknown20 & 0xFFFFFFFF,
            self.price & 0xFFFFFFFF,
            self.unknown28 & 0xFFFFFFFF,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ShopPlayerBuy:
        exact(data, 32, "OP_ShopPlayerBuy")
        npc, player, slot, unknown, quantity, gap, price, tail = struct.unpack("<8I", data)
        return cls(
            npc,
            player,
            slot,
            unknown,
            quantity,
            price,
            gap,
            tail,
        )


@dataclass
class OP_ShopPlayerSell(EQStruct):
    npc_id: int
    slot: int
    quantity: int
    price: int = 0
    slot_address: TypelessInventorySlot | None = field(default=None, repr=False, compare=False)

    def serialize(self) -> bytes:
        # common/patches/rof2_structs.h:2297 Merchant_Purchase_Struct
        # common/patches/rof2_structs.h:71 TypelessInventorySlot_Struct
        if self.slot_address:
            address = self.slot_address.preserve_typeless_slot(self.slot)
        else:
            address = TypelessInventorySlot.for_client(self.slot)

        return (
            u32(self.npc_id)
            + address.pack()
            + struct.pack(
                "<II",
                self.quantity & 0xFFFFFFFF,
                self.price & 0xFFFFFFFF,
            )
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ShopPlayerSell:
        exact(data, 20, "OP_ShopPlayerSell")
        npc_id = read_u32(data)
        address = TypelessInventorySlot.unpack(data, 4)
        quantity, price = struct.unpack_from("<II", data, 12)
        return cls(npc_id, address.client_slot, quantity, price, address)


@dataclass
class OP_ShopDelItem(EQStruct):
    npc_id: int
    player_id: int
    slot: int
    unknown12: int = 0

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:2242 Merchant_DelItem_Struct
        return struct.pack(
            "<4I",
            self.npc_id & 0xFFFFFFFF,
            self.player_id & 0xFFFFFFFF,
            self.slot & 0xFFFFFFFF,
            self.unknown12 & 0xFFFFFFFF,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ShopDelItem:
        if len(data) == 12:
            return cls(*struct.unpack("<3I", data))
        exact(data, 16, "OP_ShopDelItem")
        return cls(*struct.unpack("<4I", data))


class OP_ShopEnd(EQStruct):
    pass


class OP_ShopEndConfirm(EQStruct):
    pass


@dataclass
class OP_TradeRequest(EQStruct):
    to_id: int
    from_id: int

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:2582 TradeRequest_Struct
        return struct.pack("<II", self.to_id & 0xFFFFFFFF, self.from_id & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_TradeRequest:
        need(data, 8, "OP_TradeRequest")
        to_id, from_id = struct.unpack_from("<II", data)
        return cls(int(to_id), int(from_id))


@dataclass
class OP_TradeRequestAck(EQStruct):
    from_id: int
    to_id: int

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:2582 TradeRequest_Struct
        return struct.pack("<II", self.from_id & 0xFFFFFFFF, self.to_id & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_TradeRequestAck:
        need(data, 8, "OP_TradeRequestAck")
        from_id, to_id = struct.unpack_from("<II", data)
        return cls(int(from_id), int(to_id))


@dataclass
class OP_CancelTrade(EQStruct):
    from_id: int
    action: int = 1

    def serialize(self) -> bytes:
        # common/patches/rof2.cpp:977 OP_CancelTrade. Wire struct is common/patches/rof2_structs.h:2717.
        return struct.pack("<II", self.from_id & 0xFFFFFFFF, self.action & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_CancelTrade:
        need(data, 8, "OP_CancelTrade")
        from_id, action = struct.unpack_from("<II", data)
        return cls(int(from_id), int(action))


@dataclass
class OP_TradeSkillCombine(EQStruct):
    container_slot: int
    guildtribute_slot: int = 0
    container_type: int = 0
    guildtribute_type: int = 0
    container_address: InventorySlot | None = field(default=None, repr=False, compare=False)
    guildtribute_address: InventorySlot | None = field(default=None, repr=False, compare=False)

    def serialize(self) -> bytes:
        # common/patches/rof2_structs.h:3933 NewCombine_Struct
        if self.container_address:
            container = self.container_address.preserve_inventory_slot(
                self.container_type, self.container_slot
            )
        else:
            container = InventorySlot.for_client(self.container_type, self.container_slot)
        if self.guildtribute_address:
            tribute = self.guildtribute_address.preserve_inventory_slot(
                self.guildtribute_type, self.guildtribute_slot
            )
        else:
            tribute = InventorySlot.for_client(self.guildtribute_type, self.guildtribute_slot)

        return container.pack() + tribute.pack()

    @classmethod
    def deserialize(cls, data: bytes) -> OP_TradeSkillCombine:
        exact(data, 24, "OP_TradeSkillCombine")
        container = InventorySlot.unpack(data, 0)
        tribute = InventorySlot.unpack(data, 12)
        return cls(
            container.client_slot,
            tribute.client_slot,
            container.type,
            tribute.type,
            container,
            tribute,
        )


@dataclass
class OP_TradeAcceptClick(EQStruct):
    from_mob_id: int = 0
    unknown4: int = 0

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:2588 TradeAccept_Struct
        return struct.pack("<II", self.from_mob_id & 0xFFFFFFFF, self.unknown4 & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_TradeAcceptClick:
        need(data, 8, "OP_TradeAcceptClick")
        from_mob_id, unknown4 = struct.unpack_from("<II", data)
        return cls(int(from_mob_id), int(unknown4))


@dataclass
class OP_FinishTrade(EQStruct):
    """The server closed the trade. The body is ignored."""

    payload: bytes = b""

    def serialize(self) -> bytes:
        return self.payload

    @classmethod
    def deserialize(cls, data: bytes) -> OP_FinishTrade:
        return cls(bytes(data))
