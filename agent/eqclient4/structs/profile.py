import struct
from copy import deepcopy
from dataclasses import dataclass, field

from eqclient4.structs.wire import (
    EQStruct,
    advance,
    cstring,
    exact,
    fixed,
    i32,
    need,
    put_fixed,
    read_u32,
)
from eqclient4.utils import crc32

GM_TRAINING_SIZE = 448
GM_SKILL_COUNT = 100
PROFILE_SIZE = 14312


@dataclass
class SpellBuff(EQStruct):
    effect_type: int = 0
    level: int = 0
    bard_modifier: int = 0
    unknown: int = 0
    spell_id: int = 0
    duration: int = 0
    counters: int = 0
    caster_id: int = 0


@dataclass
class ProfileBind:
    zone_id: int = 0
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    heading: float = 0.0


@dataclass
class OP_PlayerProfile(EQStruct):
    # Original API, in the same positional order.
    name: str = ""
    gender: int = 0
    race: int = 0
    class_id: int = 0
    level: int = 0
    deity: int = 0
    home_zone_id: int = 0
    points: int = 0
    hp: int = 0
    mana: int = 0
    strength: int = 0
    stamina: int = 0
    charisma: int = 0
    dexterity: int = 0
    intelligence: int = 0
    agility: int = 0
    wisdom: int = 0
    platinum: int = 0
    gold: int = 0
    silver: int = 0
    copper: int = 0
    coin_known: bool = False
    skills: dict[int, int] | None = None
    spell_book: dict[int, int] = field(default_factory=dict)
    gems: dict[int, int] = field(default_factory=dict)

    # Additional modeled data. Appended to retain positional compatibility.
    last_name: str = ""
    binds: list[ProfileBind] = field(default_factory=list)
    innate_skills: dict[int, int] = field(default_factory=dict)
    disciplines: dict[int, int] = field(default_factory=dict)
    recast_timers: dict[int, int] = field(default_factory=dict)
    aa: dict[int, tuple[int, int, int]] = field(default_factory=dict)
    buffs: dict[int, SpellBuff] = field(default_factory=dict)
    cursor_platinum: int = 0
    cursor_gold: int = 0
    cursor_silver: int = 0
    cursor_copper: int = 0
    aa_points: int = 0
    aa_points_spent: int = 0
    endurance: int = 0
    zone_id: int = 0
    zone_instance: int = 0
    # Do NOT use the following position for gameplay
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    heading: float = 0.0
    experience: int = 0
    bank_platinum: int = 0
    bank_gold: int = 0
    bank_silver: int = 0
    bank_copper: int = 0
    shared_platinum: int = 0
    guild_id: int = 0
    gm: bool = False
    pvp: bool = False

    _raw_packet: bytes = field(default=b"", repr=False, compare=False)
    _original: dict = field(default_factory=dict, repr=False, compare=False)
    _offsets: dict[str, int] = field(default_factory=dict, repr=False, compare=False)

    # Packet offsets produced by RoF2's ENCODE(OP_PlayerProfile).
    # The 300-discipline array shifts offsets +400 from old C++ comments.
    _SCALARS = {
        "gender": ("<B", 16),
        "race": ("<I", 17),
        "class_id": ("<B", 21),
        "level": ("<B", 22),
        "deity": ("<I", 128),
        "home_zone_id": ("<I", 28),
        "points": ("<I", 940),
        "mana": ("<I", 944),
        "hp": ("<I", 948),
        "strength": ("<I", 952),
        "stamina": ("<I", 956),
        "charisma": ("<I", 960),
        "dexterity": ("<I", 964),
        "intelligence": ("<I", 968),
        "agility": ("<I", 972),
        "wisdom": ("<I", 976),
        "platinum": ("<I", 13269),
        "gold": ("<I", 13273),
        "silver": ("<I", 13277),
        "copper": ("<I", 13281),
        "cursor_platinum": ("<I", 13285),
        "cursor_gold": ("<I", 13289),
        "cursor_silver": ("<I", 13293),
        "cursor_copper": ("<I", 13297),
        "aa_points_spent": ("<I", 13321),
        "aa_points": ("<I", 13349),
    }

    @staticmethod
    def _locate_tail(data: bytes) -> dict[str, int]:
        """Walk variable-length bandolier and potion strings once."""
        offset = 13355
        count = read_u32(data, offset)
        if count > 64:
            raise ValueError(f"Implausible bandolier count: {count}")
        offset += 4
        for _ in range(count):
            _, offset = cstring(data, offset)
            for _ in range(4):
                _, offset = cstring(data, offset)
                offset = advance(data, offset, 8, "bandolier item")

        potions = read_u32(data, offset)
        if potions > 32:
            raise ValueError(f"Implausible potion belt count: {potions}")
        offset += 4
        for _ in range(potions):
            _, offset = cstring(data, offset)
            offset = advance(data, offset, 8, "potion belt item")

        name_len = offset + 96
        need(data, name_len + 4 + 64, "profile name")
        if read_u32(data, name_len) != 64:
            raise ValueError("Unexpected RoF2 profile name length")
        last_name_len = name_len + 4 + 64
        if len(data) < last_name_len + 4 + 32:
            # Older/partial captures end just after the first name.
            return {"name": name_len + 4, "endurance": name_len - 12}
        if read_u32(data, last_name_len) != 32:
            raise ValueError("Unexpected RoF2 profile surname length")
        result = {"name": name_len + 4, "last_name": last_name_len + 4, "endurance": name_len - 12}
        languages_count_offset = last_name_len + 4 + 32 + 6 * 4
        if len(data) < languages_count_offset + 4:
            return result
        languages_count = read_u32(data, languages_count_offset)
        if languages_count > 256:
            raise ValueError(f"Implausible language count: {languages_count}")
        zone = languages_count_offset + 4 + languages_count
        if len(data) >= zone + 67:
            result.update(
                {
                    "zone": zone,
                    "experience": zone + 38,
                    "bank_coins": zone + 47,
                    "shared_platinum": zone + 63,
                    "guild_id": zone + 24,
                    "pvp": zone + 21,
                    "gm": zone + 23,
                }
            )
        return result

    def _values(self) -> dict:
        from dataclasses import fields

        return {
            f.name: deepcopy(getattr(self, f.name))
            for f in fields(self)
            if not f.name.startswith("_")
        }

    @classmethod
    def deserialize(cls, data: bytes) -> OP_PlayerProfile:
        need(data, PROFILE_SIZE, "OP_PlayerProfile")
        offsets = cls._locate_tail(data)
        kwargs = {
            name: struct.unpack_from(fmt, data, offset)[0]
            for name, (fmt, offset) in cls._SCALARS.items()
        }
        kwargs["name"] = fixed(data, offsets["name"], 64)
        kwargs["endurance"] = read_u32(data, offsets["endurance"])
        kwargs["coin_known"] = True
        kwargs["skills"] = dict(enumerate(struct.unpack_from("<100I", data, 4616)))
        kwargs["spell_book"] = {
            i: spell
            for i, spell in enumerate(struct.unpack_from("<720I", data, 6900))
            if spell not in (0, 0xFFFFFFFF)
        }
        kwargs["gems"] = {
            i: spell
            for i, spell in enumerate(struct.unpack_from("<16i", data, 9784))
            if spell not in (0, -1)
        }
        kwargs["binds"] = [
            ProfileBind(*struct.unpack_from("<Iffff", data, 28 + i * 20)) for i in range(5)
        ]
        kwargs["innate_skills"] = dict(enumerate(struct.unpack_from("<25I", data, 5020)))
        kwargs["disciplines"] = {
            i: val
            for i, val in enumerate(struct.unpack_from("<300I", data, 5124))
            if val not in (0, 0xFFFFFFFF)
        }
        kwargs["recast_timers"] = dict(enumerate(struct.unpack_from("<20I", data, 6412)))
        kwargs["aa"] = {
            i: value
            for i in range(300)
            if (value := struct.unpack_from("<III", data, 1012 + 12 * i))[0] != 0
        }
        buffs = {}
        for i in range(42):
            b = 9909 + i * 80
            spell_id = read_u32(data, b + 19)
            if spell_id not in (0, 0xFFFF, 0xFFFFFFFF):
                buffs[i] = SpellBuff(
                    effect_type=data[b + 23],
                    level=data[b + 18],
                    bard_modifier=struct.unpack_from("<f", data, b + 1)[0],
                    spell_id=spell_id,
                    duration=read_u32(data, b + 14),
                    counters=read_u32(data, b + 10),
                    caster_id=read_u32(data, b + 5),
                )
        kwargs["buffs"] = buffs
        if "last_name" in offsets:
            kwargs["last_name"] = fixed(data, offsets["last_name"], 32)
        if "zone" in offsets:
            z = offsets["zone"]
            kwargs["zone_id"], kwargs["zone_instance"] = struct.unpack_from("<HH", data, z)
            kwargs["y"], kwargs["x"], kwargs["z"], kwargs["heading"] = struct.unpack_from(
                "<ffff", data, z + 4
            )
            kwargs["experience"] = struct.unpack_from("<Q", data, offsets["experience"])[0]
            (
                kwargs["bank_platinum"],
                kwargs["bank_gold"],
                kwargs["bank_silver"],
                kwargs["bank_copper"],
            ) = struct.unpack_from("<IIII", data, offsets["bank_coins"])
            kwargs["shared_platinum"] = read_u32(data, offsets["shared_platinum"])
            kwargs["guild_id"] = read_u32(data, offsets["guild_id"])
            kwargs["pvp"] = bool(data[offsets["pvp"]])
            kwargs["gm"] = bool(data[offsets["gm"]])
        obj = cls(**kwargs)
        obj._raw_packet = bytes(data)
        obj._offsets = offsets
        obj._original = obj._values()
        return obj

    def serialize(self) -> bytes:
        if not self._raw_packet:
            raise ValueError(
                "Cannot synthesize a complete RoF2 player profile; deserialize a server packet first"
            )
        changes = {k for k, v in self._values().items() if v != self._original.get(k)}
        if not changes:
            return self._raw_packet  # Exact round-trip, including original checksum.

        packet = bytearray(self._raw_packet)
        offsets = self._offsets
        for name, (fmt, offset) in self._SCALARS.items():
            if name in changes:
                if name in {"platinum", "gold", "silver", "copper"} and not self.coin_known:
                    raise ValueError("Cannot patch coin values when coin_known is false")
                struct.pack_into(fmt, packet, offset, getattr(self, name))

        if "endurance" in changes:
            struct.pack_into("<I", packet, offsets["endurance"], self.endurance)
        if "name" in changes:
            packet[offsets["name"] : offsets["name"] + 64] = b"\x00" * 64
            put_fixed(packet, offsets["name"], self.name, 64)
        if "last_name" in changes:
            if "last_name" not in offsets:
                raise ValueError("Cannot patch last name: source profile is truncated")
            packet[offsets["last_name"] : offsets["last_name"] + 32] = b"\x00" * 32
            put_fixed(packet, offsets["last_name"], self.last_name, 32)

        def patch_dict(field_name: str, start: int, count: int, fmt: str, absent: int) -> None:
            if field_name not in changes:
                return
            current = getattr(self, field_name) or {}
            original = self._original.get(field_name) or {}
            for i in set(current) | set(original):
                if not 0 <= i < count:
                    raise ValueError(f"Invalid {field_name} index: {i}")
                if current.get(i) != original.get(i):
                    struct.pack_into(
                        fmt, packet, start + i * struct.calcsize(fmt), current.get(i, absent)
                    )

        patch_dict("skills", 4616, 100, "<I", 0)
        patch_dict("spell_book", 6900, 720, "<I", 0xFFFFFFFF)
        patch_dict("gems", 9784, 16, "<i", -1)
        patch_dict("innate_skills", 5020, 25, "<I", 0)
        patch_dict("disciplines", 5124, 300, "<I", 0)
        patch_dict("recast_timers", 6412, 20, "<I", 0)
        if "aa" in changes:
            for i in set(self.aa) | set(self._original["aa"]):
                if not 0 <= i < 300:
                    raise ValueError(f"Invalid AA index: {i}")
                if self.aa.get(i) != self._original["aa"].get(i):
                    struct.pack_into("<III", packet, 1012 + i * 12, *(self.aa.get(i, (0, 0, 0))))
        if "binds" in changes:
            if len(self.binds) != 5:
                raise ValueError("RoF2 profiles require exactly 5 bind entries")
            for i, bind in enumerate(self.binds):
                struct.pack_into(
                    "<Iffff",
                    packet,
                    28 + i * 20,
                    self.home_zone_id if i == 0 and "home_zone_id" in changes else bind.zone_id,
                    bind.x,
                    bind.y,
                    bind.z,
                    bind.heading,
                )
            # `home_zone_id` aliases binds[0].zone_id; explicit home_zone_id wins.

        if "buffs" in changes:
            for i in set(self.buffs) | set(self._original["buffs"]):
                if not 0 <= i < 42:
                    raise ValueError(f"Invalid buff index: {i}")
                if self.buffs.get(i) == self._original["buffs"].get(i):
                    continue
                b = 9909 + i * 80
                buff = self.buffs.get(i)
                if buff is None:
                    packet[b : b + 80] = b"\x00" * 80
                else:
                    packet[b + 18] = buff.level & 0xFF
                    packet[b + 23] = buff.effect_type & 0xFF
                    struct.pack_into("<f", packet, b + 1, buff.bard_modifier)
                    for off, value in (
                        (5, buff.caster_id),
                        (10, buff.counters),
                        (14, buff.duration),
                        (19, buff.spell_id),
                        (32, buff.counters),
                    ):
                        struct.pack_into("<I", packet, b + off, value & 0xFFFFFFFF)
        if "zone" in offsets:
            z = offsets["zone"]
            zone_offsets = (
                ("zone_id", "<H", z),
                ("zone_instance", "<H", z + 2),
                ("y", "<f", z + 4),
                ("x", "<f", z + 8),
                ("z", "<f", z + 12),
                ("heading", "<f", z + 16),
                ("experience", "<Q", offsets["experience"]),
                ("guild_id", "<I", offsets["guild_id"]),
                ("shared_platinum", "<I", offsets["shared_platinum"]),
                ("pvp", "<B", offsets["pvp"]),
                ("gm", "<B", offsets["gm"]),
            )
            for name, fmt, off in zone_offsets:
                if name in changes:
                    struct.pack_into(fmt, packet, off, getattr(self, name))
            for i, name in enumerate(("bank_platinum", "bank_gold", "bank_silver", "bank_copper")):
                if name in changes:
                    struct.pack_into(
                        "<I", packet, offsets["bank_coins"] + 4 * i, getattr(self, name)
                    )
        else:
            missing = {
                "zone_id",
                "zone_instance",
                "x",
                "y",
                "z",
                "heading",
                "experience",
                "guild_id",
                "shared_platinum",
                "bank_platinum",
                "bank_gold",
                "bank_silver",
                "bank_copper",
                "gm",
                "pvp",
            }
            if changes & missing:
                raise ValueError("Cannot modify tail fields of a truncated profile")

        struct.pack_into("<I", packet, 4, len(packet) - 9)
        checksum = crc32(bytes(packet[8:-1])) ^ 0xFFFFFFFF
        struct.pack_into("<I", packet, 0, checksum)
        return bytes(packet)


