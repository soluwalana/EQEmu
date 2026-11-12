"""Packet-driven character state for EQEmu RoF2 (movement and inventory excluded).

Place at eqclient4/character.py. Operates on *decoded* EQStruct packets, like
CharacterInventory. Only apply authoritative server packets; do not infer
merchant payments from client requests or turn AA rank definitions into owned AAs.
"""

import pickle
from copy import deepcopy
from dataclasses import dataclass
from typing import Self

from eqclient4.log import log
from eqclient4.structs import (
    BuffIconEntry,
    EQStruct,
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
    OP_ShopPlayerBuy,
    OP_SkillUpdate,
    OP_Stamina,
    ProfileBind,
    SpellBuff,
)
from eqclient4.structs.constants import CombatSkill


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

    def combat_skill_known(self, skill: CombatSkill) -> bool:
        return self.ability_known(skill.value)

    def ability_known(self, skill_id: int) -> bool:
        return 0 < int(self.skills.get(int(skill_id), 0)) < 0xFFFFFFFF


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

        self.abilities: Abilities = Abilities()

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

    def event(self, action: str, message: str, changed: bool = False) -> CharacterEvent:
        event = CharacterEvent(action, message, changed)
        self.changes.append(event)
        return event

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
        return self.event("profile", f"Loaded {self.name!r} level {self.level}", True)

    def is_self(self, entity_id: int) -> bool:
        return self.self_id != 0 and (int(entity_id) & 0xFFFF) == (self.self_id & 0xFFFF)

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

    # Left here instead of handlers because it is used
    def on(self, opcode: str, payload: EQStruct, notify_unknown: bool = True) -> None:
        """Apply one already-decoded authoritative update."""
        char = self
        match payload:
            case OP_NewSpawn():
                if payload.spawn.name == char.name and payload.spawn.npc == 0:
                    char.self_id = payload.spawn.spawn_id
                    log.info(char.event("new-spawn", f"New spawn {char.self_id}", True))

                return

            case OP_PlayerProfile():
                log.info(char.load(payload))
                log.info(char.render())
                return

            case OP_SkillUpdate():
                prior = char.abilities.skills.get(payload.skill_id)
                char.abilities.skills[payload.skill_id] = payload.value
                log.info(
                    char.event(
                        "skill",
                        f"Skill {payload.skill_id}: {prior} -> {payload.value}",
                        prior != payload.value,
                    )
                )
                return

            case OP_Stamina():
                changed = (char.food, char.water) != (payload.food, payload.water)
                char.food, char.water = payload.food, payload.water
                log.info(char.event("stamina", f"Food {char.food}, water {char.water}", changed))
                return

            case OP_MoneyUpdate():
                previous_coin = char.coin
                char.set_coin(payload.platinum, payload.gold, payload.silver, payload.copper)
                log.info(
                    char.event(
                        "money",
                        f"Balance {char.coin} ({char.total_copper} copper)",
                        previous_coin != char.coin,
                    )
                )
                return

            case OP_ExpUpdate():
                changed = char.exp != payload.exp
                char.exp = payload.exp
                char.aa_experience_from_exp_update = payload.aa_exp
                log.info(char.event("experience", f"Experience {char.exp}", changed))
                return

            case OP_LevelUpdate():
                changed = (char.level, char.exp) != (payload.level, payload.exp)
                char.level, char.exp = payload.level, payload.exp
                log.info(char.event("level", f"Level {char.level}, experience {char.exp}", changed))
                return

            case OP_HPUpdate():
                if not char.is_self(payload.spawn_id):
                    return

                changed = (char.hp, char.max_hp) != (payload.cur_hp, payload.max_hp)
                char.hp, char.max_hp = payload.cur_hp, payload.max_hp
                char.hp_percent = round(100 * char.hp / char.max_hp) if char.max_hp > 0 else None
                log.info(char.event("hp", f"HP {char.hp}/{char.max_hp}", changed))
                return

            case OP_MobHealth():
                if not char.is_self(payload.spawn_id):
                    return
                changed = char.hp_percent != payload.percent
                char.hp_percent = payload.percent
                log.info(char.event("hp-percent", f"HP {payload.percent}%", changed))
                return

            case OP_ManaUpdate():
                if not char.is_self(payload.spawn_id):
                    return

                changed = (char.mana, char.max_mana) != (payload.cur_mana, payload.max_mana)
                char.mana, char.max_mana = payload.cur_mana, payload.max_mana
                log.info(char.event("mana", f"Mana {char.mana}/{char.max_mana}", changed))
                return

            case OP_EnduranceUpdate():
                if not char.is_self(payload.spawn_id):
                    return

                changed = (char.endurance, char.max_endurance) != (payload.cur_end, payload.max_end)
                char.endurance, char.max_endurance = payload.cur_end, payload.max_end
                log.info(
                    char.event(
                        "endurance", f"Endurance {char.endurance}/{char.max_endurance}", changed
                    )
                )
                return

            case OP_ManaChange():
                changed = char.mana != payload.new_mana
                char.mana = payload.new_mana
                log.info(char.event("mana", f"Mana {char.mana}", changed))
                return

            case OP_Buff():
                if not char.is_self(payload.entity_id):
                    return

                before = char.buffs.get(payload.slot_id)
                if payload.fade or payload.buff.spell_id in (0, 0xFFFF, 0xFFFFFFFF):
                    char.buffs.pop(payload.slot_id, None)
                    char.buff_icons.pop(payload.slot_id, None)
                    log.info(
                        char.event("buff-fade", f"Buff slot {payload.slot_id}", before is not None)
                    )
                    return

                char.buffs[payload.slot_id] = deepcopy(payload.buff)
                log.info(
                    char.event(
                        "buff",
                        f"Slot {payload.slot_id}: spell {payload.buff.spell_id}",
                        before != payload.buff,
                    )
                )
                return

            case OP_BuffCreate():
                if not char.is_self(payload.entity_id):
                    log.info(char.event("ignored", "Buff icons belong to another entity"))
                    return

                previous_buffs = char.buff_icons.copy()
                if payload.all_buffs:
                    char.buff_icons.clear()

                for entry in payload.entries:
                    if entry.spell_id in (0, 0xFFFF, 0xFFFFFFFF):
                        char.buff_icons.pop(entry.buff_slot, None)
                    else:
                        char.buff_icons[entry.buff_slot] = deepcopy(entry)

                log.info(
                    char.event(
                        "buff-icons",
                        f"{len(char.buff_icons)} buff icons",
                        previous_buffs != char.buff_icons,
                    )
                )
                return

            case OP_RespondAA():
                previous = (char.aa_slots, char.aa_points_spent)
                char.set_owned_aa({e.index: (e.aa, e.value, e.charges) for e in payload.entries})
                char.aa_points_spent = payload.aa_spent
                char.aa_points_assigned = payload.aapoints_assigned
                char.aa_spent_general = payload.aa_spent_general
                char.aa_spent_archetype = payload.aa_spent_archetype
                char.aa_spent_class = payload.aa_spent_class
                char.aa_spent_special = payload.aa_spent_special
                log.info(
                    char.event(
                        "aa-owned",
                        f"{len(char.aa_owned)} owned AA ranks, {char.aa_points_spent} points spent",
                        previous != (char.aa_slots, char.aa_points_spent),
                    )
                )
                return

            case OP_SendAATable():
                previous_aa_rank = char.aa_ranks.get(payload.aa_id)
                char.aa_ranks[payload.aa_id] = deepcopy(payload)
                log.info(
                    char.event(
                        "aa-catalog",
                        f"Rank {payload.aa_id}, ability {payload.seq}, cost {payload.cost}",
                        previous_aa_rank != payload,
                    )
                )
                return

            case OP_AAExpUpdate():
                prior_aa_exp = (
                    char.aa_points,
                    char.aa_experience_scaled,
                    char.aa_xp_allocation_percent,
                )
                char.aa_points = payload.aapoints_unspent
                char.aa_experience_scaled = payload.unknown00
                char.aa_xp_allocation_percent = payload.aaxp_percent
                log.info(
                    char.event(
                        "aa-experience",
                        f"AA unspent {char.aa_points}, scaled XP {char.aa_experience_scaled}",
                        prior_aa_exp
                        != (
                            char.aa_points,
                            char.aa_experience_scaled,
                            char.aa_xp_allocation_percent,
                        ),
                    )
                )
                return

            case OP_ShopPlayerBuy():
                char.deduct_coins(payload.price)
                return

            case _:
                if notify_unknown:
                    log.error(f"Unknown profile opcode: {opcode}")
                return

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
