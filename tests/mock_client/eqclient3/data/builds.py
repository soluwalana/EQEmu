"""One classic group build per class. The trainer, the merchant, and the gems all read it.

Skill numbers are the Titanium skill ids. A spend skill gets every point until it is
near his level. A seed skill is bought once and then left to rise from use.
"""

from __future__ import annotations

from dataclasses import dataclass

from eqclient3.structs import OP_GMEndTraining, OP_GMTrainSkill, OP_GMTraining

S1HB, S1HS, S2HB, S2HS = 0, 1, 2, 3
ABJ, ALT, POISON, ARCHERY, BACKSTAB, BIND = 4, 5, 6, 7, 8, 9
BASH, DEFENSE, DODGE, DOUBLE, DUAL = 10, 15, 19, 20, 22
EVO, FEIGN, H2H, HIDE, KICK = 24, 25, 28, 29, 30
MED, OFFENSE, PARRY, PIERCE, RIPOSTE = 31, 33, 34, 36, 37
ROUND, SENSE, SING, SNEAK = 38, 40, 41, 42
SPEC_ALT, SPEC_EVO = 44, 47
PICK, THROW = 48, 51
TIGER, TRACK = 52, 53
DRAGON, FLY, EAGLE = 21, 26, 23
BRASS, STRING, WIND, PERC = 12, 49, 54, 70
CONJ, DIV, CHAN = 14, 18, 13
LOCK, DISARM, DISARM_TRAPS, SENSE_TRAPS = 35, 16, 17, 62
MEND, FORAGE, TAUNT, BERSERK, FRENZY = 32, 27, 73, 72, 74
MAKE_POISON, RESEARCH, TINKER = 56, 58, 57

SEED_AT = 10


@dataclass(frozen=True)
class Build:
    class_id: int
    stats: tuple[str, ...]
    spend: tuple[int, ...]
    seed: tuple[int, ...]
    gems: tuple[str, ...]
    weapon: int
    spec: int | None = None


def _build(
    class_id: int,
    stats: tuple[str, ...],
    spend: tuple[int, ...],
    seed: tuple[int, ...],
    gems: tuple[str, ...] = (),
    weapon: int = S1HS,
    spec: int | None = None,
) -> Build:
    return Build(class_id, stats, spend, seed, gems, weapon, spec)


BUILDS = {
    1: _build(1, ("stamina", "strength"), (DEFENSE, OFFENSE, TAUNT, BASH, S1HS), (DODGE, PARRY, RIPOSTE, KICK, BIND, SENSE), weapon=S1HS),
    2: _build(2, ("wisdom", "stamina"), (MED, ALT, SPEC_ALT), (ABJ, DIV, EVO, CHAN, BIND), ("heal", "root", "stun", "rez"), S1HB, SPEC_ALT),
    3: _build(3, ("stamina", "strength", "wisdom"), (DEFENSE, OFFENSE, TAUNT, BASH, S1HS), (DODGE, PARRY, RIPOSTE, ABJ, ALT, DIV, MED), weapon=S1HS),
    4: _build(4, ("strength", "dexterity", "stamina", "wisdom"), (ARCHERY, OFFENSE, DUAL, DOUBLE), (S1HS, DODGE, TRACK, FORAGE, ABJ), ("snare",), ARCHERY),
    5: _build(5, ("stamina", "strength", "intelligence"), (DEFENSE, OFFENSE, TAUNT, BASH, S1HS), (DODGE, PARRY, RIPOSTE, ALT, CONJ), ("lifetap", "snare", "pet"), S1HS),
    6: _build(6, ("wisdom",), (MED, ALT, SPEC_ALT), (EVO, ABJ, CONJ, DIV, FORAGE, BIND), ("heal", "snare", "shield", "nuke"), S1HB, SPEC_ALT),
    7: _build(7, ("stamina", "strength", "agility", "dexterity"), (H2H, OFFENSE, DODGE, DUAL, DOUBLE), (DEFENSE, KICK, MEND, FEIGN, BIND, ROUND, TIGER, EAGLE, DRAGON, FLY), weapon=H2H),
    8: _build(8, ("charisma", "dexterity", "stamina"), (SING, PERC), (PIERCE, DEFENSE, OFFENSE, DODGE, DUAL, BRASS, WIND, STRING), ("speed", "resist", "mana"), PIERCE),
    9: _build(9, ("dexterity", "agility", "strength"), (BACKSTAB, PIERCE, HIDE, SNEAK, POISON), (OFFENSE, DUAL, DOUBLE, LOCK, SENSE_TRAPS, DISARM_TRAPS, PICK), weapon=PIERCE),
    10: _build(10, ("wisdom", "stamina"), (MED, ALT, SPEC_ALT), (CONJ, ABJ, EVO, CHAN), ("slow", "heal", "buff", "pet"), S1HB, SPEC_ALT),
    11: _build(11, ("intelligence", "stamina"), (MED, ALT, SPEC_ALT), (CONJ, EVO, ABJ), ("dot", "lifetap", "pet", "summon"), PIERCE, SPEC_ALT),
    12: _build(12, ("intelligence",), (MED, EVO, SPEC_EVO), (ABJ, ALT), ("nuke", "port"), PIERCE, SPEC_EVO),
    13: _build(13, ("intelligence",), (MED, EVO, SPEC_EVO), (CONJ,), ("pet", "nuke", "mend"), PIERCE, SPEC_EVO),
    14: _build(14, ("charisma", "intelligence"), (MED, ALT, SPEC_ALT), (CONJ, ABJ), ("haste", "slow", "mez"), PIERCE, SPEC_ALT),
    15: _build(15, ("wisdom", "stamina", "strength"), (OFFENSE, S1HS, ALT), (DUAL, DOUBLE, DEFENSE, DODGE, CONJ), ("pet", "slow", "heal"), S1HS),
    16: _build(16, ("strength", "stamina", "dexterity"), (S2HS, OFFENSE, DEFENSE, BERSERK, FRENZY), (THROW, DODGE, PARRY, KICK), weapon=S2HS),
}

