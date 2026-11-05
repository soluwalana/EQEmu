import struct
from dataclasses import dataclass, field

from eqclient4.structs.wire import (
    EQStruct,
    advance,
    client_slot,
    cstring,
    from_rof2_slot,
    i16,
    i32,
    need,
    pack_inventory_slot,
    pack_names,
    pack_typed_slot,
    put_cstr,
    read_u32,
    to_rof2_slot,
    two_names,
    u32,
    unpack_inventory_slot,
    InventorySlot,
    TypelessInventorySlot,
    inventory_wire,
    exact,
)

# common/patches/rof2_structs.h:4977 ItemQuaternaryBodyStruct, packed.
_QUATERNARY = 171

ITEM_MERCHANT = 0x64
ITEM_LOOT = 0x66
ITEM_TRADE = 0x67
ITEM_INVENTORY = 0x69
ITEM_SUMMON = 0x6A


def _pack_item_body(item: Item) -> bytes:
    """RoF2 SerializeItem for the fields this client reads back."""
    wire = to_rof2_slot(item.slot) if item.kind != ITEM_MERCHANT else item.slot
    wire, sub = inventory_wire(item.slot) if item.kind != ITEM_MERCHANT else (item.slot, -1)

    # common/patches/rof2_structs.h:4733 ItemSerializationHeader
    header = struct.pack(
        "<17sIIBHHHIIIIIIIIIIIB",
        b"\x00" * 17,
        max(1, int(item.stack)) & 0xFFFFFFFF,
        0,
        9 if item.kind == ITEM_MERCHANT else 0,
        int(wire) & 0xFFFF,
        0xFFFF,
        int(sub) & 0xFFFF,
        0xFFFF,
        item.price & 0xFFFFFFFF,
        1,
        0,
        0,
        0,
        0,
        max(1, int(item.stack)) & 0xFFFFFFFF,
        0,
        0,
        0,
        0,
        0,
    )
    body = bytearray(255)
    # common/patches/rof2_structs.h:4779 ItemBodyStruct
    struct.pack_into("<I", body, 0, item.item_id & 0xFFFFFFFF)
    body[11] = item.size & 0xFF
    # common/patches/rof2_structs.h:4785 ItemBodyStruct
    struct.pack_into("<I", body, 12, item.slots & 0xFFFFFFFF)
    # common/patches/rof2_structs.h:4808 ItemBodyStruct
    struct.pack_into("<i", body, 56, i32(item.ac))
    # common/patches/rof2_structs.h:4812 ItemBodyStruct
    struct.pack_into("<I", body, 72, item.classes & 0xFFFFFFFF)
    # common/patches/rof2_structs.h:4813 ItemBodyStruct
    struct.pack_into("<I", body, 76, item.races & 0xFFFFFFFF)
    # common/patches/rof2_structs.h:4825 ItemBodyStruct
    struct.pack_into("<I", body, 121, item.required_level & 0xFFFFFFFF)
    # common/patches/rof2_structs.h:4835 ItemBodyStruct
    struct.pack_into("<I", body, 146, item.damage & 0xFFFFFFFF)
    body[158] = item.item_type & 0xFF
    secondary = bytearray(74)
    secondary[69] = item.bag_slots & 0xFF
    secondary[70] = item.bag_size & 0xFF
    effects = b""
    for index in range(6):
        effect = item.scroll_effect if index == 4 else 0
        # common/patches/rof2_structs.h:4934 ClickEffectStruct
        effect_bytes = struct.pack("<i", i32(effect))
        # common/patches/rof2.cpp:6759 effect_unknown
        unknown = struct.pack("<i", 0)
        effects += effect_bytes + b"\x00" * 26 + put_cstr("") + unknown
    return (
        header
        + put_cstr("")
        + put_cstr("")
        + b"\x00" * 26
        + put_cstr(item.name)
        + put_cstr("")
        + put_cstr(item.id_file)
        + put_cstr("")
        + bytes(body)
        + put_cstr("")
        + bytes(secondary)
        + put_cstr("")
        + b"\x00" * 76
        + effects
        + bytes(_QUATERNARY)
        + struct.pack("<I", 0)
    )


