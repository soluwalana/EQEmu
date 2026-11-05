import re
import struct
from dataclasses import dataclass, field
from typing import TypeVar

from eqclient4.structs.wire import (
    EQStruct,
    ItemLink,
    MessagePart,
    cstring,
    fixed,
    i32,
    need,
    parse_message_parts,
    put_cstr,
    put_fixed,
    read_u32,
)

SAY_CHANNEL = 8
CHANNEL_MESSAGE_SIZE = 148


@dataclass
class OP_ChannelMessage(EQStruct):
    target: str = ""
    sender: str = ""
    language: int = 0
    channel: int = SAY_CHANNEL
    unused1: int = 0
    unused2: int = 0
    skill: int = 100
    text: str = ""

    def serialize(self) -> bytes:
        # common/patches/rof2.cpp:1025 OP_ChannelMessage
        language = struct.pack(
            "<III",
            0,
            self.language & 0xFFFFFFFF,
            self.channel & 0xFFFFFFFF,
        )
        # common/patches/rof2.cpp:1030 OP_ChannelMessage
        skill = struct.pack(
            "<I",
            max(0, min(100, int(self.skill))) & 0xFFFFFFFF,
        )
        return put_cstr(self.sender) + put_cstr(self.target) + language + b"\x00" * 5 + skill + put_cstr(self.text)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ChannelMessage:
        sender, offset = cstring(data, 0)
        target, offset = cstring(data, offset)
        offset += 4
        language, channel = struct.unpack_from("<II", data, offset)
        offset += 13
        skill = read_u32(data, offset)
        text, _end = cstring(data, offset + 4)
        return cls(target, sender, int(language), int(channel), 0, 0, int(skill), text)

    @property
    def text_parts(self) -> tuple[str | ItemLink, ...]:
        return parse_message_parts(self.text)


@dataclass
class OP_SpecialMesg(EQStruct):
    header: bytes = b"\x00\x00\x00"
    msg_type: int = 0
    target_spawn_id: int = 0
    speaker: str = ""
    unknown: bytes = b"\x00" * 12
    message: str = ""

    def serialize(self) -> bytes:
        head = (self.header + b"\x00\x00\x00")[:3]
        gap = (self.unknown + b"\x00" * 12)[:12]
        # common/patches/rof2.cpp:3805 OP_SpecialMesg message type
        fields = struct.pack("<ii", i32(self.msg_type), i32(self.target_spawn_id))
        return head + fields + put_cstr(self.speaker) + gap + put_cstr(self.message)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_SpecialMesg:
        if len(data) < 11:
            return cls()
        header = data[:3]
        msg_type, target = struct.unpack_from("<ii", data, 3)
        try:
            speaker, offset = cstring(data, 11)
        except ValueError:
            return cls(header, int(msg_type), int(target))
        unknown = data[offset : offset + 12]
        offset += 12
        message = ""
        if offset < len(data):
            try:
                message, _end = cstring(data, offset)
            except ValueError:
                message = ""
        return cls(header, int(msg_type), int(target), speaker, unknown, message)

    @property
    def message_parts(self) -> tuple[MessagePart, ...]:
        return parse_message_parts(self.message)


@dataclass
class OP_SimpleMessage(EQStruct):
    string_id: int
    color: int = 0
    unknown: int = 0
    texts: tuple[str, ...] = ()

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:3832 SimpleMessage_Struct
        out = struct.pack(
            "<III",
            self.string_id & 0xFFFFFFFF,
            self.color & 0xFFFFFFFF,
            self.unknown & 0xFFFFFFFF,
        )
        for text in self.texts:
            out += put_cstr(text)
        return out

    @classmethod
    def deserialize(cls, data: bytes) -> OP_SimpleMessage:
        need(data, 4, "OP_SimpleMessage")
        string_id = read_u32(data)
        color = read_u32(data, 4) if len(data) >= 8 else 0
        unknown = read_u32(data, 8) if len(data) >= 12 else 0
        texts: list[str] = []
        offset = 12
        while offset < len(data):
            try:
                text, offset = cstring(data, offset)
            except ValueError:
                break
            if not text:
                break
            texts.append(text)
        return cls(int(string_id), int(color), int(unknown), tuple(texts))

    @property
    def text_parts(self) -> tuple[tuple[MessagePart, ...], ...]:
        return tuple(parse_message_parts(text) for text in self.texts)


