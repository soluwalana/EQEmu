"""Pack and unpack the few Titanium structs this client sends and reads."""

from __future__ import annotations

import struct


SAY_CHANNEL = 8

LOGIN_BASE_SIZE = 10  # int32, bool, int8, int32, packed
LOGIN_REPLY_ACCOUNT_OFFSET = 8
LOGIN_REPLY_KEY_OFFSET = 12
LOGIN_INFO_SIZE = 488
ENTER_WORLD_SIZE = 72
ZONE_ENTRY_SIZE = 68
ZONE_SERVER_INFO_SIZE = 130
CHANNEL_MESSAGE_SIZE = 148


def cstring(data: bytes, offset: int) -> tuple[str, int]:
    end = data.find(b"\x00", offset)
    if end < 0:
        raise ValueError("unterminated string")
    return data[offset:end].decode("latin1", errors="replace"), end + 1


def login_base(sequence: int, encrypt_type: int = 0) -> bytes:
    return struct.pack("<iBbi", sequence, 0, encrypt_type, 0)


def login_credentials(username: str, password: str) -> bytes:
    return username.encode("latin1") + b"\x00" + password.encode("latin1") + b"\x00"


def parse_login_accept(plain: bytes) -> tuple[int, str]:
    if len(plain) < LOGIN_REPLY_KEY_OFFSET + 11:
        raise ValueError(f"login reply is {len(plain)} bytes")
    account_id = struct.unpack_from("<i", plain, LOGIN_REPLY_ACCOUNT_OFFSET)[0]
    key = plain[LOGIN_REPLY_KEY_OFFSET : LOGIN_REPLY_KEY_OFFSET + 11].split(b"\x00", 1)[0]
    return account_id, key.decode("latin1")


def parse_server_list(payload: bytes) -> list[int]:
    """Return world server ids from an OP_ServerListResponse body."""
    offset = LOGIN_BASE_SIZE
    _success = payload[offset]
    offset += 1
    offset += 4  # error string id
    _unused, offset = cstring(payload, offset)
    if offset + 4 > len(payload):
        return []
    count = struct.unpack_from("<i", payload, offset)[0]
    offset += 4
    servers: list[int] = []
    for _ in range(max(0, count)):
        _ip, offset = cstring(payload, offset)
        if offset + 8 > len(payload):
            break
        _server_type, server_id = struct.unpack_from("<iI", payload, offset)
        offset += 8
        _name, offset = cstring(payload, offset)
        _country, offset = cstring(payload, offset)
        _language, offset = cstring(payload, offset)
        offset += 8  # status, player count
        servers.append(server_id)
    return servers


def login_info(account_id: int, key: str) -> bytes:
    packet = bytearray(LOGIN_INFO_SIZE)
    creds = f"{account_id}\x00{key}".encode("latin1")
    packet[: min(len(creds), 64)] = creds[:64]
    return bytes(packet)


def enter_world(name: str) -> bytes:
    packet = bytearray(ENTER_WORLD_SIZE)
    encoded = name.encode("latin1")[:63]
    packet[: len(encoded)] = encoded
    return bytes(packet)


def zone_entry(name: str) -> bytes:
    packet = bytearray(ZONE_ENTRY_SIZE)
    encoded = name.encode("latin1")[:63]
    packet[4 : 4 + len(encoded)] = encoded
    return bytes(packet)


def zone_server_info(payload: bytes) -> tuple[str, int]:
    if len(payload) < ZONE_SERVER_INFO_SIZE:
        raise ValueError(f"OP_ZoneServerInfo is {len(payload)} bytes")
    host = payload[:128].split(b"\x00", 1)[0].decode("latin1")
    port = struct.unpack_from("<H", payload, 128)[0]
    return host, port


def channel_message(sender: str, text: str, channel: int = SAY_CHANNEL) -> bytes:
    packet = bytearray(CHANNEL_MESSAGE_SIZE)
    encoded_sender = sender.encode("latin1")[:63]
    packet[64 : 64 + len(encoded_sender)] = encoded_sender
    struct.pack_into("<III", packet, 128, 0, channel, 0)
    return bytes(packet) + text.encode("latin1") + b"\x00"


def channel_message_text(payload: bytes) -> str:
    if len(payload) <= CHANNEL_MESSAGE_SIZE:
        return ""
    return payload[CHANNEL_MESSAGE_SIZE:].split(b"\x00", 1)[0].decode("latin1", errors="replace")


def special_message_text(payload: bytes) -> str:
    """Client::Message layout after the Titanium OP_SpecialMesg encode."""
    if len(payload) < 11:
        return ""
    offset = 3 + 4 + 4
    _name, offset = cstring(payload, offset)
    offset += 12
    if offset >= len(payload):
        return ""
    message, _end = cstring(payload, offset)
    return message
