"""OP_Death appends Death and Reclaim only when the spawn is this agent.

A death that arrives before we know our spawn id is stashed. It is queued once
a spawn or an HP update names us and the id matches. Someone else's death is ignored.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop

from eqclient3.actions.death import Death
from eqclient3.actions.reclaim import Reclaim
from eqclient3.handlers.common import enqueue_once
from eqclient3.structs import EQStruct, OP_Death
from eqclient3.handler import Handler
from eqclient3.world import World


class DeathHandler(Handler):
    opcodes = ("OP_Death",)

    def on(self, opcode: str, payload: EQStruct) -> None:
        del opcode
        if not isinstance(payload, OP_Death) or not payload.spawn_id:
            return
        spawn_id = payload.spawn_id
        world = self.world
        self_id = world.self_id
        if self_id and spawn_id != self_id:
            return
        corpse_id = payload.corpse_id or spawn_id
        world.pending_death = spawn_id
        world.pending_corpse = corpse_id
        world.pending_where = (world.x, world.y, world.z)
        claim_pending(self.loop, world)


def claim_pending(loop: Loop, world: World) -> None:
    """Queue the stashed death once our spawn id is the one that died."""
    pending = world.pending_death or 0
    self_id = world.self_id
    if not pending or not self_id or pending != self_id or not loop:
        return
    corpse_id = world.pending_corpse or pending
    where = world.pending_where
    if not where:
        where = (world.x, world.y, world.z)
    world.pending_death = 0
    world.pending_corpse = 0
    world.pending_where = None
    queue_death(loop, world, corpse_id, where)


def queue_death(loop: Loop, world: World, corpse_id: int, where: tuple[float, float, float]) -> None:
    zone = str(world.zone or "")
    source = f"death:{zone}"
    # One death in a zone resolves this source. The next death is a new one.
    journal = loop.journal
    who = loop.character
    if journal is not None and who and journal.is_resolved(who, source):
        journal.clear_source(who, source)
    enqueue_once(loop, world, Death(), source)
    enqueue_once(loop, world, Reclaim(corpse_id, where), f"reclaim:{corpse_id}")
