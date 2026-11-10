#!/usr/bin/env python3
"""Independent, reward-seeded EverQuest epic walkthrough generator.

Required inputs: a quest_graph.jsonl and a class name. Uses the EQEmu data
caches for missing loot, merchants, and tradeskill sources. No prior walkthroughs
or v1/v2 renderer.

    python epic_writer_v2.py --graph quest_graph.jsonl --class cleric --out /tmp/epics

The generator deliberately distinguishes graph-proven steps from unresolved
prerequisites. It does not treat all dialogue at an NPC as a quest route.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict, deque
from dataclasses import dataclass, field
from pathlib import Path
import sys

from eqclient4.data.drops import ensure_drops
from eqclient4.data.merchants import ensure_merchants
from eqclient4.data.recipes import ensure_recipes

REWARDS = {
    'warrior': {'1.0': (10908,), '1.5': (60321,), '2.0': (60332,)},
    'cleric': {'1.0': (5532,), '1.5': (9955,), '2.0': (20076,)},
    'paladin': {'1.0': (10099,), '1.5': (64031,), '2.0': (48147,)},
    'ranger': {'1.0': (20487, 20488), '1.5': (62627,), '2.0': (62649,)},
    'shadowknight': {'1.0': (14383,), '1.5': (50003,), '2.0': (48136,)},
    'druid': {'1.0': (20490,), '1.5': (62863,), '2.0': (62880,)},
    'monk': {'1.0': (10652,), '1.5': (61025,), '2.0': (67742,)},
    'bard': {'1.0': (20542,), '1.5': (77631,), '2.0': (77640,)},
    'rogue': {'1.0': (11057,), '1.5': (52347,), '2.0': (52348,)},
    'shaman': {'1.0': (10651,), '1.5': (57400,), '2.0': (57405,)},
    'necromancer': {'1.0': (20544,), '1.5': (62581,), '2.0': (64067,)},
    'wizard': {'1.0': (14341,), '1.5': (12665,), '2.0': (16576,)},
    'magician': {'1.0': (28034,), '1.5': (19092,), '2.0': (19839,)},
    'enchanter': {'1.0': (10650,), '1.5': (52952,), '2.0': (52962,)},
    'beastlord': {'1.0': (8495,), '1.5': (52911,), '2.0': (57054,)},
    'berserker': {'1.0': (68299,), '1.5': (18398,), '2.0': (18609,)},
}

_ITEM = re.compile(r'^item:(\d+)$')
_GUARD_ITEM = re.compile(r'(?:item\d*\s*=>\s*|item\d*\s*=\s*|check_hasitem\([^,]+,\s*)(\d+)')
_PERL_HANDIN_ITEM = re.compile(r'(?<![\w])([1-9]\d{2,})\s*=>\s*\d+')


def guard_item_ids(value: str) -> set[int]:
    return {int(x) for x in _GUARD_ITEM.findall(value)} | {int(x) for x in _PERL_HANDIN_ITEM.findall(value)}


def ident(value: str) -> str:
    return re.sub(r'[\s_]+', ' ', value.strip()).casefold()


def actor_key(value: str) -> str:
    return '/'.join(ident(v) for v in value.split('/', 1))


def actor_of(value: str) -> str:
    return value.split('#', 1)[0]


def label(value: str) -> str:
    zone, _, npc = actor_of(value).partition('/')
    return f'{zone}/"{npc.title()}"' if npc else value


def item_id(token: str) -> int | None:
    m = _ITEM.fullmatch(str(token))
    return int(m[1]) if m else None


@dataclass
class Step:
    key: str
    text: str
    actor: str = ''
    action: str = ''
    payload: tuple[int, ...] = ()
    utterance: str = ''
    group: str = ''
    evidence: list[str] = field(default_factory=list)


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
        with graph.open(encoding='utf-8') as f:
            for line in f:
                if not line.strip():
                    continue
                row = json.loads(line)
                kind = row.get('kind')
                if kind == 'item':
                    iid = int(row['item'])
                    self.items[iid] = str(row.get('name') or '')
                    self.item_sources[iid] = tuple(str(source) for source in row.get('sources') or ())
                elif kind == 'world':
                    self.world[int(row['id'])] = str(row.get('name') or '')
                elif kind == 'dialogue':
                    key = actor_key(str(row.get('source') or ''))
                    self.dialogues[key].append(row)
                    if key.rsplit('/', 1)[-1].isdigit():
                        self.numeric_dialogues[key.split('/')[0]].append(row)
                elif kind == 'say':
                    key = actor_key(f"{row.get('zone', '')}/{row.get('npc', '')}")
                    self.says[(key, ident(str(row.get('word') or '')))] = str(row.get('text') or '')
                elif kind == 'edge':
                    self.edges.append(row)
                    src = str(row.get('from') or '')
                    dst = str(row.get('to') or '')
                    grp = str(row.get('group') or '')
                    rel = row.get('rel')
                    self.by_from[src].append(row)
                    self.by_to[dst].append(row)
                    if grp:
                        self.by_group[grp].append(row)
                    if rel in ('gives', 'loots', 'grounds', 'produces'):
                        iid = item_id(dst)
                        if iid is not None:
                            self.producers[iid].append(row)
                    if src.startswith('recipe:'):
                        self.recipes[src].append(row)
                    if rel == 'sets' and row.get('flag'):
                        self.flag_setters[str(row['flag'])].append(row)
                    if rel == 'sets' and row.get('faction') is not None:
                        self.faction_gains[str(row['faction'])].append(row)
                    if rel == 'spawns' and dst.startswith('npc:'):
                        self.spawns[dst].append(row)
                        self.actor_spawns[actor_key(actor_of(src))].append(row)

    def name(self, iid: int) -> str:
        name = self.items.get(iid) or f'Item {iid}'
        return f'"{name}" ({iid})'

    def group_rows(self, row: dict) -> list[dict]:
        grp = row.get('group')
        if grp:
            return self.by_group.get(str(grp), [])
        return self.by_from.get(str(row.get('from') or ''), [])

    def inputs(self, row: dict) -> list[int]:
        return list(dict.fromkeys(iid for r in self.group_rows(row)
                                  if r.get('rel') == 'receives'
                                  if (iid := item_id(r.get('to', ''))) is not None))

    def needs(self, row: dict) -> tuple[list[int], list[str]]:
        items, flags = [], []
        for r in self.group_rows(row):
            if r.get('rel') != 'needs':
                continue
            if (iid := item_id(r.get('to', ''))) is not None:
                if iid not in items:
                    items.append(iid)
            elif r.get('flag'):
                flags.append(str(r['flag']))
        return items, list(dict.fromkeys(flags))

    def conversation(self, actor: str, needed: tuple[int, ...] = ()) -> list[dict]:
        key = actor_key(actor)
        direct = self.dialogues.get(key, [])
        if direct:
            return direct
        # Numeric NPC scripts: accept only a unique matching item guard in this zone.
        zone = key.split('/', 1)[0]
        matched = []
        for chain in self.numeric_dialogues.get(zone, []):
            for speech in chain.get('context_speech', []):
                guards = ' '.join(map(str, speech.get('guards') or []))
                ids = guard_item_ids(guards)
                if needed and set(needed) == ids:
                    matched.append(chain)
                    break
        return matched if len(matched) == 1 else []

    def spoken(self, actor: str, word: str) -> bool:
        k = actor_key(actor)
        if (k, ident(word)) in self.says:
            return True
        return any(ident(t.get('input', '')) == ident(word)
                   for c in self.conversation(actor) for t in c.get('turns', []))


class AcquisitionCatalog:
    """Existing EQEmu acquisition catalogs, independently loaded.

    Each optional path overrides only its corresponding default cache.
    Keep parsing, index construction and schema handling in eqclient4.data.
    """

    def __init__(self, drops: Path | None = None, merchants: Path | None = None,
                 recipes: Path | None = None):
        self._drops = ensure_drops(path=str(drops) if drops else None)
        self._merchants = ensure_merchants(path=str(merchants) if merchants else None)
        self._recipes = ensure_recipes(path=str(recipes) if recipes else None)

    def drop(self, iid: int):
        return self._drops.best(iid)

    def merchant(self, iid: int):
        return self._merchants.best(iid)

    def recipe(self, iid: int):
        return self._recipes.for_item(iid)


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
        self.active_flags: set[tuple[str,str]] = set()
        self.done_flags: set[tuple[str,str]] = set()

    def put(self, key: str, text: str, *, actor: str = '', action: str = '',
            payload: tuple[int, ...] = (), utterance: str = '', group: str = '') -> None:
        if key not in self.emitted:
            self.emitted.add(key)
            self.steps.append(Step(key, text, actor, action, payload, utterance, group))
            return

        # A spawn/signal traversal may emit a hand-in before its reward is
        # discovered. Preserve the same action, but enrich it with graph gifts.
        if key.startswith('hand:') and '. Gives ' in text:
            existing = next(step for step in self.steps if step.key == key)
            reward = text.split('. Gives ', 1)[1].rstrip('.')
            if '. Gives ' not in existing.text:
                existing.text = existing.text.rstrip('.') + '. Gives ' + reward + '.'
            else:
                prefix, current = existing.text.split('. Gives ', 1)
                rewards = current.rstrip('.').split(' + ')
                if reward not in rewards:
                    existing.text = prefix + '. Gives ' + ' + '.join((*rewards, reward)) + '.'
            if payload and not existing.payload:
                existing.payload = payload

    def candidates(self, iid: int) -> list[dict]:
        options = self.g.producers.get(iid, [])
        if not options:
            return []
        # Reliable, explicitly scripted rewards precede recipe and drop alternatives.
        # Skip self-consuming recipes and prefer less ambiguous sources.
        def rank(r: dict) -> tuple[int, int, str]:
            rel = r.get('rel')
            ins = self.g.inputs(r) if rel == 'gives' else []
            if rel == 'produces':
                ins = [item_id(x.get('to', '')) for x in self.g.recipes.get(r.get('from', ''), [])
                       if x.get('rel') == 'consumes']
            cyc = iid in ins
            # An explicitly witnessed item hand-in is a stronger producer
            # than a coincidental SAY branch from another quest.
            group = str(r.get('group') or '')
            other_gifts = sum(r2.get('rel') == 'gives' and r2.get('to') != f'item:{iid}'
                              for r2 in self.g.group_rows(r))
            primary = (0 if rel == 'gives' and '#hand:' in group and not other_gifts else
                       1 if rel == 'gives' and not other_gifts else
                       2 if rel == 'gives' else
                       3 if rel == 'produces' else
                       4 if rel == 'loots' else 5)
            return (100 if cyc else primary, len(ins), str(r.get('from', '')))
        # Returning an item in exchange for that same item changes quest state,
        # but cannot supply the first copy of the item.
        return sorted((r for r in options if not (
            # A hand-in returning the same item cannot acquire the first copy.
            (r.get('rel') == 'gives' and iid in self.g.inputs(r)) or
            # An unnamed NPC in an inferred death chain is weaker evidence
            # than an explicit, named loot source in the graph item catalog.
            (r.get('rel') == 'loots' and
             str(r.get('name') or '').lower() == 'needs heading validation' and
             any(x.startswith('loot:') for x in self.g.item_sources.get(iid, ())))
        )), key=rank)

    def candidate(self, iid: int) -> dict | None:
        """First-ranked producer, for inspection; acquisition tries alternatives."""
        return next(iter(self.candidates(iid)), None)

    def summon_from_spell(self, iid: int) -> bool:
        """Prefer an explicit summon spell's acquisition chain over stray loot.

        For example the Magician epic's Orb of Mastery is summoned by
        Spell: Summon Orb, rewarded by the Master of Elements hand-in.
        """
        spells = [source.partition(':')[2] for source in self.g.item_sources.get(iid, ())
                  if source.startswith('spell:') and source.partition(':')[2]]
        for spell in spells:
            scroll = next((sid for sid, name in self.g.items.items()
                           if name.casefold() == ('Spell: ' + spell).casefold()), None)
            if scroll is None or scroll == iid:
                continue
            self.acquire(scroll)
            self.put(f'summon-spell:{iid}:{scroll}',
                     f'Learn {self.g.name(scroll)} and cast "{spell}" to summon {self.g.name(iid)}.')
            return True
        return False

    def acquire(self, iid: int) -> None:
        if iid in self.done_items:
            return
        if iid in self.active_items:
            raise AcquisitionCycle(self.g.name(iid))
        self.active_items.add(iid)
        try:
            # A named summoning spell is a causally connected acquisition
            # route; incidental loot-table drops are not the epic quest chain.
            if self.summon_from_spell(iid):
                self.done_items.add(iid)
                return
            options = self.candidates(iid)
            if not options:
                self.catalog_acquire(iid)
            else:
                rejected = []
                for row in options:
                    # Candidate speculation must not leak steps, emitted events,
                    # flags, or completed items into the next candidate.
                    mark = len(self.steps)
                    emitted = self.emitted.copy()
                    done = self.done_items.copy()
                    events = self.active_events.copy()
                    used = self.used_edges.copy()
                    done_flags = self.done_flags.copy()
                    errors_len = len(self.errors)
                    try:
                        rel = row.get('rel')
                        if rel == 'gives':
                            self.giver(row, iid)
                        elif rel == 'produces':
                            self.recipe(row, iid)
                        elif rel in ('loots', 'grounds'):
                            self.loot(row, iid)
                        else:
                            continue
                    except AcquisitionCycle as cycle:
                        del self.steps[mark:]
                        self.emitted = emitted
                        self.done_items = done
                        self.active_events = events
                        self.used_edges = used
                        self.done_flags = done_flags
                        del self.errors[errors_len:]
                        rejected.append(str(cycle))
                        continue
                    break
                else:
                    # Graph actions can exchange an item, or depend on a later
                    # quest state. Only if every usable producer fails, consult
                    # independent acquisition catalogs before reporting a cycle.
                    if not self.catalog_acquire(iid, allow_missing=False):
                        raise AcquisitionCycle(
                            f'{self.g.name(iid)}: no acyclic graph or catalog producer'
                            + (f' (via {rejected[0]})' if rejected else '')
                        )
            self.done_items.add(iid)
        finally:
            self.active_items.remove(iid)

    def item_source_acquire(self, iid: int, *, include_loot: bool = False) -> bool:
        """Use acquisition metadata embedded in the graph's item catalog.

        These are independent ways of obtaining an item, not cumulative quest
        requirements.  V1's `_made_by` used the same `sources` field.
        """
        sources = self.g.item_sources.get(iid, ())
        for kind in (('forage', 'fishing', 'ground', 'spell', 'loot') if include_loot
                     else ('forage', 'fishing', 'ground', 'spell')):
            values = list(dict.fromkeys(source.partition(':')[2] for source in sources
                                        if source.startswith(kind + ':') and source.partition(':')[2]))
            if not values:
                continue
            item = self.g.name(iid)
            if kind in ('forage', 'fishing', 'ground'):
                locations = ' or '.join(f'`{zone}`' for zone in values)
                verb = {'forage': 'Forage', 'fishing': 'Fish for',
                        'ground': 'Collect ground spawn'}[kind]
                description = f'{verb} {item} in {locations}.'
            elif kind == 'spell':
                description = f'Summon {item} by casting ' + ' or '.join(f'"{name}"' for name in values) + '.'
            else:
                locations = []
                for value in values:
                    npc, _, zone = value.partition('@')
                    locations.append(f'"{npc}"' + (f' in `{zone}`' if zone else ''))
                description = f'Loot {item} from ' + ' or '.join(locations) + '.'
            self.put(f'item-source:{kind}:{iid}', description)
            return True
        return False

    def catalog_acquire(self, iid: int, *, allow_missing: bool = True) -> bool:
        """Try independent item sources; optionally leave a missing-item marker."""
        if self.item_source_acquire(iid):
            return True
        drop = self.catalog.drop(iid)
        if drop:
            if isinstance(drop, dict):
                npc, name = int(drop['npc']), str(drop.get('name') or '')
                zone, chance = str(drop.get('where') or '?'), float(drop['chance'])
            else:
                npc, name = int(drop.npc_id), str(drop.name or '')
                zone, chance = str(drop.zone or '?'), float(drop.chance)
            self.put(f'catalog-drop:{iid}',
                     f'Loot {self.g.name(iid)} from "{name or f"NPC {npc}"}" '
                     f'(NPC {npc}) in `{zone}`. Drop cache: {chance:g}% chance per kill.')
            return True
        seller = self.catalog.merchant(iid)
        if seller:
            if isinstance(seller, tuple):
                row, cost = seller
                name, npc, zone = row.name, row.npc_id, row.zone
            else:
                name, npc, zone, cost = seller.get('name') or '', seller['npc'], seller.get('where') or '?', None
            cost_text = f' Base price: {cost:,} copper.' if cost else ''
            self.put(f'catalog-merchant:{iid}',
                     f'Buy {self.g.name(iid)} from "{name}" (NPC {npc}) in `{zone}`.{cost_text}')
            return True
        recipe = self.catalog.recipe(iid)
        if recipe and iid not in [int(x) for x, _ in (
            recipe['components'] if isinstance(recipe, dict) else recipe.components
        )]:
            if isinstance(recipe, dict):
                rid = int(recipe['id'])
                parts = [(int(x), int(count)) for x, count in recipe['components']]
                container = int(recipe.get('container') or 0)
                skill = str(recipe.get('name') or '')
            else:
                rid, parts = int(recipe.id), list(recipe.components)
                container, skill = int(recipe.container or 0), str(recipe.name or '')
            for component, _count in parts:
                self.acquire(component)
            # Containers may be tradeskill stations rather than inventory items;
            # don't invent a missing item for an unspecified world container.
            inputs = ', '.join(self.g.name(x) + (f' x{n}' if n != 1 else '')
                               for x, n in parts)
            extra = f' Requires {skill}.' if skill else ''
            self.put(f'catalog-recipe:{rid}:{iid}',
                     f'Combine recipe {rid} (container {container}): {inputs}. '
                     f'Produces {self.g.name(iid)}.{extra}')
            return True
        if self.item_source_acquire(iid, include_loot=True):
            return True
        if allow_missing:
            self.put(f'missing:{iid}',
                     f'**Unresolved acquisition:** {self.g.name(iid)} has no graph or catalog producer.')
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
                src = str(row.get('from') or '')
                if '#signal:' in src:
                    arrival = actor_of(src) + '#event_spawn'
                    for trigger in self.g.by_to.get(arrival, ()):
                        if trigger.get('rel') != 'triggers':
                            continue
                        initiator = str(trigger.get('from') or '')
                        if '#hand:' not in initiator:
                            continue
                        speech = self.g.says.get((actor_key(actor_of(initiator)), 'hail'), '').casefold()
                        for needed in self.g.by_group.get(initiator, ()):
                            if needed.get('rel') != 'receives':
                                continue
                            token = item_id(needed.get('to', ''))
                            if token is None:
                                continue
                            keywords = [w for w in re.findall(r'[a-z]{5,}', self.g.name(token).casefold())
                                        if w not in {'great', 'water', 'item', 'lord'}]
                            if keywords and any(w in speech for w in keywords):
                                return True
                pending.extend(x for x in self.g.inputs(row) if x not in seen)
                if src.startswith('recipe:'):
                    pending.extend(x for r in self.g.recipes.get(src, ())
                                   if r.get('rel') == 'consumes'
                                   if (x := item_id(r.get('to', ''))) is not None and x not in seen)
        return False

    def faction_requirements(self, row: dict) -> None:
        """Explain explicit faction gates without pretending a single gain meets them.

        The graph has threshold checks and individual faction gains, but does
        not carry the player's current faction or repeat counts. Keep these
        requirements visible rather than declaring them acquired.
        """
        requirements = [(str(r['faction']), str(r.get('at') or 'set'))
                        for r in self.g.group_rows(row)
                        if r.get('rel') == 'needs' and r.get('faction') is not None]
        for faction, at in dict.fromkeys(requirements):
            key = f'faction-need:{faction}:{at}'
            sources = self.g.faction_gains.get(faction, ())
            # Individual quest events grant faction, but neither their total
            # repetitions nor the starting standing is proven by this graph.
            actionable = sorted((r for r in sources if '#hand:' in str(r.get('from') or '')),
                                key=lambda r: str(r.get('from') or ''))
            examples = []
            for gain in actionable[:3]:
                group = str(gain.get('group') or gain.get('from') or '')
                inputs = self.g.inputs(gain)
                if inputs:
                    items = ' + '.join(self.g.name(x) for x in inputs)
                    examples.append(f'{label(actor_of(group))}: hand {items} (faction delta {gain.get("value", "?")})')
            details = (' Graph-supported ways to gain this faction include: '
                       + '; '.join(examples) + '.' if examples else '')
            self.put(key,
                     f'**Faction prerequisite:** `{faction}` must satisfy `{at}` '
                     f'before the following action. Faction progress is not automatically verified.'
                     + details)

    def giver(self, row: dict, iid: int) -> None:
        src = str(row.get('from') or '')
        group = str(row.get('group') or src)
        ins = self.g.inputs(row)
        if len(ins) > 1:
            position = {v: i for i, v in enumerate(ins)}
            ins.sort(key=lambda x: (not self.has_connected_intro(x), position[x]))
        for required in ins:
            self.acquire(required)
        needs, flags = self.g.needs(row)
        for required in needs:
            self.acquire(required)
        for flag in flags:
            conditions = [str(r.get('at') or 'set') for r in self.g.group_rows(row)
                          if r.get('rel') == 'needs' and r.get('flag') == flag]
            at = next((condition for condition in conditions if condition != 'set'), 'set')
            self.flag(flag, at)
        self.faction_requirements(row)
        actor = actor_of(src)
        if ins:
            rendered = ' + '.join(self.g.name(x) for x in ins)
            self.put(f'hand:{group}', f'{label(actor)}, hand {rendered}. Gives {self.g.name(iid)}.',
                     actor=actor, action='hand', payload=tuple(ins), group=group)
        else:
            word = group.split('#', 2)[1] if '#' in group else (src.rsplit('#', 1)[-1] if '#' in src else '')
            if word.startswith('event_') or word.startswith('timer:'):
                word = '' 
            if word.lower().startswith('event_') or word.lower().startswith('signal:'):
                self.event(src)
                self.put(f'give:{group}:{iid}', f'{label(actor)} produces {self.g.name(iid)} on `{src}`.', actor=actor)
            else:
                self.put(f'say:{group}', f'{label(actor)}, say "{word.title()}". Gives {self.g.name(iid)}.',
                         actor=actor, action='say', utterance=word, group=group)

    def flag(self, name: str, at: str) -> None:
        state = (name, at)
        if state in self.done_flags:
            return
        if at == 'unset':
            return
        if state in self.active_flags:
            # A setter may itself require the flag it purports to establish.
            # Reject this acquisition route so the caller can try alternatives.
            raise AcquisitionCycle(f'quest flag `{name}` {at}')
        self.active_flags.add(state)
        try:
            setters = self.g.flag_setters.get(name, [])
            match = re.fullmatch(r'(==|>=|>|<=|<)\s*(-?\d+)', at)
            op = None
            if match:
                op, target = match.group(1), int(match.group(2))
                compare = {'==': lambda v: v == target, '>=': lambda v: v >= target,
                           '>': lambda v: v > target, '<=': lambda v: v <= target,
                           '<': lambda v: v < target}[op]
                setters = [r for r in setters if str(r.get('value', '')).lstrip('-').isdigit()
                           and compare(int(r['value']))]
            elif at.startswith('=='):
                setters = [r for r in setters if str(r.get('value')) == at[2:].strip()]
            if not setters:
                self.errors.append(f'No graph setter for `{name}` {at}')
                return
            # A flag can have several setters. The first one may lead back to
            # the item we're currently acquiring; try the others before failing.
            setters = sorted(setters, key=lambda r: (
                int(r['value']) if match and op in ('>=', '>') else 0,
                0 if '#hand:' in str(r.get('from', '')) else
                1 if '#' in str(r.get('from', '')) else 2,
                str(r.get('from', ''))
            ))
            
            for row in setters:
                mark = len(self.steps)
                original_steps = [(step, step.text, step.payload) for step in self.steps]
                emitted = self.emitted.copy()
                done = self.done_items.copy()
                events = self.active_events.copy()
                used = self.used_edges.copy()
                done_flags = self.done_flags.copy()
                errors_len = len(self.errors)
                src = str(row.get('from') or '')
                try:
                    if '#hand:' in src:
                        self.hand_event(src)
                    elif '#recipe:' in src:
                        recipe_id = 'recipe:' + src.rsplit('#recipe:', 1)[1]
                        for rr in self.g.recipes.get(recipe_id, []):
                            if rr.get('rel') == 'consumes':
                                iid = item_id(rr.get('to', ''))
                                if iid is not None:
                                    self.acquire(iid)
                        self.put('flag:'+src, f'Combine recipe {recipe_id} to set `{name}` to `{row.get("value")}`.')
                    else:
                        word = src.rsplit('#', 1)[-1]
                        if word:
                            self.put('flag:'+src, f'{label(actor_of(src))}, say "{word.title()}". Sets `{name}` to `{row.get("value")}`.',
                                     actor=actor_of(src), action='say', utterance=word)
                        else:
                            self.errors.append(f'Cannot execute setter for `{name}` at `{src}`')
                    self.done_flags.add(state)
                    return
                except AcquisitionCycle:
                    del self.steps[mark:]
                    for step, text, payload in original_steps:
                        step.text, step.payload = text, payload
                    self.emitted = emitted
                    self.done_items = done
                    self.active_events = events
                    self.used_edges = used
                    self.done_flags = done_flags
                    del self.errors[errors_len:]
            raise AcquisitionCycle(f'quest flag `{name}` {at}: all setters are cyclic')
        finally:
            self.active_flags.remove(state)

    def recipe(self, row: dict, iid: int) -> None:
        src = str(row.get('from') or '')
        rows = self.g.recipes.get(src, [])
        consume = [int(v) for r in rows if r.get('rel') == 'consumes'
                   if (v := item_id(r.get('to', ''))) is not None and v != iid]
        containers = [item_id(r.get('to', '')) for r in rows
                      if r.get('rel') == 'container' and item_id(r.get('to', '')) is not None]
        for x in dict.fromkeys(containers + consume):
            self.acquire(x or 0)
        container = self.g.name(containers[0] or 0) if containers else 'appropriate tradeskill container'
        parts = ', '.join(self.g.name(v) for v in consume)
        skill = next((str(r.get('skill_name')) for r in rows if r.get('skill_name')), '')
        desc = f'Combine in {container}: {parts}. Produces {self.g.name(iid)}.'
        if skill:
            desc += f' Requires {skill}.'
        self.put(f'recipe:{src}:{iid}', desc)

    def loot(self, row: dict, iid: int) -> None:
        src = str(row.get('from') or '')
        name = str(row.get('name') or '')
        npc = row.get('npc')
        if '#hand:' in src:
            self.hand_event(src, target_npc=npc)
        elif '#' in src:
            self.event(src, target_npc=npc)
        if row.get('rel') == 'grounds':
            self.put(f'ground:{src}:{iid}', f'Collect {self.g.name(iid)} at `{src}`.')
            return
        place = actor_of(src).split('/', 1)[0]
        target = name or (f'NPC {npc}' if npc else actor_of(src).split('/', 1)[-1])
        if npc:
            # Treasure chests and world objects are opened, not killed.
            verb = 'Open' if any(x in target.casefold() for x in ('chest', 'coffer', 'cache', 'treasure')) else 'Kill'
            self.put(f'kill-loot:{src}:{iid}',
                     f'{verb} "{target}" (NPC {npc}) in `{place}` and loot {self.g.name(iid)}.')
        else:
            self.put(f'loot:{src}:{iid}', f'Loot {self.g.name(iid)} from "{target}" in `{place}`.')

    def event(self, node: str, target_npc: int | None = None) -> None:
        if node in self.active_events:
            self.errors.append(f'Event cycle at `{node}`')
            return
        key = f'event:{node}'
        if key in self.emitted:
            return
        self.active_events.add(node)
        try:
            if '#signal:' in node:
                # An NPC must have been spawned before receiving its signal.
                self.pre_spawned_actor(actor_of(node))
            if '#hand:' in node:
                self.hand_event(node)
            # To reach an event, follow incoming trigger edges (preconditions).
            incoming = [r for r in self.g.by_to.get(node, []) if r.get('rel') == 'triggers']
            for edge in sorted(incoming, key=lambda r: str(r.get('from', ''))):
                parent = str(edge.get('from') or '')
                if '#hand:' in parent:
                    self.hand_event(parent, target_npc=target_npc)
                elif '#event_death' in parent:
                    # Some death events require a previously spawned NPC.
                    self.pre_spawned_actor(actor_of(parent))
                    self.put(f'kill:{parent}', f'Kill {label(actor_of(parent))}.')
                else:
                    self.event(parent)
            # If no trigger points to a signal, the graph may still contain the
            # event itself; render it but do not fabricate its origin.
            for r in self.g.by_from.get(node, []):
                if r.get('rel') == 'spawns' and (target_npc is None or str(r.get('to')) == f'npc:{target_npc}'):
                    self.put(f'spawn:{node}:{r.get("to")}',
                             f'Spawns "{r.get("name") or r.get("to")}" ({r.get("to")}) '
                             f'via `{node}`.')
            self.emitted.add(key)
        finally:
            self.active_events.remove(node)

    def hand_event(self, group: str, target_npc: int | None = None) -> None:
        rows = self.g.by_group.get(group, [])
        if rows:
            self.faction_requirements(rows[0])
        ins = list(dict.fromkeys(iid for r in rows if r.get('rel') == 'receives'
                                 if (iid := item_id(r.get('to', ''))) is not None))
        for x in ins:
            self.acquire(x)
        if ins:
            self.put(f'hand:{group}', f'{label(actor_of(group))}, hand ' +
                     ' + '.join(self.g.name(x) for x in ins) + '.',
                     actor=actor_of(group), action='hand', payload=tuple(ins), group=group)
        # Spawn edges often have `from=group` but no `group` property.
        # Index both shapes rather than relying on by_group alone.
        for r in self.g.by_from.get(group, []):
            if r.get('rel') == 'spawns' and target_npc is not None and str(r.get('to')) == f'npc:{target_npc}':
                self.put(f'spawn:{group}:{r.get("to")}',
                         f'Spawns "{r.get("name") or r.get("to")}" ({r.get("to")}) '
                         f'after the hand-in.')

    def pre_spawned_actor(self, actor: str) -> None:
        # Search the trigger chain for the actor's event_spawn rather than
        # inventing a required spawn merely because an NPC has a database ID.
        target = actor_key(actor) + '#event_spawn'
        for edge in self.g.by_to.get(target, []):
            if edge.get('rel') == 'triggers':
                from_node = str(edge.get('from') or '')
                if '#hand:' in from_node:
                    self.hand_event(from_node, target_npc=edge.get('npc'))
                else:
                    self.event(from_node)

    def introduce(self) -> None:
        if not self.steps:
            return
        # A productive initial SAY is the most reliable introduction (Telin).
        productive = next((s for s in self.steps if s.action == 'say' and s.actor
                           and s.utterance.casefold() != 'hail'
                           and self.g.spoken(s.actor, 'hail')), None)
        if productive:
            chosen = productive.actor
        else:
            chosen = ''
            for step in self.steps:
                if not step.actor or not self.g.spoken(step.actor, 'hail'):
                    continue
                # Prefer an introductory hail that actually mentions the item
                # handed to this NPC, not a random late NPC greeting.
                speech = self.g.says.get((actor_key(step.actor), 'hail'), '')
                if not speech:
                    for chain in self.g.conversation(step.actor):
                        for turn in chain.get('turns', []):
                            if ident(str(turn.get('input'))) == 'hail':
                                speech += ' '.join(str(x.get('text') or '') for x in turn.get('reply', []))
                words = {w for iid in step.payload for w in re.findall(r'[a-z]{5,}', self.g.name(iid).lower())
                         if w not in {'water', 'great', 'item', 'lord'}}
                if words and any(w in speech.casefold() for w in words):
                    chosen = step.actor
                    break
        if not chosen:
            return
        hail = Step('introduction:'+actor_key(chosen), f'{label(chosen)}, say "Hail".',
                    actor=chosen, action='say', utterance='hail')
        if all(not (s.actor == chosen and s.action == 'say' and ident(s.utterance) == 'hail')
               for s in self.steps):
            self.steps.insert(0, hail)

    def plan(self, reward: int) -> list[Step]:
        try:
            self.acquire(reward)
        except AcquisitionCycle as exc:
            self.errors.append(f"No acyclic acquisition route: {exc}")
        self.introduce()
        return self.steps


def speech_for_step(g: Graph, step: Step) -> list[str]:
    if not step.actor or step.action not in ('hand', 'say'):
        return []
    chains = g.conversation(step.actor, step.payload)
    result: list[str] = []
    if step.action == 'say':
        for chain in chains:
            for turn in chain.get('turns', []):
                if ident(str(turn.get('input') or '')) != ident(step.utterance):
                    continue
                result.append(f'    - Player: "{step.utterance}"')
                for reply in turn.get('reply') or []:
                    result.append(f'      - NPC {reply.get("channel", "say")}: {reply.get("text", "")}')
                    for guard in reply.get('guards') or []:
                        result.append(f'        - Reply guard: `{guard}`')
                for guard in turn.get('guards') or []:
                    result.append(f'      - Condition: `{guard}`')
                if ident(step.utterance) != 'hail':
                    for edge in chain.get('transitions') or []:
                        if ident(str(edge.get('_to') or '')) != ident(step.utterance):
                            continue
                        basis = str(edge.get('basis') or '')
                        origin = str(edge.get('_from') or '')
                        if basis in ('explicit_mention', 'conversation_sequence'):
                            certainty = 'explicit prompt' if basis == 'explicit_mention' else 'sequence only; unverified'
                            result.append(f'      - Linked from "{origin}" ({certainty}).')
                return result
        speech = g.says.get((actor_key(step.actor), ident(step.utterance)))
        return [f'    - NPC say: {speech}'] if speech else []
    for chain in chains:
        for speech in chain.get('context_speech') or []:
            if str(speech.get('event') or '').lower() not in ('event_item', 'event_trade'):
                continue
            guards = list(map(str, speech.get('guards') or []))
            ids = set().union(*(guard_item_ids(guard) for guard in guards)) if guards else set()
            if step.payload and set(step.payload) != ids:
                continue
            # A broad unguarded speech branch cannot be attributed to this
            # specific hand-in. Exclude it rather than implying causality.
            if not ids:
                continue
            result.append(f'    - {speech.get("event")} NPC {speech.get("channel", "say")}: {speech.get("text", "")}')
            for guard in guards:
                result.append(f'      - Event guard: `{guard}`')
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
    out = [f'# {class_name.title()} — Epic Quest Walkthrough', '',
           'Generated directly from quest-graph item rewards. Unresolved dependencies are marked, not inferred.', '']
    # The first published occurrence of each graph action owns its full dialogue.
    # Stable Step keys encode the action/group, not human-readable Markdown.
    published: dict[str, tuple[int, int, int]] = {}
    previous_plans: dict[int, set[str]] = {}
    for era, rewards in REWARDS[class_name].items():
        out.extend([f'## Epic {era}', ''])
        for reward in rewards:
            # Plan *independently* for each reward. Never reuse planner.done_items:
            # doing so would skip genuine dependencies and conceal cycles.
            planner = Planner(g, catalog)
            steps = planner.plan(reward)
            out.extend([f'### {g.name(reward)}', '', f'<a id="{_anchor(reward, g)}"></a>', ''])
            planned_keys = {step.key for step in steps}
            # A complete previously documented reward path is a single
            # prerequisite, not dozens of interleaved references. Prefer the
            # maximal earlier paths: Heartwood subsumes the two Ranger 1.0
            # epics, so Aurora needs only the Heartwood route linked here.
            # Synthetic introductory hails are presentation, not causal
            # prerequisites. A nested reward may open with a different NPC.
            causal_keys = {k for k in planned_keys if not k.startswith("introduction:")}
            included = [r for r, keys in previous_plans.items()
                        if keys and {k for k in keys if not k.startswith("introduction:")}.issubset(causal_keys)]
            maximal = [r for r in included
                       if not any(r != other and previous_plans[r] < previous_plans[other]
                                  for other in included)]
            covered = set().union(*(previous_plans[r] for r in maximal)) if maximal else set()
            if maximal:
                links = ', '.join(f'[{g.name(r)}](#{_anchor(r, g)})' for r in maximal)
                out.extend([f'**Earlier reward routes required by this graph path:** {links}.',
                            'Revisit those instructions if another copy of a consumed item is needed.', ''])
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
                    entries.append(('shared', previous, None))
                else:
                    entries.append(('action', step, None))
                    new_keys.add(step.key)
            number = 0
            i = 0
            while i < len(entries):
                kind, value, _ = entries[i]
                if kind == 'shared':
                    if not isinstance(value, tuple):
                        continue
                    first = value
                    last = first
                    j = i + 1
                    while j < len(entries) and entries[j][0] == 'shared':
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
                    out.append(f'{number}. {_shared_reference(g, first, last)}')
                    i = j
                    continue
                if not isinstance(value, Step):
                    continue
                step = value
                number += 1
                out.append(f'{number}. {step.text}')
                out.extend(speech_for_step(g, step))
                # Register only printed actions. References always resolve to a
                # real step, never to another reference (no reference chains).
                published.setdefault(step.key, (reward, number, len(out)))
                i += 1
            previous_plans[reward] = planned_keys
            if planner.errors:
                out.extend(['', '**Unresolved graph dependencies:**'])
                out.extend(f'- {e}' for e in dict.fromkeys(planner.errors))
            # Final rewards may come from a corpse rather than a quest hand-in.
            # A loot action with the reward's item ID is equally verified.
            if not any(str(reward) in step.text and (
                'Gives ' in step.text or 'Produces ' in step.text or
                step.key.startswith((
                    'kill-loot:', 
                    'catalog-drop:', 
                    'loot:',
                    'item-source:loot:', 
                    'item-source:spell:',
                    'summon-spell:',
                ))
            ) for step in steps):
                out.append(f'**Unverified final reward:** {g.name(reward)}')
            out.append('')
    return '\n'.join(out).rstrip() + '\n'


def main(argv: list[str] | None = None) -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--graph', type=Path, default=Path.home() / '.eqclient' / 'quest_graph.jsonl')
    p.add_argument('--class', dest='class_name', required=True, choices=sorted(REWARDS))
    p.add_argument('--out', type=Path, default=Path('.epics'))
    p.add_argument('--drops', type=Path, help='Optional explicit drops.jsonl (for testing)')
    p.add_argument('--merchants', type=Path, help='Optional explicit merchants.jsonl (for testing)')
    p.add_argument('--recipes', type=Path, help='Optional explicit recipes.jsonl (for testing)')
    args = p.parse_args(argv)
    g = Graph(args.graph)
    catalog = AcquisitionCatalog(args.drops, args.merchants, args.recipes)
    args.out.mkdir(parents=True, exist_ok=True)
    path = args.out / f'{args.class_name}.md'
    content = render(g, args.class_name, catalog)
    path.write_text(content, encoding='utf-8')
    print(f'{path} ({len(content.splitlines())} lines)')


if __name__ == '__main__':
    main()
