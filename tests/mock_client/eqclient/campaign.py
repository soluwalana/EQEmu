"""Obtain-stack campaign planner. Goals are item ids; components nest via push/pop.

Decomposition mirrors `.epics/write_epics.py` forward():
NPC givers before recipes, hand-in needs before the give, container before
consumes, skip refund/recombine recipes, prefer class-flag-gated sources.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field

from eqclient.camps import zone_reachable
from eqclient.conduct import _WORLD_CONTAINER
from eqclient.epics import CLASS_FLAGS, can_obtain, flag_satisfied

# A stack layer, not an item. counts[FARM] is the copper still needed.
FARM = -1


@dataclass
class CampaignStep:
    """One atomic action toward the active obtain goal."""

    kind: str  # hail, hand, kill, loot, craft, buy, forage, fish, travel, level, safe, bank, sell, done, blocked
    item_id: int = 0
    zone: str = ""
    npc: str = ""
    word: str = ""
    recipe_id: int = 0
    count: int = 1
    text: str = ""


@dataclass
class _Index:
    edges: list[dict]
    gives: dict[int, list[dict]]
    produces: dict[int, list[int]]
    recipe: dict[int, dict]
    by_from: dict[str, list[dict]]
    by_group: dict[str, list[dict]]
    sets_of: dict[str, list[dict]]


@dataclass
class Campaign:
    """Stack of item ids. Top is the active obtain goal."""

    class_id: int
    race_id: int = 0
    stack: list[int] = field(default_factory=list)
    counts: dict[int, int] = field(default_factory=dict)  # required stack counts; default 1
    # Practice products: sell these (not protect) once made / when bags fill.
    sell_after: set[int] = field(default_factory=set)
    # Non-root layers with no source. Popped so they cannot sit on the epic.
    skipped: set[int] = field(default_factory=set)
    # Held items that must not auto-pop until the agent finishes a side step
    # (e.g. inventorygive a bot spell scroll). Cleared by the agent after hand-off.
    hold_until: set[int] = field(default_factory=set)
    _index_key: object = field(default=None, repr=False)
    _index: _Index | None = field(default=None, repr=False)

    def set_goal(self, item_id: int, count: int = 1, graph=None) -> bool:
        """Replace the entire stack with one root goal (epic / env bootstrap)."""
        if item_id <= 0:
            return False
        if graph is not None and not can_obtain(item_id, self.class_id, self.race_id, graph):
            return False
        self.stack = [item_id]
        self.counts = {item_id: max(1, count)}
        self.sell_after.clear()
        self.skipped.clear()
        return True

    def assign_goal(self, item_id: int, count: int = 1, graph=None) -> bool:
        """Push a player/agent assign on top without erasing prior goals.

        Prior roots stay below; nested campaign fetches still push above this.
        """
        if item_id <= 0 or item_id in self.skipped:
            return False
        if graph is not None and not can_obtain(item_id, self.class_id, self.race_id, graph):
            return False
        self.push(item_id, count)
        return True

    def load_stack(self, stack: list[int], counts: dict[int, int] | None = None) -> None:
        """Restore a journaled stack (bottom→top)."""
        self.stack = [int(item_id) for item_id in stack if int(item_id) > 0 or int(item_id) == FARM]
        self.counts = {int(item_id): max(1, int(count)) for item_id, count in (counts or {}).items()}
        for item_id in self.stack:
            self.counts.setdefault(item_id, 1)

    def push(self, item_id: int, count: int = 1) -> None:
        if item_id == 0 or (item_id < 0 and item_id != FARM):
            return
        if self.stack and self.stack[-1] == item_id:
            self.counts[item_id] = max(self.counts.get(item_id, 1), count)
            return
        self.stack.append(item_id)
        self.counts[item_id] = max(1, count)

    def pop(self) -> int | None:
        if not self.stack:
            return None
        item_id = self.stack.pop()
        self.counts.pop(item_id, None)
        return item_id

    def peek(self) -> int | None:
        return self.stack[-1] if self.stack else None

    def complete(self) -> bool:
        return not self.stack

    def held_enough(self, item_id: int, inventory_counts: dict[int, int]) -> bool:
        if item_id == FARM:
            return False
        need = self.counts.get(item_id, 1)
        return inventory_counts.get(item_id, 0) >= need

    def next_step(
        self,
        graph,
        inventory_counts: dict[int, int],
        flags: dict[str, int],
        level: int = 0,
        here: str = "",
        bag_full: bool = False,
        copper: int | None = None,
        merchants=None,
        recipes=None,
        drops=None,
        factions=None,
        skills: dict[int, int] | None = None,
    ) -> CampaignStep:
        """Expand the top goal into one step. Missing prereq items are pushed."""
        sold = self._sell_practice(inventory_counts, bag_full=bag_full, finish=False)
        if sold is not None:
            return sold
        while self.stack and self.held_enough(self.stack[-1], inventory_counts):
            item_id = self.stack[-1]
            if item_id in self.hold_until:
                break
            have = int(inventory_counts.get(item_id, 0) or 0)
            if have > 0 and item_id in self.sell_after:
                # Finished practice wave — sell the products, then drop the layer.
                # Keep sell_after until inventory is cleared (retry if shop fails).
                self.pop()
                return CampaignStep(kind="sell", item_id=item_id, count=have, text="practice")
            self.pop()
        if bag_full:
            return CampaignStep(kind="safe", text="inventory")
        if not self.stack:
            # Leftover practice products after the wave popped elsewhere.
            sold = self._sell_practice(inventory_counts, bag_full=False, finish=True)
            if sold is not None:
                return sold
            return CampaignStep(kind="done")
        # Clear sell markers once the products are gone.
        for item_id in list(self.sell_after):
            if item_id not in self.stack and int(inventory_counts.get(item_id, 0) or 0) <= 0:
                self.sell_after.discard(item_id)
        index = self._indexes(graph)
        goal = self.stack[0]
        items = getattr(graph, "items", {}) or {}
        for _ in range(32):
            item_id = self.peek()
            if item_id is None:
                return CampaignStep(kind="done")
            if item_id == FARM:
                need = self.counts.get(FARM, 0)
                if copper is not None and copper >= need:
                    self.pop()
                    continue
                return CampaignStep(kind="farm", count=need, text=str(need))
            if self.held_enough(item_id, inventory_counts):
                if item_id in self.hold_until:
                    # Waiting on inventorygive (or similar) — keep the goal visible.
                    return CampaignStep(
                        kind="have",
                        item_id=item_id,
                        count=self.counts.get(item_id, 1),
                        text="hold_until",
                    )
                have = int(inventory_counts.get(item_id, 0) or 0)
                if have > 0 and item_id in self.sell_after:
                    self.pop()
                    return CampaignStep(kind="sell", item_id=item_id, count=have, text="practice")
                self.pop()
                continue
            # Mid-practice: dump made products so bags stay open for more combines.
            if item_id in self.sell_after:
                have = int(inventory_counts.get(item_id, 0) or 0)
                need = self.counts.get(item_id, 1)
                if have >= 20 and have < need:
                    self.counts[item_id] = max(1, need - have)
                    return CampaignStep(kind="sell", item_id=item_id, count=have, text="practice")
            step = self._expand(
                item_id,
                goal,
                index,
                items,
                inventory_counts,
                flags,
                level,
                here,
                copper,
                merchants,
                recipes,
                drops,
                factions,
                skills or {},
            )
            if step.kind == "need_item" and step.item_id and step.item_id != item_id:
                if step.item_id in self.skipped:
                    root = self.stack[0] if self.stack else item_id
                    if item_id != root:
                        self.skipped.add(item_id)
                        self.pop()
                        continue
                    # The root still needs it. Put it back and stop, so a real
                    # component stays visible instead of being dropped for good.
                    self.skipped.discard(step.item_id)
                    self.push(step.item_id, step.count)
                    return CampaignStep(kind="blocked", item_id=step.item_id, text="no_source")
                if step.text and "@" in step.text:
                    self.sell_after.add(step.item_id)
                self.push(step.item_id, step.count)
                continue
            if step.kind == "need_farm":
                self.push(FARM, step.count)
                continue
            if step.kind == "blocked":
                root = self.stack[0] if self.stack else item_id
                if item_id != root:
                    self.skipped.add(item_id)
                    self.pop()
                    continue
            return step
        return CampaignStep(kind="blocked", item_id=self.peek() or 0, text="nesting")

    def _sell_practice(
        self,
        inventory_counts: dict[int, int],
        *,
        bag_full: bool = False,
        finish: bool = False,
    ) -> CampaignStep | None:
        """Sell practice products — bags full mid-wave, or leftovers after pop."""
        if not self.sell_after:
            return None
        if not bag_full and not finish:
            return None
        for item_id in list(self.sell_after):
            have = int(inventory_counts.get(item_id, 0) or 0)
            if have <= 0:
                if item_id not in self.stack:
                    self.sell_after.discard(item_id)
                continue
            if item_id in self.stack:
                if not bag_full:
                    continue
                # Credit sold units toward the practice quota so we don't remake them.
                need = self.counts.get(item_id, 1)
                remaining = need - have
                if remaining <= 0:
                    if self.peek() == item_id:
                        self.pop()
                    self.sell_after.discard(item_id)
                else:
                    self.counts[item_id] = remaining
            else:
                self.sell_after.discard(item_id)
            return CampaignStep(kind="sell", item_id=item_id, count=have, text="practice")
        return None

    def _indexes(self, graph) -> _Index:
        edges = getattr(graph, "edges", None)
        key = (id(graph), id(edges), len(edges) if edges is not None else 0)
        if self._index is not None and self._index_key == key:
            return self._index
        self._index_key = key
        self._index = _build_indexes(list(edges or ()))
        return self._index

    def _expand(
        self,
        item_id: int,
        goal: int,
        index: _Index,
        items: dict,
        inventory_counts: dict[int, int],
        flags: dict[str, int],
        level: int,
        here: str,
        copper: int | None = None,
        merchants=None,
        recipes=None,
        drops=None,
        factions=None,
        skills: dict[int, int] | None = None,
    ) -> CampaignStep:
        skills = skills or {}
        class_flags = set(CLASS_FLAGS.get(self.class_id, ()))

        # 1. real_givers — NPC paths beat tradeskill recipes for epics.
        for edge in _real_givers(index, item_id, class_flags):
            group = str(edge.get("group") or edge.get("from") or "")
            zone, npc = _zone_npc(group) if "/" in group.split("#")[0] else _zone_npc(str(edge.get("from") or ""))
            if not zone:
                zone, npc = _zone_npc(str(edge.get("from") or ""))
            if not _flags_ok(index.edges, group, flags):
                unlock = _unlock_flag(index.edges, group, flags, inventory_counts, here, self.stack, level)
                if unlock is not None:
                    return unlock
            missing = _missing_needs(index.edges, group, inventory_counts)
            if missing is None:
                for hand_id in _handed(index, edge):
                    if inventory_counts.get(hand_id, 0) < 1 and hand_id not in self.stack:
                        missing = (hand_id, 1)
                        break
            if missing:
                mid, mcount = missing
                if mid not in self.stack:
                    return CampaignStep(kind="need_item", item_id=mid, count=mcount, zone=zone, npc=npc)
            if not _flags_ok(index.edges, group, flags):
                continue
            faction = _faction_need(index.edges, group)
            if faction is not None and not _standing_ok(faction, flags, zone, npc):
                raised = _raise_faction(
                    index, faction, item_id, zone, npc, inventory_counts, flags, here, self.stack, level
                )
                if raised is not None:
                    return raised
                farmed = _faction_farm_step(factions, faction, item_id, zone, npc, here, level)
                if farmed is not None:
                    return farmed
                return CampaignStep(kind="faction", item_id=item_id, zone=zone, npc=npc, text=faction)
            if zone and here and zone != (here or "").lower():
                return _travel_to(
                    item_id,
                    zone,
                    npc,
                    level,
                    flags=flags,
                    edges=index.edges,
                    held=inventory_counts,
                    here=here,
                    stack=self.stack,
                )
            word = _hail_word(group)
            # Only this script's turn-ins — not every receives row on the same NPC
            # (Favor must stay a hail even when Kargek also has hand-in scripts).
            given = _handed(index, edge) or _hand_items(group)
            if given:
                return CampaignStep(
                    kind="hand",
                    item_id=item_id,
                    zone=zone,
                    npc=npc,
                    word=word,
                    text=_turn_in(word, given),
                    count=len(given),
                )
            return CampaignStep(kind="hail", item_id=item_id, zone=zone, npc=npc, word=word or "Hail")

        # 2. creating() — skip refund/recombine; container before consumes.
        for rid in _creating(index, item_id, class_flags):
            info = index.recipe.get(rid) or {}
            if goal in _recipe_inputs(info):
                continue
            consumes = list(info.get("consumes") or [])
            if any(comp_id in self.stack for comp_id, _count in consumes):
                continue
            # Skill up (and its bulk mats) before gathering the goal combine's own components.
            skill_gate = _skill_gate(recipes, rid, skills, item_id, inventory_counts, self.stack)
            if skill_gate is not None:
                return skill_gate
            container = int(info.get("container") or 0)
            if container and inventory_counts.get(container, 0) < 1 and container not in self.stack:
                return CampaignStep(kind="need_item", item_id=container, count=1, recipe_id=rid)
            for comp_id, count in consumes:
                if inventory_counts.get(comp_id, 0) < count and comp_id not in self.stack:
                    return CampaignStep(kind="need_item", item_id=comp_id, count=count, recipe_id=rid)
            return CampaignStep(kind="craft", item_id=item_id, recipe_id=rid)

        # 3. Leaf: loot / ground / buy / faction / key / encounter / merchant / level.
        return _leaf_step(
            item_id,
            index,
            items,
            level,
            here,
            self.counts.get(item_id, 1),
            copper,
            merchants,
            recipes,
            drops,
            inventory_counts,
            self.stack,
            flags,
            factions,
            skills,
        )


def _build_indexes(edges: list[dict]) -> _Index:
    gives: dict[int, list[dict]] = defaultdict(list)
    produces: dict[int, list[int]] = defaultdict(list)
    recipe: dict[int, dict] = defaultdict(lambda: {"consumes": [], "container": 0, "products": []})
    by_from: dict[str, list[dict]] = defaultdict(list)
    by_group: dict[str, list[dict]] = defaultdict(list)
    sets_of: dict[str, list[dict]] = defaultdict(list)
    for edge in edges:
        source = str(edge.get("from") or "")
        group = str(edge.get("group") or "")
        if source:
            by_from[source].append(edge)
        if group:
            by_group[group].append(edge)
        rel = edge.get("rel")
        to = str(edge.get("to") or "")
        if rel == "gives" and to.startswith("item:"):
            gives[int(to.split(":", 1)[1])].append(edge)
        elif rel == "produces" and source.startswith("recipe:") and to.startswith("item:"):
            rid = int(source.split(":", 1)[1])
            item_id = int(to.split(":", 1)[1])
            produces[item_id].append(rid)
            products = recipe[rid]["products"]
            count = int(edge.get("count") or 1)
            products.append((item_id, count))
        elif rel == "consumes" and source.startswith("recipe:") and to.startswith("item:"):
            rid = int(source.split(":", 1)[1])
            recipe[rid]["consumes"].append((int(to.split(":", 1)[1]), int(edge.get("count") or 1)))
        elif rel == "container" and source.startswith("recipe:") and to.startswith("item:"):
            rid = int(source.split(":", 1)[1])
            recipe[rid]["container"] = int(to.split(":", 1)[1])
        elif rel == "sets" and to.startswith("flag:"):
            name = to.split(":", 1)[1]
            flag = str(edge.get("flag") or name)
            sets_of[flag].append(edge)
        elif rel == "sets" and to.startswith("faction:"):
            sets_of[to].append(edge)
    return _Index(
        edges=edges,
        gives=dict(gives),
        produces=dict(produces),
        recipe=dict(recipe),
        by_from=dict(by_from),
        by_group=dict(by_group),
        sets_of=dict(sets_of),
    )


def _recipe_inputs(info: dict) -> set[int]:
    found = {int(comp) for comp, _count in info.get("consumes") or []}
    if info.get("container"):
        found.add(int(info["container"]))
    return found


def _recipe_refund(index: _Index, edge: dict, item_id: int) -> bool:
    """A combine that hands its container/components back is not how you obtain them."""
    source = str(edge.get("group") or edge.get("from") or "")
    if "#recipe:" not in source:
        return False
    tail = source.rsplit(":", 1)[-1]
    if not tail.isdigit():
        return False
    info = index.recipe.get(int(tail))
    return bool(info) and int(item_id) in _recipe_inputs(info)


def _handed(index: _Index, edge: dict) -> list[int]:
    source = str(edge.get("group") or edge.get("from") or "")
    found: list[int] = []
    for row in index.by_group.get(source, []) + index.by_from.get(source, []):
        if row.get("rel") != "receives" or not str(row.get("to", "")).startswith("item:"):
            continue
        needed = int(row["to"].split(":", 1)[1])
        if needed not in found:
            found.append(needed)
    if not found:
        found = _hand_items(source)
    return found


def _prefers(index: _Index, edge: dict, flags: set[str]) -> bool:
    group = edge.get("group") or ""
    rows = (
        index.by_from.get(group, [])
        + index.by_from.get(str(edge.get("from") or ""), [])
        + index.by_group.get(group, [])
    )
    for row in rows:
        if row.get("rel") == "needs" and row.get("flag") in flags:
            return True
        to = str(row.get("to") or "")
        if row.get("rel") == "needs" and to.startswith("flag:") and to.split(":", 1)[1] in flags:
            return True
    return False


def _creating(index: _Index, item_id: int, flags: set[str]) -> list[int]:
    """Recipes that make this item. A combine that hands it back plus something new does not."""
    made: list[int] = []
    for rid in index.produces.get(item_id, []):
        if item_id in _recipe_inputs(index.recipe.get(rid) or {}) or rid in made:
            continue
        made.append(rid)
    linked: list[int] = []
    for rid in made:
        for flag in flags:
            for edge in index.sets_of.get(flag, ()):
                source = str(edge.get("from") or "")
                if f"#recipe:{rid}" in source:
                    linked.append(rid)
                    break
            if rid in linked:
                break
    if linked:
        return linked
    if len(made) <= 2:
        return made
    return []


def _real_givers(index: _Index, item_id: int, flags: set[str]) -> list[dict]:
    givers = [
        edge
        for edge in index.gives.get(item_id, [])
        if not _recipe_refund(index, edge, item_id) and item_id not in _handed(index, edge)
    ]
    gated = [edge for edge in givers if _prefers(index, edge, flags)]
    return (gated or givers)[:6]


def _travel_gate(
    item_id: int,
    zone: str,
    npc: str,
    level: int,
    *,
    flags: dict[str, int] | None = None,
    edges=None,
    held: dict[int, int] | None = None,
    here: str = "",
    stack: list[int] | None = None,
) -> CampaignStep | None:
    """Level / plane-flag gates before travel. Missing zoneflag → unlock intentions."""
    reason = zone_reachable(zone, level)
    if reason:
        if reason.startswith("level:"):
            return CampaignStep(kind="level", item_id=item_id, zone=zone, npc=npc, text=reason.split(":", 1)[1])
        return CampaignStep(kind="blocked", item_id=item_id, zone=zone, npc=npc, text=reason)
    if edges is not None and flags is not None and zone:
        group = f"zone:{(zone or '').lower()}"
        if not _flags_ok(edges, group, flags):
            unlock = _unlock_flag(edges, group, flags, held or {}, here, list(stack or []), level)
            if unlock is not None:
                if item_id and not unlock.item_id:
                    unlock.item_id = item_id
                return unlock
            unmet = _unmet_flag(edges, group, flags)
            tip = unmet[0] if unmet else f"zoneflag:{zone}"
            return CampaignStep(kind="blocked", item_id=item_id, zone=zone, npc=npc, text=tip)
    return None


def _travel_to(
    item_id: int,
    zone: str,
    npc: str,
    level: int,
    *,
    flags: dict[str, int] | None = None,
    edges=None,
    held: dict[int, int] | None = None,
    here: str = "",
    stack: list[int] | None = None,
    text: str = "",
) -> CampaignStep:
    """Travel, or the intention that unlocks a missing plane/zone flag first."""
    gated = _travel_gate(item_id, zone, npc, level, flags=flags, edges=edges, held=held, here=here, stack=stack)
    if gated is not None:
        if text and not gated.text:
            gated.text = text
        return gated
    return CampaignStep(kind="travel", item_id=item_id, zone=zone, npc=npc, text=text)


def _faction_need(edges, group: str) -> str | None:
    """Return 'faction:id@at' when the script gates this step on standing."""
    for edge in edges:
        if edge.get("rel") != "needs":
            continue
        if not (
            _groups_match(str(edge.get("group") or ""), group) or _groups_match(str(edge.get("from") or ""), group)
        ):
            continue
        to = str(edge.get("to") or "")
        if to.startswith("faction:"):
            at = str(edge.get("at") or "")
            return f"{to}@{at}" if at else to
    return None


def stack_faction_ids(campaign, graph) -> set[int]:
    """Numeric faction ids gated on the current obtain stack (and nested hand-ins).

    Used to hard-deny attacking NPCs whose primary faction is one we still need
    (Qeynos/Freeport guards, etc.).
    """
    found: set[int] = set()
    if campaign is None or graph is None:
        return found
    try:
        index = campaign._indexes(graph)
    except Exception:
        return found
    queue = [int(item_id) for item_id in (campaign.stack or ()) if int(item_id) > 0]
    seen: set[int] = set()
    while queue:
        item_id = queue.pop()
        if item_id in seen:
            continue
        seen.add(item_id)
        for edge in index.gives.get(item_id, ()):
            group = str(edge.get("group") or edge.get("from") or "")
            spec = _faction_need(index.edges, group)
            if spec:
                fid, _at = _parse_faction_spec(spec)
                if fid.isdigit():
                    found.add(int(fid))
            for hand_id in _handed(index, edge):
                if hand_id > 0:
                    queue.append(int(hand_id))
        for rid in index.produces.get(item_id, ()):
            info = index.recipe.get(rid) or {}
            for comp_id, _count in info.get("consumes") or ():
                if int(comp_id) > 0:
                    queue.append(int(comp_id))
            container = int(info.get("container") or 0)
            if container > 0:
                queue.append(container)
    return found


def _parse_faction_spec(spec: str) -> tuple[str, str]:
    """Split 'faction:404@>=43' into ('404', '>=43')."""
    body = spec[8:] if spec.startswith("faction:") else spec
    if "@" in body:
        fid, _, at = body.partition("@")
        return fid, at
    return body, ""


def _standing_key(faction_id: str, zone: str = "", npc: str = "") -> str:
    """Journal/flag key for a faction standing value."""
    if faction_id == "primary":
        who = " ".join((npc or "").lower().replace("_", " ").replace("#", " ").split())
        place = f"{(zone or '').lower()}/{who}".strip("/")
        return f"faction:primary:{place}" if place else "faction:primary"
    return f"faction:{faction_id}"


def _standing_ok(spec: str, flags: dict[str, int], zone: str = "", npc: str = "") -> bool:
    """True when journaled standing already meets the gate."""
    faction_id, at = _parse_faction_spec(spec)
    if not at:
        return _standing_key(faction_id, zone, npc) in flags or f"faction:{faction_id}" in flags
    keys = [_standing_key(faction_id, zone, npc)]
    if faction_id == "primary":
        keys.append("faction:primary")
    else:
        keys.append(f"faction:{faction_id}")
    for key in keys:
        if key in flags and flag_satisfied(key, at, flags):
            return True
    return False


def _raise_faction(
    index: _Index,
    spec: str,
    item_id: int,
    zone: str,
    npc: str,
    held: dict[int, int],
    flags: dict[str, int],
    here: str,
    stack: list[int],
    level: int = 0,
) -> CampaignStep | None:
    """Turn an unmet faction gate into a +faction hand-in (or its missing items).

    Never points at killing the gated quest NPC. Numeric factions prefer positive
    `sets` edges from the graph; primary standing is raised by farming hostiles
    (handled by the agent on a bare faction step).
    """
    faction_id, _at = _parse_faction_spec(spec)
    if faction_id == "primary" or not faction_id.isdigit():
        return None
    target = f"faction:{faction_id}"
    candidates: list[tuple[int, dict]] = []
    for edge in index.sets_of.get(target, ()):
        try:
            value = int(edge.get("value") or 0)
        except (TypeError, ValueError):
            value = 0
        if value <= 0:
            continue
        set_group = str(edge.get("group") or edge.get("from") or "")
        # Skip raise paths that themselves require this faction unmet — dead end.
        gated = _faction_need(index.edges, set_group)
        if gated is not None:
            gid, _ = _parse_faction_spec(gated)
            if gid == faction_id and not _standing_ok(gated, flags, *_zone_npc(set_group)):
                continue
        candidates.append((value, edge))
    if not candidates:
        return None

    # Prefer larger gains, then paths whose hand items we already hold.
    def _rank(pair: tuple[int, dict]) -> tuple[int, int]:
        value, edge = pair
        set_group = str(edge.get("group") or edge.get("from") or "")
        missing = _missing_needs(index.edges, set_group, held)
        ready = 0 if missing else 1
        return (ready, value)

    candidates.sort(key=_rank, reverse=True)
    _value, edge = candidates[0]
    source = str(edge.get("from") or edge.get("group") or "")
    set_group = str(edge.get("group") or source)
    raise_zone, raise_npc = _zone_npc(source)
    missing = _missing_needs(index.edges, set_group, held) or _missing_needs(index.edges, source, held)
    if missing is None:
        for hand_id in _handed_ids(index.edges, set_group) or _hand_items(source) or _hand_items(set_group):
            if held.get(hand_id, 0) < 1:
                missing = (hand_id, 1)
                break
    if missing:
        mid, mcount = missing
        if mid not in stack:
            return CampaignStep(
                kind="need_item",
                item_id=mid,
                count=mcount,
                zone=raise_zone,
                npc=raise_npc,
                text=spec,
            )
    if raise_zone and here and raise_zone != (here or "").lower():
        return _travel_to(
            item_id,
            raise_zone,
            raise_npc,
            level,
            flags=flags,
            edges=index.edges,
            held=held,
            here=here,
            stack=stack,
            text=spec,
        )
    word = _hail_word(source)
    if _handed_ids(index.edges, set_group) or _hand_items(source) or _hand_items(set_group):
        return CampaignStep(
            kind="hand",
            item_id=item_id,
            zone=raise_zone,
            npc=raise_npc,
            word=word,
            text=spec,
        )
    return CampaignStep(
        kind="hail",
        item_id=item_id,
        zone=raise_zone,
        npc=raise_npc,
        word=word or "Hail",
        text=spec,
    )


def _faction_farm_step(
    factions,
    spec: str,
    item_id: int,
    quest_zone: str,
    quest_npc: str,
    here: str,
    level: int = 0,
) -> CampaignStep | None:
    """Travel to the densest +faction kill zone and farm those NPCs — never the quest NPC."""
    if factions is None:
        return None
    faction_id, _at = _parse_faction_spec(spec)
    if faction_id == "primary":
        fac_id = int(factions.primary(quest_zone, quest_npc) or 0)
    elif faction_id.isdigit():
        fac_id = int(faction_id)
    else:
        return None
    if not fac_id:
        return None
    hit = factions.farm(fac_id, here)
    if hit is None:
        return None
    farm_zone = factions.densest_zone(fac_id) or hit.zone
    quest_tag = f"@{quest_zone}/{quest_npc}".strip("/")
    if farm_zone and here and farm_zone != (here or "").lower():
        gated = _travel_gate(item_id, farm_zone, hit.name, level)
        if gated is not None:
            gated.text = spec
            gated.word = quest_tag
            return gated
        return CampaignStep(
            kind="travel",
            item_id=item_id,
            zone=farm_zone,
            npc=hit.name,
            word=quest_tag,
            text=spec,
        )
    return CampaignStep(
        kind="faction",
        item_id=item_id,
        zone=farm_zone,
        npc=hit.name,
        word=quest_tag,
        text=spec,
    )


# Practice wave size (result items). Component stacks = this × recipe comps via _recipe_step.
_SKILL_PRACTICE = 50
# Back-compat alias for callers/tests that imported the old name.
_SKILL_BULK = _SKILL_PRACTICE


def _skill_gate(
    recipes,
    recipe_id: int,
    skills: dict[int, int],
    item_id: int,
    held: dict[int, int] | None = None,
    stack: list[int] | None = None,
) -> CampaignStep | None:
    """When skill is short, push the practice result (~50); planner nests component stacks.

    Component counts come from _recipe_step (practice_count × comps per combine). After
    the wave (or mid-run when bags fill), Campaign sells those practice products.
    """
    if recipes is None or not recipe_id:
        return None
    by_id = getattr(recipes, "by_id", None) or {}
    recipe = by_id.get(recipe_id)
    if recipe is None:
        return None
    skill_id = int(getattr(recipe, "skill", 0) or 0)
    if not skill_id:
        return None
    want = max(int(getattr(recipe, "skillneeded", 0) or 0), int(getattr(recipe, "trivial", 0) or 0))
    if want <= 0:
        return None
    current = int(skills.get(skill_id, 0) or 0)
    held = held or {}
    stack = stack or []
    # Fishing / forage skill up by using the ability, not a combine.
    if skill_id in {27, 55}:
        if current >= want:
            return None
        return CampaignStep(kind="skill", item_id=item_id, recipe_id=recipe_id, text=f"{skill_id}@{want}", count=want)

    practice = recipes.practice(skill_id, current, want) if hasattr(recipes, "practice") else None
    if practice is not None and practice.id == recipe_id:
        # Expanding the practice result itself: fetch its comps / craft, no nested gate.
        return None

    # Burn leftover practice stacks (not the goal) after skill is met.
    stocked = _practice_with_stock(recipes, skill_id, held, exclude=recipe_id)
    if current >= want:
        if stocked is None:
            return None
        return CampaignStep(
            kind="skill",
            item_id=item_id,
            recipe_id=stocked.id,
            text=f"{skill_id}@{want}",
            count=want,
        )

    if practice is None:
        if int(getattr(recipe, "trivial", 0) or 0) <= current:
            if stocked is not None:
                return CampaignStep(
                    kind="skill",
                    item_id=item_id,
                    recipe_id=stocked.id,
                    text=f"{skill_id}@{want}",
                    count=want,
                )
            return CampaignStep(kind="blocked", item_id=item_id, recipe_id=recipe_id, text=f"skill:{skill_id}@{want}")
        # Goal recipe itself is the skill-up combine — practice its result.
        practice = recipe

    practice_trivial = int(getattr(practice, "trivial", 0) or 0)
    if practice_trivial <= current:
        if stocked is not None:
            return CampaignStep(
                kind="skill",
                item_id=item_id,
                recipe_id=stocked.id,
                text=f"{skill_id}@{want}",
                count=want,
            )
        return CampaignStep(kind="blocked", item_id=item_id, recipe_id=recipe_id, text=f"skill:{skill_id}@{want}")

    result_id = int(getattr(practice, "result", 0) or 0)
    if not result_id:
        return CampaignStep(kind="blocked", item_id=item_id, recipe_id=recipe_id, text=f"skill:{skill_id}@{want}")
    # Already stacking or holding this practice wave — let that finish (then sell).
    if result_id in stack or held.get(result_id, 0) >= _SKILL_PRACTICE:
        return None
    if result_id == item_id:
        # Obtaining this item is the skill plan; components via normal craft expand.
        return None
    return CampaignStep(
        kind="need_item",
        item_id=result_id,
        count=_SKILL_PRACTICE,
        recipe_id=practice.id,
        text=f"{skill_id}@{want}",
    )


def _practice_with_stock(recipes, skill_id: int, held: dict[int, int], exclude: int = 0):
    """A practice recipe we can still combine from inventory (burn stacks).

    `exclude` is the goal recipe id — don't burn the mats reserved for that combine.
    """
    by_id = getattr(recipes, "by_id", None) or {}
    for rid in getattr(recipes, "by_skill", {}).get(int(skill_id), ()):
        if exclude and int(rid) == int(exclude):
            continue
        practice = by_id.get(rid)
        if practice is None or not practice.enabled or not practice.components:
            continue
        container = int(getattr(practice, "container", 0) or 0)
        if container and container not in _WORLD_CONTAINER and held.get(container, 0) < 1:
            continue
        if all(held.get(comp_id, 0) >= count for comp_id, count in practice.components):
            return practice
    return None


def _leaf_step(
    item_id: int,
    index: _Index,
    items: dict,
    level: int,
    here: str,
    count: int = 1,
    copper: int | None = None,
    merchants=None,
    recipes=None,
    drops=None,
    inventory_counts: dict | None = None,
    stack: list | None = None,
    flags: dict[str, int] | None = None,
    factions=None,
    skills: dict[int, int] | None = None,
) -> CampaignStep:
    edges = index.edges
    flags = flags or {}
    skills = skills or {}
    stack = list(stack or [])
    held = inventory_counts or {}
    info = items.get(item_id) or {}
    still = _still(count, held, item_id)
    travel_ctx = dict(flags=flags, edges=edges, held=held, here=here, stack=stack)
    for source in info.get("sources") or ():
        step = _source_step(item_id, source, here, level, held=held, stack=stack, flags=flags, edges=edges)
        if step is not None:
            step.count = still
            return step
    for edge in edges:
        rel = edge.get("rel")
        if rel not in {"loots", "grounds"} or str(edge.get("to")) != f"item:{item_id}":
            continue
        zone = str(edge.get("zone") or "").lower()
        if not zone:
            zone = str(edge.get("from") or "").split("/", 1)[0].lower()
        npc = str(edge.get("npc") or "")
        if zone and here and zone != (here or "").lower():
            return _travel_to(item_id, zone, npc, level, **travel_ctx)
        return CampaignStep(
            kind="loot",
            item_id=item_id,
            zone=zone,
            npc=npc,
            count=still,
            text="ground" if rel == "grounds" else "kill",
        )
    for edge in edges:
        if edge.get("rel") not in {"buys", "sells"}:
            continue
        if str(edge.get("to")) != f"item:{item_id}":
            continue
        zone, npc = _zone_npc(str(edge.get("from") or ""))
        if zone and here and zone != (here or "").lower():
            return _travel_to(item_id, zone, npc, level, **travel_ctx)
        return CampaignStep(kind="buy", item_id=item_id, zone=zone, npc=npc)
    for edge in edges:
        if edge.get("rel") != "needs":
            continue
        to = str(edge.get("to") or "")
        if not to.startswith("faction:"):
            continue
        if str(edge.get("item") or "") and int(edge.get("item") or 0) != item_id:
            continue
        zone, npc = _zone_npc(str(edge.get("from") or edge.get("group") or ""))
        at = str(edge.get("at") or "")
        spec = f"{to}@{at}" if at else to
        if _standing_ok(spec, flags, zone, npc):
            continue
        raised = _raise_faction(index, spec, item_id, zone, npc, held, flags, here, stack, level)
        if raised is not None:
            return raised
        farmed = _faction_farm_step(factions, spec, item_id, zone, npc, here, level)
        if farmed is not None:
            return farmed
        return CampaignStep(
            kind="faction",
            item_id=item_id,
            zone=zone,
            npc=npc or to.split(":", 1)[1],
            text=spec,
        )
    for edge in edges:
        if edge.get("rel") not in {"key", "lockpick"}:
            continue
        if str(edge.get("to")) != f"item:{item_id}" and str(edge.get("item") or "") != str(item_id):
            continue
        zone = str(edge.get("zone") or edge.get("from") or "").split("/", 1)[0].lower()
        if zone and here and zone != (here or "").lower():
            return _travel_to(item_id, zone, "", level, **travel_ctx)
        kind = "pick_lock" if edge.get("rel") == "lockpick" else "key"
        return CampaignStep(kind=kind, item_id=item_id, zone=zone, text=str(edge.get("door") or ""))
    for edge in edges:
        if edge.get("rel") not in {"encounter", "boss", "chest", "instance"}:
            continue
        if str(edge.get("to")) != f"item:{item_id}":
            continue
        zone, npc = _zone_npc(str(edge.get("from") or ""))
        if zone and here and zone != (here or "").lower():
            return _travel_to(item_id, zone, npc, level, **travel_ctx)
        return CampaignStep(
            kind=str(edge.get("rel")),
            item_id=item_id,
            zone=zone,
            npc=npc,
            text=str(edge.get("lockout") or ""),
        )
    hunted = _drop_step(item_id, drops, here, level, still, flags=flags, edges=edges, held=held, stack=stack)
    if hunted is not None:
        return hunted
    bought = _merchant_step(
        item_id, merchants, here, level, copper, still, flags=flags, edges=edges, held=held, stack=stack
    )
    if bought is not None:
        return bought
    made = _recipe_step(item_id, recipes, inventory_counts or {}, stack or [], still, skills)
    if made is not None:
        return made
    req_level = _required_level(edges, item_id)
    if req_level and level < req_level:
        return CampaignStep(kind="level", item_id=item_id, text=str(req_level))
    if level and level < 5 and not _any_source(edges, item_id, info):
        return CampaignStep(kind="level", item_id=item_id, text=str(level))
    return CampaignStep(kind="blocked", item_id=item_id, text="no_source")


def _still(count: int, held: dict, item_id: int) -> int:
    """How many of this item are still short of the stack's required count."""
    need = max(1, int(count or 1))
    have = int((held or {}).get(item_id, 0) or 0)
    return max(1, need - have)


