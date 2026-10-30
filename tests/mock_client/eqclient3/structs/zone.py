from __future__ import annotations

import struct
from dataclasses import dataclass

from eqclient3.structs.wire import (
    EQStruct,
    _cstring,
    _fixed,
    _i32,
    _need,
    _put_cstr,
    _put_fixed,
    _read_u32,
)

ENTER_WORLD_SIZE = 72
ZONE_ENTRY_SIZE = 76
ZONE_SERVER_INFO_SIZE = 130
NEW_ZONE_SIZE = 948
ZONE_CHANGE_SIZE = 100
REQUEST_ZONE_CHANGE_SIZE = 176


@dataclass
class OP_EnterWorld(EQStruct):
    name: str
    tutorial: int = 0
    return_home: int = 0

    def serialize(self) -> bytes:
        packet = bytearray(ENTER_WORLD_SIZE)
        _put_fixed(packet, 0, self.name, 64)
        # common/eq_packet_structs.h:58 EnterWorld_Struct
        struct.pack_into("<II", packet, 64, self.tutorial & 0xFFFFFFFF, self.return_home & 0xFFFFFFFF)
        return bytes(packet)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_EnterWorld:
        _need(data, 64, "OP_EnterWorld")
        tutorial = return_home = 0
        if len(data) >= ENTER_WORLD_SIZE:
            tutorial, return_home = struct.unpack_from("<II", data, 64)
        return cls(_fixed(data, 0, 64), int(tutorial), int(return_home))


@dataclass
class OP_ZoneServerInfo(EQStruct):
    host: str
    port: int

    def serialize(self) -> bytes:
        packet = bytearray(ZONE_SERVER_INFO_SIZE)
        _put_fixed(packet, 0, self.host, 128)
        # common/eq_packet_structs.h:3660 ZoneServerInfo_Struct
        struct.pack_into("<H", packet, 128, self.port & 0xFFFF)
        return bytes(packet)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ZoneServerInfo:
        _need(data, ZONE_SERVER_INFO_SIZE, "OP_ZoneServerInfo")
        host = _fixed(data, 0, 128)
        port = struct.unpack_from("<H", data, 128)[0]
        return cls(host, int(port))


@dataclass
class OP_ZoneEntry(EQStruct):
    name: str
    unknown: int = 0

    def serialize(self) -> bytes:
        packet = bytearray(ZONE_ENTRY_SIZE)
        # common/patches/rof2_structs.h:546
        struct.pack_into("<I", packet, 0, self.unknown & 0xFFFFFFFF)
        _put_fixed(packet, 4, self.name, 64)
        return bytes(packet)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ZoneEntry:
        _need(data, ZONE_ENTRY_SIZE, "OP_ZoneEntry")
        unknown = _read_u32(data)
        return cls(_fixed(data, 4, 64), int(unknown))


@dataclass
class OP_NewZone(EQStruct):
    short_name: str
    x: float
    y: float
    z: float
    zone_id: int = 0
    instance_id: int = 0
    char_name: str = ""
    long_name: str = ""

    def serialize(self) -> bytes:
        packet = bytearray(NEW_ZONE_SIZE)
        _put_fixed(packet, 0, self.char_name, 64)
        _put_fixed(packet, 64, self.short_name, 128)
        _put_fixed(packet, 192, self.long_name, 128)
        # common/patches/rof2_structs.h:594
        struct.pack_into("<fff", packet, 588, self.y, self.x, self.z)
        # common/patches/rof2_structs.h:630
        struct.pack_into("<HH", packet, 852, self.zone_id & 0xFFFF, self.instance_id & 0xFFFF)
        return bytes(packet)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_NewZone:
        _need(data, 856, "OP_NewZone")
        safe_y, safe_x, safe_z = struct.unpack_from("<fff", data, 588)
        zone_id, instance_id = struct.unpack_from("<HH", data, 852)
        return cls(
            _fixed(data, 64, 128),
            float(safe_x),
            float(safe_y),
            float(safe_z),
            int(zone_id),
            int(instance_id),
            _fixed(data, 0, 64),
            _fixed(data, 192, 128),
        )


@dataclass
class OP_RequestClientZoneChange(EQStruct):
    zone_id: int
    x: float
    y: float
    z: float
    instance_id: int = 0
    heading: float = 0.0
    kind: int = 0

    def serialize(self) -> bytes:
        packet = bytearray(REQUEST_ZONE_CHANGE_SIZE)
        # common/patches/rof2_structs.h:1441
        struct.pack_into("<HH", packet, 0, self.zone_id & 0xFFFF, self.instance_id & 0xFFFF)
        # common/patches/rof2.cpp:3402
        struct.pack_into("<I", packet, 4, 0xFFFFFFFF)
        # common/patches/rof2_structs.h:1444
        struct.pack_into("<ffff", packet, 8, self.y, self.x, self.z, self.heading)
        # common/patches/rof2.cpp:3401 type
        struct.pack_into("<I", packet, 24, 0x0B)
        # common/patches/rof2.cpp:3403
        struct.pack_into("<I", packet, 172, 0x0168B500)
        return bytes(packet)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_RequestClientZoneChange:
        _need(data, 28, "OP_RequestClientZoneChange")
        zone_id, instance_id = struct.unpack_from("<HH", data)
        wire_y, wire_x, wire_z, heading = struct.unpack_from("<ffff", data, 8)
        kind = _read_u32(data, 24)
        return cls(
            int(zone_id), float(wire_x), float(wire_y), float(wire_z), int(instance_id), float(heading), int(kind)
        )


