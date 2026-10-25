"""Pack and unpack the few Titanium structs this client sends and reads."""

from __future__ import annotations

import struct
from dataclasses import dataclass


SAY_CHANNEL = 8

LOGIN_BASE_SIZE = 10  # int32, bool, int8, int32, packed
LOGIN_REPLY_ACCOUNT_OFFSET = 8
LOGIN_REPLY_KEY_OFFSET = 12
# Titanium::structs::LoginInfo_Struct. The header comment says 488, but the
# packed fields are 64 + 124 + 1 + 275 = 464, which is what world identifies.
LOGIN_INFO_SIZE = 464
ENTER_WORLD_SIZE = 72
ZONE_ENTRY_SIZE = 68
ZONE_SERVER_INFO_SIZE = 130
CHANNEL_MESSAGE_SIZE = 148
NAME_APPROVAL_SIZE = 72  # char name[64], uint32 race, uint32 class
CHAR_CREATE_SIZE = 80  # 20 little-endian uint32 fields
CHAR_SELECT_NAME_OFFSET = 1024
CHAR_SELECT_NAME_SLOTS = 10


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


def name_approval(name: str, race: int, class_id: int) -> bytes:
    packet = bytearray(NAME_APPROVAL_SIZE)
    encoded = name.encode("latin1")[:63]
    packet[: len(encoded)] = encoded
    struct.pack_into("<II", packet, 64, race, class_id)
    return bytes(packet)


def char_create(
    class_id: int,
    race: int,
    gender: int,
    deity: int,
    start_zone: int,
    stats: tuple[int, int, int, int, int, int, int],
) -> bytes:
    """Titanium CharCreate_Struct. stats are STR, STA, AGI, DEX, WIS, INT, CHA."""
    strength, stamina, agility, dexterity, wisdom, intelligence, charisma = stats
    return struct.pack(
        "<20I",
        class_id,
        0,  # haircolor
        0,  # beardcolor
        0,  # beard
        gender,
        race,
        start_zone,
        0,  # hairstyle
        deity,
        strength,
        stamina,
        agility,
        dexterity,
        wisdom,
        intelligence,
        charisma,
        0,  # face
        0,  # eyecolor1
        0,  # eyecolor2
        0,  # tutorial
    )


@dataclass
class Played:
    """One character as the server described it. Stats stay 0 until the profile arrives."""

    name: str
    race: int = 1
    class_id: int = 1
    gender: int = 0
    level: int = 1
    deity: int = 0
    zone_id: int = 0
    points: int = 0
    hp: int = 0
    mana: int = 0
    strength: int = 0
    stamina: int = 0
    agility: int = 0
    dexterity: int = 0
    wisdom: int = 0
    intelligence: int = 0
    charisma: int = 0


def character_by_name(payload: bytes, name: str) -> Played | None:
    """The char-select slot whose name matches. Race, class, level, deity, and zone come from that slot."""
    want = name.lower()
    for slot in range(CHAR_SELECT_NAME_SLOTS):
        start = CHAR_SELECT_NAME_OFFSET + slot * 64
        if start + 64 > len(payload) or 1694 + slot >= len(payload):
            break
        found = payload[start : start + 64].split(b"\x00", 1)[0].decode("latin1")
        if found.lower() != want:
            continue
        race = struct.unpack_from("<I", payload, slot * 4)[0]
        deity = struct.unpack_from("<I", payload, 832 + slot * 4)[0]
        zone_id = struct.unpack_from("<I", payload, 964 + slot * 4)[0]
        return Played(
            found,
            race,
            payload[1004 + slot],
            payload[1664 + slot],
            payload[1694 + slot],
            deity,
            zone_id,
        )
    return None


def player_profile(payload: bytes) -> Played | None:
    """Titanium PlayerProfile_Struct. The seven stats start at 2236; the name is at 12940."""
    if len(payload) < 2264:
        return None
    gender, race, class_id = struct.unpack_from("<III", payload, 4)
    level = payload[20]
    deity = struct.unpack_from("<I", payload, 124)[0]
    points, mana, hp = struct.unpack_from("<III", payload, 2224)
    strength, stamina, charisma, dexterity, intelligence, agility, wisdom = struct.unpack_from("<IIIIIII", payload, 2236)
    name = ""
    if len(payload) >= 13004:
        name = payload[12940:13004].split(b"\x00", 1)[0].decode("latin1")
    return Played(
        name,
        race,
        class_id,
        gender,
        level,
        deity,
        0,
        points,
        hp,
        mana,
        strength,
        stamina,
        agility,
        dexterity,
        wisdom,
        intelligence,
        charisma,
    )


