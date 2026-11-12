"""Login, world enter, zone-in, and a rezone that does not touch a dead socket.

loop.start calls connect, then enter, then zone_in. A closed session or a
reliable-stream hole calls transfer_zone. transfer_zone closes the zone session
and the world session, then rezone: OP_SendLoginInfo with zoning=1, OP_EnterWorld,
OP_ZoneServerInfo, a new zone session, and zone_in. It does not send
OP_ApproveName or OP_CharacterCreate, and it does not write a zone request on
the socket it just closed.
"""

from __future__ import annotations

import os
import struct
import time
from collections.abc import Callable
from dataclasses import dataclass

from eqclient4.log import log, write
from eqclient4.net.login import login
from eqclient4.net.opcodes import require, rof2_opcodes
from eqclient4.net.session import Session, SessionError
from eqclient4.net.sheet import CreateCharacter, build
from eqclient4.net.zone_in import drain, send, zone_in
from eqclient4.structs import (
    SAY_CHANNEL,
    CharacterSlot,
    OP_ApproveName,
    OP_ChannelMessage,
    OP_CharacterCreate,
    OP_EnterWorld,
    OP_SendCharInfo,
    OP_SendLoginInfo,
    OP_SpecialMesg,
    OP_ZoneServerInfo,
)
from eqclient4.structs.messages import channel_bucket, saylink_plain, special_bucket


@dataclass
class Login:
    host: str | None = None
    user: str | None = None
    password: str | None = None
    character: str | None = None
    login_port: int | None = None
    world_port: int | None = None
    timeout: float | None = None
    race: int | None = None
    class_id: int | None = None
    gender: int | None = None
    deity: int | None = None
    start_zone: int | None = None


def _split(packet: bytes) -> tuple[int, bytes]:
    if len(packet) < 2:
        return (0, b"")
    return (struct.unpack_from("<H", packet)[0], packet[2:])


def _wait_opcode(session: Session, opcode: int, deadline: float) -> bytes:
    while time.monotonic() < deadline:
        for packet in session.pump(0.2):
            got, payload = _split(packet)
            if got == opcode:
                return payload
    raise SessionError(f"timed out waiting for world opcode {opcode:#06x}")


def _create_character(
    session: Session,
    opcodes: dict[str, int],
    name: str,
    deadline: float,
    sheet: CreateCharacter,
) -> bytes:
    """Approve the name, then send this race and class. World replies with a fresh char select.

    tutorial=1 is the RoF2 Enter Tutorial button. The server leaves it off for
    this client version, and a zero sends the new character to the start city.
    """
    approve = require(opcodes, "OP_ApproveName")
    session.send_app(
        struct.pack("<H", approve) + OP_ApproveName(name, sheet.race, sheet.class_id).serialize()
    )
    reply = _wait_opcode(session, approve, deadline)
    try:
        approved = OP_ApproveName.deserialize(reply).approved
    except ValueError:
        log.error("approve-name reply failed to parse", exc_info=True)
        approved = False
    if not approved:
        raise SessionError(f"world rejected the name {name!r}")
    strength, stamina, agility, dexterity, wisdom, intelligence, charisma = sheet.stats
    created = OP_CharacterCreate(
        sheet.class_id,
        sheet.race,
        sheet.gender,
        sheet.deity,
        sheet.start_zone,
        strength,
        stamina,
        agility,
        dexterity,
        wisdom,
        intelligence,
        charisma,
        tutorial=1,
    ).serialize()
    session.send_app(struct.pack("<H", require(opcodes, "OP_CharacterCreate")) + created)
    select = _wait_opcode(session, require(opcodes, "OP_SendCharInfo"), deadline)
    if name not in _select_names(select):
        raise SessionError(f"world did not list {name!r} after character create")
    return select


