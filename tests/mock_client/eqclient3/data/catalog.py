"""Item names and the zones they come from, read from a local peq dump.

No live query. A name in an NPC's speech is looked up here, and a loot,
merchant, or ground spawn supplies the zone.
"""

from __future__ import annotations

import os
import re
from collections import defaultdict
from pathlib import Path

from eqclient3.log import log


class Catalog:
    def __init__(self) -> None:
        self.names: dict[str, list[int]] = {}
        self.labels: dict[int, str] = {}
        self.zones: dict[int, tuple[str, ...]] = {}
        self.item_classes: dict[int, tuple[int, ...]] = {}
        self.item_races: dict[int, tuple[int, ...]] = {}
        # recipe id -> components (item, count), the container it is made in, and the result.
        self.recipes: dict[int, dict] = {}
        # npc type id -> items on its loot table, including quest-spawned npcs with no spawn2 row.
        self.npc_drops: dict[int, tuple[int, ...]] = {}
        # npc type id -> display name from npc_types.
        self.npc_names: dict[int, str] = {}
        # How an item is created outside a quest script: "spell:Name", "forage:zone", "fishing:zone".
        self.sources: dict[int, tuple[str, ...]] = {}
        # zone.short_name, the row id in column 1, and zoneidnumber in column 13.
        # Ground spawns, forage, and fishing store zoneidnumber, not the row id.
        self.short_names: set[str] = set()
        self.row_ids: dict[int, str] = {}
        self.client_zones: dict[int, str] = {}
        self.duplicate_zone_numbers: dict[int, tuple[str, ...]] = {}
        self.ground_zone_ids: set[int] = set()
        self.forage_zone_ids: set[int] = set()
        self.fishing_zone_ids: set[int] = set()
        self.spawn_zones: set[str] = set()
        # object.type that is a tradeskill bag type. A recipe container id in this
        # map is a station in the world, not an item id.
        self.world_containers: dict[int, dict] = {}


def named_items(text: str, catalog: Catalog) -> list[int]:
    """Item ids whose name is spelled in this sentence. Longer names win."""
    tokens = _WORDS.findall(text)
    used = [False] * len(tokens)
    found: list[int] = []
    seen: set[int] = set()
    for length in range(min(6, len(tokens)), 0, -1):
        for start in range(0, len(tokens) - length + 1):
            if any(used[start : start + length]):
                continue
            chunk = tokens[start : start + length]
            while chunk and chunk[0].lower() in _LEAD:
                chunk = chunk[1:]
            if not chunk:
                continue
            if len(chunk) == 1 and (len(chunk[0]) < 4 or chunk[0].lower() in _SKIP):
                continue
            key = " ".join(word.lower() for word in chunk)
            ids = catalog.names.get(key)
            if not ids:
                continue
            for index in range(start, start + length):
                used[index] = True
            for item_id in ids[:3]:
                if item_id not in seen:
                    seen.add(item_id)
                    found.append(item_id)
    return found


def load_catalog(path: str, quests_root: str | None = None) -> Catalog:
    catalog = Catalog()
    if not path or not Path(path).is_file():
        return catalog
    with open(path, encoding="latin1", errors="replace") as handle:
        return catalog_from_lines(handle, catalog, quests_root=quests_root)