def _read_item(data: bytes, offset: int, kind: int) -> tuple[list[Item], int]:
    """One RoF2 serialized item and the items packed inside it."""
    begin = offset
    offset = advance(data, offset, 77, "item")
    base = offset - 77
    stack, _unknown, slot_type, main_slot, _sub, _aug, price = struct.unpack_from("<IIBhhhI", data, base + 17)
    evolving = data[base + 76]
    if evolving:
        offset = advance(data, offset, 25, "item")
    _ornament, offset = cstring(data, offset)
    _offhand, offset = cstring(data, offset)
    offset = advance(data, offset, 26, "item")
    name_start = offset
    name, offset = cstring(data, offset)
    name_end = offset
    _lore, offset = cstring(data, offset)
    id_file_start = offset
    id_file, offset = cstring(data, offset)
    id_file_end = offset
    _blank, offset = cstring(data, offset)
    offset = advance(data, offset, 255, "item")
    body = offset - 255
    item_id = read_u32(data, body)
    size = data[body + 11]
    slots = read_u32(data, body + 12)
    ac = struct.unpack_from("<i", data, body + 56)[0]
    classes = read_u32(data, body + 72)
    races = read_u32(data, body + 76)
    required = read_u32(data, body + 121)
    damage = read_u32(data, body + 146)
    item_type = data[body + 158]
    _charm, offset = cstring(data, offset)
    offset = advance(data, offset, 74, "item")
    secondary_start = offset
    bag_slots = data[offset - 74 + 69]
    bag_size = data[offset - 74 + 70]
    _filename, offset = cstring(data, offset)
    offset = advance(data, offset, 76, "item")
    scroll = 0
    scroll_start = -1
    for index in range(6):
        scroll_effect_start = offset
        offset = advance(data, offset, 30, "item")
        if index == 4:
            scroll_start = offset - 30
            scroll = struct.unpack_from("<i", data, scroll_start)[0]
        _effect_name, offset = cstring(data, offset)
        offset = advance(data, offset, 4, "item")
    offset = advance(data, offset, _QUATERNARY, "item")
    nested_count = read_u32(data, offset)
    offset += 4
    prefix_end = offset
    direct_children: list[Item] = []
    nested: list[Item] = []
    for _index in range(nested_count):
        entry_index = read_u32(data, offset)
        offset = advance(data, offset, 4, "item")
        descendants, offset = _read_item(data, offset, kind)
        descendants[0]._entry_index = entry_index
        direct_children.append(descendants[0])
        nested.extend(descendants)

    slot = client_slot(int(slot_type), int(main_slot), int(_sub))
    count = int(stack) if int(stack) > 0 else 1
    item = Item(
        kind,
        slot,
        name,
        id_file,
        int(item_id),
        count,
        int(slots),
        int(classes),
        int(races),
        int(ac),
        int(damage),
        int(required),
        int(size),
        int(bag_slots),
        int(bag_size),
        int(item_type),
        int(scroll),
        int(price),
    )
    item.children = direct_children
    item._wire_prefix = bytes(data[begin:prefix_end])
    item._wire_offsets = {
        "name": (name_start - begin, name_end - begin),
        "id_file": (id_file_start - begin, id_file_end - begin),
        "body": body - begin,
        "secondary": secondary_start - begin,
        "scroll": scroll_start - begin,
    }
    item._original_fields = {name: getattr(item, name) for name in (
        "slot", "name", "id_file", "item_id", "stack", "slots",
        "classes", "races", "ac", "damage", "required_level",
        "size", "bag_slots", "bag_size", "item_type", "scroll_effect", "price",
    )}
    return ([item, *nested], offset)


