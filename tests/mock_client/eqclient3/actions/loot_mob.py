"""Band 270. An NPC corpse. Picks what queued fetches still need, then closes."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.journal import Journal
    from eqclient3.loop import Loop
    from eqclient3.schedule import Schedule
    from eqclient3.world import World

from eqclient3.action import Action
from eqclient3.structs import Item, OP_EndLootRequest, OP_LootRequest
from eqclient3.actions.support import (
    LOOT_RANGE,
    character_name,
    corpse_here,
    empty_slots,
    ingest_corpse_mail,
    loot_packet,
    walk,
    yards,
)
from eqclient3.actions.fetch import Fetch
from eqclient3.actions.kill import Kill
from eqclient3.actions.kill import Kill
from eqclient3.inventory.assign import assign as run_assign
from eqclient3.inventory.assign import release_cursor
from eqclient3.inventory.assign import improves_party, mark_coin_loot, sell_when_full

EQUIP_BUFFER = 2


class LootMob(Action):

    def __init__(self, corpse_id: int, where: tuple[float, float, float]) -> None:
        super().__init__()
        self.priority = 270
        self.durable = True
        self.corpse_id = corpse_id
        self.target_id = corpse_id
        self.where = where
        self._world: World | None = None
        self.active_path = None
        self.requested = False
        self.opened = False
        self.slots: list[Item] = []
        self.picks: list[Item] = []
        self.built = False

    def opcodes(self) -> tuple[str, ...]:
        return ("OP_Consider", "OP_ItemPacket", "OP_MoneyOnCorpse")

    @staticmethod
    def key(action: Action) -> tuple[float, ...]:
        if isinstance(action, LootMob):
            return (action.distance,)
        return (0.0,)

    @property
    def distance(self) -> float:
        world = self._world
        where = self.where
        if world is None or where is None:
            return 0.0
        return world.movement.plan(where).distance

    def suspend(self) -> None:
        self.active_path = None
        self.suspended = True

    def needs(self, queue: Schedule | None, world: World) -> list[tuple[int, int, int, int]]:
        if queue is None:
            return []
        rows = []
        for action in queue:
            if isinstance(action, Fetch):
                short = int(action.count) - int(world.held(action.item_id))
                if short > 0:
                    rows.append((action.priority, action.insert, action.item_id, short))
                continue
            if isinstance(action, Kill) and action.until_item:
                item_id = int(action.until_item)
                short = max(int(action.until_count), 1) - int(world.held(item_id))
                if short > 0:
                    rows.append((action.priority, action.insert, item_id, short))
        rows.sort(reverse=True)
        return rows

    def step(self, loop: Loop, world: World) -> None:
        self._world = world
        super().step(loop, world)
        self._inbox()
        corpse_id = self.corpse_id
        where = self.where
        if corpse_id is None or where is None:
            self.complete = True
            return
        if not corpse_here(world, corpse_id):
            self.complete = True
            return
        if world.cursor:
            release_cursor(loop, world)
            self.yielding = True
            return
        if self.waiting_for("TARGET"):
            body = world.mobs.get(int(corpse_id))
            if body is None or not body.dead:
                return
            self.unwait("TARGET")
        if self.waiting_for("LOOT"):
            return
        if yards(world, where) > LOOT_RANGE:
            walk(self, loop, world, where, "run")
            return
        if not self.requested:
            loop.send("OP_LootRequest", OP_LootRequest(corpse_id).serialize())
            self.requested = True
            self.wait("LOOT")
            self.suspended = False
            return
        if not self.opened:
            return
        if not self.built:
            if self._choose(loop, world):
                return
            self.built = True
        self.suspended = False
        if self.picks:
            slot = self.picks.pop(0)
            loop.send("OP_LootItem", loot_packet(corpse_id, world.self_id, slot.slot))
            return
        loop.send("OP_EndLootRequest", OP_EndLootRequest(corpse_id).serialize())
        run_assign(loop, world)
        self.complete = True

    def _inbox(self) -> None:
        ingest_corpse_mail(self, default_stack=True)

    def _choose(self, loop: Loop, world: World) -> bool:
        """Fetch needs, then an upgrade for anyone in the party. A coin run takes the rest and sells it."""
        earning = _earning(loop)
        room = empty_slots(world) if earning else empty_slots(world) - EQUIP_BUFFER
        gained: dict[int, int] = {}
        for slot in self.slots:
            if _is_coin(slot) and slot not in self.picks:
                self.picks.append(slot)
        for _priority, _insert, item_id, short in self.needs(loop.queue, world):
            for slot in self.slots:
                if _is_coin(slot):
                    continue
                if room <= 0:
                    break
                gap = short - gained.get(item_id, 0)
                if slot.item_id != item_id or gap <= 0 or slot in self.picks:
                    continue
                self.picks.append(slot)
                gained[item_id] = gained.get(item_id, 0) + (slot.stack or 1)
                room -= 1
        who = character_name(loop, world)
        if room <= 0 and _upgrade_waiting(self.slots, world, loop.journal, who):
            if _yield_for_sell(self, loop, world, who):
                return True
        for slot in self.slots:
            if room <= 0 or _is_coin(slot) or slot in self.picks:
                continue
            if not improves_party(world, slot.item_id, loop.journal, who):
                continue
            self.picks.append(slot)
            room -= 1
        if earning:
            for slot in self.slots:
                if room <= 0 or _is_coin(slot) or slot in self.picks:
                    continue
                self.picks.append(slot)
                room -= 1
                mark_coin_loot(loop, world, loop.journal, who, slot.item_id)
            if room <= 0 and _unsold(self.slots, self.picks) and _yield_for_sell(self, loop, world, who):
                return True
        return False


def _earning(loop: Loop) -> bool:
    """A coin fetch is open, or the grind it queued is still running."""
    queue = loop.queue
    if queue is None:
        return False
    for action in queue:
        if action.complete:
            continue
        if isinstance(action, Fetch) and action.item_id == 0 and action.copper > 0:
            return True
        if "#gold:" in str(action.source or ""):
            return True
    return False


def _yield_for_sell(action: LootMob, loop: Loop, world: World, character: str) -> bool:
    if not sell_when_full(loop, world, loop.journal, character) and not _sell_open(loop):
        return False
    action.priority = 0
    action.yielding = True
    return True


def _sell_open(loop: Loop) -> bool:
    queue = loop.queue
    if queue is None:
        return False
    return any(not action.complete and type(action).__name__ == "Sell" for action in queue)


def _unsold(slots: list[Item], picks: list[Item]) -> bool:
    return any(not _is_coin(slot) and slot not in picks for slot in slots)


def _upgrade_waiting(slots: list[Item], world: World, journal: Journal | None, character: str) -> bool:
    return any(not _is_coin(slot) and improves_party(world, slot.item_id, journal, character) for slot in slots)


def _is_coin(slot: Item) -> bool:
    """A pile the server turns into money. It does not need a free bag slot."""
    name = slot.name.lower()
    return any(tip in name for tip in ("coin", "platinum", "gold piece", "silver", "copper"))
