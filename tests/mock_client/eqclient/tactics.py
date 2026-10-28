"""How a class fights alone, and how the same class fights in a group.

A rooted mob is not auto-attacked. Root breaks when he hits it.
"""

from __future__ import annotations

SOLO = {
    1: "melee",
    2: "root",
    3: "root",
    4: "kite",
    5: "pet",
    6: "kite",
    7: "melee",
    8: "song",
    9: "backstab",
    10: "slow",
    11: "pet",
    12: "root",
    13: "pet",
    14: "mez",
    15: "pet",
    16: "melee",
}

GROUP = {
    1: "tank",
    2: "heal",
    3: "tank",
    5: "tank",
    6: "heal",
    10: "slow",
    14: "mez",
}

# The gem this tactic casts before anyone swings.
OPENER = {
    "pet": "pet",
    "kite": "snare",
    "root": "root",
    "mez": "mez",
    "slow": "slow",
    "song": "slow",
    "tank": "taunt",
    "heal": "heal",
    "backstab": "hide",
}


def fight_tactic(class_id: int, grouped: bool) -> str:
    if grouped:
        return GROUP.get(class_id, "assist")
    return SOLO.get(class_id, "melee")


def may_melee(tactic: str, rooted: bool, snared: bool, slowed: bool, hp_ratio: float) -> bool:
    """True when auto-attack is the right button. Root always means no."""
    if rooted:
        return False
    if tactic == "kite":
        return snared and hp_ratio >= 0.5
    if tactic in ("pet", "root", "mez", "song"):
        return False
    if tactic == "slow":
        return slowed
    return True


def opener(tactic: str) -> str:
    return OPENER.get(tactic, "")