def catalog_from_lines(lines, catalog: Catalog | None = None, quests_root: str | None = None) -> Catalog:
    """One pass over INSERT lines. Item names, then where those items are found."""
    catalog = catalog or Catalog()
    mode = ""
    drops: dict[int, set[int]] = defaultdict(set)
    tables: dict[int, set[int]] = defaultdict(set)
    npc_loot: dict[int, int] = {}
    npc_merchant: dict[int, int] = {}
    merchant_items: dict[int, set[int]] = defaultdict(set)
    npc_groups: dict[int, set[int]] = defaultdict(set)
    group_zones: dict[int, set[str]] = defaultdict(set)
    ground: dict[int, set[int]] = defaultdict(set)
    forage: dict[int, set[int]] = defaultdict(set)
    fishing: dict[int, set[int]] = defaultdict(set)
    spells: dict[int, set[str]] = defaultdict(set)
    zone_names: dict[int, str] = {}
    recipes: dict[int, dict] = {}
    recipe_skill: dict[int, dict] = {}
    placed: dict[int, set[int]] = defaultdict(set)
    titles: dict[int, set[str]] = defaultdict(set)
    for raw in lines:
        line = raw.strip()
        if line.startswith("INSERT INTO `"):
            mode = _table(line)
            continue
        if not line.startswith("("):
            continue
        if mode == "items":
            _take_item(line, catalog)
        elif mode == "lootdrop_entries":
            fields = _tuple(line)
            if len(fields) >= 2 and fields[0].isdigit() and fields[1].lstrip("-").isdigit():
                drops[int(fields[0])].add(int(fields[1]))
        elif mode == "loottable_entries":
            fields = _tuple(line)
            if len(fields) >= 2 and fields[0].isdigit() and fields[1].isdigit():
                tables[int(fields[0])].add(int(fields[1]))
        elif mode == "npc_types":
            fields = _tuple(line)
            if len(fields) > 18 and fields[0].isdigit():
                npc_id = int(fields[0])
                if fields[1]:
                    catalog.npc_names[npc_id] = fields[1].replace("_", " ").lstrip("#")
                loot = int(fields[17]) if fields[17].isdigit() else 0
                merchant = int(fields[18]) if fields[18].isdigit() else 0
                if loot:
                    npc_loot[npc_id] = loot
                if merchant:
                    npc_merchant[npc_id] = merchant
        elif mode == "merchantlist":
            fields = _tuple(line)
            if len(fields) >= 3 and fields[0].lstrip("-").isdigit() and fields[2].lstrip("-").isdigit():
                merchant_items[int(fields[0])].add(int(fields[2]))
        elif mode == "spawnentry":
            fields = _tuple(line)
            if len(fields) >= 2 and fields[0].isdigit() and fields[1].isdigit():
                npc_groups[int(fields[1])].add(int(fields[0]))
        elif mode == "spawn2":
            fields = _tuple(line)
            if len(fields) >= 3 and fields[1].isdigit() and fields[2]:
                group_zones[int(fields[1])].add(fields[2].lower())
                catalog.spawn_zones.add(fields[2].lower())
        elif mode == "ground_spawns":
            fields = _tuple(line)
            if len(fields) > 10 and fields[1].isdigit() and fields[10].isdigit():
                ground[int(fields[10])].add(int(fields[1]))
        elif mode == "forage":
            _take_gather(line, forage)
        elif mode == "fishing":
            _take_gather(line, fishing)
        elif mode == "spells_new":
            _take_spell(line, spells)
        elif mode == "zone":
            _take_zone(line, zone_names, catalog)
        elif mode == "tradeskill_recipe":
            _take_recipe_skill(line, recipe_skill)
        elif mode == "tradeskill_recipe_entries":
            _take_recipe(line, recipes)
        elif mode == "object":
            _take_object(line, placed, titles)
    catalog.ground_zone_ids = set(zone_id for zones in ground.values() for zone_id in zones)
    catalog.forage_zone_ids = set(zone_id for zones in forage.values() for zone_id in zones)
    catalog.fishing_zone_ids = set(zone_id for zones in fishing.values() for zone_id in zones)
    catalog.zones = _zones(
        drops, tables, npc_loot, npc_merchant, merchant_items, npc_groups, group_zones, ground, zone_names, forage, fishing
    )
    _apply_recipe_skill(recipes, recipe_skill)
    catalog.recipes = recipes
    catalog.npc_drops = _npc_drops(drops, tables, npc_loot)
    _apply_historical_loot(catalog)
    trap_zones = _trap_npc_zones(quests_root)
    catalog.sources = _sources(
        forage,
        fishing,
        spells,
        zone_names,
        ground,
        catalog.npc_drops,
        catalog.npc_names,
        npc_groups,
        group_zones,
        trap_zones,
    )
    catalog.world_containers = _world_containers(placed, titles, zone_names)
    return catalog


