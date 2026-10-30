"""Opcode coverage for handlers/mobs.py."""

from __future__ import annotations

import struct

from eqclient3.actions.attack import Attack
from eqclient3.handlers import mobs
from eqclient3.structs import OP_Track
from support import (
    Loop,
    World,
    become_corpse,
    damage,
    hp,
    names,
    position,
    sources,
    spawn,
)


def test_opcodes():
    world = World(name="Hero", zone="qeynos")
    loop = Loop()
    mobs.MobsHandler().handle("OP_NewSpawn", spawn(7, "Hero", x=1, y=2, z=3), world, loop)
    mobs.MobsHandler().handle("OP_ZoneSpawns", spawn(9, "a bat", x=10, y=0, z=0), world, loop)
    assert world.self_id == 7
    assert set(world.mobs) == {7, 9}
    bat = world.mobs[9]
    assert bat.name == "a bat" and bat.npc == 1
    before = bat.position
    mobs.MobsHandler().handle("OP_ClientUpdate", position(7, 50, 50, 0), world, loop)
    mobs.MobsHandler().handle("OP_ClientUpdate", position(0, 80, 80, 0), world, loop)
    assert world.mobs[7].position == (1.0, 2.0, 3.0)
    assert bat.position == before
    mobs.MobsHandler().handle("OP_MobUpdate", position(9, 4, 0, 1), world, loop)
    assert bat.position == (4.0, 0.0, 1.0)
    assert bat is world.mobs[9]

    mobs.MobsHandler().handle("OP_Damage", damage(7, 9, 12), world, loop)
    mobs.MobsHandler().handle("OP_Damage", damage(7, 9, 8), world, loop)
    attacks = [action for action in loop.queue if isinstance(action, Attack)]
    assert len(attacks) == 1
    assert attacks[0].priority == 300
    assert attacks[0].source == "aggro:9"
    assert attacks[0].spawn_id == 9
    assert len(attacks[0].messages) == 2
    mobs.MobsHandler().handle("OP_BecomeCorpse", become_corpse(9, 4, 0, 1), world, loop)
    assert bat.dead is True and bat.npc == 3
    assert attacks[0].complete is True
    assert "Reclaim" not in names(loop)
    assert attacks[0] in loop.queue

    quiet = Loop()
    sheet = World(name="Hero", self_id=7, zone="qeynos")
    mobs.MobsHandler().handle("OP_HPUpdate", hp(7, 40, 100), sheet, quiet)
    assert sheet.hp == 40 and sheet.max_hp == 100
    assert sources(quiet) == ["heal:self"]
    assert quiet.queue[0].priority == 260
    fighting = Loop()
    fighting.append(Attack(9))
    mobs.MobsHandler().handle("OP_HPUpdate", hp(7, 20, 100), sheet, fighting)
    assert "Heal" not in names(fighting)

    held = Loop()
    live = World(name="Hero", self_id=7)
    mobs.MobsHandler().handle("OP_NewSpawn", spawn(4, "a wolf"), live, held)
    mobs.MobsHandler().handle("OP_Damage", damage(7, 4, 6, dmg_type=231, spell=12), live, held)
    assert names(held) == ["Hold"]
    assert held.queue[0].source == "hold:4" and held.queue[0].priority == 100
    live.mobs[4].dead = True
    mobs.MobsHandler().handle("OP_Damage", damage(7, 4, 6, dmg_type=231, spell=12), live, held)
    assert names(held) == ["Hold"]

    tracked = World()
    mobs.MobsHandler().handle("OP_NewSpawn", spawn(3, "a bear"), tracked, Loop())
    mobs.MobsHandler().handle("OP_Track", OP_Track([(3, 12.5), (99, 1.0)]).serialize(), tracked, Loop())
    assert tracked.mobs[3].distance == 12.5
    assert 99 not in tracked.mobs

    finder = Loop()
    mobs.MobsHandler().handle("OP_FindPersonReply", b"\x00" * 16, World(), finder)
    assert finder.queue == []
    aimed = World()
    mobs.MobsHandler().handle("OP_NewSpawn", spawn(3, "a bear"), aimed, Loop())
    mobs.MobsHandler().handle("OP_Assist", struct.pack("<I", 3), aimed, Loop())
    assert aimed.mobs[3].targeted is True
