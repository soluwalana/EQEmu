"""One graph edge becomes Zone, Talk, Deliver, Fetch, Travel, and Craft.

A giver in another zone is a Zone, then a Talk hail, then one Deliver for every
item in that hand-in. A component that drops is a Fetch, with a Travel when the
drop is in another zone. A component that is only a hand-in is the giver chain
again. A produced item is that recipe's components, then a Craft. These are v3
actions. This module does not import the loop.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.action import Action

from eqclient3.log import log
from eqclient3.actions.craft import Craft
from eqclient3.actions.deliver import Deliver
from eqclient3.actions.fetch import Fetch
from eqclient3.actions.talk import Talk
from eqclient3.actions.travel import Travel
from eqclient3.actions.zone import Zone
from eqclient3.data.recipes import Recipe, _WORLD_CONTAINER
from eqclient3.quests.graph import QuestGraph, split_npc


def expand(edge: dict, *, here: str = "", graph: QuestGraph | None = None, source: str = "") -> list:
    """Turn one gives, receives, drop, or produces edge into actions."""
    return _expand(edge, here=here, graph=graph, source=source, seen=set())


def _expand(edge: dict, *, here: str, graph: QuestGraph | None, source: str, seen: set) -> list:
    key = (edge.get("rel"), edge.get("from"), edge.get("to"), edge.get("group"))
    if key in seen:
        return []
    seen.add(key)
    rel = edge.get("rel")
    if rel == "produces":
        return _craft(edge, here=here, graph=graph, source=source, seen=seen)
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
                _obtain(
                    component,
                    1,
                    here=here,
                    graph=graph,
                    source=label,
                    seen=seen,
                    npc=npc,
                )
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


def _obtain(
    item_id: int,
    count: int,
    *,
    here: str,
    graph: QuestGraph | None,
    source: str,
    seen: set,
    npc: str,
) -> list:
    """A drop is a Fetch. A hand-in is that giver's chain. A combine is a Craft."""
    drops = graph.drops(item_id) if graph is not None else []
    if drops:
        return _drop(drops[0], here=here, source=source, item_id=item_id, count=count)
    giver = _other_giver(graph, item_id, npc, seen)
    if giver is not None:
        return _expand(giver, here=here, graph=graph, source=source, seen=seen)
    made = produced(graph, item_id) if graph is not None else None
    if made is None:
        return []
    return _expand(made, here=here, graph=graph, source=source, seen=seen)


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
    item_id = item_id or _token_item(edge.get("to"))
    if not item_id:
        return []
    count = max(1, int(edge.get("count") or count or 1))
    zone = str(edge.get("zone") or "") or split_npc(str(edge.get("from") or ""))[0]
    label = source or f"quest:item={item_id}"
    actions: list[Action] = []
    if zone and here and zone.lower() != here.lower():
        travel = Travel(zone)
        travel.source = f"{label}#travel:{zone}"
        actions.append(travel)
    fetch = Fetch(item_id, count, str(item_id))
    fetch.source = f"{label}#fetch:{item_id}"
    actions.append(fetch)
    return actions


def _giver(zone: str, npc: str, hand: list[tuple[int, int]], *, here: str, source: str) -> list:
    actions: list[Action] = []
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


def produced(graph: QuestGraph, item_id: int) -> dict | None:
    """The produces edge for the simplest recipe that creates this item and does not consume it."""
    ranked: list[tuple[tuple[int, int, int], dict]] = []
    for edge in graph.to_item(item_id):
        if edge.get("rel") != "produces":
            continue
        recipe_id = _recipe_id(str(edge.get("from") or ""))
        if not recipe_id:
            continue
        recipe = _recipe(graph, recipe_id)
        if recipe is None or not recipe.components or not recipe.result:
            continue
        if item_id in _inputs(recipe):
            continue
        rank = (len(recipe.components), recipe.trivial or 9999, recipe.id)
        ranked.append((rank, edge))
    if not ranked:
        return None
    ranked.sort(key=lambda row: row[0])
    return ranked[0][1]


