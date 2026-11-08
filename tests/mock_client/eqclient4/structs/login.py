import struct
from dataclasses import dataclass, field

from eqclient4.structs.wire import (
    EQStruct,
    cstring,
    fixed,
    i8,
    i32,
    need,
    put_cstr,
    put_fixed,
    read_u32,
    u32,
)

LOGIN_BASE_SIZE = 10
LOGIN_INFO_SIZE = 464
NAME_APPROVAL_SIZE = 72
CHAR_CREATE_SIZE = 96
CHAR_SELECT_ENTRY = 275


@dataclass
class LoginBase(EQStruct):
    sequence: int = 0
    compressed: bool = False
    encrypt_type: int = 0
    unknown: int = 0

    def serialize(self) -> bytes:
        # loginserver/login_types.h:28 LoginBaseMessage
        return struct.pack(
            "<iBbi",
            i32(self.sequence),
            int(self.compressed) & 0xFF,
            i8(self.encrypt_type),
            i32(self.unknown),
        )

    @classmethod
    def deserialize(cls, data: bytes) -> LoginBase:
        need(data, LOGIN_BASE_SIZE, "login header")
        sequence, compressed, encrypt_type, unknown = struct.unpack_from("<iBbi", data)
        return cls(int(sequence), bool(compressed), int(encrypt_type), int(unknown))


@dataclass
class ServerEntry(EQStruct):
    ip: str
    server_type: int
    server_id: int
    name: str
    country: str
    language: str
    status: int
    player_count: int


@dataclass
class CharacterSlot(EQStruct):
    name: str
    race: int = 1
    class_id: int = 1
    gender: int = 0
    level: int = 1
    deity: int = 0
    zone_id: int = 0


@dataclass
class OP_SessionReady(EQStruct):
    value: int = 1

    def serialize(self) -> bytes:
        return u32(self.value)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_SessionReady:
        need(data, 4, "OP_SessionReady")
        return cls(read_u32(data))


@dataclass
class OP_ChatMessage(EQStruct):
    sequence: int = 0
    compressed: bool = False
    encrypt_type: int = 0
    unknown: int = 0
    success: bool = False
    error_id: int = 0
    message: str = ""
    extra: str = ""

    def serialize(self) -> bytes:
        head = LoginBase(
            self.sequence, self.compressed, self.encrypt_type, self.unknown
        ).serialize()
        # loginserver/login_types.h:35 LoginBaseReplyMessage
        reply = (
            bytes((int(self.success),))
            + struct.pack("<i", i32(self.error_id))
            + put_cstr(self.message)
            + put_cstr(self.extra)
        )
        return head + reply

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ChatMessage:
        if len(data) < LOGIN_BASE_SIZE:
            return cls()
        base = LoginBase.deserialize(data)
        offset = LOGIN_BASE_SIZE
        success = False
        error_id = 0
        message = ""
        extra = ""
        if offset < len(data):
            success = bool(data[offset])
            offset += 1
        if offset + 4 <= len(data):
            error_id = struct.unpack_from("<i", data, offset)[0]
            offset += 4
        try:
            message, offset = cstring(data, offset)
            extra, offset = cstring(data, offset)
        except ValueError:
            pass
        return cls(
            base.sequence,
            base.compressed,
            base.encrypt_type,
            base.unknown,
            success,
            int(error_id),
            message,
            extra,
        )


@dataclass
class OP_Login(EQStruct):
    username: str = ""
    password: str = ""
    sequence: int = 3
    compressed: bool = False
    encrypt_type: int = 2
    unknown: int = 0
    cipher: bytes = b""

    def serialize(self) -> bytes:
        head = LoginBase(
            self.sequence, self.compressed, self.encrypt_type, self.unknown
        ).serialize()
        if self.cipher:
            return head + self.cipher
        return head + put_cstr(self.username) + put_cstr(self.password)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_Login:
        base = LoginBase.deserialize(data)
        rest = data[LOGIN_BASE_SIZE:]
        pair = _credential_pair(rest)
        if pair is None:
            return cls(
                "", "", base.sequence, base.compressed, base.encrypt_type, base.unknown, rest
            )
        username, password = pair
        return cls(
            username, password, base.sequence, base.compressed, base.encrypt_type, base.unknown, b""
        )


