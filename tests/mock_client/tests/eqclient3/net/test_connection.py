"""Scripted login and world replies on the socket connect, enter, and transfer_zone speak."""

from __future__ import annotations

import struct

from eqclient3.net.client import connect, enter, transfer_zone
from eqclient3.net.crypto import encrypt_block
from eqclient3.net.opcodes import login_opcodes, require, rof2_opcodes
from eqclient3.structs import LoginBase, OP_SendCharInfo, CharacterSlot
from eqclient3.net.sheet import build
from net.peer import Peer

NAME = "Mockone"
ACCOUNT = 42
KEY = "abcdefghij"


def _opcodes():
    world = rof2_opcodes()
    login = login_opcodes()
    return world, login


def _char_select(name: str) -> bytes:
    slots = [CharacterSlot(name, class_id=1, level=1)] if name else []
    return OP_SendCharInfo(slots).serialize()


def _zone_info(port: int) -> bytes:
    packet = bytearray(130)
    host = b"127.0.0.1"
    packet[: len(host)] = host
    struct.pack_into("<H", packet, 128, port)
    return bytes(packet)


def _login_accept() -> bytes:
    plain = bytearray(64)
    struct.pack_into("<i", plain, 8, ACCOUNT)
    raw = KEY.encode("latin1")
    plain[12 : 12 + len(raw)] = raw
    return LoginBase(0).serialize() + encrypt_block(bytes(plain))


def _server_list() -> bytes:
    def cstring(text: str) -> bytes:
        return text.encode() + b"\x00"

    payload = bytearray()
    payload += struct.pack("<iBbi", 4, 0, 0, 0)
    payload += struct.pack("<bi", 1, 101)
    payload += cstring("")
    payload += struct.pack("<i", 1)
    payload += cstring("127.0.0.1")
    payload += struct.pack("<iI", 1, 7)
    payload += cstring("test")
    payload += cstring("us")
    payload += cstring("en")
    payload += struct.pack("<iI", 0, 0)
    return bytes(payload)


def _zone_script(peer: Peer, world_ops: dict[str, int]) -> None:
    entry = require(world_ops, "OP_ZoneEntry")
    req = require(world_ops, "OP_ReqNewZone")
    new_zone = require(world_ops, "OP_NewZone")
    spawn = require(world_ops, "OP_ReqClientSpawn")
    ready = require(world_ops, "OP_SendAAStats")

    def on_entry(_peer, _payload):
        _peer.reply(1, b"")

    def on_req(_peer, _payload):
        _peer.reply(new_zone, b"")

    def on_spawn(_peer, _payload):
        _peer.reply(ready, b"")

    peer.always(entry, on_entry)
    peer.always(req, on_req)
    peer.always(spawn, on_spawn)


def _login_script(peer: Peer, login_ops: dict[str, int]) -> None:
    peer.once(
        require(login_ops, "OP_SessionReady"),
        lambda p, _payload: p.reply(require(login_ops, "OP_ChatMessage"), b"\x00"),
    )
    peer.once(
        require(login_ops, "OP_Login"),
        lambda p, _payload: p.reply(require(login_ops, "OP_LoginAccepted"), _login_accept()),
    )
    peer.once(
        require(login_ops, "OP_ServerListRequest"),
        lambda p, _payload: p.reply(require(login_ops, "OP_ServerListResponse"), _server_list()),
    )
    peer.once(
        require(login_ops, "OP_PlayEverquestRequest"),
        lambda p, _payload: p.reply(require(login_ops, "OP_PlayEverquestResponse"), b"\x00"),
    )


def _connection(login: Peer, world: Peer) -> dict:
    return {
        "host": "127.0.0.1",
        "user": "tester",
        "password": "secret",
        "character": NAME,
        "login_port": login.port,
        "world_port": world.port,
        "timeout": 15,
    }


def _names(apps, opcodes, *wanted):
    by_value = {number: name for name, number in opcodes.items()}
    found = []
    for opcode, _payload in apps:
        name = by_value.get(opcode)
        if name in wanted and (not found or found[-1] != name):
            found.append(name)
    return found


