"""One typed object per opcode eqclient4 sends or reads.

Application objects serialize and deserialize the RoF2 opcode body
(little-endian). Session objects serialize and deserialize the whole datagram
(big-endian), including the leading zero and the session opcode byte.

Inventory slots on these objects stay the client numbers (cursor 30, ammo 21,
general 22-29). Serialize and deserialize translate those to the RoF2 slot
struct, whose cursor is 33.

Coordinates on these objects are x, y, z. Serialize and deserialize convert
the y, x, z order used on the wire.
"""

import re
import struct
from dataclasses import dataclass, field
from typing import ClassVar, TypeAlias, TypeVar

OPERATIONS: dict[str, type[EQStruct]] = {}

_S = TypeVar("_S", bound="EQStruct")


class EQStruct:
    """Wire object. Opcode classes register under their name. Nested records do not."""

    opcode: ClassVar[str] = ""

    def __init_subclass__(cls, **kwargs: object) -> None:
        super().__init_subclass__(**kwargs)
        cls.__module__ = "eqclient4.structs"
        if cls.__name__.startswith("OP_"):
            cls.opcode = cls.__name__
            OPERATIONS[cls.__name__] = cls

    def serialize(self) -> bytes:
        return b""

    @classmethod
    def deserialize(cls: type[_S], data: bytes) -> _S:
        return cls()


def need(data: bytes, size: int, what: str) -> None:
    if len(data) < size:
        raise ValueError(f"{what} is {len(data)} bytes")


def exact(data: bytes, size: int, what: str) -> None:
    if len(data) != size:
        raise ValueError(f"{what} is {len(data)} bytes")


def u32(value: int) -> bytes:
    # common/serialize_buffer.h:100 WriteUInt32
    return struct.pack("<I", value & 0xFFFFFFFF)


def read_u32(data: bytes, offset: int = 0) -> int:
    return struct.unpack_from("<I", data, offset)[0]


def fixed(data: bytes, offset: int, size: int) -> str:
    if offset >= len(data):
        return ""
    chunk = data[offset : min(len(data), offset + size)]
    return chunk.split(b"\x00", 1)[0].decode("latin1", errors="replace")


def put_fixed(buf: bytearray, offset: int, text: str, size: int) -> None:
    raw = (text or "").encode("latin1", errors="replace")[: size - 1]
    buf[offset : offset + len(raw)] = raw


def cstring(data: bytes, offset: int) -> tuple[str, int]:
    end = data.find(b"\x00", offset)
    if end < 0:
        raise ValueError("unterminated string")
    return data[offset:end].decode("latin1", errors="replace"), end + 1


def put_cstr(text: str) -> bytes:
    return (text or "").encode("latin1", errors="replace") + b"\x00"


def put_lenstr(text: str) -> bytes:
    """common/serialize_buffer.h:194 WriteLengthString. Length does not include a NUL."""
    raw = (text or "").encode("latin1", errors="replace")
    # common/serialize_buffer.h:188 length, then the bytes
    return struct.pack("<I", len(raw)) + raw


def lenstr(data: bytes, offset: int) -> tuple[str, int]:
    if offset + 4 > len(data):
        raise ValueError("truncated length string")
    length = read_u32(data, offset)
    start = offset + 4
    end = start + length
    if end > len(data):
        raise ValueError("truncated length string")
    return data[start:end].decode("latin1", errors="replace"), end


def sign_extend(value: int, bits: int) -> int:
    value &= (1 << bits) - 1
    sign = 1 << (bits - 1)
    return value - (1 << bits) if value & sign else value


def pack_eq19(value: float) -> int:
    return int(round(value * 8.0)) & 0x7FFFF


def i8(value: int) -> int:
    """A uint8 bit pattern as a signed byte. 0xFF is -1."""
    value = int(value) & 0xFF
    if value >= 0x80:
        return value - 0x100
    return value


def i16(value: int) -> int:
    """A uint16 bit pattern as a signed slot. 0xFFFF is -1."""
    value = int(value) & 0xFFFF
    if value >= 0x8000:
        return value - 0x10000
    return value


def i32(value: int) -> int:
    """A uint32 bit pattern as a signed int. 0xFFFFFFFF is -1."""
    value = int(value) & 0xFFFFFFFF
    if value >= 0x80000000:
        return value - 0x100000000
    return value


def read_i32(data: bytes, offset: int = 0) -> int:
    return struct.unpack_from("<i", data, offset)[0]


# Bag contents use the same addresses as inventory.assign: general parent 22-29,
# ten subslots, stride 200, first bag slot 251.
_BAGS_BEGIN = 251
_GENERAL_LO = 22
_GENERAL_HI = 30
_BAG_STRIDE = 200
_SUBSLOTS = 10


