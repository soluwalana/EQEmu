"""Packet-driven character state for EQEmu RoF2 (movement and inventory excluded).

Place at eqclient4/character.py. Operates on *decoded* EQStruct packets, like
CharacterInventory. Only apply authoritative server packets; do not infer
merchant payments from client requests or turn AA rank definitions into owned AAs.
"""

import pickle
from copy import deepcopy
from dataclasses import dataclass
from typing import Self

from eqclient4.structs import (
    BuffIconEntry,
    OP_AAExpUpdate,
    OP_Buff,
    OP_BuffCreate,
    OP_EnduranceUpdate,
    OP_ExpUpdate,
    OP_HPUpdate,
    OP_LevelUpdate,
    OP_ManaChange,
    OP_ManaUpdate,
    OP_MobHealth,
    OP_MoneyUpdate,
    OP_NewSpawn,
    OP_PlayerProfile,
    OP_RespondAA,
    OP_SendAATable,
    OP_SkillUpdate,
    OP_Stamina,
    ProfileBind,
    SpellBuff,
)
from eqclient4.structs.wire import EQStruct


@dataclass(frozen=True)
class CharacterEvent:
    action: str
    message: str
    changed: bool = False

    def __str__(self) -> str:
        return f"{self.action}: {self.message}"


@dataclass(frozen=True)
class OwnedAA:
    """One of the 300 profile/RespondAA slots, *not* an AA ability definition.

    rank_id is the actual AA rank ID; value is the cumulative points spent for
    that rank, and charges is the charge count. index preserves wire ordering.
    """

    index: int
    rank_id: int
    value: int
    charges: int


class Abilities:
    """Ordinary skills plus equipment-derived combat capabilities.

    Kept compatible with the existing eqclient4.world.Abilities contract.
    Innate skills, spells, and alternate advancement use separate namespaces.
    """

    def __init__(self) -> None:
        self.skills: dict[int, int] = {}
        self.can_bash: bool = False
        self.shield: bool = False
        self.two_hand: bool = False


