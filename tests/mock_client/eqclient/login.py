"""Titanium login on UDP 5998."""

from __future__ import annotations

import struct
import time
from dataclasses import dataclass

from eqclient.crypto import decrypt_block, encrypt_block
from eqclient.opcodes import login_opcodes, require
from eqclient.packets import login_base, login_credentials, parse_login_accept, parse_server_list
from eqclient.session import Session, SessionError


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
        session.send_app(struct.pack("<H", require(opcodes, "OP_SessionReady")) + struct.pack("<I", 1))
        _wait_opcode(session, require(opcodes, "OP_ChatMessage"), deadline)

        plain = login_credentials(username, password)
        body = login_base(3, encrypt_type=2) + encrypt_block(plain)
        session.send_app(struct.pack("<H", require(opcodes, "OP_Login")) + body)
        accepted = _wait_opcode(session, require(opcodes, "OP_LoginAccepted"), deadline)
        header = len(login_base(0))
        cipher = accepted[header:]
        cipher = cipher[: len(cipher) - (len(cipher) % 8)]
        decoded = decrypt_block(cipher)
        account_id, key = parse_login_accept(decoded)
        if account_id <= 0 or not key:
            raise SessionError(f"login rejected for {username}")

        session.send_app(struct.pack("<HI", require(opcodes, "OP_ServerListRequest"), 4))
        listing = _wait_opcode(session, require(opcodes, "OP_ServerListResponse"), deadline)
        servers = parse_server_list(listing)
        if not servers:
            raise SessionError("login server returned no worlds")
        server_id = servers[0]

        play = login_base(5) + struct.pack("<I", server_id)
        session.send_app(struct.pack("<H", require(opcodes, "OP_PlayEverquestRequest")) + play)
        _wait_opcode(session, require(opcodes, "OP_PlayEverquestResponse"), deadline)
        return LoginResult(account_id, key, server_id)
    finally:
        session.close()


def _wait_opcode(session: Session, opcode: int, deadline: float) -> bytes:
    while time.monotonic() < deadline:
        for packet in session.pump(0.2):
            got, payload = _split(packet)
            if got == opcode:
                return payload
    raise SessionError(f"timed out waiting for login opcode {opcode:#06x}")