def test_listed_name_enters_without_character_create():
    world_ops, login_ops = _opcodes()
    login = Peer()
    world = Peer()
    zone = Peer()
    client = None
    try:
        _login_script(login, login_ops)
        _zone_script(zone, world_ops)
        charinfo = require(world_ops, "OP_SendCharInfo")
        enter_op = require(world_ops, "OP_EnterWorld")
        info = require(world_ops, "OP_ZoneServerInfo")
        world.once(
            require(world_ops, "OP_SendLoginInfo"),
            lambda peer, _payload: peer.reply(charinfo, _char_select(NAME)),
        )
        world.once(enter_op, lambda peer, _payload: peer.reply(info, _zone_info(zone.port)))
        sheet = build(1, 1, 0)
        client = connect(_connection(login, world), sheet)
        enter(client, sheet)
        sent = _names(
            world.apps,
            world_ops,
            "OP_SendLoginInfo",
            "OP_EnterWorld",
            "OP_ApproveName",
            "OP_CharacterCreate",
        )
        assert sent == ["OP_SendLoginInfo", "OP_EnterWorld"]
        assert "OP_CharacterCreate" not in sent
        assert "OP_ApproveName" not in sent
    finally:
        if client is not None:
            client.close()
        zone.stop()
        world.stop()
        login.stop()


def test_missing_name_approves_then_creates_and_waits_for_the_name():
    world_ops, login_ops = _opcodes()
    login = Peer()
    world = Peer()
    zone = Peer()
    client = None
    try:
        _login_script(login, login_ops)
        _zone_script(zone, world_ops)
        charinfo = require(world_ops, "OP_SendCharInfo")
        approve = require(world_ops, "OP_ApproveName")
        create = require(world_ops, "OP_CharacterCreate")
        enter_op = require(world_ops, "OP_EnterWorld")
        info = require(world_ops, "OP_ZoneServerInfo")
        selects = {"n": 0}

        def on_login(peer, _payload):
            selects["n"] += 1
            peer.reply(charinfo, _char_select(""))

        def on_create(peer, _payload):
            selects["n"] += 1
            peer.reply(charinfo, _char_select(NAME))

        world.once(require(world_ops, "OP_SendLoginInfo"), on_login)
        world.once(approve, lambda peer, _payload: peer.reply(approve, b"\x01"))
        world.once(create, on_create)
        world.once(enter_op, lambda peer, _payload: peer.reply(info, _zone_info(zone.port)))
        sheet = build(1, 1, 0)
        client = connect(_connection(login, world), sheet)
        enter(client, sheet)
        sent = _names(
            world.apps,
            world_ops,
            "OP_SendLoginInfo",
            "OP_ApproveName",
            "OP_CharacterCreate",
            "OP_EnterWorld",
        )
        assert sent == [
            "OP_SendLoginInfo",
            "OP_ApproveName",
            "OP_CharacterCreate",
            "OP_EnterWorld",
        ]
        assert selects["n"] == 2
    finally:
        if client is not None:
            client.close()
        zone.stop()
        world.stop()
        login.stop()


def test_transfer_zone_rezones_without_touching_the_dead_socket():
    world_ops, login_ops = _opcodes()
    login = Peer()
    world = Peer()
    zone = Peer()
    client = None
    try:
        _login_script(login, login_ops)
        _zone_script(zone, world_ops)
        charinfo = require(world_ops, "OP_SendCharInfo")
        enter_op = require(world_ops, "OP_EnterWorld")
        info_op = require(world_ops, "OP_ZoneServerInfo")
        login_info = require(world_ops, "OP_SendLoginInfo")
        change = require(world_ops, "OP_ZoneChange")

        def on_login(peer, payload):
            if payload[188:189] == b"\x01":
                peer.reply(enter_op, b"")
                return
            peer.reply(charinfo, _char_select(NAME))

        world.always(login_info, on_login)
        world.always(enter_op, lambda peer, _payload: peer.reply(info_op, _zone_info(zone.port)))
        sheet = build(1, 1, 0)
        client = connect(_connection(login, world), sheet)
        enter(client, sheet)
        old_zone = client.session
        old_world = client.world
        before = len(world.apps)
        zone_before = len(zone.apps)
        client.session.needs_rezone = True
        assert client.needs_rezone
        transfer_zone(client)
        assert old_zone.closed
        assert old_world.closed
        fresh = world.apps[before:]
        sent = _names(
            fresh,
            world_ops,
            "OP_SendLoginInfo",
            "OP_EnterWorld",
            "OP_ApproveName",
            "OP_CharacterCreate",
        )
        assert sent == ["OP_SendLoginInfo", "OP_EnterWorld"]
        info = next(payload for opcode, payload in fresh if opcode == login_info)
        assert info[188] == 1
        assert change not in {opcode for opcode, _payload in zone.apps[zone_before:]}
        assert change not in {opcode for opcode, _payload in zone.apps}
    finally:
        if client is not None:
            client.close()
        zone.stop()
        world.stop()
        login.stop()
