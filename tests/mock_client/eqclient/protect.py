"""Items the agent must not drop, destroy, or vendor."""

from __future__ import annotations


def protected_ids(graph=None, campaign=None, zone_quests=None) -> set[int]:
    """Quest / campaign / irreplaceable item ids.

    Protects active campaign goals, current zone script needs, every graph
    hand-in need/receive, and quest rewards that have no loot/forage/buy/recipe
    source (cannot be obtained again without the flagged quest).
    """
    found: set[int] = set()
    if campaign is not None:
        sell_after = {int(item_id) for item_id in (getattr(campaign, "sell_after", ()) or ())}
        found.update(
            int(item_id)
            for item_id in (getattr(campaign, "stack", ()) or ())
            if int(item_id) not in sell_after
        )
    if zone_quests is not None:
        for script in getattr(zone_quests, "scripts", {}).values():
            for need in getattr(script, "needs", ()) or ():
                item_id = int(getattr(need, "item_id", 0) or 0)
                if item_id:
                    found.add(item_id)

    regenerative: set[int] = set()
    hand_ins: set[int] = set()
    quest_gives: set[int] = set()
    if graph is not None:
        for edge in getattr(graph, "edges", ()) or ():
            to = str(edge.get("to") or "")
            if not to.startswith("item:"):
                continue
            try:
                item_id = int(to.split(":", 1)[1])
            except ValueError:
                continue
            rel = edge.get("rel")
            if rel in {"loots", "grounds", "produces", "buys", "sells"}:
                regenerative.add(item_id)
            elif rel in {"needs", "receives"}:
                hand_ins.add(item_id)
            elif rel == "gives":
                quest_gives.add(item_id)
        for item_id, info in (getattr(graph, "items", {}) or {}).items():
            sources = info.get("sources") or ()
            if any(
                str(src).startswith(("loot:", "forage:", "fishing:", "ground:", "merchant:"))
                for src in sources
            ):
                regenerative.add(int(item_id))

    found |= hand_ins
    found |= {item_id for item_id in quest_gives if item_id not in regenerative}
    return found


def is_protected(item_id: int, graph=None, campaign=None, zone_quests=None) -> bool:
    if item_id <= 0:
        return False
    return item_id in protected_ids(graph, campaign, zone_quests)
