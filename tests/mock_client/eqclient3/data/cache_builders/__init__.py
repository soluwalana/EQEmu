"""Offline builders that materialize ~/.eqclient/*.jsonl caches from peq / quests.

Runtime code (agent) always loads the jsonl caches. Rebuild with:

    python -m eqclient3.data.cache_builders
    python -m eqclient3.data.cache_builders faction_list
"""

from __future__ import annotations

BUILDERS = (
    "faction_list",
    "factions",
    "drops",
    "merchants",
    "items",
    "spells",
    "bot_spells",
    "recipes",
    "zone_graph",
    "quest_graph",
    "item_locations",
)
