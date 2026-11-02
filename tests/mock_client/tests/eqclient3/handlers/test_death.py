"""Opcode coverage for handlers/death.py."""

from eqclient3.handlers import death
from support import Loop, World, death as death_packet, names


def test_opcodes():
    world = World(name="Hero", zone="qeynos", self_id=7, x=1, y=2, z=3)
    loop = Loop()
    kept = object()
    loop.queue.append(kept)
    death.DeathHandler().handle("OP_Death", death_packet(7, 9, 15), world, loop)
    assert names(loop)[1:] == ["Death", "Reclaim"]
    assert kept in loop.queue
    assert loop.queue[1].priority == 410
    assert loop.queue[1].source == "death:qeynos"
    assert loop.queue[2].priority == 270
    assert loop.queue[2].source == "reclaim:15"
    assert loop.queue[2].corpse_id == 15
    assert loop.queue[2].where == (1.0, 2.0, 3.0)

    other = Loop()
    death.DeathHandler().handle("OP_Death", death_packet(0, 0, 0), world, other)
    assert other.queue == []
    death.DeathHandler().handle("OP_Death", death_packet(99, 0, 4), world, other)
    assert other.queue == []

    unknown = World(zone="qeynos", x=8, y=9, z=0)
    pending = Loop()
    death.DeathHandler().handle("OP_Death", death_packet(7, 1, 7), unknown, pending)
    assert unknown.pending_death == 7
    assert unknown.pending_corpse == 7
    assert unknown.pending_where == (8.0, 9.0, 0.0)
    assert names(pending) == []
    unknown.self_id = 4
    death.claim_pending(pending, unknown)
    assert names(pending) == []
    assert unknown.pending_death == 7
    unknown.self_id = 7
    death.claim_pending(pending, unknown)
    assert unknown.pending_death == 0
    assert names(pending) == ["Death", "Reclaim"]
    assert pending.queue[1].corpse_id == 7
    assert pending.queue[1].where == (8.0, 9.0, 0.0)

    fresh = Loop()
    sheet = World(name="Hero", zone="qeynos", self_id=7, x=1, y=2, z=3)
    sheet.formed_for = "qeynos"
    death.DeathHandler().handle("OP_Death", death_packet(7, 9, 15), sheet, fresh)
    fallen = next(action for action in fresh.queue if type(action).__name__ == "Death")
    fallen.step(fresh, sheet)
    assert sheet.formed_for == ""
    assert not any(action.source == "form:qeynos" for action in fresh.queue)
