from __future__ import annotations

import struct
from dataclasses import dataclass, field

from eqclient3.structs.wire import (
    EQStruct,
    _cstring,
    _fixed,
    _need,
    _put_fixed,
    _read_u32,
    _two_names,
)


@dataclass
class OP_GroupInvite(EQStruct):
    invitee: str
    inviter: str = ""

    def serialize(self) -> bytes:
        packet = bytearray(148)
        _put_fixed(packet, 0, self.invitee, 64)
        _put_fixed(packet, 64, self.inviter, 64)
        # common/patches/rof2_structs.h:2569 GroupInvite_Struct
        struct.pack_into("<IIIII", packet, 128, 0, 0, 0, 0, 0)
        return bytes(packet)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_GroupInvite:
        invitee, inviter = _two_names(data)
        return cls(invitee, inviter)


@dataclass
class OP_GroupInvite2(EQStruct):
    invitee: str
    inviter: str = ""

    def serialize(self) -> bytes:
        packet = bytearray(148)
        _put_fixed(packet, 0, self.invitee, 64)
        _put_fixed(packet, 64, self.inviter, 64)
        # common/patches/rof2_structs.h:2569 GroupInvite_Struct
        struct.pack_into("<IIIII", packet, 128, 0, 0, 0, 0, 0)
        return bytes(packet)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_GroupInvite2:
        invitee, inviter = _two_names(data)
        return cls(invitee, inviter)


@dataclass
class OP_GroupUpdate(EQStruct):
    action: int = 0
    your_name: str = ""
    members: list[str] = field(default_factory=list)
    leader: str = ""
    full: bool = False

    def serialize(self) -> bytes:
        return _pack_group(self.action, self.your_name, self.members, self.leader, self.full)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_GroupUpdate:
        action, your_name, members, leader, full = _read_group(data, full_opcode=True)
        return cls(action, your_name, members, leader, full)


@dataclass
class OP_GroupUpdateB(OP_GroupUpdate):
    """Full roster. The server sends this instead of the fixed group update."""

    @classmethod
    def deserialize(cls, data: bytes) -> OP_GroupUpdateB:
        your_name, members, leader = _read_group_roster(data)
        return cls(7, your_name, members, leader, True)


@dataclass
class OP_GroupDisbandYou(EQStruct):
    your_name: str = ""
    member_name: str = ""

    @classmethod
    def deserialize(cls, data: bytes) -> OP_GroupDisbandYou:
        your_name, member_name = _two_names(data)
        return cls(your_name, member_name)


@dataclass
class OP_GroupDisbandOther(EQStruct):
    your_name: str = ""
    member_name: str = ""

    @classmethod
    def deserialize(cls, data: bytes) -> OP_GroupDisbandOther:
        your_name, member_name = _two_names(data)
        return cls(your_name, member_name)


def _read_group_roster(data: bytes) -> tuple[str, list[str], str]:
    if len(data) < 8:
        return "", [], ""
    count = _read_u32(data, 4)
    try:
        leader, offset = _cstring(data, 8)
    except ValueError:
        return "", [], ""
    names: list[str] = []
    for _index in range(count):
        if offset + 4 > len(data):
            break
        offset += 4
        try:
            name, offset = _cstring(data, offset)
        except ValueError:
            break
        offset += 18
        if name:
            names.append(name)
    your_name = names[0] if names else ""
    return your_name, names[1:], leader


@dataclass
class OP_RaidUpdate(EQStruct):
    action: int = 0
    your_name: str = ""
    leader: str = ""

    def serialize(self) -> bytes:
        your_name = (self.your_name or "").encode("latin1", errors="replace")[:63]
        leader = (self.leader or "").encode("latin1", errors="replace")[:63]
        # common/patches/rof2_structs.h:4370 RaidGeneral_Struct
        return struct.pack("<I64sI64sI", self.action & 0xFFFFFFFF, your_name, 0, leader, 0)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_RaidUpdate:
        # Add, note, motd, and leadership updates are this header plus a tail.
        _need(data, 140, "OP_RaidUpdate")
        return cls(int(_read_u32(data)), _fixed(data, 4, 64), _fixed(data, 72, 64))


@dataclass
class OP_RaidJoin(EQStruct):
    action: int = 0
    your_name: str = ""
    leader: str = ""

    def serialize(self) -> bytes:
        your_name = (self.your_name or "").encode("latin1", errors="replace")[:63]
        leader = (self.leader or "").encode("latin1", errors="replace")[:63]
        # common/patches/rof2_structs.h:4370 RaidGeneral_Struct
        return struct.pack("<I64sI64sI", self.action & 0xFFFFFFFF, your_name, 0, leader, 0)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_RaidJoin:
        _need(data, 140, "OP_RaidJoin")
        return cls(int(_read_u32(data)), _fixed(data, 4, 64), _fixed(data, 72, 64))


def _pack_group(action: int, your_name: str, members: list[str], leader: str, full: bool) -> bytes:
    if full:
        packet = bytearray(452)
        # common/eq_packet_structs.h:2497 GroupUpdate_Struct
        struct.pack_into("<I", packet, 0, action & 0xFFFFFFFF)
        _put_fixed(packet, 4, your_name, 64)
        for index in range(5):
            name = members[index] if index < len(members) else ""
            _put_fixed(packet, 68 + index * 64, name, 64)
        _put_fixed(packet, 388, leader, 64)
        return bytes(packet)
    packet = bytearray(132)
    # common/eq_packet_structs.h:2515 GroupJoin_Struct
    struct.pack_into("<I", packet, 0, action & 0xFFFFFFFF)
    _put_fixed(packet, 4, your_name, 64)
    _put_fixed(packet, 68, leader, 64)
    return bytes(packet)


def _read_group(data: bytes, full_opcode: bool) -> tuple[int, str, list[str], str, bool]:
    if len(data) < 4:
        return 0, "", [], "", False
    if full_opcode and len(data) == 148:
        return 0, _fixed(data, 64, 64), [], "", False
    action = _read_u32(data)
    if full_opcode and len(data) >= 452:
        your_name = _fixed(data, 4, 64)
        members = [_fixed(data, 68 + index * 64, 64) for index in range(5)]
        leader = _fixed(data, 388, 64)
        return int(action), your_name, members, leader, True
    if len(data) >= 132:
        return int(action), _fixed(data, 4, 64), [], _fixed(data, 68, 64), False
    return int(action), "", [], "", False
