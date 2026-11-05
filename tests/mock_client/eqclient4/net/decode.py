"""Decode one application payload into the opcode struct."""

from __future__ import annotations

import struct

from eqclient4.log import log
from eqclient4.structs import OPERATIONS, EQStruct


def body(name: str, payload: object) -> EQStruct | None:
    """The struct for this opcode. An already-built one is returned. Short or unknown packets are None."""
    cls = OPERATIONS.get(name)
    if cls and isinstance(payload, cls):
        return payload
    if cls is None or not isinstance(payload, (bytes, bytearray)):
        return None
    try:
        return cls.deserialize(bytes(payload))
    except (ValueError, struct.error):
        log.error("decode %s failed", name, exc_info=True)
        return None
