"""World enter on UDP 9000. Returns the zone host and port."""

from __future__ import annotations

import struct
import time

from eqclient.opcodes import require, titanium_opcodes
from eqclient.packets import enter_world, login_info, zone_server_info
from eqclient.session import Session, SessionError


def _split(packet: bytes) -> tuple[int, bytes]:
    if len(packet) < 2:
        return 0, b""
    return struct.unpack_from("<H", packet)[0], packet[2:]


def enter(
    host: str,
    port: int,
    account_id: int,
    key: str,
    character: str,
    timeout: float = 15.0,
) -> tuple[Session, str, int]:
    """Leave the world session open. World drops the client, and its zone auth, when it closes."""
    opcodes = titanium_opcodes()
    session = Session()
    try:
        session.connect(host, port, timeout=min(timeout, 5.0))
        deadline = time.monotonic() + timeout
        info = login_info(account_id, key)
        session.send_app(struct.pack("<H", require(opcodes, "OP_SendLoginInfo")) + info)
        # World identifies Titanium from this packet, then sends char select.
        _wait_opcode(session, require(opcodes, "OP_SendCharInfo"), deadline)
        session.send_app(struct.pack("<H", require(opcodes, "OP_EnterWorld")) + enter_world(character))
        zone = _wait_opcode(session, require(opcodes, "OP_ZoneServerInfo"), deadline)
        zone_host, zone_port = zone_server_info(zone)
        if not zone_host or zone_host == "0.0.0.0":
            zone_host = host
        if zone_port == 0:
            raise SessionError("world returned zone port 0")
        return session, zone_host, zone_port
    except Exception:
        session.close()
        raise


def _wait_opcode(session: Session, opcode: int, deadline: float) -> bytes:
    while time.monotonic() < deadline:
        for packet in session.pump(0.2):
            got, payload = _split(packet)
            if got == opcode:
                return payload
    raise SessionError(f"timed out waiting for world opcode {opcode:#06x}")