# Lossless inventory-location records. Keep all six original signed words.
@dataclass(frozen=True)
class InventorySlot:
    type: int
    unknown02: int = field(compare=False)
    main_slot: int
    sub_index: int
    aug_index: int
    unknown10: int = field(compare=False)

    @classmethod
    def unpack(cls, data: bytes, offset: int = 0) -> InventorySlot:
        need(data, offset + 12, "InventorySlot")
        return cls(*struct.unpack_from("<6h", data, offset))

    @classmethod
    def for_client(cls, kind: int, slot: int) -> InventorySlot:
        # Possessions use translated client indices, including bag subslots.
        if kind == 0:
            main, sub = inventory_wire(slot)
        else:
            main, sub = slot, -1
        return cls(
            i16(kind),
            0,
            i16(main),
            i16(sub),
            -1,
            0,
        )

    @property
    def client_slot(self) -> int:
        return client_slot(self.type, self.main_slot, self.sub_index)

    def pack(self) -> bytes:
        return struct.pack(
            "<6h",
            self.type,
            self.unknown02,
            self.main_slot,
            self.sub_index,
            self.aug_index,
            self.unknown10,
        )

    def preserve_inventory_slot(self, kind: int, slot: int) -> InventorySlot:
        if self.type == kind and self.client_slot == slot:
            return self
        return InventorySlot.for_client(kind, slot)


@dataclass(frozen=True)
class TypelessInventorySlot:
    main_slot: int
    sub_index: int = -1
    aug_index: int = -1
    unknown06: int = 0

    @classmethod
    def unpack(cls, data: bytes, offset: int = 0) -> TypelessInventorySlot:
        need(data, offset + 8, "TypelessInventorySlot")
        return cls(*struct.unpack_from("<4h", data, offset))

    @classmethod
    def for_client(cls, slot: int) -> TypelessInventorySlot:
        main, sub = inventory_wire(slot)
        return cls(i16(main), i16(sub), -1, 0)

    @property
    def client_slot(self) -> int:
        return client_slot(
            0,
            self.main_slot,
            self.sub_index,
        )

    def pack(self) -> bytes:
        return struct.pack(
            "<4h",
            self.main_slot,
            self.sub_index,
            self.aug_index,
            self.unknown06,
        )

    def preserve_typeless_slot(self, slot: int) -> TypelessInventorySlot:
        if self.client_slot == slot:
            return self
        return TypelessInventorySlot.for_client(slot)


def inventory_wire(slot: int) -> tuple[int, int]:
    """RoF2 (main slot, sub index) for a client slot. A bag address carries its sub index."""
    if slot >= _BAGS_BEGIN:
        parent_index = (slot - _BAGS_BEGIN) // _BAG_STRIDE
        sub = (slot - _BAGS_BEGIN) % _BAG_STRIDE
        parent = _GENERAL_LO + parent_index
        if 0 <= sub < _SUBSLOTS and _GENERAL_LO <= parent < _GENERAL_HI:
            return (to_rof2_slot(parent), sub)
    return (to_rof2_slot(slot), -1)


def client_slot(slot_type: int, main_slot: int, sub_slot: int) -> int:
    """Client slot for a RoF2 inventory address. A sub index lands inside that bag."""
    if slot_type == 0 and 0 <= sub_slot < _SUBSLOTS:
        parent = from_rof2_slot(main_slot)
        if _GENERAL_LO <= parent < _GENERAL_HI:
            return _BAGS_BEGIN + (parent - _GENERAL_LO) * _BAG_STRIDE + sub_slot
    if slot_type == 0:
        return from_rof2_slot(main_slot)
    return main_slot


def to_rof2_slot(slot: int) -> int:
    """Client possession slot to the RoF2 slot number. Cursor 30 is 33."""
    slot = i16(slot)
    if slot < 0:
        return -1
    if slot <= 20:
        return slot
    if slot == 21:
        return 22
    if 22 <= slot <= 29:
        return slot + 1
    if slot == 30:
        return 33
    return slot


def from_rof2_slot(slot: int) -> int:
    slot = i16(slot)
    if slot < 0:
        return -1
    if slot <= 20:
        return slot
    if slot == 22:
        return 21
    if 23 <= slot <= 30:
        return slot - 1
    if slot == 33:
        return 30
    return slot


def pack_typed_slot(kind: int, slot: int) -> bytes:
    """A window slot. Trade is type 3, and slot 0 is the first hand-in cell."""
    # common/patches/rof2_structs.h:57 InventorySlot_Struct
    return struct.pack("<hhhhhh", i16(kind), 0, i16(slot), -1, -1, 0)


def pack_inventory_slot(slot: int) -> bytes:
    """Type 0. A general slot has an invalid sub index. A bag slot names the parent and the sub index."""
    # common/patches/rof2_structs.h:57 InventorySlot_Struct
    wire, sub = inventory_wire(slot)
    return struct.pack("<hhhhhh", 0, 0, i16(wire), i16(sub), -1, 0)


