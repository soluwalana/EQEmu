"""Write one markdown file per class from the quest graph only."""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

from eqclient4.data.drops import ensure_drops
from eqclient4.data.merchants import ensure_merchants
from eqclient4.data.recipes import ensure_recipes

DROP_BOOK = ensure_drops()
MERCHANT_BOOK = ensure_merchants()
RECIPE_BOOK = ensure_recipes()

GRAPH = Path.home() / ".eqclient" / "quest_graph.jsonl"
OUT = Path(__file__).resolve().parent

# Main flags in the order a character meets them. A 2.0 flag is the one the
# graph actually names with 20. Where 1.5 and 2.0 share one flag, the values
# stay in one section and the gaps are marked.
CLASSES = [
    (
        "warrior",
        "Warrior",
        ["warrior_pre", "warrior_epic"],
        ("warr_epic", "warrior_epic_"),
    ),
    (
        "cleric",
        "Cleric",
        ["cleric15pre", "cleric_epic", "cleric20"],
        ("cleric20_", "cleric_epic_"),
    ),
    ("paladin", "Paladin", ["paladin_epic"], ("paladin_epic_",)),
    # ranger_epic through 7 is the 1.5 chain. Value 8 is where the scripts say 2.0 starts.
    (
        "ranger",
        "Ranger",
        [
            ("ranger_epic", None, 8, None),
            "ranger_epic15_pre",
            ("ranger_epic", 8, None, "2.0"),
        ],
        ("ranger_epic_",),
    ),
    (
        "shadowknight",
        "Shadow Knight",
        ["shadowknight_pre", "shadowknight_epic"],
        ("sk_",),
    ),
    ("druid", "Druid", ["druid_epic"], ("druid_epic_",)),
    ("monk", "Monk", ["MnkPre", "monk_epic", "mnk_epic20"], ("monk_epic_",)),
    (
        "bard",
        "Bard",
        ["bardPQ", "bard15", "Fatestealer_bard", "bard20"],
        ("bard15_", "bard20_"),
    ),
    (
        "rogue",
        "Rogue",
        ["roguepre", ("Fatestealer", None, None, "1.5")],
        ("rogue_epic_", "rogue_", "rog_epic_"),
    ),
    ("shaman", "Shaman", ["shaman_pre", "shaman_epic"], ("shaman_epic_",)),
    (
        "necromancer",
        "Necromancer",
        [
            "NecroPre",
            ("Soulwhisper", None, None, "1.5"),
            ("necro_epic", None, None, "2.0"),
        ],
        ("nec_epic_",),
    ),
    (
        "wizard",
        "Wizard",
        [
            "wiz_epic_pre",
            "wizepic",
            "wizepicA",
            "wizepicB",
            "wizepicK",
            "wiz_epic",
            "wiz_epic20",
        ],
        ("wiz20_", "wiz_epic_s", "wiz_epic_w"),
    ),
    (
        "magician",
        "Magician",
        [("mage_epic", None, 8, "1.5"), ("mage_epic", 8, None, "2.0")],
        ("mage_epic_",),
    ),
    ("enchanter", "Enchanter", ["EnchPre", "ench_epic"], ("ench_epic_",)),
    ("beastlord", "Beastlord", ["bstepic", "beast_epic"], ("beast_epic_", "bst_")),
    ("berserker", "Berserker", ["berserk_epic"], ("ber_epic_", "berserk_epic_")),
]

# Final rewards are traversal roots. Quest globals are prerequisites discovered
# while walking backwards from a reward, not a proxy for the reward itself.
# Keep both Ranger 1.0 swords: they are separate, independently earned epics.
EPIC_ITEMS: dict[str, dict[str, tuple[int, ...]]] = {
    "warrior": {"1.0": (10908,), "1.5": (60321,), "2.0": (60332,)},
    "cleric": {"1.0": (5532,), "1.5": (9955,), "2.0": (20076,)},
    "paladin": {"1.0": (10099,), "1.5": (64031,), "2.0": (48147,)},
    "ranger": {"1.0": (20487, 20488), "1.5": (62627,), "2.0": (62649,)},
    "shadowknight": {"1.0": (14383,), "1.5": (50003,), "2.0": (48136,)},
    "druid": {"1.0": (20490,), "1.5": (62863,), "2.0": (62880,)},
    "monk": {"1.0": (10652,), "1.5": (61025,), "2.0": (67742,)},
    "bard": {"1.0": (20542,), "1.5": (77631,), "2.0": (77640,)},
    "rogue": {"1.0": (11057,), "1.5": (52347,), "2.0": (52348,)},
    "shaman": {"1.0": (10651,), "1.5": (57400,), "2.0": (57405,)},
    "necromancer": {"1.0": (20544,), "1.5": (62581,), "2.0": (64067,)},
    "wizard": {"1.0": (14341,), "1.5": (12665,), "2.0": (16576,)},
    "magician": {"1.0": (28034,), "1.5": (19092,), "2.0": (19839,)},
    "enchanter": {"1.0": (10650,), "1.5": (52952,), "2.0": (52962,)},
    "beastlord": {"1.0": (8495,), "1.5": (52911,), "2.0": (57054,)},
    "berserker": {"1.0": (68299,), "1.5": (18398,), "2.0": (18609,)},
}


def load():
    items: dict[int, dict] = {}
    edges: list[dict] = []
    says: dict[tuple[str, str, str], str] = {}
    world: dict[int, dict] = {}
    dialogues: dict[str, list[dict]] = defaultdict(list)
    for line in GRAPH.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        kind = row.get("kind")
        if kind == "item":
            items[int(row["item"])] = row
        elif kind == "world":
            world[int(row["id"])] = {
                "name": row.get("name") or "",
                "zones": list(row.get("zones") or []),
            }
        elif kind == "edge":
            edges.append(row)
        elif kind == "dialogue":
            dialogues[str(row.get("source") or "").lower()].append(row)
        elif kind == "say":
            says[
                (
                    str(row.get("zone", "")).lower(),
                    str(row.get("npc", "")).lower(),
                    str(row.get("word", "")).lower(),
                )
            ] = (
                row.get("text") or ""
            )
    return items, edges, says, world, dialogues


def fallback_drop(items, item_id: int) -> str | None:
    """Only for items with no quest, recipe, or catalog acquisition path."""
    dropper = DROP_BOOK.best(int(item_id))
    if not dropper:
        return None

    if dropper.name:
        npc = quoted(dropper.name)
    else:
        npc = f"NPC {dropper.npc_id}"

    where = ""
    if dropper.zone:
        where = f" in `{dropper.zone}`"

    chance = f"{dropper.chance:.2f}".rstrip("0").rstrip(".")
    return (
        f"Loot {quoted_item(items, item_id)} from {npc} "
        f"(NPC {dropper.npc_id}){where}. "
        f"Drop cache: {chance}% chance per kill."
    )


def fallback_merchant(items, item_id: int) -> str | None:
    """Buy an otherwise unresolved item from a spawned NPC vendor."""
    found = MERCHANT_BOOK.best(int(item_id))
    if found is None:
        return None
    seller, copper = found
    npc = quoted(seller.name) if seller.name else f"NPC {seller.npc_id}"
    zone = f" in `{seller.zone}`" if seller.zone else ""
    # Vendor prices change with faction/charisma; the cache has the item's base price.
    price = f" Base price: {copper:,} copper." if copper > 0 else ""
    return (
        f"Buy {quoted_item(items, item_id)} from {npc} "
        f"(NPC {seller.npc_id}){zone}.{price}"
    )


def indexes(edges, world):
    by_from = defaultdict(list)
    by_group = defaultdict(list)
    sets_of = defaultdict(list)
    gives = defaultdict(list)
    loots = defaultdict(list)
    grounds = defaultdict(list)
    produces = defaultdict(list)
    recipe = defaultdict(
        lambda: {
            "consumes": [],
            "container": 0,
            "produces": 0,
            "products": [],
            "world": None,
        }
    )
    for edge in edges:
        by_from[edge.get("from")].append(edge)
        if edge.get("group"):
            by_group[edge["group"]].append(edge)
        rel = edge.get("rel")
        to = str(edge.get("to") or "")
        source = str(edge.get("from") or "")
        if rel == "sets" and edge.get("flag"):
            sets_of[edge["flag"]].append(edge)
        if source.startswith("recipe:"):
            recipe_id = int(source.split(":", 1)[1])
            for key in (
                "skill",
                "skill_name",
                "skillneeded",
                "trivial",
                "nofail",
                "must_learn",
            ):
                if key in edge:
                    recipe[recipe_id][key] = edge[key]
        if (
            rel == "container"
            and source.startswith("recipe:")
            and to.startswith("world:")
        ):
            recipe_id = int(source.split(":", 1)[1])
            type_id = int(to.split(":", 1)[1])
            station = world.get(type_id) or {
                "name": f"world container {type_id}",
                "zones": [],
            }
            recipe[recipe_id]["world"] = {"id": type_id, **station}
            continue
        if not to.startswith("item:"):
            continue
        item_id = int(to.split(":", 1)[1])
        if rel == "gives":
            gives[item_id].append(edge)
        elif rel == "loots":
            loots[item_id].append(edge)
        elif rel == "grounds":
            grounds[item_id].append(edge)
        elif rel == "produces" and source.startswith("recipe:"):
            recipe_id = int(source.split(":", 1)[1])
            produces[item_id].append(recipe_id)
            if not recipe[recipe_id]["produces"]:
                recipe[recipe_id]["produces"] = item_id
            products = recipe[recipe_id]["products"]
            if not any(known == item_id for known, _count in products):
                products.append((item_id, int(edge.get("count") or 1)))
        elif rel == "consumes" and source.startswith("recipe:"):
            recipe_id = int(source.split(":", 1)[1])
            recipe[recipe_id]["consumes"].append((item_id, int(edge.get("count") or 1)))
        elif rel == "container" and source.startswith("recipe:"):
            recipe_id = int(source.split(":", 1)[1])
            recipe[recipe_id]["container"] = item_id
    return by_from, by_group, sets_of, gives, loots, grounds, produces, recipe


