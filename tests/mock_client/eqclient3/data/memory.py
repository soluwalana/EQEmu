"""Read ~/.eqclient caches once and keep the indexed books."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from eqclient3.bots.spells import read_bot_spells
from eqclient3.data.cache_builders.faction_list import read_faction_list
from eqclient3.data.drops import read_drops
from eqclient3.data.factions import read_factions
from eqclient3.data.locations import LocationBook, read_locations
from eqclient3.data.merchants import read_merchants
from eqclient3.data.spells import read_spells
from eqclient3.nav.travel import ZoneGraph, read_zone_graph
from eqclient3.quests.graph import QuestGraph, read_graph


@dataclass
class Caches:
    """In-memory indexes. Queries hit these dicts, not the jsonl files."""

    items: ItemBook
    drops: object
    merchants: object
    factions: object
    faction_names: dict[str, int]
    faction_ids: dict[int, str]
    spells: object
    bot_spells: object
    recipes: RecipeBook
    zones: ZoneGraph
    graph: QuestGraph
    locations: LocationBook

    def faction_id(self, name: str) -> int:
        return int(self.faction_names.get((name or "").lower(), 0))

    def faction_name(self, faction_id: int) -> str:
        return self.faction_ids.get(int(faction_id), "")


def load_caches(root: str | Path | None = None) -> Caches:
    """Read every cache file under `root` (default ~/.eqclient) and index it.

    An explicit root ignores EQEMU_* path overrides. The default root still honors them.
    A missing file becomes an empty index. Drops and item locations map a sibling
    `.eqm` file, and build that file from the jsonl when it is missing or older.
    """
    # item_stats and conduct are not in this tree; import them when caches load.
    from eqclient3.inventory.item_stats import read_items
    from eqclient3.quests.conduct import read_recipes

    if root is None:
        directory = Path(os.environ.get("EQEMU_CACHE", Path.home() / ".eqclient"))

        def file(env: str, name: str) -> str:
            return os.environ.get(env) or str(directory / name)
    else:
        directory = Path(root)

        def file(_env: str, name: str) -> str:
            return str(directory / name)

    names = read_faction_list(file("EQEMU_FACTION_LIST", "faction_list.jsonl"))
    ids = {int(faction_id): name for name, faction_id in names.items() if int(faction_id)}
    caches = Caches(
        items=read_items(file("EQEMU_ITEMS", "items.jsonl")),
        drops=read_drops(file("EQEMU_DROPS", "drops.jsonl")),
        merchants=read_merchants(file("EQEMU_MERCHANTS", "merchants.jsonl")),
        factions=read_factions(file("EQEMU_FACTIONS", "faction_hits.jsonl")),
        faction_names=names,
        faction_ids=ids,
        spells=read_spells(file("EQEMU_SPELLS", "spells.jsonl")),
        bot_spells=read_bot_spells(file("EQEMU_BOT_SPELLS", "bot_spells.jsonl")),
        recipes=read_recipes(file("EQEMU_RECIPES", "recipes.jsonl")),
        zones=read_zone_graph(file("EQEMU_ZONE_GRAPH", "zone_graph.jsonl")),
        graph=read_graph(file("EQEMU_GRAPH", "quest_graph.jsonl")),
        locations=read_locations(file("EQEMU_ITEM_LOCATIONS", "item_locations.jsonl")),
    )
    nodes = len(caches.graph.edges)
    print(
        "caches:"
        f" {len(caches.items.by_id)} items,"
        f" {len(caches.drops.by_npc)} drop npcs,"
        f" {len(caches.merchants.by_npc)} merchants,"
        f" {len(caches.factions.by_faction)} factions,"
        f" {len(caches.faction_names)} faction names,"
        f" {len(caches.spells.rows)} spells,"
        f" {len(caches.bot_spells.rows)} bot spells,"
        f" {len(caches.recipes.by_id)} recipes,"
        f" {len(caches.zones.zones)} zones,"
        f" {nodes} quest edges,"
        f" {len(caches.locations.by_item)} item locations"
        f" from {directory}",
        flush=True,
    )
    return caches