@dataclass
class OP_ZoneChange(EQStruct):
    name: str
    zone_id: int
    x: float
    y: float
    z: float
    instance_id: int = 0
    zone_reason: int = 0
    success: int = 0

    def serialize(self) -> bytes:
        packet = bytearray(ZONE_CHANGE_SIZE)
        _put_fixed(packet, 0, self.name, 64)
        # common/patches/rof2_structs.h:1427
        struct.pack_into("<HH", packet, 64, self.zone_id & 0xFFFF, self.instance_id & 0xFFFF)
        # common/patches/rof2_structs.h:1431
        struct.pack_into("<fff", packet, 76, self.y, self.x, self.z)
        # common/patches/rof2_structs.h:1434
        struct.pack_into("<Ii", packet, 88, self.zone_reason & 0xFFFFFFFF, _i32(self.success))
        return bytes(packet)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ZoneChange:
        _need(data, ZONE_CHANGE_SIZE, "OP_ZoneChange")
        zone_id, instance_id = struct.unpack_from("<HH", data, 64)
        wire_y, wire_x, wire_z = struct.unpack_from("<fff", data, 76)
        zone_reason, success = struct.unpack_from("<Ii", data, 88)
        return cls(
            _fixed(data, 0, 64),
            int(zone_id),
            float(wire_x),
            float(wire_y),
            float(wire_z),
            int(instance_id),
            int(zone_reason),
            int(success),
        )


@dataclass
class OP_ZonePlayerToBind(EQStruct):
    zone_id: int = 0
    instance_id: int = 0
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    heading: float = 0.0
    zone_name: str = ""

    def serialize(self) -> bytes:
        # common/patches/rof2.cpp:4550 bind_zone_id
        head = struct.pack(
            "<HHffff",
            self.zone_id & 0xFFFF,
            self.instance_id & 0xFFFF,
            self.x,
            self.y,
            self.z,
            self.heading,
        )
        # common/patches/rof2.cpp:4557 save items
        tail = struct.pack("<BIII", 1, 0, 0, 0)
        return head + _put_cstr(self.zone_name) + tail

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ZonePlayerToBind:
        if len(data) < 20:
            return cls()
        zone_id, instance_id = struct.unpack_from("<HH", data)
        x, y, z, heading = struct.unpack_from("<ffff", data, 4)
        name = ""
        if len(data) > 20:
            try:
                name, _end = _cstring(data, 20)
            except ValueError:
                name = _fixed(data, 20, max(0, len(data) - 20))
        return cls(int(zone_id), int(instance_id), float(x), float(y), float(z), float(heading), name)


@dataclass
class OP_FloatListThing(EQStruct):
    x: float
    y: float
    z: float
    timestamp: int
    sample_type: int = 0

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:6362 UpdateMovementEntry
        return struct.pack("<fffBI", self.y, self.x, self.z, self.sample_type & 0xFF, self.timestamp & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_FloatListThing:
        _need(data, 17, "OP_FloatListThing")
        wire_y, wire_x, wire_z, sample_type, timestamp = struct.unpack_from("<fffBI", data)
        return cls(float(wire_x), float(wire_y), float(wire_z), int(timestamp), int(sample_type))


@dataclass
class OP_ClientReady(EQStruct):
    """Zone-in finished. The body is empty."""


@dataclass
class OP_ReqNewZone(EQStruct):
    """Asks for OP_NewZone. The body is empty."""


@dataclass
class OP_SendExpZonein(EQStruct):
    """Sent after OP_NewZone. The body is empty."""


@dataclass
class OP_ReqClientSpawn(EQStruct):
    """Asks for the spawn burst. The body is empty."""


@dataclass
class OP_SendAAStats(EQStruct):
    """Marker that the spawn burst has finished. The body is ignored."""


@dataclass
class OP_ZoneServerReady(EQStruct):
    """RoF2 leaves this opcode at zero. The body is empty."""


@dataclass
class OP_ZoneComplete(EQStruct):
    """Sent when the opcode table has it. The body is empty."""


@dataclass
class OP_ReliableHole(EQStruct):
    """Synthetic opcode for a reliable-stream hole. There is no wire body."""