class Character:
    """A single character's non-movement, non-inventory state.

    OP_PlayerProfile initializes the character. Incremental server packets
    update matching fields. AA ownership and the AA rank catalog are separate.
    Incoming entity-scoped packets are ignored until self_id is known.
    """

    def __init__(self, name: str = "") -> None:
        self.name: str = name
        self.last_name: str = ""
        self.loaded: bool = False
        self.abilities: Abilities = Abilities()
        self.tutorial_started: bool = False
        self.quest_started: bool = False

        self.self_id: int = 0
        self.class_id: int = 0
        self.race: int = 0
        self.gender: int = 0
        self.deity: int = 0
        self.level: int = 0
        self.exp: int = 0
        self.training_points: int = 0
        self.points: int = 0
        self.hp: int = 0
        self.max_hp: int = 0
        self.hp_percent: int | None = None
        self.mana: int = 0
        self.max_mana: int = 0
        self.endurance: int = 0
        self.max_endurance: int = 0
        self.food: int = 0
        self.water: int = 0
        self.strength: int = 0
        self.stamina: int = 0
        self.agility: int = 0
        self.dexterity: int = 0
        self.wisdom: int = 0
        self.intelligence: int = 0
        self.charisma: int = 0

        self._coin: tuple[int, int, int, int] = (0, 0, 0, 0)
        self.coin_known: bool = False
        self.cursor_coin: tuple[int, int, int, int] = (0, 0, 0, 0)
        self.bank_coin: tuple[int, int, int, int] = (0, 0, 0, 0)
        self.shared_platinum: int = 0

        self.home_zone_id: int = 0
        self.zone_id: int = 0
        self.zone_instance: int = 0
        self.binds: list[ProfileBind] = []
        self.guild_id: int = 0
        self.gm: bool = False
        self.pvp: bool = False

        self.innate_skills: dict[int, int] = {}
        self.disciplines: dict[int, int] = {}
        self.recast_timers: dict[int, int] = {}
        self.spell_book: dict[int, int] = {}
        self.gems: dict[int, int] = {}
        self.buffs: dict[int, SpellBuff] = {}
        self.buff_icons: dict[int, BuffIconEntry] = {}

        # AA snapshots use rank IDs; catalog definitions also expose a distinct
        # ability ID (OP_SendAATable.seq). Do not merge the two namespaces.
        self.aa_owned: dict[int, OwnedAA] = {}  # keyed by rank ID
        self.aa_slots: dict[int, OwnedAA] = {}  # keyed by profile table index
        self.aa_ranks: dict[int, OP_SendAATable] = {}  # rank ID -> definition
        self.aa_points: int = 0  # unspent points, from profile or AAExpUpdate
        self.aa_points_spent: int = 0
        self.aa_points_assigned: int = 0  # RespondAA header; NOT unspent points
        self.aa_spent_general: int = 0
        self.aa_spent_archetype: int = 0
        self.aa_spent_class: int = 0
        self.aa_spent_special: int = 0
        self.aa_experience_scaled: int = 0  # AAExpUpdate first u32 (server scales to 330)
        self.aa_experience_from_exp_update: int = 0  # ExpUpdate second u32, when present
        self.aa_xp_allocation_percent: int = 0  # AAExpUpdate aaxp_percent

        self.changes: list[CharacterEvent] = []

    def _event(self, action: str, message: str, changed: bool = False) -> CharacterEvent:
        event = CharacterEvent(action, message, changed)
        self.changes.append(event)
        return event

    def ability_known(self, skill_id: int) -> bool:
        return 0 < int(self.abilities.skills.get(int(skill_id), 0)) < 0xFFFFFFFF

    @property
    def coin(self) -> tuple[int, int, int, int]:
        return self._coin

    @coin.setter
    def coin(self, value: tuple[int, int, int, int]) -> None:
        self._coin = (int(value[0]), int(value[1]), int(value[2]), int(value[3]))
        self.coin_known = True

    @property
    def total_copper(self) -> int:
        p, g, s, c = self.coin
        return p * 1000 + g * 100 + s * 10 + c

    def set_coin(self, platinum: int, gold: int, silver: int, copper: int) -> None:
        self.coin = (int(platinum), int(gold), int(silver), int(copper))

    def add_coins(self, platinum: int, gold: int, silver: int, copper: int) -> None:
        """Add denominations and normalize into canonical coin counts."""
        value = 1000 * platinum + 100 * gold + 10 * silver + copper
        self.add_coin(value)

    def add_coin(self, coin: int) -> None:
        value = self.total_copper + int(coin)
        if value < 0:
            raise ValueError("Insufficient funds")
        p, value = divmod(value, 1000)
        g, value = divmod(value, 100)
        s, c = divmod(value, 10)
        self.set_coin(p, g, s, c)

    def deduct_coins(
        self,
        price: int,
    ) -> tuple[int, int, int, int] | None:
        """Deduct copper-denominated price, matching EQEmu's TakeMoneyFromPP."""
        plat, gold, silver, copper = self.coin

        if price < 0:
            raise ValueError("Negative price")

        total = plat * 1000 + gold * 100 + silver * 10 + copper
        if price > total:
            return None  # Insufficient funds

        if copper >= price:
            return plat, gold, silver, copper - price

        price -= copper
        copper = 0

        if silver * 10 >= price:
            silver, copper = divmod(silver * 10 - price, 10)
            return plat, gold, silver, copper

        price -= silver * 10
        silver = 0

        if gold * 100 >= price:
            gold, remainder = divmod(gold * 100 - price, 100)
            silver, copper = divmod(remainder, 10)
            return plat, gold, silver, copper

        price -= gold * 100
        gold = 0

        plat, remainder = divmod(plat * 1000 - price, 1000)
        gold, remainder = divmod(remainder, 100)
        silver, copper = divmod(remainder, 10)

        return plat, gold, silver, copper

    def set_owned_aa(self, entries: dict[int, tuple[int, int, int]]) -> None:
        """Atomically replace owned ranks from the 300-entry AA snapshot."""
        slots: dict[int, OwnedAA] = {}
        owned: dict[int, OwnedAA] = {}
        for index, (rank_id, value, charges) in entries.items():
            if not 0 <= index < 300:
                raise ValueError(f"AA index outside 300-entry table: {index}")
            if rank_id <= 0:
                continue
            entry = OwnedAA(int(index), int(rank_id), int(value), int(charges))
            slots[index] = entry
            owned[rank_id] = entry
        self.aa_slots = slots
        self.aa_owned = owned

    def aa_known(self, rank_id: int) -> bool:
        return int(rank_id) in self.aa_owned

    def aa_rank(self, rank_id: int) -> OP_SendAATable | None:
        return self.aa_ranks.get(int(rank_id))

    def aa_ability(self, ability_id: int) -> list[OP_SendAATable]:
        """All catalogued ranks in this ability, sorted by rank sequence."""
        return sorted(
            (rank for rank in self.aa_ranks.values() if rank.seq == ability_id),
            key=lambda rank: rank.current_level,
        )

    @classmethod
    def from_packet(cls, packet: OP_PlayerProfile) -> Self:
        result = cls(packet.name)
        result.load(packet)
        return result

    @classmethod
    def from_payload(cls, payload: bytes) -> Self:
        return cls.from_packet(OP_PlayerProfile.deserialize(payload))

    def load(self, packet: OP_PlayerProfile) -> CharacterEvent:
        """Authoritative profile snapshot; preserve identity and AA catalog."""
        self.loaded = True
        if packet.name:
            self.name = packet.name
        self.last_name = packet.last_name
        for attr in (
            "gender",
            "race",
            "class_id",
            "level",
            "deity",
            "home_zone_id",
            "points",
            "hp",
            "mana",
            "strength",
            "stamina",
            "charisma",
            "dexterity",
            "intelligence",
            "agility",
            "wisdom",
            "endurance",
            "zone_id",
            "zone_instance",
            "guild_id",
            "gm",
            "pvp",
            "shared_platinum",
            "aa_points",
            "aa_points_spent",
        ):
            setattr(self, attr, getattr(packet, attr))
        self.training_points = packet.points
        self.exp = packet.experience
        self.max_hp = 0  # not present in OP_PlayerProfile
        self.max_mana = 0
        self.max_endurance = 0
        self.hp_percent = None
        self.coin_known = packet.coin_known
        self._coin = (packet.platinum, packet.gold, packet.silver, packet.copper)
        self.cursor_coin = (
            packet.cursor_platinum,
            packet.cursor_gold,
            packet.cursor_silver,
            packet.cursor_copper,
        )
        self.bank_coin = (
            packet.bank_platinum,
            packet.bank_gold,
            packet.bank_silver,
            packet.bank_copper,
        )
        if packet.skills is not None:
            self.abilities.skills = {
                int(k): int(v) for k, v in packet.skills.items() if v != 0xFFFFFFFF
            }
        self.innate_skills = dict(packet.innate_skills)
        self.disciplines = dict(packet.disciplines)
        self.recast_timers = dict(packet.recast_timers)
        self.spell_book = dict(packet.spell_book)
        self.gems = dict(packet.gems)
        self.binds = deepcopy(packet.binds)
        self.buffs = deepcopy(packet.buffs)
        self.buff_icons.clear()
        self.set_owned_aa(packet.aa)
        # NOTE: packet.x/y/z/heading intentionally belong to Movement, not Character.
        return self._event("profile", f"Loaded {self.name!r} level {self.level}", True)

    def _is_self(self, entity_id: int) -> bool:
        return self.self_id != 0 and (int(entity_id) & 0xFFFF) == (self.self_id & 0xFFFF)

    def apply(self, packet: EQStruct, from_server: bool = True) -> CharacterEvent | None:
        """Apply one already-decoded authoritative update; return a change event.

        Pass from_server=False for client-originated packets. Self-scoped HP,
        mana, endurance, and buff updates require self_id to have been assigned.
        """
        if not from_server:
            return self._event("ignored", f"Client-originated {type(packet).__name__}")

        match packet:

            case OP_NewSpawn():
                if packet.spawn.name == self.name and packet.spawn.npc == 0:
                    self.self_id = packet.spawn.spawn_id
                    return self._event("new-spawn", f"New spawn {self.self_id}", True)

            case OP_PlayerProfile():
                return self.load(packet)

            case OP_SkillUpdate():
                prior = self.abilities.skills.get(packet.skill_id)
                self.abilities.skills[packet.skill_id] = packet.value
                return self._event(
                    "skill",
                    f"Skill {packet.skill_id}: {prior} -> {packet.value}",
                    prior != packet.value,
                )

            case OP_Stamina():
                changed = (self.food, self.water) != (packet.food, packet.water)
                self.food, self.water = packet.food, packet.water
                return self._event("stamina", f"Food {self.food}, water {self.water}", changed)

            case OP_MoneyUpdate():
                previous_coin = self.coin
                self.set_coin(packet.platinum, packet.gold, packet.silver, packet.copper)
                return self._event(
                    "money",
                    f"Balance {self.coin} ({self.total_copper} copper)",
                    previous_coin != self.coin,
                )

            case OP_ExpUpdate():
                changed = self.exp != packet.exp
                self.exp = packet.exp
                self.aa_experience_from_exp_update = packet.aa_exp
                return self._event("experience", f"Experience {self.exp}", changed)

            case OP_LevelUpdate():
                changed = (self.level, self.exp) != (packet.level, packet.exp)
                self.level, self.exp = packet.level, packet.exp
                return self._event("level", f"Level {self.level}, experience {self.exp}", changed)

            case OP_HPUpdate():
                if not self._is_self(packet.spawn_id):
                    return self._event(
                        "ignored", "HP update belongs to another spawn (or self_id is unknown)"
                    )
                changed = (self.hp, self.max_hp) != (packet.cur_hp, packet.max_hp)
                self.hp, self.max_hp = packet.cur_hp, packet.max_hp
                self.hp_percent = round(100 * self.hp / self.max_hp) if self.max_hp > 0 else None
                return self._event("hp", f"HP {self.hp}/{self.max_hp}", changed)

            case OP_MobHealth():
                if not self._is_self(packet.spawn_id):
                    return self._event("ignored", "MobHealth belongs to another spawn")
                changed = self.hp_percent != packet.percent
                self.hp_percent = packet.percent
                return self._event("hp-percent", f"HP {packet.percent}%", changed)

            case OP_ManaUpdate():
                if not self._is_self(packet.spawn_id):
                    return self._event("ignored", "ManaUpdate belongs to another spawn")
                changed = (self.mana, self.max_mana) != (packet.cur_mana, packet.max_mana)
                self.mana, self.max_mana = packet.cur_mana, packet.max_mana
                return self._event("mana", f"Mana {self.mana}/{self.max_mana}", changed)

            case OP_EnduranceUpdate():
                if not self._is_self(packet.spawn_id):
                    return self._event("ignored", "EnduranceUpdate belongs to another spawn")
                changed = (self.endurance, self.max_endurance) != (packet.cur_end, packet.max_end)
                self.endurance, self.max_endurance = packet.cur_end, packet.max_end
                return self._event(
                    "endurance", f"Endurance {self.endurance}/{self.max_endurance}", changed
                )

            case OP_ManaChange():
                changed = self.mana != packet.new_mana
                self.mana = packet.new_mana
                return self._event("mana", f"Mana {self.mana}", changed)

            case OP_Buff():
                if not self._is_self(packet.entity_id):
                    return self._event("ignored", "Buff belongs to another entity")
                before = self.buffs.get(packet.slot_id)
                if packet.fade or packet.buff.spell_id in (0, 0xFFFF, 0xFFFFFFFF):
                    self.buffs.pop(packet.slot_id, None)
                    self.buff_icons.pop(packet.slot_id, None)
                    return self._event(
                        "buff-fade", f"Buff slot {packet.slot_id}", before is not None
                    )
                self.buffs[packet.slot_id] = deepcopy(packet.buff)
                return self._event(
                    "buff",
                    f"Slot {packet.slot_id}: spell {packet.buff.spell_id}",
                    before != packet.buff,
                )

            case OP_BuffCreate():
                if not self._is_self(packet.entity_id):
                    return self._event("ignored", "Buff icons belong to another entity")

                previous_buffs = self.buff_icons.copy()
                if packet.all_buffs:
                    self.buff_icons.clear()
                for entry in packet.entries:
                    if entry.spell_id in (0, 0xFFFF, 0xFFFFFFFF):
                        self.buff_icons.pop(entry.buff_slot, None)
                    else:
                        self.buff_icons[entry.buff_slot] = deepcopy(entry)

                return self._event(
                    "buff-icons",
                    f"{len(self.buff_icons)} buff icons",
                    previous_buffs != self.buff_icons,
                )

            case OP_RespondAA():
                previous = (self.aa_slots, self.aa_points_spent)
                self.set_owned_aa({e.index: (e.aa, e.value, e.charges) for e in packet.entries})
                self.aa_points_spent = packet.aa_spent
                self.aa_points_assigned = packet.aapoints_assigned
                self.aa_spent_general = packet.aa_spent_general
                self.aa_spent_archetype = packet.aa_spent_archetype
                self.aa_spent_class = packet.aa_spent_class
                self.aa_spent_special = packet.aa_spent_special
                return self._event(
                    "aa-owned",
                    f"{len(self.aa_owned)} owned AA ranks, {self.aa_points_spent} points spent",
                    previous != (self.aa_slots, self.aa_points_spent),
                )

            case OP_SendAATable():
                previous_aa_rank = self.aa_ranks.get(packet.aa_id)
                self.aa_ranks[packet.aa_id] = deepcopy(packet)
                return self._event(
                    "aa-catalog",
                    f"Rank {packet.aa_id}, ability {packet.seq}, cost {packet.cost}",
                    previous_aa_rank != packet,
                )

            case OP_AAExpUpdate():
                prior_aa_exp = (
                    self.aa_points,
                    self.aa_experience_scaled,
                    self.aa_xp_allocation_percent,
                )
                self.aa_points = packet.aapoints_unspent
                self.aa_experience_scaled = packet.unknown00
                self.aa_xp_allocation_percent = packet.aaxp_percent
                return self._event(
                    "aa-experience",
                    f"AA unspent {self.aa_points}, scaled XP {self.aa_experience_scaled}",
                    prior_aa_exp
                    != (self.aa_points, self.aa_experience_scaled, self.aa_xp_allocation_percent),
                )

            case _:
                return self._event(
                    "ignored", f"{type(packet).__name__} is not a character-state update"
                )

        return None

    def render_change(self, event: CharacterEvent) -> str:
        return str(event)

    def render(self) -> str:
        return "\n".join(
            (
                f"CHARACTER  {self.name} {self.last_name}".rstrip(),
                "=" * 62,
                f"Spawn {self.self_id} | class {self.class_id} race {self.race} | level {self.level}",
                f"HP {self.hp}/{self.max_hp} | Mana {self.mana}/{self.max_mana} | Endurance {self.endurance}/{self.max_endurance}",
                f"EXP {self.exp} | training points {self.training_points}",
                f"STR {self.strength} STA {self.stamina} AGI {self.agility} DEX {self.dexterity} WIS {self.wisdom} INT {self.intelligence} CHA {self.charisma}",
                f"Coin {self.coin} | Food {self.food} Water {self.water}",
                f"Skills {sum(v > 0 for v in self.abilities.skills.values())} | Spells {len(self.spell_book)} | Buffs {len(self.buffs)}",
                f"AA {len(self.aa_owned)} owned / {len(self.aa_ranks)} catalog ranks | spent {self.aa_points_spent} unspent {self.aa_points}",
            )
        )

    def __str__(self) -> str:
        return self.render()

    def dump(self) -> bytes:
        return pickle.dumps(self.__dict__, protocol=pickle.HIGHEST_PROTOCOL)

    @classmethod
    def restore(cls, pkl: bytes) -> Self:
        result = cls()
        data = pickle.loads(pkl)
        if not isinstance(data, dict):
            raise ValueError("Invalid character state")
        result.__dict__.update(data)
        return result
