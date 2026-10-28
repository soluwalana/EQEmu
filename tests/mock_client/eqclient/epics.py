"""Class epic helpers and item obtainability checks for the campaign planner.

Goals are item ids. Epic 2.0 defaults are convenience roots, not a separate mode.
"""

from __future__ import annotations

from dataclasses import dataclass

# Titanium class ids (1-based), matching sheet._CLASS_NAMES order.
CLASS_BY_NAME = {
    "warrior": 1,
    "cleric": 2,
    "paladin": 3,
    "ranger": 4,
    "shadowknight": 5,
    "shadow knight": 5,
    "druid": 6,
    "monk": 7,
    "bard": 8,
    "rogue": 9,
    "shaman": 10,
    "necromancer": 11,
    "wizard": 12,
    "magician": 13,
    "enchanter": 14,
    "beastlord": 15,
    "berserker": 16,
}

# Epic 2.0 terminal items by class id (from .epics pages / peq items).
_EPIC20_ITEM: dict[int, int] = {
    1: 60329,  # warrior — Raging Sword of Eternal Power
    2: 20076,  # cleric — Aegis of Superior Divinity
    3: 64031,  # paladin — Redemption
    4: 62649,  # ranger — Aurora, the Heartwood Blade
    5: 48136,  # shadowknight — Innoruuk's Dark Blessing
    6: 62863,  # druid — Staff of Living Brambles
    7: 67742,  # monk — Transcended Fistwraps of Immortality
    8: 77640,  # bard — Blade of Vesagran
    9: 52348,  # rogue — Nightshade, Blade of Entropy
    10: 57405,  # shaman — Blessed Spiritstaff of the Heyokah
    11: 64067,  # necromancer — Deathwhisper
    12: 16576,  # wizard — Staff of Phenomenal Power
    13: 19839,  # magician — Focus of Primal Elements
    14: 52952,  # enchanter — Oculus of Persuasion
    15: 52911,  # beastlord — Savage Lord's Totem
    16: 18609,  # berserker — Vengeful Taelosian Blood Axe
}

# Plane / GoD entry uses journal keys `zoneflag:<zoneid>` (zone.flag_needed == 1).
# Those are codified on ZoneGraph.flagged / TransitNeed.zone_flag and unlocked via
# quest-graph `sets` from set_zone_flag — see campaign._travel_to / _unlock_flag.

# Flag families useful for gate reasoning (not goals).
CLASS_FLAGS: dict[int, tuple[str, ...]] = {
    1: ("warrior_pre", "warrior_epic"),
    2: ("cleric15pre", "cleric_epic", "cleric20"),
    3: ("paladin_epic",),
    4: ("ranger_epic", "ranger_epic15_pre"),
    5: ("shadowknight_pre", "shadowknight_epic"),
    6: ("druid_epic",),
    7: ("MnkPre", "monk_epic", "mnk_epic20"),
    8: ("bardPQ", "bard15", "Fatestealer_bard", "bard20"),
    9: ("roguepre",),
    10: ("shaman_pre", "shaman_epic"),
    11: ("NecroPre", "necro_epic"),
    12: ("wiz_epic_pre", "wizepic", "wiz_epic", "wiz_epic20"),
    13: ("mage_epic",),
    14: ("EnchPre", "ench_epic"),
    15: ("bstepic", "beast_epic"),
    16: ("berserk_epic",),
}


@dataclass(frozen=True)
class EpicGoal:
    class_id: int
    item_id: int
    flags: tuple[str, ...]


def default_epic20_item(class_id: int) -> int | None:
    return _EPIC20_ITEM.get(class_id)


def goal_for(class_id: int) -> EpicGoal | None:
    item_id = default_epic20_item(class_id)
    if item_id is None:
        return None
    return EpicGoal(class_id, item_id, CLASS_FLAGS.get(class_id, ()))


def can_obtain(item_id: int, class_id: int, race_id: int = 0, graph=None) -> bool:
    """True when the graph does not bar this class/race from the item.

    Empty restrictions mean the item is treated as obtainable (quest pieces often
    have no class mask on the graph item row).
    """
    if item_id <= 0 or class_id <= 0:
        return False
    if graph is None:
        return True
    info = getattr(graph, "items", {}).get(item_id) or {}
    classes = info.get("classes") or ()
    races = info.get("races") or ()
    if classes and int(class_id) not in {int(c) for c in classes}:
        return False
    if races and race_id and int(race_id) not in {int(r) for r in races}:
        return False
    # Class-gated give edges: if every give is class-restricted and none match, reject.
    matched = False
    saw_class_gate = False
    for edge in getattr(graph, "edges", ()) or ():
        if edge.get("rel") not in {"gives", "produces"}:
            continue
        if str(edge.get("to") or "") != f"item:{item_id}":
            continue
        edge_classes = edge.get("classes") or ()
        if edge_classes:
            saw_class_gate = True
            if int(class_id) in {int(c) for c in edge_classes}:
                matched = True
        else:
            matched = True
    if saw_class_gate and not matched:
        return False
    return True


def flag_satisfied(name: str, need: str, values: dict[str, int]) -> bool:
    """Evaluate a graph flag need such as '>=3', '==6', 'set', or 'unset'."""
    if need in {"", "set"}:
        return name in values
    if need == "unset":
        return name not in values
    current = values.get(name)
    if current is None:
        return False
    op = need[:2] if need[:2] in {"==", "!=", ">=", "<="} else need[:1]
    raw = need[len(op) :]
    try:
        want = int(raw)
    except ValueError:
        return str(current) == raw
    if op == "==":
        return current == want
    if op == "!=":
        return current != want
    if op == ">=":
        return current >= want
    if op == "<=":
        return current <= want
    if op == ">":
        return current > want
    if op == "<":
        return current < want
    return False
