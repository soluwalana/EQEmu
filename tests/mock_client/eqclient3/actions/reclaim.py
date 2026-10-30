"""Band 270. Our corpse: drag inside 45 yards, then loot, then bury."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import Mob, World

from eqclient3.action import Action
from eqclient3.structs import Item, OP_EndLootRequest, OP_LootRequest
from eqclient3.actions.bots.summon import Summon
from eqclient3.actions.rez import Rez
from eqclient3.actions.support import (
    CORPSE_NEAR,
    HOSTILE_CLOSE,
    HOSTILE_FAR,
    corpse_drag,
    corpse_name,
    hostiles_within,
    ingest_corpse_mail,
    loot_packet,
    queued,
    walk,
    yield_to,
)
from eqclient3.inventory.assign import assign as run_assign


class Reclaim(Action):

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
        self.dragged = False
        self.slots: list[Item] = []

    def opcodes(self) -> tuple[str, ...]:
        return ("OP_Consider", "OP_ItemPacket", "OP_MoneyOnCorpse")

    @staticmethod
    def key(action: Action) -> tuple[float, ...]:
        if isinstance(action, Reclaim):
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

    def step(self, loop: Loop, world: World) -> None:
        self._world = world
        super().step(loop, world)
        self._inbox()
        if self.waiting_for("TARGET"):
            return
        if self.waiting_for("LOOT"):
            return
        corpse_id = self.corpse_id
        if corpse_id is None:
            return
        if world.level > 10 and (not queued(loop, "Rez", corpse_id=corpse_id)):
            payload = world.rezz_payload or b""
            yield_to(self, loop, world, Rez(corpse_id, payload), f"rez:{corpse_id}")
        if self.distance > CORPSE_NEAR:
            self._approach(loop, world)
            return
        if not self.dragged:
            loop.send(
                "OP_CorpseDrag",
                corpse_drag(corpse_name(world, corpse_id), world.name),
            )
            self.dragged = True
            self.suspended = False
            return
        if not self.requested:
            loop.send("OP_LootRequest", OP_LootRequest(corpse_id).serialize())
            self.requested = True
            self.wait("LOOT")
            self.suspended = False
            return
        self.suspended = False
        if self.slots:
            slot = self.slots.pop(0)
            loop.send("OP_LootItem", loot_packet(corpse_id, world.self_id, slot.slot))
            return
        if not self.opened:
            return
        loop.send("OP_EndLootRequest", OP_EndLootRequest(corpse_id).serialize())
        run_assign(loop, world)
        self.complete = True

    def _inbox(self) -> None:
        ingest_corpse_mail(self)

    def _approach(self, loop: Loop, world: World) -> None:
        mover = world.movement
        seen = mover.visible_mobs()
        on_path = mover.mobs_on_path(seen) or []
        close = hostiles_within(seen, HOSTILE_CLOSE) + hostiles_within(on_path, HOSTILE_CLOSE)
        far = hostiles_within(seen, HOSTILE_FAR) + hostiles_within(on_path, HOSTILE_FAR)
        if close and (not queued(loop, "Summon")):
            yield_to(self, loop, world, Summon(271), f"summon:{self.corpse_id}")
            return
        if close:
            hostile = close[0]
            walk(self, loop, world, hostile.position, "walk")
            if world.line_of_sight(hostile):
                self._cautious_attack(loop, world, hostile)
            self.suspended = False
            return
        where = self.where
        if where is None:
            return
        mode = "walk" if far else "run"
        walk(self, loop, world, where, mode)

    def _cautious_attack(self, loop: Loop, world: World, mob: Mob) -> None:
        # Attack constructs Reclaim, so this import stays in the method.
        from eqclient3.actions.attack import Attack
        from eqclient3.handlers.common import attack_for, mark_fight

        spawn = int(mob.id or 0)
        if not spawn or attack_for(loop, Attack, spawn):
            return
        attack = Attack(spawn, cautious=True)
        mark_fight(world, spawn)
        attack.level = int(mob.level or 0)
        yield_to(self, loop, world, attack, f"aggro:{spawn}")