# Pre-revamp epic loot missing from the PEQ dump. Matches utils/sql/git/optional/2026_10_26_peq_content_gaps.sql.
# npc id → items. Zones come from spawn2 or trap-script overlays.
_HISTORICAL_LOOT = {
    89000: (14333,),  # Tolapumj → Mistletoe Powder (sebilis)
    72003: (14332,),  # Cazic_Thule → Cazic's Skin (fearplane)
}


_SPAWN2_IDS = re.compile(
    r"(?:quest::spawn2|eq\.spawn2|Spawn2)\s*\(\s*(?:quest::ChooseRandom\s*\(([^)]+)\)|([0-9]+))",
    re.I,
)
_TRAP_SCRIPT = re.compile(r"(?i)(?:^|#|_)trap|a_creature")
_SKIP_QUEST_DIRS = frozenset({"plugins", "lua_modules"})


def _trap_npc_zones(quests_root: str | Path | None = None) -> dict[int, tuple[str, ...]]:
    """npc id → zones for proximity / EVENT_ENTER trap scripts (no spawn2 row in the dump)."""
    root = Path(quests_root if quests_root is not None else os.environ.get("EQEMU_QUESTS", "") or "")
    if not root.is_dir():
        return {}
    found: dict[int, set[str]] = defaultdict(set)
    for path in root.rglob("*"):
        if path.suffix not in {".pl", ".lua"}:
            continue
        if any(part in _SKIP_QUEST_DIRS for part in path.parts):
            continue
        try:
            rel = path.relative_to(root)
        except ValueError:
            log.error("quest path %s is outside %s", path, root, exc_info=True)
            continue
        if len(rel.parts) < 2:
            continue
        zone = rel.parts[0]
        if zone in _SKIP_QUEST_DIRS or zone.startswith("."):
            continue
        try:
            text = path.read_text(encoding="latin1", errors="replace")
        except OSError:
            log.error("quest file %s failed to read", path, exc_info=True)
            continue
        low = text.lower()
        name = path.name
        if not (
            "set_proximity" in low
            or "setproximity" in low
            or "event_enter" in low
            or _TRAP_SCRIPT.search(name)
        ):
            continue
        for match in _SPAWN2_IDS.finditer(text):
            blob = match.group(1) or match.group(2) or ""
            for npc in re.findall(r"\b(\d{4,7})\b", blob):
                found[int(npc)].add(zone)
    return {npc: tuple(sorted(zones)) for npc, zones in found.items()}


def _apply_historical_loot(catalog: Catalog) -> None:
    """Merge restored epic drops into npc_drops and zones until a fresh peq dump includes them."""
    for npc, item_ids in _HISTORICAL_LOOT.items():
        have = set(catalog.npc_drops.get(npc, ()))
        have.update(item_ids)
        catalog.npc_drops[npc] = tuple(sorted(have))
        if npc not in catalog.npc_names:
            continue
    # Zone hints when the NPC has a spawn2 row already reflected in catalog.zones via loot.
    # Tolapumj / Cazic already spawn; inject zone onto the new items.
    zone_for_npc = {
        89000: "sebilis",
        72003: "fearplane",
    }
    zones = dict(catalog.zones)
    for npc, item_ids in _HISTORICAL_LOOT.items():
        zone = zone_for_npc.get(npc)
        if not zone:
            continue
        for item_id in item_ids:
            current = set(zones.get(item_id, ()))
            current.add(zone)
            zones[item_id] = tuple(sorted(current))
    catalog.zones = zones


