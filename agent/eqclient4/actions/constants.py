from dataclasses import dataclass
from typing import Protocol, runtime_checkable

TOKEN = 22292

# Distances

MELEE_RANGE = 3
SPELL_RANGE = 25
HAIL_RANGE = 10
INTERACT_RANGE = 10
CORPSE_COLLECT_RANGE = 15
CORPSE_SUMMON_RANGE = (
    50  # server Corpse::Summon accepts 100 yards (DistanceSquaredNoZ <= 100^2, Z ignored)
)
HOSTILE_CLOSE_RANGE = 150
HOSTILE_FAR_RANGE = 250
NORMAL_LOOT_RANGE = 2
TOO_FAR_RANGE = 5

SIT_RANGE = 110


@dataclass
class SpellInfo:
    mana: int = 0
    recast: float = 0.0
    heal: bool = False
    cure: str | None = None
    combat: bool = False


# @runtime_checkable
# class _SpellMeta(Protocol):
#     mana: int
#     recast: float
#     heal: bool
#     cure: str | None
#     combat: bool
