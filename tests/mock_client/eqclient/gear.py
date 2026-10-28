"""Beginner → mid → late gear goals under the epic root, for the agent and party bots.

Item ids are classic Titanium medium-size pieces that merchants sell or early zones drop.
Campaign assign order is late then mid then beginner so the stack top is the next buy.
"""

from __future__ import annotations

# Cloth — casters (clr/enc/wiz/mag/nec).
_CLOTH = (1001, 1004, 1008, 1010, 1011, 1012, 1006)
# Leather / patchwork — melee hybrids and rogue.
_LEATHER = (2001, 2004, 2008, 2010, 2011, 2012, 2006)
_PATCHWORK = (2104, 2108, 2111, 2112, 2106)
_RAWHIDE = (2137, 2140, 2144, 2146, 2148, 2142)  # skullcap,tunic,sleeves,gloves,boots,cloak
# Banded — warriors / tanks.
_BANDED = (3053, 3056, 3060, 3063, 3064, 3058)
# Cured silk — late caster.
_SILK = (1180, 1183, 1187, 1185, 1191)

# Primary weapons by class (1-based Titanium ids).
_WEAPON_BEGIN = {
    1: 5013,   # war — rusty short sword
    2: 6011,   # clr — rusty mace
    3: 5013,   # pal
    4: 5013,   # rng
    5: 5013,   # sk
    6: 6011,   # dru
    7: 0,      # mnk — fists
    8: 7007,   # brd — rusty dagger
    9: 7007,   # rog
    10: 6011,  # shm
    11: 7007,  # nec
    12: 7007,  # wiz
    13: 7007,  # mag
    14: 7007,  # enc
    15: 5013,  # bst
    16: 5023,  # ber — rusty 2hs
}
_WEAPON_MID = {
    1: 5026,   # bronze short sword
    2: 6019,   # bronze mace
    3: 5026,
    9: 7012,   # bronze dagger
    12: 7012,
    14: 7012,
}
_WEAPON_LATE = {
    1: 5352,   # fine steel short sword
    2: 6019,
    9: 7350,   # fine steel dagger
    12: 7350,
    14: 7350,
}

# Cleric heal scrolls (spell-at-level priority for the bot). Item ids from peq.
HEAL_SCROLLS = (9993, 15017, 15012, 15015, 15009, 15013)  # minor → … → complete

# Human race bit index for bot create.
BOT_RACE = 1

_CLOTH_CLASSES = {2, 11, 12, 13, 14}
_LEATHER_CLASSES = {4, 7, 8, 9, 15}
_PLATE_CLASSES = {1, 3, 5, 16}


def gear_tier(level: int) -> str:
    if level < 11:
        return "beginner"
    if level < 31:
        return "mid"
    return "late"


def _armor_for(class_id: int, tier: str) -> tuple[int, ...]:
    if class_id in _CLOTH_CLASSES:
        if tier == "beginner":
            return _CLOTH[:4]  # cap, shirt, sleeves, gloves
        if tier == "mid":
            return _CLOTH
        return _SILK[:4]
    if class_id in _LEATHER_CLASSES:
        if tier == "beginner":
            return _LEATHER[:4]
        if tier == "mid":
            return _PATCHWORK[:4] or _LEATHER
        return _RAWHIDE[:4]
    # plate / chain / hybrid
    if tier == "beginner":
        return _LEATHER[:4]
    if tier == "mid":
        return _BANDED[:4]
    return _BANDED


def _weapon_for(class_id: int, tier: str) -> int:
    table = _WEAPON_BEGIN
    if tier == "mid":
        table = {**_WEAPON_BEGIN, **_WEAPON_MID}
    elif tier == "late":
        table = {**_WEAPON_BEGIN, **_WEAPON_MID, **_WEAPON_LATE}
    return int(table.get(class_id) or 0)


def kit_for(class_id: int, tier: str) -> list[int]:
    """Weapon + a few armor pieces for one class at this tier."""
    items: list[int] = []
    weapon = _weapon_for(class_id, tier)
    if weapon:
        items.append(weapon)
    items.extend(_armor_for(class_id, tier))
    # Preserve order, drop dupes.
    seen: set[int] = set()
    out: list[int] = []
    for item_id in items:
        if item_id and item_id not in seen:
            seen.add(item_id)
            out.append(item_id)
    return out


def tiers_up_to(level: int) -> tuple[str, ...]:
    """Tiers the character should pursue, late→beginner so beginner lands on top."""
    tier = gear_tier(level)
    if tier == "beginner":
        return ("beginner",)
    if tier == "mid":
        return ("mid", "beginner")
    return ("late", "mid", "beginner")


def seed_gear_goals(
    campaign,
    class_id: int,
    level: int,
    held: set[int],
    party: list[tuple[str, int]] | None = None,
    graph=None,
) -> list[str]:
    """Assign beginner/mid/late kits under the current root. Returns labels pushed."""
    labels: list[str] = []
    skip = set(campaign.stack) | set(held)
    # Late first, beginner last → beginner is stack top.
    for tier in tiers_up_to(level):
        classes = [class_id] + [cid for _name, cid in (party or ()) if cid != class_id]
        # Deduplicate class kits (agent + one kit per distinct bot class).
        seen_class: set[int] = set()
        for cid in classes:
            if cid in seen_class:
                continue
            seen_class.add(cid)
            for item_id in kit_for(cid, tier):
                if item_id in skip:
                    continue
                if campaign.assign_goal(item_id, graph=graph):
                    skip.add(item_id)
                    who = "self" if cid == class_id else f"class{cid}"
                    labels.append(f"{tier}:{who}:{item_id}")
    return labels
