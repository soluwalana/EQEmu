from __future__ import annotations

import struct
from dataclasses import dataclass

from eqclient3.structs.wire import (
    EQStruct,
    _i16,
    _need,
    _pack_inventory_slot,
    _read_u32,
    _unpack_inventory_slot,
)

_FACTION_SWAP = {6: 9, 7: 8, 8: 7, 9: 6}


@dataclass
class OP_Consider(EQStruct):
    player_id: int
    target_id: int
    faction: int = 0
    level: int = 0
    cur_hp: int = 0
    max_hp: int = 0
    pvp: int = 0

    def serialize(self) -> bytes:
        # common/patches/rof2_structs.h:1531
        return struct.pack(
            "<IIIIBBBB",
            self.player_id & 0xFFFFFFFF,
            self.target_id & 0xFFFFFFFF,
            _FACTION_SWAP.get(self.faction, self.faction) & 0xFFFFFFFF,
            self.level & 0xFFFFFFFF,
            self.pvp & 0xFF,
            0,
            0,
            0,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_Consider:
        _need(data, 20, "OP_Consider")
        player_id, target_id, faction, level = struct.unpack_from("<IIII", data)
        return cls(
            int(player_id),
            int(target_id),
            _FACTION_SWAP.get(int(faction), int(faction)),
            int(level),
            0,
            0,
            int(data[16]),
        )


@dataclass
class OP_TargetMouse(EQStruct):
    spawn_id: int

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:1148 ClientTarget_Struct
        return struct.pack("<I", self.spawn_id & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_TargetMouse:
        _need(data, 4, "OP_TargetMouse")
        return cls(_read_u32(data))


@dataclass
class OP_AutoAttack(EQStruct):
    attacking: int

    def serialize(self) -> bytes:
        # zone/client_packet.cpp:3524 OP_AutoAttack
        return struct.pack("<I", self.attacking & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_AutoAttack:
        _need(data, 4, "OP_AutoAttack")
        return cls(_read_u32(data))


@dataclass
class OP_Taunt(EQStruct):
    spawn_id: int

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:1148 ClientTarget_Struct
        return struct.pack("<I", self.spawn_id & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_Taunt:
        _need(data, 4, "OP_Taunt")
        return cls(_read_u32(data))


@dataclass
class OP_CombatAbility(EQStruct):
    target_id: int
    attack: int = 0
    skill: int = 0

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:1993 CombatAbility_Struct
        return struct.pack("<III", self.target_id & 0xFFFFFFFF, self.attack & 0xFFFFFFFF, self.skill & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_CombatAbility:
        _need(data, 12, "OP_CombatAbility")
        target_id, attack, skill = struct.unpack_from("<III", data)
        return cls(int(target_id), int(attack), int(skill))


@dataclass
class OP_CastSpell(EQStruct):
    slot: int
    spell_id: int
    target_id: int
    inventory_slot: int = 0xFFFF

    def serialize(self) -> bytes:
        if _i16(self.inventory_slot) == -1:
            # common/patches/rof2_structs.h:57 InventorySlot_Struct
            held = struct.pack("<hhhhhh", _i16(0xFFFF), 0, _i16(0xFFFF), _i16(0xFFFF), _i16(0xFFFF), 0)
        else:
            held = _pack_inventory_slot(self.inventory_slot)
        # common/patches/rof2_structs.h:730 CastSpell_Struct
        head = struct.pack("<II", self.slot & 0xFFFFFFFF, self.spell_id & 0xFFFFFFFF)
        # common/patches/rof2_structs.h:733 CastSpell_Struct
        tail = struct.pack(
            "<III3f",
            self.target_id & 0xFFFFFFFF,
            0,
            0,
            0.0,
            0.0,
            0.0,
        )
        return head + held + tail

    @classmethod
    def deserialize(cls, data: bytes) -> OP_CastSpell:
        _need(data, 24, "OP_CastSpell")
        slot, spell_id = struct.unpack_from("<II", data)
        inventory_slot = _unpack_inventory_slot(data, 8)
        target_id = _read_u32(data, 20)
        return cls(int(slot), int(spell_id), int(target_id), int(inventory_slot))


@dataclass
class OP_MemorizeSpell(EQStruct):
    slot: int
    spell_id: int
    scribing: int
    reduction: int = 0

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:415 MemorizeSpell_Struct
        return struct.pack(
            "<IIII",
            self.slot & 0xFFFFFFFF,
            self.spell_id & 0xFFFFFFFF,
            self.scribing & 0xFFFFFFFF,
            self.reduction & 0xFFFFFFFF,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_MemorizeSpell:
        _need(data, 12, "OP_MemorizeSpell")
        slot, spell_id, scribing = struct.unpack_from("<III", data)
        reduction = _read_u32(data, 12) if len(data) >= 16 else 0
        return cls(int(slot), int(spell_id), int(scribing), int(reduction))


@dataclass
class OP_Consume(EQStruct):
    slot: int
    kind: int
    auto: int = 0xFFFFFFFF

    def serialize(self) -> bytes:
        # common/patches/rof2_structs.h:1783 Consume_Struct
        tail = struct.pack("<III", self.auto & 0xFFFFFFFF, self.kind & 0xFFFFFFFF, 0)
        return _pack_inventory_slot(self.slot) + tail

    @classmethod
    def deserialize(cls, data: bytes) -> OP_Consume:
        _need(data, 20, "OP_Consume")
        slot = _unpack_inventory_slot(data, 0)
        auto, kind = struct.unpack_from("<II", data, 12)
        return cls(int(slot), int(kind), int(auto))


@dataclass
class OP_Bind_Wound(EQStruct):
    target_id: int
    unknown2: int = 0
    type: int = 0
    unknown6: int = 0

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:1258 BindWound_Struct
        return struct.pack(
            "<HHHH", self.target_id & 0xFFFF, self.unknown2 & 0xFFFF, self.type & 0xFFFF, self.unknown6 & 0xFFFF
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_Bind_Wound:
        _need(data, 8, "OP_Bind_Wound")
        target_id, unknown2, kind, unknown6 = struct.unpack_from("<HHHH", data)
        return cls(int(target_id), int(unknown2), int(kind), int(unknown6))


@dataclass
class OP_Forage(EQStruct):
    """Forage. The body is empty."""


@dataclass
class OP_Fishing(EQStruct):
    """Fishing. The body is empty."""
