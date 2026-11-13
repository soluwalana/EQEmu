import struct
from dataclasses import dataclass, field

from eqclient4.structs.wire import (
    EQStruct,
    advance,
    bitfield,
    bitword,
    cstring,
    i16,
    i32,
    need,
    pack_eq19,
    put_cstr,
    read_u32,
)

_PLAYER_RACES = {128, 130, 330, 522}


def _playable_spawn(npc: int, race: int) -> bool:
    return npc == 0 or race <= 12 or race in _PLAYER_RACES


def _kept_name(text: str) -> str:
    """A RoF2 last name. Anything that is not a name stays off the hail."""
    spoken = " ".join((text or "").replace("_", " ").split())
    if spoken and all(ch.isalpha() or ch in " '-" for ch in spoken):
        return spoken
    return ""


def _pack_spawn(spawn: Spawn) -> bytes:
    """One RoF2 spawn body. The position words are the 19-bit coordinates."""
    out = bytearray()
    out += put_cstr(spawn.name)
    # common/patches/rof2.cpp:4664
    out += struct.pack(
        "<IBfB", spawn.spawn_id & 0xFFFFFFFF, spawn.level & 0xFF, 0.0, spawn.npc & 0xFF
    )
    other = (0x10 if spawn.title else 0) | (0x20 if spawn.suffix else 0)
    out += bytes(4) + bytes((other,))
    # common/patches/rof2.cpp:4735 unknown3
    out += struct.pack("<ff", -1.0, 0.0)
    # common/patches/rof2.cpp:4771
    out += struct.pack("<BI", 1, spawn.body & 0xFFFFFFFF)
    out += b"\x00" * 23
    # common/patches/rof2.cpp:4795 size, face, walkspeed, runspeed, race
    out += struct.pack("<fBffI", 0.0, 0, 0.0, 0.0, spawn.race & 0xFFFFFFFF)
    # common/patches/rof2.cpp:4802
    out += struct.pack("<BI", 0, 0)
    # common/patches/rof2.cpp:4806
    out += struct.pack("<II", 0xFFFFFFFF, 0) if spawn.npc else struct.pack("<II", 0, 0)
    out += bytes((spawn.class_id & 0xFF, 0, 0, 0, 0))
    out += put_cstr(spawn.last_name)
    # common/patches/rof2.cpp:4835 aatitle
    out += struct.pack("<IBBIB", 0, 0, 0, 0, 0)
    out += b"\x00" * 16
    # common/patches/rof2.cpp:4846 WeaponEquip
    out += struct.pack("<II", 0xFFFFFFFF, 0xFFFFFFFF)
    out += b"\x00" * (216 if _playable_spawn(spawn.npc, spawn.race) else 60)
    # common/patches/rof2.cpp:4893
    out += struct.pack(
        "<IIIII",
        bitword((0, 12), (pack_eq19(spawn.y), 19), (0, 1)),
        0,
        bitword((pack_eq19(spawn.x), 19), (0, 12), (0, 1)),
        bitword((0, 10), (pack_eq19(spawn.z), 19), (0, 3)),
        0,
    )
    if spawn.title:
        out += put_cstr(spawn.title)

    if spawn.suffix:
        out += put_cstr(spawn.suffix)

    out += bytes(8)  # unknown IDs
    out += b"\x00"  # IsMercenary
    out += b"0000000000000000\x00"  # RealEstateItemGuid
    out += struct.pack("<II", 0xFFFFFFFF, 0xFFFFFFFF)
    out += bytes(29)
    return bytes(out)


