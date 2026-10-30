from __future__ import annotations

import struct
from dataclasses import dataclass, field

from eqclient3.log import log
from eqclient3.structs.wire import (
    EQStruct,
    _advance,
    _cstring,
    _fixed,
    _i32,
    _need,
    _put_cstr,
    _put_fixed,
    _read_u32,
    _u32,
)

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
class OP_PlayerProfile(EQStruct):
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

    def serialize(self) -> bytes:
        packet = bytearray(PROFILE_SIZE)
        packet[16] = self.gender & 0xFF
        # common/patches/rof2.cpp:2519 PlayerProfile race
        struct.pack_into("<I", packet, 17, self.race & 0xFFFFFFFF)
        packet[21] = self.class_id & 0xFF
        packet[22] = self.level & 0xFF
        # common/patches/rof2.cpp:2529 PlayerProfile bind zone_id
        struct.pack_into("<I", packet, 28, self.home_zone_id & 0xFFFFFFFF)
        # common/patches/rof2.cpp:2536 PlayerProfile deity
        struct.pack_into("<I", packet, 128, self.deity & 0xFFFFFFFF)
        # common/patches/rof2.cpp:2630 PlayerProfile points
        struct.pack_into("<III", packet, 940, self.points & 0xFFFFFFFF, self.mana & 0xFFFFFFFF, self.hp & 0xFFFFFFFF)
        # common/patches/rof2.cpp:2634 PlayerProfile STR
        struct.pack_into(
            "<IIIIIII",
            packet,
            952,
            self.strength & 0xFFFFFFFF,
            self.stamina & 0xFFFFFFFF,
            self.charisma & 0xFFFFFFFF,
            self.dexterity & 0xFFFFFFFF,
            self.intelligence & 0xFFFFFFFF,
            self.agility & 0xFFFFFFFF,
            self.wisdom & 0xFFFFFFFF,
        )
        skills = [0] * 100
        for index, value in (self.skills or {}).items():
            if 0 <= int(index) < 100:
                skills[int(index)] = int(value) & 0xFFFFFFFF
        # common/patches/rof2.cpp:2672 PlayerProfile skills
        struct.pack_into("<100I", packet, 4616, *skills)
        book = [0xFFFFFFFF] * 720
        for index, spell in self.spell_book.items():
            if 0 <= int(index) < 720:
                book[int(index)] = int(spell) & 0xFFFFFFFF
        # common/patches/rof2_structs.h:1173 spell_book
        struct.pack_into("<720I", packet, 6500, *book)
        gems = [-1] * 16
        for index, spell in self.gems.items():
            if 0 <= int(index) < 16:
                gems[int(index)] = _i32(spell)
        # common/patches/rof2_structs.h:1175 mem_spells. Empty gems are -1.
        struct.pack_into("<16i", packet, 9384, *gems)
        if self.coin_known:
            # common/patches/rof2_structs.h:1181 platinum
            struct.pack_into(
                "<IIII",
                packet,
                12869,
                self.platinum & 0xFFFFFFFF,
                self.gold & 0xFFFFFFFF,
                self.silver & 0xFFFFFFFF,
                self.copper & 0xFFFFFFFF,
            )
        # common/patches/rof2_structs.h:1203 bandolier_count
        struct.pack_into("<I", packet, 12955, 20)
        # common/patches/rof2_structs.h:1205 potionbelt_count
        struct.pack_into("<I", packet, 13699, 5)
        # common/patches/rof2_structs.h:1222 name_str_len
        struct.pack_into("<I", packet, 13844, 64)
        # common/patches/rof2_structs.h:1223 name
        _put_fixed(packet, 13848, self.name, 64)
        return bytes(packet)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_PlayerProfile:
        _need(data, 23, "OP_PlayerProfile")
        gender = data[16]
        race = _read_u32(data, 17)
        class_id = data[21]
        level = data[22]
        home_zone_id = _read_u32(data, 28) if len(data) >= 32 else 0
        deity = _read_u32(data, 128) if len(data) >= 132 else 0
        points = mana = hp = 0
        strength = stamina = charisma = dexterity = intelligence = agility = wisdom = 0
        if len(data) >= 980:
            points, mana, hp = struct.unpack_from("<III", data, 940)
            strength, stamina, charisma, dexterity, intelligence, agility, wisdom = struct.unpack_from(
                "<IIIIIII", data, 952
            )
        platinum = gold = silver = copper = 0
        coin_known = False
        if len(data) >= 12885:
            platinum, gold, silver, copper = struct.unpack_from("<IIII", data, 12869)
            coin_known = True
        skills: dict[int, int] | None = None
        if len(data) >= 4616 + 400:
            raw = struct.unpack_from("<100I", data, 4616)
            skills = {index: int(value) for index, value in enumerate(raw)}
        book: dict[int, int] = {}
        gems: dict[int, int] = {}
        if len(data) >= 6500 + 720 * 4:
            for index, spell in enumerate(struct.unpack_from("<720I", data, 6500)):
                if spell not in (0, 0xFFFFFFFF):
                    book[index] = int(spell)
        if len(data) >= 9384 + 16 * 4:
            for index, spell in enumerate(struct.unpack_from("<16i", data, 9384)):
                if spell not in (0, -1):
                    gems[index] = int(spell)
        name = _profile_name(data)
        return cls(
            name,
            int(gender),
            int(race),
            int(class_id),
            int(level),
            int(deity),
            int(home_zone_id),
            int(points),
            int(hp),
            int(mana),
            int(strength),
            int(stamina),
            int(charisma),
            int(dexterity),
            int(intelligence),
            int(agility),
            int(wisdom),
            int(platinum),
            int(gold),
            int(silver),
            int(copper),
            coin_known,
            skills,
            book,
            gems,
        )