# Same named reward under two item ids. Elder Spirit accepts either Spear of Fate.
_ITEM_ALIAS = {
    36223: 10651,  # Spear of Fate (legacy id → Spirit Sentinel reward)
}


def _made_by(items, item_id: int) -> list[str]:
    """A spell, a forage, fishing, ground spawn, or dump loot creates the item without a quest script."""
    sources = list((items.get(int(item_id)) or {}).get("sources") or [])
    named = quoted_item(items, item_id)
    spells = sorted(
        (source.split(":", 1)[1] for source in sources if source.startswith("spell:")),
        key=len,
    )
    lines = []
    if spells:
        shown = ", ".join(quoted(name) for name in spells[:3])
        extra = f" and {len(spells) - 3} more" if len(spells) > 3 else ""
        lines.append(f"- Summon {named} by casting {shown}{extra}.")
    for source in sources:
        if source.startswith("forage:"):
            lines.append(f"- Forage {named} in `{source.split(':', 1)[1]}`.")
        elif source.startswith("fishing:"):
            lines.append(f"- Fish {named} in `{source.split(':', 1)[1]}`.")
        elif source.startswith("ground:"):
            lines.append(f"- Ground spawn of {named} in `{source.split(':', 1)[1]}`.")
        elif source.startswith("loot:"):
            body = source.split(":", 1)[1]
            who, _, zone = body.partition("@")
            text = f"- Loot {named} from {quoted(who)}"
            if zone:
                text += f" in `{zone}`"
            lines.append(text + ".")
    return lines


# Tradeskill ids. A recipe that names some other skill and requires nothing of it is not a skill check.
_CRAFT_SKILLS = {55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 68, 69}


def _recipe_inputs(info: dict) -> set[int]:
    found = {int(item_id) for item_id, _count in info.get("consumes") or []}
    if info.get("container"):
        found.add(int(info["container"]))
    return found


def _recipe_refund(recipes: dict, edge: dict, item_id: int) -> bool:
    """A combine hands its own container and components back when the result is not an item. That is not how you obtain them."""
    source = str(edge.get("group") or edge.get("from") or "")
    if "#recipe:" not in source:
        return False
    tail = source.rsplit(":", 1)[-1]
    if not tail.isdigit():
        return False
    info = recipes.get(int(tail))
    return bool(info) and int(item_id) in _recipe_inputs(info)


def _skill_line(info: dict) -> str:
    """The tradeskill a combine requires. A skill of 0 can attempt only when skillneeded is 0, and it fails below trivial."""
    name = info.get("skill_name") or ""
    if not name and info.get("skill"):
        name = f"skill {info['skill']}"
    needed = int(info.get("skillneeded") or 0)
    trivial = int(info.get("trivial") or 0)
    parts = []
    if needed and trivial and needed != trivial:
        head = f"{name} {needed}".strip()
        parts.append(f"Requires {head}. Trivial at {trivial}.")
    elif trivial:
        head = f"{name}, trivial {trivial}" if name else f"trivial {trivial}"
        parts.append(f"Requires {head}.")
    elif needed:
        parts.append(f"Requires {f'{name} {needed}'.strip()}.")
    elif name and int(info.get("skill") or 0) in _CRAFT_SKILLS:
        parts.append(f"Requires {name}.")
    if info.get("nofail"):
        parts.append("The combine does not fail.")
    if int(info.get("must_learn") or 0) & 1:
        parts.append("The recipe must be learned first.")
    return " ".join(parts)


def item_name(items, item_id) -> str:
    info = items.get(int(item_id)) or {}
    return f"{info.get('name') or 'unnamed'} ({item_id})"


def _pretty(name: str) -> str:
    cleaned = " ".join(str(name).replace("_", " ").replace("`", "'").split())
    # Spawn comments sometimes leave "(186107) real" after the name.
    cleaned = re.sub(r"\s*\(\d+\)\s*.*$", "", cleaned).strip()
    if cleaned.islower():
        return cleaned.title()
    return cleaned


def quoted(name: str) -> str:
    return f'"{_pretty(name)}"' if str(name).strip() else ""


def quoted_item(items, item_id) -> str:
    info = items.get(int(item_id)) or {}
    return f"{quoted(info.get('name') or 'unnamed')} ({item_id})"


def quoted_who(who: str) -> str:
    zone, _, npc = str(who).partition("/")
    if not npc:
        return who
    return f"{zone}/{quoted(npc)}"


def quoted_action(items, action: str) -> str:
    if action.startswith("hand "):
        parts = []
        for bit in action[5:].split("+"):
            parts.append(quoted_item(items, int(bit)) if bit.isdigit() else bit)
        return "hand " + " + ".join(parts)
    if action.startswith("say "):
        return "say " + quoted(action[4:])
    return action


def parse_who(source: str) -> tuple[str, str, str]:
    source = str(source)
    if "#recipe:" in source:
        who, _, recipe_id = source.partition("#recipe:")
        return who, f"combine recipe {recipe_id}", who.split("/", 1)[0]
    if "#" not in source:
        zone = source.split("/", 1)[0]
        return source, "", zone
    who, act = source.split("#", 1)
    act = act.split("#holds:")[0].split("#branch:")[0]
    if act.startswith("hand:"):
        act = "hand " + act[5:]
    elif act.startswith("timer:"):
        act = f"on timer {act[6:]}"
    elif act.startswith("event:"):
        act = f"on event {act[6:]}"
    elif act in {"enter", "loot", "kill"} or act.startswith("event_"):
        act = f"on {act}"
    else:
        act = f"say {act}"
    return who, act, who.split("/", 1)[0]


def bundle(by_from, by_group, source: str, group: str) -> list[dict]:
    rows = []
    seen = set()
    scoped = bool(group and group != source)
    for key in dict.fromkeys((source, group)):
        if not key:
            continue
        # Source-level lookup must not import the requirements of another
        # branch in the same callback. The selected group is authoritative.
        candidates = by_from.get(key, []) + by_group.get(key, [])
        for edge in candidates:
            if scoped and edge.get("group") not in (group, None, ""):
                continue
            if scoped and key == source and edge.get("group") in (None, ""):
                # Ungrouped legacy edges may describe another sibling too;
                # only the selected branch is usable for its prerequisites.
                continue
            ident = (
                edge.get("rel"),
                edge.get("from"),
                edge.get("to"),
                edge.get("at"),
                edge.get("value"),
                edge.get("flag"),
                edge.get("item"),
                edge.get("op"),
                edge.get("npc"),
            )
            if ident in seen:
                continue
            seen.add(ident)
            rows.append(edge)
    return rows


def signature(by_from, by_group, edge: dict) -> tuple:
    rows = bundle(by_from, by_group, edge.get("from", ""), edge.get("group", ""))
    parts = []
    for row in rows:
        source = re.sub(r"^[^/#]+/", "", str(row.get("from") or ""))
        parts.append(
            (
                row.get("rel"),
                source,
                row.get("to"),
                row.get("at"),
                row.get("value"),
                row.get("op"),
                row.get("flag"),
            )
        )
    return tuple(sorted(parts, key=lambda part: tuple(str(bit) for bit in part)))


def quote_for(says, who: str, action: str) -> str:
    if not action.startswith("say "):
        return ""
    word = action[4:].lower()
    zone, _, npc = who.partition("/")
    text = says.get((zone.lower(), npc.lower(), word), "")
    text = " ".join(text.split())
    if len(text) > 160:
        text = text[:157] + "..."
    return text.replace("`", "'")


def _section(entry) -> tuple[str, int | None, int | None, str | None]:
    if isinstance(entry, str):
        return entry, None, None, None
    flag, lo, hi, era = entry
    return flag, lo, hi, era


def _era_rank(entry) -> tuple:
    """1.0, then 1.5, then 2.0. A pre flag stays in front of the epic in the same era."""
    flag, lo, hi, era = _section(entry)
    name = flag.lower()
    if era == "2.0" or "20" in name:
        rank = 2
    elif era == "1.5" or "15" in name:
        rank = 1
    else:
        rank = 0
    pre = 0 if "pre" in name or name.endswith("pq") else 1
    slice_order = 0 if hi is not None else (1 if lo is not None else 0)
    return (rank, slice_order, pre, name)


def _at_fits(at, lo: int | None, hi: int | None) -> bool:
    digits = "".join(ch if ch.isdigit() else " " for ch in str(at or "")).split()
    if not digits:
        return lo is None
    number = int(digits[0])
    if lo is not None and number < lo:
        return False
    if hi is not None and number >= hi:
        return False
    return True