@dataclass
class OP_SkillUpdate(EQStruct):
    skill_id: int
    value: int

    def serialize(self) -> bytes:
        # common/patches/rof2_structs.h:2549 SkillUpdate_Struct
        return struct.pack(
            "<IIBBBB",
            self.skill_id & 0xFFFFFFFF,
            self.value & 0xFFFFFFFF,
            1,
            80,
            136,
            54,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_SkillUpdate:
        need(data, 8, "OP_SkillUpdate")
        skill_id, value = struct.unpack_from("<II", data)
        return cls(int(skill_id), int(value))


@dataclass
class OP_Stamina(EQStruct):
    food: int
    water: int

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:1510
        return struct.pack(
            "<II",
            self.food & 0xFFFFFFFF,
            self.water & 0xFFFFFFFF,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_Stamina:
        need(data, 8, "OP_Stamina")
        food, water = struct.unpack_from("<II", data)
        return cls(int(food), int(water))


@dataclass
class OP_MoneyUpdate(EQStruct):
    platinum: int
    gold: int
    silver: int
    copper: int

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:3804 MoneyUpdate_Struct
        return struct.pack(
            "<iiii",
            i32(self.platinum),
            i32(self.gold),
            i32(self.silver),
            i32(self.copper),
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_MoneyUpdate:
        need(data, 16, "OP_MoneyUpdate")
        platinum, gold, silver, copper = struct.unpack_from("<iiii", data)
        return cls(int(platinum), int(gold), int(silver), int(copper))


@dataclass
class OP_ManaChange(EQStruct):
    new_mana: int
    stamina: int = 0
    spell_id: int = 0
    keep_casting: int = 0
    slot: int = -1

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:462 ManaChange_Struct
        return struct.pack(
            "<IIIB3si",
            self.new_mana & 0xFFFFFFFF,
            self.stamina & 0xFFFFFFFF,
            self.spell_id & 0xFFFFFFFF,
            self.keep_casting & 0xFF,
            b"\x00\x00\x00",
            i32(self.slot),
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ManaChange:
        need(data, 4, "OP_ManaChange")
        new_mana = read_u32(data)
        stamina = read_u32(data, 4) if len(data) >= 8 else 0
        spell_id = read_u32(data, 8) if len(data) >= 12 else 0
        keep = data[12] if len(data) > 12 else 0
        slot = struct.unpack_from("<i", data, 16)[0] if len(data) >= 20 else -1
        return cls(int(new_mana), int(stamina), int(spell_id), int(keep), int(slot))


@dataclass
class OP_ExpUpdate(EQStruct):
    exp: int
    aa_exp: int = 0

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:1531 ExpUpdate_Struct
        return struct.pack(
            "<II",
            self.exp & 0xFFFFFFFF,
            self.aa_exp & 0xFFFFFFFF,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ExpUpdate:
        need(data, 4, "OP_ExpUpdate")
        exp = read_u32(data)
        aa_exp = read_u32(data, 4) if len(data) >= 8 else 0
        return cls(int(exp), int(aa_exp))


@dataclass
class OP_LevelUpdate(EQStruct):
    level: int
    level_old: int
    exp: int

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:1519 LevelUpdate_Struct
        return struct.pack(
            "<III",
            self.level & 0xFFFFFFFF,
            self.level_old & 0xFFFFFFFF,
            self.exp & 0xFFFFFFFF,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_LevelUpdate:
        need(data, 12, "OP_LevelUpdate")
        level, old, exp = struct.unpack_from("<III", data)
        return cls(int(level), int(old), int(exp))


@dataclass
class OP_Buff(EQStruct):
    entity_id: int
    buff: SpellBuff
    slot_id: int = 0
    fade: int = 0

    def serialize(self) -> bytes:
        packet = bytearray(100)
        # common/patches/rof2_structs.h:776 SpellBuffPacket_Struct
        struct.pack_into("<I", packet, 0, self.entity_id & 0xFFFFFFFF)
        packet[4] = self.buff.effect_type & 0xFF
        packet[5] = self.buff.level & 0xFF
        # common/patches/rof2_structs.h:762 SpellBuff_Struct
        # bard_modifier through y. The buff starts 4 bytes after entity id.
        struct.pack_into(
            "<fIIIIf",
            packet,
            8,
            1.0,
            self.buff.spell_id & 0xFFFFFFFF,
            self.buff.duration & 0xFFFFFFFF,
            self.buff.caster_id & 0xFFFFFFFF,
            self.buff.counters & 0xFFFFFFFF,
            0.0,
        )
        # common/patches/rof2_structs.h:778 SpellBuffPacket_Struct
        fade = 2
        if self.fade:
            fade = 1
        struct.pack_into(
            "<II",
            packet,
            92,
            self.slot_id & 0xFFFFFFFF,
            fade,
        )
        return bytes(packet)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_Buff:
        need(data, 100, "OP_Buff")
        entity_id = read_u32(data)
        effect = data[4]
        level = data[5]
        spell_id = read_u32(data, 12)
        duration = read_u32(data, 16)
        caster_id = read_u32(data, 20)
        counters = read_u32(data, 24)
        slot_id = read_u32(data, 92)
        fade = 1 if read_u32(data, 96) == 1 else 0
        buff = SpellBuff(
            int(effect),
            int(level),
            0,
            0,
            int(spell_id),
            int(duration),
            int(counters),
            int(caster_id),
        )
        return cls(int(entity_id), buff, int(slot_id), int(fade))


@dataclass
class OP_GMTraining(EQStruct):
    npc_id: int
    player_id: int
    skills: tuple[int, ...] = ()

    def serialize(self) -> bytes:
        packet = bytearray(GM_TRAINING_SIZE)
        # common/eq_packet_structs.h:608 GMTrainee_Struct
        struct.pack_into(
            "<II",
            packet,
            0,
            self.npc_id & 0xFFFFFFFF,
            self.player_id & 0xFFFFFFFF,
        )
        values = list(self.skills[:GM_SKILL_COUNT])
        values.extend([0] * (GM_SKILL_COUNT - len(values)))
        # common/eq_packet_structs.h:610 GMTrainee_Struct
        struct.pack_into(
            "<100I",
            packet,
            8,
            *(value & 0xFFFFFFFF for value in values),
        )
        return bytes(packet)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_GMTraining:
        need(data, 8, "OP_GMTraining")
        npc_id, player_id = struct.unpack_from("<II", data)
        skills: tuple[int, ...] = ()
        if len(data) >= 8 + GM_SKILL_COUNT * 4:
            skills = tuple(int(value) for value in struct.unpack_from("<100I", data, 8))
        return cls(int(npc_id), int(player_id), skills)


@dataclass
class OP_GMTrainSkill(EQStruct):
    npc_id: int
    skill_id: int
    skill_bank: int = 0

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:622 GMSkillChange_Struct
        return struct.pack(
            "<H2sH2sH2s",
            self.npc_id & 0xFFFF,
            b"\x00\x00",
            self.skill_bank & 0xFFFF,
            b"\x00\x00",
            self.skill_id & 0xFFFF,
            b"\x00\x00",
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_GMTrainSkill:
        need(data, 12, "OP_GMTrainSkill")
        npc_id, _pad1, skill_bank, _pad2, skill_id, _pad3 = struct.unpack_from("<H2sH2sH2s", data)
        return cls(int(npc_id), int(skill_id), int(skill_bank))


@dataclass
class OP_GMEndTraining(EQStruct):
    npc_id: int
    player_id: int

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:615 GMTrainEnd_Struct
        return struct.pack("<II", self.npc_id & 0xFFFFFFFF, self.player_id & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_GMEndTraining:
        need(data, 8, "OP_GMEndTraining")
        npc_id, player_id = struct.unpack_from("<II", data)
        return cls(int(npc_id), int(player_id))


@dataclass
class OP_ReadBook(EQStruct):
    """RoF2 BookRequest_Struct, used for both requests and responses.

    Client -> Server:
        txtfile identifies the book record to retrieve.

    Server -> Client:
        txtfile contains the actual readable book text.

    The internal EQEmu BookRequest_Struct and BookText_Struct have
    different layouts. This models the RoF2 wire representation.
    """

    window: int = 0xFFFFFFFF

    # TypelessInventorySlot_Struct (8 bytes)
    slot: int = -1
    sub_index: int = -1
    aug_index: int = -1
    slot_unknown: int = 0

    type: int = 1
    target_id: int = 0
    can_cast: int = 0
    can_scribe: int = 0
    txtfile: str = ""

    SIZE = 8216
    FORMAT = "<I4hIIBB8194s"

    def serialize(self) -> bytes:
        # Latin-1 preserves individual byte values for round-tripping.
        encoded = self.txtfile.encode("latin-1")

        if len(encoded) >= 8194:
            raise ValueError("OP_ReadBook txtfile exceeds 8193 bytes")

        return struct.pack(
            self.FORMAT,
            self.window,
            self.slot,
            self.sub_index,
            self.aug_index,
            self.slot_unknown,
            self.type,
            self.target_id,
            self.can_cast,
            self.can_scribe,
            encoded,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ReadBook:
        exact(data, cls.SIZE, cls.__name__)

        (
            window,
            slot,
            sub_index,
            aug_index,
            slot_unknown,
            type_,
            target_id,
            can_cast,
            can_scribe,
            txtfile,
        ) = struct.unpack(cls.FORMAT, data)

        return cls(
            window=window,
            slot=slot,
            sub_index=sub_index,
            aug_index=aug_index,
            slot_unknown=slot_unknown,
            type=type_,
            target_id=target_id,
            can_cast=can_cast,
            can_scribe=can_scribe,
            txtfile=txtfile.split(b"\x00", 1)[0].decode("latin-1"),
        )