def _profile_name(data: bytes) -> str:
    """Name sits after the bandolier and potion strings, which vary in length."""
    offset = 12955
    if len(data) < offset + 4:
        return ""
    try:
        count = _read_u32(data, offset)
        offset += 4
        for _bandolier in range(count):
            _name, offset = _cstring(data, offset)
            for _item in range(4):
                _item_name, offset = _cstring(data, offset)
                offset = _advance(data, offset, 8, "OP_PlayerProfile")
        potions = _read_u32(data, offset)
        offset += 4
        for _potion in range(potions):
            _potion_name, offset = _cstring(data, offset)
            offset = _advance(data, offset, 8, "OP_PlayerProfile")
        offset = _advance(data, offset, 96, "OP_PlayerProfile")
    except ValueError:
        log.error("OP_PlayerProfile name walk failed", exc_info=True)
        return ""
    if len(data) < offset + 5:
        return ""
    return _fixed(data, offset + 4, 64)


@dataclass
class OP_SkillUpdate(EQStruct):
    skill_id: int
    value: int

    def serialize(self) -> bytes:
        # common/patches/rof2_structs.h:2549 SkillUpdate_Struct
        return struct.pack("<IIBBBB", self.skill_id & 0xFFFFFFFF, self.value & 0xFFFFFFFF, 1, 80, 136, 54)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_SkillUpdate:
        _need(data, 8, "OP_SkillUpdate")
        skill_id, value = struct.unpack_from("<II", data)
        return cls(int(skill_id), int(value))


