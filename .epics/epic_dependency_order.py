"""Bounded, cycle-safe prerequisite ordering for epic hand-ins.

An NPC spawned by a quest action can make an earlier reward necessary to
acquire an item from that NPC.  This index records such dependencies once,
then uses visited-node reachability rather than recursively enumerating every
quest path.  It is intentionally conservative: cycles and ambiguous ordering
fall back to the input order.
"""
from __future__ import annotations

from collections import defaultdict, deque
from collections.abc import Iterable, Mapping


def _item(token: object) -> int | None:
    value = str(token or "")
    if value.startswith("item:") and value[5:].isdigit():
        return int(value[5:])
    return None


class ItemPrecedence:
    def __init__(self, by_from: Mapping[str, list[dict]]):
        # Index action prerequisites and rewards.  All processing is linear in
        # the edge count; no recursive graph expansion during construction.
        receives: dict[str, set[int]] = defaultdict(set)
        gives: dict[str, set[int]] = defaultdict(set)
        producers: dict[int, list[tuple[str, str]]] = defaultdict(list)
        spawn_sources: dict[str, set[str]] = defaultdict(set)
        for rows in by_from.values():
            for row in rows:
                rel = row.get("rel")
                source = str(row.get("group") or row.get("from") or "")
                if rel == "receives":
                    item = _item(row.get("to"))
                    if item is not None:
                        receives[source].add(item)
                elif rel in {"gives", "loots"}:
                    item = _item(row.get("to"))
                    if item is not None:
                        gives[source].add(item)
                        producers[item].append((source, str(row.get("from") or "").split("#", 1)[0]))
                elif rel == "triggers":
                    target = str(row.get("to") or "")
                    if target.endswith("#event_spawn"):
                        spawn_sources[target.removesuffix("#event_spawn")].add(
                            str(row.get("from") or "")
                        )

        # Item -> items that must precede it along a known acquisition path.
        self.dependencies: dict[int, set[int]] = defaultdict(set)
        for item, sources in producers.items():
            for source, actor in sources:
                self.dependencies[item].update(receives.get(source, ()))
                # NPC availability can itself be produced by an earlier hand-in.
                # Connect to the *reward* of the spawning action when there is
                # one (e.g. Omat's robe hand-in both grants Frozen Water and
                # spawns Natasha).  Other spawn origins are alternatives.
                for spawn_action in spawn_sources.get(actor, ()):
                    self.dependencies[item].update(gives.get(spawn_action, ()))
                    self.dependencies[item].update(receives.get(spawn_action, ()))
            self.dependencies[item].discard(item)
        self._cache: dict[tuple[int, int], int | None] = {}

    def distance(self, item: int, prerequisite: int, *, limit: int = 4096) -> int | None:
        if item == prerequisite:
            return None
        key = (item, prerequisite)
        if key in self._cache:
            return self._cache[key]
        pending = deque([(item, 0)])
        visited: set[int] = set()
        while pending and len(visited) < limit:
            node, depth = pending.popleft()
            if node in visited:
                continue
            visited.add(node)
            for needed in self.dependencies.get(node, ()):
                if needed == prerequisite:
                    self._cache[key] = depth + 1
                    return depth + 1
                if needed not in visited:
                    pending.append((needed, depth + 1))
        self._cache[key] = None
        return None

    def depends_on(self, item: int, prerequisite: int) -> bool:
        return self.distance(item, prerequisite) is not None

    def order(self, items: Iterable[int]) -> list[int]:
        remaining = list(dict.fromkeys(items))
        if len(remaining) < 2:
            return remaining
        # Prefer shorter causal paths when a large graph offers reciprocal
        # paths through alternate acquisition routes.  Equal evidence leaves
        # the original order unchanged.
        edges: dict[int, set[int]] = {item: set() for item in remaining}
        for i, a in enumerate(remaining):
            for b in remaining[i + 1:]:
                a_to_b = self.distance(a, b)
                b_to_a = self.distance(b, a)
                if a_to_b is not None and (b_to_a is None or a_to_b < b_to_a):
                    edges[a].add(b)
                elif b_to_a is not None and (a_to_b is None or b_to_a < a_to_b):
                    edges[b].add(a)
        result: list[int] = []
        while remaining:
            ready = next((v for v in remaining if not edges[v].intersection(remaining)), None)
            if ready is None:
                result.extend(remaining)
                break
            result.append(ready)
            remaining.remove(ready)
        return result


def opening_dialogue_actor(
    steps: list[str], by_from: Mapping[str, list[dict]]
) -> tuple[str, str, str] | None:
    """Find an opening hail for the first *productive* conversation.

    This is deliberately limited to the beginning of the acquisition path.
    Later NPC hails (such as Usbak's) must not replace the starter's hail.
    A purely narrative hail is not a mechanical prerequisite.
    """
    import re

    for step in steps:
        # A quest whose path starts with a loot acquisition or hand-in needs
        # the existing item-linked introductory-hail inference instead.
        if re.match(r"(?:Loot|Hand|Combine|Kill|Acquisition of)\b", step):
            break
        match = re.search(
            r'([a-z0-9_]+)/"([^"]+)", say "(?!Hail")[^"]+".*\bGives\b',
            step, re.I,
        )
        if not match:
            continue
        zone, npc = match.groups()
        source = f"{zone}/{npc.casefold()}#hail"
        speech = " ".join(
            str(row.get("text") or "")
            for row in by_from.get(source, ())
            if row.get("rel") == "speaks"
        ).strip()
        if speech:
            return zone, npc, speech
    return None