def _drop_step(
    item_id: int,
    drops,
    here: str,
    level: int,
    count: int = 1,
    *,
    flags: dict[str, int] | None = None,
    edges=None,
    held: dict[int, int] | None = None,
    stack: list[int] | None = None,
) -> CampaignStep | None:
    """Kill the mob most likely to drop this item when no quest names the drop."""
    if drops is None:
        return None
    killer = drops.best(item_id, here)
    if killer is None:
        return None
    if killer.zone and here and killer.zone != (here or "").lower():
        step = _travel_to(
            item_id, killer.zone, killer.name, level, flags=flags, edges=edges, held=held, here=here, stack=stack
        )
        step.count = count
        return step
    return CampaignStep(kind="loot", item_id=item_id, zone=killer.zone, npc=killer.name, count=count, text="kill")


def _merchant_step(
    item_id: int,
    merchants,
    here: str,
    level: int,
    copper: int | None,
    count: int,
    *,
    flags: dict[str, int] | None = None,
    edges=None,
    held: dict[int, int] | None = None,
    stack: list[int] | None = None,
) -> CampaignStep | None:
    """Buy from the cached vendor list when nothing else produces the item."""
    if merchants is None:
        return None
    found = merchants.best(item_id, here)
    if found is None:
        return None
    seller, price = found
    cost = price * max(1, count)
    if copper is not None and cost > copper:
        return CampaignStep(kind="need_farm", item_id=item_id, count=cost, zone=seller.zone, npc=seller.name)
    if seller.zone and here and seller.zone != (here or "").lower():
        return _travel_to(
            item_id, seller.zone, seller.name, level, flags=flags, edges=edges, held=held, here=here, stack=stack
        )
    return CampaignStep(kind="buy", item_id=item_id, zone=seller.zone, npc=seller.name, count=count, text=str(cost))


