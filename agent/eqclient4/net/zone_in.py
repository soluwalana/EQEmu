"""Zone-in through OP_ClientReady. The session stays open for chat."""

from __future__ import annotations

import struct
import time
from collections.abc import Callable

from eqclient4.net.opcodes import require
from eqclient4.net.session import Session, SessionError
from eqclient4.structs import (
    OP_ClientReady,
    OP_ReqClientSpawn,
    OP_ReqNewZone,
    OP_SendExpZonein,
    OP_ZoneComplete,
    OP_ZoneEntry,
)

AppHandler = Callable[[int, bytes], None]


def _split(packet: bytes) -> tuple[int, bytes]:
    if len(packet) < 2:
        return 0, b""
    return struct.unpack_from("<H", packet)[0], packet[2:]


def zone_in(
    session: Session,
    opcodes: dict[str, int],
    character: str,
    on_app: AppHandler,
    timeout: float = 20.0,
) -> None:
    deadline = time.monotonic() + timeout
    send(session, require(opcodes, "OP_ZoneEntry"), OP_ZoneEntry(character).serialize())
    _wait_any(session, on_app, deadline)

    send(session, require(opcodes, "OP_ReqNewZone"), OP_ReqNewZone().serialize())
    _wait(session, opcodes, on_app, "OP_NewZone", deadline)

    send(session, require(opcodes, "OP_SendExpZonein"), OP_SendExpZonein().serialize())
    send(session, require(opcodes, "OP_ReqClientSpawn"), OP_ReqClientSpawn().serialize())
    # RoF2 leaves OP_ZoneServerReady at 0x0000. The same handler sends OP_SendAAStats
    # immediately before that empty opcode, so that is the packet this client can see.
    ready = opcodes.get("OP_ZoneServerReady") or opcodes.get("OP_SendAAStats")
    if not ready:
        raise SessionError("no RoF2 opcode to mark the end of OP_ReqClientSpawn")
    _wait_opcode(session, on_app, ready, "spawn contents", deadline)

    complete = opcodes.get("OP_ZoneComplete") or 0
    if complete:
        send(session, complete, OP_ZoneComplete().serialize())
    send(session, require(opcodes, "OP_ClientReady"), OP_ClientReady().serialize())
    # Give CompleteConnect, including FormOnConnect, time to answer.
    _drain(session, on_app, min(deadline, time.monotonic() + 2.0))


def send(session: Session, opcode: int, payload: bytes) -> None:
    session.send_app(struct.pack("<H", opcode) + payload)


def drain(session: Session, on_app: AppHandler, timeout: float) -> None:
    deadline = time.monotonic() + timeout
    _drain(session, on_app, deadline)


def _emit(packets: list[bytes], on_app: AppHandler) -> None:
    for packet in packets:
        opcode, payload = _split(packet)
        if opcode:
            on_app(opcode, payload)


def _drain(session: Session, on_app: AppHandler, deadline: float) -> None:
    # timeout 0 still reads what is already queued. The old loop never entered.
    if time.monotonic() >= deadline:
        _emit(session.pump(0), on_app)
        return
    while time.monotonic() < deadline:
        _emit(session.pump(0.1), on_app)


def _wait_any(session: Session, on_app: AppHandler, deadline: float) -> None:
    while time.monotonic() < deadline:
        packets = session.pump(0.2)
        if packets:
            _emit(packets, on_app)
            return
    raise SessionError("zone did not answer OP_ZoneEntry")


def _wait(
    session: Session,
    opcodes: dict[str, int],
    on_app: AppHandler,
    name: str,
    deadline: float,
) -> None:
    _wait_opcode(session, on_app, require(opcodes, name), name, deadline)


def _wait_opcode(
    session: Session,
    on_app: AppHandler,
    expected: int,
    name: str,
    deadline: float,
) -> None:
    while time.monotonic() < deadline:
        packets = session.pump(0.2)
        _emit(packets, on_app)
        if any(_split(packet)[0] == expected for packet in packets):
            return
    raise SessionError(f"timed out waiting for {name}")
