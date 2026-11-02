"""Gem bar, mana, and engaged cast order for the player.

Bot spell settings walk types by engaged priority and take the best spell of
that type the bot can afford. The player does the same with the class build:
the strongest scribed spell of each gem role is memorized, heals and cures
already ran, and what is left casts in the engaged order. A meditating class
sits when the pool is too low to spend on an attack spell. Gem recast is kept
in tenths of a second, which is one pulse.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Protocol, runtime_checkable

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import World

from eqclient3.action import Action
from eqclient3.actions.support import SIT, GemView, memorized, ready_gem
from eqclient3.data.builds import build_for
from eqclient3.data.spells import DEFAULT_SPELLS, GEM_SLOTS, read_spells, role_of, spell_name
from eqclient3.structs import OP_MemorizeSpell, OP_SpawnAppearance

# Cleric, druid, shaman, necromancer, wizard, magician, enchanter. Hybrids melee.
MEDITATE = frozenset({2, 6, 10, 11, 12, 13, 14})
# Below this fraction a caster stops spending mana on attack spells and sits.
MANA_FLOOR = 0.2
# eaStanding. Sit is support.SIT (110).
STAND = 100
# After heal and cure. Once-per-fight roles land a single time; the rest recast.
OFFENSE = ("buff", "haste", "slow", "snare", "root", "mez", "stun", "debuff", "dot", "lifetap", "nuke")
ONCE = frozenset({"buff", "haste", "slow", "snare", "root", "mez", "debuff"})

_LEVELS: dict[tuple[int, int], int] | None = None


@dataclass(frozen=True)
class CastChoice:
    gem: GemView
    target: int
    role: str


@runtime_checkable
class _Cost(Protocol):
    mana: int


def tick_recasts(action: Action) -> None:
    """One pulse passed. A gem with no time left leaves the table."""
    recast = action._gem_recast
    for slot, ticks in list(recast.items()):
        if ticks <= 1:
            recast.pop(slot, None)
        else:
            recast[slot] = ticks - 1


def fill_bar(loop: Loop, world: World) -> bool:
    """Memorize one gem that is missing or holding a weaker spell. One packet."""
    wanted = _desired(world)
    if not wanted:
        return False
    gems = world.gems
    for slot, spell_id in wanted.items():
        current = gems.get(slot, 0)
        if current == spell_id:
            continue
        if current:
            loop.send("OP_MemorizeSpell", OP_MemorizeSpell(slot, current, 2).serialize())
            gems.pop(slot, None)
            return True
        loop.send("OP_MemorizeSpell", OP_MemorizeSpell(slot, spell_id, 1).serialize())
        gems[slot] = spell_id
        return True
    return False


def next_offense(world: World, action: Action, landed: set[str]) -> CastChoice | None:
    """The first affordable attack spell in the engaged order."""
    spawn = action.spawn_id or 0
    if not spawn:
        return None
    gems = memorized(world, action)
    for role in OFFENSE:
        if role in ONCE and role in landed:
            continue
        gem = _best(world, gems, role)
        if gem is None or not ready_gem(world, gem):
            continue
        return CastChoice(gem, spawn, role)
    return None


def sit_for_mana(loop: Loop, world: World) -> bool:
    """True when a meditating class is too low to spend mana and should sit."""
    if world.class_id not in MEDITATE:
        return False
    pool = _ratio(world)
    if pool is None or pool >= MANA_FLOOR:
        return False
    loop.send(
        "OP_SpawnAppearance",
        OP_SpawnAppearance(world.self_id, 14, SIT).serialize(),
    )
    return True


def stand(loop: Loop, world: World) -> None:
    loop.send(
        "OP_SpawnAppearance",
        OP_SpawnAppearance(world.self_id, 14, STAND).serialize(),
    )


def _desired(world: World) -> dict[int, int]:
    build = build_for(world.class_id)
    if build is None or not build.gems:
        return {}
    known = _scribed(world)
    if not known:
        return {}
    chosen: dict[int, int] = {}
    used: set[int] = set()
    for slot, role in enumerate(build.gems):
        if slot >= GEM_SLOTS:
            break
        best = 0
        best_rank = (-1, -1)
        for spell_id in known:
            if spell_id in used or _role(world, spell_id, None) != role:
                continue
            rank = _rank(world, spell_id)
            if rank <= best_rank:
                continue
            best = spell_id
            best_rank = rank
        if best:
            chosen[slot] = best
            used.add(best)
    return chosen


def _best(world: World, gems: list[GemView], role: str) -> GemView | None:
    found: GemView | None = None
    found_rank = (-1, -1)
    for gem in gems:
        if _role(world, gem.spell_id, gem) != role:
            continue
        rank = _rank(world, gem.spell_id)
        if found is not None and rank <= found_rank:
            continue
        found = gem
        found_rank = rank
    return found


def _role(world: World, spell_id: int, gem: GemView | None) -> str:
    named = role_of(_name(world, spell_id))
    if named in OFFENSE or named in ("heal", "cure", "buff", "haste"):
        return named
    if gem is None:
        return named
    if gem.heal:
        return "heal"
    if gem.cure:
        return "cure"
    if gem.combat:
        return "nuke"
    return named


def _rank(world: World, spell_id: int) -> tuple[int, int]:
    level = _levels().get((world.class_id, spell_id), 0)
    return (level, _mana(world, spell_id))


def _mana(world: World, spell_id: int) -> int:
    info = world.spell_info
    if not isinstance(info, dict):
        return 0
    meta = info.get(spell_id)
    if isinstance(meta, _Cost):
        return meta.mana
    if isinstance(meta, dict):
        value = meta.get("mana")
        if isinstance(value, int) and not isinstance(value, bool):
            return value
    return 0


def _name(world: World, spell_id: int) -> str:
    names = world.spell_names
    if isinstance(names, dict):
        raw = names.get(spell_id)
        if isinstance(raw, str) and raw:
            return raw
    return spell_name(spell_id)


def _scribed(world: World) -> list[int]:
    found: list[int] = []
    for book in (world.spell_book, world.spells):
        if not isinstance(book, dict):
            continue
        for value in book.values():
            if isinstance(value, int) and not isinstance(value, bool) and value > 0 and value not in found:
                found.append(value)
    return found


def _ratio(world: World) -> float | None:
    maximum = world.max_mana
    if maximum <= 0:
        return None
    return world.mana / maximum


def _levels() -> dict[tuple[int, int], int]:
    global _LEVELS
    if _LEVELS is not None:
        return _LEVELS
    found: dict[tuple[int, int], int] = {}
    for row in read_spells(DEFAULT_SPELLS).rows:
        found[(row.class_id, row.spell_id)] = row.level
    _LEVELS = found
    return found
