"""Pack and unpack the few Titanium structs this client sends and reads."""

from __future__ import annotations

import re
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


def login_info(account_id: int, key: str, *, zoning: bool = False) -> bytes:
    packet = bytearray(LOGIN_INFO_SIZE)
    creds = f"{account_id}\x00{key}".encode("latin1")
    packet[: min(len(creds), 64)] = creds[:64]
    # LoginInfo.zoning at 188 — world skips char select and Clearance(1)s into the saved zone.
    if zoning:
        packet[188] = 1
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
    home_zone_id: int = 0
    platinum: int = 0
    gold: int = 0
    silver: int = 0
    copper: int = 0
    coin_known: bool = False


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
    home_zone_id = struct.unpack_from("<I", payload, 24)[0]
    level = payload[20]
    deity = struct.unpack_from("<I", payload, 124)[0]
    points, mana, hp = struct.unpack_from("<III", payload, 2224)
    strength, stamina, charisma, dexterity, intelligence, agility, wisdom = struct.unpack_from("<IIIIIII", payload, 2236)
    name = ""
    if len(payload) >= 13004:
        name = payload[12940:13004].split(b"\x00", 1)[0].decode("latin1")
    # Header comment puts platinum at 4720. This client's spell book is 272 bytes earlier
    # (2584 → 2312), so the purse is at 4448.
    platinum = gold = silver = copper = 0
    coin_known = False
    if len(payload) >= 4464:
        platinum, gold, silver, copper = struct.unpack_from("<IIII", payload, 4448)
        coin_known = True
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
        home_zone_id,
        platinum,
        gold,
        silver,
        copper,
        coin_known,
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


def channel_message(
    sender: str,
    text: str,
    channel: int = SAY_CHANNEL,
    target: str = "",
    *,
    language: int = 0,
    lang_skill: int = 100,
) -> bytes:
    """ChannelMessage_Struct. language 0 is Common; group chat (2) trains foreign tongues."""
    packet = bytearray(CHANNEL_MESSAGE_SIZE)
    encoded_target = target.encode("latin1")[:63]
    packet[: len(encoded_target)] = encoded_target
    encoded_sender = sender.encode("latin1")[:63]
    packet[64 : 64 + len(encoded_sender)] = encoded_sender
    struct.pack_into(
        "<IIIII",
        packet,
        128,
        language & 0xFF,
        channel & 0xFFFFFFFF,
        0,
        0,
        max(0, min(100, int(lang_skill))),
    )
    return bytes(packet) + text.encode("latin1") + b"\x00"


def channel_number(payload: bytes) -> int:
    """Tell is 7 and group is 2. Say, which we already send, is 8."""
    if len(payload) < 136:
        return 0
    return struct.unpack_from("<I", payload, 132)[0]


def channel_message_text(payload: bytes) -> str:
    if len(payload) <= CHANNEL_MESSAGE_SIZE:
        return ""
    return payload[CHANNEL_MESSAGE_SIZE:].split(b"\x00", 1)[0].decode("latin1", errors="replace")


_SAYLINK = re.compile(r"\x12.{45}([^\x12]+?)\x12")


def consume_packet(slot: int, kind: int) -> bytes:
    """kind 1 is food and 2 is water. The auto field is the right-click value."""
    return struct.pack("<II4sB3s", slot, 0xFFFFFFFF, b"\x00" * 4, kind, b"\x00" * 3)


def memorize_packet(slot: int, spell_id: int, scribing: int) -> bytes:
    """scribing 0 writes the book, 1 memorizes a gem, 2 forgets it."""
    return struct.pack("<IIII", slot, spell_id, scribing, 0)


def cast_packet(slot: int, spell_id: int, target_id: int) -> bytes:
    """Titanium CastSpell. Inventory slot 0xFFFF is a gem, not a clicky."""
    return struct.pack("<IIII4s", slot, spell_id, 0xFFFF, target_id, b"\x00" * 4)


def group_invite(invitee: str, inviter: str) -> bytes:
    return _two_names(invitee, inviter)


def group_follow(member: str, leader: str) -> bytes:
    return _two_names(member, leader)


def _two_names(first: str, second: str) -> bytes:
    packet = bytearray(128)
    packet[: len(first.encode("latin1")[:63])] = first.encode("latin1")[:63]
    packet[64 : 64 + len(second.encode("latin1")[:63])] = second.encode("latin1")[:63]
    return bytes(packet)


def who_request(name: str) -> bytes:
    packet = bytearray(152)
    packet[: len(name.encode("latin1")[:63])] = name.encode("latin1")[:63]
    struct.pack_into("<6I", packet, 64, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0, 0)
    return bytes(packet)