def enter_world_session(
    host: str,
    port: int,
    account_id: int,
    key: str,
    character: str,
    timeout: float = 15.0,
    sheet: CreateCharacter | None = None,
) -> tuple[Session, str, int, CharacterSlot | None]:
    """OP_SendLoginInfo, char select or create, OP_EnterWorld, OP_ZoneServerInfo.

    The world session stays open. A name already on the list is entered. A missing
    name is created and the next char select must list it. The sheet is built
    before this function opens a socket when the caller has not already built one.
    """
    if sheet is None:
        sheet = build()
    opcodes = rof2_opcodes()
    session = Session()
    try:
        session.connect(host, port, timeout=min(timeout, 5.0))
        deadline = time.monotonic() + timeout
        info = OP_SendLoginInfo(account_id, key).serialize()
        session.send_app(struct.pack("<H", require(opcodes, "OP_SendLoginInfo")) + info)
        select = _wait_opcode(session, require(opcodes, "OP_SendCharInfo"), deadline)
        played = _character_slot(select, character)
        if played is None:
            log.info("creating %s", character)
            select = _create_character(session, opcodes, character, deadline, sheet)
            played = _character_slot(select, character)
            log.info("created %s", character)
        if played is not None:
            log.info(
                "character card %s race=%s class=%s level=%s zone=%s",
                played.name,
                played.race,
                played.class_id,
                played.level,
                played.zone_id,
            )
        session.send_app(
            struct.pack("<H", require(opcodes, "OP_EnterWorld"))
            + OP_EnterWorld(character).serialize()
        )
        zone = OP_ZoneServerInfo.deserialize(
            _wait_opcode(session, require(opcodes, "OP_ZoneServerInfo"), deadline)
        )
        zone_host, zone_port = zone.host, zone.port
        if not zone_host or zone_host == "0.0.0.0":
            zone_host = host
        if zone_port == 0:
            raise SessionError("world returned zone port 0")
        log.info("zone server %s:%s", zone_host, zone_port)
        return (session, zone_host, zone_port, played)
    except Exception:
        session.close()
        raise


def rezone(
    host: str,
    port: int,
    account_id: int,
    key: str,
    character: str,
    timeout: float = 15.0,
) -> tuple[Session, str, int]:
    """World reconnect after the old sessions are closed.

    OP_SendLoginInfo.zoning=1 skips character select. This does not send
    OP_ApproveName or OP_CharacterCreate.
    """
    opcodes = rof2_opcodes()
    session = Session()
    try:
        session.connect(host, port, timeout=min(timeout, 5.0))
        deadline = time.monotonic() + timeout
        info = OP_SendLoginInfo(account_id, key, zoning=True).serialize()
        session.send_app(struct.pack("<H", require(opcodes, "OP_SendLoginInfo")) + info)
        enter_op = require(opcodes, "OP_EnterWorld")
        zsi_op = require(opcodes, "OP_ZoneServerInfo")
        prompt_deadline = min(deadline, time.monotonic() + 2.0)
        while time.monotonic() < prompt_deadline:
            for packet in session.pump(0.2):
                got, _payload = _split(packet)
                if got == enter_op:
                    prompt_deadline = time.monotonic()
                    break
            else:
                continue
            break
        session.send_app(struct.pack("<H", enter_op) + OP_EnterWorld(character).serialize())
        zone = OP_ZoneServerInfo.deserialize(_wait_opcode(session, zsi_op, deadline))
        zone_host, zone_port = zone.host, zone.port
        if not zone_host or zone_host == "0.0.0.0":
            zone_host = host
        if zone_port == 0:
            raise SessionError("world returned zone port 0 after transfer")
        return (session, zone_host, zone_port)
    except Exception:
        session.close()
        raise