TRADE_SKILLS = {MAKE_POISON, RESEARCH, TINKER}


def build_for(class_id: int) -> Build | None:
    return BUILDS.get(class_id)


def next_train(build: Build, known: dict[int, int], level: int, retired: set[int]) -> int | None:
    """The next skill point. Spend skills stay ahead of his level. Seed skills stop at ten."""
    level = max(level, 1)
    for skill in (*build.spend, *build.seed):
        if skill in retired or skill in TRADE_SKILLS:
            continue
        value = known.get(skill, 0)
        cap = level * 5 if skill in build.spend else SEED_AT
        if value < cap:
            return skill
    return None


def train_due(state: State) -> bool:
    return state.world.points > 0 and near_spawn(state, ("guildmaster", "trainer"), reach=20.0) is not None


def train_actions(state: State) -> list:
    trainer = near_spawn(state, ("guildmaster", "trainer"), reach=20.0)
    if trainer is None:
        return []
    if not state.trainer_open:
        state.trainer_open = True
        return [("op", "OP_GMTraining", OP_GMTraining(int(trainer.spawn_id), int(state.world.self_id)).serialize())]
    build = build_for(state.world.class_id or 1)
    skill = next_train(build, state.world.skills or {}, state.world.level or 1, state.retired_skills) if build else None
    if skill is None or state.world.points <= 0:
        state.world.points = 0
        return [("op", "OP_GMEndTraining", OP_GMEndTraining(int(trainer.spawn_id), int(state.world.self_id)).serialize())]
    state.retired_skills.add(int(skill))
    return [(
        "op",
        "OP_GMTrainSkill",
        OP_GMTrainSkill(int(trainer.spawn_id), int(skill)).serialize(),
    )]


def gear_value(
    build: Build | None,
    ac: int,
    damage: int,
    *,
    strength: int = 0,
    stamina: int = 0,
    agility: int = 0,
    dexterity: int = 0,
    wisdom: int = 0,
    intelligence: int = 0,
    charisma: int = 0,
    hp: int = 0,
    mana: int = 0,
) -> int:
    """Score wearable gear. Packet AC is often 0 — callers pass peq-cache stats too.

    Plate/melee weights AC; casters weight damage then primary stats (INT/WIS/CHA).
    """
    pool = {
        "strength": strength,
        "stamina": stamina,
        "agility": agility,
        "dexterity": dexterity,
        "wisdom": wisdom,
        "intelligence": intelligence,
        "charisma": charisma,
    }
    stat_score = 0
    if build is not None and build.stats:
        for index, name in enumerate(build.stats):
            weight = max(1, 4 - index)
            stat_score += pool.get(name, 0) * weight
    else:
        stat_score = sum(pool.values())
    vitals = hp // 4 + mana // 4
    if build is None or not build.stats:
        return ac + damage + stat_score + vitals
    if build.stats[0] in ("wisdom", "intelligence", "charisma"):
        return damage * 10 + ac + stat_score * 3 + vitals
    return ac * 3 + damage + stat_score * 2 + vitals


def held_gear_value(build: Build | None, held) -> int:
    """gear_value from a Held (after item-cache enrich)."""
    return gear_value(
        build,
        int(getattr(held, "ac", 0) or 0),
        int(getattr(held, "damage", 0) or 0),
        strength=int(getattr(held, "astr", 0) or 0),
        stamina=int(getattr(held, "asta", 0) or 0),
        agility=int(getattr(held, "aagi", 0) or 0),
        dexterity=int(getattr(held, "adex", 0) or 0),
        wisdom=int(getattr(held, "awis", 0) or 0),
        intelligence=int(getattr(held, "aint", 0) or 0),
        charisma=int(getattr(held, "acha", 0) or 0),
        hp=int(getattr(held, "hp", 0) or 0),
        mana=int(getattr(held, "mana", 0) or 0),
    )