def _credential_pair(rest: bytes) -> tuple[str, str] | None:
    try:
        username, offset = cstring(rest, 0)
        password, end = cstring(rest, offset)
    except ValueError:
        return None
    if end != len(rest) or not username.isascii() or not password.isascii():
        return None
    return username, password


@dataclass
class OP_LoginAccepted(EQStruct):
    success: bool = True
    error_id: int = 0
    message: str = ""
    unknown1: int = 0
    unknown2: int = 0
    account_id: int = 0
    key: str = ""
    failed_attempts: int = 0
    show_player_count: bool = False
    offer_min_days: int = 0
    offer_min_views: int = 0
    offer_cooldown_minutes: int = 0
    web_offer_number: int = 0
    web_offer_min_days: int = 0
    web_offer_min_views: int = 0
    web_offer_cooldown_minutes: int = 0
    username: str = ""

    def serialize(self) -> bytes:
        """Decrypted reply body. The login session encrypts this before send."""
        out = bytearray()
        out.append(int(self.success))
        # loginserver/login_types.h:35 LoginBaseReplyMessage
        out += struct.pack("<i", i32(self.error_id))
        out += put_cstr(self.message)
        out.append(self.unknown1 & 0xFF)
        out.append(self.unknown2 & 0xFF)
        # loginserver/login_types.h:48 PlayerLoginReply
        out += struct.pack("<i", i32(self.account_id))
        key = self.key.encode("latin1", errors="replace")[:10]
        out += key + b"\x00" * (11 - len(key))
        # loginserver/login_types.h:48 PlayerLoginReply
        out += struct.pack("<i", i32(self.failed_attempts))
        out.append(int(self.show_player_count))
        # loginserver/login_types.h:48 PlayerLoginReply
        out += struct.pack(
            "<7i",
            i32(self.offer_min_days),
            i32(self.offer_min_views),
            i32(self.offer_cooldown_minutes),
            i32(self.web_offer_number),
            i32(self.web_offer_min_days),
            i32(self.web_offer_min_views),
            i32(self.web_offer_cooldown_minutes),
        )
        out += put_cstr(self.username)
        # loginserver/login_types.h:48 PlayerLoginReply
        out += struct.pack("<B", 0)
        return bytes(out)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_LoginAccepted:
        """`data` is the decrypted reply, without the 10-byte login header."""
        need(data, 23, "OP_LoginAccepted")
        success = bool(data[0])
        error_id = struct.unpack_from("<i", data, 1)[0]
        message, offset = cstring(data, 5)
        unknown1 = data[offset] if offset < len(data) else 0
        unknown2 = data[offset + 1] if offset + 1 < len(data) else 0
        account_at = offset + 2
        need(data, account_at + 4 + 11, "OP_LoginAccepted")
        account_id = struct.unpack_from("<i", data, account_at)[0]
        key = (
            data[account_at + 4 : account_at + 15]
            .split(b"\x00", 1)[0]
            .decode("latin1", errors="replace")
        )
        cursor = account_at + 15
        failed = show = 0
        offers = [0, 0, 0, 0, 0, 0, 0]
        username = ""
        if cursor + 4 <= len(data):
            failed = struct.unpack_from("<i", data, cursor)[0]
            cursor += 4
        if cursor < len(data):
            show = data[cursor]
            cursor += 1
        if cursor + 28 <= len(data):
            offers = [int(value) for value in struct.unpack_from("<7i", data, cursor)]
            cursor += 28
        if cursor < len(data):
            try:
                username, _end = cstring(data, cursor)
            except ValueError:
                username = ""
        return cls(
            success,
            int(error_id),
            message,
            unknown1,
            unknown2,
            int(account_id),
            key,
            int(failed),
            bool(show),
            offers[0],
            offers[1],
            offers[2],
            offers[3],
            offers[4],
            offers[5],
            offers[6],
            username,
        )