class Client:
    """One account session. The zone socket is `session`. The world socket is `world`."""

    def __init__(self) -> None:
        self.messages: list[str] = []
        self.account_id = 0
        self.key = ""
        self.server_id = 0
        self.zone_host = ""
        self.zone_port = 0
        self.session: Session | None = None
        self.world: Session | None = None
        self.character = ""
        self.sheet: CreateCharacter | None = None
        self.played: CharacterSlot | None = None
        self.timeout = 20.0
        self.opcodes = rof2_opcodes()
        self._host = ""
        self._login_port = 5999
        self._world_port = 9000
        self._username = ""
        self._password = ""
        self._listeners: list[Callable[[int, bytes], None]] = []
        self._inbox: list[tuple[int, bytes]] = []
        self._names: dict[int, str] | None = None
        self._channel = require(self.opcodes, "OP_ChannelMessage")
        self._special = require(self.opcodes, "OP_SpecialMesg")

    @property
    def closed(self) -> bool:
        """True once the zone session has been closed. A client that has not entered is not closed."""
        session = self.session
        if session is None:
            return False
        return bool(session.closed or not session.connected)

    @property
    def needs_rezone(self) -> bool:
        """A reliable-stream hole on the zone session. The loop calls transfer_zone."""
        session = self.session
        return bool(session is not None and session.needs_rezone)

    @property
    def open(self) -> bool:
        """The zone socket is up. A client that has not entered is not open."""
        session = self.session
        if session is None:
            return False
        return bool(session.open)

    def on_app(self, opcode: int, payload: bytes) -> None:
        """zone_in and pump hand every application packet here."""
        text = ""
        who = ""
        bucket = ""
        try:
            if opcode == self._special:
                special = OP_SpecialMesg.deserialize(payload)
                who, text = special.speaker, special.message
                bucket = special_bucket(special.msg_type)
            elif opcode == self._channel:
                channel = OP_ChannelMessage.deserialize(payload)
                text = channel.text
                who = channel.sender
                bucket = channel_bucket(channel.channel)
        except ValueError:
            log.error("application packet %s failed to parse", opcode, exc_info=True)
            text = ""
        if text:
            text = saylink_plain(text)
            self.messages.append(text)
            if bucket and "faction standing" not in text.lower():
                speaker = f"{who}: " if who else ""
                log.debug("[%s] %s%s", bucket, speaker, text)
        self._inbox.append((opcode, payload))
        for handler in self._listeners:
            handler(opcode, payload)

    def listen(self, handler: Callable[[int, bytes], None]) -> None:
        self._listeners.append(handler)

    def start_io(self) -> None:
        """Start the zone and world writer/receiver threads. Handshake does not call this."""
        for session in (self.world, self.session):
            if session is None:
                continue
            start = getattr(session, "start_channels", None)
            if start is None or session.closed or not session.connected:
                continue
            start()

    def stop_io(self) -> None:
        for session in (self.session, self.world):
            if session is None:
                continue
            stop = getattr(session, "stop_channels", None)
            if stop is not None:
                stop()

    def pump(self, timeout: float = 0.0) -> list[tuple[str, bytes]]:
        """Drain the zone socket and return (opcode name, payload) for the loop.

        zone_in already called on_app, so those packets are waiting here too.
        The play loop is the consumer: another pump call takes the same packets.
        Once the channels are up, this only reads the receiver queue.
        """
        self.start_io()
        if self.world is not None:
            self.world.pump(0)
        session = self.session
        if (
            session is not None
            and session.connected
            and (not session.closed)
            and (not session.needs_rezone)
        ):
            drain(session, self.on_app, timeout)
        rows = self._inbox
        self._inbox = []
        found: list[tuple[str, bytes]] = []
        for opcode, payload in rows:
            name = self._opcode_name(opcode)
            if name:
                found.append((name, payload))
        return found

    def _opcode_name(self, number: int) -> str:
        if self._names is None:
            self._names = _preferred_names(self.opcodes)
        return self._names.get(number, "")

    def send(self, opcode_name: str, payload: bytes) -> None:
        """Write an application packet on the live zone session.

        A closed session raises. It does not write the bytes to the dead socket.
        """
        if self.session is None or not self.session.connected or self.session.closed:
            raise SessionError("client is not in a zone")
        if opcode_name == "OP_ChannelMessage":
            _print_say(payload, self.character)
        send(self.session, require(self.opcodes, opcode_name), payload)

    def say(
        self, text: str, *, language: int = 0, lang_skill: int = 100, pump: bool = True
    ) -> None:
        self._chat(text, SAY_CHANNEL, language=language, lang_skill=lang_skill, pump=pump)

    def command(self, text: str, *, pump: bool = True) -> None:
        if not text.startswith("^"):
            text = "^" + text
        self._chat(text, SAY_CHANNEL, pump=pump)

    def close(self) -> None:
        self.stop_io()
        for session in (self.session, self.world):
            if session is not None:
                session.close()
        self.session = None
        self.world = None

    def _chat(
        self,
        text: str,
        channel: int,
        target: str = "",
        *,
        language: int = 0,
        lang_skill: int = 100,
        pump: bool = True,
    ) -> None:
        payload = OP_ChannelMessage(
            target, self.character, language, channel, skill=lang_skill, text=text
        ).serialize()
        self.send("OP_ChannelMessage", payload)
        if pump:
            self.pump(0.05)


def _print_say(payload: bytes, character: str) -> None:
    """The say as it leaves. The server echo is a later line."""
    try:
        row = OP_ChannelMessage.deserialize(payload)
    except (ValueError, struct.error):
        return
    if int(row.channel) != SAY_CHANNEL:
        return
    who = (row.sender or character or "").strip()
    text = row.text
    write(f"> {who}: {text}" if who else f"> {text}")


def _select_names(payload: bytes) -> list[str]:
    return [slot.name for slot in OP_SendCharInfo.deserialize(payload).slots if slot.name]


def _character_slot(payload: bytes, name: str) -> CharacterSlot | None:
    want = name.lower()
    for slot in OP_SendCharInfo.deserialize(payload).slots:
        if slot.name.lower() == want:
            return slot
    return None


def _preferred_names(opcodes: dict[str, int]) -> dict[int, str]:
    """One wire number, one opcode name. A handler's name wins over an alias."""
    return {value: name for name, value in opcodes.items() if value}


def _connection_fields(connection: Login | dict | None, overrides: dict) -> dict:
    """Keywords win over the login record. A missing login reads the environment."""
    names = (
        "host",
        "user",
        "password",
        "character",
        "login_port",
        "world_port",
        "timeout",
        "race",
        "class_id",
        "gender",
        "deity",
        "start_zone",
    )
    fields: dict = {}
    if isinstance(connection, dict):
        source = connection
    elif connection is not None:
        source = {name: getattr(connection, name, None) for name in names}
    else:
        source = {}
    for name in names:
        value = source.get(name)
        if value is not None:
            fields[name] = value
    for key, value in overrides.items():
        if value is not None:
            fields[key] = value
    return fields