def _craft(edge: dict, *, here: str, graph: QuestGraph | None, source: str, seen: set) -> list[Action]:
    """Components first, then the station zone, then the combine."""
    if graph is None:
        return []
    recipe_id = _recipe_id(str(edge.get("from") or ""))
    if not recipe_id:
        return []
    recipe = _recipe(graph, recipe_id)
    if recipe is None or not recipe.components:
        return []
    item_id = _token_item(edge.get("to"))
    if item_id in _inputs(recipe):
        return []
    label = source or f"recipe:{recipe.id}"
    actions: list[Action] = []
    for component, count in recipe.components:
        actions.extend(_obtain(component, count, here=here, graph=graph, source=label, seen=seen, npc=""))
    if recipe.container and recipe.container not in _WORLD_CONTAINER:
        actions.extend(_obtain(recipe.container, 1, here=here, graph=graph, source=label, seen=seen, npc=""))
    zone = _station_zone(graph, recipe.container, here)
    if zone:
        station = Zone(zone)
        station.source = f"{label}#zone:{zone}"
        actions.append(station)
    made = Craft(recipe)
    made.source = f"{label}#craft:{recipe.id}"
    actions.append(made)
    return actions


def _recipe(graph: QuestGraph, recipe_id: int) -> Recipe | None:
    """One Recipe from the consumes, container, and produces edges of recipe:{id}."""
    source = f"recipe:{recipe_id}"
    rows = [edge for edge in graph.edges if str(edge.get("from") or "") == source]
    if not rows:
        return None
    components: list[tuple[int, int]] = []
    results: list[tuple[int, int]] = []
    container = 0
    skill = 0
    skillneeded = 0
    trivial = 0
    name = ""
    for edge in rows:
        rel = edge.get("rel")
        token = str(edge.get("to") or "")
        if rel == "consumes":
            item_id = _token_item(token)
            if item_id:
                components.append((item_id, _count(edge)))
        elif rel == "produces":
            item_id = _token_item(token)
            if item_id:
                results.append((item_id, _count(edge)))
        elif rel == "container":
            container = _id_token(token)
        if not skill:
            skill = _number(edge, "skill")
        if not skillneeded:
            skillneeded = _number(edge, "skillneeded")
        if not trivial:
            trivial = _number(edge, "trivial")
        if not name:
            name = _text(edge, "skill_name")
    if not results:
        return None
    return Recipe(
        id=recipe_id,
        result=results[0][0],
        components=tuple(components),
        container=container,
        results=tuple(results),
        skill=skill,
        skillneeded=skillneeded,
        trivial=trivial,
        name=name,
    )


def _inputs(recipe: Recipe) -> set[int]:
    found = {component for component, _count in recipe.components}
    if recipe.container and recipe.container not in _WORLD_CONTAINER:
        found.add(recipe.container)
    return found


def _station_zone(graph: QuestGraph, container: int, here: str) -> str:
    """A forge or oven zone when this one has none. Empty when the station is already here."""
    if not here or container not in _WORLD_CONTAINER:
        return ""
    info = graph.world.get(container)
    if not info:
        return ""
    zones = info.get("zones") or ()
    if isinstance(zones, str) or not isinstance(zones, (list, tuple)):
        return ""
    names = [zone for zone in zones if isinstance(zone, str) and zone]
    if not names or any(zone.lower() == here.lower() for zone in names):
        return ""
    return names[0]


def _recipe_id(origin: str) -> int:
    if not origin.startswith("recipe:"):
        return 0
    raw = origin[7:]
    if not raw.isdigit():
        return 0
    return int(raw)


def _id_token(token: str) -> int:
    kind, _, raw = token.partition(":")
    if kind not in {"item", "world"} or not raw.isdigit():
        return 0
    return int(raw)


def _count(edge: dict) -> int:
    value = edge.get("count")
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        return 1
    return value


def _number(edge: dict, name: str) -> int:
    value = edge.get(name)
    if isinstance(value, bool) or not isinstance(value, int):
        return 0
    return value


def _text(edge: dict, name: str) -> str:
    value = edge.get(name)
    if isinstance(value, str):
        return value
    return ""


def _token_item(token: object) -> int:
    text = token if isinstance(token, str) else ""
    if not text.startswith("item:"):
        return 0
    try:
        return int(text.split(":", 1)[1])
    except ValueError:
        log.error("item token failed to parse: %s", text, exc_info=True)
        return 0