def class_flags(sets_of, mains, prefixes) -> set[str]:
    found = set(_section(entry)[0] for entry in mains)
    for flag in sets_of:
        if any(flag.startswith(prefix) for prefix in prefixes):
            found.add(flag)
    return found


def prefers(by_from, by_group, edge: dict, flags: set[str]) -> bool:
    group = edge.get("group") or ""
    for row in (
        by_from.get(group, [])
        + by_from.get(edge.get("from"), [])
        + by_group.get(group, [])
    ):
        if row.get("rel") == "needs" and row.get("flag") in flags:
            return True
    return False


def write_class(name, title, mains, prefixes, ctx, *, verbose=False):
    (
        items,
        says,
        by_from,
        by_group,
        sets_of,
        gives,
        loots,
        grounds,
        produces,
        recipe,
        dialogues,
    ) = ctx
    flags = class_flags(sets_of, mains, prefixes)
    triggered = {
        str(row.get("to"))
        for rows in by_from.values()
        for row in rows
        if row.get("rel") == "triggers"
    }
    # A shared player event can contain branches for several classes.  Its
    # graph source (e.g. veksar/player#enter) is not branch-specific; exclude
    # predicates owned exclusively by another class rather than turning the
    # Ranger event into a prerequisite for the Warrior epic (and vice versa).
    owners: dict[str, set[str]] = defaultdict(set)
    for slug, _label, class_mains, class_prefixes in CLASSES:
        for owned_flag in class_flags(sets_of, class_mains, class_prefixes):
            owners[owned_flag].add(slug)
    foreign_flags = {
        flag for flag, slugs in owners.items() if name not in slugs and len(slugs) == 1
    }

    def foreign_only_source(edge: dict) -> bool:
        """Avoid choosing a different class's quest reward as our source.

        The player event graph sometimes coalesces Ranger and Warrior branches
        under one source.  Preserve those shared events when this class also
        has a predicate on that source.
        """
        needed = [
            row.get("flag")
            for row in bundle(
                by_from, by_group, edge.get("from", ""), edge.get("group", "")
            )
            if row.get("rel") == "needs" and row.get("flag")
        ]
        return any(flag in foreign_flags for flag in needed) and not any(
            flag in flags for flag in needed
        )

    lines: list[str] = []
    shown_dialogues: set[str] = set()

    def dialogue_lines(who: str, pad: str = "  ") -> list[str]:
        """Full conversation, including guards and reply effects, at first encounter."""
        if not verbose:
            return []
        key = str(who).lower()
        if key in shown_dialogues:
            return []
        records = dialogues.get(key, ())
        if not records:
            return []
        shown_dialogues.add(key)
        output = [f"{pad}- Dialogue with {quoted_who(key)}:"]
        for chain in records:
            # Prefer an earlier SAY prompt over item/trade speech. External
            # events can mention the same word in entirely different quest
            # states; they are evidence only when no earlier SAY prompt exists.
            transitions_by_target: dict[str, list[dict]] = defaultdict(list)
            for transition in chain.get("transitions", ()):
                target = transition.get("_to", "")
                transitions_by_target[str(target).casefold()].append(transition)
            
            previous = None
            earlier_inputs: set[str] = set()
            for turn in chain.get("turns", ()):
                utterance = str(turn.get("input") or "")
                candidates = transitions_by_target.get(utterance.casefold(), ())
                # Only a SAY response already encountered in this displayed
                # chain can introduce the next utterance. Prefer the immediately
                # preceding response, then any older response. The source can
                # still be an EVENT_ITEM when no earlier SAY speech prompts it.
                grounded_say = [
                    t for t in candidates
                    if t.get("basis") not in {"conversation_sequence", "external_event_mention"}
                    and str(t.get("_from") or "").casefold()
                    in earlier_inputs
                ]
                transition = next(
                    (t for t in grounded_say
                     if str(t.get("_from") or "").casefold()
                     == str(previous or "").casefold()),
                    grounded_say[0] if grounded_say else None,
                )
                if transition is None:
                    external = [
                        t for t in candidates
                        if t.get("basis") == "external_event_mention"
                    ]
                    # Multiple unrelated hand-ins mentioning a keyword do not
                    # establish which event prompted the player. Do not pick
                    # one arbitrarily and present it as the quest path.
                    if len(external) == 1:
                        transition = external[0]
                if transition is None and previous is not None:
                    transition = next(
                        (t for t in candidates
                         if t.get("basis") == "conversation_sequence"
                         and t.get("_from") == previous),
                        None,
                    )
                entry = f"{pad}  - Player: {quoted(utterance)}"
                
                if transition:
                    basis = str(transition.get("basis") or "")
                    if basis:
                        entry += f" (link: {basis.replace('_', ' ')})"
                
                output.append(entry)
                if transition and transition.get("basis") == "external_event_mention":
                    event = str(transition.get("event") or "event_item")
                    output.append(f"{pad}    - Prompted by `{event}`:")
                    evidence = " ".join(str(transition.get("evidence") or "").split())
                    if evidence:
                        output.append(f"{pad}      - NPC say: {evidence}")
                    for guard in transition.get("guards") or ():
                        output.append(f"{pad}      - Event guard: `{guard}`")
                
                elif transition and transition.get("basis") != "conversation_sequence":
                    origin = transition.get("_from")
                    if origin and origin != previous:
                        output.append(f"{pad}    - Prompted by player input: {quoted(origin)}")
                
                for reply in turn.get("reply") or ():
                    channel = reply.get("channel", "say")
                    speech = " ".join(str(reply.get("text") or "").split())
                    if speech:
                        output.append(f"{pad}    - NPC {channel}: {speech}")
                    for guard in reply.get("guards") or ():
                        output.append(f"{pad}      - Reply guard: `{guard}`")
                
                for guard in turn.get("guards") or ():
                    output.append(f"{pad}    - Condition: `{guard}`")
                
                for effect in turn.get("effects") or ():
                    rel = effect.get("rel")
                    if rel == "gives":
                        output.append(
                            f"{pad}    - Gives {item_name(items, effect['item'])}."
                        )
                    elif rel == "sets":
                        output.append(
                            f"{pad}    - Sets `{effect['flag']}` to `{effect.get('value')}`."
                        )
                    elif rel == "spawns":
                        output.append(f"{pad}    - Spawns NPC {effect['npc']}.")
                previous = utterance
                earlier_inputs.add(utterance.casefold())
        return output

    seen_flags: set[str] = set()
    seen_recipes: set[int] = set()

    def handed(edge: dict) -> list[int]:
        source = str(edge.get("group") or edge.get("from") or "")
        found: list[int] = []
        for row in by_group.get(source, []) + by_from.get(source, []):
            if row.get("rel") != "receives" or not str(row.get("to", "")).startswith(
                "item:"
            ):
                continue
            needed = int(row["to"].split(":", 1)[1])
            if needed not in found:
                found.append(needed)
        return found

    prereq_ids: list[int] = []
    first_seen_item: dict[int, int] = {}

    def recipe_inputs(recipe_id: int) -> set[int]:
        info = recipe.get(recipe_id) or {}
        found = {int(comp) for comp, _count in info.get("consumes") or []}
        if info.get("container"):
            found.add(int(info["container"]))
        return found

    def creating(item_id: int) -> list[int]:
        """Recipes that make this item. A combine that hands the item back plus something new does not make it."""
        made = []
        for rid in produces.get(item_id, []):
            if item_id in recipe_inputs(rid) or rid in made:
                continue
            made.append(rid)
        linked = []
        for rid in made:
            for edge in sets_of_flat(flags):
                source = str(edge.get("from") or "")
                if f"#recipe:{rid}" in source and edge.get("flag") in flags:
                    linked.append(rid)
                    break
        if linked:
            return linked[:1]
        # Generic PEQ recipes may produce one item through dozens of unrelated
        # combines. RecipeBook.for_item chooses one enabled, non-refunding,
        # low-component recipe, avoiding sprawling branches (e.g. Bottle).
        preferred = RECIPE_BOOK.for_item(int(item_id))
        # If an item is available in many zones, generic brewing/crafting
        # variants are not evidence that an epic must execute one of them.
        widely_available = len((items.get(int(item_id)) or {}).get("zones") or []) >= 4
        if len(made) > 2 and widely_available:
            return []
        if preferred is not None and preferred.id in made:
            return [preferred.id]
        if len(made) <= 2:
            return made[:1]
        return []

    def real_givers(item_id: int) -> list[dict]:
        givers = [
            edge
            for edge in gives.get(item_id, [])
            if not _recipe_refund(recipe, edge, item_id)
            and item_id not in handed(edge)
            and not foreign_only_source(edge)
        ]
        gated = [edge for edge in givers if prefers(by_from, by_group, edge, flags)]
        candidates = gated or givers

        def necessarily_requires(
            needed: int, target: int, visiting: frozenset[int] = frozenset()
        ) -> bool:
            """True only if every known way to acquire `needed` depends on `target`.

            A returned quest container must not be selected as its own initial
            source. Explore alternative producers before declaring a cycle.
            """
            if needed == target:
                return True
            if needed in visiting:
                return False
            active = visiting | {needed}
            paths = [
                handed(giver)
                for giver in gives.get(needed, ())
                if not _recipe_refund(recipe, giver, needed)
                and needed not in handed(giver)
            ]
            paths.extend(
                list(recipe_inputs(rid))
                for rid in produces.get(needed, ())
                if needed not in recipe_inputs(rid)
            )
            return bool(paths) and all(
                any(
                    necessarily_requires(component, target, active)
                    for component in path
                )
                for path in paths
            )

        def cyclic_source(edge: dict) -> bool:
            return any(
                necessarily_requires(component, item_id) for component in handed(edge)
            )

        # A reward that returns inputs from a later combine is not the initial
        # way of obtaining them.  For 62611-62614, Corun gives the blood samples
        # back AFTER 62615 is handed in, but recipes 13406-13409 create them.
        # Do not emit both acquisition paths as mandatory sequential actions.
        noncyclic = [edge for edge in candidates if not cyclic_source(edge)]
        if noncyclic:
            candidates = noncyclic
        elif creating(item_id):
            return []  # use the noncyclic recipe instead of a return/reward loop

        return sorted(
            candidates,
            key=lambda edge: (
                cyclic_source(edge),
                not bool(
                    handed(edge)
                    or any(
                        row.get("rel") == "needs"
                        for row in bundle(
                            by_from,
                            by_group,
                            edge.get("from", ""),
                            edge.get("group", ""),
                        )
                    )
                ),
                str(edge.get("group") or edge.get("from")),
            ),
        )[:1]

    def note_prereq(item_id: int) -> None:
        if item_id and item_id not in prereq_ids:
            prereq_ids.append(int(item_id))

    def is_chain(item_id: int) -> bool:
        """A multi-step questline: a combine, or an NPC who needs item turn-ins."""
        if creating(item_id):
            return True
        if any(
            "#timer:" in str(edge.get("from") or "") for edge in loots.get(item_id, [])
        ):
            return True
        if any(
            "#timer:" in str(edge.get("group") or "") for edge in real_givers(item_id)
        ):
            return True
        return any(
            handed(edge)
            or any(
                row.get("rel") == "needs" and (row.get("flag") or row.get("item"))
                for row in bundle(
                    by_from, by_group, edge.get("from", ""), edge.get("group", "")
                )
            )
            for edge in real_givers(item_id)
        )

    def simple_acquire(item_id: int) -> list[str]:
        """Buy it, say a word, or take a coin hand-in. Not its own questline section."""
        if is_chain(item_id) or creating(item_id):
            return []
        return [giver_sentence(edge, item_id) for edge in real_givers(item_id)]

    def hand_before_loot(zone: str, spawn_name: str) -> list[str]:
        """Get the turn-in items, hand them over, then the fight/loot can happen."""
        if not spawn_name:
            return []
        want = f"{zone}/{spawn_name.replace('_', ' ').lower()}"
        found = []
        seen = set()
        for source, rows in by_group.items():
            if not str(source).startswith(want + "#hand:"):
                continue
            who, action, _zone = parse_who(source)
            turns = []
            needed_ids = []
            sets = []
            for row in rows + by_from.get(source, []):
                if row.get("rel") == "receives" and str(row.get("to", "")).startswith(
                    "item:"
                ):
                    needed = int(row["to"].split(":", 1)[1])
                    needed_ids.append(needed)
                    turns.append(quoted_item(items, needed))
                elif row.get("rel") == "sets" and row.get("flag"):
                    sets.append(f"`{row['flag']}` to `{row.get('value')}`")
            if not turns:
                continue
            key = (source, tuple(turns))
            if key in seen:
                continue
            seen.add(key)
            for needed in needed_ids:
                found.extend(simple_acquire(needed))
            text = f"Hand {' + '.join(turns)} to {quoted_who(who)}."
            if sets:
                text += " Sets " + "; ".join(sets) + "."
            found.append(text)
        return found[:6]

    def event_chain(
        source: str,
        expand_item=None,
        visiting: frozenset[str] = frozenset(),
    ) -> list[str]:
        """Explain named timers by following causal edges, including encounter lifecycle."""
        if source in visiting:
            return [f"**Broken:** cyclic event trigger at `{source}`."]

        incoming = [
            edge
            for rows in by_from.values()
            for edge in rows
            if edge.get("rel") == "triggers" and edge.get("to") == source
        ]
        if not incoming:
            if "#event:spawn:" in source:
                npc = source.rsplit(":", 1)[-1]
                who, _, zone = parse_who(source)
                return [f"Encounter starts when NPC {npc} spawns in `{zone}`."]
            if "#signal:" in source or "#event_signal" in source:
                return [f"**Broken:** no event trigger found for `{source}`."]
            if "#event:" in source:
                who, action, _zone = parse_who(source)
                return [f"{quoted_who(who)}, {action}."]
            return [f"**Broken:** no event trigger found for `{source}`."]

        # More than one incoming edge means alternative routes, not mandatory steps.
        edge = sorted(
            incoming,
            key=lambda row: (
                0 if "#event:spawn:" in str(row.get("from", "")) else 1,
                str(row.get("from", "")),
            ),
        )[0]
        parent = str(edge["from"])
        active = visiting | {source}
        if any(mark in parent for mark in ("#signal:", "#timer:", "#event:", "#event_", "#kill:")):
            steps = event_chain(parent, expand_item, active)
            if "#kill:" in source:
                steps.append(f"Kill NPC {source.rsplit(':', 1)[-1]}.")
            elif "#timer:" in source:
                steps.append(f"Starts timer `{source.rsplit(':', 1)[-1]}`.")
            return steps

        who, action, _zone = parse_who(parent)
        steps: list[str] = []
        for needed in handed({"from": parent, "group": parent}):
            if expand_item is not None:
                expand_item(needed)
            else:
                steps.append(f"Acquire {quoted_item(items, needed)}.")
        description = quoted_who(who)
        if action:
            description += f", {quoted_action(items, action)}"
        steps.append(f"{description}. Triggers `{source}`.")
        return steps

    def leaf_bits(item_id: int, expand_item=None, expand_action=None) -> list[str]:
        bits = []
        for edge in real_givers(item_id):
            who, action, _zone = parse_who(edge.get("group") or edge.get("from"))
            # bits.append(f"Given by {quoted_who(who)}" + (f", {quoted_action(items, action)}" if action else "") + ".")
            # New
            bits.extend(giver_prereqs(edge))
            bits.append(
                f"Given by {quoted_who(who)}"
                + (f", {quoted_action(items, action)}" if action else "")
                + "."
            )
            # new end
        loot_rows = loots.get(item_id, [])
        gated_loot = [
            edge for edge in loot_rows if prefers(by_from, by_group, edge, flags)
        ]
        # One loot path is sufficient to acquire an item. The old code emitted
        # up to four routes consecutively, falsely implying four required kills.
        possible_loot = [
            edge for edge in (gated_loot or loot_rows) if not foreign_only_source(edge)
        ]
        unique_loot = list(
            dict.fromkeys(
                (str(edge.get("from") or ""), str(edge.get("npc") or ""))
                for edge in possible_loot
            )
        )
        chosen_loot = next(
            (edge for edge in possible_loot if "#hand:" in str(edge.get("from") or "")),
            None,
        )
        if chosen_loot is None:
            # A timer without a causal `triggers` edge is NOT an executable
            # acquisition path. Prefer a reachable timer, then any other
            # explicit encounter, before resorting to an orphan timer.
            chosen_loot = next(
                (
                    edge for edge in possible_loot
                    if "#timer:" in str(edge.get("from") or "")
                    and str(edge.get("from")) in triggered
                ),
                None,
            )
        if chosen_loot is None:
            chosen_loot = next(
                (edge for edge in possible_loot
                 if "#" in str(edge.get("from") or "")
                 and "#timer:" not in str(edge.get("from") or "")),
                None,
            )
        if chosen_loot is None:
            chosen_loot = next(
                (edge for edge in possible_loot if "#" in str(edge.get("from") or "")),
                None,
            )
        if chosen_loot is None and possible_loot:
            chosen_loot = possible_loot[0]
        for edge in ([chosen_loot] if chosen_loot else []):
            if expand_action is not None:
                expand_action(edge)
            source = str(edge.get("from") or "")
            who, action, zone = parse_who(source)
            spawn = str(edge.get("name") or "")
            if edge.get("npc") and not spawn:
                for row in by_group.get(source, []) + by_from.get(source, []):
                    if (
                        row.get("rel") == "spawns"
                        and row.get("npc") == edge.get("npc")
                        and row.get("name")
                    ):
                        spawn = str(row["name"])
                        break
            corpse = (
                quoted(spawn)
                if spawn
                else (f"npc {edge['npc']}" if edge.get("npc") else "")
            )
            npc_id = edge.get("npc")
            parts = []
            if "#timer:" in source:
                bits.extend(event_chain(source, expand_item))
                bits.append(f"Spawns {corpse} ({npc_id}) after `{source}`.")
                bits.append(f"Loot {quoted_item(items, item_id)} from {corpse}.")
            elif ("#signal:" in source or "#event_signal" in source) and corpse:
                # Signals are not free spawns. Walk their incoming causal chain,
                # including earlier hand-ins, NPC spawns and required kills.
                bits.extend(event_chain(source, expand_item))
                bits.append(f"Loot {quoted_item(items, item_id)} from {corpse}.")
            elif action.startswith("hand ") and corpse:
                for bit in action[5:].split("+"):
                    if bit.isdigit():
                        bits.extend(simple_acquire(int(bit)))
                parts.append(
                    f"Hand {quoted_action(items, action)[5:]} to {quoted_who(who)}."
                )
                parts.append(
                    f"Spawns {corpse}" + (f" ({npc_id})" if npc_id else "") + "."
                )
                parts.append(f"Loot {quoted_item(items, item_id)} from {corpse}.")
                bits.append(" ".join(parts))
            elif action.startswith("on ") and corpse:
                # The zone/NPC event only places the corpse NPC. Name who triggered it when we can.
                trigger = quoted_who(who)
                if action == "on event_death_complete":
                    bits.append(
                        f"Kill {trigger}. Spawns {corpse}"
                        + (f" ({npc_id})" if npc_id else "")
                        + "."
                    )
                else:
                    bits.append(
                        f"Spawns {corpse}"
                        + (f" ({npc_id})" if npc_id else "")
                        + f" in `{zone}` {action}."
                    )
                bits.extend(hand_before_loot(zone, spawn))
                bits.append(f"Loot {quoted_item(items, item_id)} from {corpse}.")
            elif action.startswith("say ") and corpse:
                bits.append(
                    f'{quoted_action(items, action).replace("say ", "Say ", 1)} to {quoted_who(who)}.'
                )
                bits.append(
                    f"Spawns {corpse}" + (f" ({npc_id})" if npc_id else "") + "."
                )
                bits.append(f"Loot {quoted_item(items, item_id)} from {corpse}.")
            elif corpse:
                where = f" at {quoted_who(who)}" + (
                    f", {quoted_action(items, action)}" if action else ""
                )
                bits.append(
                    f"Loot {quoted_item(items, item_id)} from {corpse}"
                    + (f" ({npc_id})" if npc_id and not spawn else "")
                    + f"{where}."
                )
            else:
                bits.append(
                    f"Loot {quoted_item(items, item_id)} at {quoted_who(who)}"
                    + (f", {quoted_action(items, action)}" if action else "")
                    + "."
                )
        # Show every distinct loot source, rather than hiding them behind a count.
        # Only the selected source expands prerequisites; alternatives are choices,
        # not additional mandatory encounters.
        selected_key = (
            (str(chosen_loot.get("from") or ""), str(chosen_loot.get("npc") or ""))
            if chosen_loot
            else None
        )
        for source, npc in unique_loot:
            if (source, npc) == selected_key:
                continue
            alternate = next(
                edge
                for edge in possible_loot
                if str(edge.get("from") or "") == source
                and str(edge.get("npc") or "") == npc
            )
            who, action, zone = parse_who(source)
            name = str(alternate.get("name") or "")
            corpse = (
                quoted(name) if name else (f"NPC {npc}" if npc else quoted_who(who))
            )
            ident = f" (NPC {npc})" if npc and name else ""
            where = f" in `{zone}`" if zone else ""
            trigger = (
                f"; trigger: {quoted_who(who)}, {quoted_action(items, action)}"
                if action
                else ""
            )
            bits.append(
                f"Alternative: Loot {quoted_item(items, item_id)} "
                f"from {corpse}{ident}{where}{trigger}."
            )
        for edge in grounds.get(item_id, [])[:3]:
            bits.append(
                f"Ground spawn of {quoted_item(items, item_id)} in `{edge.get('zone') or 'an unstated zone'}`."
            )
        for line in _made_by(items, item_id):
            if loot_rows and line.startswith("- Loot "):
                continue
            bits.append(line[2:] if line.startswith("- ") else line)
        # The selected recipe is already emitted by forward(); don't expand
        # alternate unrelated generic recipes as mandatory sources in a leaf.
        if expand_item is None:
            for rid in creating(item_id):
                bits.append(recipe_sentence(rid))
        if bits:
            return bits
        # Duplicate epic reward ids (Spear of Fate 10651 vs 36223). Prefer the id a script gives.
        alias = _ITEM_ALIAS.get(int(item_id))
        if alias and alias != item_id:
            bits = leaf_bits(alias)
            if bits and not bits[0].startswith("**Broken:**"):
                return [f"Same item as {quoted_item(items, alias)}."] + bits

        merchant = fallback_merchant(items, item_id)
        if merchant:
            return [merchant]

        fallback = fallback_drop(items, item_id)
        if fallback:
            return [fallback]

        zones = (items.get(item_id) or {}).get("zones") or []
        if zones:
            if len(zones) > 3:
                return [
                    f"Common item: {item_name(items, item_id)}. Listed in {len(zones)} zones."
                ]
            shown = ", ".join(zones)
            return [
                f"No quest step gives {item_name(items, item_id)}. The dump lists it in {shown}."
            ]
        return [
            f"**Broken:** nothing in the graph gives, loots, spawns, or combines {item_name(items, item_id)}."
        ]

    def cite(item_id: int) -> list[str]:
        if is_chain(item_id):
            note_prereq(item_id)
            return [f"- Prerequisite: {quoted_item(items, item_id)}. See section 0."]
        return [f"- {bit}" for bit in leaf_bits(item_id)]

    def recipe_sentence(recipe_id: int) -> str:
        info = recipe[recipe_id]
        if info.get("world"):
            where = f"{info['world']['name']} ({info['world']['id']})"
        elif info.get("container"):
            where = quoted_item(items, info["container"])
        else:
            where = "no container"
        puts = ", ".join(
            quoted_item(items, comp) for comp, _count in info.get("consumes") or []
        )
        products = list(info.get("products") or [])
        if not products and info.get("produces"):
            products = [(info["produces"], 1)]
        inputs = recipe_inputs(recipe_id)
        handed_back = [
            quoted_item(items, comp) for comp, _count in products if comp in inputs
        ]
        fresh = [
            quoted_item(items, comp) + (f" x{count}" if count > 1 else "")
            for comp, count in products
            if comp not in inputs
        ]
        text = f"Combine in {where}: {puts or 'nothing'}."
        if handed_back:
            text += " Hands back " + ", ".join(handed_back) + "."
        text += " Produces " + (", ".join(fresh) if fresh else "no new item") + "."
        skill = _skill_line(info)
        if skill:
            text += f" {skill}"
        return text

    # new
    def giver_prereqs(edge: dict) -> list[str]:
        rows = bundle(
            by_from,
            by_group,
            edge.get("from", ""),
            edge.get("group", ""),
        )

        return list(
            dict.fromkeys(
                f"Requires `{row['flag']}` {row.get('at') or 'set'}"
                for row in rows
                if row.get("rel") == "needs"
                and row.get("flag")
                and row.get("flag") not in foreign_flags
            )
        )

    def giver_sentence(edge: dict, item_id: int) -> str:
        who, action, _zone = parse_who(edge.get("group") or edge.get("from"))
        text = quoted_who(who)
        if action:
            text += ", " + quoted_action(items, action)
        if not action.startswith("hand"):
            turns = ", ".join(quoted_item(items, needed) for needed in handed(edge))
            if turns:
                text += f". Turn in {turns}"

        prereqs = giver_prereqs(edge)
        if prereqs:
            text += ". " + ". ".join(prereqs)

        text += f". Gives {quoted_item(items, item_id)}."
        return text

    # new end
    # def giver_sentence(edge: dict, item_id: int) -> str:
    #     who, action, _zone = parse_who(edge.get("group") or edge.get("from"))
    #     text = quoted_who(who)
    #     if action:
    #         text += ", " + quoted_action(items, action)
    #     if not action.startswith("hand"):
    #         turns = ", ".join(quoted_item(items, needed) for needed in handed(edge))
    #         if turns:
    #             text += f". Turn in {turns}"
    #     text += f". Gives {quoted_item(items, item_id)}."
    #     return text

    def take_simple(item_id: int, steps: list[str], seen: set) -> None:
        for text in simple_acquire(item_id):
            key = ("simple", item_id, text)
            if key in seen:
                continue
            seen.add(key)
            steps.append(text)

    def forward(
        item_id: int,
        trail: set[int],
        steps: list[str],
        seen: set,
        goal: int,
        flag_trail: frozenset[str] = frozenset(),
    ) -> None:
        if item_id in trail:
            return
        if item_id in seen:
            earlier = first_seen_item.get(item_id)
            if earlier and earlier != goal:
                ref_key = ("already-documented", goal, item_id)
                if ref_key not in seen:
                    seen.add(ref_key)
                    steps.append(
                        f"Acquisition of {quoted_item(items, item_id)} is documented "
                        f"under {quoted_item(items, earlier)}; obtain another copy if needed."
                    )
            return

        seen.add(item_id)
        first_seen_item[item_id] = goal
        trail = trail | {item_id}

        def dependencies(edge: dict) -> list[dict]:
            """Requirements on this action, with weaker 'set' checks subsumed.

            `flag == N` already entails `flag set`. Keeping both causes a
            spurious recursive lookup for the same global (Soulwhisper).
            """
            rows = [
                row
                for row in bundle(
                    by_from,
                    by_group,
                    edge.get("from", ""),
                    edge.get("group", ""),
                )
                if row.get("rel") == "needs" and row.get("flag") not in foreign_flags
            ]
            precise = {
                str(row["flag"])
                for row in rows
                if row.get("flag") and str(row.get("at") or "set") != "set"
            }
            filtered = [
                row
                for row in rows
                if not (
                    row.get("flag") in precise and str(row.get("at") or "set") == "set"
                )
            ]
            return list(
                {
                    (
                        str(row.get("flag")),
                        str(row.get("at")),
                        str(row.get("item")),
                        str(row.get("state")),
                        str(row.get("op")),
                    ): row
                    for row in filtered
                }.values()
            )

        def value_matches(value: str, at: str) -> bool:
            if at == "set":
                return True
            if at == "unset":
                return False

            match = re.fullmatch(r"(==|!=|>=|<=|>|<)(-?\d+)", at)
            if not match:
                return False

            try:
                actual = int(value)
            except (TypeError, ValueError):
                return False

            op, expected = match.group(1), int(match.group(2))
            return {
                "==": actual == expected,
                "!=": actual != expected,
                ">=": actual >= expected,
                "<=": actual <= expected,
                ">": actual > expected,
                "<": actual < expected,
            }[op]

        def expand_item(needed: int) -> None:
            forward(
                needed,
                trail,
                steps,
                seen,
                goal,
                flag_trail,
            )

        def expand_flag(
            flag: str, at: str, active: frozenset[tuple[str, str]] = frozenset()
        ) -> None:
            """Resolve an exact quest-global state, including earlier values of the SAME flag.

            Different values of Soulwhisper are successive states, not a flag
            recursion cycle. The active path tracks (flag, predicate), while
            'seen' tracks only transitions that have actually been emitted.
            """
            predicate = at.replace(" ", "")
            state = (flag, predicate)
            # Any concrete, already-active value satisfies a bare `set`
            # requirement. It is not another step of the state machine.
            if predicate == "set" and any(
                f == flag and p not in {"set", "unset"} for f, p in active
            ):
                return
            if state in active:
                steps.append(f"Unresolved cyclic prerequisite: `{flag}` {at}.")
                return
            if ("flag", flag, predicate) in seen:
                return
            if predicate == "unset":
                # An initially unset global is a starting condition, not an action.
                return

            candidates = [
                edge
                for edge in sets_of.get(flag, [])
                if value_matches(str(edge.get("value", "")), predicate)
            ]
            if not candidates:
                steps.append(
                    f"Unresolved prerequisite: `{flag}` {at}; no matching setter in graph."
                )
                return

            def score(edge: dict) -> tuple:
                value = str(edge.get("value") or "")
                requirements = dependencies(edge)
                same = [row for row in requirements if row.get("flag") == flag]
                prior = []
                for row in same:
                    m = re.fullmatch(
                        r"==(\d+)", str(row.get("at") or "").replace(" ", "")
                    )
                    if m:
                        prior.append(int(m.group(1)))
                current = int(value) if value.isdigit() else None
                # Prefer the immediately preceding value, never a setter that
                # requires a *later* state (e.g. Tarlang resets 4 -> 3).
                backward = 0 if current is None else sum(p > current for p in prior)
                contiguous = 0 if current is not None and current - 1 in prior else 1
                if predicate == "set":
                    number = current if current is not None else 999999
                else:
                    number = 0
                return (
                    backward,
                    contiguous,
                    number,
                    len(handed(edge)),
                    str(edge.get("group") or edge.get("from")),
                )

            setter = min(candidates, key=score)
            source = str(setter.get("group") or setter.get("from") or "")
            setter_key = ("setter", source, flag, str(setter.get("value")))
            if setter_key in seen:
                seen.add(("flag", flag, predicate))
                return

            next_active = active | {state}
            requirements = dependencies(setter)
            mandatory = [row for row in requirements if row.get("op") != "or"]
            optional = [row for row in requirements if row.get("op") == "or"]
            # Recursing through a different value of this same flag is allowed.
            for row in mandatory + optional[:1]:
                if row.get("flag"):
                    expand_flag(
                        str(row["flag"]), str(row.get("at") or "set"), next_active
                    )
                elif row.get("item"):
                    expand_item(int(row["item"]))
            for needed in handed(setter):
                expand_item(needed)

            if setter_key not in seen:
                seen.add(setter_key)
                who, action, _zone = parse_who(source)
                description = quoted_who(who)
                if action:
                    description += f", {quoted_action(items, action)}"
                steps.append(
                    f"{description}. Sets `{flag}` to `{setter.get('value')}`."
                )
            seen.add(("flag", flag, predicate))

        def expand_action(edge: dict) -> None:
            requirements = dependencies(edge)

            # Ordinary requirements must all be satisfied.
            for row in requirements:
                if row.get("op") == "or":
                    continue

                if row.get("flag"):
                    expand_flag(
                        str(row["flag"]),
                        str(row.get("at") or "set"),
                    )
                elif row.get("item"):
                    expand_item(int(row["item"]))
                    if row.get("equipped"):
                        slot = str(row.get("slot") or "specified slot")
                        steps.append(
                            f"Equip {quoted_item(items, int(row['item']))} in {slot} slot."
                        )
                elif row.get("state") == "sitting":
                    steps.append(
                        "Sit before the NPC while its timer checks your posture."
                    )

            # Alternative requirements are not all mandatory.
            alternatives = [row for row in requirements if row.get("op") == "or"]
            if alternatives:
                selected = alternatives[0]
                if selected.get("flag"):
                    expand_flag(
                        str(selected["flag"]),
                        str(selected.get("at") or "set"),
                    )
                elif selected.get("item"):
                    expand_item(int(selected["item"]))

            for needed in handed(edge):
                expand_item(needed)

        made_here = False

        for edge in real_givers(item_id):
            group = str(edge.get("group") or edge.get("from") or "")
            if "#timer:" in group:
                for description in event_chain(group, expand_item):
                    key = ("event", group, description)
                    if key not in seen:
                        seen.add(key)
                        steps.append(description)
            expand_action(edge)

            key = (
                "give",
                str(edge.get("group") or edge.get("from")),
                item_id,
            )
            if key not in seen:
                seen.add(key)
                steps.append(giver_sentence(edge, item_id))

            made_here = True

        for rid in ([] if made_here else creating(item_id)):
            if goal in recipe_inputs(rid):
                continue

            info = recipe[rid]

            if info.get("container"):
                expand_item(int(info["container"]))

            for comp, _count in info.get("consumes") or []:
                expand_item(int(comp))

            key = ("recipe", rid)
            if key not in seen:
                seen.add(key)
                steps.append(recipe_sentence(rid))

            made_here = True

        if made_here:
            return

        for bit in leaf_bits(
            item_id, expand_item=expand_item, expand_action=expand_action
        ):
            key = ("leaf", item_id, bit)
            if key not in seen:
                seen.add(key)
                steps.append(bit)

    # def forward(item_id: int, trail: set[int], steps: list[str], seen: set, goal: int) -> None:
    #     if item_id in trail or item_id in seen or len(trail) > 12:
    #         return
    #     seen.add(item_id)
    #     trail = set(trail)
    #     trail.add(item_id)
    #     made_here = False
    #     def expand_needed(needed: int) -> None:
    #         # take_simple and forward both print a hail/buy line. Pick one.
    #         # Loot-only items have no simple_acquire text — forward into leaf_bits.
    #         if is_chain(needed) or not simple_acquire(needed):
    #             forward(needed, trail, steps, seen, goal)
    #         else:
    #             take_simple(needed, steps, seen)

    #     # NPC givers first. A split/recombine loop must not hide the hand-in that creates the item.
    #     for edge in real_givers(item_id):
    #         for needed in handed(edge):
    #             expand_needed(needed)
    #         key = ("give", str(edge.get("group") or edge.get("from")), item_id)
    #         if key not in seen:
    #             seen.add(key)
    #             steps.append(giver_sentence(edge, item_id))
    #         made_here = True
    #     for rid in creating(item_id):
    #         # A combine that consumes the item we are obtaining hands that item back. It is not a source.
    #         if goal in recipe_inputs(rid):
    #             continue
    #         info = recipe[rid]
    #         if info.get("container"):
    #             expand_needed(int(info["container"]))
    #         for comp, _count in info.get("consumes") or []:
    #             expand_needed(int(comp))
    #         key = ("recipe", rid)
    #         if key not in seen:
    #             seen.add(key)
    #             steps.append(recipe_sentence(rid))
    #         made_here = True
    #     if made_here:
    #         return
    #     for bit in leaf_bits(item_id):
    #         key = ("leaf", item_id, bit)
    #         if key in seen:
    #             continue
    #         seen.add(key)
    #         steps.append(bit)

    def render_prereqs() -> list[str]:
        block = [
            "## 0. Prerequisites",
            "",
            "Shared acquisition steps appear in the first prerequisite chain that needs them. Later sections reference that chain rather than repeating it.",
            "",
        ]

        # Probe each chain WITHOUT the shared ledger.  The old ordering was the
        # order render_flag happened to request its inputs, not the order in
        # which a player begins the quest.  Prefer chains whose initial leaf
        # is an NPC dialogue/hand-in, then use the earliest starting action as
        # a stable tie-breaker.  Only the actual rendering mutates shared_seen.
        def prereq_order(item_id: int) -> tuple:
            # forward records provenance in first_seen_item; previews must not
            # claim ownership of a chain that has not been rendered yet.
            first_seen_item.clear()
            preview: list[str] = []
            forward(item_id, set(), preview, set(), item_id)
            first = next(
                (line for line in preview if not line.startswith("Acquisition of ")), ""
            )
            # A dialogue usually introduces an epic, whereas forage, loot, and
            # crafting are subquests discovered after that introduction.
            opening = bool(re.search(r'\b(?:say|hand)\s+"?[^.]+', first, re.I))
            return (0 if opening else 1, first.casefold(), item_id)

        order = sorted(prereq_ids, key=prereq_order)
        first_seen_item.clear()
        shared_seen: set = set()
        for item_id in order:
            block.append(f"### {quoted_item(items, item_id)}")
            block.append("")
            steps: list[str] = []
            forward(item_id, set(), steps, shared_seen, item_id)
            name = quoted_item(items, item_id)
            kept: list[str] = []
            for text in steps:
                kept.append(text)
                produced = text.split("Produces ", 1)[-1] if "Produces " in text else ""
                if f"Gives {name}." in text or (
                    name in produced and "no new item" not in produced
                ):
                    break
            steps = kept
            if not steps:
                block.append("The graph has no earlier step for this.")
            for number, text in enumerate(steps, 1):
                block.append(f"{number}. {text}")
                # Conversation sources in the acquisition path are part of the
                # journey too, not just the NPCs that write epic flags.
                if verbose:
                    match = re.match(
                        r'([^\s/]+)/(?:"([^"]+)"|([^,]+)),\s*(?:say|hand)\b', text
                    )
                    if match:
                        zone, quoted_npc, plain_npc = match.groups()
                        npc = (
                            (quoted_npc or plain_npc).strip().lower().replace(" ", "_")
                        )
                        # The graph uses normalized NPC names, not the display names.
                        key = f"{zone}/{npc.replace('_', ' ')}"
                        block.extend(dialogue_lines(key, "    "))
            block.append("")
        return block

    def sets_of_flat(flag_set):
        for flag in flag_set:
            yield from sets_of.get(flag, ())

    def render_recipe(
        recipe_id: int, depth: int, trail: set[int], spawns: list[dict] | None = None
    ) -> list[str]:
        info = recipe[recipe_id]
        if (
            not info["produces"]
            and not info["consumes"]
            and not info["container"]
            and not info.get("products")
        ):
            return [
                f"- **Broken:** `recipe:{recipe_id}` is named and has no components in the graph."
            ]
        if recipe_id in seen_recipes and depth > 1:
            return [f"- `recipe:{recipe_id}` is already shown."]
        seen_recipes.add(recipe_id)
        pad = ""
        products = list(info.get("products") or [])
        if not products and info["produces"]:
            products = [(info["produces"], 1)]
        out: list[str] = []
        world = info.get("world")
        if world:
            zones = list(world.get("zones") or [])
            shown = ", ".join(zones[:6])
            extra = f" and {len(zones) - 6} more" if len(zones) > 6 else ""
            where = f" Placed in {shown}{extra}." if shown else ""
            out.append(
                f"{pad}- `recipe:{recipe_id}` is combined in {world['name']} ({world['id']}). A container in the world.{where}"
            )
        elif info["container"]:
            out.append(
                f"{pad}- `recipe:{recipe_id}` is combined in {item_name(items, info['container'])}."
            )
            for line in cite(info["container"]):
                out.append(f"{pad}  {line}")
        else:
            out.append(f"{pad}- `recipe:{recipe_id}`.")
        for item_id, count in info["consumes"]:
            out.append(f"{pad}  - Put in x{count}: {item_name(items, item_id)}.")
            for line in cite(item_id):
                out.append(f"{pad}    {line}")
        if products:
            inputs = recipe_inputs(recipe_id)
            handed_back = [
                item_name(items, comp) for comp, _count in products if comp in inputs
            ]
            fresh = [
                item_name(items, comp) + (f" x{count}" if count > 1 else "")
                for comp, count in products
                if comp not in inputs
            ]
            if handed_back:
                out.append(f"{pad}  - Hands back {', '.join(handed_back)}.")
            out.append(
                f"{pad}  - Produces {', '.join(fresh) if fresh else 'no new item'}."
            )
        elif spawns:
            for row in spawns:
                label = row.get("name") or row.get("to")
                out.append(f"{pad}  - Spawns {label} ({row.get('npc')}).")
                for loot in row.get("loots") or []:
                    out.append(f"{pad}    - Loots {item_name(items, loot)}.")
        else:
            out.append(f"{pad}  - The combine returns no item.")
        skill = _skill_line(info)
        if skill:
            out.append(f"{pad}  - {skill}")
        return out

    def render_flag(
        flag: str,
        level: int,
        lo: int | None = None,
        hi: int | None = None,
        era: str | None = None,
    ) -> None:
        if flag in seen_flags and lo is None and hi is None:
            lines.append(f"{'#' * min(level, 4)} `{flag}`")
            lines.append("")
            lines.append(f"See `{flag}` earlier in this file.")
            lines.append("")
            return
        seen_flags.add(flag)
        sets = []
        for edge in sets_of.get(flag, ()):
            value_text = str(edge.get("value") or "")
            if value_text.isdigit():
                value = int(value_text)
                if lo is not None and value < lo:
                    continue
                if hi is not None and value >= hi:
                    continue
            elif lo is not None or hi is not None:
                continue
            sets.append(edge)
        hashes = "#" * min(level, 4)
        title = f"`{flag}`" + (f" {era}" if era else "")
        lines.append(f"{hashes} {title}")
        lines.append("")
        if not sets:
            lines.append(f"**Broken:** nothing in the graph sets `{flag}`.")
            lines.append("")
            return
        numeric = sorted(
            {
                int(edge["value"])
                for edge in sets
                if str(edge.get("value", "")).isdigit()
            }
        )
        if numeric:
            lines.append(
                f"Values written: {', '.join(str(number) for number in numeric)}."
            )
            lines.append("")
        odd = sorted(
            {
                str(edge.get("value"))
                for edge in sets
                if not str(edge.get("value", "")).isdigit()
            }
        )
        if odd:
            lines.append(
                "**Broken:** these writes are not a plain number, so they cannot be ordered: "
                + ", ".join(f"`{value}`" for value in odd)
                + "."
            )
            lines.append("")
        groups: dict[tuple, list] = {}
        for edge in sets:
            key = (str(edge.get("value")), signature(by_from, by_group, edge))
            groups.setdefault(key, []).append(edge)

        def stage_sort(group):
            edge = group[0]
            value = str(edge.get("value") or "")
            if not value.isdigit():
                return (1, float("inf"), str(edge.get("from")))
            current = int(value)
            rows = bundle(
                by_from, by_group, edge.get("from", ""), edge.get("group", "")
            )
            predecessors = []
            for row in rows:
                if row.get("rel") == "needs" and row.get("flag") == flag:
                    match = re.fullmatch(
                        r"==(\d+)", str(row.get("at") or "").replace(" ", "")
                    )
                    if match:
                        predecessors.append(int(match.group(1)))
            rollback_from = max((n for n in predecessors if n > current), default=None)
            position = (
                float(rollback_from) + 0.5
                if rollback_from is not None
                else float(current)
            )
            return (0, position, str(edge.get("from")))

        ordered = sorted(groups.values(), key=stage_sort)
        used = set()
        shown_values: set[str] = set()
        for group in ordered:
            value = str(group[0].get("value") or "")
            if value in shown_values:
                lines.append(
                    f"Alternative or repeat transition to `{flag}` = `{value}` (not an additional required stage)."
                )
                lines.append("")
            shown_values.add(value)
            render_step(group, level + 1, flag)
            for edge in group:
                used.add(edge.get("from"))
                if edge.get("group"):
                    used.add(edge.get("group"))
        render_extras(flag, used, level + 1, lo, hi)

    def render_step(group: list[dict], level: int, flag: str) -> None:
        """Walkthrough-style stage: action, requirements, then effects and subquests."""
        edge = group[0]
        source = str(edge.get("from") or "")
        who, action, zone = parse_who(source)
        rows = bundle(by_from, by_group, source, edge.get("group", ""))
        value = edge.get("value")
        action_text = quoted_action(items, action) if action else "interact"
        lines.append(
            f"{value}. {quoted_who(who)}, {action_text}. Sets `{flag}` to `{value}`."
        )
        needs = []
        or_needs = []
        for row in rows:
            if row.get("rel") != "needs":
                continue
            if row.get("flag"):
                dep = f"`{row['flag']}` {row.get('at') or 'set'}"
            elif row.get("item"):
                dep = quoted_item(items, int(row["item"]))
            else:
                continue
            (or_needs if row.get("op") == "or" else needs).append(dep)
        for dep in dict.fromkeys(needs):
            lines.append(f"    - Requires {dep}.")
        if or_needs:
            lines.append(
                "    - Requires one of: " + "; ".join(dict.fromkeys(or_needs)) + "."
            )
        needed_items: list[int] = []
        for row in rows:
            rel = row.get("rel")
            to = str(row.get("to") or "")
            if rel == "needs" and row.get("item"):
                needed_items.append(int(row["item"]))
            if rel == "receives" and to.startswith("item:"):
                item_id = int(to.split(":", 1)[1])
                needed_items.append(item_id)
                lines.append(
                    f"    - Hand in x{row.get('count') or 1}: {quoted_item(items, item_id)}."
                )
            elif rel == "receives" and to.startswith("coin:"):
                lines.append(f"    - Hand in {row.get('count')} {to.split(':', 1)[1]}.")
        for item_id in dict.fromkeys(needed_items):
            for part in cite(item_id):
                lines.append(f"    {part}")
        recipe_id = 0
        if "#recipe:" in source and source.rsplit(":", 1)[-1].isdigit():
            recipe_id = int(source.rsplit(":", 1)[-1])
        if recipe_id:
            spawned = []
            loots_by_npc = defaultdict(list)
            for row in rows:
                if (
                    row.get("rel") == "loots"
                    and row.get("npc")
                    and str(row.get("to") or "").startswith("item:")
                ):
                    loots_by_npc[int(row["npc"])].append(
                        int(str(row["to"]).split(":", 1)[1])
                    )
            for row in rows:
                if row.get("rel") == "spawns":
                    spawned.append(
                        {**row, "loots": loots_by_npc.get(int(row.get("npc") or 0), [])}
                    )
            info = recipe.get(recipe_id) or {}
            spawn_result = not (info.get("products") or info.get("produces"))
            for line in render_recipe(
                recipe_id, 0, set(), spawned if spawn_result else None
            ):
                lines.append("    " + line)
        else:
            ordered = sorted(rows, key=lambda r: int(r.get("order") or 0))
            seen_effects = set()
            for row in ordered:
                rel = row.get("rel")
                to = str(row.get("to") or "")
                ident = (rel, to, row.get("value"), row.get("npc"))
                if ident in seen_effects:
                    continue
                seen_effects.add(ident)
                if rel == "gives" and to.startswith("item:"):
                    item_id = int(to.split(":", 1)[1])
                    if not _recipe_refund(recipe, row, item_id):
                        lines.append(f"    - Gives {quoted_item(items, item_id)}.")
                elif rel == "spawns":
                    lines.append(
                        f"    - Spawns {row.get('name') or to} ({row.get('npc')})."
                    )
                elif rel == "grounds" and to.startswith("item:"):
                    lines.append(
                        f"    - Ground spawn {quoted_item(items, int(to.split(':', 1)[1]))}."
                    )
                elif rel == "sets" and row.get("flag") != flag:
                    lines.append(f"    - Sets `{row['flag']}` to `{row.get('value')}`.")
        if verbose:
            lines.extend(dialogue_lines(who, "    "))
        lines.append("")
        for sub in dict.fromkeys(
            row.get("flag")
            for row in rows
            if row.get("rel") == "needs" and row.get("flag") and row.get("flag") != flag
        ):
            if sub in seen_flags:
                lines.append(f"    - Subquest `{sub}` documented earlier.")
            else:
                lines.append(f"    - Subquest `{sub}`:")
                render_flag(sub, min(level + 1, 5))

    def render_extras(
        flag: str, used: set, level: int, lo: int | None = None, hi: int | None = None
    ) -> None:
        found: dict[str, dict] = {}
        for edge in by_from_needs(flag):
            if not _at_fits(edge.get("at"), lo, hi):
                continue
            source = edge.get("group") or edge.get("from")
            if not source or source in used:
                continue
            rows = bundle(
                by_from, by_group, edge.get("from", ""), edge.get("group", "")
            )
            if not any(
                row.get("rel") in {"receives", "gives", "spawns", "loots", "grounds"}
                or (row.get("rel") == "sets" and row.get("flag") != flag)
                for row in rows
            ):
                continue
            found.setdefault(str(source), edge)
        if not found:
            return
        lines.append(f"{'#' * min(level, 6)} Steps on `{flag}` that do not change it")
        lines.append("")
        for source, edge in sorted(found.items()):
            who, action, zone = parse_who(
                source if "#" in str(source) else edge.get("from")
            )
            npc = who.split("/", 1)[-1]
            lines.append(
                f"- `{zone}` {npc}"
                + (f", {action}" if action else "")
                + f" needs `{flag}` {edge.get('at')}."
            )
            rows = bundle(
                by_from, by_group, edge.get("from", ""), edge.get("group", "")
            )
            for row in rows:
                if row.get("rel") == "receives" and str(row.get("to", "")).startswith(
                    "item:"
                ):
                    lines.append(
                        f"  - Turn in {item_name(items, int(row['to'].split(':', 1)[1]))}."
                    )
                elif row.get("rel") == "gives" and str(row.get("to", "")).startswith(
                    "item:"
                ):
                    lines.append(
                        f"  - Gives {item_name(items, int(row['to'].split(':', 1)[1]))}."
                    )
                elif row.get("rel") == "spawns":
                    lines.append(
                        f"  - Spawns {row.get('name') or row.get('to')} ({row.get('npc')})."
                    )
                elif row.get("rel") == "loots" and str(row.get("to", "")).startswith(
                    "item:"
                ):
                    lines.append(
                        f"  - Loots {item_name(items, int(row['to'].split(':', 1)[1]))}."
                    )
                elif row.get("rel") == "sets" and row.get("flag") != flag:
                    lines.append(f"  - Sets `{row['flag']}` to `{row.get('value')}`.")
        lines.append("")

    def by_from_needs(flag: str):
        for edge in edges_needing[flag]:
            yield edge

    lines.append(f"# {title}")
    lines.append("")
    lines.append(
        "Acquisition paths traced backwards from the 1.0, 1.5 and 2.0 epic rewards. "
        "Flags are dependencies, not the definition of an epic. "
        "**Broken** indicates missing graph provenance."
    )
    lines.append("")
    roots = EPIC_ITEMS[name]
    for era in ("1.0", "1.5", "2.0"):
        lines.append(f"## Epic {era}")
        lines.append("")
        for item_id in roots[era]:
            lines.append(f"### {quoted_item(items, item_id)}")
            lines.append("")
            # Each reward is independently obtainable; a shared item used in
            # two chains must not be suppressed by the first walkthrough.
            first_seen_item.clear()
            steps: list[str] = []
            forward(item_id, set(), steps, set(), item_id)
            if not (gives.get(item_id) or loots.get(item_id) or produces.get(item_id)):
                lines.append(
                    f"**Broken:** no quest hand-in, encounter or recipe produces "
                    f"{quoted_item(items, item_id)} in the graph. "
                    "Catalog drops/spells below are not proof of the epic quest."
                )
                lines.append("")
            if not steps:
                lines.append(f"**Broken:** no acquisition path for item {item_id}.")
            for number, step in enumerate(steps, 1):
                lines.append(f"{number}. {step}")
                if verbose:
                    # Preserve the dialogue detail previously shown for
                    # flag-rooted steps without making flags the entrypoints.
                    match = re.match(
                        r'([^\s/]+)/(?:(?:"([^"]+)")|([^,]+)),\s*(?:say|hand)\b',
                        step,
                    )
                    if match:
                        zone, quoted_npc, plain_npc = match.groups()
                        npc = (quoted_npc or plain_npc).strip().lower().replace(" ", "_")
                        lines.extend(dialogue_lines(f"{zone}/{npc}", "    "))
            lines.append("")

    # Retain the full state-machine walkthrough as supporting evidence. Some
    # older scripts gate encounters through globals without a causal edge
    # from the resulting loot back to that global. Removing this view would
    # regress the complete Ranger 1.5/2.0 progression while those edges are
    # still absent from the graph.
    lines.append("## Quest-state progression")
    lines.append("")
    mains = sorted(mains, key=_era_rank)
    state_at = len(lines)
    for entry in mains:
        flag, lo, hi, era = _section(entry)
        render_flag(flag, 3, lo, hi, era)
    if prereq_ids:
        lines[state_at:state_at] = render_prereqs()
    side_flags = {_section(entry)[0] for entry in mains}
    sides = sorted(
        flag for flag in flags if flag not in side_flags and flag not in seen_flags
    )
    if sides:
        lines.append("### Other flags touched along the way")
        lines.append("")
        for flag in sides:
            brief = sorted({str(edge.get("value")) for edge in sets_of.get(flag, ())})
            where = sorted(
                {parse_who(edge.get("from"))[0] for edge in sets_of.get(flag, ())}
            )
            lines.append(
                f"- `{flag}` set to {', '.join(brief) or 'nothing'} at {', '.join(where[:4])}."
            )
        lines.append("")
    path = OUT / f"{name}.md"
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return path, len(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Generate epic quest walkthroughs")
    parser.add_argument(
        "-c",
        "--class",
        dest="class_name",
        metavar="CLASS",
        help="Generate only the named class (e.g. ranger)",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Inline full NPC dialogue chains and guards",
    )
    parser.add_argument("--graph", type=Path, default=None)
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args(argv)
    global GRAPH, OUT
    GRAPH = args.graph or GRAPH
    OUT = args.out or OUT
    choices = [
        row
        for row in CLASSES
        if not args.class_name
        or row[0].casefold() == args.class_name.casefold()
        or row[1].casefold() == args.class_name.casefold()
    ]
    if not choices:
        parser.error(
            f"Unknown class {args.class_name!r}; choose from: "
            + ", ".join(row[0] for row in CLASSES)
        )
    items, edges, says, world, dialogues = load()
    by_from, by_group, sets_of, gives, loots, grounds, produces, recipe = indexes(
        edges, world
    )
    global edges_needing
    edges_needing = defaultdict(list)
    for edge in edges:
        if edge.get("rel") == "needs" and edge.get("flag"):
            edges_needing[edge["flag"]].append(edge)
    ctx = (
        items,
        says,
        by_from,
        by_group,
        sets_of,
        gives,
        loots,
        grounds,
        produces,
        recipe,
        dialogues,
    )
    OUT.mkdir(parents=True, exist_ok=True)
    for slug, title, mains, prefixes in choices:
        path, count = write_class(
            slug, title, mains, prefixes, ctx, verbose=args.verbose
        )
        print(f"{path.name} {count} lines")


if __name__ == "__main__":
    main()