@dataclass
class OP_ServerListRequest(EQStruct):
    sequence: int = 4

    def serialize(self) -> bytes:
        return u32(self.sequence)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ServerListRequest:
        need(data, 4, "OP_ServerListRequest")
        return cls(read_u32(data))


@dataclass
class OP_ServerListResponse(EQStruct):
    sequence: int = 4
    compressed: bool = False
    encrypt_type: int = 0
    unknown: int = 0
    success: bool = True
    error_id: int = 0
    message: str = ""
    servers: list[ServerEntry] = field(default_factory=list)

    def serialize(self) -> bytes:
        out = bytearray(
            LoginBase(self.sequence, self.compressed, self.encrypt_type, self.unknown).serialize()
        )
        out.append(int(self.success))
        # loginserver/login_types.h:35 LoginBaseReplyMessage
        out += struct.pack("<i", i32(self.error_id))
        out += put_cstr(self.message)
        # loginserver/login_types.h:83 ServerListReply
        out += struct.pack("<i", i32(len(self.servers)))
        for server in self.servers:
            out += put_cstr(server.ip)
            # loginserver/world_server.cpp:721 SerializeForClientServerList
            out += struct.pack("<iI", i32(server.server_type), server.server_id & 0xFFFFFFFF)
            out += put_cstr(server.name)
            out += put_cstr(server.country)
            out += put_cstr(server.language)
            # loginserver/world_server.cpp:749 SerializeForClientServerList
            out += struct.pack("<iI", i32(server.status), server.player_count & 0xFFFFFFFF)
        return bytes(out)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ServerListResponse:
        if len(data) < LOGIN_BASE_SIZE:
            return cls()
        base = LoginBase.deserialize(data)
        offset = LOGIN_BASE_SIZE
        success = bool(data[offset]) if offset < len(data) else False
        offset += 1
        error_id = struct.unpack_from("<i", data, offset)[0] if offset + 4 <= len(data) else 0
        offset += 4
        message = ""
        try:
            message, offset = cstring(data, offset)
        except ValueError:
            return cls(
                base.sequence,
                base.compressed,
                base.encrypt_type,
                base.unknown,
                success,
                int(error_id),
                message,
            )
        servers: list[ServerEntry] = []
        if offset + 4 > len(data):
            return cls(
                base.sequence,
                base.compressed,
                base.encrypt_type,
                base.unknown,
                success,
                int(error_id),
                message,
                servers,
            )
        count = struct.unpack_from("<i", data, offset)[0]
        offset += 4
        for _index in range(max(0, count)):
            try:
                ip, offset = cstring(data, offset)
            except ValueError:
                break
            if offset + 8 > len(data):
                break
            server_type, server_id = struct.unpack_from("<iI", data, offset)
            offset += 8
            try:
                name, offset = cstring(data, offset)
                country, offset = cstring(data, offset)
                language, offset = cstring(data, offset)
            except ValueError:
                break
            if offset + 8 > len(data):
                break
            status, players = struct.unpack_from("<iI", data, offset)
            offset += 8
            servers.append(
                ServerEntry(
                    ip,
                    int(server_type),
                    int(server_id),
                    name,
                    country,
                    language,
                    int(status),
                    int(players),
                )
            )
        return cls(
            base.sequence,
            base.compressed,
            base.encrypt_type,
            base.unknown,
            success,
            int(error_id),
            message,
            servers,
        )


