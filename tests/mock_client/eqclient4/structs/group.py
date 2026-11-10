import struct
from dataclasses import dataclass, field

from eqclient4.structs.wire import (
    EQStruct,
    cstring,
    fixed,
    need,
    put_fixed,
    read_u32,
    two_names,
)


@dataclass
class OP_GroupInvite(EQStruct):
    invitee: str
    inviter: str = ""

    def serialize(self) -> bytes:
        packet = bytearray(148)
        put_fixed(packet, 0, self.invitee, 64)
        put_fixed(packet, 64, self.inviter, 64)
        # common/patches/rof2_structs.h:2569 GroupInvite_Struct
        struct.pack_into("<IIIII", packet, 128, 0, 0, 0, 0, 0)
        return bytes(packet)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_GroupInvite:
        invitee, inviter = two_names(data)
        return cls(invitee, inviter)


@dataclass
class OP_GroupInvite2(EQStruct):
    invitee: str
    inviter: str = ""

    def serialize(self) -> bytes:
        packet = bytearray(148)
        put_fixed(packet, 0, self.invitee, 64)
        put_fixed(packet, 64, self.inviter, 64)
        # common/patches/rof2_structs.h:2569 GroupInvite_Struct
        struct.pack_into("<IIIII", packet, 128, 0, 0, 0, 0, 0)
        return bytes(packet)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_GroupInvite2:
        invitee, inviter = two_names(data)
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
    """RoF2 variable-length group roster."""

    def serialize(self) -> bytes:
        names = [self.your_name] + list(self.members)

        out = bytearray(struct.pack("<II", 0, len(names)))
        out += self.leader.encode("latin1", errors="replace") + b"\0"

        for index, name in enumerate(names):
            out += struct.pack("<I", index)
            out += name.encode("latin1", errors="replace") + b"\0"

            # Merc owner flag, string marker, level, role flags,
            # offline flag, timestamp.
            out += struct.pack(
                "<H B I BBB II",
                0,  # merc owner
                0,  # string marker
                0x46,  # level
                0,  # tank
                0,  # assist
                0,  # puller
                0,  # offline
                0,  # timestamp
            )

        return bytes(out)

    @classmethod
    def deserialize(cls, data: bytes) -> "OP_GroupUpdateB":
        need(data, 8, cls.__name__)

        count = read_u32(data, 4)
        leader, offset = cstring(data, 8)

        names = []
        for _ in range(count):
            need(data[offset:], 4, cls.__name__)
            offset += 4  # member index

            name, offset = cstring(data, offset)
            offset += 18  # fixed member metadata

            names.append(name)

        return cls(
            action=7,
            your_name=names[0] if names else "",
            members=names[1:],
            leader=leader,
            full=True,
        )


@dataclass
class OP_GroupDisbandYou(EQStruct):
    your_name: str = ""
    member_name: str = ""

    def serialize(self) -> bytes:
        out = bytearray(128)
        put_fixed(out, 0, self.your_name, 64)
        put_fixed(out, 64, self.member_name, 64)
        return bytes(out)

    @classmethod
    def deserialize(cls, data: bytes) -> "OP_GroupDisbandYou":
        your_name, member_name = two_names(data)
        return cls(your_name, member_name)


@dataclass
class OP_GroupDisbandOther(EQStruct):
    your_name: str = ""
    member_name: str = ""

    def serialize(self) -> bytes:
        out = bytearray(128)
        put_fixed(out, 0, self.your_name, 64)
        put_fixed(out, 64, self.member_name, 64)
        return bytes(out)

    @classmethod
    def deserialize(cls, data: bytes) -> "OP_GroupDisbandOther":
        your_name, member_name = two_names(data)
        return cls(your_name, member_name)


def _read_group_roster(data: bytes) -> tuple[str, list[str], str]:
    if len(data) < 8:
        return "", [], ""
    count = read_u32(data, 4)
    try:
        leader, offset = cstring(data, 8)
    except ValueError:
        return "", [], ""
    names: list[str] = []
    for _index in range(count):
        if offset + 4 > len(data):
            break
        offset += 4
        try:
            name, offset = cstring(data, offset)
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
        if self.action == 10:
            # zone/client.cpp:860. rof2.cpp:3323 case raidNoRaid queues this buffer unchanged.
            # common/patches/rof2_structs.h:3838 ZoneInSendName_Struct
            return struct.pack("<I64s64sI", self.action & 0xFFFFFFFF, your_name, leader, 0)
        # common/patches/rof2_structs.h:4370 RaidGeneral_Struct
        return struct.pack("<I64sI64sI", self.action & 0xFFFFFFFF, your_name, 0, leader, 0)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_RaidUpdate:
        # common/patches/rof2_structs.h:3838 ZoneInSendName_Struct is 136 bytes.
        # zone/client.cpp:860 sends it with action raidNoRaid (10). rof2.cpp:3323 does not widen it.
        if len(data) == 136:
            return cls(int(read_u32(data)), fixed(data, 4, 64), fixed(data, 68, 64))
        # Add, note, motd, and leadership updates are RaidGeneral_Struct plus a tail.
        # common/patches/rof2_structs.h:4370 RaidGeneral_Struct
        need(data, 140, "OP_RaidUpdate")
        return cls(int(read_u32(data)), fixed(data, 4, 64), fixed(data, 72, 64))


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
        need(data, 140, "OP_RaidJoin")
        return cls(int(read_u32(data)), fixed(data, 4, 64), fixed(data, 72, 64))


def _pack_group(action: int, your_name: str, members: list[str], leader: str, full: bool) -> bytes:
    if full:
        packet = bytearray(452)
        # common/eq_packet_structs.h:2497 GroupUpdate_Struct
        struct.pack_into("<I", packet, 0, action & 0xFFFFFFFF)
        put_fixed(packet, 4, your_name, 64)
        for index in range(5):
            name = members[index] if index < len(members) else ""
            put_fixed(packet, 68 + index * 64, name, 64)
        put_fixed(packet, 388, leader, 64)
        return bytes(packet)
    packet = bytearray(132)
    # common/eq_packet_structs.h:2515 GroupJoin_Struct
    struct.pack_into("<I", packet, 0, action & 0xFFFFFFFF)
    put_fixed(packet, 4, your_name, 64)
    put_fixed(packet, 68, leader, 64)
    return bytes(packet)


def _read_group(data: bytes, full_opcode: bool) -> tuple[int, str, list[str], str, bool]:
    if len(data) < 4:
        return 0, "", [], "", False
    if full_opcode and len(data) == 148:
        return 0, fixed(data, 64, 64), [], "", False
    action = read_u32(data)
    if full_opcode and len(data) >= 452:
        your_name = fixed(data, 4, 64)
        members = [fixed(data, 68 + index * 64, 64) for index in range(5)]
        leader = fixed(data, 388, 64)
        return int(action), your_name, members, leader, True
    if len(data) >= 132:
        return int(action), fixed(data, 4, 64), [], fixed(data, 68, 64), False
    return int(action), "", [], "", False
