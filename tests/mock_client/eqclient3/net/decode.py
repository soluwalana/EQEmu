"""Decode one application payload into the opcode struct."""

from __future__ import annotations

import struct

from eqclient3.log import log
from eqclient3.structs import EQStruct, OPERATIONS


def body(name: str, payload: object) -> EQStruct | None:
    """The struct for this opcode. An already-built one is returned. Short or unknown packets are None."""
    cls = OPERATIONS.get(name)
    if cls is not None and isinstance(payload, cls):
        return payload
    if cls is None or not isinstance(payload, (bytes, bytearray)):
        return None
    try:
        return cls.deserialize(bytes(payload))
    except (ValueError, struct.error):
        log.error("decode %s failed", name, exc_info=True)
        return None
