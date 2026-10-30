"""Band 0. Obtain a count of an item. A drop in another zone is Travel, not Zone."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import World

from eqclient3.action import Action
from eqclient3.actions.kill import Kill
from eqclient3.actions.pickup import Pickup
from eqclient3.actions.support import FetchDrop, fetch_plan, has_soulbind, yield_to, walk
from eqclient3.actions.talk import Talk, append_soulbind, hail_name
from eqclient3.actions.trade import Trade
from eqclient3.actions.travel import Travel
from eqclient3.actions.zone import Zone


class Fetch(Action):

    def __init__(self, item_id: int, count: int, task_text: str) -> None:
        super().__init__()
        self.priority = 0
        self.durable = True
        self.item_id = item_id
        self.count = count
        self.task_text = task_text
        self.active_path = None

    def opcodes(self) -> tuple[str, ...]:
        return ()

    def suspend(self) -> None:
        self.active_path = None
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        self.suspended = False
        if self.item_id == 0:
            if hail_name(self.task_text):
                yield_to(
                    self,
                    loop,
                    world,
                    Talk(0, "hail", self.task_text),
                    f"hail:{hail_name(self.task_text).lower()}",
                )
                self.complete = True
                return
        if world.held(self.item_id) >= self.count:
            self.complete = True
            return
        plan = fetch_plan(world, self.item_id)
        drop = plan.drop
        if drop is not None and (not has_soulbind(loop, world)):
            if append_soulbind(self, loop, world):
                return
        quest = plan.quest
        if quest:
            self._chain(loop, world, quest, f"quest:{self.item_id}")
            return
        merchant = plan.merchant
        if merchant is not None and _here(world, merchant.zone):
            opened = Trade(merchant.npc, self.item_id)
            opened.merchant_zone = str(merchant.zone or "")
            if yield_to(self, loop, world, opened, f"trade:{self.item_id}"):
                return
            return
        ground = plan.ground
        if ground is not None and _here(world, ground.zone):
            yield_to(
                self,
                loop,
                world,
                Pickup(ground.drop_id, ground.point),
                f"pickup:{ground.drop_id}",
            )
            return
        if drop is not None:
            self._drop(loop, world, drop)
            return
        vendor_zone = plan.vendor_zone or plan.station_zone
        if vendor_zone and vendor_zone != world.zone:
            yield_to(self, loop, world, Zone(vendor_zone), f"zone:{vendor_zone}")
            return
        station = plan.station or world.station
        if station is None:
            return
        walk(self, loop, world, station, "run")

    def _chain(
        self,
        loop: Loop,
        world: World,
        quest: list[Action] | tuple[Action, ...] | Action,
        source: str,
    ) -> None:
        rows = list(quest) if isinstance(quest, (list, tuple)) else [quest]
        pushed = False
        for index, action in enumerate(rows):
            if yield_to(self, loop, world, action, action.source or f"{source}:{index}"):
                pushed = True
        if pushed:
            self.yielding = True

    def _drop(self, loop: Loop, world: World, drop: FetchDrop) -> None:
        zone = drop.zone
        if drop.above_level:
            camp = drop.camp
            level = drop.level
            yield_to(
                self,
                loop,
                world,
                Kill(camp=camp, level=level),
                f"kill:camp:{self.item_id}",
            )
            return
        if zone and zone != world.zone:
            yield_to(self, loop, world, Travel(zone), f"travel:{zone}")
            return
        queue = loop.queue
        for spawn_id in drop.spawns:
            if queue is not None and any(isinstance(action, Kill) and action.spawn_id == spawn_id for action in queue):
                continue
            yield_to(self, loop, world, Kill(spawn_id=spawn_id), f"kill:{spawn_id}")


def _here(world: World, zone: str) -> bool:
    return not zone or zone == world.zone
