"""One graph edge becomes Zone, QuestTalk, Fetch, Travel, and Craft.

A giver in another zone is a Zone, then one QuestTalk for that conversation.
The talk follows then-links while the flag those links need was set on the way,
and stops at the say or hand that gives the item. A component that drops is a
Fetch, with a Travel when the drop is in another zone. A component that is
only a hand-in is the giver chain again. A produced item is that recipe's
components, then a Craft. These are v3 actions. This module does not import
the loop.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.action import Action

from eqclient3.log import log
from eqclient3.actions.craft import Craft
from eqclient3.actions.fetch import Fetch
from eqclient3.actions.quest_talk import (
    Expect,
    ExpectFaction,
    ExpectItem,
    ExpectMoney,
    Faction,
    Hand,
    Money,
    Need,
    QuestTalk,
    Receive,
    Say,
    Turn,
)
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
    actions.extend(_giver(zone, npc, hand, here=here, source=label, graph=graph, edge=edge))
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


def conversation(graph: QuestGraph, origin: str, expect: int) -> tuple[tuple[Turn, ...], Expect | None]:
    """The say, hand, and receive steps from this node through the then-links that belong to it.

    A later say is part of this conversation when the flag it needs was set on the way.
    The say or hand that gives expect ends the chain. The second value is what ends the
    talk: that item, or the money or faction this conversation pays when it gives no item.
    """
    node = _bare(origin)
    if "#" not in node:
        return (), None
    index = _by_origin(graph)
    turns: list[Turn] = []
    sets: dict[str, str] = {}
    seen: set[str] = set()
    held: set[int] = set()
    done: Expect | None = ExpectItem(expect) if expect else None
    while node and node not in seen:
        seen.add(node)
        tail = _tail(node)
        hands = _hand_ids(tail)
        for item_id in _item_needs(index, node):
            if item_id not in hands and item_id not in held:
                turns.append(Need(item_id))
        word = _word(tail)
        if word:
            turns.append(Say(word))
        for item_id in hands:
            if item_id not in held:
                turns.append(Need(item_id))
            turns.append(Hand(item_id))
        gave = _gives(index, node)
        for item_id in gave:
            turns.append(Receive(item_id))
            held.add(item_id)
        turns.extend(_pay_steps(index, node))
        sets.update(_flag_sets(index, node))
        if done is None:
            done = _paid(index, node)
        if expect and expect in gave:
            break
        nxt = _then_next(index, node)
        if not nxt or not _gate_open(index, nxt, sets, _received(turns)):
            break
        node = _bare(nxt)
    return tuple(turns), done


def _giver(
    zone: str,
    npc: str,
    hand: list[tuple[int, int]],
    *,
    here: str,
    source: str,
    graph: QuestGraph | None,
    edge: dict,
) -> list:
    actions: list[Action] = []
    if zone and here and zone.lower() != here.lower():
        zone_action = Zone(zone)
        zone_action.source = f"{source}#zone:{zone}"
        actions.append(zone_action)
    item = _reward(graph, edge)
    origin = str(edge.get("group") or edge.get("from") or "")
    steps: tuple[Turn, ...] = ()
    done: Expect | None = ExpectItem(item) if item else None
    if graph is not None:
        steps, done = conversation(graph, origin, item)
        if item:
            done = ExpectItem(item)
    if not steps:
        steps = _fallback(origin, hand)
    if not steps:
        return actions
    talk = QuestTalk(npc, steps, expect=done)
    talk.source = _talk_source(source, npc, steps)
    actions.append(talk)
    return actions


def _fallback(origin: str, hand: list[tuple[int, int]]) -> tuple[Turn, ...]:
    turns: list[Turn] = []
    word = _word(_tail(origin))
    if word:
        turns.append(Say(word))
    if turns:
        return tuple(turns)
    for item_id, _count in hand:
        turns.append(Hand(item_id))
    return tuple(turns)


def _talk_source(source: str, npc: str, steps: tuple[Turn, ...]) -> str:
    said = [turn.word for turn in steps if isinstance(turn, Say)]
    if said:
        return f"{source}#say:{npc}:{said[0]}"
    handed = [str(turn.item) for turn in steps if isinstance(turn, Hand)]
    if handed:
        return f"{source}#hand:{npc}:{'+'.join(handed)}"
    return f"{source}#talk:{npc}"


def _by_origin(graph: QuestGraph) -> dict[str, list[dict]]:
    found: dict[str, list[dict]] = {}
    for edge in graph.edges:
        origin = edge.get("from")
        if isinstance(origin, str) and origin:
            found.setdefault(origin, []).append(edge)
        group = edge.get("group")
        if isinstance(group, str) and group and group != origin:
            found.setdefault(group, []).append(edge)
            bare = _bare(group)
            if bare != group:
                found.setdefault(bare, []).append(edge)
    return found


def _bare(origin: str) -> str:
    if "#holds:" in origin:
        return origin.split("#holds:", 1)[0]
    return origin


def _tail(origin: str) -> str:
    if "#" not in origin:
        return ""
    return origin.split("#", 1)[1]


def _word(tail: str) -> str:
    """The script match. A hand-in, a recipe, and an event have none."""
    if not tail or tail.startswith(("hand:", "recipe:", "event_")) or tail in {"enter", "loot", "kill"}:
        return ""
    return tail


def _hand_ids(tail: str) -> list[int]:
    if not tail.startswith("hand:"):
        return []
    found: list[int] = []
    for bit in tail[5:].split("+"):
        if bit.isdigit():
            found.append(int(bit))
    return found


def _gives(index: dict[str, list[dict]], node: str) -> list[int]:
    found: list[int] = []
    for edge in index.get(node, []):
        if edge.get("rel") != "gives":
            continue
        item_id = _token_item(edge.get("to"))
        if item_id and item_id not in found:
            found.append(item_id)
    return found


def _item_needs(index: dict[str, list[dict]], node: str) -> list[int]:
    """Items this line requires him to already hold. The hand-in items are fetched with the hand."""
    found: list[int] = []
    for edge in index.get(node, []):
        if edge.get("rel") != "needs" or edge.get("from") != node:
            continue
        item_id = _whole(edge.get("item"))
        if item_id is not None and item_id > 0 and item_id not in found:
            found.append(item_id)
    return found


def _pay_steps(index: dict[str, list[dict]], node: str) -> list[Turn]:
    """Coin and faction changes this line waits for before the conversation goes on."""
    steps: list[Turn] = []
    paid = _money_pay(index, node)
    if paid is not None:
        steps.append(Money(paid.platinum, paid.gold, paid.silver, paid.copper))
    for edge in index.get(node, []):
        if edge.get("rel") != "sets" or edge.get("from") != node:
            continue
        faction_id = _whole(edge.get("faction"))
        delta = _whole(edge.get("value"))
        if faction_id is None or delta is None or faction_id <= 0:
            continue
        steps.append(Faction(faction_id, delta))
    return steps


def _paid(index: dict[str, list[dict]], node: str) -> Expect | None:
    """Faction standing or coin this line pays, when it summons no item."""
    faction = _faction_pay(index, node)
    if faction is not None:
        return faction
    return _money_pay(index, node)


def _faction_pay(index: dict[str, list[dict]], node: str) -> ExpectFaction | None:
    chosen: ExpectFaction | None = None
    for edge in index.get(node, []):
        if edge.get("rel") != "sets" or edge.get("from") != node:
            continue
        faction_id = _whole(edge.get("faction"))
        delta = _whole(edge.get("value"))
        if faction_id is None or delta is None or faction_id <= 0:
            continue
        pay = ExpectFaction(faction_id, delta)
        if chosen is None or (chosen.delta < 0 < delta):
            chosen = pay
    return chosen


def _money_pay(index: dict[str, list[dict]], node: str) -> ExpectMoney | None:
    amounts = [0, 0, 0, 0]
    found = False
    slots = {"platinum": 0, "gold": 1, "silver": 2, "copper": 3}
    for edge in index.get(node, []):
        if edge.get("rel") != "gives":
            continue
        token = edge.get("to")
        if not isinstance(token, str) or not token.startswith("coin:"):
            continue
        slot = slots.get(token.split(":", 1)[1])
        if slot is None:
            continue
        count = _whole(edge.get("count"))
        if count is not None and count > 0:
            amounts[slot] += count
        found = True
    if not found:
        return None
    return ExpectMoney(amounts[0], amounts[1], amounts[2], amounts[3])


def _whole(value: object) -> int | None:
    if isinstance(value, bool) or value is None:
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, str) and value.lstrip("-").isdigit():
        return int(value)
    return None


def _flag_sets(index: dict[str, list[dict]], node: str) -> dict[str, str]:
    found: dict[str, str] = {}
    for edge in index.get(node, []):
        if edge.get("rel") != "sets" or edge.get("from") != node:
            continue
        flag = edge.get("flag")
        value = edge.get("value")
        if isinstance(flag, str) and isinstance(value, str):
            found[flag] = value
    return found


def _then_next(index: dict[str, list[dict]], node: str) -> str:
    for edge in index.get(node, []):
        if edge.get("rel") != "then" or edge.get("from") != node:
            continue
        dest = edge.get("to")
        if isinstance(dest, str) and dest:
            return dest
    return ""


def _gate_open(index: dict[str, list[dict]], node: str, sets: dict[str, str], received: set[int]) -> bool:
    """True when this say's flag and item gates were met by the lines already included."""
    for edge in index.get(node, []):
        if edge.get("rel") != "needs" or edge.get("from") != node:
            continue
        item = edge.get("item")
        if isinstance(item, int) and not isinstance(item, bool):
            if item not in received:
                return False
            continue
        flag = edge.get("flag")
        at = edge.get("at")
        if isinstance(flag, str) and isinstance(at, str) and not _flag_met(sets.get(flag), at):
            return False
    return True


def _flag_met(have: str | None, at: str) -> bool:
    if at == "unset":
        return have is None
    if have is None:
        return False
    op = ""
    raw = at
    for token in ("==", ">=", "<=", ">", "<"):
        if at.startswith(token):
            op = token
            raw = at[len(token) :]
            break
    if not op or not have.lstrip("-").isdigit() or not raw.lstrip("-").isdigit():
        return False
    got = int(have)
    want = int(raw)
    if op == "==":
        return got == want
    if op == ">=":
        return got >= want
    if op == "<=":
        return got <= want
    if op == ">":
        return got > want
    return got < want


def _received(turns: list[Turn]) -> set[int]:
    return {turn.item for turn in turns if isinstance(turn, Receive)}


def _reward(graph: QuestGraph | None, edge: dict) -> int:
    """The item this giver summons. A hand-in edge points at the same group as its gives edge."""
    if edge.get("rel") == "gives":
        return _token_item(edge.get("to"))
    group = str(edge.get("group") or "")
    if graph is None or not group:
        return 0
    for row in graph.edges:
        if row.get("rel") == "gives" and row.get("group") == group:
            return _token_item(row.get("to"))
    return 0


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