def character_select_names(payload: bytes) -> list[str]:
    names: list[str] = []
    base = CHAR_SELECT_NAME_OFFSET
    for slot in range(CHAR_SELECT_NAME_SLOTS):
        start = base + slot * 64
        if start + 64 > len(payload):
            break
        name = payload[start : start + 64].split(b"\x00", 1)[0].decode("latin1")
        if name:
            names.append(name)
    return names


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


def sign_extend(value: int, bits: int) -> int:
    value &= (1 << bits) - 1
    sign = 1 << (bits - 1)
    return value - (1 << bits) if value & sign else value


def eq19(word: int, shift: int) -> float:
    """GCC little-endian bitfield. The server stores FloatToEQ19 (value * 8)."""
    return sign_extend(word >> shift, 19) / 8.0


def pack_eq19(value: float) -> int:
    return int(round(value * 8.0)) & 0x7FFFF


SPAWN_SIZE = 385
DOOR_SIZE = 80


def server_position(payload: bytes) -> tuple[int, float, float, float]:
    """Titanium PlayerPositionUpdateServer_Struct. x/y/z are the EQ19 fields."""
    if len(payload) < 22:
        raise ValueError(f"server position update is {len(payload)} bytes")
    spawn_id = struct.unpack_from("<H", payload)[0]
    word_x, word_y, word_z = struct.unpack_from("<iii", payload, 2)
    return spawn_id, eq19(word_x, 10), eq19(word_y, 0), eq19(word_z, 0)


def pack_server_position(spawn_id: int, x: float, y: float, z: float) -> bytes:
    word_x = pack_eq19(x) << 10
    word_y = pack_eq19(y)
    word_z = pack_eq19(z)
    return struct.pack("<Hiiiii", spawn_id, word_x, word_y, word_z, 0, 0)


def spawn_position(blob: bytes) -> tuple[float, float, float]:
    word_x, word_y, word_z = struct.unpack_from("<iii", blob, 94)
    return eq19(word_x, 10), eq19(word_y, 0), eq19(word_z, 0)


def new_zone(payload: bytes) -> tuple[str, float, float, float]:
    """Short name at 64. Safe point is y, x, z starting at 492."""
    if len(payload) < 504:
        raise ValueError(f"OP_NewZone is {len(payload)} bytes")
    short = payload[64:96].split(b"\x00", 1)[0].decode("latin1")
    safe_y, safe_x, safe_z = struct.unpack_from("<fff", payload, 492)
    return short, safe_x, safe_y, safe_z


def request_zone_change(payload: bytes) -> tuple[int, float, float, float]:
    """OP_RequestClientZoneChange. Floats are y, x, z."""
    if len(payload) < 16:
        raise ValueError(f"zone change request is {len(payload)} bytes")
    zone_id = struct.unpack_from("<H", payload)[0]
    y, x, z = struct.unpack_from("<fff", payload, 4)
    return zone_id, x, y, z


def zone_change_position(payload: bytes) -> tuple[float, float, float]:
    """OP_ZoneChange floats are y, x, z at 68."""
    if len(payload) < 80:
        raise ValueError(f"OP_ZoneChange is {len(payload)} bytes")
    y, x, z = struct.unpack_from("<fff", payload, 68)
    return x, y, z


def _fixed_string(blob: bytes, offset: int, size: int) -> str:
    return blob[offset : offset + size].split(b"\x00", 1)[0].decode("latin1", errors="replace")