def _read_spawn(data: bytes, offset: int) -> tuple[Spawn, int]:
    """Walk the RoF2 OP_ZoneSpawns encode. One spawn, starting at offset."""

    name, offset = cstring(data, offset)
    offset = advance(data, offset, 10, "spawn")
    spawn_id, level, _bounds, npc = struct.unpack_from("<IBfB", data, offset - 10)
    offset = advance(data, offset, 5, "spawn")
    other = data[offset - 1]
    has_title = bool(other & 0x10)
    has_suffix = bool(other & 0x20)
    offset = advance(data, offset, 8, "spawn")
    if other & 0xE1 == 0xE1 or other & 0x04:
        for _index in range(3):
            _text, offset = cstring(data, offset)
        offset = advance(data, offset, 53, "spawn")
    if other & 0xE1 == 0xE1:
        offset = advance(data, offset, 1, "spawn")
        body = 0
    else:
        offset = advance(data, offset, 5, "spawn")
        body = read_u32(data, offset - 4)
    offset = advance(data, offset, 23, "spawn")
    offset = advance(data, offset, 17, "spawn")
    _size, _face, _walk, _run, race = struct.unpack_from("<fBffI", data, offset - 17)
    offset = advance(data, offset, 5, "spawn")
    offset = advance(data, offset, 8, "spawn")
    class_id = data[offset]
    offset = advance(data, offset, 5, "spawn")
    last_name, offset = cstring(data, offset)
    offset = advance(data, offset, 11, "spawn")
    offset = advance(data, offset, 24, "spawn")
    offset = advance(data, offset, 216 if _playable_spawn(int(npc), int(race)) else 60, "spawn")
    offset = advance(data, offset, 20, "spawn")
    word_y, _delta, word_x, word_z, _anim = struct.unpack_from("<IIIII", data, offset - 20)
    # RoF2 spawn data continues after the 20-byte position block.
    # Titles and suffixes are optional C strings.
    _title = ""
    _suffix = ""
    if has_title:
        _title, offset = cstring(data, offset)

    if has_suffix:
        _suffix, offset = cstring(data, offset)
    offset = advance(data, offset, 63, "spawn trailer")

    return (
        Spawn(
            int(spawn_id),
            name,
            int(npc),
            int(level),
            int(body),
            bitfield(word_x, 0, 19) / 8.0,
            bitfield(word_y, 12, 19) / 8.0,
            bitfield(word_z, 10, 19) / 8.0,
            int(class_id),
            int(race),
            _kept_name(last_name),
            _title,
            _suffix,
        ),
        offset,
    )


@dataclass
class Spawn(EQStruct):
    spawn_id: int
    name: str
    npc: int
    level: int
    body: int
    x: float
    y: float
    z: float
    class_id: int
    race: int
    last_name: str = ""
    title: str = ""
    suffix: str = ""

    def serialize(self) -> bytes:
        return _pack_spawn(self)

    @classmethod
    def deserialize(cls, data: bytes) -> Spawn:
        spawn, _offset = _read_spawn(data, 0)
        return spawn


def _pack_server_position(
    spawn_id: int,
    x: float,
    y: float,
    z: float,
    heading: float = 0,
    vehicle_id: int = 0,
    animation: int = 0,
    delta_x: float = 0.0,
    delta_y: float = 0.0,
    delta_z: float = 0.0,
    delta_heading: float = 0.0,
) -> bytes:
    """RoF2 PlayerPositionUpdateServer_Struct. 24 bytes."""
    return struct.pack(
        "<HHIIIII",
        spawn_id & 0xFFFF,
        vehicle_id & 0xFFFF,
        bitword(
            (0, 12),
            (pack_eq19(y), 19),
            (0, 1),
        ),
        bitword(
            (int(delta_z * 64), 13),
            (int(delta_x * 64), 13),
            (0, 6),
        ),
        bitword(
            (pack_eq19(x), 19),
            (int(heading * 4), 12),
            (0, 1),
        ),
        bitword(
            (int(delta_heading * 20), 10),
            (pack_eq19(z), 19),
            (0, 3),
        ),
        bitword(
            (animation, 10),
            (int(delta_y * 64), 13),
            (0, 9),
        ),
    )


def _read_server_position(data: bytes) -> "OP_ClientUpdate":
    need(data, 24, "server position")

    (
        spawn_id,
        vehicle_id,
        word_y,
        word_delta,
        word_x,
        word_z,
        word_anim,
    ) = struct.unpack_from("<HHIIIII", data)

    return OP_ClientUpdate(
        spawn_id=spawn_id,
        x=bitfield(word_x, 0, 19) / 8.0,
        y=bitfield(word_y, 12, 19) / 8.0,
        z=bitfield(word_z, 10, 19) / 8.0,
        heading=bitfield(word_x, 19, 12, signed=False) / 4.0,
        animation=bitfield(word_anim, 0, 10),
        delta_x=bitfield(word_delta, 13, 13) / 64.0,
        delta_y=bitfield(word_anim, 10, 13) / 64.0,
        delta_z=bitfield(word_delta, 0, 13) / 64.0,
        server=True,
        vehicle_id=vehicle_id,
        delta_heading=bitfield(word_z, 0, 10) / 20.0,
    )


