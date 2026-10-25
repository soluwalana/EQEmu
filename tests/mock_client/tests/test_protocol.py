"""Protocol tests that do not need a running server."""

import struct

from eqclient.crc import crc32
from eqclient.crypto import decrypt_block, encrypt_block
from eqclient.packets import (
    CHAR_CREATE_SIZE,
    channel_message_text,
    char_create,
    character_select_names,
    parse_login_accept,
    parse_server_list,
    special_message_text,
)
from eqclient.session import OP_PACKET, Session


def test_crc32_matches_iso_hdlc_empty_and_check_value():
    assert crc32(b"") == 0
    assert crc32(b"123456789") == 0xCBF43926


def test_keyed_crc_mixes_the_key_before_the_payload():
    payload = b"zone"
    assert crc32(payload, 0x01020304) != crc32(payload)
    assert crc32(payload, 0x01020304) == crc32(payload, 0x01020304)


def test_login_des_round_trip():
    plain = b"tester\x00secret\x00"
    cipher = encrypt_block(plain)
    assert len(cipher) % 8 == 0
    assert decrypt_block(cipher).startswith(plain)


def test_character_select_names_and_create_packet():
    payload = bytearray(1704)
    payload[1024:1031] = b"Mockone"
    assert character_select_names(bytes(payload)) == ["Mockone"]
    created = char_create(1, 1, 0, 396, 1, (110, 85, 80, 75, 75, 75, 75))
    assert len(created) == CHAR_CREATE_SIZE
    assert created[:8] == struct.pack("<II", 1, 0)


def test_login_accept_layout():
    # PlayerLoginReply: reply header 6, unk1, unk2, lsid, key[11]
    plain = bytearray(64)
    plain[8:12] = struct.pack("<i", 42)
    plain[12:22] = b"abcdefghij"
    account_id, key = parse_login_accept(bytes(plain))
    assert account_id == 42
    assert key == "abcdefghij"


def test_server_list_parser_reads_the_first_world_id():
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
    assert parse_server_list(bytes(payload)) == [7]


def test_special_and_channel_text():
    special = bytearray()
    special += bytes((1, 0, 0))
    special += struct.pack("<II", 1, 0)
    special += b"\x00"
    special += struct.pack("<iii", 0, 0, 0)
    special += b"Bot raid formed.\x00"
    assert special_message_text(bytes(special)) == "Bot raid formed."

    channel = bytearray(148) + b"integration smoke\x00"
    assert channel_message_text(bytes(channel)) == "integration smoke"


def _reliable(sequence: int, app: bytes) -> bytes:
    return struct.pack(">BBH", 0, OP_PACKET, sequence) + app


def test_combined_reliable_packets_arrive_in_order():
    session = Session()
    session.connected = True
    session._peer = ("127.0.0.1", 9)
    app1 = struct.pack("<H", 0x1111) + b"one"
    app2 = struct.pack("<H", 0x2222) + b"two"
    first = _reliable(0, app1)
    second = _reliable(1, app2)
    combined = bytes([0, 0x03, len(first)]) + first + bytes([len(second)]) + second
    session._process_decoded(combined)
    assert session._inbox == [app1, app2]
    session.close()


def test_fragments_reassemble_before_the_app_packet_is_delivered():
    session = Session()
    session.connected = True
    session._peer = ("127.0.0.1", 9)
    app = struct.pack("<H", 0x3333) + b"abcdefghij"
    first = struct.pack(">BBHI", 0, 0x0D, 0, len(app)) + app[:4]
    second = struct.pack(">BBH", 0, 0x0D, 1) + app[4:]
    session._process_decoded(first)
    assert session._inbox == []
    session._process_decoded(second)
    assert session._inbox == [app]
    session.close()


def test_compressed_crc_datagram_decodes_to_the_app_packet():
    session = Session()
    session.connected = True
    session.crc_bytes = 2
    session.encode_key = 0x01020304
    session.encode_passes = (1, 0)
    session._peer = ("127.0.0.1", 9)
    app = struct.pack("<H", 0x4444) + (b"zone-in profile " * 8)
    raw = _reliable(0, app)
    encoded = session._apply_encode(raw)
    datagram = encoded + struct.pack(">H", crc32(encoded, session.encode_key) & 0xFFFF)
    session._handle_datagram(datagram)
    assert session._inbox == [app]
    session.close()
