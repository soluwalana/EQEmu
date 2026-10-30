"""RoF2 login on UDP 5999."""

from __future__ import annotations

import struct
import time
from dataclasses import dataclass

from eqclient3.net.crypto import decrypt_block, encrypt_block
from eqclient3.net.opcodes import login_opcodes, require
from eqclient3.net.session import Session, SessionError
from eqclient3.structs import (
    LOGIN_BASE_SIZE,
    OP_Login,
    OP_LoginAccepted,
    OP_PlayEverquestRequest,
    OP_ServerListRequest,
    OP_ServerListResponse,
    OP_SessionReady,
)


@dataclass
class LoginResult:
    account_id: int
    key: str
    server_id: int


def _split(packet: bytes) -> tuple[int, bytes]:
    if len(packet) < 2:
        return 0, b""
    return struct.unpack_from("<H", packet)[0], packet[2:]


def login(host: str, port: int, username: str, password: str, timeout: float = 10.0) -> LoginResult:
    opcodes = login_opcodes()
    session = Session()
    try:
        session.connect(host, port, timeout=timeout)
        deadline = time.monotonic() + timeout
        session.send_app(struct.pack("<H", require(opcodes, "OP_SessionReady")) + OP_SessionReady(1).serialize())
        _wait_opcode(session, require(opcodes, "OP_ChatMessage"), deadline)

        plain = OP_Login(username, password).serialize()
        body = OP_Login(username, password, cipher=encrypt_block(plain[LOGIN_BASE_SIZE:])).serialize()
        session.send_app(struct.pack("<H", require(opcodes, "OP_Login")) + body)
        accepted = _wait_opcode(session, require(opcodes, "OP_LoginAccepted"), deadline)
        received = OP_Login.deserialize(accepted)
        cipher = received.cipher[: len(received.cipher) - (len(received.cipher) % 8)]
        decoded = OP_LoginAccepted.deserialize(decrypt_block(cipher))
        if decoded.account_id <= 0 or not decoded.key:
            raise SessionError(f"login rejected for {username}")

        session.send_app(
            struct.pack("<H", require(opcodes, "OP_ServerListRequest")) + OP_ServerListRequest(4).serialize()
        )
        listing = _wait_opcode(session, require(opcodes, "OP_ServerListResponse"), deadline)
        servers = OP_ServerListResponse.deserialize(listing).servers
        if not servers:
            raise SessionError("login server returned no worlds")
        server_id = servers[0].server_id

        session.send_app(
            struct.pack("<H", require(opcodes, "OP_PlayEverquestRequest"))
            + OP_PlayEverquestRequest(server_id).serialize()
        )
        _wait_opcode(session, require(opcodes, "OP_PlayEverquestResponse"), deadline)
        return LoginResult(decoded.account_id, decoded.key, server_id)
    finally:
        session.close()


def _wait_opcode(session: Session, opcode: int, deadline: float) -> bytes:
    while time.monotonic() < deadline:
        for packet in session.pump(0.2):
            got, payload = _split(packet)
            if got == opcode:
                return payload
    raise SessionError(f"timed out waiting for login opcode {opcode:#06x}")
