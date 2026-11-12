"""RoF2 application packets missing from eqclient4, based on EQEmu agent-v4.

Add `from eqclient4.structs import rof2_missing` to structs/__init__.py to register
all OP_* classes in the existing OPERATIONS registry (no duplicate definitions).
"""

import struct
from dataclasses import dataclass, field

from eqclient4.structs.wire import (
    EQStruct,
    cstring,
    exact,
    fixed,
    fixed_bytes,
    need,
    put_cstr,
)


@dataclass
class OP_TimeOfDay(EQStruct):
    """RoF2 TimeOfDay_Struct: four u8, a u16 year, u16 unused."""

    hour: int
    minute: int
    day: int
    month: int
    year: int
    unknown06: int = 0

    def serialize(self) -> bytes:
        return struct.pack(
            "<4BHH", self.hour, self.minute, self.day, self.month, self.year, self.unknown06
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_TimeOfDay:
        exact(data, 8, cls.__name__)
        return cls(*struct.unpack("<4BHH", data))


@dataclass
class OP_TributeUpdate(EQStruct):
    """TributeInfo_Struct: active, five tribute IDs, five tiers, master ID."""

    active: int = 0
    tributes: tuple[int, ...] = (0xFFFFFFFF,) * 5
    tiers: tuple[int, ...] = (0,) * 5
    tribute_master_id: int = 0xFFFFFFFF

    def serialize(self) -> bytes:
        if len(self.tributes) != 5 or len(self.tiers) != 5:
            raise ValueError("OP_TributeUpdate expects five tribute slots and tiers")
        return struct.pack(
            "<12I",
            self.active,
            *self.tributes,
            *self.tiers,
            self.tribute_master_id,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_TributeUpdate:
        exact(data, 48, cls.__name__)
        values = struct.unpack("<12I", data)
        return cls(values[0], values[1:6], values[6:11], values[11])


@dataclass
class OP_TributeTimer(EQStruct):
    """Time remaining on character tribute timer, in milliseconds."""

    milliseconds: int

    def serialize(self) -> bytes:
        return struct.pack("<I", self.milliseconds)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_TributeTimer:
        exact(data, 4, cls.__name__)
        return cls(struct.unpack("<I", data)[0])


@dataclass
class OP_Weather(EQStruct):
    """Weather_Struct; zone.cpp sometimes also emits the 8-byte variant."""

    val1: int = 0xFF
    weather_type: int = 0
    mode: int | None = 0

    def serialize(self) -> bytes:
        header = struct.pack("<II", self.val1, self.weather_type)
        return header if self.mode is None else header + struct.pack("<I", self.mode)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_Weather:
        if len(data) not in (8, 12):
            raise ValueError(f"OP_Weather expected 8 or 12 bytes, got {len(data)}")
        a, b = struct.unpack_from("<II", data)
        return cls(
            a,
            b,
            struct.unpack_from("<I", data, 8)[0] if len(data) == 12 else None,
        )


@dataclass
class AARankEffect:
    skill_id: int
    base_value: int
    limit_value: int
    slot: int


@dataclass
class OP_SendAATable(EQStruct):
    """RoF2 encoded AA rank information, variable-sized prereqs/effects.

    This models the data written by ENCODE(OP_SendAATable), not the internal
    server's SendAA_Struct (which has a different layout).
    """

    aa_id: int
    hotkey_sid: int = -1
    hotkey_sid2: int = -1
    title_sid: int = -1
    desc_sid: int = -1
    level_req: int = 0
    cost: int = 0
    seq: int = 0
    current_level: int = 0
    prereq_skills: list[int] = field(default_factory=lambda: [0])
    prereq_points: list[int] = field(default_factory=lambda: [0])
    aa_type: int = 0
    spell_id: int = 0
    unknown057: int = 1
    spell_type: int = 0
    spell_refresh: int = 0
    classes: int = 0
    max_level: int = 0
    prev_id: int = 0
    next_id: int = 0
    total_cost: int = 0
    flags93: bytes = b"\x00\x00\x00"  # middle byte: grant_only
    charges: int = 0
    expansion: int = 0
    category: int = 0
    flags108: bytes = b"\x00\x00\x00\x00"
    effects: list[AARankEffect] = field(default_factory=list)
    unknown004: int = 1
    trailing: bytes = b""

    @property
    def grant_only(self) -> int:
        return self.flags93[1]

    def serialize(self) -> bytes:
        if len(self.flags93) != 3 or len(self.flags108) != 4:
            raise ValueError("invalid OP_SendAATable flag lengths")
        if not self.prereq_skills or not self.prereq_points:
            raise ValueError("RoF2 requires at least one entry in each prereq array")
        out = bytearray(struct.pack("<IB", self.aa_id, self.unknown004))
        out += struct.pack(
            "<6i2I",
            self.hotkey_sid,
            self.hotkey_sid2,
            self.title_sid,
            self.desc_sid,
            self.level_req,
            self.cost,
            self.seq,
            self.current_level,
        )
        out += struct.pack("<I", len(self.prereq_skills))
        out += struct.pack(f"<{len(self.prereq_skills)}i", *self.prereq_skills)
        out += struct.pack("<I", len(self.prereq_points))
        out += struct.pack(f"<{len(self.prereq_points)}i", *self.prereq_points)
        out += struct.pack(
            "<10i",
            self.aa_type,
            self.spell_id,
            self.unknown057,
            self.spell_type,
            self.spell_refresh,
            self.classes,
            self.max_level,
            self.prev_id,
            self.next_id,
            self.total_cost,
        )
        out += self.flags93
        out += struct.pack("<Iii", self.charges, self.expansion, self.category)
        out += self.flags108
        out += struct.pack("<I", len(self.effects))
        for e in self.effects:
            out += struct.pack("<4I", e.skill_id, e.base_value, e.limit_value, e.slot)
        return bytes(out) + self.trailing

    @classmethod
    def deserialize(cls, data: bytes) -> OP_SendAATable:
        need(data, 116, cls.__name__)
        aa_id, unknown004 = struct.unpack_from("<IB", data)
        hotkey_sid, hotkey_sid2, title_sid, desc_sid, level_req, cost, seq, current_level = (
            struct.unpack_from("<6i2I", data, 5)
        )
        offset = 37
        prereqs = []
        for which in range(2):
            if len(data) - offset < 4:
                raise ValueError("truncated AA prerequisite count")
            count = struct.unpack_from("<I", data, offset)[0]
            offset += 4
            if count > (len(data) - offset) // 4:
                raise ValueError("truncated AA prerequisites")
            values = list(struct.unpack_from(f"<{count}i", data, offset)) if count else []
            prereqs.append(values)
            offset += count * 4
        if len(data) - offset < 63:
            raise ValueError("truncated AA rank fields")
        fields = struct.unpack_from("<10i", data, offset)
        offset += 40
        flags93 = data[offset : offset + 3]
        offset += 3
        charges, expansion, category = struct.unpack_from("<Iii", data, offset)
        offset += 12
        flags108 = data[offset : offset + 4]
        offset += 4
        count = struct.unpack_from("<I", data, offset)[0]
        offset += 4
        if count > (len(data) - offset) // 16:
            raise ValueError("truncated AA effect array")
        effects = [
            AARankEffect(*struct.unpack_from("<4I", data, offset + 16 * i)) for i in range(count)
        ]
        offset += count * 16
        return cls(
            aa_id=aa_id,
            hotkey_sid=hotkey_sid,
            hotkey_sid2=hotkey_sid2,
            title_sid=title_sid,
            desc_sid=desc_sid,
            level_req=level_req,
            cost=cost,
            seq=seq,
            current_level=current_level,
            prereq_skills=prereqs[0],
            prereq_points=prereqs[1],
            aa_type=fields[0],
            spell_id=fields[1],
            unknown057=fields[2],
            spell_type=fields[3],
            spell_refresh=fields[4],
            classes=fields[5],
            max_level=fields[6],
            prev_id=fields[7],
            next_id=fields[8],
            total_cost=fields[9],
            flags93=flags93,
            charges=charges,
            expansion=expansion,
            category=category,
            flags108=flags108,
            effects=effects,
            unknown004=unknown004,
            trailing=data[offset:],
        )


@dataclass
class OP_UpdateAA(EQStruct):
    """Client -> server: request current AA data (empty payload)."""

    def serialize(self) -> bytes:
        return b""

    @classmethod
    def deserialize(cls, data: bytes) -> OP_UpdateAA:
        exact(data, 0, cls.__name__)
        return cls()


@dataclass
class _FourByteRequest(EQStruct):
    value: int

    def serialize(self) -> bytes:
        return struct.pack("<I", self.value)

    @classmethod
    def deserialize(cls, data: bytes) -> _FourByteRequest:
        exact(data, 4, cls.__name__)
        return cls(struct.unpack("<I", data)[0])


class OP_SendTributes(_FourByteRequest):
    """Client -> server, 4-byte value as observed; exact meaning not verified."""


class OP_RequestGuildTributes(_FourByteRequest):
    """Client -> server, 4-byte value as observed; exact meaning not verified."""


@dataclass
class TributeTier:
    level: int
    tribute_item_id: int
    cost: int


@dataclass
class OP_TributeInfo(EQStruct):
    """RoF2 tribute ability: 10 big-endian tiers, one unknown u32, C string."""

    tribute_id: int
    tier_count: int
    tiers: list[TributeTier] = field(default_factory=list)
    name: str = ""
    unknown128: int = 0
    trailing: bytes = b""

    def serialize(self) -> bytes:
        if len(self.tiers) > 10:
            raise ValueError("max 10 tribute tiers")
        out = bytearray(struct.pack(">II", self.tribute_id, self.tier_count))
        for i in range(10):
            t = self.tiers[i] if i < len(self.tiers) else TributeTier(0, 0, 0)
            out += struct.pack(">III", t.level, t.tribute_item_id, t.cost)
        out += struct.pack("<I", self.unknown128)
        return bytes(out) + put_cstr(self.name) + self.trailing

    @classmethod
    def deserialize(cls, data: bytes) -> OP_TributeInfo:
        need(data, 133, cls.__name__)
        tribute_id, tier_count = struct.unpack_from(">II", data)
        tiers = [TributeTier(*struct.unpack_from(">III", data, 8 + 12 * i)) for i in range(10)]
        unknown128 = struct.unpack_from("<I", data, 128)[0]
        name, end = cstring(data, 132)
        return cls(tribute_id, tier_count, tiers, name, unknown128, data[end:])


@dataclass
class ZonePointEntry:
    iterator: int
    y: float
    x: float
    z: float
    heading: float
    zone_id: int
    instance_id: int
    unknown024: int = 0
    unknown028: int = 0

    _FMT = "<IffffHHII"

    def pack(self) -> bytes:
        return struct.pack(
            self._FMT,
            self.iterator,
            self.y,
            self.x,
            self.z,
            self.heading,
            self.zone_id,
            self.instance_id,
            self.unknown024,
            self.unknown028,
        )

    @classmethod
    def unpack(cls, data: bytes, offset: int) -> ZonePointEntry:
        return cls(*struct.unpack_from(cls._FMT, data, offset))


@dataclass
class OP_SendZonepoints(EQStruct):
    """RoF2 count + 32-byte entries + one extra sentinel entry."""

    entries: list[ZonePointEntry] = field(default_factory=list)
    sentinel: bytes = bytes(32)
    trailing: bytes = b""

    def serialize(self) -> bytes:
        if len(self.sentinel) != 32:
            raise ValueError("zonepoint sentinel must be 32 bytes")
        return (
            struct.pack("<I", len(self.entries))
            + b"".join(e.pack() for e in self.entries)
            + self.sentinel
            + self.trailing
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_SendZonepoints:
        need(data, 36, cls.__name__)
        count = struct.unpack_from("<I", data)[0]
        if count > (len(data) - 36) // 32:
            raise ValueError("truncated OP_SendZonepoints entries or sentinel")
        entries = [ZonePointEntry.unpack(data, 4 + 32 * i) for i in range(count)]
        offset = 4 + count * 32
        return cls(entries, data[offset : offset + 32], data[offset + 32 :])


@dataclass
class OP_GuildMOTD(EQStruct):
    """GuildMOTD_Struct (648 bytes), names 64 bytes, MOTD 512 bytes."""

    name: str = ""
    setby_name: str = ""
    motd: str = ""
    unknown0: int = 0
    unknown132: int = 0

    def serialize(self) -> bytes:
        return (
            struct.pack("<I", self.unknown0)
            + fixed_bytes(self.name, 64)
            + fixed_bytes(self.setby_name, 64)
            + struct.pack("<I", self.unknown132)
            + fixed_bytes(self.motd, 512)
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_GuildMOTD:
        exact(data, 648, cls.__name__)
        return cls(
            fixed(data, 4, 64),
            fixed(data, 68, 64),
            fixed(data, 136, 512),
            struct.unpack_from("<I", data)[0],
            struct.unpack_from("<I", data, 132)[0],
        )


@dataclass
class OP_BlockedBuffs(EQStruct):
    """RoF2 blocked buffs: 30 * i32, count u32, pet/init u8, flags u16."""

    spell_ids: tuple[int, ...] = (-1,) * 30
    count: int = 0
    pet: int = 0
    initialise: int = 0
    flags: int = 0

    def serialize(self) -> bytes:
        if len(self.spell_ids) != 30:
            raise ValueError("RoF2 requires exactly 30 blocked buff slots")
        return struct.pack("<30i", *self.spell_ids) + struct.pack(
            "<IBBH",
            self.count,
            self.pet,
            self.initialise,
            self.flags,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_BlockedBuffs:
        exact(data, 128, cls.__name__)
        return cls(struct.unpack_from("<30i", data), *struct.unpack_from("<IBBH", data, 120))


@dataclass
class OP_ChangeSize(EQStruct):
    entity_id: int
    size: float
    unknown08: int = 0
    scale: float = 1.0

    def serialize(self) -> bytes:
        return struct.pack("<IfIf", self.entity_id, self.size, self.unknown08, self.scale)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ChangeSize:
        exact(data, 16, cls.__name__)
        return cls(*struct.unpack("<IfIf", data))


class OP_TaskRequestTimer(_FourByteRequest):
    """One uint32 timer value; unit has not been verified from the capture."""


@dataclass
class DzCompassEntry:
    zone_id: int
    instance_id: int
    dz_type: int
    switch_id: int
    y: float
    x: float
    z: float

    _FMT = "<HHIIfff"

    def pack(self) -> bytes:
        return struct.pack(
            self._FMT,
            self.zone_id,
            self.instance_id,
            self.dz_type,
            self.switch_id,
            self.y,
            self.x,
            self.z,
        )

    @classmethod
    def unpack(cls, data: bytes, offset: int) -> DzCompassEntry:
        return cls(*struct.unpack_from(cls._FMT, data, offset))


@dataclass
class OP_DzCompass(EQStruct):
    client_id: int
    entries: list[DzCompassEntry] = field(default_factory=list)
    trailing: bytes = b""

    def serialize(self) -> bytes:
        return (
            struct.pack("<II", self.client_id, len(self.entries))
            + b"".join(e.pack() for e in self.entries)
            + self.trailing
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_DzCompass:
        need(data, 8, cls.__name__)
        client_id, count = struct.unpack_from("<II", data)
        if count > (len(data) - 8) // 24:
            raise ValueError("truncated DZ compass entries")
        entries = [DzCompassEntry.unpack(data, 8 + 24 * i) for i in range(count)]
        return cls(client_id, entries, data[8 + 24 * count :])


@dataclass
class DzLockoutEntry:
    expedition_name: str
    seconds_remaining: int
    event_type: int
    event_name: str


@dataclass
class OP_DzExpeditionLockoutTimers(EQStruct):
    client_id: int
    entries: list[DzLockoutEntry] = field(default_factory=list)
    trailing: bytes = b""

    def serialize(self) -> bytes:
        out = bytearray(struct.pack("<II", self.client_id, len(self.entries)))
        for e in self.entries:
            out += put_cstr(e.expedition_name)
            out += struct.pack("<Ii", e.seconds_remaining, e.event_type)
            out += put_cstr(e.event_name)
        return bytes(out) + self.trailing

    @classmethod
    def deserialize(cls, data: bytes) -> OP_DzExpeditionLockoutTimers:
        need(data, 8, cls.__name__)
        client_id, count = struct.unpack_from("<II", data)
        if count > (len(data) - 8) // 10:
            raise ValueError("truncated DZ lockouts")
        entries = []
        offset = 8
        for _ in range(count):
            expedition_name, offset = cstring(data, offset)
            if len(data) - offset < 8:
                raise ValueError("truncated DZ lockout timer")
            remaining, event_type = struct.unpack_from("<Ii", data, offset)
            offset += 8
            event_name, offset = cstring(data, offset)
            entries.append(
                DzLockoutEntry(
                    expedition_name,
                    remaining,
                    event_type,
                    event_name,
                )
            )
        return cls(client_id, entries, data[offset:])


@dataclass
class BuffIconEntry:
    buff_slot: int
    spell_id: int
    tics_remaining: int
    num_hits: int
    caster: str = ""


@dataclass
class OP_BuffCreate(EQStruct):
    """RoF2 buff-icon updates, separate from OP_Buff's full buff details."""

    entity_id: int
    tic_timer: int = 0
    all_buffs: int = 1
    entries: list[BuffIconEntry] = field(default_factory=list)
    buff_type: int = 0
    trailing: bytes = b""

    def serialize(self) -> bytes:
        out = bytearray(
            struct.pack("<IIBH", self.entity_id, self.tic_timer, self.all_buffs, len(self.entries)),
        )
        for e in self.entries:
            out += struct.pack(
                "<IIII",
                e.buff_slot,
                e.spell_id,
                e.tics_remaining,
                e.num_hits,
            )
            out += put_cstr(e.caster)
        out.append(self.buff_type)
        return bytes(out) + self.trailing

    @classmethod
    def deserialize(cls, data: bytes) -> OP_BuffCreate:
        need(data, 12, cls.__name__)
        entity_id, timer, all_buffs, count = struct.unpack_from("<IIBH", data)
        offset = 11
        if count > (len(data) - 12) // 17:
            raise ValueError("truncated buff icon entries")
        entries = []
        for _ in range(count):
            if len(data) - offset < 17:
                raise ValueError("truncated buff icon")
            slot, spell, tics, hits = struct.unpack_from("<IIII", data, offset)
            offset += 16
            caster, offset = cstring(data, offset)
            entries.append(BuffIconEntry(slot, spell, tics, hits, caster))
        if offset >= len(data):
            raise ValueError("missing buff icon type")
        return cls(entity_id, timer, all_buffs, entries, data[offset], data[offset + 1 :])


@dataclass
class OP_AAExpUpdate(EQStruct):
    unknown00: int = 0
    aapoints_unspent: int = 0
    aaxp_percent: int = 0
    unknown09: bytes = b"\x00\x00\x00"

    def serialize(self) -> bytes:
        if len(self.unknown09) != 3:
            raise ValueError("AAExpUpdate trailing bytes must be 3 bytes")
        return (
            struct.pack("<IIB", self.unknown00, self.aapoints_unspent, self.aaxp_percent)
            + self.unknown09
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_AAExpUpdate:
        exact(data, 12, cls.__name__)
        unknown00, aapoints_unspent, aaxp_percent = struct.unpack_from("<IIB", data)
        return cls(
            unknown00=unknown00,
            aapoints_unspent=aapoints_unspent,
            aaxp_percent=aaxp_percent,
            unknown09=data[9:12],
        )


@dataclass(repr=False)
class OP_Save(EQStruct):
    """RoF2 Save_Struct: 484 bytes, no verified field semantics."""

    payload: bytes = bytes(484)

    def serialize(self) -> bytes:
        exact(self.payload, 484, self.__class__.__name__)
        return self.payload

    @classmethod
    def deserialize(cls, data: bytes) -> OP_Save:
        exact(data, 484, cls.__name__)
        return cls(bytes(data))

    def __repr__(self) -> str:
        return f"OP_Save(size={len(self.payload)}, hex={self.payload[:32].hex(' ')} ...)"


@dataclass
class OP_ItemLinkText(EQStruct):
    """Legacy EQEmu item-link packet, with optional sender and trailing padding."""

    unknown00: int = 0
    message_type: int = 0x1D3
    unknown08: int = 0x11E
    prefix: bytes = b""
    link: str = ""
    trailing: bytes = b""

    def serialize(self) -> bytes:
        return (
            struct.pack("<III", self.unknown00, self.message_type, self.unknown08)
            + self.prefix
            + self.link.encode("ascii")
            + self.trailing
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ItemLinkText:
        need(data, 12, cls.__name__)

        unknown00, message_type, unknown08 = struct.unpack_from("<III", data)

        start = data.find(b"\x12", 12)
        end = data.find(b"\x12", start + 1) if start >= 0 else -1

        if end < 0:
            raise ValueError("OP_ItemLinkText: missing link delimiter")

        return cls(
            unknown00=unknown00,
            message_type=message_type,
            unknown08=unknown08,
            prefix=data[12:start],
            link=data[start : end + 1].decode("ascii"),
            trailing=data[end + 1 :],
        )

    @property
    def item_id(self) -> int | None:
        body = self.link[1:-1]
        if len(body) >= 7 and body[0] == "0" and body[1:7].isdigit():
            return int(body[1:7])
        return None