def unpack_inventory_slot(data: bytes, offset: int) -> int:
    kind, _unknown, wire, sub, _aug, _tail = struct.unpack_from("<hhhhhh", data, offset)
    return client_slot(int(kind), int(wire), int(sub))


def bitword(*parts: tuple[int, int]) -> int:
    word = 0
    shift = 0
    for value, bits in parts:
        word |= (int(value) & ((1 << bits) - 1)) << shift
        shift += bits
    return word & 0xFFFFFFFF


def bitfield(word: int, shift: int, bits: int, signed: bool = True) -> int:
    value = (word >> shift) & ((1 << bits) - 1)
    if signed:
        return sign_extend(value, bits)
    return value


def advance(data: bytes, offset: int, size: int, what: str) -> int:
    if offset + size > len(data):
        raise ValueError(f"{what} is {len(data)} bytes")
    return offset + size


def pack_names(first: str, second: str, size: int = 128) -> bytes:
    packet = bytearray(size)
    put_fixed(packet, 0, first, 64)
    put_fixed(packet, 64, second, 64)
    return bytes(packet)


def two_names(data: bytes) -> tuple[str, str]:
    first = fixed(data, 0, 64) if len(data) >= 64 else ""
    second = fixed(data, 64, 64) if len(data) >= 128 else ""
    return first, second


@dataclass
class ItemLink:
    item_id: int
    name: str
    action: int = 0
    augments: tuple[int, ...] = (0, 0, 0, 0, 0, 0)
    is_evolving: int = 0
    evolve_group: int = 0
    evolve_level: int = 0
    ornament_icon: int = 0
    hash: int = 0

    @classmethod
    def deserialize(cls, text: str) -> "ItemLink":
        if not (text.startswith("\x12") and text.endswith("\x12")):
            raise ValueError("Invalid item link delimiters")

        body = text[1:-1]
        if len(body) < 56:
            raise ValueError("Item link header too short")

        header = body[:56]

        def field(start: int, end: int) -> int:
            return int(header[start:end], 16)

        return cls(
            item_id=field(1, 6),
            name=body[56:],
            action=field(0, 1),
            augments=tuple(field(6 + i * 5, 11 + i * 5) for i in range(6)),
            is_evolving=field(36, 37),
            evolve_group=field(37, 41),
            evolve_level=field(41, 43),
            ornament_icon=field(43, 48),
            hash=field(48, 56),
        )

    def serialize(self) -> str:
        if len(self.augments) != 6:
            raise ValueError("Item links require six augment slots")

        values = [
            (self.action, 1),
            (self.item_id, 5),
            *((augment, 5) for augment in self.augments),
            (self.is_evolving, 1),
            (self.evolve_group, 4),
            (self.evolve_level, 2),
            (self.ornament_icon, 5),
            (self.hash, 8),
        ]

        for value, width in values:
            if not 0 <= value < (1 << (4 * width)):
                raise ValueError(f"Item link field {value} exceeds {width} hex digits")

        header = "".join(f"{value:0{width}X}" for value, width in values)
        return f"\x12{header}{self.name}\x12"

    @property
    def is_say_link(self) -> bool:
        return self.item_id == 0xFFFFF

    @property
    def saylink_id(self) -> int | None:
        if not self.is_say_link:
            return None
        return self.augments[0] or self.augments[1] or None

    @property
    def is_silent(self) -> bool:
        return self.is_say_link and self.augments[1] != 0


MessagePart: TypeAlias = str | ItemLink

_LINK_RE = re.compile(r"\x12[^\x12]*\x12")
_HEX_RE = re.compile(r"[0-9a-fA-F]{56}")


def parse_message_parts(text: str) -> tuple[MessagePart, ...]:
    """Split RoF2 text into plain strings and typed hyperlinks."""
    parts: list[MessagePart] = []
    pos = 0

    for match in _LINK_RE.finditer(text):
        raw = match.group()
        body = raw[1:-1]

        if len(body) < 56 or not _HEX_RE.fullmatch(body[:56]):
            continue

        try:
            link = ItemLink.deserialize(raw)
        except ValueError:
            continue

        if match.start() > pos:
            parts.append(text[pos : match.start()])

        parts.append(link)
        pos = match.end()

    if pos < len(text):
        parts.append(text[pos:])

    return tuple(parts)


def leading_int(text: str) -> int:
    """First integer in a RoF zone or skill list. Empty and non-numeric lists are 0."""
    raw = text or ""
    start = 0
    while start < len(raw) and not (
        raw[start].isdigit()
        or (raw[start] == "-" and start + 1 < len(raw) and raw[start + 1].isdigit())
    ):
        start += 1
    if start >= len(raw):
        return 0
    end = start + 1
    while end < len(raw) and raw[end].isdigit():
        end += 1
    return int(raw[start:end], 10)
