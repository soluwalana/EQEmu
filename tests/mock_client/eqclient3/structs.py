"""One typed object per opcode eqclient3 sends or reads.

Application objects serialize and deserialize the opcode body (little-endian).
Session objects serialize and deserialize the whole datagram (big-endian),
including the leading zero and the session opcode byte.

Coordinates on these objects are x, y, z. Serialize and deserialize convert
the y, x, z order used on the wire.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass, field
from typing import ClassVar, TypeVar

SAY_CHANNEL = 8
SPAWN_SIZE = 385
DOOR_SIZE = 80
LOGIN_BASE_SIZE = 10
LOGIN_INFO_SIZE = 464
ENTER_WORLD_SIZE = 72
ZONE_ENTRY_SIZE = 68
ZONE_SERVER_INFO_SIZE = 130
CHANNEL_MESSAGE_SIZE = 148
NAME_APPROVAL_SIZE = 72
CHAR_CREATE_SIZE = 80
CHAR_SELECT_SLOTS = 10
CHAR_SELECT_SIZE = 1704
NEW_ZONE_SIZE = 700
ZONE_CHANGE_SIZE = 88
GM_TRAINING_SIZE = 448
GM_SKILL_COUNT = 100
PROFILE_SIZE = 13004

ITEM_MERCHANT = 0x64
ITEM_LOOT = 0x66
ITEM_TRADE = 0x67
ITEM_INVENTORY = 0x69
ITEM_SUMMON = 0x6A

OP_SESSION_REQUEST_ID = 0x01
OP_SESSION_RESPONSE_ID = 0x02
OP_COMBINED_ID = 0x03
OP_SESSION_DISCONNECT_ID = 0x05
OP_KEEPALIVE_ID = 0x06
OP_SESSION_STAT_REQUEST_ID = 0x07
OP_SESSION_STAT_RESPONSE_ID = 0x08
OP_PACKET_ID = 0x09
OP_FRAGMENT_ID = 0x0D
OP_OUT_OF_ORDER_ACK_ID = 0x11
OP_ACK_ID = 0x15
OP_APP_COMBINED_ID = 0x19
OP_OUTBOUND_PING_ID = 0x1C
OP_OUT_OF_SESSION_ID = 0x1D

_FACTION_SWAP = {6: 9, 7: 8, 8: 7, 9: 6}

OPERATIONS: dict[str, type] = {}

_S = TypeVar("_S", bound="EQStruct")


class EQStruct:
    """Wire object. Opcode classes register under their name. Nested records do not."""

    opcode: ClassVar[str] = ""

    def __init_subclass__(cls, **kwargs: object) -> None:
        super().__init_subclass__(**kwargs)
        if cls.__name__.startswith("OP_"):
            cls.opcode = cls.__name__
            OPERATIONS[cls.__name__] = cls

    def serialize(self) -> bytes:
        return b""

    @classmethod
    def deserialize(cls: type[_S], data: bytes) -> _S:
        return cls()


def _need(data: bytes, size: int, what: str) -> None:
    if len(data) < size:
        raise ValueError(f"{what} is {len(data)} bytes")


def _u32(value: int) -> bytes:
    return struct.pack("<I", value & 0xFFFFFFFF)


def _read_u32(data: bytes, offset: int = 0) -> int:
    return struct.unpack_from("<I", data, offset)[0]


def _fixed(data: bytes, offset: int, size: int) -> str:
    if offset >= len(data):
        return ""
    chunk = data[offset : min(len(data), offset + size)]
    return chunk.split(b"\x00", 1)[0].decode("latin1", errors="replace")


def _put_fixed(buf: bytearray, offset: int, text: str, size: int) -> None:
    raw = (text or "").encode("latin1", errors="replace")[: size - 1]
    buf[offset : offset + len(raw)] = raw


def _cstring(data: bytes, offset: int) -> tuple[str, int]:
    end = data.find(b"\x00", offset)
    if end < 0:
        raise ValueError("unterminated string")
    return data[offset:end].decode("latin1", errors="replace"), end + 1


def _put_cstr(text: str) -> bytes:
    return (text or "").encode("latin1", errors="replace") + b"\x00"


def _sign_extend(value: int, bits: int) -> int:
    value &= (1 << bits) - 1
    sign = 1 << (bits - 1)
    return value - (1 << bits) if value & sign else value


def _eq19(word: int, shift: int) -> float:
    return _sign_extend(word >> shift, 19) / 8.0


def _pack_eq19(value: float) -> int:
    return int(round(value * 8.0)) & 0x7FFFF


def _faction_from_wire(raw: int) -> int:
    return _FACTION_SWAP.get(raw, raw)


def _faction_to_wire(value: int) -> int:
    return _FACTION_SWAP.get(value, value)


def _pipe_int(fields: list[str], index: int) -> int:
    if index >= len(fields):
        return 0
    text = fields[index].strip()
    if not text or not text.lstrip("-").isdigit():
        return 0
    return int(text)


@dataclass
class LoginBase(EQStruct):
    sequence: int = 0
    compressed: bool = False
    encrypt_type: int = 0
    unknown: int = 0

    def serialize(self) -> bytes:
        return struct.pack("<iBbi", self.sequence, int(self.compressed), self.encrypt_type, self.unknown)

    @classmethod
    def deserialize(cls, data: bytes) -> LoginBase:
        _need(data, LOGIN_BASE_SIZE, "login header")
        sequence, compressed, encrypt_type, unknown = struct.unpack_from("<iBbi", data)
        return cls(int(sequence), bool(compressed), int(encrypt_type), int(unknown))


@dataclass
class ServerEntry(EQStruct):
    ip: str
    server_type: int
    server_id: int
    name: str
    country: str
    language: str
    status: int
    player_count: int


@dataclass
class CharacterSlot(EQStruct):
    name: str
    race: int = 1
    class_id: int = 1
    gender: int = 0
    level: int = 1
    deity: int = 0
    zone_id: int = 0


@dataclass
class Spawn(EQStruct):
    spawn_id: int
    name: str
    npc: int
    level: int
    body: int
    x: float
    y: float
    z: float
    class_id: int
    race: int

    def serialize(self) -> bytes:
        blob = bytearray(SPAWN_SIZE)
        _put_fixed(blob, 7, self.name, 64)
        blob[83] = self.npc & 0xFF
        blob[151] = self.level & 0xFF
        struct.pack_into("<I", blob, 284, self.race & 0xFFFFFFFF)
        blob[331] = self.class_id & 0xFF
        blob[335] = self.body & 0xFF
        struct.pack_into("<I", blob, 340, self.spawn_id & 0xFFFFFFFF)
        struct.pack_into(
            "<iii",
            blob,
            94,
            _pack_eq19(self.x) << 10,
            _pack_eq19(self.y),
            _pack_eq19(self.z),
        )
        return bytes(blob)

    @classmethod
    def deserialize(cls, data: bytes) -> Spawn:
        _need(data, SPAWN_SIZE, "spawn")
        word_x, word_y, word_z = struct.unpack_from("<iii", data, 94)
        return cls(
            _read_u32(data, 340),
            _fixed(data, 7, 64),
            data[83],
            data[151],
            data[335],
            _eq19(word_x, 10),
            _eq19(word_y, 0),
            _eq19(word_z, 0),
            data[331],
            _read_u32(data, 284),
        )


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
        struct.pack_into("<fff", blob, 32, self.y, self.x, self.z)
        blob[60] = self.door_id & 0xFF
        blob[61] = self.open_type & 0xFF
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

    def text(self) -> str:
        instance = ["0", "0", "0", "0"]
        instance[0] = str(int(self.stack))
        instance[2] = str(int(self.slot))
        instance[3] = str(int(self.price))
        static = [""] * 155
        static[1] = self.name
        static[3] = self.id_file
        static[4] = str(int(self.item_id))
        static[8] = str(int(self.size))
        static[9] = str(int(self.slots))
        static[30] = str(int(self.ac))
        static[40] = str(int(self.required_level))
        static[50] = str(int(self.damage))
        static[52] = str(int(self.classes))
        static[53] = str(int(self.races))
        static[56] = str(int(self.item_type))
        static[97] = str(int(self.bag_slots))
        static[98] = str(int(self.bag_size))
        static[154] = str(int(self.scroll_effect))
        return "|".join(instance) + '"' + "|".join(static)

    def serialize(self) -> bytes:
        return _u32(self.kind) + self.text().encode("latin1", errors="replace") + b"\x00"

    @classmethod
    def deserialize(cls, data: bytes) -> Item:
        parsed = _parse_item(data)
        if parsed is None:
            raise ValueError("item packet has no serialized item")
        return parsed


def _parse_item(data: bytes) -> Item | None:
    if len(data) < 5:
        return None
    kind = _read_u32(data)
    text = data[4:].split(b"\x00", 1)[0].decode("latin1", errors="replace")
    quote = text.find('"')
    if quote < 0:
        return None
    instance = text[:quote].split("|")
    static = text[quote + 1 :].split("|")
    if len(instance) < 3 or len(static) < 5 or not static[4].lstrip("-").isdigit():
        return None
    slot = int(instance[2]) if instance[2].lstrip("-").isdigit() else 0
    stack = int(instance[0]) if instance[0].lstrip("-").isdigit() else 1
    if stack <= 0:
        stack = 1
    price = int(instance[3]) if len(instance) > 3 and instance[3].lstrip("-").isdigit() else 0
    return Item(
        kind,
        slot,
        static[1],
        static[3],
        int(static[4]),
        stack,
        _pipe_int(static, 9),
        _pipe_int(static, 52),
        _pipe_int(static, 53),
        _pipe_int(static, 30),
        _pipe_int(static, 50),
        _pipe_int(static, 40),
        _pipe_int(static, 8),
        _pipe_int(static, 97),
        _pipe_int(static, 98),
        _pipe_int(static, 56),
        _pipe_int(static, 154),
        price,
    )


@dataclass
class TaskElement(EQStruct):
    activity_id: int
    kind: int
    request: int
    target: str
    item_list: str
    goal: int
    skill: int
    spell: int
    zone_id: int
    description: str


@dataclass
class TaskChoice(EQStruct):
    task_id: int
    duration: int
    duration_code: int
    title: str
    description: str
    elements: list[TaskElement] = field(default_factory=list)


@dataclass
class SpellBuff(EQStruct):
    effect_type: int = 0
    level: int = 0
    bard_modifier: int = 0
    unknown: int = 0
    spell_id: int = 0
    duration: int = 0
    counters: int = 0
    caster_id: int = 0


def _pack_server_position(spawn_id: int, x: float, y: float, z: float) -> bytes:
    return struct.pack(
        "<Hiiiii",
        spawn_id & 0xFFFF,
        _pack_eq19(x) << 10,
        _pack_eq19(y),
        _pack_eq19(z),
        0,
        0,
    )


def _read_server_position(data: bytes) -> tuple[int, float, float, float]:
    _need(data, 22, "server position")
    spawn_id = struct.unpack_from("<H", data)[0]
    word_x, word_y, word_z = struct.unpack_from("<iii", data, 2)
    return spawn_id, _eq19(word_x, 10), _eq19(word_y, 0), _eq19(word_z, 0)


def _pack_names(first: str, second: str, size: int = 128) -> bytes:
    packet = bytearray(size)
    _put_fixed(packet, 0, first, 64)
    _put_fixed(packet, 64, second, 64)
    return bytes(packet)


def _two_names(data: bytes) -> tuple[str, str]:
    first = _fixed(data, 0, 64) if len(data) >= 64 else ""
    second = _fixed(data, 64, 64) if len(data) >= 128 else ""
    return first, second


# --- session datagrams -------------------------------------------------------


@dataclass
class OP_SESSION_REQUEST(EQStruct):
    protocol_version: int = 3
    connect_code: int = 0
    max_packet_size: int = 512

    def serialize(self) -> bytes:
        return struct.pack(
            ">BBIII",
            0,
            OP_SESSION_REQUEST_ID,
            self.protocol_version & 0xFFFFFFFF,
            self.connect_code & 0xFFFFFFFF,
            self.max_packet_size & 0xFFFFFFFF,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_SESSION_REQUEST:
        _need(data, 14, "OP_SESSION_REQUEST")
        _zero, _opcode, version, code, max_size = struct.unpack(">BBIII", data[:14])
        return cls(int(version), int(code), int(max_size))


@dataclass
class OP_SESSION_RESPONSE(EQStruct):
    connect_code: int
    encode_key: int
    crc_bytes: int
    encode_pass1: int
    encode_pass2: int
    max_packet_size: int

    def serialize(self) -> bytes:
        return struct.pack(
            ">BBIIBBBI",
            0,
            OP_SESSION_RESPONSE_ID,
            self.connect_code & 0xFFFFFFFF,
            self.encode_key & 0xFFFFFFFF,
            self.crc_bytes & 0xFF,
            self.encode_pass1 & 0xFF,
            self.encode_pass2 & 0xFF,
            self.max_packet_size & 0xFFFFFFFF,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_SESSION_RESPONSE:
        _need(data, 17, "OP_SESSION_RESPONSE")
        _zero, _opcode, code, key, crc_bytes, pass1, pass2, max_size = struct.unpack(">BBIIBBBI", data[:17])
        return cls(int(code), int(key), int(crc_bytes), int(pass1), int(pass2), int(max_size))


@dataclass
class OP_COMBINED(EQStruct):
    parts: tuple[bytes, ...] = ()

    def serialize(self) -> bytes:
        out = bytearray((0, OP_COMBINED_ID))
        for part in self.parts:
            if len(part) > 255:
                raise ValueError(f"combined part is {len(part)} bytes")
            out.append(len(part))
            out += part
        return bytes(out)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_COMBINED:
        parts: list[bytes] = []
        offset = 2
        while offset < len(data):
            length = data[offset]
            offset += 1
            if offset + length > len(data):
                break
            parts.append(data[offset : offset + length])
            offset += length
        return cls(tuple(parts))


@dataclass
class OP_SESSION_DISCONNECT(EQStruct):
    connect_code: int = 0

    def serialize(self) -> bytes:
        return struct.pack(">BBI", 0, OP_SESSION_DISCONNECT_ID, self.connect_code & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_SESSION_DISCONNECT:
        _need(data, 6, "OP_SESSION_DISCONNECT")
        _zero, _opcode, code = struct.unpack(">BBI", data[:6])
        return cls(int(code))


@dataclass
class OP_KEEPALIVE(EQStruct):
    def serialize(self) -> bytes:
        return bytes((0, OP_KEEPALIVE_ID))

    @classmethod
    def deserialize(cls, data: bytes) -> OP_KEEPALIVE:
        return cls()


@dataclass
class OP_SESSION_STAT_REQUEST(EQStruct):
    timestamp: int = 0
    stat_ping: int = 0
    avg_ping: int = 0
    min_ping: int = 0
    max_ping: int = 0
    last_ping: int = 0
    packets_sent: int = 0
    packets_recv: int = 0

    def serialize(self) -> bytes:
        return struct.pack(
            ">BBHIIIIIQQ",
            0,
            OP_SESSION_STAT_REQUEST_ID,
            self.timestamp & 0xFFFF,
            self.stat_ping & 0xFFFFFFFF,
            self.avg_ping & 0xFFFFFFFF,
            self.min_ping & 0xFFFFFFFF,
            self.max_ping & 0xFFFFFFFF,
            self.last_ping & 0xFFFFFFFF,
            self.packets_sent & 0xFFFFFFFFFFFFFFFF,
            self.packets_recv & 0xFFFFFFFFFFFFFFFF,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_SESSION_STAT_REQUEST:
        _need(data, 40, "OP_SESSION_STAT_REQUEST")
        values = struct.unpack(">BBHIIIIIQQ", data[:40])
        return cls(*(int(value) for value in values[2:]))


@dataclass
class OP_SESSION_STAT_RESPONSE(EQStruct):
    timestamp: int = 0
    our_timestamp: int = 0
    client_sent: int = 0
    client_recv: int = 0
    server_sent: int = 0
    server_recv: int = 0

    def serialize(self) -> bytes:
        return struct.pack(
            ">BBHIQQQQ",
            0,
            OP_SESSION_STAT_RESPONSE_ID,
            self.timestamp & 0xFFFF,
            self.our_timestamp & 0xFFFFFFFF,
            self.client_sent & 0xFFFFFFFFFFFFFFFF,
            self.client_recv & 0xFFFFFFFFFFFFFFFF,
            self.server_sent & 0xFFFFFFFFFFFFFFFF,
            self.server_recv & 0xFFFFFFFFFFFFFFFF,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_SESSION_STAT_RESPONSE:
        _need(data, 40, "OP_SESSION_STAT_RESPONSE")
        values = struct.unpack(">BBHIQQQQ", data[:40])
        return cls(*(int(value) for value in values[2:]))


@dataclass
class OP_PACKET(EQStruct):
    stream_id: int
    sequence: int
    payload: bytes

    def serialize(self) -> bytes:
        header = struct.pack(">BBH", 0, OP_PACKET_ID + (self.stream_id & 3), self.sequence & 0xFFFF)
        return header + self.payload

    @classmethod
    def deserialize(cls, data: bytes) -> OP_PACKET:
        _need(data, 4, "OP_PACKET")
        _zero, opcode, sequence = struct.unpack(">BBH", data[:4])
        stream_id = int(opcode) - OP_PACKET_ID
        return cls(stream_id, int(sequence), data[4:])


@dataclass
class OP_FRAGMENT(EQStruct):
    stream_id: int
    sequence: int
    data: bytes
    total_size: int | None = None

    def serialize(self) -> bytes:
        header = struct.pack(">BBH", 0, OP_FRAGMENT_ID + (self.stream_id & 3), self.sequence & 0xFFFF)
        if self.total_size is None:
            return header + self.data
        return header + struct.pack(">I", self.total_size & 0xFFFFFFFF) + self.data

    @classmethod
    def deserialize(cls, data: bytes) -> OP_FRAGMENT:
        """Continuation fragment. A first fragment's total size stays in `data`."""
        _need(data, 4, "OP_FRAGMENT")
        _zero, opcode, sequence = struct.unpack(">BBH", data[:4])
        return cls(int(opcode) - OP_FRAGMENT_ID, int(sequence), data[4:])