def popup_message(payload: bytes) -> tuple[str, str, int]:
    """Titanium OP_OnLevelMessage: title, text, and the id the OK button sends back."""
    if len(payload) < 128:
        return "", "", 0
    title = payload[:128].split(b"\x00", 1)[0].decode("latin1", errors="replace")
    text = payload[128:128 + 4096].split(b"\x00", 1)[0].decode("latin1", errors="replace")
    popup_id = struct.unpack_from("<I", payload, 4232)[0] if len(payload) >= 4236 else 0
    return title, popup_plain(text), popup_id


def popup_plain(text: str) -> str:
    text = re.sub(r"<br\s*/?>", " ", text, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", "", text)
    return " ".join(text.split())


def popup_response(popup_id: int) -> bytes:
    """OK on that window. The server reads the popup id from the second field."""
    return struct.pack("<II", 0, popup_id)


def saylink_words(text: str) -> list[str]:
    """The visible words inside Titanium saylinks. Those are what you say back."""
    words: list[str] = []
    for match in _SAYLINK.finditer(text):
        word = match.group(1).strip()
        if word and word.lower() not in {item.lower() for item in words}:
            words.append(word)
    return words


def saylink_plain(text: str) -> str:
    """Replace \x12 item-link blobs with their visible names for chat logs."""
    if "\x12" not in text:
        return text
    return _SAYLINK.sub(lambda m: m.group(1), text)


def channel_sender(payload: bytes) -> str:
    if len(payload) < 128:
        return ""
    return payload[64:128].split(b"\x00", 1)[0].decode("latin1", errors="replace")


def movement_history(x: float, y: float, z: float, timestamp: int) -> bytes:
    """One OP_FloatListThing entry. The zone wants this before position updates.

    The packed struct is Y, X, Z, then a type byte and a timestamp. Type 0 is a
    normal sample; a teleport type is what the warp check looks for.
    """
    return struct.pack("<fffBI", y, x, z, 0, timestamp & 0xFFFFFFFF)


def special_message(payload: bytes) -> tuple[str, str]:
    """Speaker and text from the Titanium OP_SpecialMesg encode."""
    if len(payload) < 11:
        return "", ""
    offset = 3 + 4 + 4
    name, offset = cstring(payload, offset)
    offset += 12
    if offset >= len(payload):
        return name, ""
    message, _end = cstring(payload, offset)
    return name, message


def special_message_text(payload: bytes) -> str:
    """Client::Message layout after the Titanium OP_SpecialMesg encode."""
    return special_message(payload)[1]


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


def new_zone_id(payload: bytes) -> int:
    """Zone id at the end of OP_NewZone. Short packets from tests have none."""
    if len(payload) < 686:
        return 0
    return struct.unpack_from("<H", payload, 684)[0]


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
    return zone_change(payload)[2:5]


def zone_change(payload: bytes) -> tuple[int, int, float, float, float, int]:
    """OP_ZoneChange: zone_id, instance_id, x, y, z, success.

    success==1 with a different zone_id means disconnect and re-enter through world.
    success==1 with the same zone_id is cancel / in-zone MovePC.
    """
    if len(payload) < 88:
        raise ValueError(f"OP_ZoneChange is {len(payload)} bytes")
    zone_id, instance_id = struct.unpack_from("<HH", payload, 64)
    y, x, z = struct.unpack_from("<fff", payload, 68)
    success = struct.unpack_from("<i", payload, 84)[0]
    return zone_id, instance_id, x, y, z, success


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


def find_person_request(entity_id: int, x: float, y: float, z: float) -> bytes:
    """FindPersonRequest_Struct. The point is stored y, x, z, and the id is the spawn."""
    return struct.pack("<Ifff", entity_id, y, x, z)


def find_destination(payload: bytes) -> tuple[float, float, float] | None:
    """NPC position from FindPersonResult_Struct.dest (y, x, z floats)."""
    if len(payload) < 12:
        return None
    py, px, pz = struct.unpack_from("<fff", payload, 0)
    return (px, py, pz)


def find_path(payload: bytes) -> list[tuple[float, float, float]]:
    """Points from OP_FindPersonReply.

    The first 12 bytes are the destination. The path follows, each point y, x, z,
    and the server repeats the destination at the end.
    """
    if len(payload) < 24:
        return []
    points: list[tuple[float, float, float]] = []
    offset = 12
    while offset + 12 <= len(payload):
        py, px, pz = struct.unpack_from("<fff", payload, offset)
        points.append((px, py, pz))
        offset += 12
    if len(points) >= 2 and _same_point(points[-1], points[-2]):
        points.pop()
    return points


def guide_from(
    points: list[tuple[float, float, float]],
    here: tuple[float, float, float],
) -> list[tuple[float, float, float]]:
    """The glowing line continues after the point he is already standing on."""
    if not points:
        return []
    nearest = min(range(len(points)), key=lambda index: _span(points[index], here))
    route = [point for point in points[nearest + 1 :] if _span(point, here) > 1.0]
    if route:
        return route
    if _span(points[-1], here) > 1.0:
        return [points[-1]]
    return []


def _same_point(a: tuple[float, float, float], b: tuple[float, float, float]) -> bool:
    return _span(a, b) <= 0.1


def _span(a: tuple[float, float, float], b: tuple[float, float, float]) -> float:
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


def eq_heading(x1: float, y1: float, x2: float, y2: float) -> int:
    """0-512 heading, the same quadrants the server uses for IsFacingMob."""
    import math

    x_diff = abs(x1 - x2)
    y_diff = abs(y1 - y2) or 1e-9
    angle = math.atan2(x_diff, y_diff) * 180.0 * 0.3183099014828645
    if y1 >= y2:
        degrees = (90.0 - angle + 90.0) if x2 >= x1 else (angle + 180.0)
    elif y1 > y2 or x2 > x1:
        degrees = angle
    else:
        degrees = 90.0 - angle + 270.0
    return int(degrees * 511.5 * 0.0027777778) & 0xFFF


def client_position(
    spawn_id: int,
    sequence: int,
    x: float,
    y: float,
    z: float,
    ox: float | None = None,
    oy: float | None = None,
    oz: float | None = None,
    heading: int = 0,
    animation: int = 0,
) -> bytes:
    """PlayerPositionUpdateClient_Struct, 36 bytes.

    Spawn id 0 is this client. A nonzero id that is not the player's is handled
    as a boat and the player's position stays put. Horizontal deltas are the
    step. Vertical delta stays 0 so a watcher does not play a jump.

    `animation` is SpeedRun (server TODO comment), not a 1=walk/2=run enum:
    0 stand, ~12 walk, ~28 default run (client runspeed 0.7 → base_runspeed 28).
    """
    dx = 0.0 if ox is None else x - ox
    dy = 0.0 if oy is None else y - oy
    dz = 0.0
    # Titanium: animation:10 | delta_heading:10 | padding:12 (padding mostly 1).
    anim_word = (animation & 0x3FF) | (1 << 20)
    return struct.pack(
        "<HH4fI2fH2s",
        spawn_id & 0xFFFF,
        sequence & 0xFFFF,
        y,
        dz,
        dx,
        dy,
        anim_word,
        x,
        z,
        (heading * 4) & 0xFFF,
        b"\x00\x00",
    )


def consider_faction(payload: bytes) -> int:
    if len(payload) < 12:
        raise ValueError(f"consider is {len(payload)} bytes")
    raw = struct.unpack_from("<I", payload, 8)[0]
    # Titanium swaps 6↔9 and 7↔8 before send; undo so stored values match server truth.
    if raw == 6:
        return 9
    if raw == 7:
        return 8
    if raw == 9:
        return 6
    if raw == 8:
        return 7
    return raw


def is_enemy_faction(faction: int) -> bool:
    """Threatening (8) and scowling (9)."""
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


def parse_inventory(payload: bytes) -> list[tuple[int, int, str, str, int, int, int, int, int, int, int, int, int, int, int]]:
    """OP_CharInventory is the login list: null-terminated items, with no type prefix."""
    found = []
    for blob in payload.split(b"\x00"):
        if b'"' not in blob:
            continue
        parsed = parse_item_packet(struct.pack("<I", ITEM_INVENTORY) + blob)
        if parsed is not None:
            found.append(parsed)
    return found


def profile_spells(payload: bytes) -> tuple[dict[int, int], dict[int, int]]:
    """Spell book at 2312, four hundred ids. Gems at 4360. 0 and 0xffffffff are empty."""
    book: dict[int, int] = {}
    gems: dict[int, int] = {}
    if len(payload) >= 2312 + 400 * 4:
        for index, spell in enumerate(struct.unpack_from("<400I", payload, 2312)):
            if spell not in (0, 0xFFFFFFFF):
                book[index] = spell
    if len(payload) >= 4360 + 12 * 4:
        for index, spell in enumerate(struct.unpack_from("<12I", payload, 4360)):
            if spell not in (0, 0xFFFFFFFF):
                gems[index] = spell
    return book, gems


def parse_item_packet(payload: bytes) -> tuple[int, int, str, str, int, int, int, int, int, int, int, int, int, int, int, int, int] | None:
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
    # item type at 56, bag type at 96, bag slots at 97, bag size at 98,
    # scroll effect at 154. That effect is the spell id a scroll scribes.
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
        _pipe_int(static, 56),
        _pipe_int(static, 154),
    )
