"""Death drops everything, levels buy skills, and gear that fits gets worn."""

from __future__ import annotations

import struct

from eqclient.items import Held, Inventory, can_receive, content_slot, equip_move, fits, missing_entries, stow_move
from eqclient.plan import choose
from eqclient.quests import ZoneQuests
from eqclient.tasks import KILL, Activity, TaskBook
from eqclient.world import Door, Spawn, ZoneModel


def _world() -> ZoneModel:
    world = ZoneModel("Mockone")
    world.zone = "tutorialb"
    world.class_id = 1
    world.race_id = 1
    world.level = 4
    world.x, world.y, world.z = 2.0, -146.0, 19.0
    world.have_position = True
    return world


def _kill_book() -> TaskBook:
    book = TaskBook()
    book.set_here("tutorialb")
    book.add(Activity(5102, 1, 1, KILL, "a gloom spider"))
    return book


def test_death_saves_the_spot_and_a_respawn_does_not_move_it():
    world = _world()
    world.self_id = 7
    world.spawns[7] = Spawn(7, "Mockone", 0, 4, 1, 2.0, -146.0, 19.0, 1, 1)
    world.on_become_corpse(struct.pack("<Ifff", 7, -40.0, 80.0, 5.0))
    assert world.needs_corpse
    assert world.own_corpse_at == (80.0, -40.0, 5.0)
    assert world.position == (2.0, -146.0, 19.0)
    world.apply_server_position(2.0, -146.0, 19.6)
    assert world.own_corpse_at == (80.0, -40.0, 5.0)
    assert world.on_death(struct.pack("<I", 7))

    blob = bytearray(385)
    blob[83] = 2
    struct.pack_into("<I", blob, 340, 99)
    blob[7:14] = b"Mockone"
    world.on_spawns(bytes(blob))
    assert world.own_corpse_id == 99
    assert world.self_id == 7


def test_reclaim_outranks_a_task_kill():
    world = _world()
    world.needs_corpse = True
    world.own_corpse_zone = "tutorialb"
    world.own_corpse_at = (80.0, -40.0, 5.0)
    world.spawns[4] = Spawn(4, "a gloom spider", 1, 2, 1, 3.0, -140.0, 19.0, 1, 1)
    intent = choose(world, _kill_book(), ZoneQuests("tutorialb"), Inventory(), True)
    assert intent is not None
    assert intent.kind == "reclaim"
    assert intent.where == (80.0, -40.0, 5.0)


def test_level_gain_adds_five_points_and_the_class_trainer_is_next():
    world = _world()
    world.level = 1
    world.grant_levels(2, 1)
    assert world.level == 2
    assert world.points == 5
    world.grant_levels(2, 2)
    assert world.points == 5
    world.spawns[3] = Spawn(3, "Arias", 1, 50, 1, 4.0, -140.0, 19.0, 20, 1)
    world.spawns[4] = Spawn(4, "a gloom spider", 1, 2, 1, 3.0, -140.0, 19.0, 1, 1)
    intent = choose(world, _kill_book(), ZoneQuests("tutorialb"), Inventory(), True)
    assert intent is not None
    assert intent.kind == "train"
    assert intent.target == 3


def test_leave_waits_until_level_five():
    world = _world()
    world.level = 4
    quests = ZoneQuests("tutorialb")
    quests.exits = [11]
    world.doors[11] = Door(11, "exit", 10.0, -100.0, 19.0, 5)
    intent = choose(world, TaskBook(), quests, Inventory(), True)
    assert intent is not None
    assert intent.kind == "explore"
    world.level = 5
    intent = choose(world, TaskBook(), quests, Inventory(), True)
    assert intent is not None
    assert intent.kind == "leave"
    assert intent.target == 11


def test_equip_fits_an_empty_slot_and_skips_a_mismatch_or_a_turn_in():
    bag = Inventory()
    sword = Held(9991, 22, 1, "sword", "IT1", slots=1 << 13, classes=1, races=1, damage=6)
    wrong = Held(9992, 23, 1, "mace", "IT2", slots=1 << 13, classes=1 << 1, races=1, damage=9)
    silk = Held(54234, 24, 1, "silk", "IT3", slots=1 << 13, classes=1, races=1, damage=8)
    bag.slots = {22: sword, 23: wrong, 24: silk}
    assert fits(sword, 1, 1, 4)
    assert not fits(wrong, 1, 1, 4)
    assert equip_move(bag, 1, 1, 4, {54234}) == (22, 13)


def test_corpse_is_done_only_when_every_listed_item_is_back():
    sword = Held(1, 22, 1, "sword", "")
    silk = Held(54234, 23, 1, "silk", "")
    before = {}
    after = {1: 1}
    assert missing_entries(before, after, [sword, silk]) == 1
    assert missing_entries(before, {1: 1, 54234: 1}, [sword, silk]) == 0
    world = _world()
    world.needs_corpse = True
    world.note_corpse_contents(2, 1)
    assert world.needs_corpse
    assert world.own_corpse_count == 2
    assert world.own_corpse_missing == 1
    world.note_corpse_contents(2, 0)
    assert not world.needs_corpse


def test_bags_hold_items_and_a_full_pack_yields_the_corpse_turn():
    assert content_slot(22, 0) == 251
    assert content_slot(23, 1) == 262
    bag = Inventory()
    container = Held(100, 30, 1, "bag", "", bag_slots=4, bag_size=2, slots=1 << 22)
    gem = Held(200, 30, 1, "gem", "", size=1)
    bag.slots[30] = container
    assert stow_move(bag) == (30, 22)
    bag.slots = {22: container, 30: gem}
    for slot in range(23, 30):
        bag.slots[slot] = Held(slot, slot, 1, "fill", "")
    assert stow_move(bag) == (30, 251)
    huge = Held(201, 30, 1, "crate", "", size=4)
    bag.slots[30] = huge
    bag.slots[251] = Held(1, 251, 1, "a", "")
    bag.slots[252] = Held(2, 252, 1, "b", "")
    bag.slots[253] = Held(3, 253, 1, "c", "")
    bag.slots[254] = Held(4, 254, 1, "d", "")
    assert stow_move(bag) is None
    assert not can_receive(bag)
    world = _world()
    world.needs_corpse = True
    world.own_corpse_at = (80.0, -40.0, 5.0)
    world.own_corpse_zone = "tutorialb"
    intent = choose(world, TaskBook(), ZoneQuests("tutorialb"), bag, True)
    assert intent is not None
    assert intent.kind != "reclaim"
