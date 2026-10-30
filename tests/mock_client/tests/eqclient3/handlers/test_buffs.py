"""Opcode coverage for handlers/buffs.py."""

from eqclient3.actions.attack import Attack
from eqclient3.handlers import buffs
from eqclient3.structs import OP_Buff, SpellBuff
from support import Loop, World, names


def _buff(entity, spell_id, counters, fade=0) -> bytes:
    return OP_Buff(
        int(entity),
        SpellBuff(spell_id=int(spell_id), counters=int(counters)),
        fade=int(fade),
    ).serialize()


def test_opcodes():
    world = World(self_id=7, name="Hero")
    loop = Loop()
    buffs.BuffsHandler().handle("OP_Buff", _buff(7, 55, 3), world, loop)
    assert (7, 55) in world.buffs
    assert names(loop) == ["Cure"]
    assert loop.queue[0].priority == 250
    assert loop.queue[0].source == "cure:55"
    assert loop.queue[0].entity == 7
    buffs.BuffsHandler().handle("OP_Buff", _buff(7, 55, 3), world, loop)
    assert names(loop) == ["Cure"]

    fighting = Loop()
    fighting.append(Attack(9))
    buffs.BuffsHandler().handle("OP_Buff", _buff(7, 56, 1), world, fighting)
    assert "Cure" not in names(fighting)
    assert (7, 56) in world.buffs

    buffs.BuffsHandler().handle("OP_Buff", _buff(7, 55, 0, fade=1), world, loop)
    assert (7, 55) not in world.buffs
