"""One graph edge becomes Zone, Talk, Deliver, Fetch, and Travel.

A giver in another zone is a Zone, then a Talk hail, then one Deliver for every
item in that hand-in. A component that drops is a Fetch, with a Travel when the
drop is in another zone. A component that is only a hand-in is the giver chain
again. These are v3 actions. This module does not import the loop.
"""

from __future__ import annotations

from eqclient3.log import log
from eqclient3.actions.deliver import Deliver
from eqclient3.actions.fetch import Fetch
from eqclient3.actions.talk import Talk
from eqclient3.actions.travel import Travel
from eqclient3.actions.zone import Zone
from eqclient3.quests.graph import QuestGraph, split_npc


def expand(edge: dict, *, here: str = "", graph: QuestGraph | None = None, source: str = "") -> list:
    """Turn one gives, receives, or drop edge into actions."""
    return _expand(edge, here=here, graph=graph, source=source, seen=set())


def _expand(edge: dict, *, here: str, graph: QuestGraph | None, source: str, seen: set) -> list:
    key = (edge.get("rel"), edge.get("from"), edge.get("to"), edge.get("group"))
    if key in seen:
        return []
    seen.add(key)
    rel = edge.get("rel")
    if rel in {"loots", "grounds"}:
        return _drop(edge, here=here, source=source)
    if rel not in {"gives", "receives"}:
        return []
    zone, npc = split_npc(str(edge.get("from") or ""))
    if not npc:
        return []
    label = source or f"quest:{zone}/{npc}"
    hand = _hand_items(edge, graph)
    reward = _token_item(edge.get("to")) if edge.get("rel") == "gives" else 0
    actions: list = []
    if graph is not None and reward:
        for component in graph.components(reward):
            actions.extend(
                _obtain(component, 1, here=here, graph=graph, source=label, seen=seen, npc=npc)
            )
    for item_id, count in hand:
        actions.extend(_obtain(item_id, count, here=here, graph=graph, source=label, seen=seen, npc=npc))
    actions.extend(_giver(zone, npc, hand, here=here, source=label))
    return actions


def _hand_items(edge: dict, graph: QuestGraph | None) -> list[tuple[int, int]]:
    """The items that cross in this hand-in. A hail with no receives has none."""
    group = str(edge.get("group") or "")
    if graph is not None and group:
        received = graph.receives_in(group)
        if received:
            return received
    if edge.get("rel") == "receives":
        item_id = _token_item(edge.get("to"))
        if item_id:
            return [(item_id, max(1, int(edge.get("count") or 1)))]
    return []


def _obtain(item_id: int, count: int, *, here: str, graph: QuestGraph | None, source: str, seen: set, npc: str) -> list:
    """A drop is a Fetch. A hand-in-only component is that giver's chain."""
    drops = graph.drops(item_id) if graph is not None else []
    if drops:
        return _drop(drops[0], here=here, source=source, item_id=item_id, count=count)
    giver = _other_giver(graph, item_id, npc, seen)
    if giver is None:
        return []
    return _expand(giver, here=here, graph=graph, source=source, seen=seen)


def _other_giver(graph: QuestGraph | None, item_id: int, npc: str, seen: set) -> dict | None:
    if graph is None:
        return None
    edge = graph.gives(item_id)
    if edge is None:
        return None
    _zone, giver = split_npc(str(edge.get("from") or ""))
    if giver.lower() == npc.lower():
        return None
    key = (edge.get("rel"), edge.get("from"), edge.get("to"), edge.get("group"))
    if key in seen:
        return None
    return edge


def _drop(edge: dict, *, here: str, source: str, item_id: int = 0, count: int = 1) -> list:
    Zone, Talk, Deliver, Fetch, Travel = _classes()
    del Zone, Talk, Deliver
    item_id = item_id or _token_item(edge.get("to"))
    if not item_id:
        return []
    count = max(1, int(edge.get("count") or count or 1))
    zone = str(edge.get("zone") or "") or split_npc(str(edge.get("from") or ""))[0]
    label = source or f"quest:item={item_id}"
    actions = []
    if zone and here and zone.lower() != here.lower():
        travel = Travel(zone)
        travel.source = f"{label}#travel:{zone}"
        actions.append(travel)
    fetch = Fetch(item_id, count, str(item_id))
    fetch.source = f"{label}#fetch:{item_id}"
    actions.append(fetch)
    return actions


def _giver(zone: str, npc: str, hand: list[tuple[int, int]], *, here: str, source: str) -> list:
    Zone, Talk, Deliver, Fetch, Travel = _classes()
    del Fetch, Travel
    actions = []
    if zone and here and zone.lower() != here.lower():
        zone_action = Zone(zone)
        zone_action.source = f"{source}#zone:{zone}"
        actions.append(zone_action)
    text = "+".join(str(item_id) for item_id, _count in hand)
    talk = Talk(npc, "hail", text, 280)
    talk.priority = 280
    talk.source = f"{source}#hail:{npc}"
    actions.append(talk)
    for item_id, _count in hand:
        deliver = Deliver(item_id, npc)
        deliver.source = f"{source}#deliver:{item_id}"
        actions.append(deliver)
    return actions


def _token_item(token: str) -> int:
    text = str(token or "")
    if not text.startswith("item:"):
        return 0
    try:
        return int(text.split(":", 1)[1])
    except ValueError:
        log.error("item token failed to parse: %s", text, exc_info=True)
        return 0


def _classes() -> tuple[object, ...]:
    return Zone, Talk, Deliver, Fetch, Travel