@dataclass
class OP_FormattedMessage(EQStruct):
    """12-byte header plus <=9 null-terminated substitution strings."""

    unknown0: int
    string_id: int
    type: int
    arguments: list[str] = field(default_factory=list)
    trailing: bytes = b""
    terminated: bool = True

    def serialize(self) -> bytes:
        if len(self.arguments) > 9:
            raise ValueError("OP_FormattedMessage can carry at most 9 arguments")
        out = bytearray(struct.pack("<III", self.unknown0, self.string_id, self.type))
        for value in self.arguments:
            out += value.encode("latin1", errors="replace") + b"\0"
        if self.terminated:
            out += b"\0"
        return bytes(out) + self.trailing

    @classmethod
    def deserialize(cls, data: bytes) -> OP_FormattedMessage:
        need(data, 12, cls.__name__)
        header = struct.unpack_from("<III", data)
        args: list[str] = []
        i = 12
        terminated = False
        while i < len(data) and len(args) < 9:
            end = data.find(b"\x00", i)
            if end < 0:
                args.append(data[i:].decode("latin1"))
                i = len(data)
                break
            if end == i:
                i += 1
                terminated = True
                break
            args.append(data[i:end].decode("latin1"))
            i = end + 1
        # When all nine substitution slots are populated, the final NUL is
        # after the ninth string rather than an empty slot in the loop.
        if len(args) == 9 and i < len(data) and data[i] == 0:
            terminated = True
            i += 1
        return cls(header[0], header[1], header[2], args, data[i:], terminated)

    @property
    def argument_parts(self) -> tuple[tuple[MessagePart, ...], ...]:
        return tuple(parse_message_parts(arg) for arg in self.arguments)


@dataclass
class OP_OnLevelMessage(EQStruct):
    title: str = ""
    text: str = ""
    buttons: int = 0
    duration: int = 0
    popup_id: int = 0
    unknown4236: int = 0
    unknown4240: int = 0

    def serialize(self) -> bytes:
        packet = bytearray(4310)
        # common/patches/rof2.cpp:2449 OnLevelMessage_Struct
        struct.pack_into("<I", packet, 0, 128)
        put_fixed(packet, 4, self.title, 128)
        # common/patches/rof2.cpp:2451 OnLevelMessage_Struct
        struct.pack_into("<I", packet, 132, 4096)
        put_fixed(packet, 136, self.text, 4096)
        # common/patches/rof2.cpp:2459 OnLevelMessage_Struct
        struct.pack_into("<I", packet, 4232, 25)
        # common/patches/rof2.cpp:2461 OnLevelMessage_Struct
        struct.pack_into("<I", packet, 4261, 25)
        # common/patches/rof2.cpp:2455 OnLevelMessage_Struct
        struct.pack_into("<I", packet, 4292, self.duration & 0xFFFFFFFF)
        # common/patches/rof2.cpp:2456 OnLevelMessage_Struct
        struct.pack_into("<II", packet, 4296, self.popup_id & 0xFFFFFFFF, self.unknown4236 & 0xFFFFFFFF)
        packet[4290] = self.buttons & 0xFF
        return bytes(packet)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_OnLevelMessage:
        if len(data) < 132:
            return cls()
        title = fixed(data, 4, 128)
        text = fixed(data, 136, 4096) if len(data) >= 4232 else ""
        buttons = data[4290] if len(data) > 4290 else 0
        duration = read_u32(data, 4292) if len(data) >= 4296 else 0
        popup_id = read_u32(data, 4296) if len(data) >= 4300 else 0
        return cls(title, text, int(buttons), int(duration), int(popup_id), 0, 0)