@dataclass
class OP_PlayEverquestRequest(EQStruct):
    server_id: int
    sequence: int = 5
    compressed: bool = False
    encrypt_type: int = 0
    unknown: int = 0

    def serialize(self) -> bytes:
        return LoginBase(
            self.sequence, self.compressed, self.encrypt_type, self.unknown
        ).serialize() + u32(self.server_id)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_PlayEverquestRequest:
        need(data, LOGIN_BASE_SIZE + 4, "OP_PlayEverquestRequest")
        base = LoginBase.deserialize(data)
        return cls(
            read_u32(data, LOGIN_BASE_SIZE),
            base.sequence,
            base.compressed,
            base.encrypt_type,
            base.unknown,
        )


@dataclass
class OP_PlayEverquestResponse(EQStruct):
    sequence: int = 0
    compressed: bool = False
    encrypt_type: int = 0
    unknown: int = 0
    success: bool = False
    error_id: int = 0
    message: str = ""
    server_id: int = 0

    def serialize(self) -> bytes:
        out = bytearray(
            LoginBase(self.sequence, self.compressed, self.encrypt_type, self.unknown).serialize()
        )
        out.append(int(self.success))
        # loginserver/login_types.h:35 LoginBaseReplyMessage
        out += struct.pack("<i", i32(self.error_id))
        out += put_cstr(self.message)
        out += u32(self.server_id)
        return bytes(out)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_PlayEverquestResponse:
        if len(data) < LOGIN_BASE_SIZE:
            return cls()
        base = LoginBase.deserialize(data)
        offset = LOGIN_BASE_SIZE
        success = bool(data[offset]) if offset < len(data) else False
        offset += 1
        error_id = struct.unpack_from("<i", data, offset)[0] if offset + 4 <= len(data) else 0
        offset += 4
        message = ""
        try:
            message, offset = cstring(data, offset)
        except ValueError:
            offset = len(data)
        server_id = read_u32(data, offset) if offset + 4 <= len(data) else 0
        return cls(
            base.sequence,
            base.compressed,
            base.encrypt_type,
            base.unknown,
            success,
            int(error_id),
            message,
            int(server_id),
        )


@dataclass
class OP_SendLoginInfo(EQStruct):
    account_id: int
    key: str
    zoning: bool = False

    def serialize(self) -> bytes:
        packet = bytearray(LOGIN_INFO_SIZE)
        creds = f"{self.account_id}\x00{self.key}".encode("latin1", errors="replace")
        packet[: min(len(creds), 64)] = creds[:64]
        if self.zoning:
            packet[188] = 1
        return bytes(packet)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_SendLoginInfo:
        need(data, 64, "OP_SendLoginInfo")
        parts = data[:64].split(b"\x00")
        account_id = int(parts[0]) if parts and parts[0].isdigit() else 0
        key = parts[1].decode("latin1", errors="replace") if len(parts) > 1 else ""
        zoning = len(data) > 188 and data[188] == 1
        return cls(account_id, key, zoning)


@dataclass
class OP_SendCharInfo(EQStruct):
    slots: list[CharacterSlot] = field(default_factory=list)

    def serialize(self) -> bytes:
        # common/patches/rof2_structs.h:276 CharacterSelect_Struct
        out = bytearray(struct.pack("<I", len(self.slots) & 0xFFFFFFFF))
        for slot in self.slots:
            out += put_cstr(slot.name)
            rest = bytearray(CHAR_SELECT_ENTRY - 1)
            rest[0] = slot.class_id & 0xFF
            # common/patches/rof2_structs.h:241 CharacterSelectEntry_Struct Race. rest starts after Name[1].
            struct.pack_into("<I", rest, 1, slot.race & 0xFFFFFFFF)
            rest[5] = slot.level & 0xFF
            # common/patches/rof2_structs.h:245 CharacterSelectEntry_Struct Zone
            struct.pack_into("<H", rest, 11, slot.zone_id & 0xFFFF)
            rest[15] = slot.gender & 0xFF
            # common/patches/rof2_structs.h:254 CharacterSelectEntry_Struct Deity
            struct.pack_into("<I", rest, 243, slot.deity & 0xFFFFFFFF)
            out += rest
        return bytes(out)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_SendCharInfo:
        if len(data) < 4:
            return cls([])
        count = read_u32(data)
        offset = 4
        slots: list[CharacterSlot] = []
        for _index in range(count):
            try:
                name, end = cstring(data, offset)
            except ValueError:
                break
            base = end - 1
            if base + CHAR_SELECT_ENTRY > len(data):
                break
            slots.append(
                CharacterSlot(
                    name,
                    read_u32(data, base + 2),
                    data[base + 1],
                    data[base + 16],
                    data[base + 6],
                    read_u32(data, base + 244),
                    struct.unpack_from("<H", data, base + 12)[0],
                )
            )
            offset = base + CHAR_SELECT_ENTRY
        return cls(slots)