def _zones(
    drops, tables, npc_loot, npc_merchant, merchant_items, npc_groups, group_zones, ground, zone_names, forage, fishing
) -> dict[int, tuple[str, ...]]:
    drop_tables: dict[int, set[int]] = defaultdict(set)
    for table, drop_ids in tables.items():
        for drop_id in drop_ids:
            drop_tables[drop_id].add(table)
    table_npcs: dict[int, set[int]] = defaultdict(set)
    for npc, table in npc_loot.items():
        table_npcs[table].add(npc)
    merchant_npcs: dict[int, set[int]] = defaultdict(set)
    for npc, merchant in npc_merchant.items():
        merchant_npcs[merchant].add(npc)
    found: dict[int, set[str]] = defaultdict(set)

    def add_npc(item_id: int, npc: int) -> None:
        for group in npc_groups.get(npc, ()):
            found[item_id].update(group_zones.get(group, ()))

    for drop_id, item_ids in drops.items():
        for table in drop_tables.get(drop_id, ()):
            for npc in table_npcs.get(table, ()):
                for item_id in item_ids:
                    add_npc(item_id, npc)
    for merchant, item_ids in merchant_items.items():
        for npc in merchant_npcs.get(merchant, ()):
            for item_id in item_ids:
                add_npc(item_id, npc)
    for item_id, zone_ids in ground.items():
        for zone_id in zone_ids:
            name = zone_names.get(zone_id)
            if name:
                found[item_id].add(name)
    for gathered in (forage, fishing):
        for item_id, zone_ids in gathered.items():
            for zone_id in zone_ids:
                name = zone_names.get(zone_id)
                if name:
                    found[item_id].add(name)
    return {item_id: tuple(sorted(zones)) for item_id, zones in found.items() if zones}


def _take_zone(line: str, client_zones: dict[int, str], catalog: Catalog) -> None:
    """Column 1 is the row id. Column 13 is zoneidnumber, the original client zone id."""
    fields = _tuple(line)
    if len(fields) < 2 or not fields[0] or not fields[1].isdigit():
        return
    short = fields[0].lower()
    catalog.short_names.add(short)
    catalog.row_ids[int(fields[1])] = short
    if len(fields) > 13 and fields[13].lstrip("-").isdigit() and int(fields[13]) > 0:
        number = int(fields[13])
        previous = client_zones.get(number)
        if previous and previous != short:
            known = list(catalog.duplicate_zone_numbers.get(number, (previous,)))
            if short not in known:
                known.append(short)
            catalog.duplicate_zone_numbers[number] = tuple(known)
        else:
            client_zones[number] = short
            catalog.client_zones[number] = short


def _take_gather(line: str, found: dict[int, set[int]]) -> None:
    """A forage or fishing row is (id, zone id, item id, ...)."""
    fields = _tuple(line)
    if len(fields) >= 3 and fields[1].isdigit() and fields[2].isdigit():
        found[int(fields[2])].add(int(fields[1]))


def _take_spell(line: str, found: dict[int, set[str]]) -> None:
    """Effect 32 is Summon Item. Its base value is the item the spell creates."""
    fields = _tuple(line)
    if len(fields) < 98 or not fields[1]:
        return
    for slot in range(12):
        if fields[86 + slot] == "32" and fields[20 + slot].isdigit() and int(fields[20 + slot]) > 0:
            found[int(fields[20 + slot])].add(fields[1])


