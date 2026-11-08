"""Write one markdown file per class from the quest graph only."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

GRAPH = Path.home() / ".eqclient" / "quest_graph.jsonl"
OUT = Path("/Users/samo/work/EQEmu/.epics")

# Main flags in the order a character meets them. A 2.0 flag is the one the
# graph actually names with 20. Where 1.5 and 2.0 share one flag, the values
# stay in one section and the gaps are marked.
CLASSES = [
    ("warrior", "Warrior", ["warrior_pre", "warrior_epic"], ("warr_epic", "warrior_epic_")),
    ("cleric", "Cleric", ["cleric15pre", "cleric_epic", "cleric20"], ("cleric20_", "cleric_epic_")),
    ("paladin", "Paladin", ["paladin_epic"], ("paladin_epic_",)),
    # ranger_epic through 7 is the 1.5 chain. Value 8 is where the scripts say 2.0 starts.
    ("ranger", "Ranger", [("ranger_epic", None, 8, None), "ranger_epic15_pre", ("ranger_epic", 8, None, "2.0")], ("ranger_epic_",)),
    ("shadowknight", "Shadow Knight", ["shadowknight_pre", "shadowknight_epic"], ("sk_",)),
    ("druid", "Druid", ["druid_epic"], ("druid_epic_",)),
    ("monk", "Monk", ["MnkPre", "monk_epic", "mnk_epic20"], ("monk_epic_",)),
    ("bard", "Bard", ["bardPQ", "bard15", "Fatestealer_bard", "bard20"], ("bard15_", "bard20_")),
    ("rogue", "Rogue", ["roguepre"], ("rogue_epic_", "rogue_")),
    ("shaman", "Shaman", ["shaman_pre", "shaman_epic"], ("shaman_epic_",)),
    ("necromancer", "Necromancer", ["NecroPre", "necro_epic"], ("nec_epic_",)),
    (
        "wizard",
        "Wizard",
        ["wiz_epic_pre", "wizepic", "wizepicA", "wizepicB", "wizepicK", "wiz_epic", "wiz_epic20"],
        ("wiz20_", "wiz_epic_s", "wiz_epic_w"),
    ),
    ("magician", "Magician", ["mage_epic"], ("mage_epic_",)),
    ("enchanter", "Enchanter", ["EnchPre", "ench_epic"], ("ench_epic_",)),
    ("beastlord", "Beastlord", ["bstepic", "beast_epic"], ("beast_epic_", "bst_")),
    ("berserker", "Berserker", ["berserk_epic"], ("ber_epic_", "berserk_epic_")),
]


def load():
    items: dict[int, dict] = {}
    edges: list[dict] = []
    says: dict[tuple[str, str, str], str] = {}
    world: dict[int, dict] = {}
    for line in GRAPH.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        kind = row.get("kind")
        if kind == "item":
            items[int(row["item"])] = row
        elif kind == "world":
            world[int(row["id"])] = {"name": row.get("name") or "", "zones": list(row.get("zones") or [])}
        elif kind == "edge":
            edges.append(row)
        elif kind == "say":
            says[(str(row.get("zone", "")).lower(), str(row.get("npc", "")).lower(), str(row.get("word", "")).lower())] = (
                row.get("text") or ""
            )
    return items, edges, says, world


def indexes(edges, world):
    by_from = defaultdict(list)
    by_group = defaultdict(list)
    sets_of = defaultdict(list)
    gives = defaultdict(list)
    loots = defaultdict(list)
    grounds = defaultdict(list)
    produces = defaultdict(list)
    recipe = defaultdict(lambda: {"consumes": [], "container": 0, "produces": 0, "products": [], "world": None})
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
            for key in ("skill", "skill_name", "skillneeded", "trivial", "nofail", "must_learn"):
                if key in edge:
                    recipe[recipe_id][key] = edge[key]
        if rel == "container" and source.startswith("recipe:") and to.startswith("world:"):
            recipe_id = int(source.split(":", 1)[1])
            type_id = int(to.split(":", 1)[1])
            station = world.get(type_id) or {"name": f"world container {type_id}", "zones": []}
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
    spells = sorted((source.split(":", 1)[1] for source in sources if source.startswith("spell:")), key=len)
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
    act = act.split("#holds:")[0]
    if act.startswith("hand:"):
        act = "hand " + act[5:]
    elif act in {"enter", "loot", "kill"} or act.startswith("event_"):
        act = f"on {act}"
    else:
        act = f"say {act}"
    return who, act, who.split("/", 1)[0]


def bundle(by_from, by_group, source: str, group: str) -> list[dict]:
    rows = []
    seen = set()
    for key in (source, group):
        if not key:
            continue
        for edge in by_from.get(key, []) + by_group.get(key, []):
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
        parts.append((row.get("rel"), source, row.get("to"), row.get("at"), row.get("value"), row.get("op"), row.get("flag")))
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
    if era or "20" in name:
        rank = 2
    elif "15" in name:
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
    for row in by_from.get(group, []) + by_from.get(edge.get("from"), []) + by_group.get(group, []):
        if row.get("rel") == "needs" and row.get("flag") in flags:
            return True
    return False


def write_class(name, title, mains, prefixes, ctx):
    items, says, by_from, by_group, sets_of, gives, loots, grounds, produces, recipe = ctx
    flags = class_flags(sets_of, mains, prefixes)
    lines: list[str] = []
    seen_flags: set[str] = set()
    seen_recipes: set[int] = set()

    def handed(edge: dict) -> list[int]:
        source = str(edge.get("group") or edge.get("from") or "")
        found: list[int] = []
        for row in by_group.get(source, []) + by_from.get(source, []):
            if row.get("rel") != "receives" or not str(row.get("to", "")).startswith("item:"):
                continue
            needed = int(row["to"].split(":", 1)[1])
            if needed not in found:
                found.append(needed)
        return found

    prereq_ids: list[int] = []

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
            return linked
        if len(made) <= 2:
            return made
        return []

    def real_givers(item_id: int) -> list[dict]:
        givers = [
            edge
            for edge in gives.get(item_id, [])
            if not _recipe_refund(recipe, edge, item_id) and item_id not in handed(edge)
        ]
        gated = [edge for edge in givers if prefers(by_from, by_group, edge, flags)]
        return (gated or givers)[:6]

    def note_prereq(item_id: int) -> None:
        if item_id and item_id not in prereq_ids:
            prereq_ids.append(int(item_id))

    def is_chain(item_id: int) -> bool:
        """A multi-step questline: a combine, or an NPC who needs item turn-ins."""
        if creating(item_id):
            return True
        if any("#timer:" in str(edge.get("from") or "") for edge in loots.get(item_id, [])):
            return True
        return any(
            handed(edge) or any(
                row.get("rel") == "needs" and (row.get("flag") or row.get("item"))
                for row in bundle(by_from, by_group, edge.get("from", ""), edge.get("group", ""))
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
                if row.get("rel") == "receives" and str(row.get("to", "")).startswith("item:"):
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
        """Follow triggers backward from a timer to its initiating hand-in.

        The graph stores `source -> event` triggers. Render prerequisites in
        execution order; use the caller's item traversal for hand-in inputs.
        """
        if source in visiting:
            return [f"**Broken:** cyclic event trigger at `{source}`."]

        incoming = [
            edge
            for rows in by_from.values()
            for edge in rows
            if edge.get("rel") == "triggers" and edge.get("to") == source
        ]
        if not incoming:
            return [f"**Broken:** no event trigger found for `{source}`."]

        # More than one incoming trigger denotes alternative ways to reach an
        # event, not a requirement to perform every trigger.
        edge = sorted(incoming, key=lambda row: str(row.get("from", "")))[0]
        parent = str(edge["from"])
        active = visiting | {source}

        if "#signal:" in parent or "#timer:" in parent:
            return event_chain(parent, expand_item, active) + [
                f"Trigger `{source}` from `{parent}`."
            ]

        who, action, _zone = parse_who(parent)
        steps: list[str] = []
        requirements = handed({"from": parent, "group": parent})
        for needed in requirements:
            if expand_item is not None:
                expand_item(needed)
            else:
                steps.append(f"Acquire {quoted_item(items, needed)}.")

        description = quoted_who(who)
        if action:
            description += f", {quoted_action(items, action)}"
        steps.append(f"{description}. Triggers `{source}`.")
        return steps

    def leaf_bits(item_id: int, expand_item=None) -> list[str]:
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
        gated_loot = [edge for edge in loot_rows if prefers(by_from, by_group, edge, flags)]
        for edge in (gated_loot or loot_rows)[:4]:
            source = str(edge.get("from") or "")
            who, action, zone = parse_who(source)
            spawn = str(edge.get("name") or "")
            if edge.get("npc") and not spawn:
                for row in by_group.get(source, []) + by_from.get(source, []):
                    if row.get("rel") == "spawns" and row.get("npc") == edge.get("npc") and row.get("name"):
                        spawn = str(row["name"])
                        break
            corpse = quoted(spawn) if spawn else (f"npc {edge['npc']}" if edge.get("npc") else "")
            npc_id = edge.get("npc")
            parts = []
            if "#timer:" in source:
                bits.extend(event_chain(source, expand_item))
                bits.append(f"Spawns {corpse} ({npc_id}) after `{source}`.")
                bits.append(f"Loot {quoted_item(items, item_id)} from {corpse}.")
            elif action.startswith("hand ") and corpse:
                for bit in action[5:].split("+"):
                    if bit.isdigit():
                        bits.extend(simple_acquire(int(bit)))
                parts.append(f"Hand {quoted_action(items, action)[5:]} to {quoted_who(who)}.")
                parts.append(f"Spawns {corpse}" + (f" ({npc_id})" if npc_id else "") + ".")
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
                bits.append(f'{quoted_action(items, action).replace("say ", "Say ", 1)} to {quoted_who(who)}.')
                bits.append(f"Spawns {corpse}" + (f" ({npc_id})" if npc_id else "") + ".")
                bits.append(f"Loot {quoted_item(items, item_id)} from {corpse}.")
            elif corpse:
                where = f" at {quoted_who(who)}" + (f", {quoted_action(items, action)}" if action else "")
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
        if len(loot_rows) > 4 and not gated_loot:
            bits.append(f"{len(loot_rows) - 4} other loot steps also yield {item_name(items, item_id)}.")
        for edge in grounds.get(item_id, [])[:3]:
            bits.append(
                f"Ground spawn of {quoted_item(items, item_id)} in `{edge.get('zone') or 'an unstated zone'}`."
            )
        for line in _made_by(items, item_id):
            bits.append(line[2:] if line.startswith("- ") else line)
        made = creating(item_id)
        if not made:
            made = [
                rid
                for rid in produces.get(item_id, [])
                if item_id not in recipe_inputs(rid)
            ][:2]
        for rid in made[:2]:
            bits.append(recipe_sentence(rid))
        if len(produces.get(item_id, [])) > 2 and made:
            extra = len([rid for rid in produces[item_id] if item_id not in recipe_inputs(rid)]) - len(made[:2])
            if extra > 0:
                bits.append(f"{extra} other recipes also produce {item_name(items, item_id)}.")
        if bits:
            return bits
        # Duplicate epic reward ids (Spear of Fate 10651 vs 36223). Prefer the id a script gives.
        alias = _ITEM_ALIAS.get(int(item_id))
        if alias and alias != item_id:
            bits = leaf_bits(alias)
            if bits and not bits[0].startswith("**Broken:**"):
                return [f"Same item as {quoted_item(items, alias)}."] + bits
        zones = (items.get(item_id) or {}).get("zones") or []
        if zones:
            if len(zones) > 3:
                return [f"Common item: {item_name(items, item_id)}. Listed in {len(zones)} zones."]
            shown = ", ".join(zones)
            return [f"No quest step gives {item_name(items, item_id)}. The dump lists it in {shown}."]
        return [f"**Broken:** nothing in the graph gives, loots, spawns, or combines {item_name(items, item_id)}."]

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
        puts = ", ".join(quoted_item(items, comp) for comp, _count in info.get("consumes") or [])
        products = list(info.get("products") or [])
        if not products and info.get("produces"):
            products = [(info["produces"], 1)]
        inputs = recipe_inputs(recipe_id)
        handed_back = [quoted_item(items, comp) for comp, _count in products if comp in inputs]
        fresh = [quoted_item(items, comp) + (f" x{count}" if count > 1 else "") for comp, count in products if comp not in inputs]
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

        return list(dict.fromkeys(
            f"Requires `{row['flag']}` {row.get('at') or 'set'}"
            for row in rows
            if row.get("rel") == "needs" and row.get("flag")
        ))

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
        if item_id in trail or item_id in seen:
            return

        seen.add(item_id)
        trail = trail | {item_id}

        def dependencies(edge: dict) -> list[dict]:
            return [
                row
                for row in bundle(
                    by_from,
                    by_group,
                    edge.get("from", ""),
                    edge.get("group", ""),
                )
                if row.get("rel") == "needs"
            ]

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

        def expand_flag(flag: str, at: str) -> None:
            key = ("flag", flag, at)

            if key in seen:
                return

            if flag in flag_trail:
                steps.append(f"Unresolved cyclic prerequisite: `{flag}` {at}.")
                return

            seen.add(key)

            if at == "unset":
                steps.append(
                    f"Requires `{flag}` unset; no setter establishes this state."
                )
                return

            setters = [
                edge
                for edge in sets_of.get(flag, [])
                if value_matches(str(edge.get("value", "")), at)
            ]

            if not setters:
                steps.append(
                    f"Unresolved prerequisite: `{flag}` {at}; "
                    "no matching setter in graph."
                )
                return

            # Favor direct, inexpensive prerequisites over long hand-in chains.
            setters.sort(
                key=lambda edge: (
                    len(handed(edge)),
                    str(edge.get("from", "")),
                )
            )

            setter = setters[0]
            source = str(setter.get("group") or setter.get("from") or "")
            setter_key = ("setter", source, flag, at)

            if setter_key in seen:
                return

            next_flags = flag_trail | {flag}

            # Resolve prerequisites of the action that sets this flag.
            for row in dependencies(setter):
                if row.get("flag"):
                    forward_flag = row["flag"]
                    if forward_flag in next_flags:
                        continue

                    # Recursive flag dependencies use the extended traversal state.
                    previous = flag_trail
                    flag_trail_holder[0] = next_flags
                    try:
                        resolve_flag(
                            forward_flag,
                            str(row.get("at") or "set"),
                            next_flags,
                        )
                    finally:
                        flag_trail_holder[0] = previous

                elif row.get("item"):
                    expand_item(int(row["item"]))

            # Acquire items that must be handed in to establish the flag.
            for needed in handed(setter):
                expand_item(needed)

            if setter_key not in seen:
                seen.add(setter_key)
                who, action, _zone = parse_who(source)
                description = quoted_who(who)

                if action:
                    description += f", {quoted_action(items, action)}"

                steps.append(
                    f"{description}. "
                    f"Sets `{flag}` to `{setter.get('value')}`."
                )

        # Explicit flag recursion avoids confusing item and flag cycle detection.
        flag_trail_holder = [flag_trail]

        def resolve_flag(
            flag: str,
            at: str,
            active: frozenset[str],
        ) -> None:
            if flag in active:
                return
            forward_flag_dependency(flag, at, active)

        def forward_flag_dependency(
            flag: str,
            at: str,
            active: frozenset[str],
        ) -> None:
            # Re-enter the normal dependency resolver with the current flag path.
            nonlocal flag_trail
            previous = flag_trail
            flag_trail = active
            try:
                expand_flag(flag, at)
            finally:
                flag_trail = previous

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

            # Alternative requirements are not all mandatory.
            alternatives = [
                row for row in requirements if row.get("op") == "or"
            ]
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

        for rid in creating(item_id):
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

        for bit in leaf_bits(item_id, expand_item=expand_item):
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
            "Each list is the order you obtain that item. Later steps point here instead of repeating the chain.",
            "",
        ]
        for item_id in list(prereq_ids):
            block.append(f"### {quoted_item(items, item_id)}")
            block.append("")
            steps: list[str] = []
            forward(item_id, set(), steps, set(), item_id)
            name = quoted_item(items, item_id)
            kept: list[str] = []
            for text in steps:
                kept.append(text)
                produced = text.split("Produces ", 1)[-1] if "Produces " in text else ""
                if f"Gives {name}." in text or (name in produced and "no new item" not in produced):
                    break
            steps = kept
            if not steps:
                block.append("The graph has no earlier step for this.")
            for number, text in enumerate(steps, 1):
                block.append(f"{number}. {text}")
            block.append("")
        return block

    def sets_of_flat(flag_set):
        for flag in flag_set:
            yield from sets_of.get(flag, ())

    def render_recipe(recipe_id: int, depth: int, trail: set[int], spawns: list[dict] | None = None) -> list[str]:
        info = recipe[recipe_id]
        if not info["produces"] and not info["consumes"] and not info["container"] and not info.get("products"):
            return [f"- **Broken:** `recipe:{recipe_id}` is named and has no components in the graph."]
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
            out.append(f"{pad}- `recipe:{recipe_id}` is combined in {world['name']} ({world['id']}). A container in the world.{where}")
        elif info["container"]:
            out.append(f"{pad}- `recipe:{recipe_id}` is combined in {item_name(items, info['container'])}.")
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
            handed_back = [item_name(items, comp) for comp, _count in products if comp in inputs]
            fresh = [
                item_name(items, comp) + (f" x{count}" if count > 1 else "")
                for comp, count in products
                if comp not in inputs
            ]
            if handed_back:
                out.append(f"{pad}  - Hands back {', '.join(handed_back)}.")
            out.append(f"{pad}  - Produces {', '.join(fresh) if fresh else 'no new item'}.")
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

    def render_flag(flag: str, level: int, lo: int | None = None, hi: int | None = None, era: str | None = None) -> None:
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
        numeric = sorted({int(edge["value"]) for edge in sets if str(edge.get("value", "")).isdigit()})
        if numeric:
            lines.append(f"Values written: {', '.join(str(number) for number in numeric)}.")
            lines.append("")
        odd = sorted({str(edge.get("value")) for edge in sets if not str(edge.get("value", "")).isdigit()})
        if odd:
            lines.append("**Broken:** these writes are not a plain number, so they cannot be ordered: " + ", ".join(f"`{value}`" for value in odd) + ".")
            lines.append("")
        groups: dict[tuple, list] = {}
        for edge in sets:
            key = (str(edge.get("value")), signature(by_from, by_group, edge))
            groups.setdefault(key, []).append(edge)
        ordered = sorted(groups.values(), key=lambda group: (not str(group[0].get("value", "")).isdigit(), int(group[0]["value"]) if str(group[0].get("value", "")).isdigit() else 0, str(group[0].get("from"))))
        used = set()
        for group in ordered:
            render_step(group, level + 1, flag)
            for edge in group:
                used.add(edge.get("from"))
                if edge.get("group"):
                    used.add(edge.get("group"))
        render_extras(flag, used, level + 1, lo, hi)

    def render_step(group: list[dict], level: int, flag: str) -> None:
        edge = group[0]
        zones = []
        for one in group:
            who, _action, zone = parse_who(one.get("from"))
            if zone and zone not in zones:
                zones.append(zone)
        who, action, _zone = parse_who(edge.get("from"))
        npc = who.split("/", 1)[-1]
        title = npc
        if action:
            title += f" — {action}"
        lines.append(f"{'#' * min(level, 6)} {edge.get('value')}. {title}")
        lines.append("")
        if len(zones) > 1:
            lines.append("Zones: " + ", ".join(f"`{zone}`" for zone in zones) + ".")
        else:
            lines.append(f"Zone: `{zones[0] if zones else who}`.")
        lines.append("")
        spoken = quote_for(says, who, action)
        if spoken:
            lines.append(f"> {spoken}")
            lines.append("")
        rows = bundle(by_from, by_group, edge.get("from", ""), edge.get("group", ""))
        lines.append(f"Sets `{flag}` to `{edge.get('value')}`.")
        lines.append("")
        ors = []
        for row in rows:
            if row.get("rel") != "needs":
                continue
            if row.get("flag"):
                text = f"`{row['flag']}` {row.get('at')}"
            elif row.get("item"):
                text = item_name(items, row["item"])
            elif str(row.get("to", "")).startswith("coin:"):
                text = str(row["to"])
            else:
                continue
            if row.get("op") == "or":
                ors.append(text)
            else:
                lines.append(f"- Needs {text}.")
        if ors:
            lines.append("- One of: " + "; ".join(ors) + ".")
        for row in rows:
            if row.get("rel") == "receives" and str(row.get("to", "")).startswith("item:"):
                count = row.get("count") or 1
                lines.append(f"- Turn in x{count}: {item_name(items, int(row['to'].split(':', 1)[1]))}.")
            elif row.get("rel") == "receives" and str(row.get("to", "")).startswith("coin:"):
                lines.append(f"- Turn in {row.get('count')} {row['to'].split(':', 1)[1]}.")
        recipe_id = 0
        source = str(edge.get("from") or "")
        if "#recipe:" in source and source.rsplit(":", 1)[-1].isdigit():
            recipe_id = int(source.rsplit(":", 1)[-1])
        recipe_info = recipe.get(recipe_id) if recipe_id else None
        spawn_is_result = bool(recipe_info) and not (recipe_info.get("products") or recipe_info.get("produces"))
        actions = []
        for row in rows:
            if row.get("rel") == "gives" and str(row.get("to", "")).startswith("item:"):
                if _recipe_refund(recipe, row, int(row["to"].split(":", 1)[1])):
                    continue
            if row.get("rel") == "spawns" and spawn_is_result:
                continue
            if row.get("rel") in {"gives", "spawns", "grounds", "sets"} or (row.get("rel") == "loots" and not row.get("npc")):
                actions.append(row)
        actions.sort(key=lambda row: (0, int(row["order"])) if "order" in row else (1, 0))
        loots_of: dict[int, list] = defaultdict(list)
        for row in rows:
            if row.get("rel") == "loots" and row.get("npc") and str(row.get("to", "")).startswith("item:"):
                loots_of[int(row["npc"])].append(row)
        if actions:
            lines.append("In script order:")
            lines.append("")
        seen_action = set()
        number = 0
        for row in actions:
            ident = (row.get("rel"), row.get("to"), row.get("flag"), row.get("value"), row.get("npc"))
            if ident in seen_action:
                continue
            seen_action.add(ident)
            if row.get("rel") == "gives" and str(row.get("to", "")).startswith("item:"):
                text = f"Gives {item_name(items, int(row['to'].split(':', 1)[1]))}."
            elif row.get("rel") == "spawns":
                label = row.get("name") or row.get("to")
                text = f"Spawns {label} ({row.get('npc')})."
            elif row.get("rel") == "grounds":
                text = f"Ground spawn {item_name(items, int(row['to'].split(':', 1)[1]))}."
            elif row.get("rel") == "sets" and row.get("flag"):
                text = f"Sets `{row['flag']}` to `{row.get('value')}`."
            elif row.get("rel") == "loots":
                text = f"Loots {item_name(items, int(row['to'].split(':', 1)[1]))}."
            else:
                continue
            number += 1
            lines.append(f"{number}. {text}")
            if row.get("rel") == "spawns" and row.get("npc"):
                for loot in loots_of.get(int(row["npc"]), []):
                    lines.append(f"   - Loots {item_name(items, int(loot['to'].split(':', 1)[1]))}.")
        if actions:
            lines.append("")
        lines.append("")
        if recipe_id:
            spawned = []
            for row in rows:
                if row.get("rel") != "spawns":
                    continue
                loots = [
                    int(loot["to"].split(":", 1)[1])
                    for loot in loots_of.get(int(row["npc"]), [])
                    if str(loot.get("to", "")).startswith("item:")
                ] if row.get("npc") else []
                spawned.append({**row, "loots": loots})
            lines.append("Combine:")
            lines.append("")
            lines.extend(render_recipe(recipe_id, 0, set(), spawned if spawn_is_result else None))
            lines.append("")
        needed_items = []
        needed_flags = []
        for row in rows:
            if row.get("rel") != "needs":
                continue
            if row.get("item"):
                needed_items.append(int(row["item"]))
            if row.get("flag") and row.get("flag") != flag:
                needed_flags.append(row["flag"])
        for row in rows:
            if row.get("rel") == "receives" and str(row.get("to", "")).startswith("item:"):
                needed_items.append(int(row["to"].split(":", 1)[1]))
        shown_items = []
        for item_id in needed_items:
            if item_id not in shown_items:
                shown_items.append(item_id)
        if shown_items:
            lines.append("How the items are reached:")
            lines.append("")
            for item_id in shown_items:
                lines.append(f"- {item_name(items, item_id)}")
                for bit in cite(item_id):
                    lines.append(f"  {bit}")
            lines.append("")
        shown_sub = []
        for sub in needed_flags:
            if sub not in shown_sub:
                shown_sub.append(sub)
        for sub in shown_sub:
            if sub in seen_flags:
                lines.append(f"This step also depends on `{sub}`, shown above.")
                lines.append("")
                continue
            lines.append(f"Subquest `{sub}`:")
            lines.append("")
            render_flag(sub, level + 1)

    def render_extras(flag: str, used: set, level: int, lo: int | None = None, hi: int | None = None) -> None:
        found: dict[str, dict] = {}
        for edge in by_from_needs(flag):
            if not _at_fits(edge.get("at"), lo, hi):
                continue
            source = edge.get("group") or edge.get("from")
            if not source or source in used:
                continue
            rows = bundle(by_from, by_group, edge.get("from", ""), edge.get("group", ""))
            if not any(row.get("rel") in {"receives", "gives", "spawns", "loots", "grounds"} or (row.get("rel") == "sets" and row.get("flag") != flag) for row in rows):
                continue
            found.setdefault(str(source), edge)
        if not found:
            return
        lines.append(f"{'#' * min(level, 6)} Steps on `{flag}` that do not change it")
        lines.append("")
        for source, edge in sorted(found.items()):
            who, action, zone = parse_who(source if "#" in str(source) else edge.get("from"))
            npc = who.split("/", 1)[-1]
            lines.append(f"- `{zone}` {npc}" + (f", {action}" if action else "") + f" needs `{flag}` {edge.get('at')}.")
            rows = bundle(by_from, by_group, edge.get("from", ""), edge.get("group", ""))
            for row in rows:
                if row.get("rel") == "receives" and str(row.get("to", "")).startswith("item:"):
                    lines.append(f"  - Turn in {item_name(items, int(row['to'].split(':', 1)[1]))}.")
                elif row.get("rel") == "gives" and str(row.get("to", "")).startswith("item:"):
                    lines.append(f"  - Gives {item_name(items, int(row['to'].split(':', 1)[1]))}.")
                elif row.get("rel") == "spawns":
                    lines.append(f"  - Spawns {row.get('name') or row.get('to')} ({row.get('npc')}).")
                elif row.get("rel") == "loots" and str(row.get("to", "")).startswith("item:"):
                    lines.append(f"  - Loots {item_name(items, int(row['to'].split(':', 1)[1]))}.")
                elif row.get("rel") == "sets" and row.get("flag") != flag:
                    lines.append(f"  - Sets `{row['flag']}` to `{row.get('value')}`.")
        lines.append("")

    def by_from_needs(flag: str):
        for edge in edges_needing[flag]:
            yield edge

    mains = sorted(mains, key=_era_rank)
    lines.append(f"# {title}")
    lines.append("")
    lines.append("Steps taken from the quest graph only. **Broken** means the graph has no edge for that value or that item.")
    lines.append("")
    main_flags = [_section(entry)[0] for entry in mains]
    present = []
    for flag in main_flags:
        if sets_of.get(flag) and flag not in present:
            present.append(flag)
    missing = [flag for flag in main_flags if not sets_of.get(flag)]
    lines.append("Flags with writes: " + (", ".join(f"`{flag}`" for flag in present) if present else "none") + ".")
    if missing:
        lines.append("")
        lines.append("**Broken:** these flags were expected for this class and nothing sets them: " + ", ".join(f"`{flag}`" for flag in missing) + ".")
    lines.append("")
    body_at = len(lines)
    for entry in mains:
        flag, lo, hi, era = _section(entry)
        render_flag(flag, 2, lo, hi, era)
    if prereq_ids:
        lines[body_at:body_at] = render_prereqs()
    side_flags = { _section(entry)[0] for entry in mains }
    sides = sorted(flag for flag in flags if flag not in side_flags and flag not in seen_flags)
    if sides:
        lines.append("## Other flags touched along the way")
        lines.append("")
        for flag in sides:
            brief = sorted({str(edge.get("value")) for edge in sets_of.get(flag, ())})
            where = sorted({parse_who(edge.get("from"))[0] for edge in sets_of.get(flag, ())})
            lines.append(f"- `{flag}` set to {', '.join(brief) or 'nothing'} at {', '.join(where[:4])}.")
        lines.append("")
    path = OUT / f"{name}.md"
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return path, len(lines)


def main():
    items, edges, says, world = load()
    by_from, by_group, sets_of, gives, loots, grounds, produces, recipe = indexes(edges, world)
    global edges_needing
    edges_needing = defaultdict(list)
    for edge in edges:
        if edge.get("rel") == "needs" and edge.get("flag"):
            edges_needing[edge["flag"]].append(edge)
    ctx = (items, says, by_from, by_group, sets_of, gives, loots, grounds, produces, recipe)
    OUT.mkdir(parents=True, exist_ok=True)
    for slug, title, mains, prefixes in CLASSES:
        path, count = write_class(slug, title, mains, prefixes, ctx)
        print(f"{path.name} {count} lines")


if __name__ == "__main__":
    main()