@dataclass
class OP_ApproveName(EQStruct):
    name: str = ""
    race: int = 0
    class_id: int = 0
    approved: bool | None = None

    def serialize(self) -> bytes:
        if self.name:
            packet = bytearray(NAME_APPROVAL_SIZE)
            put_fixed(packet, 0, self.name, 64)
            # common/eq_packet_structs.h:646 NameApproval_Struct
            struct.pack_into(
                "<II",
                packet,
                64,
                self.race & 0xFFFFFFFF,
                self.class_id & 0xFFFFFFFF,
            )
            return bytes(packet)
        return bytes((1 if self.approved else 0,))

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ApproveName:
        if len(data) >= 64:
            race = class_id = 0
            if len(data) >= NAME_APPROVAL_SIZE:
                race, class_id = struct.unpack_from("<II", data, 64)
            return cls(fixed(data, 0, 64), int(race), int(class_id), None)
        if not data:
            raise ValueError("OP_ApproveName is empty")
        return cls(approved=data[0] == 1)


@dataclass
class OP_CharacterCreate(EQStruct):
    class_id: int
    race: int
    gender: int
    deity: int
    start_zone: int
    strength: int
    stamina: int
    agility: int
    dexterity: int
    wisdom: int
    intelligence: int
    charisma: int
    hair_color: int = 0
    beard_color: int = 0
    beard: int = 0
    hair_style: int = 0
    face: int = 0
    eye_color1: int = 0
    eye_color2: int = 0
    tutorial: int = 0

    def serialize(self) -> bytes:
        # common/patches/rof2_structs.h:870 CharCreate_Struct
        return struct.pack(
            "<24I",
            self.gender & 0xFFFFFFFF,
            self.race & 0xFFFFFFFF,
            self.class_id & 0xFFFFFFFF,
            self.deity & 0xFFFFFFFF,
            self.start_zone & 0xFFFFFFFF,
            self.hair_color & 0xFFFFFFFF,
            self.beard & 0xFFFFFFFF,
            self.beard_color & 0xFFFFFFFF,
            self.hair_style & 0xFFFFFFFF,
            self.face & 0xFFFFFFFF,
            self.eye_color1 & 0xFFFFFFFF,
            self.eye_color2 & 0xFFFFFFFF,
            0,
            0,
            0,
            self.strength & 0xFFFFFFFF,
            self.stamina & 0xFFFFFFFF,
            self.agility & 0xFFFFFFFF,
            self.dexterity & 0xFFFFFFFF,
            self.wisdom & 0xFFFFFFFF,
            self.intelligence & 0xFFFFFFFF,
            self.charisma & 0xFFFFFFFF,
            self.tutorial & 0xFFFFFFFF,
            0,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_CharacterCreate:
        need(data, CHAR_CREATE_SIZE, "OP_CharacterCreate")
        (
            gender,
            race,
            class_id,
            deity,
            start_zone,
            hair_color,
            beard,
            beard_color,
            hair_style,
            face,
            eye_color1,
            eye_color2,
            _heritage,
            _tattoo,
            _details,
            strength,
            stamina,
            agility,
            dexterity,
            wisdom,
            intelligence,
            charisma,
            tutorial,
            _unknown,
        ) = struct.unpack_from("<24I", data)
        return cls(
            int(class_id),
            int(race),
            int(gender),
            int(deity),
            int(start_zone),
            int(strength),
            int(stamina),
            int(agility),
            int(dexterity),
            int(wisdom),
            int(intelligence),
            int(charisma),
            int(hair_color),
            int(beard_color),
            int(beard),
            int(hair_style),
            int(face),
            int(eye_color1),
            int(eye_color2),
            int(tutorial),
        )


import struct
from dataclasses import dataclass, field


@dataclass
class RaceClassAllocation:
    Index: int
    BaseStats: tuple[int, ...]
    DefaultPointAllocation: tuple[int, ...]

    FORMAT = "<15I"
    SIZE = struct.calcsize(FORMAT)

    def serialize(self) -> bytes:
        if len(self.BaseStats) != 7 or len(self.DefaultPointAllocation) != 7:
            raise ValueError("Expected 7 stats and 7 allocations")
        return struct.pack(
            self.FORMAT,
            self.Index,
            *self.BaseStats,
            *self.DefaultPointAllocation,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> "RaceClassAllocation":
        values = struct.unpack(cls.FORMAT, data)
        return cls(
            Index=values[0],
            BaseStats=values[1:8],
            DefaultPointAllocation=values[8:15],
        )


@dataclass
class RaceClassCombos:
    ExpansionRequired: int
    Race: int
    Class: int
    Deity: int
    AllocationIndex: int
    Zone: int

    FORMAT = "<6I"
    SIZE = struct.calcsize(FORMAT)

    def serialize(self) -> bytes:
        return struct.pack(
            self.FORMAT,
            self.ExpansionRequired,
            self.Race,
            self.Class,
            self.Deity,
            self.AllocationIndex,
            self.Zone,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> "RaceClassCombos":
        return cls(*struct.unpack(cls.FORMAT, data))


@dataclass
class OP_CharacterCreateRequest(EQStruct):
    unknown: int = 0
    allocations: list[RaceClassAllocation] = field(default_factory=list)
    combos: list[RaceClassCombos] = field(default_factory=list)

    def serialize(self) -> bytes:
        # Empty instance represents the client request
        if not self.allocations and not self.combos:
            return b""
        data = bytearray()
        data += struct.pack("<BI", self.unknown, len(self.allocations))

        for allocation in self.allocations:
            data += allocation.serialize()

        data += struct.pack("<I", len(self.combos))

        for combo in self.combos:
            data += combo.serialize()

        return bytes(data)

    @classmethod
    def deserialize(cls, data: bytes) -> "OP_CharacterCreateRequest":
        if not data:
            return cls()

        if len(data) < 9:
            raise ValueError("Packet too short")

        unknown, allocation_count = struct.unpack_from("<BI", data, 0)
        offset = 5

        required = offset + allocation_count * RaceClassAllocation.SIZE + 4
        if len(data) < required:
            raise ValueError("Truncated allocation data")

        allocations = []
        for _ in range(allocation_count):
            size = RaceClassAllocation.SIZE
            allocations.append(RaceClassAllocation.deserialize(data[offset : offset + size]))
            offset += size

        (combo_count,) = struct.unpack_from("<I", data, offset)
        offset += 4

        expected = offset + combo_count * RaceClassCombos.SIZE
        if len(data) != expected:
            raise ValueError(f"Expected {expected} bytes, got {len(data)}")

        combos = []
        for _ in range(combo_count):
            size = RaceClassCombos.SIZE
            combos.append(RaceClassCombos.deserialize(data[offset : offset + size]))
            offset += size

        return cls(
            unknown=unknown,
            allocations=allocations,
            combos=combos,
        )