def parse_spawn(blob: bytes) -> tuple[int, str, int, int, int, float, float, float, int, int]:
    """One Spawn_Struct: id, name, npc flag, level, body, x, y, z, class, race."""
    if len(blob) < SPAWN_SIZE:
        raise ValueError(f"spawn is {len(blob)} bytes")
    name = _fixed_string(blob, 7, 64)
    npc = blob[83]
    level = blob[151]
    body = blob[335]
    class_id = blob[331]
    race_id = struct.unpack_from("<I", blob, 284)[0]
    spawn_id = struct.unpack_from("<I", blob, 340)[0]
    x, y, z = spawn_position(blob)
    return spawn_id, name, npc, level, body, x, y, z, class_id, race_id


def parse_door(blob: bytes) -> tuple[int, str, float, float, float, int]:
    """Door_Struct: door id, name, x, y, z, opentype. Floats on the wire are y, x, z."""
    if len(blob) < DOOR_SIZE:
        raise ValueError(f"door is {len(blob)} bytes")
    name = _fixed_string(blob, 0, 32)
    y, x, z = struct.unpack_from("<fff", blob, 32)
    return blob[60], name, x, y, z, blob[61]


def parse_ground(blob: bytes) -> tuple[int, str, float, float, float]:
    """Object_Struct. drop_id at 12, floats heading/z/x/y at 28, name at 44."""
    if len(blob) < 45:
        raise ValueError(f"ground spawn is {len(blob)} bytes")
    drop_id = struct.unpack_from("<I", blob, 12)[0]
    _heading, z, x, y = struct.unpack_from("<ffff", blob, 28)
    name, _end = cstring(blob, 44)
    return drop_id, name, x, y, z


def client_position(spawn_id: int, sequence: int, x: float, y: float, z: float) -> bytes:
    """PlayerPositionUpdateClient_Struct, 36 bytes. The decoder reads the float x/y/z."""
    return struct.pack("<HH4fI2fH2s", spawn_id, sequence & 0xFFFF, y, 0.0, 0.0, 0.0, 0, x, z, 0, b"\x00\x00")


def consider_faction(payload: bytes) -> int:
    if len(payload) < 12:
        raise ValueError(f"consider is {len(payload)} bytes")
    return struct.unpack_from("<I", payload, 8)[0]


def is_enemy_faction(faction: int) -> bool:
    """Faction 8 threatens and 9 scowls."""
    return faction in (8, 9)


ITEM_LOOT = 0x66
ITEM_TRADE = 0x67
ITEM_INVENTORY = 0x69
ITEM_SUMMON = 0x6A
HELD_ITEM_TYPES = (ITEM_LOOT, ITEM_TRADE, ITEM_INVENTORY, ITEM_SUMMON)


def _pipe_int(fields: list[str], index: int) -> int:
    if index >= len(fields):
        return 0
    text = fields[index].strip()
    if not text or not text.lstrip("-").isdigit():
        return 0
    return int(text)


def parse_item_packet(payload: bytes) -> tuple[int, int, str, str, int, int, int, int, int, int, int, int, int, int, int] | None:
    """Type, slot, name, IDFile, id, stack, slot bits, classes, races, AC, damage, req level, size, bag slots, bag size."""
    if len(payload) < 5:
        return None
    kind = struct.unpack_from("<I", payload)[0]
    text = payload[4:].split(b"\x00", 1)[0].decode("latin1", errors="replace")
    quote = text.find('"')
    if quote < 0:
        return None
    instance = text[:quote].split("|")
    static = text[quote + 1 :].split("|")
    if len(instance) < 3 or len(static) < 5 or not static[4].lstrip("-").isdigit():
        return None
    slot = int(instance[2]) if instance[2].lstrip("-").isdigit() else 0
    stack = int(instance[0]) if instance[0].lstrip("-").isdigit() else 1
    if stack <= 0:
        stack = 1
    # SerializeItem order after the quote: class, name, lore, IDFile, id, size at 8, slots at 9,
    # AC at 30, required level at 40, damage at 50, classes at 52, races at 53,
    # bag type at 96, bag slots at 97, bag size at 98.
    return (
        kind,
        slot,
        static[1],
        static[3],
        int(static[4]),
        stack,
        _pipe_int(static, 9),
        _pipe_int(static, 52),
        _pipe_int(static, 53),
        _pipe_int(static, 30),
        _pipe_int(static, 50),
        _pipe_int(static, 40),
        _pipe_int(static, 8),
        _pipe_int(static, 97),
        _pipe_int(static, 98),
    )