def connect(
    connection: Login | dict | None = None,
    sheet: CreateCharacter | None = None,
    **overrides: object,
) -> Client:
    """Log in. loop.start calls connect(connection, sheet).

    The sheet is built before any socket opens. A race and class that cannot
    pair raises here, before OP_SessionReady. connection carries host, user,
    password, character, and the ports. Omitted sheet fields read the environment.
    """
    fields = _connection_fields(connection, overrides)
    if sheet is None:
        sheet = build(
            fields.get("race"),
            fields.get("class_id"),
            fields.get("gender"),
            fields.get("deity"),
            fields.get("start_zone"),
        )
    host = fields.get("host")
    if not isinstance(host, str):
        host = os.environ.get("EQEMU_HOST", "127.0.0.1")
    user = fields.get("user")
    if not isinstance(user, str):
        user = os.environ["EQEMU_USER"]
    password = fields.get("password")
    if not isinstance(password, str):
        password = os.environ["EQEMU_PASS"]
    character = fields.get("character")
    if character is None:
        character = sheet.name or os.environ["EQEMU_CHAR"]
    login_port = fields.get("login_port")
    if login_port is None:
        login_port = int(os.environ.get("EQEMU_LOGIN_PORT", "5999"))
    world_port = fields.get("world_port")
    if world_port is None:
        world_port = int(os.environ.get("EQEMU_WORLD_PORT", "9000"))
    timeout = float(fields.get("timeout") or 20.0)
    client = Client()
    client._host = host
    client._login_port = login_port
    client._world_port = world_port
    client._username = user
    client._password = password
    client.character = character
    client.timeout = timeout
    client.sheet = sheet
    result = login(host, login_port, user, password, timeout=timeout)
    client.account_id = result.account_id
    client.key = result.key
    client.server_id = result.server_id
    log.info(
        "logged in %s account=%s server=%s at %s:%s",
        user,
        result.account_id,
        result.server_id,
        host,
        login_port,
    )
    return client


def enter(
    session: Client, sheet: CreateCharacter | None = None, *, timeout: float | None = None
) -> Client:
    """Char select or create, connect the zone session, and zone_in.

    loop.start calls enter(session, sheet) after connect. zone_in is the public
    function this calls once the zone socket is up.
    """
    client = session
    if sheet is not None:
        client.sheet = sheet
    if client.sheet is None:
        client.sheet = build()
    limit = client.timeout if timeout is None else timeout
    world_session, zone_host, zone_port, played = enter_world_session(
        client._host,
        client._world_port,
        client.account_id,
        client.key,
        client.character,
        timeout=limit,
        sheet=client.sheet,
    )
    client.played = played
    client.world = world_session
    client.zone_host = zone_host
    client.zone_port = zone_port
    zone_session = Session()
    try:
        zone_session.connect(zone_host, zone_port, timeout=min(limit, 5.0))
        client.session = zone_session
        zone_in(zone_session, client.opcodes, client.character, client.on_app, timeout=limit)
    except Exception:
        client.close()
        raise
    return client


def transfer_zone(session: Client | Session, *args: object, **kwargs: object) -> Client | None:
    """Close both sessions, then rezone. Nothing is written to the closed sockets.

    loop.start and a reliable-stream hole call transfer_zone(session).
    zoning=1 skips character select. zone_in runs on the new zone session.
    A session that is not this client is left alone: a dead socket gets no zone request.
    """
    client: Client | None
    if isinstance(session, Client):
        client = session
    else:
        owner = session.__dict__.get("client") if hasattr(session, "__dict__") else None
        client = owner if isinstance(owner, Client) else None
    if not isinstance(client, Client):
        return None
    timeout = kwargs.get("timeout")
    if args and timeout is None and isinstance(args[0], (int, float)):
        timeout = args[0]
    limit = float(timeout) if isinstance(timeout, (int, float)) else client.timeout
    zone = client.session
    world = client.world
    client.session = None
    client.world = None
    for sock in (zone, world):
        if sock is not None:
            sock.close()
    world_session, zone_host, zone_port = rezone(
        client._host,
        client._world_port,
        client.account_id,
        client.key,
        client.character,
        timeout=limit,
    )
    client.world = world_session
    client.zone_host = zone_host
    client.zone_port = zone_port
    zone_session = Session()
    try:
        zone_session.connect(zone_host, zone_port, timeout=min(limit, 5.0))
        client.session = zone_session
        zone_in(zone_session, client.opcodes, client.character, client.on_app, timeout=limit)
    except Exception:
        client.close()
        raise
    return client
