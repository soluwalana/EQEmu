"""High-level Titanium client: login, enter world, zone in, say, and bot commands."""

from __future__ import annotations

import os
import time

from eqclient.login import login
from eqclient.opcodes import require, titanium_opcodes
from eqclient.packets import (
    SAY_CHANNEL,
    channel_message,
    channel_message_text,
    special_message_text,
)
from eqclient.session import Session, SessionError
from eqclient.world import enter
from eqclient.zone import drain, send, zone_in


class Client:
    def __init__(self) -> None:
        self.messages: list[str] = []
        self.account_id = 0
        self.key = ""
        self.server_id = 0
        self.zone_host = ""
        self.zone_port = 0
        self._host = ""
        self._login_port = 5998
        self._world_port = 9000
        self._username = ""
        self._password = ""
        self._character = ""
        self._timeout = 20.0
        self._opcodes = titanium_opcodes()
        self._world: Session | None = None
        self._session: Session | None = None
        self._channel = require(self._opcodes, "OP_ChannelMessage")
        self._special = require(self._opcodes, "OP_SpecialMesg")

    def say(self, text: str) -> None:
        self._chat(text, SAY_CHANNEL)

    def command(self, text: str) -> None:
        if not text.startswith("^"):
            text = "^" + text
        self._chat(text, SAY_CHANNEL)

    def wait_message(self, substring: str, timeout: float = 10.0) -> str:
        deadline = time.monotonic() + timeout
        while True:
            for message in self.messages:
                if substring in message:
                    return message
            if time.monotonic() >= deadline:
                seen = " | ".join(self.messages[-8:]) or "(no messages)"
                raise SessionError(f"timed out waiting for {substring!r}; recent: {seen}")
            self._pump(min(0.2, deadline - time.monotonic()))

    def close(self) -> None:
        for session in (self._session, self._world):
            if session is not None:
                session.close()
        self._session = None
        self._world = None

    def _chat(self, text: str, channel: int) -> None:
        if self._session is None:
            raise SessionError("client is not in a zone")
        payload = channel_message(self._character, text, channel)
        send(self._session, self._channel, payload)
        self._pump(0.05)

    def _pump(self, timeout: float) -> None:
        if self._world is not None:
            self._world.pump(0)
        if self._session is None:
            return
        drain(self._session, self._on_app, timeout)

    def _on_app(self, opcode: int, payload: bytes) -> None:
        if opcode == self._special:
            text = special_message_text(payload)
        elif opcode == self._channel:
            text = channel_message_text(payload)
        else:
            return
        if text:
            self.messages.append(text)


def connect(
    host: str | None = None,
    user: str | None = None,
    password: str | None = None,
    character: str | None = None,
    login_port: int | None = None,
    world_port: int | None = None,
    timeout: float = 20.0,
) -> Client:
    """Log in, enter world, and finish zone-in. Reads EQEMU_* when an argument is omitted."""
    host = host if host is not None else os.environ.get("EQEMU_HOST", "127.0.0.1")
    user = user if user is not None else os.environ["EQEMU_USER"]
    password = password if password is not None else os.environ["EQEMU_PASS"]
    character = character if character is not None else os.environ["EQEMU_CHAR"]
    login_port = login_port if login_port is not None else int(os.environ.get("EQEMU_LOGIN_PORT", "5998"))
    world_port = world_port if world_port is not None else int(os.environ.get("EQEMU_WORLD_PORT", "9000"))

    client = Client()
    client._host = host
    client._login_port = login_port
    client._world_port = world_port
    client._username = user
    client._password = password
    client._character = character
    client._timeout = timeout

    result = login(host, login_port, user, password, timeout=timeout)
    client.account_id = result.account_id
    client.key = result.key
    client.server_id = result.server_id

    world_session, zone_host, zone_port = enter(
        host, world_port, result.account_id, result.key, character, timeout=timeout
    )
    client._world = world_session
    client.zone_host = zone_host
    client.zone_port = zone_port

    try:
        session = Session()
        session.connect(zone_host, zone_port, timeout=min(timeout, 5.0))
        client._session = session
        zone_in(session, client._opcodes, character, client._on_app, timeout=timeout)
    except Exception:
        client.close()
        raise
    return client