@dataclass
class OP_ClientUpdate(EQStruct):
    spawn_id: int
    x: float
    y: float
    z: float

    sequence: int = 0
    heading: float = 0
    animation: int = 0

    delta_x: float = 0.0
    delta_y: float = 0.0
    delta_z: float = 0.0

    server: bool = False

    # Additional movement fields
    vehicle_id: int = 0
    delta_heading: float = 0.0

    # Client-only placeholder bytes at offset 6
    unknown06: bytes = b"\x00\x00\x00\x00"

    def serialize(self) -> bytes:
        if self.server:
            return _pack_server_position(
                self.spawn_id,
                self.x,
                self.y,
                self.z,
                self.heading,
                vehicle_id=self.vehicle_id,
                animation=self.animation,
                delta_x=self.delta_x,
                delta_y=self.delta_y,
                delta_z=self.delta_z,
                delta_heading=self.delta_heading,
            )

        return struct.pack(
            "<HHH4sfIffffIfI",
            self.sequence & 0xFFFF,
            self.spawn_id & 0xFFFF,
            self.vehicle_id & 0xFFFF,
            self.unknown06,
            self.delta_x,
            int(self.heading * 4) & 0xFFF,
            self.x,
            self.delta_z,
            self.z,
            self.y,
            self.animation & 0x3FF,
            self.delta_y,
            int(self.delta_heading * 20) & 0x3FF,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> "OP_ClientUpdate":
        if len(data) == 24:
            return _read_server_position(data)

        if len(data) not in (46, 47):
            raise ValueError(f"OP_ClientUpdate: unexpected size {len(data)}")

        (
            sequence,
            spawn_id,
            vehicle_id,
            unknown06,
            delta_x,
            heading_word,
            x,
            delta_z,
            z,
            y,
            animation_word,
            delta_y,
            delta_heading_word,
        ) = struct.unpack_from("<HHH4sfIffffIfI", data)

        return cls(
            spawn_id=spawn_id,
            x=x,
            y=y,
            z=z,
            sequence=sequence,
            heading=bitfield(heading_word, 0, 12, signed=False) / 4.0,
            animation=bitfield(animation_word, 0, 10, signed=False),
            delta_x=delta_x,
            delta_y=delta_y,
            delta_z=delta_z,
            server=False,
            vehicle_id=vehicle_id,
            delta_heading=bitfield(delta_heading_word, 0, 10) / 20.0,
            unknown06=unknown06,
        )


@dataclass
class OP_NewSpawn(EQStruct):
    spawn: Spawn

    def serialize(self) -> bytes:
        return self.spawn.serialize()

    @classmethod
    def deserialize(cls, data: bytes) -> OP_NewSpawn:
        return cls(Spawn.deserialize(data))


@dataclass
class OP_ZoneSpawns(EQStruct):
    spawns: list[Spawn] = field(default_factory=list)

    def serialize(self) -> bytes:
        return b"".join(spawn.serialize() for spawn in self.spawns)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ZoneSpawns:
        spawns = []
        offset = 0

        while offset < len(data):
            spawn, next_offset = _read_spawn(data, offset)

            if next_offset <= offset:
                raise ValueError(f"OP_ZoneSpawns made no progress at offset {offset}")

            spawns.append(spawn)
            offset = next_offset

        return cls(spawns)


@dataclass
class OP_DeleteSpawn(EQStruct):
    spawn_id: int

    def serialize(self) -> bytes:
        # common/patches/rof2.cpp:1165
        return struct.pack("<IB", self.spawn_id & 0xFFFFFFFF, 1)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_DeleteSpawn:
        need(data, 4, "OP_DeleteSpawn")
        return cls(read_u32(data))


@dataclass
class OP_SpawnAppearance(EQStruct):
    spawn_id: int
    type: int
    parameter: int

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:523
        return struct.pack(
            "<HHI", self.spawn_id & 0xFFFF, self.type & 0xFFFF, self.parameter & 0xFFFFFFFF
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_SpawnAppearance:
        need(data, 8, "OP_SpawnAppearance")
        spawn_id, kind, parameter = struct.unpack_from("<HHI", data)
        return cls(int(spawn_id), int(kind), int(parameter))


@dataclass
class OP_HPUpdate(EQStruct):
    cur_hp: int
    max_hp: int
    spawn_id: int

    def serialize(self) -> bytes:
        # common/patches/rof2_structs.h:1679
        return struct.pack(
            "<hIi",
            i16(self.spawn_id),
            self.cur_hp & 0xFFFFFFFF,
            i32(self.max_hp),
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_HPUpdate:
        need(data, 10, "OP_HPUpdate")
        spawn_id, cur_hp, max_hp = struct.unpack_from("<hIi", data)
        return cls(int(cur_hp), int(max_hp), int(spawn_id))


@dataclass
class OP_MobHealth(EQStruct):
    spawn_id: int
    percent: int

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:1477
        return struct.pack("<hB", i16(self.spawn_id), self.percent & 0xFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_MobHealth:
        need(data, 3, "OP_MobHealth")
        spawn_id, percent = struct.unpack_from("<HB", data)
        return cls(int(spawn_id), int(percent))


@dataclass
class OP_Damage(EQStruct):
    target: int
    source: int
    type: int
    spell_id: int
    amount: int
    force: float = 0.0
    hit_heading: float = 0.0
    hit_pitch: float = 0.0

    def serialize(self) -> bytes:
        # common/patches/rof2_structs.h:1511
        return struct.pack(
            "<HHBIi3fBI",
            self.target & 0xFFFF,
            self.source & 0xFFFF,
            self.type & 0xFF,
            self.spell_id & 0xFFFFFFFF,
            i32(self.amount),
            self.force,
            self.hit_heading,
            self.hit_pitch,
            0,
            0,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_Damage:
        need(data, 13, "OP_Damage")
        target, source = struct.unpack_from("<HH", data)
        spell_id = read_u32(data, 5)
        amount = struct.unpack_from("<i", data, 9)[0]
        force = hit_heading = hit_pitch = 0.0
        if len(data) >= 25:
            force, hit_heading, hit_pitch = struct.unpack_from("<fff", data, 13)
        return cls(
            int(target),
            int(source),
            int(data[4]),
            int(spell_id),
            int(amount),
            float(force),
            float(hit_heading),
            float(hit_pitch),
        )


@dataclass
class OP_Death(EQStruct):
    spawn_id: int
    killer_id: int = 0
    corpse_id: int = 0
    attack_skill: int = 0
    spell_id: int = 0
    bind_zone_id: int = 0
    damage: int = 0
    unknown: int = 0

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:1366
        return struct.pack(
            "<8I",
            self.spawn_id & 0xFFFFFFFF,
            self.killer_id & 0xFFFFFFFF,
            self.corpse_id & 0xFFFFFFFF,
            self.bind_zone_id & 0xFFFFFFFF,
            self.spell_id & 0xFFFFFFFF,
            self.attack_skill & 0xFFFFFFFF,
            self.damage & 0xFFFFFFFF,
            self.unknown & 0xFFFFFFFF,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_Death:
        need(data, 32, "OP_Death")
        spawn_id, killer_id, corpse_id, bind_zone_id, spell_id, attack_skill, damage, unknown = (
            struct.unpack_from("<8I", data)
        )
        return cls(
            int(spawn_id),
            int(killer_id),
            int(corpse_id),
            int(attack_skill),
            int(spell_id),
            int(bind_zone_id),
            int(damage),
            int(unknown),
        )


@dataclass
class OP_BecomeCorpse(EQStruct):
    spawn_id: int
    x: float
    y: float
    z: float

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:1378
        return struct.pack(
            "<Ifff",
            self.spawn_id & 0xFFFFFFFF,
            self.y,
            self.x,
            self.z,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_BecomeCorpse:
        need(data, 16, "OP_BecomeCorpse")
        spawn_id, wire_y, wire_x, wire_z = struct.unpack_from("<Ifff", data)
        return cls(int(spawn_id), float(wire_x), float(wire_y), float(wire_z))


@dataclass
class OP_Assist(EQStruct):
    entity_id: int

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:84 EntityId_Struct
        return struct.pack("<I", self.entity_id & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_Assist:
        if len(data) >= 4:
            return cls(read_u32(data))
        if len(data) >= 2:
            return cls(struct.unpack_from("<H", data)[0])
        raise ValueError(f"OP_Assist is {len(data)} bytes")


@dataclass
class TrackDetails:
    level: int = 0
    is_npc: int = 0
    name: str = ""
    is_pet: int = 0
    is_merc: int = 0


@dataclass
class OP_Track(EQStruct):
    entries: list[tuple[int, float]] = field(default_factory=list)
    details: list[TrackDetails] = field(default_factory=list)

    def serialize(self) -> bytes:
        out = struct.pack("<H", len(self.entries) & 0xFFFF)

        for index, (entity_id, distance) in enumerate(self.entries):

            if index < len(self.details):
                info = self.details[index]
            else:
                info = TrackDetails()

            out += struct.pack(
                "<IfBB",
                entity_id & 0xFFFFFFFF,
                float(distance),
                info.level & 0xFF,
                info.is_npc & 0xFF,
            )
            out += put_cstr(info.name)
            out += struct.pack("<BB", info.is_pet, info.is_merc)

        return bytes(out)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_Track:
        if len(data) < 2:
            return cls()

        count = struct.unpack_from("<H", data)[0]
        offset = 2

        entries = []
        details = []

        for _ in range(count):
            entity_id, distance, level, is_npc = struct.unpack_from("<IfBB", data, offset)
            offset += 10

            name, offset = cstring(data, offset)

            is_pet, is_merc = struct.unpack_from("<BB", data, offset)
            offset += 2

            entries.append((int(entity_id), float(distance)))
            details.append(
                TrackDetails(
                    level=int(level),
                    is_npc=int(is_npc),
                    name=name,
                    is_pet=int(is_pet),
                    is_merc=int(is_merc),
                )
            )

        return cls(entries=entries, details=details)


@dataclass
class OP_TrackTarget(EQStruct):
    entity_id: int

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:3648 TrackTarget_Struct
        return struct.pack("<I", self.entity_id & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_TrackTarget:
        need(data, 4, "OP_TrackTarget")
        return cls(read_u32(data))


@dataclass
class OP_FindPersonRequest(EQStruct):
    entity_id: int
    x: float
    y: float
    z: float

    def serialize(self) -> bytes:
        # common/patches/rof2_structs.h:4026 FindPersonRequest_Struct
        return struct.pack(
            "<IIII3fIII",
            0,
            self.entity_id & 0xFFFFFFFF,
            0,
            0,
            self.y,
            self.x,
            self.z,
            0,
            0,
            0,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_FindPersonRequest:
        need(data, 28, "OP_FindPersonRequest")
        entity = read_u32(data, 4)
        wire_y, wire_x, wire_z = struct.unpack_from("<fff", data, 16)
        return cls(int(entity), float(wire_x), float(wire_y), float(wire_z))


@dataclass
class OP_FindPersonReply(EQStruct):
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    points: list[tuple[float, float, float]] = field(default_factory=list)

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:4404 FindPerson_Point
        out = struct.pack("<fff", self.y, self.x, self.z)
        for point in self.points:
            # common/eq_packet_structs.h:4416 FindPersonResult_Struct
            out += struct.pack("<fff", point[1], point[0], point[2])
        return out

    @classmethod
    def deserialize(cls, data: bytes) -> OP_FindPersonReply:
        if len(data) < 12:
            return cls()

        dest_y, dest_x, dest_z = struct.unpack_from("<fff", data)
        points: list[tuple[float, float, float]] = []
        offset = 12
        while offset + 12 <= len(data):
            wire_y, wire_x, wire_z = struct.unpack_from("<fff", data, offset)
            points.append((float(wire_x), float(wire_y), float(wire_z)))
            offset += 12
        if len(points) >= 2 and _close(points[-1], points[-2]):
            points.pop()
        return cls(float(dest_x), float(dest_y), float(dest_z), points)


def _close(a: tuple[float, float, float], b: tuple[float, float, float]) -> bool:
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 <= 0.01