def audit_zones(catalog: Catalog, quest_dirs: set[str]) -> dict[str, list]:
    """Quest folders against short_name, and client zone ids against zoneidnumber.

    A number that is one zone's row id and another zone's zoneidnumber is not a match.
    Ground spawns, forage, and fishing carry the zoneidnumber.
    """
    skip = {"plugins", "lua_modules"}
    folders = sorted(name.lower() for name in quest_dirs if name.lower() not in skip and not name.startswith("."))
    shorts = catalog.short_names

    def unresolved(zone_ids: set[int]) -> list[tuple[int, str]]:
        found = []
        for zone_id in sorted(zone_ids):
            if zone_id in catalog.client_zones:
                continue
            other = catalog.row_ids.get(zone_id)
            if other:
                found.append((zone_id, f"row id of {other}, not a zoneidnumber"))
            else:
                found.append((zone_id, "no zone row"))
        return found

    collisions = []
    for zone_id, row_name in sorted(catalog.row_ids.items()):
        client_name = catalog.client_zones.get(zone_id)
        if client_name and client_name != row_name:
            collisions.append((zone_id, row_name, client_name))
    return {
        "quest_without_zone": [name for name in folders if name not in shorts],
        "spawn_without_zone": sorted(zone for zone in catalog.spawn_zones if zone not in shorts),
        "ground_unresolved": unresolved(catalog.ground_zone_ids),
        "forage_unresolved": unresolved(catalog.forage_zone_ids),
        "fishing_unresolved": unresolved(catalog.fishing_zone_ids),
        "id_collisions": collisions,
        "duplicate_zone_numbers": sorted(catalog.duplicate_zone_numbers.items()),
    }


def _sources(
    forage,
    fishing,
    spells,
    zone_names,
    ground=None,
    npc_drops=None,
    npc_names=None,
    npc_groups=None,
    group_zones=None,
    trap_zones=None,
) -> dict[int, tuple[str, ...]]:
    """How an item is obtained outside a quest script: spell, forage, fishing, ground, or a rare NPC drop."""
    found: dict[int, set[str]] = defaultdict(set)

    def place(zone_id: int) -> str:
        return zone_names.get(zone_id) or f"zone {zone_id}"

    for item_id, zones in forage.items():
        for zone_id in zones:
            found[item_id].add("forage:" + place(zone_id))
    for item_id, zones in fishing.items():
        for zone_id in zones:
            found[item_id].add("fishing:" + place(zone_id))
    for item_id, names in spells.items():
        for name in names:
            found[item_id].add("spell:" + name)
    for item_id, zone_ids in (ground or {}).items():
        for zone_id in zone_ids:
            found[item_id].add("ground:" + place(zone_id))
    # World NPCs that are not quest-spawned. Skip trash that hundreds of NPCs drop.
    by_item: dict[int, list[tuple[int, str, tuple[str, ...]]]] = defaultdict(list)
    names = npc_names or {}
    groups = npc_groups or {}
    zones_of = group_zones or {}
    traps = trap_zones or {}
    for npc, item_ids in (npc_drops or {}).items():
        name = names.get(npc) or ""
        if not name:
            continue
        zones = tuple(sorted({zone for group in groups.get(npc, ()) for zone in zones_of.get(group, ())}))
        for item_id in item_ids:
            by_item[item_id].append((npc, name, zones))
    for item_id, droppers in by_item.items():
        # Rare named drops (boss / trap packs). Trash with dozens of NPCs stays zone-only.
        if len(droppers) > 6:
            continue
        for npc, name, zones in droppers[:6]:
            place_zones = zones or traps.get(npc, ())
            if place_zones:
                for zone in place_zones[:3]:
                    found[item_id].add(f"loot:{name}@{zone}")
            else:
                found[item_id].add(f"loot:{name}")
    return {item_id: tuple(sorted(rows)) for item_id, rows in found.items()}


def _npc_drops(drops, tables, npc_loot) -> dict[int, tuple[int, ...]]:
    """Items an NPC type can drop. A quest spawn never has a spawn2 row, so the zone join misses it."""
    found: dict[int, set[int]] = defaultdict(set)
    for npc, table in npc_loot.items():
        for drop_id in tables.get(table, ()):
            found[npc].update(drops.get(drop_id, ()))
    return {npc: tuple(sorted(items)) for npc, items in found.items() if items}