@dataclass
class OP_OUT_OF_ORDER_ACK(EQStruct):
    stream_id: int
    sequence: int

    def serialize(self) -> bytes:
        return struct.pack(">BBH", 0, OP_OUT_OF_ORDER_ACK_ID + (self.stream_id & 3), self.sequence & 0xFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_OUT_OF_ORDER_ACK:
        _need(data, 4, "OP_OUT_OF_ORDER_ACK")
        _zero, opcode, sequence = struct.unpack(">BBH", data[:4])
        return cls(int(opcode) - OP_OUT_OF_ORDER_ACK_ID, int(sequence))


@dataclass
class OP_ACK(EQStruct):
    stream_id: int
    sequence: int

    def serialize(self) -> bytes:
        return struct.pack(">BBH", 0, OP_ACK_ID + (self.stream_id & 3), self.sequence & 0xFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ACK:
        _need(data, 4, "OP_ACK")
        _zero, opcode, sequence = struct.unpack(">BBH", data[:4])
        return cls(int(opcode) - OP_ACK_ID, int(sequence))


@dataclass
class OP_APP_COMBINED(EQStruct):
    parts: tuple[bytes, ...] = ()

    def serialize(self) -> bytes:
        out = bytearray((0, OP_APP_COMBINED_ID))
        for part in self.parts:
            length = len(part)
            if length < 0xFF:
                out.append(length)
            elif length <= 0xFFFF:
                out.append(0xFF)
                out += struct.pack(">H", length)
            else:
                out += b"\xff\xff\xff"
                out += struct.pack(">I", length)
            out += part
        return bytes(out)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_APP_COMBINED:
        parts: list[bytes] = []
        offset = 2
        end = len(data)
        while offset < end:
            if data[offset] == 0xFF:
                if offset + 3 > end:
                    break
                if data[offset + 1] == 0xFF and data[offset + 2] == 0xFF:
                    if offset + 7 > end:
                        break
                    length = struct.unpack_from(">I", data, offset + 3)[0]
                    offset += 7
                else:
                    length = struct.unpack_from(">H", data, offset + 1)[0]
                    offset += 3
            else:
                length = data[offset]
                offset += 1
            if offset + length > end:
                break
            parts.append(data[offset : offset + length])
            offset += length
        return cls(tuple(parts))


@dataclass
class OP_OUTBOUND_PING(EQStruct):
    payload: bytes = b""

    def serialize(self) -> bytes:
        return bytes((0, OP_OUTBOUND_PING_ID)) + self.payload

    @classmethod
    def deserialize(cls, data: bytes) -> OP_OUTBOUND_PING:
        return cls(data[2:])


@dataclass
class OP_OUT_OF_SESSION(EQStruct):
    connect_code: int = 0

    def serialize(self) -> bytes:
        return struct.pack(">BBI", 0, OP_OUT_OF_SESSION_ID, self.connect_code & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_OUT_OF_SESSION:
        _need(data, 6, "OP_OUT_OF_SESSION")
        _zero, _opcode, code = struct.unpack(">BBI", data[:6])
        return cls(int(code))


# --- login server ------------------------------------------------------------


@dataclass
class OP_SessionReady(EQStruct):
    value: int = 1

    def serialize(self) -> bytes:
        return _u32(self.value)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_SessionReady:
        _need(data, 4, "OP_SessionReady")
        return cls(_read_u32(data))


@dataclass
class OP_ChatMessage(EQStruct):
    sequence: int = 0
    compressed: bool = False
    encrypt_type: int = 0
    unknown: int = 0
    success: bool = False
    error_id: int = 0
    message: str = ""
    extra: str = ""

    def serialize(self) -> bytes:
        head = LoginBase(self.sequence, self.compressed, self.encrypt_type, self.unknown).serialize()
        reply = bytes((int(self.success),)) + struct.pack("<i", self.error_id) + _put_cstr(self.message) + _put_cstr(self.extra)
        return head + reply

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ChatMessage:
        if len(data) < LOGIN_BASE_SIZE:
            return cls()
        base = LoginBase.deserialize(data)
        offset = LOGIN_BASE_SIZE
        success = False
        error_id = 0
        message = ""
        extra = ""
        if offset < len(data):
            success = bool(data[offset])
            offset += 1
        if offset + 4 <= len(data):
            error_id = struct.unpack_from("<i", data, offset)[0]
            offset += 4
        try:
            message, offset = _cstring(data, offset)
            extra, offset = _cstring(data, offset)
        except ValueError:
            pass
        return cls(base.sequence, base.compressed, base.encrypt_type, base.unknown, success, int(error_id), message, extra)


@dataclass
class OP_Login(EQStruct):
    username: str = ""
    password: str = ""
    sequence: int = 3
    compressed: bool = False
    encrypt_type: int = 2
    unknown: int = 0
    cipher: bytes = b""

    def serialize(self) -> bytes:
        head = LoginBase(self.sequence, self.compressed, self.encrypt_type, self.unknown).serialize()
        if self.cipher:
            return head + self.cipher
        return head + _put_cstr(self.username) + _put_cstr(self.password)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_Login:
        base = LoginBase.deserialize(data)
        rest = data[LOGIN_BASE_SIZE:]
        pair = _credential_pair(rest)
        if pair is None:
            return cls("", "", base.sequence, base.compressed, base.encrypt_type, base.unknown, rest)
        username, password = pair
        return cls(username, password, base.sequence, base.compressed, base.encrypt_type, base.unknown, b"")


def _credential_pair(rest: bytes) -> tuple[str, str] | None:
    try:
        username, offset = _cstring(rest, 0)
        password, end = _cstring(rest, offset)
    except ValueError:
        return None
    if end != len(rest) or not username.isascii() or not password.isascii():
        return None
    return username, password


@dataclass
class OP_LoginAccepted(EQStruct):
    success: bool = True
    error_id: int = 0
    message: str = ""
    unknown1: int = 0
    unknown2: int = 0
    account_id: int = 0
    key: str = ""
    failed_attempts: int = 0
    show_player_count: bool = False
    offer_min_days: int = 0
    offer_min_views: int = 0
    offer_cooldown_minutes: int = 0
    web_offer_number: int = 0
    web_offer_min_days: int = 0
    web_offer_min_views: int = 0
    web_offer_cooldown_minutes: int = 0
    username: str = ""

    def serialize(self) -> bytes:
        """Decrypted reply body. The login session encrypts this before send."""
        out = bytearray()
        out.append(int(self.success))
        out += struct.pack("<i", self.error_id)
        out += _put_cstr(self.message)
        out.append(self.unknown1 & 0xFF)
        out.append(self.unknown2 & 0xFF)
        out += struct.pack("<i", self.account_id)
        key = self.key.encode("latin1", errors="replace")[:10]
        out += key + b"\x00" * (11 - len(key))
        out += struct.pack("<i", self.failed_attempts)
        out.append(int(self.show_player_count))
        out += struct.pack(
            "<7i",
            self.offer_min_days,
            self.offer_min_views,
            self.offer_cooldown_minutes,
            self.web_offer_number,
            self.web_offer_min_days,
            self.web_offer_min_views,
            self.web_offer_cooldown_minutes,
        )
        out += _put_cstr(self.username)
        return bytes(out)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_LoginAccepted:
        """`data` is the decrypted reply, without the 10-byte login header."""
        _need(data, 23, "OP_LoginAccepted")
        success = bool(data[0])
        error_id = struct.unpack_from("<i", data, 1)[0]
        message, offset = _cstring(data, 5)
        unknown1 = data[offset] if offset < len(data) else 0
        unknown2 = data[offset + 1] if offset + 1 < len(data) else 0
        account_at = offset + 2
        _need(data, account_at + 4 + 11, "OP_LoginAccepted")
        account_id = struct.unpack_from("<i", data, account_at)[0]
        key = data[account_at + 4 : account_at + 15].split(b"\x00", 1)[0].decode("latin1", errors="replace")
        cursor = account_at + 15
        failed = show = 0
        offers = [0, 0, 0, 0, 0, 0, 0]
        username = ""
        if cursor + 4 <= len(data):
            failed = struct.unpack_from("<i", data, cursor)[0]
            cursor += 4
        if cursor < len(data):
            show = data[cursor]
            cursor += 1
        if cursor + 28 <= len(data):
            offers = [int(value) for value in struct.unpack_from("<7i", data, cursor)]
            cursor += 28
        if cursor < len(data):
            try:
                username, _end = _cstring(data, cursor)
            except ValueError:
                username = ""
        return cls(
            success,
            int(error_id),
            message,
            unknown1,
            unknown2,
            int(account_id),
            key,
            int(failed),
            bool(show),
            *(int(value) for value in offers),
            username,
        )


@dataclass
class OP_ServerListRequest(EQStruct):
    sequence: int = 4

    def serialize(self) -> bytes:
        return _u32(self.sequence)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ServerListRequest:
        _need(data, 4, "OP_ServerListRequest")
        return cls(_read_u32(data))


@dataclass
class OP_ServerListResponse(EQStruct):
    sequence: int = 4
    compressed: bool = False
    encrypt_type: int = 0
    unknown: int = 0
    success: bool = True
    error_id: int = 0
    message: str = ""
    servers: list[ServerEntry] = field(default_factory=list)

    def serialize(self) -> bytes:
        out = bytearray(LoginBase(self.sequence, self.compressed, self.encrypt_type, self.unknown).serialize())
        out.append(int(self.success))
        out += struct.pack("<i", self.error_id)
        out += _put_cstr(self.message)
        out += struct.pack("<i", len(self.servers))
        for server in self.servers:
            out += _put_cstr(server.ip)
            out += struct.pack("<iI", server.server_type, server.server_id & 0xFFFFFFFF)
            out += _put_cstr(server.name)
            out += _put_cstr(server.country)
            out += _put_cstr(server.language)
            out += struct.pack("<ii", server.status, server.player_count)
        return bytes(out)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ServerListResponse:
        if len(data) < LOGIN_BASE_SIZE:
            return cls()
        base = LoginBase.deserialize(data)
        offset = LOGIN_BASE_SIZE
        success = bool(data[offset]) if offset < len(data) else False
        offset += 1
        error_id = struct.unpack_from("<i", data, offset)[0] if offset + 4 <= len(data) else 0
        offset += 4
        message = ""
        try:
            message, offset = _cstring(data, offset)
        except ValueError:
            return cls(base.sequence, base.compressed, base.encrypt_type, base.unknown, success, int(error_id), message)
        servers: list[ServerEntry] = []
        if offset + 4 > len(data):
            return cls(base.sequence, base.compressed, base.encrypt_type, base.unknown, success, int(error_id), message, servers)
        count = struct.unpack_from("<i", data, offset)[0]
        offset += 4
        for _index in range(max(0, count)):
            try:
                ip, offset = _cstring(data, offset)
            except ValueError:
                break
            if offset + 8 > len(data):
                break
            server_type, server_id = struct.unpack_from("<iI", data, offset)
            offset += 8
            try:
                name, offset = _cstring(data, offset)
                country, offset = _cstring(data, offset)
                language, offset = _cstring(data, offset)
            except ValueError:
                break
            if offset + 8 > len(data):
                break
            status, players = struct.unpack_from("<ii", data, offset)
            offset += 8
            servers.append(ServerEntry(ip, int(server_type), int(server_id), name, country, language, int(status), int(players)))
        return cls(base.sequence, base.compressed, base.encrypt_type, base.unknown, success, int(error_id), message, servers)


@dataclass
class OP_PlayEverquestRequest(EQStruct):
    server_id: int
    sequence: int = 5
    compressed: bool = False
    encrypt_type: int = 0
    unknown: int = 0

    def serialize(self) -> bytes:
        return LoginBase(self.sequence, self.compressed, self.encrypt_type, self.unknown).serialize() + _u32(self.server_id)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_PlayEverquestRequest:
        _need(data, LOGIN_BASE_SIZE + 4, "OP_PlayEverquestRequest")
        base = LoginBase.deserialize(data)
        return cls(_read_u32(data, LOGIN_BASE_SIZE), base.sequence, base.compressed, base.encrypt_type, base.unknown)


@dataclass
class OP_PlayEverquestResponse(EQStruct):
    sequence: int = 0
    compressed: bool = False
    encrypt_type: int = 0
    unknown: int = 0
    success: bool = False
    error_id: int = 0
    message: str = ""
    server_id: int = 0

    def serialize(self) -> bytes:
        out = bytearray(LoginBase(self.sequence, self.compressed, self.encrypt_type, self.unknown).serialize())
        out.append(int(self.success))
        out += struct.pack("<i", self.error_id)
        out += _put_cstr(self.message)
        out += _u32(self.server_id)
        return bytes(out)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_PlayEverquestResponse:
        if len(data) < LOGIN_BASE_SIZE:
            return cls()
        base = LoginBase.deserialize(data)
        offset = LOGIN_BASE_SIZE
        success = bool(data[offset]) if offset < len(data) else False
        offset += 1
        error_id = struct.unpack_from("<i", data, offset)[0] if offset + 4 <= len(data) else 0
        offset += 4
        message = ""
        try:
            message, offset = _cstring(data, offset)
        except ValueError:
            offset = len(data)
        server_id = _read_u32(data, offset) if offset + 4 <= len(data) else 0
        return cls(base.sequence, base.compressed, base.encrypt_type, base.unknown, success, int(error_id), message, int(server_id))


# --- world entry -------------------------------------------------------------


@dataclass
class OP_SendLoginInfo(EQStruct):
    account_id: int
    key: str
    zoning: bool = False

    def serialize(self) -> bytes:
        packet = bytearray(LOGIN_INFO_SIZE)
        creds = f"{self.account_id}\x00{self.key}".encode("latin1", errors="replace")
        packet[: min(len(creds), 64)] = creds[:64]
        if self.zoning:
            packet[188] = 1
        return bytes(packet)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_SendLoginInfo:
        _need(data, 64, "OP_SendLoginInfo")
        parts = data[:64].split(b"\x00")
        account_id = int(parts[0]) if parts and parts[0].isdigit() else 0
        key = parts[1].decode("latin1", errors="replace") if len(parts) > 1 else ""
        zoning = len(data) > 188 and data[188] == 1
        return cls(account_id, key, zoning)


@dataclass
class OP_SendCharInfo(EQStruct):
    slots: list[CharacterSlot] = field(default_factory=list)

    def serialize(self) -> bytes:
        packet = bytearray(CHAR_SELECT_SIZE)
        for index, slot in enumerate(self.slots[:CHAR_SELECT_SLOTS]):
            struct.pack_into("<I", packet, index * 4, slot.race & 0xFFFFFFFF)
            struct.pack_into("<I", packet, 832 + index * 4, slot.deity & 0xFFFFFFFF)
            struct.pack_into("<I", packet, 964 + index * 4, slot.zone_id & 0xFFFFFFFF)
            packet[1004 + index] = slot.class_id & 0xFF
            packet[1664 + index] = slot.gender & 0xFF
            packet[1694 + index] = slot.level & 0xFF
            _put_fixed(packet, 1024 + index * 64, slot.name, 64)
        return bytes(packet)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_SendCharInfo:
        slots: list[CharacterSlot] = []
        for index in range(CHAR_SELECT_SLOTS):
            name_at = 1024 + index * 64
            if name_at + 64 > len(data):
                break
            name = _fixed(data, name_at, 64)
            race = _read_u32(data, index * 4) if index * 4 + 4 <= len(data) else 0
            deity = _read_u32(data, 832 + index * 4) if 832 + index * 4 + 4 <= len(data) else 0
            zone_id = _read_u32(data, 964 + index * 4) if 964 + index * 4 + 4 <= len(data) else 0
            class_id = data[1004 + index] if 1004 + index < len(data) else 0
            gender = data[1664 + index] if 1664 + index < len(data) else 0
            level = data[1694 + index] if 1694 + index < len(data) else 0
            if name or race or class_id:
                slots.append(CharacterSlot(name, int(race), int(class_id), int(gender), int(level), int(deity), int(zone_id)))
        return cls(slots)


@dataclass
class OP_ApproveName(EQStruct):
    name: str = ""
    race: int = 0
    class_id: int = 0
    approved: bool | None = None

    def serialize(self) -> bytes:
        if self.name:
            packet = bytearray(NAME_APPROVAL_SIZE)
            _put_fixed(packet, 0, self.name, 64)
            struct.pack_into("<II", packet, 64, self.race & 0xFFFFFFFF, self.class_id & 0xFFFFFFFF)
            return bytes(packet)
        return bytes((1 if self.approved else 0,))

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ApproveName:
        if len(data) >= 64:
            race = class_id = 0
            if len(data) >= NAME_APPROVAL_SIZE:
                race, class_id = struct.unpack_from("<II", data, 64)
            return cls(_fixed(data, 0, 64), int(race), int(class_id), None)
        if not data:
            raise ValueError("OP_ApproveName is empty")
        return cls(approved=data[0] == 1)


@dataclass
class OP_CharacterCreate(EQStruct):
    class_id: int
    race: int
    gender: int
    deity: int
    start_zone: int
    strength: int
    stamina: int
    agility: int
    dexterity: int
    wisdom: int
    intelligence: int
    charisma: int
    hair_color: int = 0
    beard_color: int = 0
    beard: int = 0
    hair_style: int = 0
    face: int = 0
    eye_color1: int = 0
    eye_color2: int = 0
    tutorial: int = 0

    def serialize(self) -> bytes:
        return struct.pack(
            "<20I",
            self.class_id,
            self.hair_color,
            self.beard_color,
            self.beard,
            self.gender,
            self.race,
            self.start_zone,
            self.hair_style,
            self.deity,
            self.strength,
            self.stamina,
            self.agility,
            self.dexterity,
            self.wisdom,
            self.intelligence,
            self.charisma,
            self.face,
            self.eye_color1,
            self.eye_color2,
            self.tutorial,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_CharacterCreate:
        _need(data, CHAR_CREATE_SIZE, "OP_CharacterCreate")
        (
            class_id,
            hair_color,
            beard_color,
            beard,
            gender,
            race,
            start_zone,
            hair_style,
            deity,
            strength,
            stamina,
            agility,
            dexterity,
            wisdom,
            intelligence,
            charisma,
            face,
            eye_color1,
            eye_color2,
            tutorial,
        ) = struct.unpack_from("<20I", data)
        return cls(
            int(class_id),
            int(race),
            int(gender),
            int(deity),
            int(start_zone),
            int(strength),
            int(stamina),
            int(agility),
            int(dexterity),
            int(wisdom),
            int(intelligence),
            int(charisma),
            int(hair_color),
            int(beard_color),
            int(beard),
            int(hair_style),
            int(face),
            int(eye_color1),
            int(eye_color2),
            int(tutorial),
        )


@dataclass
class OP_EnterWorld(EQStruct):
    name: str
    tutorial: int = 0
    return_home: int = 0

    def serialize(self) -> bytes:
        packet = bytearray(ENTER_WORLD_SIZE)
        _put_fixed(packet, 0, self.name, 64)
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
        _put_fixed(packet, 64, self.short_name, 32)
        _put_fixed(packet, 96, self.long_name, 278)
        struct.pack_into("<fff", packet, 492, self.y, self.x, self.z)
        struct.pack_into("<HH", packet, 684, self.zone_id & 0xFFFF, self.instance_id & 0xFFFF)
        return bytes(packet)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_NewZone:
        _need(data, 504, "OP_NewZone")
        safe_y, safe_x, safe_z = struct.unpack_from("<fff", data, 492)
        zone_id = instance_id = 0
        if len(data) >= 686:
            zone_id = struct.unpack_from("<H", data, 684)[0]
        if len(data) >= 688:
            instance_id = struct.unpack_from("<H", data, 686)[0]
        return cls(
            _fixed(data, 64, 32),
            float(safe_x),
            float(safe_y),
            float(safe_z),
            int(zone_id),
            int(instance_id),
            _fixed(data, 0, 64),
            _fixed(data, 96, 278),
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
        return struct.pack(
            "<HHffffI",
            self.zone_id & 0xFFFF,
            self.instance_id & 0xFFFF,
            self.y,
            self.x,
            self.z,
            self.heading,
            self.kind & 0xFFFFFFFF,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_RequestClientZoneChange:
        _need(data, 16, "OP_RequestClientZoneChange")
        zone_id, instance_id = struct.unpack_from("<HH", data)
        wire_y, wire_x, wire_z = struct.unpack_from("<fff", data, 4)
        heading = struct.unpack_from("<f", data, 16)[0] if len(data) >= 20 else 0.0
        kind = _read_u32(data, 20) if len(data) >= 24 else 0
        return cls(int(zone_id), float(wire_x), float(wire_y), float(wire_z), int(instance_id), float(heading), int(kind))


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
        struct.pack_into("<HH", packet, 64, self.zone_id & 0xFFFF, self.instance_id & 0xFFFF)
        struct.pack_into("<fff", packet, 68, self.y, self.x, self.z)
        struct.pack_into("<Ii", packet, 80, self.zone_reason & 0xFFFFFFFF, self.success)
        return bytes(packet)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ZoneChange:
        _need(data, ZONE_CHANGE_SIZE, "OP_ZoneChange")
        zone_id, instance_id = struct.unpack_from("<HH", data, 64)
        wire_y, wire_x, wire_z = struct.unpack_from("<fff", data, 68)
        zone_reason, success = struct.unpack_from("<Ii", data, 80)
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
        return struct.pack(
            "<HHffff",
            self.zone_id & 0xFFFF,
            self.instance_id & 0xFFFF,
            self.x,
            self.y,
            self.z,
            self.heading,
        ) + _put_cstr(self.zone_name)

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


# --- movement and spawns -----------------------------------------------------


@dataclass
class OP_FloatListThing(EQStruct):
    x: float
    y: float
    z: float
    timestamp: int
    sample_type: int = 0

    def serialize(self) -> bytes:
        return struct.pack("<fffBI", self.y, self.x, self.z, self.sample_type & 0xFF, self.timestamp & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_FloatListThing:
        _need(data, 17, "OP_FloatListThing")
        wire_y, wire_x, wire_z, sample_type, timestamp = struct.unpack_from("<fffBI", data)
        return cls(float(wire_x), float(wire_y), float(wire_z), int(timestamp), int(sample_type))


@dataclass
class OP_ClientUpdate(EQStruct):
    spawn_id: int
    x: float
    y: float
    z: float
    sequence: int = 0
    heading: int = 0
    animation: int = 0
    delta_x: float = 0.0
    delta_y: float = 0.0
    delta_z: float = 0.0
    server: bool = False

    def serialize(self) -> bytes:
        if self.server:
            return _pack_server_position(self.spawn_id, self.x, self.y, self.z)
        anim_word = (self.animation & 0x3FF) | (1 << 20)
        return struct.pack(
            "<HH4fI2fH2s",
            self.spawn_id & 0xFFFF,
            self.sequence & 0xFFFF,
            self.y,
            self.delta_z,
            self.delta_x,
            self.delta_y,
            anim_word,
            self.x,
            self.z,
            (self.heading * 4) & 0xFFF,
            b"\x00\x00",
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ClientUpdate:
        if len(data) >= 36:
            spawn_id, sequence = struct.unpack_from("<HH", data)
            wire_y, delta_z, delta_x, delta_y = struct.unpack_from("<4f", data, 4)
            anim_word = _read_u32(data, 20)
            x, z = struct.unpack_from("<ff", data, 24)
            heading = struct.unpack_from("<H", data, 32)[0] // 4 & 0xFFF
            return cls(
                int(spawn_id),
                float(x),
                float(wire_y),
                float(z),
                int(sequence),
                int(heading),
                int(anim_word) & 0x3FF,
                float(delta_x),
                float(delta_y),
                float(delta_z),
                False,
            )
        spawn_id, x, y, z = _read_server_position(data)
        return cls(spawn_id, x, y, z, server=True)


@dataclass
class OP_MobUpdate(EQStruct):
    spawn_id: int
    x: float
    y: float
    z: float

    def serialize(self) -> bytes:
        return _pack_server_position(self.spawn_id, self.x, self.y, self.z)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_MobUpdate:
        spawn_id, x, y, z = _read_server_position(data)
        return cls(spawn_id, x, y, z)


@dataclass
class OP_NewSpawn(EQStruct):
    spawn: Spawn

    def serialize(self) -> bytes:
        return self.spawn.serialize()

    @classmethod
    def deserialize(cls, data: bytes) -> OP_NewSpawn:
        return cls(Spawn.deserialize(data))


@dataclass
class OP_ZoneSpawns(EQStruct):
    spawns: list[Spawn] = field(default_factory=list)

    def serialize(self) -> bytes:
        return b"".join(spawn.serialize() for spawn in self.spawns)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ZoneSpawns:
        if len(data) < SPAWN_SIZE:
            return cls([])
        usable = data[: len(data) - len(data) % SPAWN_SIZE]
        spawns = [Spawn.deserialize(usable[offset : offset + SPAWN_SIZE]) for offset in range(0, len(usable), SPAWN_SIZE)]
        return cls(spawns)


@dataclass
class OP_DeleteSpawn(EQStruct):
    spawn_id: int

    def serialize(self) -> bytes:
        return _u32(self.spawn_id)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_DeleteSpawn:
        _need(data, 4, "OP_DeleteSpawn")
        return cls(_read_u32(data))


@dataclass
class OP_SpawnAppearance(EQStruct):
    spawn_id: int
    type: int
    parameter: int

    def serialize(self) -> bytes:
        return struct.pack("<HHI", self.spawn_id & 0xFFFF, self.type & 0xFFFF, self.parameter & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_SpawnAppearance:
        _need(data, 8, "OP_SpawnAppearance")
        spawn_id, kind, parameter = struct.unpack_from("<HHI", data)
        return cls(int(spawn_id), int(kind), int(parameter))


@dataclass
class OP_HPUpdate(EQStruct):
    cur_hp: int
    max_hp: int
    spawn_id: int

    def serialize(self) -> bytes:
        return struct.pack("<IiH", self.cur_hp & 0xFFFFFFFF, self.max_hp, self.spawn_id & 0xFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_HPUpdate:
        _need(data, 10, "OP_HPUpdate")
        cur_hp, max_hp, spawn_id = struct.unpack_from("<IiH", data)
        return cls(int(cur_hp), int(max_hp), int(spawn_id))


@dataclass
class OP_MobHealth(EQStruct):
    spawn_id: int
    percent: int

    def serialize(self) -> bytes:
        return struct.pack("<HB", self.spawn_id & 0xFFFF, self.percent & 0xFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_MobHealth:
        _need(data, 3, "OP_MobHealth")
        spawn_id, percent = struct.unpack_from("<HB", data)
        return cls(int(spawn_id), int(percent))


@dataclass
class OP_Damage(EQStruct):
    target: int
    source: int
    type: int
    spell_id: int
    amount: int
    force: float = 0.0
    hit_heading: float = 0.0
    hit_pitch: float = 0.0

    def serialize(self) -> bytes:
        return struct.pack(
            "<HHBHi3f",
            self.target & 0xFFFF,
            self.source & 0xFFFF,
            self.type & 0xFF,
            self.spell_id & 0xFFFF,
            self.amount,
            self.force,
            self.hit_heading,
            self.hit_pitch,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_Damage:
        _need(data, 11, "OP_Damage")
        target, source = struct.unpack_from("<HH", data)
        spell_id = struct.unpack_from("<H", data, 5)[0]
        amount = struct.unpack_from("<i", data, 7)[0]
        force = hit_heading = hit_pitch = 0.0
        if len(data) >= 23:
            force, hit_heading, hit_pitch = struct.unpack_from("<fff", data, 11)
        return cls(int(target), int(source), int(data[4]), int(spell_id), int(amount), float(force), float(hit_heading), float(hit_pitch))


@dataclass
class OP_Death(EQStruct):
    spawn_id: int
    killer_id: int = 0
    corpse_id: int = 0
    attack_skill: int = 0
    spell_id: int = 0
    bind_zone_id: int = 0
    damage: int = 0
    unknown: int = 0

    def serialize(self) -> bytes:
        return struct.pack(
            "<8I",
            self.spawn_id & 0xFFFFFFFF,
            self.killer_id & 0xFFFFFFFF,
            self.corpse_id & 0xFFFFFFFF,
            self.attack_skill & 0xFFFFFFFF,
            self.spell_id & 0xFFFFFFFF,
            self.bind_zone_id & 0xFFFFFFFF,
            self.damage & 0xFFFFFFFF,
            self.unknown & 0xFFFFFFFF,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_Death:
        _need(data, 4, "OP_Death")
        values = list(struct.unpack_from("<8I", data[:32].ljust(32, b"\x00")))
        return cls(*(int(value) for value in values))


@dataclass
class OP_BecomeCorpse(EQStruct):
    spawn_id: int
    x: float
    y: float
    z: float

    def serialize(self) -> bytes:
        return struct.pack("<Ifff", self.spawn_id & 0xFFFFFFFF, self.y, self.x, self.z)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_BecomeCorpse:
        _need(data, 16, "OP_BecomeCorpse")
        spawn_id, wire_y, wire_x, wire_z = struct.unpack_from("<Ifff", data)
        return cls(int(spawn_id), float(wire_x), float(wire_y), float(wire_z))


@dataclass
class OP_Assist(EQStruct):
    entity_id: int

    def serialize(self) -> bytes:
        return _u32(self.entity_id)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_Assist:
        if len(data) >= 4:
            return cls(_read_u32(data))
        if len(data) >= 2:
            return cls(struct.unpack_from("<H", data)[0])
        raise ValueError(f"OP_Assist is {len(data)} bytes")


@dataclass
class OP_Track(EQStruct):
    entries: list[tuple[int, float]] = field(default_factory=list)

    def serialize(self) -> bytes:
        return b"".join(struct.pack("<If", entity & 0xFFFFFFFF, distance) for entity, distance in self.entries)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_Track:
        entries: list[tuple[int, float]] = []
        offset = 0
        while offset + 8 <= len(data):
            entity, distance = struct.unpack_from("<If", data, offset)
            entries.append((int(entity), float(distance)))
            offset += 8
        return cls(entries)


@dataclass
class OP_TrackTarget(EQStruct):
    entity_id: int

    def serialize(self) -> bytes:
        return _u32(self.entity_id)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_TrackTarget:
        _need(data, 4, "OP_TrackTarget")
        return cls(_read_u32(data))


@dataclass
class OP_FindPersonRequest(EQStruct):
    entity_id: int
    x: float
    y: float
    z: float

    def serialize(self) -> bytes:
        return struct.pack("<Ifff", self.entity_id & 0xFFFFFFFF, self.y, self.x, self.z)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_FindPersonRequest:
        _need(data, 16, "OP_FindPersonRequest")
        entity, wire_y, wire_x, wire_z = struct.unpack_from("<Ifff", data)
        return cls(int(entity), float(wire_x), float(wire_y), float(wire_z))


@dataclass
class OP_FindPersonReply(EQStruct):
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    points: list[tuple[float, float, float]] = field(default_factory=list)

    def serialize(self) -> bytes:
        out = struct.pack("<fff", self.y, self.x, self.z)
        for point in self.points:
            out += struct.pack("<fff", point[1], point[0], point[2])
        return out

    @classmethod
    def deserialize(cls, data: bytes) -> OP_FindPersonReply:
        if len(data) < 12:
            return cls()
        dest_y, dest_x, dest_z = struct.unpack_from("<fff", data)
        points: list[tuple[float, float, float]] = []
        offset = 12
        while offset + 12 <= len(data):
            wire_y, wire_x, wire_z = struct.unpack_from("<fff", data, offset)
            points.append((float(wire_x), float(wire_y), float(wire_z)))
            offset += 12
        if len(points) >= 2 and _close(points[-1], points[-2]):
            points.pop()
        return cls(float(dest_x), float(dest_y), float(dest_z), points)


def _close(a: tuple[float, float, float], b: tuple[float, float, float]) -> bool:
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 <= 0.01


# --- doors, objects, combat verbs --------------------------------------------


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
        packet = bytearray(92)
        struct.pack_into("<I", packet, 12, self.drop_id & 0xFFFFFFFF)
        struct.pack_into("<ffff", packet, 28, self.heading, self.z, self.x, self.y)
        _put_fixed(packet, 44, self.name, 32)
        return bytes(packet)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_GroundSpawn:
        _need(data, 45, "OP_GroundSpawn")
        drop_id = _read_u32(data, 12)
        heading, z, x, y = struct.unpack_from("<ffff", data, 28)
        try:
            name, _end = _cstring(data, 44)
        except ValueError:
            name = _fixed(data, 44, 32)
        return cls(int(drop_id), name, float(x), float(y), float(z), float(heading))


@dataclass
class OP_ClickObject(EQStruct):
    drop_id: int
    player_id: int | None = None

    def serialize(self) -> bytes:
        if self.player_id is None:
            return _u32(self.drop_id)
        return struct.pack("<II", self.drop_id & 0xFFFFFFFF, self.player_id & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ClickObject:
        _need(data, 4, "OP_ClickObject")
        drop_id = _read_u32(data)
        if len(data) >= 8:
            return cls(drop_id, _read_u32(data, 4))
        return cls(drop_id, None)


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
        return struct.pack(
            "<IIIIiiBBBB",
            self.player_id & 0xFFFFFFFF,
            self.target_id & 0xFFFFFFFF,
            _faction_to_wire(self.faction) & 0xFFFFFFFF,
            self.level & 0xFFFFFFFF,
            self.cur_hp,
            self.max_hp,
            self.pvp & 0xFF,
            0,
            0,
            0,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_Consider:
        _need(data, 12, "OP_Consider")
        player_id, target_id, faction = struct.unpack_from("<III", data)
        level = _read_u32(data, 12) if len(data) >= 16 else 0
        cur_hp = max_hp = 0
        if len(data) >= 24:
            cur_hp, max_hp = struct.unpack_from("<ii", data, 16)
        pvp = data[24] if len(data) > 24 else 0
        return cls(int(player_id), int(target_id), _faction_from_wire(int(faction)), int(level), int(cur_hp), int(max_hp), int(pvp))


@dataclass
class OP_TargetMouse(EQStruct):
    spawn_id: int

    def serialize(self) -> bytes:
        return _u32(self.spawn_id)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_TargetMouse:
        _need(data, 4, "OP_TargetMouse")
        return cls(_read_u32(data))


@dataclass
class OP_AutoAttack(EQStruct):
    attacking: int

    def serialize(self) -> bytes:
        return _u32(self.attacking)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_AutoAttack:
        _need(data, 4, "OP_AutoAttack")
        return cls(_read_u32(data))


@dataclass
class OP_Taunt(EQStruct):
    spawn_id: int

    def serialize(self) -> bytes:
        return _u32(self.spawn_id)

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
        return struct.pack("<IIII4s", self.slot & 0xFFFFFFFF, self.spell_id & 0xFFFFFFFF, self.inventory_slot & 0xFFFFFFFF, self.target_id & 0xFFFFFFFF, b"\x00" * 4)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_CastSpell:
        _need(data, 16, "OP_CastSpell")
        slot, spell_id, inventory_slot, target_id = struct.unpack_from("<IIII", data)
        return cls(int(slot), int(spell_id), int(target_id), int(inventory_slot))


@dataclass
class OP_MemorizeSpell(EQStruct):
    slot: int
    spell_id: int
    scribing: int
    reduction: int = 0

    def serialize(self) -> bytes:
        return struct.pack("<IIII", self.slot & 0xFFFFFFFF, self.spell_id & 0xFFFFFFFF, self.scribing & 0xFFFFFFFF, self.reduction & 0xFFFFFFFF)

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
        return struct.pack("<II4sB3s", self.slot & 0xFFFFFFFF, self.auto & 0xFFFFFFFF, b"\x00" * 4, self.kind & 0xFF, b"\x00" * 3)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_Consume:
        _need(data, 13, "OP_Consume")
        slot, auto = struct.unpack_from("<II", data)
        return cls(int(slot), int(data[12]), int(auto))


@dataclass
class OP_Bind_Wound(EQStruct):
    target_id: int
    unknown2: int = 0
    type: int = 0
    unknown6: int = 0

    def serialize(self) -> bytes:
        return struct.pack("<HHHH", self.target_id & 0xFFFF, self.unknown2 & 0xFFFF, self.type & 0xFFFF, self.unknown6 & 0xFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_Bind_Wound:
        _need(data, 8, "OP_Bind_Wound")
        target_id, unknown2, kind, unknown6 = struct.unpack_from("<HHHH", data)
        return cls(int(target_id), int(unknown2), int(kind), int(unknown6))


# --- profile, inventory, loot ------------------------------------------------


@dataclass
class OP_PlayerProfile(EQStruct):
    name: str = ""
    gender: int = 0
    race: int = 0
    class_id: int = 0
    level: int = 0
    deity: int = 0
    home_zone_id: int = 0
    points: int = 0
    hp: int = 0
    mana: int = 0
    strength: int = 0
    stamina: int = 0
    charisma: int = 0
    dexterity: int = 0
    intelligence: int = 0
    agility: int = 0
    wisdom: int = 0
    platinum: int = 0
    gold: int = 0
    silver: int = 0
    copper: int = 0
    coin_known: bool = False
    skills: dict[int, int] | None = None
    spell_book: dict[int, int] = field(default_factory=dict)
    gems: dict[int, int] = field(default_factory=dict)

    def serialize(self) -> bytes:
        packet = bytearray(PROFILE_SIZE)
        struct.pack_into("<III", packet, 4, self.gender & 0xFFFFFFFF, self.race & 0xFFFFFFFF, self.class_id & 0xFFFFFFFF)
        packet[20] = self.level & 0xFF
        struct.pack_into("<I", packet, 24, self.home_zone_id & 0xFFFFFFFF)
        struct.pack_into("<I", packet, 124, self.deity & 0xFFFFFFFF)
        struct.pack_into("<III", packet, 2224, self.points & 0xFFFFFFFF, self.mana & 0xFFFFFFFF, self.hp & 0xFFFFFFFF)
        struct.pack_into(
            "<IIIIIII",
            packet,
            2236,
            self.strength & 0xFFFFFFFF,
            self.stamina & 0xFFFFFFFF,
            self.charisma & 0xFFFFFFFF,
            self.dexterity & 0xFFFFFFFF,
            self.intelligence & 0xFFFFFFFF,
            self.agility & 0xFFFFFFFF,
            self.wisdom & 0xFFFFFFFF,
        )
        book = [0] * 400
        for index, spell in self.spell_book.items():
            if 0 <= int(index) < 400:
                book[int(index)] = int(spell) & 0xFFFFFFFF
        struct.pack_into("<400I", packet, 2312, *book)
        gems = [0] * 12
        for index, spell in self.gems.items():
            if 0 <= int(index) < 12:
                gems[int(index)] = int(spell) & 0xFFFFFFFF
        struct.pack_into("<12I", packet, 4360, *gems)
        if self.coin_known:
            struct.pack_into("<IIII", packet, 4428, self.platinum & 0xFFFFFFFF, self.gold & 0xFFFFFFFF, self.silver & 0xFFFFFFFF, self.copper & 0xFFFFFFFF)
        skills = [0] * 100
        for index, value in (self.skills or {}).items():
            if 0 <= int(index) < 100:
                skills[int(index)] = int(value) & 0xFFFFFFFF
        struct.pack_into("<100I", packet, 4460, *skills)
        _put_fixed(packet, 12940, self.name, 64)
        return bytes(packet)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_PlayerProfile:
        _need(data, 2264, "OP_PlayerProfile")
        gender, race, class_id = struct.unpack_from("<III", data, 4)
        home_zone_id = _read_u32(data, 24)
        level = data[20]
        deity = _read_u32(data, 124)
        points, mana, hp = struct.unpack_from("<III", data, 2224)
        strength, stamina, charisma, dexterity, intelligence, agility, wisdom = struct.unpack_from("<IIIIIII", data, 2236)
        name = _fixed(data, 12940, 64) if len(data) >= 13004 else ""
        platinum = gold = silver = copper = 0
        coin_known = False
        if len(data) >= 4444:
            platinum, gold, silver, copper = struct.unpack_from("<IIII", data, 4428)
            coin_known = True
        skills: dict[int, int] | None = None
        if len(data) >= 4460 + 400:
            raw = struct.unpack_from("<100I", data, 4460)
            skills = {index: int(value) for index, value in enumerate(raw)}
        book: dict[int, int] = {}
        gems: dict[int, int] = {}
        if len(data) >= 2312 + 400 * 4:
            for index, spell in enumerate(struct.unpack_from("<400I", data, 2312)):
                if spell not in (0, 0xFFFFFFFF):
                    book[index] = int(spell)
        if len(data) >= 4360 + 12 * 4:
            for index, spell in enumerate(struct.unpack_from("<12I", data, 4360)):
                if spell not in (0, 0xFFFFFFFF):
                    gems[index] = int(spell)
        return cls(
            name,
            int(gender),
            int(race),
            int(class_id),
            int(level),
            int(deity),
            int(home_zone_id),
            int(points),
            int(hp),
            int(mana),
            int(strength),
            int(stamina),
            int(charisma),
            int(dexterity),
            int(intelligence),
            int(agility),
            int(wisdom),
            int(platinum),
            int(gold),
            int(silver),
            int(copper),
            coin_known,
            skills,
            book,
            gems,
        )


@dataclass
class OP_SkillUpdate(EQStruct):
    skill_id: int
    value: int

    def serialize(self) -> bytes:
        return struct.pack("<II", self.skill_id & 0xFFFFFFFF, self.value & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_SkillUpdate:
        _need(data, 8, "OP_SkillUpdate")
        skill_id, value = struct.unpack_from("<II", data)
        return cls(int(skill_id), int(value))


@dataclass
class OP_Stamina(EQStruct):
    food: int
    water: int

    def serialize(self) -> bytes:
        return struct.pack("<II", self.food & 0xFFFFFFFF, self.water & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_Stamina:
        _need(data, 8, "OP_Stamina")
        food, water = struct.unpack_from("<II", data)
        return cls(int(food), int(water))


@dataclass
class OP_MoneyUpdate(EQStruct):
    platinum: int
    gold: int
    silver: int
    copper: int

    def serialize(self) -> bytes:
        return struct.pack("<iiii", self.platinum, self.gold, self.silver, self.copper)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_MoneyUpdate:
        _need(data, 16, "OP_MoneyUpdate")
        platinum, gold, silver, copper = struct.unpack_from("<iiii", data)
        return cls(int(platinum), int(gold), int(silver), int(copper))


@dataclass
class OP_ManaChange(EQStruct):
    new_mana: int
    stamina: int = 0
    spell_id: int = 0
    keep_casting: int = 0

    def serialize(self) -> bytes:
        return struct.pack("<IIIB3s", self.new_mana & 0xFFFFFFFF, self.stamina & 0xFFFFFFFF, self.spell_id & 0xFFFFFFFF, self.keep_casting & 0xFF, b"\x00\x00\x00")

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ManaChange:
        _need(data, 4, "OP_ManaChange")
        new_mana = _read_u32(data)
        stamina = _read_u32(data, 4) if len(data) >= 8 else 0
        spell_id = _read_u32(data, 8) if len(data) >= 12 else 0
        keep = data[12] if len(data) > 12 else 0
        return cls(int(new_mana), int(stamina), int(spell_id), int(keep))


@dataclass
class OP_ExpUpdate(EQStruct):
    exp: int
    aa_exp: int = 0

    def serialize(self) -> bytes:
        return struct.pack("<II", self.exp & 0xFFFFFFFF, self.aa_exp & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ExpUpdate:
        _need(data, 4, "OP_ExpUpdate")
        exp = _read_u32(data)
        aa_exp = _read_u32(data, 4) if len(data) >= 8 else 0
        return cls(int(exp), int(aa_exp))


@dataclass
class OP_LevelUpdate(EQStruct):
    level: int
    level_old: int
    exp: int

    def serialize(self) -> bytes:
        return struct.pack("<III", self.level & 0xFFFFFFFF, self.level_old & 0xFFFFFFFF, self.exp & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_LevelUpdate:
        _need(data, 12, "OP_LevelUpdate")
        level, old, exp = struct.unpack_from("<III", data)
        return cls(int(level), int(old), int(exp))


@dataclass
class OP_Buff(EQStruct):
    entity_id: int
    buff: SpellBuff
    slot_id: int = 0
    fade: int = 0

    def serialize(self) -> bytes:
        return struct.pack(
            "<IBBBBIiIIII",
            self.entity_id & 0xFFFFFFFF,
            self.buff.effect_type & 0xFF,
            self.buff.level & 0xFF,
            self.buff.bard_modifier & 0xFF,
            self.buff.unknown & 0xFF,
            self.buff.spell_id & 0xFFFFFFFF,
            self.buff.duration,
            self.buff.counters & 0xFFFFFFFF,
            self.buff.caster_id & 0xFFFFFFFF,
            self.slot_id & 0xFFFFFFFF,
            self.fade & 0xFFFFFFFF,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_Buff:
        _need(data, 32, "OP_Buff")
        entity_id = _read_u32(data)
        effect, level, bard, unknown = struct.unpack_from("<BBBB", data, 4)
        spell_id = _read_u32(data, 8)
        duration = struct.unpack_from("<i", data, 12)[0]
        counters = _read_u32(data, 16)
        caster_id = _read_u32(data, 20)
        slot_id = _read_u32(data, 24)
        fade = _read_u32(data, 28)
        buff = SpellBuff(int(effect), int(level), int(bard), int(unknown), int(spell_id), int(duration), int(counters), int(caster_id))
        return cls(int(entity_id), buff, int(slot_id), int(fade))


@dataclass
class OP_CharInventory(EQStruct):
    items: list[Item] = field(default_factory=list)

    def serialize(self) -> bytes:
        return b"".join(item.text().encode("latin1", errors="replace") + b"\x00" for item in self.items)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_CharInventory:
        found: list[Item] = []
        for blob in data.split(b"\x00"):
            if b'"' not in blob:
                continue
            parsed = _parse_item(_u32(ITEM_INVENTORY) + blob)
            if parsed is not None:
                found.append(parsed)
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
        if self.to_slot is None and self.count is None:
            return _u32(self.from_slot)
        return struct.pack("<III", self.from_slot & 0xFFFFFFFF, (self.to_slot or 0) & 0xFFFFFFFF, (self.count or 0) & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_DeleteItem:
        _need(data, 4, "OP_DeleteItem")
        from_slot = _read_u32(data)
        if len(data) >= 12:
            to_slot, count = struct.unpack_from("<II", data, 4)
            return cls(int(from_slot), int(to_slot), int(count))
        return cls(int(from_slot))


@dataclass
class OP_MoveItem(EQStruct):
    from_slot: int
    to_slot: int
    count: int = 0

    def serialize(self) -> bytes:
        return struct.pack("<III", self.from_slot & 0xFFFFFFFF, self.to_slot & 0xFFFFFFFF, self.count & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_MoveItem:
        _need(data, 12, "OP_MoveItem")
        from_slot, to_slot, count = struct.unpack_from("<III", data)
        return cls(int(from_slot), int(to_slot), int(count))


@dataclass
class OP_LootRequest(EQStruct):
    spawn_id: int

    def serialize(self) -> bytes:
        return _u32(self.spawn_id)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_LootRequest:
        _need(data, 4, "OP_LootRequest")
        return cls(_read_u32(data))


@dataclass
class OP_EndLootRequest(EQStruct):
    spawn_id: int

    def serialize(self) -> bytes:
        return _u32(self.spawn_id)

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
        return struct.pack("<IIH2sI", self.corpse_id & 0xFFFFFFFF, self.player_id & 0xFFFFFFFF, self.slot & 0xFFFF, b"\x00\x00", self.auto_loot)

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
        return struct.pack("<4sIIII", bytes((self.response & 0xFF, 0, 0, 0)), self.platinum & 0xFFFFFFFF, self.gold & 0xFFFFFFFF, self.silver & 0xFFFFFFFF, self.copper & 0xFFFFFFFF)

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


# --- merchant, trade, group, tasks -------------------------------------------


@dataclass
class OP_ShopRequest(EQStruct):
    npc_id: int
    player_id: int
    command: int
    rate: float = 0.0

    def serialize(self) -> bytes:
        if self.rate:
            return struct.pack("<IIIf", self.npc_id & 0xFFFFFFFF, self.player_id & 0xFFFFFFFF, self.command & 0xFFFFFFFF, self.rate)
        return struct.pack("<III", self.npc_id & 0xFFFFFFFF, self.player_id & 0xFFFFFFFF, self.command & 0xFFFFFFFF)

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
        return struct.pack(
            "<IIIIII",
            self.npc_id & 0xFFFFFFFF,
            self.player_id & 0xFFFFFFFF,
            self.slot & 0xFFFFFFFF,
            self.unknown & 0xFFFFFFFF,
            self.quantity & 0xFFFFFFFF,
            self.price & 0xFFFFFFFF,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ShopPlayerBuy:
        _need(data, 24, "OP_ShopPlayerBuy")
        npc_id, player_id, slot, unknown, quantity, price = struct.unpack_from("<IIIIII", data)
        return cls(int(npc_id), int(player_id), int(slot), int(unknown), int(quantity), int(price))


@dataclass
class OP_ShopPlayerSell(EQStruct):
    npc_id: int
    slot: int
    quantity: int
    price: int = 0

    def serialize(self) -> bytes:
        return struct.pack("<IIII", self.npc_id & 0xFFFFFFFF, self.slot & 0xFFFFFFFF, self.quantity & 0xFFFFFFFF, self.price & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ShopPlayerSell:
        _need(data, 16, "OP_ShopPlayerSell")
        npc_id, slot, quantity, price = struct.unpack_from("<IIII", data)
        return cls(int(npc_id), int(slot), int(quantity), int(price))


@dataclass
class OP_ShopDelItem(EQStruct):
    npc_id: int
    player_id: int
    slot: int

    def serialize(self) -> bytes:
        return struct.pack("<III", self.npc_id & 0xFFFFFFFF, self.player_id & 0xFFFFFFFF, self.slot & 0xFFFFFFFF)

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
        return struct.pack("<hh", self.container_slot, self.guildtribute_slot)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_TradeSkillCombine:
        _need(data, 4, "OP_TradeSkillCombine")
        container_slot, guildtribute_slot = struct.unpack_from("<hh", data)
        return cls(int(container_slot), int(guildtribute_slot))


@dataclass
class OP_GroupInvite(EQStruct):
    invitee: str
    inviter: str = ""

    def serialize(self) -> bytes:
        return _pack_names(self.invitee, self.inviter)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_GroupInvite:
        invitee, inviter = _two_names(data)
        return cls(invitee, inviter)


@dataclass
class OP_GroupInvite2(EQStruct):
    invitee: str
    inviter: str = ""

    def serialize(self) -> bytes:
        return _pack_names(self.invitee, self.inviter)

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
class OP_RaidUpdate(EQStruct):
    action: int = 0
    your_name: str = ""
    leader: str = ""

    def serialize(self) -> bytes:
        return _pack_group(self.action, self.your_name, [], self.leader, False)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_RaidUpdate:
        action, your_name, _members, leader, _full = _read_group(data, full_opcode=False)
        return cls(action, your_name, leader)


@dataclass
class OP_RaidJoin(EQStruct):
    action: int = 0
    your_name: str = ""
    leader: str = ""

    def serialize(self) -> bytes:
        return _pack_group(self.action, self.your_name, [], self.leader, False)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_RaidJoin:
        action, your_name, _members, leader, _full = _read_group(data, full_opcode=False)
        return cls(action, your_name, leader)


def _pack_group(action: int, your_name: str, members: list[str], leader: str, full: bool) -> bytes:
    if full:
        packet = bytearray(452)
        struct.pack_into("<I", packet, 0, action & 0xFFFFFFFF)
        _put_fixed(packet, 4, your_name, 64)
        for index in range(5):
            name = members[index] if index < len(members) else ""
            _put_fixed(packet, 68 + index * 64, name, 64)
        _put_fixed(packet, 388, leader, 64)
        return bytes(packet)
    packet = bytearray(132)
    struct.pack_into("<I", packet, 0, action & 0xFFFFFFFF)
    _put_fixed(packet, 4, your_name, 64)
    _put_fixed(packet, 68, leader, 64)
    return bytes(packet)


def _read_group(data: bytes, full_opcode: bool) -> tuple[int, str, list[str], str, bool]:
    if len(data) < 4:
        return 0, "", [], "", False
    action = _read_u32(data)
    if full_opcode and len(data) >= 452:
        your_name = _fixed(data, 4, 64)
        members = [_fixed(data, 68 + index * 64, 64) for index in range(5)]
        leader = _fixed(data, 388, 64)
        return int(action), your_name, members, leader, True
    if len(data) >= 132:
        return int(action), _fixed(data, 4, 64), [], _fixed(data, 68, 64), False
    return int(action), "", [], "", False


@dataclass
class OP_GMTraining(EQStruct):
    npc_id: int
    player_id: int
    skills: tuple[int, ...] = ()

    def serialize(self) -> bytes:
        packet = bytearray(GM_TRAINING_SIZE)
        struct.pack_into("<II", packet, 0, self.npc_id & 0xFFFFFFFF, self.player_id & 0xFFFFFFFF)
        values = list(self.skills[:GM_SKILL_COUNT])
        values.extend([0] * (GM_SKILL_COUNT - len(values)))
        struct.pack_into("<100I", packet, 8, *(value & 0xFFFFFFFF for value in values))
        return bytes(packet)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_GMTraining:
        _need(data, 8, "OP_GMTraining")
        npc_id, player_id = struct.unpack_from("<II", data)
        skills: tuple[int, ...] = ()
        if len(data) >= 8 + GM_SKILL_COUNT * 4:
            skills = tuple(int(value) for value in struct.unpack_from("<100I", data, 8))
        return cls(int(npc_id), int(player_id), skills)


@dataclass
class OP_GMTrainSkill(EQStruct):
    npc_id: int
    skill_id: int
    skill_bank: int = 0

    def serialize(self) -> bytes:
        return struct.pack("<H2sH2sH2s", self.npc_id & 0xFFFF, b"\x00\x00", self.skill_bank & 0xFFFF, b"\x00\x00", self.skill_id & 0xFFFF, b"\x00\x00")

    @classmethod
    def deserialize(cls, data: bytes) -> OP_GMTrainSkill:
        _need(data, 12, "OP_GMTrainSkill")
        npc_id, _pad1, skill_bank, _pad2, skill_id, _pad3 = struct.unpack_from("<H2sH2sH2s", data)
        return cls(int(npc_id), int(skill_id), int(skill_bank))


@dataclass
class OP_GMEndTraining(EQStruct):
    npc_id: int
    player_id: int

    def serialize(self) -> bytes:
        return struct.pack("<II", self.npc_id & 0xFFFFFFFF, self.player_id & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_GMEndTraining:
        _need(data, 8, "OP_GMEndTraining")
        npc_id, player_id = struct.unpack_from("<II", data)
        return cls(int(npc_id), int(player_id))


@dataclass
class OP_ReadBook(EQStruct):
    spell_id: int = 0
    window: int = 0
    book_type: int = 0
    text_file: str = ""

    def serialize(self) -> bytes:
        if self.text_file:
            return bytes((self.window & 0xFF, self.book_type & 0xFF)) + _put_cstr(self.text_file)
        return _u32(self.spell_id)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ReadBook:
        if len(data) == 4:
            return cls(_read_u32(data))
        if len(data) >= 3:
            try:
                text_file, _end = _cstring(data, 2)
            except ValueError:
                text_file = ""
            return cls(0, int(data[0]), int(data[1]), text_file)
        raise ValueError(f"OP_ReadBook is {len(data)} bytes")


@dataclass
class OP_AcceptNewTask(EQStruct):
    task_id: int
    task_master_id: int

    def serialize(self) -> bytes:
        return struct.pack("<II", self.task_id & 0xFFFFFFFF, self.task_master_id & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_AcceptNewTask:
        _need(data, 8, "OP_AcceptNewTask")
        task_id, master = struct.unpack_from("<II", data)
        return cls(int(task_id), int(master))


@dataclass
class OP_TaskSelectWindow(EQStruct):
    task_type: int = 0
    giver: int = 0
    tasks: list[TaskChoice] = field(default_factory=list)

    def serialize(self) -> bytes:
        out = bytearray()
        out += struct.pack("<III", len(self.tasks), self.task_type & 0xFFFFFFFF, self.giver & 0xFFFFFFFF)
        for task in self.tasks:
            out += struct.pack("<III", task.task_id & 0xFFFFFFFF, task.duration & 0xFFFFFFFF, task.duration_code & 0xFFFFFFFF)
            out += _put_cstr(task.title)
            out += _put_cstr(task.description)
            out += _u32(len(task.elements))
            for element in task.elements:
                out += struct.pack(
                    "<iii",
                    element.activity_id,
                    element.kind,
                    element.request,
                )
                out += _put_cstr(element.target)
                out += _put_cstr(element.item_list)
                out += struct.pack("<iiii", element.goal, element.skill, element.spell, element.zone_id)
                out += _put_cstr(element.description)
        return bytes(out)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_TaskSelectWindow:
        _need(data, 12, "OP_TaskSelectWindow")
        count, task_type, giver = struct.unpack_from("<III", data)
        offset = 12
        tasks: list[TaskChoice] = []
        for _index in range(int(count)):
            task_id, duration, duration_code = struct.unpack_from("<III", data, offset)
            offset += 12
            title, offset = _cstring(data, offset)
            description, offset = _cstring(data, offset)
            elements_n = _read_u32(data, offset)
            offset += 4
            elements: list[TaskElement] = []
            for _element in range(int(elements_n)):
                activity_id, kind, request = struct.unpack_from("<iii", data, offset)
                offset += 12
                target, offset = _cstring(data, offset)
                item_list, offset = _cstring(data, offset)
                goal, skill, spell, zone_id = struct.unpack_from("<iiii", data, offset)
                offset += 16
                element_description, offset = _cstring(data, offset)
                elements.append(
                    TaskElement(
                        int(activity_id),
                        int(kind),
                        int(request),
                        target,
                        item_list,
                        int(goal),
                        int(skill),
                        int(spell),
                        int(zone_id),
                        element_description,
                    )
                )
            tasks.append(TaskChoice(int(task_id), int(duration), int(duration_code), title, description, elements))
        return cls(int(task_type), int(giver), tasks)


@dataclass
class OP_TaskActivity(EQStruct):
    task_id: int = 0
    activity_id: int = 0
    locked: bool = False
    client_index: int = 0
    task_type: int = 0
    list_group: int = 0
    kind: int = 0
    optional: int = 0
    request: int = 0
    target: str = ""
    item_list: str = ""
    goal: int = 0
    skill: int = 0
    spell: int = 0
    zone_id: int = 0
    dynamic_zone: int = 0
    description: str = ""
    done: int = 0

    def serialize(self) -> bytes:
        if self.locked:
            packet = bytearray(25)
            struct.pack_into("<II", packet, 8, self.task_id & 0xFFFFFFFF, self.activity_id & 0xFFFFFFFF)
            return bytes(packet)
        out = struct.pack(
            "<IIIII",
            self.client_index & 0xFFFFFFFF,
            self.task_type & 0xFFFFFFFF,
            self.task_id & 0xFFFFFFFF,
            self.activity_id & 0xFFFFFFFF,
            self.list_group & 0xFFFFFFFF,
        )
        out += struct.pack("<iii", self.kind, self.optional, self.request)
        out += _put_cstr(self.target)
        out += _put_cstr(self.item_list)
        out += struct.pack("<iiiii", self.goal, self.skill, self.spell, self.zone_id, self.dynamic_zone)
        out += _put_cstr(self.description)
        out += struct.pack("<i", self.done)
        return out

    @classmethod
    def deserialize(cls, data: bytes) -> OP_TaskActivity:
        if len(data) < 25:
            raise ValueError(f"OP_TaskActivity is {len(data)} bytes")
        if len(data) == 25:
            task_id, activity_id = struct.unpack_from("<II", data, 8)
            return cls(int(task_id), int(activity_id), True)
        offset = 0
        client_index, task_type, task_id, activity_id, list_group = struct.unpack_from("<IIIII", data, offset)
        offset += 20
        kind, optional, request = struct.unpack_from("<iii", data, offset)
        offset += 12
        target, offset = _cstring(data, offset)
        item_list, offset = _cstring(data, offset)
        goal, skill, spell, zone_id, dynamic_zone = struct.unpack_from("<iiiii", data, offset)
        offset += 20
        description, offset = _cstring(data, offset)
        done = struct.unpack_from("<i", data, offset)[0]
        return cls(
            int(task_id),
            int(activity_id),
            False,
            int(client_index),
            int(task_type),
            int(list_group),
            int(kind),
            int(optional),
            int(request),
            target,
            item_list,
            int(goal),
            int(skill),
            int(spell),
            int(zone_id),
            int(dynamic_zone),
            description,
            int(done),
        )


@dataclass
class OP_TaskActivityComplete(EQStruct):
    index: int
    task_type: int
    task_id: int
    activity_id: int
    task_completed: int
    stage_complete: int

    def serialize(self) -> bytes:
        return struct.pack(
            "<IIIIII",
            self.index & 0xFFFFFFFF,
            self.task_type & 0xFFFFFFFF,
            self.task_id & 0xFFFFFFFF,
            self.activity_id & 0xFFFFFFFF,
            self.task_completed & 0xFFFFFFFF,
            self.stage_complete & 0xFFFFFFFF,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_TaskActivityComplete:
        _need(data, 24, "OP_TaskActivityComplete")
        index, task_type, task_id, activity_id, task_completed, stage_complete = struct.unpack_from("<IIIIII", data)
        return cls(int(index), int(task_type), int(task_id), int(activity_id), int(task_completed), int(stage_complete))


# --- chat, popups, rez -------------------------------------------------------


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
        packet = bytearray(CHANNEL_MESSAGE_SIZE)
        _put_fixed(packet, 0, self.target, 64)
        _put_fixed(packet, 64, self.sender, 64)
        struct.pack_into(
            "<IIIII",
            packet,
            128,
            self.language & 0xFF,
            self.channel & 0xFFFFFFFF,
            self.unused1 & 0xFFFFFFFF,
            self.unused2 & 0xFFFFFFFF,
            max(0, min(100, int(self.skill))),
        )
        return bytes(packet) + _put_cstr(self.text)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ChannelMessage:
        _need(data, CHANNEL_MESSAGE_SIZE, "OP_ChannelMessage")
        language, channel, unused1, unused2, skill = struct.unpack_from("<IIIII", data, 128)
        text = ""
        if len(data) > CHANNEL_MESSAGE_SIZE:
            text = data[CHANNEL_MESSAGE_SIZE:].split(b"\x00", 1)[0].decode("latin1", errors="replace")
        return cls(_fixed(data, 0, 64), _fixed(data, 64, 64), int(language), int(channel), int(unused1), int(unused2), int(skill), text)


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
        return head + struct.pack("<II", self.msg_type & 0xFFFFFFFF, self.target_spawn_id & 0xFFFFFFFF) + _put_cstr(self.speaker) + gap + _put_cstr(self.message)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_SpecialMesg:
        if len(data) < 11:
            return cls()
        header = data[:3]
        msg_type, target = struct.unpack_from("<II", data, 3)
        try:
            speaker, offset = _cstring(data, 11)
        except ValueError:
            return cls(header, int(msg_type), int(target))
        unknown = data[offset : offset + 12]
        offset += 12
        message = ""
        if offset < len(data):
            try:
                message, _end = _cstring(data, offset)
            except ValueError:
                message = ""
        return cls(header, int(msg_type), int(target), speaker, unknown, message)


@dataclass
class OP_SimpleMessage(EQStruct):
    string_id: int
    color: int = 0
    unknown: int = 0
    texts: tuple[str, ...] = ()

    def serialize(self) -> bytes:
        out = struct.pack("<III", self.string_id & 0xFFFFFFFF, self.color & 0xFFFFFFFF, self.unknown & 0xFFFFFFFF)
        for text in self.texts:
            out += _put_cstr(text)
        return out

    @classmethod
    def deserialize(cls, data: bytes) -> OP_SimpleMessage:
        _need(data, 4, "OP_SimpleMessage")
        string_id = _read_u32(data)
        color = _read_u32(data, 4) if len(data) >= 8 else 0
        unknown = _read_u32(data, 8) if len(data) >= 12 else 0
        texts: list[str] = []
        offset = 12
        while offset < len(data):
            try:
                text, offset = _cstring(data, offset)
            except ValueError:
                break
            if not text:
                break
            texts.append(text)
        return cls(int(string_id), int(color), int(unknown), tuple(texts))


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
        packet = bytearray(4244)
        _put_fixed(packet, 0, self.title, 128)
        _put_fixed(packet, 128, self.text, 4096)
        struct.pack_into(
            "<IIIII",
            packet,
            4224,
            self.buttons & 0xFFFFFFFF,
            self.duration & 0xFFFFFFFF,
            self.popup_id & 0xFFFFFFFF,
            self.unknown4236 & 0xFFFFFFFF,
            self.unknown4240 & 0xFFFFFFFF,
        )
        return bytes(packet)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_OnLevelMessage:
        if len(data) < 128:
            return cls()
        title = _fixed(data, 0, 128)
        text = _fixed(data, 128, 4096) if len(data) > 128 else ""
        buttons = duration = popup_id = unknown4236 = unknown4240 = 0
        if len(data) >= 4244:
            buttons, duration, popup_id, unknown4236, unknown4240 = struct.unpack_from("<IIIII", data, 4224)
        elif len(data) >= 4236:
            popup_id = _read_u32(data, 4232)
        return cls(title, text, int(buttons), int(duration), int(popup_id), int(unknown4236), int(unknown4240))


@dataclass
class OP_PopupResponse(EQStruct):
    popup_id: int
    unknown: int = 0

    def serialize(self) -> bytes:
        return struct.pack("<II", self.unknown & 0xFFFFFFFF, self.popup_id & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_PopupResponse:
        _need(data, 8, "OP_PopupResponse")
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
    packet = bytearray(228)
    struct.pack_into("<IHH", packet, 0, row.unknown00 & 0xFFFFFFFF, row.zone_id & 0xFFFF, row.instance_id & 0xFFFF)
    struct.pack_into("<fff", packet, 8, row.y, row.x, row.z)
    _put_fixed(packet, 20, row.your_name, 64)
    struct.pack_into("<I", packet, 84, row.unknown88 & 0xFFFFFFFF)
    _put_fixed(packet, 88, row.rezzer_name, 64)
    struct.pack_into("<I", packet, 152, row.spell_id & 0xFFFFFFFF)
    _put_fixed(packet, 156, row.corpse_name, 64)
    struct.pack_into("<I", packet, 220, row.action & 0xFFFFFFFF)
    return bytes(packet)


def _read_resurrect(cls: type[_S], data: bytes) -> _S:
    if len(data) < 8:
        return cls()
    unknown00 = _read_u32(data)
    zone_id, instance_id = struct.unpack_from("<HH", data, 4)
    x = y = z = 0.0
    if len(data) >= 20:
        wire_y, wire_x, wire_z = struct.unpack_from("<fff", data, 8)
        x, y, z = float(wire_x), float(wire_y), float(wire_z)
    your_name = _fixed(data, 20, 64) if len(data) >= 84 else ""
    unknown88 = _read_u32(data, 84) if len(data) >= 88 else 0
    rezzer = _fixed(data, 88, 64) if len(data) >= 152 else ""
    spell_id = _read_u32(data, 152) if len(data) >= 156 else 0
    corpse = _fixed(data, 156, 64) if len(data) >= 220 else ""
    action = _read_u32(data, 220) if len(data) >= 224 else 0
    return cls(int(zone_id), int(instance_id), x, y, z, your_name, int(unknown88), rezzer, int(spell_id), corpse, int(action), int(unknown00))


# --- empty bodies ------------------------------------------------------------


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
    """Titanium leaves this opcode at zero. The body is empty."""


@dataclass
class OP_ZoneComplete(EQStruct):
    """Sent when the opcode table has it. The body is empty."""


@dataclass
class OP_Forage(EQStruct):
    """Forage. The body is empty."""


@dataclass
class OP_Fishing(EQStruct):
    """Fishing. The body is empty."""


@dataclass
class OP_TradeAcceptClick(EQStruct):
    """Accepts an open trade. The body is empty."""


@dataclass
class OP_FinishTrade(EQStruct):
    """The server closed the trade. The body is ignored."""


@dataclass
class OP_ReliableHole(EQStruct):
    """Synthetic opcode for a reliable-stream hole. There is no wire body."""
