"""Sibling `.eqm` caches. A header, a string table, an id index, and fixed records.

The loader maps the file and binary-searches the index. A lookup unpacks one
slice. The jsonl is read only to create the file the first time, or when the
jsonl is newer.
"""

from __future__ import annotations

import mmap
import os
import struct
from pathlib import Path

_View = bytes | bytearray | memoryview | mmap.mmap

MAGIC = b"EQM1"
VERSION = 1
HEADER_SIZE = 64
_HEADER = struct.Struct("<4s4sHH8I")


def eqm_path(source: Path) -> Path:
    return source.with_suffix(".eqm")


def eqm_ready(source: Path, mapped: Path) -> bool:
    """True when the mapped file is present and at least as new as the jsonl."""
    if not mapped.is_file() or mapped.stat().st_size < HEADER_SIZE:
        return False
    if not source.is_file():
        return True
    return mapped.stat().st_mtime >= source.stat().st_mtime


def pack_header(kind: bytes, slots: tuple[int, ...]) -> bytes:
    if len(kind) != 4 or len(slots) != 8:
        raise ValueError("eqm header needs a 4-byte kind and 8 slots")
    packed = _HEADER.pack(MAGIC, kind, VERSION, 0, *slots)
    return packed + b"\x00" * (HEADER_SIZE - len(packed))


def read_header(buf: _View, kind: bytes) -> tuple[int, ...]:
    if len(buf) < HEADER_SIZE or buf[:4] != MAGIC:
        raise ValueError("not an eqm cache")
    _magic, found, version, _flags, *slots = _HEADER.unpack_from(buf, 0)
    if found != kind or version != VERSION or len(slots) != 8:
        raise ValueError("eqm kind or version does not match")
    return tuple(slots)


class StringTable:
    """Unique utf-8 strings. `add` returns a byte offset into the finished blob."""

    def __init__(self) -> None:
        self.buf = bytearray()
        self._at: dict[str, int] = {}

    def add(self, text: str) -> int:
        found = self._at.get(text)
        if found is not None:
            return found
        raw = text.encode("utf-8")
        if len(raw) > 65535:
            raw = raw[:65535]
        off = len(self.buf)
        self.buf += struct.pack("<H", len(raw))
        self.buf += raw
        self._at[text] = off
        return off


def read_string(buf: _View, strings_off: int, rel: int) -> str:
    at = strings_off + rel
    size = struct.unpack_from("<H", buf, at)[0]
    return bytes(buf[at + 2 : at + 2 + size]).decode("utf-8")


class IdIndex:
    """Sorted `(id, start, count)` triples. `in` and `len` do not copy the table."""

    def __init__(self, buf: _View, offset: int, count: int) -> None:
        self._buf = buf
        self._offset = offset
        self._count = count

    def __len__(self) -> int:
        return self._count

    def __bool__(self) -> bool:
        return self._count > 0

    def __contains__(self, key: object) -> bool:
        if not isinstance(key, int):
            return False
        return self.span(key) is not None

    def span(self, key: int) -> tuple[int, int] | None:
        lo, hi = 0, self._count
        while lo < hi:
            mid = (lo + hi) // 2
            found, start, count = struct.unpack_from("<III", self._buf, self._offset + mid * 12)
            if found == key:
                return start, count
            if found < key:
                lo = mid + 1
            else:
                hi = mid
        return None


def find_record(buf: _View, offset: int, count: int, stride: int, key: int) -> int | None:
    """Byte offset of the fixed record whose first u32 is `key`."""
    lo, hi = 0, count
    while lo < hi:
        mid = (lo + hi) // 2
        at = offset + mid * stride
        found = struct.unpack_from("<I", buf, at)[0]
        if found == key:
            return at
        if found < key:
            lo = mid + 1
        else:
            hi = mid
    return None


def write_eqm(
    dest: Path, kind: bytes, slots: tuple[int, ...], parts: list[bytes | bytearray]
) -> None:
    blob = bytearray(pack_header(kind, slots))
    for part in parts:
        blob += part
    tmp = dest.with_name(dest.name + ".tmp")
    tmp.write_bytes(blob)
    os.replace(tmp, dest)
