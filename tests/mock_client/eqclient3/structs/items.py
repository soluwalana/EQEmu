from __future__ import annotations

import struct
from dataclasses import dataclass, field

from eqclient3.structs.wire import (
    EQStruct,
    _advance,
    _client_slot,
    _cstring,
    _from_rof2_slot,
    _i16,
    _i32,
    _need,
    _pack_inventory_slot,
    _pack_typed_slot,
    _pack_names,
    _put_cstr,
    _read_u32,
    _to_rof2_slot,
    _two_names,
    _u32,
    _unpack_inventory_slot,
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
    wire = _to_rof2_slot(item.slot) if item.kind != ITEM_MERCHANT else item.slot
    # common/patches/rof2_structs.h:4733 ItemSerializationHeader
    header = struct.pack(
        "<17sIIBHHHIIIIIIIIIIIB",
        b"\x00" * 17,
        max(1, int(item.stack)) & 0xFFFFFFFF,
        0,
        9 if item.kind == ITEM_MERCHANT else 0,
        int(wire) & 0xFFFF,
        0xFFFF,
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
    struct.pack_into("<i", body, 56, _i32(item.ac))
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
        effect_bytes = struct.pack("<i", _i32(effect))
        # common/patches/rof2.cpp:6759 effect_unknown
        unknown = struct.pack("<i", 0)
        effects += effect_bytes + b"\x00" * 26 + _put_cstr("") + unknown
    return (
        header
        + _put_cstr("")
        + _put_cstr("")
        + b"\x00" * 26
        + _put_cstr(item.name)
        + _put_cstr("")
        + _put_cstr(item.id_file)
        + _put_cstr("")
        + bytes(body)
        + _put_cstr("")
        + bytes(secondary)
        + _put_cstr("")
        + b"\x00" * 76
        + effects
        + bytes(_QUATERNARY)
        + struct.pack("<I", 0)
    )


def _read_item(data: bytes, offset: int, kind: int) -> tuple[list[Item], int]:
    """One RoF2 serialized item and the items packed inside it."""
    offset = _advance(data, offset, 77, "item")
    base = offset - 77
    stack, _unknown, slot_type, main_slot, _sub, _aug, price = struct.unpack_from("<IIBhhhI", data, base + 17)
    evolving = data[base + 76]
    if evolving:
        offset = _advance(data, offset, 25, "item")
    _ornament, offset = _cstring(data, offset)
    _offhand, offset = _cstring(data, offset)
    offset = _advance(data, offset, 26, "item")
    name, offset = _cstring(data, offset)
    _lore, offset = _cstring(data, offset)
    id_file, offset = _cstring(data, offset)
    _blank, offset = _cstring(data, offset)
    offset = _advance(data, offset, 255, "item")
    body = offset - 255
    item_id = _read_u32(data, body)
    size = data[body + 11]
    slots = _read_u32(data, body + 12)
    ac = struct.unpack_from("<i", data, body + 56)[0]
    classes = _read_u32(data, body + 72)
    races = _read_u32(data, body + 76)
    required = _read_u32(data, body + 121)
    damage = _read_u32(data, body + 146)
    item_type = data[body + 158]
    _charm, offset = _cstring(data, offset)
    offset = _advance(data, offset, 74, "item")
    bag_slots = data[offset - 74 + 69]
    bag_size = data[offset - 74 + 70]
    _filename, offset = _cstring(data, offset)
    offset = _advance(data, offset, 76, "item")
    scroll = 0
    for index in range(6):
        offset = _advance(data, offset, 30, "item")
        if index == 4:
            scroll = struct.unpack_from("<i", data, offset - 30)[0]
        _effect_name, offset = _cstring(data, offset)
        offset = _advance(data, offset, 4, "item")
    offset = _advance(data, offset, _QUATERNARY, "item")
    nested_count = _read_u32(data, offset)
    offset += 4
    nested: list[Item] = []
    for _index in range(nested_count):
        offset = _advance(data, offset, 4, "item")
        children, offset = _read_item(data, offset, kind)
        nested.extend(children)
    slot = _client_slot(int(slot_type), int(main_slot), int(_sub))
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

    def serialize(self) -> bytes:
        # common/patches/rof2_structs.h:1767 ItemPacket_Struct
        return _u32(self.kind) + _pack_item_body(self)

    @classmethod
    def deserialize(cls, data: bytes) -> Item:
        _need(data, 4, "item packet")
        found, _offset = _read_item(data, 4, _read_u32(data))
        return found[0]


@dataclass
class OP_CharInventory(EQStruct):
    items: list[Item] = field(default_factory=list)

    def serialize(self) -> bytes:
        # common/patches/rof2.cpp:1075 OP_CharInventory
        out = bytearray(struct.pack("<I", len(self.items)))
        for item in self.items:
            out += _pack_item_body(item)
        return bytes(out)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_CharInventory:
        if len(data) < 4:
            return cls([])
        count = _read_u32(data)
        offset = 4
        found: list[Item] = []
        for _index in range(count):
            rows, offset = _read_item(data, offset, ITEM_INVENTORY)
            found.extend(rows)
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

    def serialize(self) -> bytes:
        # common/patches/rof2_structs.h:1818 DeleteItem_Struct
        count = struct.pack("<I", (self.count or 0) & 0xFFFFFFFF)
        return _pack_inventory_slot(self.from_slot) + _pack_inventory_slot(self.to_slot or 0) + count

    @classmethod
    def deserialize(cls, data: bytes) -> OP_DeleteItem:
        if len(data) >= 28:
            return cls(_unpack_inventory_slot(data, 0), _unpack_inventory_slot(data, 12), _read_u32(data, 24))
        _need(data, 4, "OP_DeleteItem")
        return cls(_read_u32(data))


@dataclass
class OP_MoveItem(EQStruct):
    from_slot: int
    to_slot: int
    count: int = 0
    to_type: int = 0

    def serialize(self) -> bytes:
        # common/patches/rof2_structs.h:1826 MoveItem_Struct
        count = struct.pack("<I", self.count & 0xFFFFFFFF)
        dest = _pack_typed_slot(self.to_type, self.to_slot) if self.to_type else _pack_inventory_slot(self.to_slot)
        return _pack_inventory_slot(self.from_slot) + dest + count

    @classmethod
    def deserialize(cls, data: bytes) -> OP_MoveItem:
        _need(data, 28, "OP_MoveItem")
        return cls(_unpack_inventory_slot(data, 0), _unpack_inventory_slot(data, 12), _read_u32(data, 24))


@dataclass
class OP_LootRequest(EQStruct):
    spawn_id: int

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:84 EntityId_Struct
        return struct.pack("<I", self.spawn_id & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_LootRequest:
        _need(data, 4, "OP_LootRequest")
        return cls(_read_u32(data))


@dataclass
class OP_EndLootRequest(EQStruct):
    spawn_id: int

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:84 EntityId_Struct
        return struct.pack("<I", self.spawn_id & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_EndLootRequest:
        _need(data, 4, "OP_EndLootRequest")
        return cls(_read_u32(data))


@dataclass
class OP_LootItem(EQStruct):
    corpse_id: int
    player_id: int
    slot: int
    auto_loot: int = 0

    def serialize(self) -> bytes:
        # common/patches/rof2_structs.h:2058 LootingItem_Struct
        return struct.pack(
            "<IIHHiI",
            self.corpse_id & 0xFFFFFFFF,
            self.player_id & 0xFFFFFFFF,
            self.slot & 0xFFFF,
            0,
            _i32(self.auto_loot),
            0,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_LootItem:
        _need(data, 12, "OP_LootItem")
        corpse_id, player_id = struct.unpack_from("<II", data)
        slot = struct.unpack_from("<H", data, 8)[0]
        auto_loot = struct.unpack_from("<i", data, 12)[0] if len(data) >= 16 else 0
        return cls(int(corpse_id), int(player_id), int(slot), int(auto_loot))


@dataclass
class OP_MoneyOnCorpse(EQStruct):
    response: int = 0
    platinum: int = 0
    gold: int = 0
    silver: int = 0
    copper: int = 0

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:1829 moneyOnCorpseStruct. zone/corpse.cpp:1280 writes 0x42, 0xef.
        return struct.pack(
            "<BBBBIIII",
            self.response & 0xFF,
            0x42,
            0xEF,
            0,
            self.platinum & 0xFFFFFFFF,
            self.gold & 0xFFFFFFFF,
            self.silver & 0xFFFFFFFF,
            self.copper & 0xFFFFFFFF,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_MoneyOnCorpse:
        if not data:
            return cls()
        response = data[0]
        if len(data) < 20:
            return cls(int(response))
        platinum, gold, silver, copper = struct.unpack_from("<IIII", data, 4)
        return cls(int(response), int(platinum), int(gold), int(silver), int(copper))


@dataclass
class OP_CorpseDrag(EQStruct):
    corpse: str
    dragger: str

    def serialize(self) -> bytes:
        return _pack_names(self.corpse, self.dragger, 152)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_CorpseDrag:
        corpse, dragger = _two_names(data)
        return cls(corpse, dragger)


@dataclass
class OP_ShopRequest(EQStruct):
    npc_id: int
    player_id: int
    command: int
    rate: float = 0.0

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:2136 MerchantClick_Struct
        return struct.pack(
            "<IIIfii",
            self.npc_id & 0xFFFFFFFF,
            self.player_id & 0xFFFFFFFF,
            self.command & 0xFFFFFFFF,
            self.rate,
            0,
            0,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ShopRequest:
        _need(data, 12, "OP_ShopRequest")
        npc_id, player_id, command = struct.unpack_from("<III", data)
        rate = struct.unpack_from("<f", data, 12)[0] if len(data) >= 16 else 0.0
        return cls(int(npc_id), int(player_id), int(command), float(rate))


@dataclass
class OP_ShopPlayerBuy(EQStruct):
    npc_id: int
    player_id: int
    slot: int
    unknown: int = 0
    quantity: int = 1
    price: int = 0

    def serialize(self) -> bytes:
        # common/patches/rof2_structs.h:2284 Merchant_Sell_Struct
        return struct.pack(
            "<IIIIIIII",
            self.npc_id & 0xFFFFFFFF,
            self.player_id & 0xFFFFFFFF,
            self.slot & 0xFFFFFFFF,
            self.unknown & 0xFFFFFFFF,
            self.quantity & 0xFFFFFFFF,
            0,
            self.price & 0xFFFFFFFF,
            0,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ShopPlayerBuy:
        _need(data, 32, "OP_ShopPlayerBuy")
        npc_id, player_id, slot, unknown, quantity, _gap, price, _tail = struct.unpack_from("<IIIIIIII", data)
        return cls(int(npc_id), int(player_id), int(slot), int(unknown), int(quantity), int(price))


@dataclass
class OP_ShopPlayerSell(EQStruct):
    npc_id: int
    slot: int
    quantity: int
    price: int = 0

    def serialize(self) -> bytes:
        # common/patches/rof2_structs.h:2297 Merchant_Purchase_Struct
        npc = struct.pack("<I", self.npc_id & 0xFFFFFFFF)
        # common/patches/rof2_structs.h:71 TypelessInventorySlot_Struct
        slot = struct.pack("<hhhh", _i16(_to_rof2_slot(self.slot)), _i16(0xFFFF), _i16(0xFFFF), 0)
        # common/patches/rof2_structs.h:2299 Merchant_Purchase_Struct
        rest = struct.pack(
            "<II",
            self.quantity & 0xFFFFFFFF,
            self.price & 0xFFFFFFFF,
        )
        return npc + slot + rest

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ShopPlayerSell:
        _need(data, 20, "OP_ShopPlayerSell")
        npc_id = _read_u32(data)
        slot = _from_rof2_slot(struct.unpack_from("<h", data, 4)[0])
        quantity, price = struct.unpack_from("<II", data, 12)
        return cls(int(npc_id), int(slot), int(quantity), int(price))


@dataclass
class OP_ShopDelItem(EQStruct):
    npc_id: int
    player_id: int
    slot: int

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:2242 Merchant_DelItem_Struct
        return struct.pack("<IIII", self.npc_id & 0xFFFFFFFF, self.player_id & 0xFFFFFFFF, self.slot & 0xFFFFFFFF, 0)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ShopDelItem:
        _need(data, 12, "OP_ShopDelItem")
        npc_id, player_id, slot = struct.unpack_from("<III", data)
        return cls(int(npc_id), int(player_id), int(slot))


@dataclass
class OP_TradeRequest(EQStruct):
    to_id: int
    from_id: int

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:2582 TradeRequest_Struct
        return struct.pack("<II", self.to_id & 0xFFFFFFFF, self.from_id & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_TradeRequest:
        _need(data, 8, "OP_TradeRequest")
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
        _need(data, 8, "OP_TradeRequestAck")
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
        _need(data, 8, "OP_CancelTrade")
        from_id, action = struct.unpack_from("<II", data)
        return cls(int(from_id), int(action))


@dataclass
class OP_TradeSkillCombine(EQStruct):
    container_slot: int
    guildtribute_slot: int = 0

    def serialize(self) -> bytes:
        # common/patches/rof2_structs.h:3933 NewCombine_Struct
        return _pack_inventory_slot(self.container_slot) + _pack_inventory_slot(self.guildtribute_slot)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_TradeSkillCombine:
        _need(data, 24, "OP_TradeSkillCombine")
        return cls(_unpack_inventory_slot(data, 0), _unpack_inventory_slot(data, 12))


@dataclass
class OP_TradeAcceptClick(EQStruct):
    from_mob_id: int = 0
    unknown4: int = 0

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:2588 TradeAccept_Struct
        return struct.pack("<II", self.from_mob_id & 0xFFFFFFFF, self.unknown4 & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_TradeAcceptClick:
        _need(data, 8, "OP_TradeAcceptClick")
        from_mob_id, unknown4 = struct.unpack_from("<II", data)
        return cls(int(from_mob_id), int(unknown4))


@dataclass
class OP_FinishTrade(EQStruct):
    """The server closed the trade. The body is ignored."""
