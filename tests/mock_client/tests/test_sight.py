"""Doors on a step, the zone map between two eyes, and a character read from the server."""

from __future__ import annotations

import struct

from eqclient.maps import ZoneMap
from eqclient.packets import character_by_name, player_profile
from eqclient.world import Door, ZoneModel, doors_along


def test_a_door_on_the_step_is_opened_and_the_exit_is_not():
    gate = Door(4, "gate", 5.0, 0.0, 0.0, 5)
    exit_door = Door(11, "out", 6.0, 0.0, 0.0, 5)
    far = Door(8, "upstairs", 5.0, 40.0, 0.0, 5)
    hits = doors_along([gate, exit_door, far], (0.0, 0.0, 0.0), (10.0, 0.0, 0.0), {11})
    assert [door.door_id for door in hits] == [4]


def test_a_wall_blocks_the_shot_and_open_air_does_not():
    wall = ((0.0, 0.0, 0.0), (0.0, 10.0, 0.0), (0.0, 0.0, 10.0))
    zone = ZoneMap([wall])
    assert not zone.clear((-5.0, 5.0, 0.0), (5.0, 5.0, 0.0))
    assert zone.clear((-5.0, 5.0, 0.0), (-1.0, 5.0, 0.0))


def test_account_and_name_load_the_server_character():
    select = bytearray(1704)
    struct.pack_into("<I", select, 0, 1)
    struct.pack_into("<I", select, 4, 6)
    select[1004] = 1
    select[1005] = 12
    select[1664] = 0
    select[1665] = 1
    select[1694] = 4
    select[1695] = 7
    struct.pack_into("<I", select, 832, 396)
    struct.pack_into("<I", select, 836, 206)
    struct.pack_into("<I", select, 964, 189)
    struct.pack_into("<I", select, 968, 40)
    select[1024:1031] = b"Mockone"
    select[1088:1094] = b"Velkyn"
    played = character_by_name(bytes(select), "Velkyn")
    assert played is not None
    assert played.race == 6
    assert played.class_id == 12
    assert played.level == 7
    assert played.deity == 206
    assert played.zone_id == 40
    assert played.gender == 1

    profile = bytearray(13004)
    struct.pack_into("<III", profile, 4, 1, 6, 12)
    profile[20] = 7
    struct.pack_into("<I", profile, 124, 206)
    struct.pack_into("<III", profile, 2224, 15, 40, 80)
    struct.pack_into("<IIIIIII", profile, 2236, 70, 75, 60, 75, 129, 95, 83)
    profile[12940:12946] = b"Velkyn"
    loaded = player_profile(bytes(profile))
    assert loaded is not None
    assert (loaded.strength, loaded.stamina, loaded.charisma, loaded.intelligence) == (70, 75, 60, 129)
    assert loaded.points == 15

    model = ZoneModel("Someone")
    model.class_id = 1
    model.race_id = 1
    model.apply_played(played)
    model.apply_played(loaded)
    assert model.character == "Velkyn"
    assert model.race_id == 6
    assert model.class_id == 12
    assert model.level == 7
    assert model.strength == 70
    assert model.points == 15
