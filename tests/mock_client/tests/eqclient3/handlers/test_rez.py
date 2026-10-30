"""Opcode coverage for handlers/rez.py."""

from eqclient3.handlers import rez
from eqclient3.structs import OP_RezzRequest
from support import Loop, World, names


def test_opcodes():
    world = World(name="Hero", zone="qeynos")
    world.pending_death = 15
    world.x, world.y, world.z = 4.0, 5.0, 6.0
    loop = Loop()
    rez.RezHandler().handle("OP_ZonePlayerToBind", b"", world, loop)
    assert names(loop) == ["Reclaim"]
    assert loop.queue[0].priority == 270
    assert loop.queue[0].source == "reclaim:15"
    assert loop.queue[0].where == (4.0, 5.0, 6.0)

    payload = OP_RezzRequest(corpse_name="Hero").serialize()
    rez.RezHandler().handle("OP_RezzRequest", payload, world, loop)
    assert names(loop) == ["Reclaim", "Rez"]
    action = loop.queue[1]
    assert action.priority == 230
    assert isinstance(action.payload, OP_RezzRequest)
    assert action.payload.corpse_name == "Hero"
    assert action.corpse_id == 15
    assert action.source.startswith("rez:")
