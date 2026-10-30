"""One typed object per opcode eqclient3 sends or reads.

Application objects serialize and deserialize the RoF2 opcode body
(little-endian). Session objects serialize and deserialize the whole datagram
(big-endian), including the leading zero and the session opcode byte.

Inventory slots on these objects stay the client numbers (cursor 30, ammo 21,
general 22-29). Serialize and deserialize translate those to the RoF2 slot
struct, whose cursor is 33.

Coordinates on these objects are x, y, z. Serialize and deserialize convert
the y, x, z order used on the wire.
"""

from __future__ import annotations

import struct
from typing import ClassVar, TypeVar

OPERATIONS: dict[str, type[EQStruct]] = {}

_S = TypeVar("_S", bound="EQStruct")


class EQStruct:
    """Wire object. Opcode classes register under their name. Nested records do not."""

    opcode: ClassVar[str] = ""

    def __init_subclass__(cls, **kwargs: object) -> None:
        super().__init_subclass__(**kwargs)
        cls.__module__ = "eqclient3.structs"
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
    # common/serialize_buffer.h:100 WriteUInt32
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


def _put_lenstr(text: str) -> bytes:
    """common/serialize_buffer.h:194 WriteLengthString. Length does not include a NUL."""
    raw = (text or "").encode("latin1", errors="replace")
    # common/serialize_buffer.h:188 length, then the bytes
    return struct.pack("<I", len(raw)) + raw


def _lenstr(data: bytes, offset: int) -> tuple[str, int]:
    if offset + 4 > len(data):
        raise ValueError("truncated length string")
    length = _read_u32(data, offset)
    start = offset + 4
    end = start + length
    if end > len(data):
        raise ValueError("truncated length string")
    return data[start:end].decode("latin1", errors="replace"), end


def _sign_extend(value: int, bits: int) -> int:
    value &= (1 << bits) - 1
    sign = 1 << (bits - 1)
    return value - (1 << bits) if value & sign else value


def _pack_eq19(value: float) -> int:
    return int(round(value * 8.0)) & 0x7FFFF


def _i8(value: int) -> int:
    """A uint8 bit pattern as a signed byte. 0xFF is -1."""
    value = int(value) & 0xFF
    if value >= 0x80:
        return value - 0x100
    return value


def _i16(value: int) -> int:
    """A uint16 bit pattern as a signed slot. 0xFFFF is -1."""
    value = int(value) & 0xFFFF
    if value >= 0x8000:
        return value - 0x10000
    return value


def _i32(value: int) -> int:
    """A uint32 bit pattern as a signed int. 0xFFFFFFFF is -1."""
    value = int(value) & 0xFFFFFFFF
    if value >= 0x80000000:
        return value - 0x100000000
    return value


def _to_rof2_slot(slot: int) -> int:
    """Client possession slot to the RoF2 slot number. Cursor 30 is 33."""
    slot = _i16(slot)
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


def _from_rof2_slot(slot: int) -> int:
    slot = _i16(slot)
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


def _pack_inventory_slot(slot: int) -> bytes:
    """Type 0, the RoF2 slot, sub-index and augment both invalid."""
    # common/patches/rof2_structs.h:57 InventorySlot_Struct
    return struct.pack("<hhhhhh", 0, 0, _i16(_to_rof2_slot(slot)), -1, -1, 0)


def _unpack_inventory_slot(data: bytes, offset: int) -> int:
    _kind, _unknown, wire, _sub, _aug, _tail = struct.unpack_from("<hhhhhh", data, offset)
    return _from_rof2_slot(int(wire))


def _bitword(*parts: tuple[int, int]) -> int:
    word = 0
    shift = 0
    for value, bits in parts:
        word |= (int(value) & ((1 << bits) - 1)) << shift
        shift += bits
    return word & 0xFFFFFFFF


def _bitfield(word: int, shift: int, bits: int, signed: bool = True) -> int:
    value = (word >> shift) & ((1 << bits) - 1)
    if signed:
        return _sign_extend(value, bits)
    return value


def _advance(data: bytes, offset: int, size: int, what: str) -> int:
    if offset + size > len(data):
        raise ValueError(f"{what} is {len(data)} bytes")
    return offset + size


def _pack_names(first: str, second: str, size: int = 128) -> bytes:
    packet = bytearray(size)
    _put_fixed(packet, 0, first, 64)
    _put_fixed(packet, 64, second, 64)
    return bytes(packet)


def _two_names(data: bytes) -> tuple[str, str]:
    first = _fixed(data, 0, 64) if len(data) >= 64 else ""
    second = _fixed(data, 64, 64) if len(data) >= 128 else ""
    return first, second
