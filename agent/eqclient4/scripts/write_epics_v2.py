#!/usr/bin/env python3
"""Independent, reward-seeded EverQuest epic walkthrough generator.

Required inputs: a quest_graph.jsonl and a class name. Uses the EQEmu data
caches for missing loot, merchants, and tradeskill sources. No prior walkthroughs
or v1/v2 renderer.

    python epic_writer_v2.py --graph quest_graph.jsonl --class cleric --out /tmp/epics

The generator deliberately distinguishes graph-proven steps from unresolved
prerequisites. It does not treat all dialogue at an NPC as a quest route.
"""

import argparse
import json
import re
from collections import defaultdict, deque
from dataclasses import dataclass, field
from pathlib import Path

from eqclient4.data.drops import ensure_drops
from eqclient4.data.merchants import ensure_merchants
from eqclient4.data.recipes import ensure_recipes

REWARDS: dict[str, dict] = {
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

_ITEM = re.compile(r"^item:(\d+)$")
_GUARD_ITEM = re.compile(r"(?:item\d*\s*=>\s*|item\d*\s*=\s*|check_hasitem\([^,]+,\s*)(\d+)")
_PERL_HANDIN_ITEM = re.compile(r"(?<![\w])([1-9]\d{2,})\s*=>\s*\d+")


def guard_item_ids(value: str) -> set[int]:
    return {int(x) for x in _GUARD_ITEM.findall(value)} | {
        int(x) for x in _PERL_HANDIN_ITEM.findall(value)
    }


def ident(value: str) -> str:
    return re.sub(r"[\s_]+", " ", value.strip()).casefold()


def actor_key(value: str) -> str:
    return "/".join(ident(v) for v in value.split("/", 1))


def actor_of(value: str) -> str:
    return value.split("#", 1)[0]


def label(value: str) -> str:
    zone, _, npc = actor_of(value).partition("/")
    return f'{zone}/"{npc.title()}"' if npc else value


def item_id(token: str) -> int | None:
    m = _ITEM.fullmatch(str(token))
    return int(m[1]) if m else None


@dataclass
class Step:
    key: str
    text: str
    actor: str = ""
    action: str = ""
    payload: tuple[int, ...] = ()
    utterance: str = ""
    group: str = ""
    evidence: list[str] = field(default_factory=list)
    produced_items: set[int] = field(default_factory=set)


class Graph:
    def __init__(self, graph: Path):
        self.items: dict[int, str] = {}
        self.item_sources: dict[int, tuple[str, ...]] = {}
        self.edges: list[dict] = []
        self.dialogues: dict[str, list[dict]] = defaultdict(list)
        self.says: dict[tuple[str, str], str] = {}
        self.world: dict[int, str] = {}
        self.by_group: dict[str, list[dict]] = defaultdict(list)
        self.by_from: dict[str, list[dict]] = defaultdict(list)
        self.by_to: dict[str, list[dict]] = defaultdict(list)
        self.producers: dict[int, list[dict]] = defaultdict(list)
        self.recipes: dict[str, list[dict]] = defaultdict(list)
        self.spawns: dict[str, list[dict]] = defaultdict(list)
        self.actor_spawns: dict[str, list[dict]] = defaultdict(list)
        self.numeric_dialogues: dict[str, list[dict]] = defaultdict(list)
        self.flag_setters: dict[str, list[dict]] = defaultdict(list)
        self.faction_gains: dict[str, list[dict]] = defaultdict(list)
        self.blocked_loot_npcs: set[tuple[str, int]] = set()
        self.blocked_loot_names: set[tuple[str, str]] = set()
        with graph.open(encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                row = json.loads(line)
                kind = row.get("kind")
                if kind == "item":
                    iid = int(row["item"])
                    self.items[iid] = str(row.get("name") or "")
                    self.item_sources[iid] = tuple(
                        str(source) for source in row.get("sources") or ()
                    )
                elif kind == "world":
                    self.world[int(row["id"])] = str(row.get("name") or "")
                elif kind == "dialogue":
                    key = actor_key(str(row.get("source") or ""))
                    self.dialogues[key].append(row)
                    if key.rsplit("/", 1)[-1].isdigit():
                        self.numeric_dialogues[key.split("/")[0]].append(row)
                elif kind == "say":
                    key = actor_key(f"{row.get('zone', '')}/{row.get('npc', '')}")
                    self.says[(key, ident(str(row.get("word") or "")))] = str(row.get("text") or "")
                elif kind == "edge":
                    self.edges.append(row)
                    src = str(row.get("from") or "")
                    dst = str(row.get("to") or "")
                    grp = str(row.get("group") or "")
                    rel = row.get("rel")
                    self.by_from[src].append(row)
                    self.by_to[dst].append(row)
                    if grp:
                        self.by_group[grp].append(row)
                    if rel in ("gives", "loots", "grounds", "produces"):
                        iid0 = item_id(dst)
                        if iid0 is not None:
                            self.producers[iid0].append(row)
                    if src.startswith("recipe:"):
                        self.recipes[src].append(row)
                    if rel == "sets" and row.get("flag"):
                        self.flag_setters[str(row["flag"])].append(row)
                    if rel == "sets" and row.get("faction") is not None:
                        self.faction_gains[str(row["faction"])].append(row)
                    if rel == "blocks_loot" and row.get("npc"):
                        zone = str(row.get("zone") or actor_of(src).split("/", 1)[0])
                        self.blocked_loot_npcs.add((zone, int(row["npc"])))
                        if row.get("name"):
                            self.blocked_loot_names.add((zone, ident(str(row["name"]))))
                    if rel == "spawns":
                        # Encounter edges can target a typed #event:spawned node.
                        npc = row.get("npc")
                        if npc:
                            self.spawns[f"npc:{int(npc)}"].append(row)
                        elif dst.startswith("npc:"):
                            self.spawns[dst].append(row)
                        self.actor_spawns[actor_key(actor_of(src))].append(row)

    def name(self, iid: int) -> str:
        name = self.items.get(iid) or f"Item {iid}"
        return f'"{name}" ({iid})'

    def group_rows(self, row: dict) -> list[dict]:
        grp = row.get("group")
        if not grp:
            return self.by_from.get(str(row.get("from") or ""), [])
        # Branch-specific edges carry `group`; event-level guard edges often
        # use `from=group` instead. Both belong to this same action.
        grouped = self.by_group.get(str(grp), ())
        direct = self.by_from.get(str(grp), ())
        return list({id(r): r for r in (*grouped, *direct)}.values())

    def inputs(self, row: dict) -> list[int]:
        return list(
            dict.fromkeys(
                iid
                for r in self.group_rows(row)
                if r.get("rel") == "receives"
                if (iid := item_id(r.get("to", ""))) is not None
            )
        )

    def needs(self, row: dict) -> tuple[list[int], list[str]]:
        items, flags = [], []
        for r in self.group_rows(row):
            if r.get("rel") != "needs":
                continue
            if (iid := item_id(r.get("to", ""))) is not None:
                if iid not in items:
                    items.append(iid)
            elif r.get("flag"):
                flags.append(str(r["flag"]))
        return items, list(dict.fromkeys(flags))

    def conversation(self, actor: str, needed: tuple[int, ...] = ()) -> list[dict]:
        key = actor_key(actor)
        direct = self.dialogues.get(key, [])
        if direct:
            return direct
        # Numeric NPC scripts: accept only a unique matching item guard in this zone.
        zone = key.split("/", 1)[0]
        matched = []
        for chain in self.numeric_dialogues.get(zone, []):
            for speech in chain.get("context_speech", []):
                guards = " ".join(map(str, speech.get("guards") or []))
                ids = guard_item_ids(guards)
                if needed and set(needed) == ids:
                    matched.append(chain)
                    break
        return matched if len(matched) == 1 else []

    def spoken(self, actor: str, word: str) -> bool:
        k = actor_key(actor)
        if (k, ident(word)) in self.says:
            return True
        return any(
            ident(t.get("input", "")) == ident(word)
            for c in self.conversation(actor)
            for t in c.get("turns", [])
        )


@dataclass(frozen=True)
class CatalogDrop:
    npc: int
    name: str
    zone: str
    chance: float


@dataclass(frozen=True)
class CatalogMerchant:
    npc: int
    name: str
    zone: str
    cost: int | None


@dataclass(frozen=True)
class CatalogRecipe:
    id: int
    components: tuple[tuple[int, int], ...]
    container: int
    name: str


class AcquisitionCatalog:
    """Normalize the EQEmu caches before their records reach the planner."""

    def __init__(
        self,
        drops: Path | None = None,
        merchants: Path | None = None,
        recipes: Path | None = None,
    ):
        self._drops = ensure_drops(path=str(drops) if drops else None)
        self._merchants = ensure_merchants(path=str(merchants) if merchants else None)
        self._recipes = ensure_recipes(path=str(recipes) if recipes else None)

    def drop(self, iid: int) -> CatalogDrop | None:
        row = self._drops.best(iid)
        if row is None:
            return None
        if isinstance(row, dict):
            return CatalogDrop(
                int(row["npc"]),
                str(row.get("name") or ""),
                str(row.get("where") or "?"),
                float(row["chance"]),
            )
        return CatalogDrop(
            int(row.npc_id),
            str(row.name or ""),
            str(row.zone or "?"),
            float(row.chance),
        )

    def merchant(self, iid: int) -> CatalogMerchant | None:
        found = self._merchants.best(iid)
        if found is None:
            return None
        if isinstance(found, tuple):
            row, cost = found
            return CatalogMerchant(int(row.npc_id), str(row.name or ""), str(row.zone or "?"), cost)
        return CatalogMerchant(
            int(found["npc"]),
            str(found.get("name") or ""),
            str(found.get("where") or "?"),
            None,
        )

    def recipe(self, iid: int) -> CatalogRecipe | None:
        row = self._recipes.for_item(iid)
        if row is None:
            return None
        if isinstance(row, dict):
            return CatalogRecipe(
                int(row["id"]),
                tuple((int(i), int(n)) for i, n in row["components"]),
                int(row.get("container") or 0),
                str(row.get("name") or ""),
            )
        return CatalogRecipe(
            int(row.id),
            tuple((int(i), int(n)) for i, n in row.components),
            int(row.container or 0),
            str(row.name or ""),
        )


_GUARD_TOKEN = re.compile(
    r"""\s*(?:e\.other:HasItem\(\s*(?P<item>\d+)\s*\)"""
    r"""|qglobals\[\s*["'](?P<flag>[A-Za-z0-9_]+)["']\s*\]\s*"""
    r"""(?P<comparison>==|>=|<=|>|<)\s*["']?(?P<value>-?\d+)["']?"""
    r"""|(?P<operator>\band\b|\bor\b)|(?P<paren>[()]))""",
    re.IGNORECASE,
)


def _guard_options(guard: str) -> list[list[tuple[str, str, str]]] | None:
    """DNF of a *fully recognized* Lua HasItem/flag Boolean expression.

    Return None rather than guessing when another predicate or Lua syntax occurs.
    """
    tokens: list[object] = []
    cursor = 0
    while cursor < len(guard):
        match = _GUARD_TOKEN.match(guard, cursor)
        if match is None:
            if not guard[cursor:].strip():
                break
            return None
        cursor = match.end()
        if match.group("item"):
            tokens.append(("item", match.group("item"), ""))
        elif match.group("flag"):
            tokens.append(
                (
                    "flag",
                    match.group("flag"),
                    match.group("comparison") + match.group("value"),
                )
            )
        else:
            tokens.append((match.group("operator") or match.group("paren")).lower())

    pos = 0

    def atom() -> list[list[tuple[str, str, str]]]:
        nonlocal pos
        if pos >= len(tokens):
            raise ValueError("incomplete expression")
        token = tokens[pos]
        pos += 1
        if token == "(":
            result = disjunction()
            if pos >= len(tokens) or tokens[pos] != ")":
                raise ValueError("unbalanced parentheses")
            pos += 1
            return result
        if isinstance(token, tuple):
            return [[token]]
        raise ValueError("unexpected token")

    def conjunction() -> list[list[tuple[str, str, str]]]:
        nonlocal pos
        clauses = atom()
        while pos < len(tokens) and tokens[pos] == "and":
            pos += 1
            right = atom()
            clauses = [a + b for a in clauses for b in right]
            if len(clauses) > 32:
                raise ValueError("too many alternatives")
        return clauses

    def disjunction() -> list[list[tuple[str, str, str]]]:
        nonlocal pos
        clauses = conjunction()
        while pos < len(tokens) and tokens[pos] == "or":
            pos += 1
            clauses.extend(conjunction())
            if len(clauses) > 32:
                raise ValueError("too many alternatives")
        return clauses

    try:
        result = disjunction()
    except ValueError:
        return None
    return result if pos == len(tokens) and len(result) > 1 else None


class AcquisitionCycle(Exception):
    """A candidate depends on an item already on the acquisition stack."""


class Planner:
    def __init__(self, graph: Graph, catalog: AcquisitionCatalog):
        self.g = graph
        self.catalog = catalog
        self.steps: list[Step] = []
        self.emitted: set[str] = set()
        self.active_items: set[int] = set()
        self.done_items: set[int] = set()
        self.active_events: set[str] = set()
        self.errors: list[str] = []
        self.used_edges: set[int] = set()
        self.active_flags: set[tuple[str, str]] = set()
        self.done_flags: set[tuple[str, str]] = set()
        # Track current values: a later event can overwrite an earlier stage.
        self.flag_values: dict[str, str] = {}

    def put(
        self,
        key: str,
        text: str,
        *,
        actor: str = "",
        action: str = "",
        payload: tuple[int, ...] = (),
        utterance: str = "",
        group: str = "",
        produced_items: tuple[int, ...] = (),
    ) -> None:
        if key not in self.emitted:
            self.emitted.add(key)
            self.steps.append(
                Step(
                    key,
                    text,
                    actor,
                    action,
                    payload,
                    utterance,
                    group,
                    produced_items=set(produced_items),
                )
            )
            return

        # An existing step can acquire additional rewards via the same action.
        if produced_items:
            next(step for step in self.steps if step.key == key).produced_items.update(
                produced_items
            )

        # A spawn/signal traversal may emit a hand-in before its reward is
        # discovered. Preserve the same action, but enrich it with graph gifts.
        if key.startswith("hand:") and ". Gives " in text:
            existing = next(step for step in self.steps if step.key == key)
            reward = text.split(". Gives ", 1)[1].rstrip(".")
            if ". Gives " not in existing.text:
                existing.text = existing.text.rstrip(".") + ". Gives " + reward + "."
            else:
                prefix, current = existing.text.split(". Gives ", 1)
                rewards = current.rstrip(".").split(" + ")
                if reward not in rewards:
                    existing.text = prefix + ". Gives " + " + ".join((*rewards, reward)) + "."
            if payload and not existing.payload:
                existing.payload = payload

    def eligible_producer(self, row: dict, iid: int) -> bool:
        """Reject producers that cannot establish an independent acquisition."""
        rel = row.get("rel")
        if rel == "gives" and iid in self.g.inputs(row):
            return False
        if rel != "loots":
            return True
        if str(row.get("name") or "").lower() == "needs heading validation" and any(
            source.startswith("loot:") for source in self.g.item_sources.get(iid, ())
        ):
            return False
        if row.get("npc") and not row.get("reachable"):
            zone = actor_of(str(row.get("from") or "")).split("/", 1)[0]
            return (zone, int(row["npc"])) not in self.g.blocked_loot_npcs
        return True

    def producer_rank(self, row: dict, iid: int) -> tuple[int, int, str]:
        """Order eligible graph routes without deciding their eligibility."""
        rel = row.get("rel")
        inputs = self.g.inputs(row) if rel == "gives" else []
        if rel == "produces":
            inputs = [
                item_id(r.get("to", "")) or 0
                for r in self.g.recipes.get(row.get("from", ""), [])
                if r.get("rel") == "consumes"
            ]
        group = str(row.get("group") or "")
        other_gifts = sum(
            r.get("rel") == "gives" and r.get("to") != f"item:{iid}" for r in self.g.group_rows(row)
        )
        priority = (
            0
            if rel == "gives" and "#hand:" in group and not other_gifts
            else (
                1
                if rel == "gives" and not other_gifts
                else (
                    2 if rel == "gives" else 3 if rel == "produces" else 4 if rel == "loots" else 5
                )
            )
        )
        return (
            100 if iid in inputs else priority,
            len(inputs),
            str(row.get("from", "")),
        )

    def candidates(self, iid: int) -> list[dict]:
        return sorted(
            (row for row in self.g.producers.get(iid, ()) if self.eligible_producer(row, iid)),
            key=lambda row: self.producer_rank(row, iid),
        )

    def candidate(self, iid: int) -> dict | None:
        """First-ranked producer, for inspection; acquisition tries alternatives."""
        return next(iter(self.candidates(iid)), None)

    def _restore(self, snapshot: tuple) -> None:
        mark, prior_steps, emitted, done, events, used, flags, values, errors_len = snapshot
        del self.steps[mark:]
        for step, text, payload, produced in prior_steps:
            step.text, step.payload = text, payload
            step.produced_items = produced
        self.emitted = emitted
        self.done_items = done
        self.active_events = events
        self.used_edges = used
        self.done_flags = flags
        self.flag_values = values
        del self.errors[errors_len:]

    def _snapshot(self) -> tuple:
        return (
            len(self.steps),
            [(step, step.text, step.payload, step.produced_items.copy()) for step in self.steps],
            self.emitted.copy(),
            self.done_items.copy(),
            self.active_events.copy(),
            self.used_edges.copy(),
            self.done_flags.copy(),
            self.flag_values.copy(),
            len(self.errors),
        )

    def graph_acquire(self, iid: int) -> tuple[bool, list[str]]:
        """Try causally connected graph routes, restoring state on failed branches."""
        rejected: list[str] = []

        # Spell: Summon Orb is itself earned from a quest graph. Prefer that
        # causal chain to unrelated direct drops of Orb of Mastery.
        for source in self.g.item_sources.get(iid, ()):
            if not source.startswith("spell:"):
                continue
            spell = source.partition(":")[2]
            scroll = next(
                (
                    sid
                    for sid, name in self.g.items.items()
                    if name.casefold() == ("Spell: " + spell).casefold()
                ),
                None,
            )
            if scroll is None or scroll == iid or not self.g.producers.get(scroll):
                continue
            snapshot = self._snapshot()
            try:
                self.acquire(scroll)
                self.put(
                    f"summon-spell:{iid}:{scroll}",
                    f'Learn {self.g.name(scroll)} and cast "{spell}" to summon {self.g.name(iid)}.',
                    produced_items=(iid,),
                )
                return True, rejected
            except AcquisitionCycle as cycle:
                self._restore(snapshot)
                rejected.append(str(cycle))

        for row in self.candidates(iid):
            snapshot = self._snapshot()
            try:
                rel = row.get("rel")
                if rel == "gives":
                    self.giver(row, iid)
                elif rel == "produces":
                    self.recipe(row, iid)
                elif rel in ("loots", "grounds"):
                    self.loot(row, iid)
                else:
                    continue
                return True, rejected
            except AcquisitionCycle as cycle:
                self._restore(snapshot)
                rejected.append(str(cycle))
        return False, rejected

    def acquire(self, iid: int) -> None:
        if iid in self.done_items:
            return
        if iid in self.active_items:
            raise AcquisitionCycle(self.g.name(iid))
        self.active_items.add(iid)
        try:
            found, rejected = self.graph_acquire(iid)
            if not found:
                # Independent catalog acquisition is considered exactly once,
                # whether the graph has no producers or all of them cycle.
                found = self.catalog_acquire(iid)
            if not found:
                reason = f"{self.g.name(iid)}: no graph or catalog acquisition route"
                if rejected:
                    reason += f" (graph route rejected: {rejected[0]})"
                raise AcquisitionCycle(reason)
            self.done_items.add(iid)
        finally:
            self.active_items.remove(iid)

    def catalog_acquire(self, iid: int) -> bool:
        """Independent sources only: item metadata, drops, merchants, recipes."""
        sources = self.g.item_sources.get(iid, ())
        # Non-loot item metadata is generally more specific than a random mob
        # drop. Collect candidates once; don't run two source passes.
        by_kind: dict[str, list[str]] = defaultdict(list)
        for source in sources:
            kind, sep, value = source.partition(":")
            if sep and value and value not in by_kind[kind]:
                by_kind[kind].append(value)

        for kind in ("forage", "fishing", "ground", "spell"):
            values = by_kind.get(kind, [])
            if not values:
                continue
            if kind in ("forage", "fishing", "ground"):
                verb = {
                    "forage": "Forage",
                    "fishing": "Fish for",
                    "ground": "Collect ground spawn",
                }[kind]
                text = (
                    f"{verb} {self.g.name(iid)} in "
                    + " or ".join(f"`{zone}`" for zone in values)
                    + "."
                )
            else:
                text = (
                    f"Summon {self.g.name(iid)} by casting "
                    + " or ".join(f'"{name}"' for name in values)
                    + "."
                )
            self.put(f"item-source:{kind}:{iid}", text, produced_items=(iid,))
            return True

        drop = self.catalog.drop(iid)
        if drop:
            npc, name, zone, chance = drop.npc, drop.name, drop.zone, drop.chance
            if (zone, npc) not in self.g.blocked_loot_npcs:
                self.put(
                    f"catalog-drop:{iid}",
                    f'Loot {self.g.name(iid)} from "{name or f"NPC {npc}"}" '
                    f"(NPC {npc}) in `{zone}`. Drop cache: {chance:g}% chance per kill.",
                    produced_items=(iid,),
                )
                return True

        seller = self.catalog.merchant(iid)
        if seller:
            npc, name, zone, cost = seller.npc, seller.name, seller.zone, seller.cost
            cost_text = f" Base price: {cost:,} copper." if cost else ""
            self.put(
                f"catalog-merchant:{iid}",
                f'Buy {self.g.name(iid)} from "{name}" (NPC {npc}) in `{zone}`.{cost_text}',
                produced_items=(iid,),
            )
            return True

        recipe = self.catalog.recipe(iid)
        if recipe:
            rid, parts, container, skill = (
                recipe.id,
                recipe.components,
                recipe.container,
                recipe.name,
            )
            if iid not in (component for component, _ in parts):
                snapshot = self._snapshot()
                try:
                    for component, _count in parts:
                        self.acquire(component)
                    inputs = ", ".join(
                        self.g.name(x) + (f" x{n}" if n != 1 else "") for x, n in parts
                    )
                    extra = f" Requires {skill}." if skill else ""
                    self.put(
                        f"catalog-recipe:{rid}:{iid}",
                        f"Combine recipe {rid} (container {container}): {inputs}. "
                        f"Produces {self.g.name(iid)}.{extra}",
                        produced_items=(iid,),
                    )
                    return True
                except AcquisitionCycle:
                    self._restore(snapshot)

        # The graph's item-source hints are an independent fallback, not a
        # producer edge. Filter out sources explicitly blocked by scripts.
        loot = [
            value
            for value in by_kind.get("loot", [])
            if (value.partition("@")[2], ident(value.partition("@")[0]))
            not in self.g.blocked_loot_names
        ]
        if loot:
            places = []
            for value in loot:
                n1, _, z1 = value.partition("@")
                places.append(f'"{n1}"' + (f" in `{z1}`" if z1 else ""))
            self.put(
                f"item-source:loot:{iid}",
                f"Loot {self.g.name(iid)} from " + " or ".join(places) + ".",
                produced_items=(iid,),
            )
            return True
        return False

    def has_connected_intro(self, root: int) -> bool:
        """Bounded search for a quest-starting hand-in reachable from an item.

        Used only to order independent inputs at a multi-item hand-in. An
        event-spawn link to an NPC with a matching introductory hail is
        stronger evidence of quest origin than arbitrary item numbering.
        """
        pending = deque([root])
        seen: set[int] = set()
        while pending and len(seen) < 256:
            iid = pending.popleft()
            if iid in seen:
                continue
            seen.add(iid)
            for row in self.g.producers.get(iid, ()):
                src = str(row.get("from") or "")
                if "#signal:" in src:
                    arrival = actor_of(src) + "#event_spawn"
                    for trigger in self.g.by_to.get(arrival, ()):
                        if trigger.get("rel") != "triggers":
                            continue
                        initiator = str(trigger.get("from") or "")
                        if "#hand:" not in initiator:
                            continue
                        speech = self.g.says.get(
                            (actor_key(actor_of(initiator)), "hail"), ""
                        ).casefold()
                        for needed in self.g.by_group.get(initiator, ()):
                            if needed.get("rel") != "receives":
                                continue
                            token = item_id(needed.get("to", ""))
                            if token is None:
                                continue
                            keywords = [
                                w
                                for w in re.findall(r"[a-z]{5,}", self.g.name(token).casefold())
                                if w not in {"great", "water", "item", "lord"}
                            ]
                            if keywords and any(w in speech for w in keywords):
                                return True
                pending.extend(x for x in self.g.inputs(row) if x not in seen)
                if src.startswith("recipe:"):
                    pending.extend(
                        x
                        for r in self.g.recipes.get(src, ())
                        if r.get("rel") == "consumes"
                        if (x := item_id(r.get("to", ""))) is not None and x not in seen
                    )
        return False

    def faction_requirements(self, row: dict) -> None:
        """Explain explicit faction gates without pretending a single gain meets them.

        The graph has threshold checks and individual faction gains, but does
        not carry the player's current faction or repeat counts. Keep these
        requirements visible rather than declaring them acquired.
        """
        requirements = [
            (str(r["faction"]), str(r.get("at") or "set"))
            for r in self.g.group_rows(row)
            if r.get("rel") == "needs" and r.get("faction") is not None
        ]
        for faction, at in dict.fromkeys(requirements):
            key = f"faction-need:{faction}:{at}"
            self.put(key, f"**Faction:** `{faction}` `{at}` required. Progress unverified.")

    def _satisfies_flag(self, name: str, at: str) -> bool:
        value = self.flag_values.get(name)
        if at == "unset":
            return value is None
        if value is None:
            return False
        if at == "set":
            return True
        match = re.fullmatch(r"(==|>=|>|<=|<)\s*(-?\d+)", at)
        if match and value.lstrip("-").isdigit():
            op, target = match[1], int(match[2])
            actual = int(value)
            return {
                "==": actual == target,
                ">=": actual >= target,
                ">": actual > target,
                "<=": actual <= target,
                "<": actual < target,
            }[op]
        return at.startswith("==") and value == at[2:].strip()

    def action_requirements(self, row: dict) -> None:
        """Satisfy the requirements on one action, including ungrouped guards."""
        rows = self.g.group_rows(row)
        for iid in dict.fromkeys(
            value
            for r in rows
            if r.get("rel") == "needs"
            if (value := item_id(r.get("to", ""))) is not None
        ):
            self.acquire(iid)
        conditions: dict[str, list[str]] = defaultdict(list)
        for r in rows:
            if r.get("rel") == "needs" and r.get("flag"):
                conditions[str(r["flag"])].append(str(r.get("at") or "set"))
        for name, guards in conditions.items():
            for at in dict.fromkeys(g for g in guards if g != "set"):
                self.flag(name, at)
            if all(g == "set" for g in guards):
                self.flag(name, "set")
        self.faction_requirements(row)

    def action_sets(self, row: dict) -> None:
        """Apply quest-state mutations only after the action has executed."""
        for r in self.g.group_rows(row):
            if r.get("rel") == "sets" and r.get("flag") and r.get("value") is not None:
                if not all(
                    self._satisfies_flag(str(need["flag"]), str(need["at"]))
                    for need in r.get("post_write_needs", ())
                ):
                    continue
                self.flag_values[str(r["flag"])] = str(r["value"])
                self.done_flags.add((str(r["flag"]), "==" + str(r["value"])))

    def giver(self, row: dict, iid: int) -> None:
        src = str(row.get("from") or "")
        group = str(row.get("group") or src)
        ins = self.g.inputs(row)
        if len(ins) > 1:
            position = {v: i for i, v in enumerate(ins)}
            ins.sort(key=lambda x: (not self.has_connected_intro(x), position[x]))
        for required in ins:
            self.acquire(required)
        self.action_requirements(row)
        actor = actor_of(src)
        if ins:
            rendered = " + ".join(self.g.name(x) for x in ins)
            self.put(
                f"hand:{group}",
                f"{label(actor)}, hand {rendered}. Gives {self.g.name(iid)}.",
                actor=actor,
                action="hand",
                payload=tuple(ins),
                group=group,
                produced_items=(iid,),
            )
        else:
            word = (
                group.split("#", 2)[1]
                if "#" in group
                else (src.rsplit("#", 1)[-1] if "#" in src else "")
            )
            if word.startswith("event_") or word.startswith("timer:"):
                word = ""
            if word.lower().startswith("event_") or word.lower().startswith("signal:"):
                self.event(src)
                self.put(
                    f"give:{group}:{iid}",
                    f"{label(actor)} produces {self.g.name(iid)} on `{src}`.",
                    actor=actor,
                    produced_items=(iid,),
                )
            else:
                self.put(
                    f"say:{group}",
                    f'{label(actor)}, say "{word.title()}". Gives {self.g.name(iid)}.',
                    actor=actor,
                    action="say",
                    utterance=word,
                    group=group,
                    produced_items=(iid,),
                )
        self.action_sets(row)

    def setter_requirements(self, setter: dict) -> None:
        """Resolve only a flag setter's alternatives, not arbitrary reward paths.

        This retains the old planner's behavior for ordinary acquisitions.
        Each failed alternative is rolled back before the next is tried.
        """
        rows = [r for r in self.g.group_rows(setter) if r.get("rel") == "needs"]
        alternatives: dict[str, list[list[tuple[str, str, str]]]] = {}
        covered: set[tuple[str, str, str]] = set()

        def requirement(row: dict) -> tuple[str, str, str] | None:
            iid = item_id(row.get("to", ""))
            if iid is not None:
                return ("item", str(iid), "")
            if row.get("flag"):
                at = str(row.get("at") or "set")
                if re.fullmatch(r"-?\d+", at):
                    at = "==" + at
                return ("flag", str(row["flag"]), at)
            return None

        # Explicit OR edges already emitted for simpler Lua comparisons.
        for row in rows:
            if row.get("op") != "or":
                continue
            key = str(row.get("or_group") or row.get("group") or row.get("from"))
            term = requirement(row)
            if term is not None:
                alternatives.setdefault(key, []).append([term])
                covered.add(term)

        # Mixed AND/OR guards require parenthesized alternatives (e.g.
        # (weapon A and weapon B) or (weapon C and weapon D) or prequest).
        # The speech guard is source evidence; accept it only if every atom
        # matches a flattened need on this *specific setter* branch.
        available = {term for row in rows if (term := requirement(row)) is not None}
        for speech in self.g.by_from.get(str(setter.get("from") or ""), ()):
            if speech.get("rel") != "speaks":
                continue
            for guard in speech.get("guards") or ():
                options = _guard_options(str(guard))
                if options is None or not any(len(choice) > 1 for choice in options):
                    continue
                atoms = {term for choice in options for term in choice}
                if not atoms.issubset(available) or atoms & covered:
                    continue
                key = f"mixed:{setter.get('from')}:{sorted(atoms)}"
                alternatives[key] = options
                covered.update(atoms)

        def satisfy(term: tuple[str, str, str]) -> None:
            kind, name, at = term
            if kind == "item":
                self.acquire(int(name))
            else:
                self.flag(name, at)
                if not (self._satisfies_flag(name, at) or (name, at) in self.done_flags):
                    raise AcquisitionCycle(f"Unverified alternative `{name}` {at}")

        seen: set[tuple[str, str, str]] = set()
        for row in rows:
            term = requirement(row)
            if term is not None and term not in covered and term not in seen:
                seen.add(term)
                satisfy(term)

        for key, choices in alternatives.items():
            failures = []
            for choice in choices:
                snapshot = self._snapshot()
                try:
                    for term in choice:
                        satisfy(term)
                    break
                except AcquisitionCycle as error:
                    self._restore(snapshot)
                    failures.append(str(error))
            else:
                raise AcquisitionCycle(
                    f"No proven setter alternative for `{key}`: " + "; ".join(failures)
                )
        self.faction_requirements(setter)

    def flag(self, name: str, at: str) -> None:
        # Encounter guards may encode a numeric comparison as a bare value.
        # A requirement at="1" is equality, not an unknown predicate.
        at = at.strip()
        if re.fullmatch(r"-?\d+", at):
            at = "==" + at
        if self._satisfies_flag(name, at) or (name, at) in self.done_flags:
            return
        if at == "unset":
            raise AcquisitionCycle(f"quest flag `{name}` must be unset")
        state = (name, at)
        if state in self.active_flags:
            raise AcquisitionCycle(f"quest flag `{name}` {at}: recursive setter")
        self.active_flags.add(state)
        try:
            setters = self.g.flag_setters.get(name, [])

            def valid(row: dict) -> bool:
                val = str(row.get("value") or "")
                if at == "set":
                    return True
                match = re.fullmatch(r"(==|>=|>|<=|<)\s*(-?\d+)", at)
                if match and val.lstrip("-").isdigit():
                    actual, target = int(val), int(match[2])
                    return {
                        "==": actual == target,
                        ">=": actual >= target,
                        ">": actual > target,
                        "<=": actual <= target,
                        "<": actual < target,
                    }[match[1]]
                return at.startswith("==") and val == at[2:].strip()

            comparison = re.fullmatch(r"(==|>=|>|<=|<)\s*(-?\d+)", at)

            def cmp(r: dict) -> tuple[int, int, int, str]:
                # A >= N prerequisite must establish N before attempting
                # later stages whose hand-ins may themselves require N.
                # Ranking hand-ins first previously selected stage 17 for
                # >=16, recursively depending on the same prerequisite.
                output = [0, 0, 0, ""]

                value = str(r.get("value") or "")

                if comparison and comparison[1] in (">=", ">"):
                    output[0] = int(value)

                if "#hand:" not in str(r.get("from") or ""):
                    output[1] = 1

                if value.isdigit():
                    output[2] = int(str(r.get("value") or ""))

                output[3] = str(r.get("from") or "")

                return tuple(output)  # type: ignore

            setters = sorted((r for r in setters if valid(r)), key=cmp)
            for setter in setters:
                snapshot = self._snapshot()
                src = str(setter.get("from") or "")
                # Guard and setter edges sometimes have no `group` attribute.
                # Resolve the specific branch that contains this mutation.
                try:
                    for requirement in setter.get("post_write_needs", ()):
                        self.flag(str(requirement["flag"]), str(requirement["at"]))
                    self.setter_requirements(setter)
                    if "#hand:" in src:
                        self.hand_event(src, resolve=False)
                    elif "#recipe:" in src:
                        recipe_id = "recipe:" + src.rsplit("#recipe:", 1)[1]
                        for rr in self.g.recipes.get(recipe_id, []):
                            if rr.get("rel") == "consumes":
                                iid = item_id(rr.get("to", ""))
                                if iid is not None:
                                    self.acquire(iid)
                        self.put(
                            "flag:" + src,
                            f'Combine recipe {recipe_id} to set `{name}` to `{setter.get("value")}`.',
                        )
                    elif "#" in src:
                        word = src.split("#", 1)[1]
                        if word.startswith("event_"):
                            self.event(src)
                        else:
                            self.put(
                                "flag:" + src,
                                f'{label(actor_of(src))}, say "{word.title()}". Sets `{name}` to `{setter.get("value")}`.',
                                actor=actor_of(src),
                                action="say",
                                utterance=word,
                            )
                    else:
                        raise AcquisitionCycle(f"cannot execute flag setter `{src}`")
                    self.action_sets(setter)
                    if not self._satisfies_flag(name, at):
                        raise AcquisitionCycle(f"setter `{src}` failed to establish `{name}` {at}")
                    return
                except AcquisitionCycle:
                    self._restore(snapshot)
            # Preserve the rest of the route when the graph cannot establish
            # this prerequisite, but never claim the flag was acquired.
            self.errors.append(f"Unverified quest flag `{name}` {at}: no acyclic setter")
            self.put(
                f"unverified-flag:{name}:{at}",
                f"**Unverified quest flag:** `{name}` `{at}` required.",
            )
        finally:
            self.active_flags.remove(state)

    def recipe(self, row: dict, iid: int) -> None:
        src = str(row.get("from") or "")
        rows = self.g.recipes.get(src, [])
        consume = [
            int(v)
            for r in rows
            if r.get("rel") == "consumes"
            if (v := item_id(r.get("to", ""))) is not None and v != iid
        ]
        containers = [
            item_id(r.get("to", "")) or 0
            for r in rows
            if r.get("rel") == "container" and item_id(r.get("to", "")) is not None
        ]
        for x in dict.fromkeys(containers + consume):
            self.acquire(x or 0)

        container = (
            self.g.name(containers[0] or 0) if containers else "appropriate tradeskill container"
        )
        parts = ", ".join(self.g.name(v) for v in consume)
        skill = next((str(r.get("skill_name")) for r in rows if r.get("skill_name")), "")
        desc = f"Combine in {container}: {parts}. Produces {self.g.name(iid)}."
        if skill:
            desc += f" Requires {skill}."
        self.put(f"recipe:{src}:{iid}", desc, produced_items=(iid,))

    def loot(self, row: dict, iid: int) -> None:
        src = str(row.get("from") or "")
        name = str(row.get("name") or "")
        npc = row.get("npc")
        self.action_requirements(row)
        if "#hand:" in src:
            self.hand_event(src, target_npc=npc)
        elif "#" in src:
            self.event(src, target_npc=npc)
        self.action_sets(row)
        if row.get("rel") == "grounds":
            self.put(
                f"ground:{src}:{iid}",
                f"Collect {self.g.name(iid)} at `{src}`.",
                produced_items=(iid,),
            )
            return
        place = actor_of(src).split("/", 1)[0]
        if npc and (place, int(npc)) in self.g.blocked_loot_npcs and not row.get("reachable"):
            self.errors.append(f"Loot {iid} from NPC {npc} conflicts with ClearItemList in {place}")
            return
        target = name or (f"NPC {npc}" if npc else actor_of(src).split("/", 1)[-1])
        if npc:
            # Treasure chests and world objects are opened, not killed.
            verb = (
                "Open"
                if any(x in target.casefold() for x in ("chest", "coffer", "cache", "treasure"))
                else "Kill"
            )
            self.put(
                f"kill-loot:{src}:{iid}",
                f'{verb} "{target}" (NPC {npc}) in `{place}` and loot {self.g.name(iid)}.',
                produced_items=(iid,),
            )
        else:
            self.put(
                f"loot:{src}:{iid}",
                f'Loot {self.g.name(iid)} from "{target}" in `{place}`.',
                produced_items=(iid,),
            )

    def event(self, node: str, target_npc: int | None = None) -> None:
        if node in self.active_events:
            self.errors.append(f"Event cycle at `{node}`")
            return
        key = f"event:{node}"
        if key in self.emitted:
            return
        self.active_events.add(node)
        try:
            if node.endswith("#hail"):
                self.put(
                    f"hail:{node}",
                    f'{label(actor_of(node))}, say "Hail".',
                    actor=actor_of(node),
                    action="say",
                    utterance="hail",
                )
            if "#signal:" in node:
                # An NPC must have been spawned before receiving its signal.
                self.pre_spawned_actor(actor_of(node))
            if "#hand:" in node:
                self.hand_event(node)
            # Triggers arriving at the same signal number are OR, not AND.
            # A repeated signal can be sent by its initial player action and
            # later by the deaths of mobs it spawned. Following every incoming
            # edge turns this normal event loop into a false dependency cycle.
            incoming = [r for r in self.g.by_to.get(node, []) if r.get("rel") == "triggers"]
            if "#signal:" in node and incoming:
                # Favor explicit player-started routes; then other routes that
                # do not immediately revisit an active event. Do not assert
                # that *all* signal senders must execute to receive a signal.
                reachable = [
                    r for r in incoming if str(r.get("from") or "") not in self.active_events
                ]
                incoming = sorted(
                    reachable,
                    key=lambda r: (
                        (
                            0
                            if "#event_say" in str(r.get("from", ""))
                            else (
                                1
                                if "#hand:" in str(r.get("from", ""))
                                else (2 if "#event_spawn" in str(r.get("from", "")) else 3)
                            )
                        ),
                        str(r.get("from", "")),
                    ),
                )[:1]
                if not incoming:
                    self.errors.append(f"No acyclic signal predecessor for `{node}`")
            for edge in sorted(incoming, key=lambda r: str(r.get("from", ""))):
                parent = str(edge.get("from") or "")
                if edge.get("action") == "signal_count":
                    self.event(parent)
                    counter = str(edge["counter"])
                    count = int(edge["count"])
                    additional = int(edge["additional_signals"])
                    self.put(
                        f"signal-count:{node}",
                        f"Advance `{counter}` to {count} by receiving signal "
                        f"{edge['signal']} {additional} additional time(s). "
                        "The triggering action(s) must be verified from the encounter.",
                    )
                elif edge.get("action") == "defeat_wave":
                    self.event(parent)
                    wave = int(edge["wave"])
                    count = int(edge["required_kills"])
                    self.put(
                        f"wave:{parent}:{count}",
                        f"Defeat the {count} encounter enemies in wave {wave} "
                        + (
                            "to complete the trial."
                            if "#wave_complete:" in node
                            else f"before wave {wave + 1} can proceed."
                        ),
                    )
                elif edge.get("action") == "say":
                    who = actor_of(parent)
                    self.put(
                        f"say:{parent}",
                        f'{label(who)}, say "{edge["keyword"]}".',
                        actor=who,
                        action="say",
                        utterance=str(edge["keyword"]),
                    )
                elif parent.endswith("#event_say"):
                    # The source records an event, not necessarily the exact
                    # player utterance. Do not fabricate a keyword.
                    self.put(
                        f"talk:{parent}",
                        f"Talk to {label(actor_of(parent))} to trigger the encounter.",
                    )
                elif "#hand:" in parent:
                    self.hand_event(parent, target_npc=target_npc)
                elif "#event_death" in parent:
                    # Some death events require a previously spawned NPC.
                    self.pre_spawned_actor(actor_of(parent))
                    self.put(f"kill:{parent}", f"Kill {label(actor_of(parent))}.")
                else:
                    self.event(parent)
            # If no trigger points to a signal, the graph may still contain the
            # event itself; render it but do not fabricate its origin.
            for r in self.g.by_from.get(node, []):
                # Runtime-selected spawns are alternatives, not an instruction
                # to kill every NPC in a wave.
                if "#event:wave:" in node and target_npc is None:
                    continue
                if r.get("rel") == "spawns" and (
                    target_npc is None
                    or r.get("npc") == target_npc
                    or str(r.get("to")) == f"npc:{target_npc}"
                ):
                    self.put(
                        f'spawn:{node}:{r.get("to")}',
                        f'Spawns "{r.get("name") or r.get("to")}" ({r.get("to")}) '
                        f"via `{node}`.",
                    )
            self.emitted.add(key)
        finally:
            self.active_events.remove(node)

    def hand_event(
        self, group: str, target_npc: int | None = None, *, resolve: bool = True
    ) -> None:
        rows = self.g.group_rows({"group": group})
        if rows and resolve:
            self.action_requirements({"group": group})
        ins = list(
            dict.fromkeys(
                iid
                for r in rows
                if r.get("rel") == "receives"
                if (iid := item_id(r.get("to", ""))) is not None
            )
        )
        for x in ins:
            self.acquire(x)
        if ins:
            self.put(
                f"hand:{group}",
                f"{label(actor_of(group))}, hand " + " + ".join(self.g.name(x) for x in ins) + ".",
                actor=actor_of(group),
                action="hand",
                payload=tuple(ins),
                group=group,
            )
        self.action_sets({"group": group})
        # Spawn edges often have `from=group` but no `group` property.
        # Index both shapes rather than relying on by_group alone.
        for r in self.g.by_from.get(group, []):
            if (
                r.get("rel") == "spawns"
                and target_npc is not None
                and str(r.get("to")) == f"npc:{target_npc}"
            ):
                self.put(
                    f'spawn:{group}:{r.get("to")}',
                    f'Spawns "{r.get("name") or r.get("to")}" ({r.get("to")}) '
                    f"after the hand-in.",
                )

    def pre_spawned_actor(self, actor: str) -> None:
        # Search the trigger chain for the actor's event_spawn rather than
        # inventing a required spawn merely because an NPC has a database ID.
        target = actor_key(actor) + "#event_spawn"
        for edge in self.g.by_to.get(target, []):
            if edge.get("rel") == "triggers":
                from_node = str(edge.get("from") or "")
                if "#hand:" in from_node:
                    self.hand_event(from_node, target_npc=edge.get("npc"))
                else:
                    self.event(from_node)

        # Encounter Lua uses typed NPC spawn nodes, not old #event_spawn IDs.
        match = re.search(r"/npc:(\d+)$", actor_key(actor))
        if match:
            npc = int(match.group(1))
            candidates = [
                r
                for r in self.g.spawns.get(f"npc:{npc}", ())
                if str(r.get("from", "")).startswith(actor.split("/", 1)[0] + "/")
            ]
            # Alternative spawn paths are OR, never AND.
            if candidates:
                source = str(sorted(candidates, key=lambda r: str(r["from"]))[0]["from"])
                if source not in self.active_events:
                    self.event(source)

    def introduce(self) -> None:
        if not self.steps:
            return
        # A productive initial SAY is the most reliable introduction (Telin).
        productive = next(
            (
                s
                for s in self.steps
                if s.action == "say"
                and s.actor
                and s.utterance.casefold() != "hail"
                and self.g.spoken(s.actor, "hail")
            ),
            None,
        )
        if productive:
            chosen = productive.actor
        else:
            chosen = ""
            for step in self.steps:
                if not step.actor or not self.g.spoken(step.actor, "hail"):
                    continue
                # Prefer an introductory hail that actually mentions the item
                # handed to this NPC, not a random late NPC greeting.
                speech = self.g.says.get((actor_key(step.actor), "hail"), "")
                if not speech:
                    for chain in self.g.conversation(step.actor):
                        for turn in chain.get("turns", []):
                            if ident(str(turn.get("input"))) == "hail":
                                speech += " ".join(
                                    str(x.get("text") or "") for x in turn.get("reply", [])
                                )
                words = {
                    w
                    for iid in step.payload
                    for w in re.findall(r"[a-z]{5,}", self.g.name(iid).lower())
                    if w not in {"water", "great", "item", "lord"}
                }
                if words and any(w in speech.casefold() for w in words):
                    chosen = step.actor
                    break
        if not chosen:
            return
        hail = Step(
            "introduction:" + actor_key(chosen),
            f'{label(chosen)}, say "Hail".',
            actor=chosen,
            action="say",
            utterance="hail",
        )
        if all(
            not (s.actor == chosen and s.action == "say" and ident(s.utterance) == "hail")
            for s in self.steps
        ):
            self.steps.insert(0, hail)

    def plan(self, reward: int) -> list[Step]:
        try:
            self.acquire(reward)
        except AcquisitionCycle as exc:
            self.errors.append(f"No acyclic acquisition route: {exc}")
        self.introduce()
        return self.steps


def speech_for_step(g: Graph, step: Step) -> list[str]:
    if not step.actor or step.action not in ("hand", "say"):
        return []
    chains = g.conversation(step.actor, step.payload)
    result: list[str] = []
    if step.action == "say":
        for chain in chains:
            for turn in chain.get("turns", []):
                if ident(str(turn.get("input") or "")) != ident(step.utterance):
                    continue
                result.append(f'    - Player: "{step.utterance}"')
                for reply in turn.get("reply") or []:
                    result.append(
                        f'      - NPC {reply.get("channel", "say")}: {reply.get("text", "")}'
                    )
                    for guard in reply.get("guards") or []:
                        result.append(f"        - Reply guard: `{guard}`")
                for guard in turn.get("guards") or []:
                    result.append(f"      - Condition: `{guard}`")
                if ident(step.utterance) != "hail":
                    for edge in chain.get("transitions") or []:
                        if ident(str(edge.get("_to") or "")) != ident(step.utterance):
                            continue
                        basis = str(edge.get("basis") or "")
                        origin = str(edge.get("_from") or "")
                        if basis in ("explicit_mention", "conversation_sequence"):
                            certainty = (
                                "explicit prompt"
                                if basis == "explicit_mention"
                                else "sequence only; unverified"
                            )
                            result.append(f'      - Linked from "{origin}" ({certainty}).')
                return result
        speech = g.says.get((actor_key(step.actor), ident(step.utterance)))
        return [f"    - NPC say: {speech}"] if speech else []
    for chain in chains:
        for speech in chain.get("context_speech") or []:
            if str(speech.get("event") or "").lower() not in (
                "event_item",
                "event_trade",
            ):
                continue
            guards = list(map(str, speech.get("guards") or []))
            ids = set().union(*(guard_item_ids(guard) for guard in guards)) if guards else set()
            if step.payload and set(step.payload) != ids:
                continue
            # A broad unguarded speech branch cannot be attributed to this
            # specific hand-in. Exclude it rather than implying causality.
            if not ids:
                continue
            result.append(
                f'    - {speech.get("event")} NPC {speech.get("channel", "say")}: {speech.get("text", "")}'
            )
            for guard in guards:
                result.append(f"      - Event guard: `{guard}`")
    return list(dict.fromkeys(result))


def _anchor(iid: int, graph: Graph) -> str:
    """Explicit stable anchor: names can contain punctuation or change over time."""
    return f"epic-item-{iid}"


def _shared_reference(g: Graph, first: tuple[int, int, int], last: tuple[int, int, int]) -> str:
    """One reference to a previously printed sequence, not an acquisition action."""
    reward, start, _ = first
    assert reward == last[0]
    finish = last[1]
    span = f"step {start}" if start == finish else f"steps {start}–{finish}"
    return (
        f"Shared prerequisite: see [{g.name(reward)}](#{_anchor(reward, g)}), "
        f"{span}. Follow those instructions again if the required item "
        "was consumed or another copy is needed."
    )


def render(g: Graph, class_name: str, catalog: AcquisitionCatalog) -> str:
    out = [
        f"# {class_name.title()} — Epic Quest Walkthrough",
        "",
        "Generated directly from quest-graph item rewards. Unresolved dependencies are marked, not inferred.",
        "",
    ]
    # The first published occurrence of each graph action owns its full dialogue.
    # Stable Step keys encode the action/group, not human-readable Markdown.
    published: dict[str, tuple[int, int, int]] = {}
    previous_plans: dict[int, set[str]] = {}
    for era, rewards in REWARDS[class_name].items():
        out.extend([f"## Epic {era}", ""])
        for reward in rewards:
            # Plan *independently* for each reward. Never reuse planner.done_items:
            # doing so would skip genuine dependencies and conceal cycles.
            planner = Planner(g, catalog)
            steps = planner.plan(reward)
            out.extend([f"### {g.name(reward)}", "", f'<a id="{_anchor(reward, g)}"></a>', ""])
            planned_keys = {step.key for step in steps}
            # A complete previously documented reward path is a single
            # prerequisite, not dozens of interleaved references. Prefer the
            # maximal earlier paths: Heartwood subsumes the two Ranger 1.0
            # epics, so Aurora needs only the Heartwood route linked here.
            # Synthetic introductory hails are presentation, not causal
            # prerequisites. A nested reward may open with a different NPC.
            causal_keys = {k for k in planned_keys if not k.startswith("introduction:")}
            included = [
                r
                for r, keys in previous_plans.items()
                if keys
                and {k for k in keys if not k.startswith("introduction:")}.issubset(causal_keys)
            ]
            maximal = [
                r
                for r in included
                if not any(
                    r != other and previous_plans[r] < previous_plans[other] for other in included
                )
            ]
            covered = set().union(*(previous_plans[r] for r in maximal)) if maximal else set()
            if maximal:
                links = ", ".join(f"[{g.name(r)}](#{_anchor(r, g)})" for r in maximal)
                out.extend(
                    [
                        f"**Earlier reward routes required by this graph path:** {links}.",
                        "Revisit those instructions if another copy of a consumed item is needed.",
                        "",
                    ]
                )
            # Mark repeated contiguous runs in source order. Crucially, group by
            # the original published section and consecutive source step numbers:
            # two branches may share some actions but not the entire branch.
            entries: list[tuple[str, Step | tuple[int, int, int], tuple[int, int, int] | None]] = []
            new_keys: set[str] = set()
            for step in steps:
                if step.key in covered:
                    continue
                previous = published.get(step.key)
                if previous and step.key not in new_keys:
                    entries.append(("shared", previous, None))
                else:
                    entries.append(("action", step, None))
                    new_keys.add(step.key)
            number = 0
            i = 0
            while i < len(entries):
                kind, value, _ = entries[i]
                if kind == "shared":
                    if not isinstance(value, tuple):
                        continue
                    first = value
                    last = first
                    j = i + 1
                    while j < len(entries) and entries[j][0] == "shared":
                        next_ref = entries[j][1]
                        if not isinstance(next_ref, tuple):
                            continue
                        # Only combine adjacent steps from the same earlier
                        # walkthrough; don't merge unrelated shared branches.
                        if next_ref[0] != last[0] or next_ref[1] != last[1] + 1:
                            break
                        last = next_ref
                        j += 1
                    number += 1
                    out.append(f"{number}. {_shared_reference(g, first, last)}")
                    i = j
                    continue
                if not isinstance(value, Step):
                    continue
                step = value
                number += 1
                out.append(f"{number}. {step.text}")
                out.extend(speech_for_step(g, step))
                # Register only printed actions. References always resolve to a
                # real step, never to another reference (no reference chains).
                published.setdefault(step.key, (reward, number, len(out)))
                i += 1
            previous_plans[reward] = planned_keys
            if planner.errors:
                out.extend(["", "**Unresolved graph dependencies:**"])
                out.extend(f"- {e}" for e in dict.fromkeys(planner.errors))
            # Verify the reward using structured acquisition metadata, not prose.
            if not any(reward in step.produced_items for step in steps):
                out.append(f"**Unverified final reward:** {g.name(reward)}")
            out.append("")
    return "\n".join(out).rstrip() + "\n"


def main(argv: list[str] | None = None) -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--graph", type=Path, default=Path.home() / ".eqclient" / "quest_graph.jsonl")
    p.add_argument("--class", dest="class_name", required=True, choices=sorted(REWARDS))
    p.add_argument("--out", type=Path, default=Path(".epics"))
    p.add_argument("--drops", type=Path, help="Optional explicit drops.jsonl (for testing)")
    p.add_argument("--merchants", type=Path, help="Optional explicit merchants.jsonl (for testing)")
    p.add_argument("--recipes", type=Path, help="Optional explicit recipes.jsonl (for testing)")
    args = p.parse_args(argv)
    g = Graph(args.graph)
    catalog = AcquisitionCatalog(args.drops, args.merchants, args.recipes)
    args.out.mkdir(parents=True, exist_ok=True)
    path = args.out / f"{args.class_name}.md"
    content = render(g, args.class_name, catalog)
    path.write_text(content, encoding="utf-8")
    print(f"{path} ({len(content.splitlines())} lines)")


if __name__ == "__main__":
    main()