def _recipe_step(
    item_id: int,
    recipes,
    inventory_counts: dict,
    stack: list,
    count: int,
    skills: dict[int, int] | None = None,
) -> CampaignStep | None:
    """Combine from the recipe cache when the item is not given, dropped, or sold."""
    if recipes is None:
        return None
    recipe = recipes.for_item(item_id)
    if recipe is None:
        return None
    # Practice bulk mats before the goal recipe's own ingredients.
    skill_gate = _skill_gate(recipes, recipe.id, skills or {}, item_id, inventory_counts, stack)
    if skill_gate is not None:
        return skill_gate
    container = recipe.container
    if (
        container
        and container not in _WORLD_CONTAINER
        and inventory_counts.get(container, 0) < 1
        and container not in stack
    ):
        return CampaignStep(kind="need_item", item_id=container, count=1, recipe_id=recipe.id)
    makes = 1
    for result_id, qty in recipe.results or ((recipe.result, 1),):
        if result_id == item_id and qty > 0:
            makes = qty
            break
    batches = max(1, (max(1, count) + makes - 1) // makes)
    for comp_id, comp_count in recipe.components:
        want = comp_count * batches
        if inventory_counts.get(comp_id, 0) < want and comp_id not in stack:
            return CampaignStep(kind="need_item", item_id=comp_id, count=want, recipe_id=recipe.id)
    return CampaignStep(kind="craft", item_id=item_id, recipe_id=recipe.id, count=count)


def _required_level(edges, item_id: int) -> int:
    for edge in edges:
        if str(edge.get("to")) != f"item:{item_id}":
            continue
        try:
            return int(edge.get("level") or 0)
        except (TypeError, ValueError):
            continue
    return 0


def _any_source(edges, item_id: int, info: dict) -> bool:
    if info.get("sources"):
        return True
    token = f"item:{item_id}"
    return any(
        str(e.get("to")) == token and e.get("rel") in {"gives", "loots", "grounds", "produces", "buys", "sells"}
        for e in edges
    )


def _zone_npc(source: str) -> tuple[str, str]:
    """Parse 'zone/npc#word' or 'zone/npc'."""
    base = source.split("#", 1)[0]
    if "/" not in base:
        return "", base
    zone, npc = base.split("/", 1)
    return zone.lower(), npc.replace("_", " ")


def _hail_word(group: str) -> str:
    if "#" in group:
        return group.split("#", 1)[1]
    return "Hail"


def _turn_in(word: str, items: list[int]) -> str:
    """Keyword, if it is not a plain hail, then every item this script takes."""
    body = "+".join(str(item) for item in items)
    token = (word or "").strip()
    if token and token.lower() not in {"hail"} and not token.lower().startswith("hand:"):
        return f"{token}|{body}" if body else token
    return body


def _hand_items(group: str) -> list[int]:
    """Item ids encoded in `#hand:a+b+c` script tags when the graph omitted needs rows."""
    word = _hail_word(group)
    if not word.lower().startswith("hand:"):
        return []
    out: list[int] = []
    for part in word.split(":", 1)[1].split("+"):
        part = part.strip()
        if part.isdigit():
            out.append(int(part))
    return out


def _script_base(group: str) -> str:
    """zone/npc#word — strip #holds:… annotations used on alternate need rows."""
    text = str(group or "")
    if "#holds:" in text:
        return text.split("#holds:", 1)[0]
    return text


def _groups_match(left: str, right: str) -> bool:
    if not left or not right:
        return False
    if left == right:
        return True
    a, b = _script_base(left), _script_base(right)
    return a == b or a.startswith(b + "#") or b.startswith(a + "#")


def _missing_needs(edges, group: str, held: dict[int, int]) -> tuple[int, int] | None:
    for edge in edges:
        if edge.get("rel") != "needs":
            continue
        if not (
            _groups_match(str(edge.get("group") or ""), group) or _groups_match(str(edge.get("from") or ""), group)
        ):
            continue
        to = str(edge.get("to") or "")
        if not to.startswith("item:"):
            continue
        item_id = int(to.split(":", 1)[1])
        count = int(edge.get("count") or 1)
        if held.get(item_id, 0) < count:
            return item_id, count
    return None


def _has_receives(edges, group: str) -> bool:
    return any(
        e.get("rel") == "receives"
        and (_groups_match(str(e.get("group") or ""), group) or _groups_match(str(e.get("from") or ""), group))
        for e in edges
    )


def _flags_ok(edges, group: str, flags: dict[str, int]) -> bool:
    for edge in edges:
        if edge.get("rel") != "needs":
            continue
        if not (
            _groups_match(str(edge.get("group") or ""), group) or _groups_match(str(edge.get("from") or ""), group)
        ):
            continue
        to = str(edge.get("to") or "")
        if not to.startswith("flag:"):
            continue
        name = to.split(":", 1)[1]
        need = str(edge.get("at") or "set")
        if not flag_satisfied(name, need, flags):
            return False
    return True


def _unmet_flag(edges, group: str, flags: dict[str, int]) -> tuple[str, str] | None:
    for edge in edges:
        if edge.get("rel") != "needs":
            continue
        if not (
            _groups_match(str(edge.get("group") or ""), group) or _groups_match(str(edge.get("from") or ""), group)
        ):
            continue
        to = str(edge.get("to") or "")
        if not to.startswith("flag:"):
            continue
        name = to.split(":", 1)[1]
        need = str(edge.get("at") or "set")
        if not flag_satisfied(name, need, flags):
            return name, need
    return None


def _unlock_flag(
    edges,
    group: str,
    flags: dict[str, int],
    held: dict[int, int],
    here: str,
    stack: list[int],
    level: int = 0,
) -> CampaignStep | None:
    """Turn an unmet flag gate into the next set-step (item fetch or hail/travel)."""
    unmet = _unmet_flag(edges, group, flags)
    if unmet is None:
        return None
    name, _need = unmet
    current = int(flags.get(name) or 0)
    candidates: list[tuple[int, dict]] = []
    for edge in edges:
        if edge.get("rel") != "sets":
            continue
        to = str(edge.get("to") or "")
        if to != f"flag:{name}":
            continue
        try:
            value = int(edge.get("value") or 1)
        except (TypeError, ValueError):
            value = 1
        if value > current:
            candidates.append((value, edge))
    if not candidates:
        return None
    candidates.sort(key=lambda pair: pair[0])
    _value, edge = candidates[0]
    source = str(edge.get("from") or edge.get("group") or "")
    set_group = str(edge.get("group") or source)
    zone, npc = _zone_npc(source)
    missing = _missing_needs(edges, set_group, held) or _missing_needs(edges, source, held)
    if missing:
        mid, mcount = missing
        if mid not in stack:
            return CampaignStep(kind="need_item", item_id=mid, count=mcount, zone=zone, npc=npc, text=name)
    if zone and here and zone != (here or "").lower():
        return _travel_to(0, zone, npc, level, flags=flags, edges=edges, held=held, here=here, stack=stack, text=name)
    word = _hail_word(source)
    if _handed_ids(edges, set_group) or _hand_items(source) or _hand_items(set_group):
        return CampaignStep(kind="hand", item_id=0, zone=zone, npc=npc, word=word, text=name)
    return CampaignStep(kind="hail", item_id=0, zone=zone, npc=npc, word=word or "Hail", text=name)


def _handed_ids(edges, group: str) -> list[int]:
    found: list[int] = []
    for edge in edges:
        if edge.get("rel") != "receives":
            continue
        if not (
            _script_base(str(edge.get("group") or "")) == _script_base(group) or str(edge.get("group") or "") == group
        ):
            continue
        to = str(edge.get("to") or "")
        if to.startswith("item:"):
            found.append(int(to.split(":", 1)[1]))
    return found


# Vendor defaults — push these item ids onto the stack; planner buys/farms as usual.
FISH_POLE = 13100
FISH_BAIT = 13101
FISH_BAIT_WANT = 20
ITEM_FISHING_POLE = 36
ITEM_FISHING_BAIT = 37


def _source_step(
    item_id: int,
    source: str,
    here: str,
    level: int = 0,
    held: dict[int, int] | None = None,
    stack: list[int] | None = None,
    *,
    flags: dict[str, int] | None = None,
    edges=None,
) -> CampaignStep | None:
    ctx = dict(flags=flags, edges=edges, held=held, here=here, stack=stack)
    if source.startswith("forage:"):
        zone = source.split(":", 1)[1]
        if here and zone != (here or "").lower():
            return _travel_to(item_id, zone, "", level, **ctx)
        return CampaignStep(kind="forage", item_id=item_id, zone=zone)
    if source.startswith("fishing:"):
        zone = source.split(":", 1)[1]
        if here and zone != (here or "").lower():
            return _travel_to(item_id, zone, "", level, **ctx)
        return CampaignStep(kind="fish", item_id=item_id, zone=zone)
    if source.startswith("ground:"):
        zone = source.split(":", 1)[1]
        if here and zone != (here or "").lower():
            return _travel_to(item_id, zone, "", level, **ctx)
        return CampaignStep(kind="loot", item_id=item_id, zone=zone, text="ground")
    if source.startswith("loot:"):
        body = source.split(":", 1)[1]
        npc, _, zone = body.partition("@")
        if zone and here and zone != (here or "").lower():
            return _travel_to(item_id, zone, npc, level, **ctx)
        return CampaignStep(kind="kill", item_id=item_id, zone=zone, npc=npc)
    return None