def _take_object(line: str, placed: dict[int, set[int]], titles: dict[int, set[str]]) -> None:
    """One world object. Column 2 is zoneidnumber. Column 11 is the bag type."""
    fields = _tuple(line)
    if len(fields) < 11 or not fields[1].lstrip("-").isdigit() or not fields[10].lstrip("-").isdigit():
        return
    kind = int(fields[10])
    zone_id = int(fields[1])
    if kind not in _BAG_TYPES or zone_id <= 0:
        return
    placed[kind].add(zone_id)
    if len(fields) > 25 and fields[25] not in {"", "NULL"}:
        titles[kind].add(fields[25])


def _world_containers(placed, titles, zone_names) -> dict[int, dict]:
    """Stations you combine in. The name is the bag type; the zones are where one is placed."""
    found: dict[int, dict] = {}
    for kind, zone_ids in placed.items():
        zones = tuple(sorted(zone_names[zone_id] for zone_id in zone_ids if zone_id in zone_names))
        name = _BAG_TYPES.get(kind) or next(iter(titles.get(kind, ())), f"world container {kind}")
        found[kind] = {"name": name, "zones": zones}
    return found


def _take_recipe_skill(line: str, recipe_skill: dict[int, dict]) -> None:
    """One tradeskill_recipe row. skillneeded is the minimum. trivial is where it stops failing."""
    fields = _tuple(line)
    if len(fields) < 5 or not fields[0].isdigit():
        return

    def number(index: int) -> int:
        if index >= len(fields) or not fields[index].lstrip("-").isdigit():
            return 0
        return int(fields[index])

    skill = number(2)
    recipe_skill[int(fields[0])] = {
        "skill": skill,
        "skill_name": _SKILLS.get(skill, ""),
        "skillneeded": number(3),
        "trivial": number(4),
        "nofail": number(5),
        "must_learn": number(8),
        "enabled": number(11) if len(fields) > 11 else 1,
    }


def _apply_recipe_skill(recipes: dict[int, dict], recipe_skill: dict[int, dict]) -> None:
    for recipe_id, info in recipes.items():
        row = recipe_skill.get(recipe_id)
        if row:
            info.update(row)


def _take_recipe(line: str, recipes: dict[int, dict]) -> None:
    """One tradeskill_recipe_entries row.

    successcount > 0 is returned on a successful combine. A recipe can return more than one item.
    componentcount > 0 is an ingredient, including an ingredient that is also returned.
    """
    fields = _tuple(line)
    if len(fields) < 8 or not fields[1].isdigit() or not fields[2].lstrip("-").isdigit():
        return
    recipe_id = int(fields[1])
    item_id = int(fields[2])
    success = int(fields[3]) if fields[3].lstrip("-").isdigit() else 0
    count = int(fields[5]) if fields[5].lstrip("-").isdigit() else 0
    container = int(fields[7]) if fields[7].lstrip("-").isdigit() else 0
    slot = recipes.setdefault(recipe_id, {"components": [], "container": 0, "result": 0, "results": []})
    slot.setdefault("results", [])
    if container and item_id:
        slot["container"] = item_id
    if count > 0 and item_id and not container:
        slot["components"].append((item_id, count))
    if success > 0 and item_id and not container:
        slot["results"].append((item_id, success))
        if not slot["result"]:
            slot["result"] = item_id


def _table(line: str) -> str:
    start = line.find("`") + 1
    end = line.find("`", start)
    return line[start:end]


def _take_item(line: str, catalog: Catalog) -> None:
    fields = _tuple(line)
    if len(fields) < 3 or not fields[0].isdigit() or not fields[2]:
        return
    item_id = int(fields[0])
    label = fields[2]
    key = " ".join(label.lower().split())
    catalog.names.setdefault(key, [])
    if item_id not in catalog.names[key]:
        catalog.names[key].append(item_id)
    catalog.labels.setdefault(item_id, label)


