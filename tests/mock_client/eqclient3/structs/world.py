from __future__ import annotations

import struct
from dataclasses import dataclass, field

from eqclient3.structs.wire import (
    EQStruct,
    _advance,
    _cstring,
    _fixed,
    _need,
    _put_cstr,
    _put_fixed,
    _read_u32,
    _u32,
)

DOOR_SIZE = 100


@dataclass
class Door(EQStruct):
    door_id: int
    name: str
    x: float
    y: float
    z: float
    open_type: int

    def serialize(self) -> bytes:
        blob = bytearray(DOOR_SIZE)
        _put_fixed(blob, 0, self.name, 32)
        # common/patches/rof2_structs.h:3002
        struct.pack_into("<fff", blob, 32, self.y, self.x, self.z)
        blob[60] = self.door_id & 0xFF
        blob[61] = self.open_type & 0xFF
        # common/patches/rof2.cpp:3785 unknown0081
        struct.pack_into("<B", blob, 81, 1)
        # common/patches/rof2.cpp:3787 unknown0083
        struct.pack_into("<B", blob, 83, 1)
        return bytes(blob)

    @classmethod
    def deserialize(cls, data: bytes) -> Door:
        _need(data, DOOR_SIZE, "door")
        y, x, z = struct.unpack_from("<fff", data, 32)
        return cls(data[60], _fixed(data, 0, 32), x, y, z, data[61])


def _door_list(data: bytes) -> list[Door]:
    if len(data) < DOOR_SIZE:
        return []
    usable = data[: len(data) - len(data) % DOOR_SIZE]
    return [Door.deserialize(usable[offset : offset + DOOR_SIZE]) for offset in range(0, len(usable), DOOR_SIZE)]


def _pack_doors(doors: list[Door]) -> bytes:
    return b"".join(door.serialize() for door in doors)


@dataclass
class OP_SpawnDoor(EQStruct):
    doors: list[Door] = field(default_factory=list)

    def serialize(self) -> bytes:
        return _pack_doors(self.doors)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_SpawnDoor:
        return cls(_door_list(data))


@dataclass
class OP_DoorSpawn(EQStruct):
    doors: list[Door] = field(default_factory=list)

    def serialize(self) -> bytes:
        return _pack_doors(self.doors)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_DoorSpawn:
        return cls(_door_list(data))


@dataclass
class OP_Doors(EQStruct):
    doors: list[Door] = field(default_factory=list)

    def serialize(self) -> bytes:
        return _pack_doors(self.doors)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_Doors:
        return cls(_door_list(data))


@dataclass
class OP_MoveDoor(EQStruct):
    door_id: int
    action: int = 0

    def serialize(self) -> bytes:
        return bytes((self.door_id & 0xFF, self.action & 0xFF))

    @classmethod
    def deserialize(cls, data: bytes) -> OP_MoveDoor:
        if not data:
            raise ValueError("OP_MoveDoor is empty")
        action = data[1] if len(data) > 1 else 0
        return cls(int(data[0]), int(action))


@dataclass
class OP_ClickDoor(EQStruct):
    door_id: int
    unknown1: int = 0
    unknown2: int = 0
    unknown3: int = 0
    pick_lock_skill: int = 0
    item_id: int = 0
    player_id: int = 0

    def serialize(self) -> bytes:
        packet = bytearray(16)
        packet[0] = self.door_id & 0xFF
        packet[1] = self.unknown1 & 0xFF
        packet[2] = self.unknown2 & 0xFF
        packet[3] = self.unknown3 & 0xFF
        packet[4] = self.pick_lock_skill & 0xFF
        # common/eq_packet_structs.h:2943
        struct.pack_into("<IH", packet, 8, self.item_id & 0xFFFFFFFF, self.player_id & 0xFFFF)
        return bytes(packet)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ClickDoor:
        if not data:
            raise ValueError("OP_ClickDoor is empty")
        unknown1 = data[1] if len(data) > 1 else 0
        unknown2 = data[2] if len(data) > 2 else 0
        unknown3 = data[3] if len(data) > 3 else 0
        pick = data[4] if len(data) > 4 else 0
        item_id = _read_u32(data, 8) if len(data) >= 12 else 0
        player_id = struct.unpack_from("<H", data, 12)[0] if len(data) >= 14 else 0
        return cls(int(data[0]), int(unknown1), int(unknown2), int(unknown3), int(pick), int(item_id), int(player_id))


@dataclass
class OP_GroundSpawn(EQStruct):
    drop_id: int
    name: str
    x: float
    y: float
    z: float
    heading: float = 0.0

    def serialize(self) -> bytes:
        prefix = _u32(self.drop_id) + _put_cstr(self.name)
        # common/patches/rof2.cpp:1507
        return prefix + struct.pack(
            "<HHII4f3fi",
            0,
            0,
            self.drop_id & 0xFFFFFFFF,
            0,
            self.heading,
            0.0,
            0.0,
            1.0,
            self.y,
            self.x,
            self.z,
            0,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_GroundSpawn:
        _need(data, 5, "OP_GroundSpawn")
        drop_id = _read_u32(data)
        name, offset = _cstring(data, 4)
        offset = _advance(data, offset, 12 + 28, "OP_GroundSpawn")
        heading, _tilt_x, _tilt_y, _size, wire_y, wire_x, wire_z = struct.unpack_from("<7f", data, offset - 28)
        return cls(int(drop_id), name, float(wire_x), float(wire_y), float(wire_z), float(heading))


@dataclass
class OP_ClickObject(EQStruct):
    drop_id: int
    player_id: int | None = None

    def serialize(self) -> bytes:
        player_id = 0 if self.player_id is None else self.player_id
        # common/eq_packet_structs.h:2853 ClickObject_Struct
        return struct.pack("<II", self.drop_id & 0xFFFFFFFF, int(player_id) & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ClickObject:
        _need(data, 4, "OP_ClickObject")
        drop_id = _read_u32(data)
        if len(data) >= 8:
            return cls(drop_id, _read_u32(data, 4))
        return cls(drop_id, None)