@dataclass
class OP_Stamina(EQStruct):
    food: int
    water: int

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:1510
        return struct.pack("<II", self.food & 0xFFFFFFFF, self.water & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_Stamina:
        _need(data, 8, "OP_Stamina")
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
        return struct.pack("<iiii", _i32(self.platinum), _i32(self.gold), _i32(self.silver), _i32(self.copper))

    @classmethod
    def deserialize(cls, data: bytes) -> OP_MoneyUpdate:
        _need(data, 16, "OP_MoneyUpdate")
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
            _i32(self.slot),
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ManaChange:
        _need(data, 4, "OP_ManaChange")
        new_mana = _read_u32(data)
        stamina = _read_u32(data, 4) if len(data) >= 8 else 0
        spell_id = _read_u32(data, 8) if len(data) >= 12 else 0
        keep = data[12] if len(data) > 12 else 0
        slot = struct.unpack_from("<i", data, 16)[0] if len(data) >= 20 else -1
        return cls(int(new_mana), int(stamina), int(spell_id), int(keep), int(slot))


@dataclass
class OP_ExpUpdate(EQStruct):
    exp: int
    aa_exp: int = 0

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:1531 ExpUpdate_Struct
        return struct.pack("<II", self.exp & 0xFFFFFFFF, self.aa_exp & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ExpUpdate:
        _need(data, 4, "OP_ExpUpdate")
        exp = _read_u32(data)
        aa_exp = _read_u32(data, 4) if len(data) >= 8 else 0
        return cls(int(exp), int(aa_exp))


@dataclass
class OP_LevelUpdate(EQStruct):
    level: int
    level_old: int
    exp: int

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:1519 LevelUpdate_Struct
        return struct.pack("<III", self.level & 0xFFFFFFFF, self.level_old & 0xFFFFFFFF, self.exp & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_LevelUpdate:
        _need(data, 12, "OP_LevelUpdate")
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
        struct.pack_into("<II", packet, 92, self.slot_id & 0xFFFFFFFF, 1 if self.fade else 2)
        return bytes(packet)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_Buff:
        _need(data, 100, "OP_Buff")
        entity_id = _read_u32(data)
        effect = data[4]
        level = data[5]
        spell_id = _read_u32(data, 12)
        duration = _read_u32(data, 16)
        caster_id = _read_u32(data, 20)
        counters = _read_u32(data, 24)
        slot_id = _read_u32(data, 92)
        fade = 1 if _read_u32(data, 96) == 1 else 0
        buff = SpellBuff(int(effect), int(level), 0, 0, int(spell_id), int(duration), int(counters), int(caster_id))
        return cls(int(entity_id), buff, int(slot_id), int(fade))


@dataclass
class OP_GMTraining(EQStruct):
    npc_id: int
    player_id: int
    skills: tuple[int, ...] = ()

    def serialize(self) -> bytes:
        packet = bytearray(GM_TRAINING_SIZE)
        # common/eq_packet_structs.h:608 GMTrainee_Struct
        struct.pack_into("<II", packet, 0, self.npc_id & 0xFFFFFFFF, self.player_id & 0xFFFFFFFF)
        values = list(self.skills[:GM_SKILL_COUNT])
        values.extend([0] * (GM_SKILL_COUNT - len(values)))
        # common/eq_packet_structs.h:610 GMTrainee_Struct
        struct.pack_into("<100I", packet, 8, *(value & 0xFFFFFFFF for value in values))
        return bytes(packet)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_GMTraining:
        _need(data, 8, "OP_GMTraining")
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
        _need(data, 12, "OP_GMTrainSkill")
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
        _need(data, 8, "OP_GMEndTraining")
        npc_id, player_id = struct.unpack_from("<II", data)
        return cls(int(npc_id), int(player_id))


@dataclass
class OP_ReadBook(EQStruct):
    spell_id: int = 0
    window: int = 0
    book_type: int = 0
    text_file: str = ""

    def serialize(self) -> bytes:
        if self.text_file:
            return bytes((self.window & 0xFF, self.book_type & 0xFF)) + _put_cstr(self.text_file)
        # No RoF2 DECODE accepts a spell id. BookRequest_Struct is 8216 bytes
        # (common/patches/rof2_structs.h:2899) and the server looks books up by txtfile.
        # The scribe call site sends these 4 bytes; leave them, do not expand to 8216.
        return _u32(self.spell_id)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ReadBook:
        if len(data) == 4:
            return cls(_read_u32(data))
        if len(data) >= 3:
            try:
                text_file, _end = _cstring(data, 2)
            except ValueError:
                text_file = ""
            return cls(0, int(data[0]), int(data[1]), text_file)
        raise ValueError(f"OP_ReadBook is {len(data)} bytes")