@dataclass
class Item(EQStruct):
    kind: int
    slot: int
    name: str
    id_file: str
    item_id: int
    stack: int = 1
    slots: int = 0
    classes: int = 0
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
    # Direct children; unlike the old flattened parser this preserves nesting.
    children: list[Item] = field(default_factory=list, repr=False, compare=False)
    _entry_index: int = field(default=0, repr=False, compare=False)
    _wire_prefix: bytes = field(default=b"", repr=False, compare=False)
    _wire_offsets: dict = field(default_factory=dict, repr=False, compare=False)
    _original_fields: dict = field(default_factory=dict, repr=False, compare=False)

    def _serialize_body(self) -> bytes:
        if not self._wire_prefix:
            # Synthetic items retain the previous minimal serializer.
            data = bytearray(_pack_item_body(self))
        else:
            data = bytearray(self._wire_prefix)
            original = self._original_fields
            offsets = self._wire_offsets
            body = offsets["body"]
            secondary = offsets["secondary"]

            def changed(name: str) -> bool:
                return getattr(self, name) != original[name]

            def patch(name: str, fmt: str, location: int) -> None:
                if changed(name):
                    struct.pack_into(fmt, data, location, getattr(self, name))

            patch("stack", "<I", 17)
            patch("price", "<I", 32)
            patch("item_id", "<I", body)
            patch("size", "<B", body + 11)
            patch("slots", "<I", body + 12)
            patch("ac", "<i", body + 56)
            patch("classes", "<I", body + 72)
            patch("races", "<I", body + 76)
            patch("required_level", "<I", body + 121)
            patch("damage", "<I", body + 146)
            patch("item_type", "<B", body + 158)
            patch("bag_slots", "<B", secondary + 69)
            patch("bag_size", "<B", secondary + 70)
            patch("scroll_effect", "<i", offsets["scroll"])

            if changed("slot"):
                slot_type = data[25]
                if slot_type == 0:
                    main, sub = inventory_wire(self.slot)
                else:
                    main, sub = self.slot, -1
                struct.pack_into("<hh", data, 26, i16(main), i16(sub))

            # Apply variable-size string updates in reverse offset order.
            # Everything else was patched using offsets from the original bytes.
            edits = []
            if changed("name"):
                edits.append((*offsets["name"], put_cstr(self.name)))
            if changed("id_file"):
                edits.append((*offsets["id_file"], put_cstr(self.id_file)))
            for start, end, value in sorted(edits, reverse=True):
                data[start:end] = value

        struct.pack_into("<I", data, len(data) - 4, len(self.children))
        for child in self.children:
            data += u32(child._entry_index)
            data += child._serialize_body()
        return bytes(data)

    def serialize(self) -> bytes:
        return u32(self.kind) + self._serialize_body()

    def walk(self):
        yield self
        for child in self.children:
            yield from child.walk()
 
    @classmethod
    def deserialize(cls, data: bytes) -> Item:
        need(data, 4, "item packet")
        found, offset = _read_item(data, 4, read_u32(data))
        if offset != len(data):
            raise ValueError(f"Item packet trailing data: {len(data) - offset} bytes")
        return found[0]


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
            rows, offset = _read_item(data, offset, ITEM_INVENTORY)
            found.extend(rows[0])
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
        return cls(source.client_slot, dest.client_slot, read_u32(data, 24),
                   source.type, dest.type, False, source, dest,)
 

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
        return cls(source.client_slot, dest.client_slot, read_u32(data, 24),
                   dest.type, source.type, source, dest,)


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
        exact(data, 12, "OP_LootItem")
        corpse_id, player_id, slot, unknown10, auto_loot, unknown16 = struct.unpack_from("<IIHHiI", data)
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
        
        return struct.pack("<BBBBIIII", self.response & 0xFF,
                           self.unknown01 & 0xFF, self.unknown02 & 0xFF,
                           self.unknown03 & 0xFF, self.platinum & 0xFFFFFFFF,
                           self.gold & 0xFFFFFFFF, self.silver & 0xFFFFFFFF,
                           self.copper & 0xFFFFFFFF,)

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
    unknown16: int = 0
    unknown20: int = 0

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:2136 MerchantClick_Struct
        return struct.pack(
            "<IIIfii",
            self.npc_id & 0xFFFFFFFF,
            self.player_id & 0xFFFFFFFF,
            self.command & 0xFFFFFFFF,
            self.rate,
            i32(self.unknown16),
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
        return cls(npc, player, slot, unknown, quantity, price, gap, tail)

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
        
        return u32(self.npc_id) + address.pack() + struct.pack(
            "<II", self.quantity & 0xFFFFFFFF, self.price & 0xFFFFFFFF,)
 
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
        exact(data, 16, "OP_ShopDelItem")
        return cls(*struct.unpack("<4I", data))


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
        
        return pack_inventory_slot(self.container_slot) + pack_inventory_slot(self.guildtribute_slot)
    
    def serialize(self) -> bytes:
        # common/patches/rof2_structs.h:3933 NewCombine_Struct
        if self.container_address:
            container = self.container_address.preserve_inventory_slot(self.container_type, self.container_slot)
        else:
            container = InventorySlot.for_client(self.container_type, self.container_slot)
        if self.guildtribute_address:
            tribute = self.guildtribute_address.preserve_inventory_slot(self.guildtribute_type, self.guildtribute_slot)
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

