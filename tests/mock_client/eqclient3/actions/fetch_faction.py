"""Band 0. The largest reachable quest for this faction, else one nearby NPC kill."""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, runtime_checkable

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import World

from eqclient3.action import Action
from eqclient3.actions.kill import Kill
from eqclient3.actions.support import yield_to


class FetchFaction(Action):

    def __init__(self, faction_id: int) -> None:
        super().__init__()
        self.priority = 0
        self.durable = True
        self.faction_id = int(faction_id)

    def opcodes(self) -> tuple[str, ...]:
        return ()

    def suspend(self) -> None:
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        self.suspended = False
        quests = _quests(world, self.faction_id)
        reachable = world.reachable
        for quest in quests:
            if not _can_reach(quest, reachable):
                continue
            source = quest.source or f"faction:{self.faction_id}:{quest.value}"
            journal = loop.journal
            who = loop.character or world.name
            if journal is not None and who and journal.is_resolved(who, source):
                continue
            chain = quest.actions or []
            if not chain:
                continue
            for index, action in enumerate(list(chain)):
                yield_to(self, loop, world, action, action.source or f"{source}:{index}")
            self.complete = True
            return
        npc = _npc(world)
        if npc is not None:
            spawn = npc.spawn_id
            yield_to(
                self,
                loop,
                world,
                Kill(spawn_id=spawn),
                f"faction:{self.faction_id}:{spawn}",
            )
        self.complete = True


@runtime_checkable
class _Quest(Protocol):
    faction_id: int
    value: int
    start: str
    zones: tuple[str, ...]
    actions: list[Action]
    source: str


@runtime_checkable
class _Npc(Protocol):
    spawn_id: int
    level: int
    value: int


def _quests(world: World, faction_id: int) -> list[_Quest]:
    rows = [row for row in world.faction_quests if isinstance(row, _Quest) and row.faction_id == faction_id]
    rows.sort(key=lambda row: row.value, reverse=True)
    return rows


def _can_reach(quest: _Quest, reachable: set[str]) -> bool:
    if quest.start and quest.start not in reachable:
        return False
    for zone in quest.zones:
        if zone not in reachable:
            return False
    return True


def _npc(world: World) -> _Npc | None:
    level = world.level or 1
    close = [row for row in world.faction_npcs if isinstance(row, _Npc) and abs(row.level - level) <= 10]
    if not close:
        return None
    close.sort(key=lambda row: row.value, reverse=True)
    return close[0]