def _tuple(line: str) -> list[str]:
    """Fields of one `(...)` values row. Quotes keep commas inside a name.

    The last row of an INSERT ends in `);`. Dropping that semicolon is what keeps the row.
    """
    text = line.strip().rstrip(";").rstrip(",").strip()
    if not text.startswith("(") or not text.endswith(")"):
        return []
    body = text[1:-1]
    fields: list[str] = []
    index = 0
    size = len(body)
    while index < size:
        if body[index] == "'":
            index += 1
            chars: list[str] = []
            while index < size:
                if body[index] == "\\" and index + 1 < size:
                    chars.append(body[index + 1])
                    index += 2
                    continue
                if body[index] == "'":
                    if index + 1 < size and body[index + 1] == "'":
                        chars.append("'")
                        index += 2
                        continue
                    index += 1
                    break
                chars.append(body[index])
                index += 1
            fields.append("".join(chars))
        else:
            comma = body.find(",", index)
            if comma < 0:
                fields.append(body[index:].strip())
                break
            fields.append(body[index:comma].strip())
            index = comma
        if index < size and body[index] == ",":
            index += 1
        while index < size and body[index] == " ":
            index += 1
    return fields


# EQ::item::BagType. object.type and a recipe's iscontainer value share these numbers.
# The comments in item_data.h are database string ids, not the enum values.
_BAG_TYPES = {
    9: "Medicine Bag",
    10: "Toolbox",
    11: "Lexicon",
    12: "Mortar",
    13: "Self Dusting",
    14: "Mixing Bowl",
    15: "Oven",
    16: "Sewing Kit",
    17: "Forge",
    18: "Fletching Kit",
    19: "Brew Barrel",
    20: "Jeweler's Kit",
    21: "Pottery Wheel",
    22: "Kiln",
    23: "Keymaker",
    24: "Wizard's Lexicon",
    25: "Mage's Lexicon",
    26: "Necromancer's Lexicon",
    27: "Enchanter's Lexicon",
    29: "Concordance of Research",
    30: "Always Works",
    31: "Koada'Dal Forge",
    32: "Teir'Dal Forge",
    33: "Oggok Forge",
    34: "Stormguard Forge",
    35: "Ak'Anon Forge",
    36: "Northman Forge",
    38: "Cabilis Forge",
    39: "Freeport Forge",
    40: "Royal Qeynos Forge",
    41: "Halfling Tailoring Kit",
    42: "Erudite Tailoring Kit",
    43: "Fier'Dal Tailoring Kit",
    44: "Fier'Dal Fletching Kit",
    45: "Iksar Pottery Wheel",
    46: "Tackle Box",
    47: "Troll Forge",
    48: "Fier'Dal Forge",
    49: "Vale Forge",
    50: "Erudite Forge",
    52: "Gukta Forge",
    54: "Ice Cream Churn",
    55: "Transformation Mold",
    56: "Detransformation Mold",
    57: "Unattuner",
    58: "Tradeskill Bag",
    59: "Collectible Bag",
}

# EQ::skills::SkillType values used by tradeskill_recipe.tradeskill.
_SKILLS = {
    55: "Fishing",
    56: "Make Poison",
    57: "Tinkering",
    58: "Research",
    59: "Alchemy",
    60: "Baking",
    61: "Tailoring",
    63: "Blacksmithing",
    64: "Fletching",
    65: "Brewing",
    68: "Jewelry Making",
    69: "Pottery",
    75: "Remove Traps",
}

_WORDS = re.compile(r"[A-Za-z][A-Za-z'`-]*")
_LEAD = {"a", "an", "the"}
_SKIP = {
    "you", "your", "must", "bring", "from", "with", "and", "then", "will", "this", "that",
    "have", "for", "are", "our", "not", "yet", "into", "they", "them", "their", "hello",
    "there", "need", "something", "accept", "thanks", "reward", "quested", "well",
}