@dataclass
class OP_PopupResponse(EQStruct):
    popup_id: int
    unknown: int = 0

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:1902 PopupResponse_Struct
        return struct.pack(
            "<II",
            self.unknown & 0xFFFFFFFF,
            self.popup_id & 0xFFFFFFFF,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_PopupResponse:
        need(data, 8, "OP_PopupResponse")
        unknown, popup_id = struct.unpack_from("<II", data)
        return cls(int(popup_id), int(unknown))


@dataclass
class OP_RezzRequest(EQStruct):
    zone_id: int = 0
    instance_id: int = 0
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    your_name: str = ""
    unknown88: int = 0
    rezzer_name: str = ""
    spell_id: int = 0
    corpse_name: str = ""
    action: int = 0
    unknown00: int = 0

    def serialize(self) -> bytes:
        return _pack_resurrect(self)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_RezzRequest:
        return _read_resurrect(cls, data)


@dataclass
class OP_RezzAnswer(EQStruct):
    zone_id: int = 0
    instance_id: int = 0
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    your_name: str = ""
    unknown88: int = 0
    rezzer_name: str = ""
    spell_id: int = 0
    corpse_name: str = ""
    action: int = 1
    unknown00: int = 0

    def serialize(self) -> bytes:
        return _pack_resurrect(self)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_RezzAnswer:
        return _read_resurrect(cls, data)


def _pack_resurrect(row: OP_RezzRequest | OP_RezzAnswer) -> bytes:
    packet = bytearray(236)
    # common/patches/rof2_structs.h:3070 Resurrect_Struct
    struct.pack_into(
        "<IHH",
        packet,
        0,
        row.unknown00 & 0xFFFFFFFF,
        row.zone_id & 0xFFFF,
        row.instance_id & 0xFFFF,
    )
    # common/patches/rof2_structs.h:3073 Resurrect_Struct
    struct.pack_into("<fff", packet, 8, row.y, row.x, row.z)
    put_fixed(packet, 24, row.your_name, 64)
    # common/patches/rof2_structs.h:3078 Resurrect_Struct
    struct.pack_into("<I", packet, 88, row.unknown88 & 0xFFFFFFFF)
    put_fixed(packet, 92, row.rezzer_name, 64)
    # common/patches/rof2_structs.h:3080 Resurrect_Struct
    struct.pack_into("<I", packet, 156, row.spell_id & 0xFFFFFFFF)
    put_fixed(packet, 160, row.corpse_name, 64)
    # common/patches/rof2_structs.h:3082 Resurrect_Struct
    struct.pack_into("<I", packet, 224, row.action & 0xFFFFFFFF)
    return bytes(packet)


_Rez = TypeVar("_Rez", OP_RezzRequest, OP_RezzAnswer)


def _read_resurrect(cls: type[_Rez], data: bytes) -> _Rez:
    if len(data) < 8:
        return cls()
    unknown00 = read_u32(data)
    zone_id, instance_id = struct.unpack_from("<HH", data, 4)
    x = y = z = 0.0
    if len(data) >= 20:
        wire_y, wire_x, wire_z = struct.unpack_from("<fff", data, 8)
        x, y, z = float(wire_x), float(wire_y), float(wire_z)

    your_name = fixed(data, 24, 64) if len(data) >= 88 else ""
    unknown88 = read_u32(data, 88) if len(data) >= 92 else 0
    rezzer = fixed(data, 92, 64) if len(data) >= 156 else ""
    spell_id = read_u32(data, 156) if len(data) >= 160 else 0
    corpse = fixed(data, 160, 64) if len(data) >= 224 else ""
    action = read_u32(data, 224) if len(data) >= 228 else 0
    return cls(
        int(zone_id),
        int(instance_id),
        x,
        y,
        z,
        your_name,
        int(unknown88),
        rezzer,
        int(spell_id),
        corpse,
        int(action),
        int(unknown00),
    )


_SAYLINK = re.compile(r"\x12(.{56})([^\x12]+?)\x12")
_QUEST_ITEM = "FFFFF"


def channel_bucket(channel: int) -> str:
    """says, tell, or gm. Other channels are not one of those."""
    if channel in (7, 14):
        return "tell"
    if channel in (11, 18):
        return "gm"
    if channel == SAY_CHANNEL:
        return "says"
    return ""


def special_bucket(msg_type: int) -> str:
    """Say and tell colors stay in those buckets. Every other special line is the server."""
    if msg_type in (10, 256, 307):
        return "says"
    if msg_type in (257, 308):
        return "tell"
    return "server"


def saylink_words(text: str) -> list[str]:
    """Quest saylinks. An item link uses the same brackets and is not something to say."""
    words: list[str] = []
    for match in _SAYLINK.finditer(text or ""):
        body, word = match.group(1), match.group(2).strip()
        if len(body) < 6 or body[1:6].upper() != _QUEST_ITEM:
            continue
        if word and word.lower() not in {item.lower() for item in words}:
            words.append(word)
    return words


def saylink_plain(text: str) -> str:
    """Replace item-link blobs with their visible names for chat logs."""
    if "\x12" not in text:
        return text
    return _SAYLINK.sub(lambda m: m.group(2), text)
