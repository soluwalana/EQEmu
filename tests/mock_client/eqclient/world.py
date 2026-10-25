"""World enter on UDP 9000. Returns the zone host and port."""

from __future__ import annotations

import struct
import time

from eqclient.opcodes import require, titanium_opcodes
from eqclient.packets import (
    character_select_names,
    char_create,
    enter_world,
    login_info,
    name_approval,
    zone_server_info,
)

# Human warrior. Base 75s plus the warrior class adds, with the 25 point pool in STR.
# CheckCharCreateInfoTitanium requires the total to match and no stat below its base.
_HUMAN = 1
_WARRIOR = 1
_QEYNOS = 1
_AGNOSTIC = 396
_HUMAN_WARRIOR_STATS = (110, 85, 80, 75, 75, 75, 75)
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
        select = _wait_opcode(session, require(opcodes, "OP_SendCharInfo"), deadline)
        if character not in character_select_names(select):
            _create_character(session, opcodes, character, deadline)
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


def _create_character(session: Session, opcodes: dict[str, int], name: str, deadline: float) -> None:
    """Approve the name, then send a human warrior. World replies with a fresh char select."""
    approve = require(opcodes, "OP_ApproveName")
    session.send_app(struct.pack("<H", approve) + name_approval(name, _HUMAN, _WARRIOR))
    reply = _wait_opcode(session, approve, deadline)
    if not reply or reply[0] != 1:
        raise SessionError(f"world rejected the name {name!r}")
    created = char_create(_WARRIOR, _HUMAN, 0, _AGNOSTIC, _QEYNOS, _HUMAN_WARRIOR_STATS)
    session.send_app(struct.pack("<H", require(opcodes, "OP_CharacterCreate")) + created)
    select = _wait_opcode(session, require(opcodes, "OP_SendCharInfo"), deadline)
    if name not in character_select_names(select):
        raise SessionError(f"world did not list {name!r} after character create")


def _wait_opcode(session: Session, opcode: int, deadline: float) -> bytes:
    while time.monotonic() < deadline:
        for packet in session.pump(0.2):
            got, payload = _split(packet)
            if got == opcode:
                return payload
    raise SessionError(f"timed out waiting for world opcode {opcode:#06x}")
