"""Death drops everything, levels buy skills, and gear that fits gets worn."""

from __future__ import annotations

import struct

from eqclient.explore import AreaSearch, Survey, bearing, cell_of, next_length, other_step, refused
from eqclient.packets import (
    find_path,
    find_person_request,
    guide_from,
    movement_history,
    parse_inventory,
    player_profile,
    popup_message,
    popup_response,
    saylink_words,
)
from eqclient.items import (
    BACKPACK_ITEM,
    Held,
    Inventory,
    bags_short,
    can_receive,
    content_slot,
    equip_move,
    fits,
    has_loot_room,
    missing_entries,
    server_slot,
    stow_move,
    trash_slots,
)
from eqclient.plan import choose, guide, lesson_from, recover
from eqclient.quests import ZoneQuests, door_destinations, parse_script, reply_order
from eqclient.tasks import DELIVER, KILL, SPEAK, Activity, TaskBook
from eqclient.world import Door, Spawn, ZoneModel, blocks_step


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


def test_grind_picks_a_nearby_spider_over_a_grey_bat():
    world = _world()
    world.level = 3
    world.spawns[1] = Spawn(1, "a_cave_bat004", 1, 1, 1, 4.0, -148.0, 19.0, 1, 1)
    world.spawns[2] = Spawn(2, "a_gloom_spider001", 1, 3, 1, 20.0, -160.0, 19.0, 1, 1)
    intent = choose(world, TaskBook(), ZoneQuests("tutorialb"), Inventory(), True)
    assert intent is not None
    assert intent.kind == "task_kill"
    assert intent.target == 2


def test_level_four_in_the_mine_goes_to_hobart_and_the_exit_waits():
    world = _world()
    world.level = 4
    world.spawns[8] = Spawn(8, "Guard Hobart", 1, 20, 1, 30.0, -80.0, 19.0, 1, 1)
    quests = ZoneQuests("tutorialb")
    quests.exits = [11]
    world.doors[11] = Door(11, "exit", 10.0, -100.0, 19.0, 5)
    intent = choose(world, TaskBook(), quests, Inventory(), True)
    assert intent is not None
    assert intent.kind == "task_talk"
    assert intent.target == 8
    done = TaskBook()
    done.completed.add(5102)
    world.level = 5
    intent = choose(world, done, quests, Inventory(), True)
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


def _pace(survey: Survey, signature=((1448, 0, 0),)) -> None:
    for x, y in ((0.0, -122.0), (-6.0, -127.0)) * 4:
        survey.note((x, y, 10.0), signature)


def test_a_repeated_walk_is_a_loop_and_the_task_stays():
    survey = Survey()
    _pace(survey)
    assert survey.looping()
    world = _world()
    world.spawns[8] = Spawn(8, "Arias", 1, 50, 1, 0.0, -122.0, 10.0, 1, 1)
    book = TaskBook()
    book.set_here("tutorialb")
    book.add(Activity(1448, 0, 1, SPEAK, "Arias"))
    intent = choose(world, book, ZoneQuests("tutorialb"), Inventory(), True)
    assert intent is not None and intent.where is not None
    assert intent.kind == "task_talk"
    first = survey.new_approach((0.0, -122.0, 10.0), intent.where)
    second = survey.new_approach((0.0, -122.0, 10.0), intent.where)
    assert first is not None and second is not None
    assert cell_of(first[0], first[1]) not in set(survey.samples)
    assert first != second
    again = choose(world, book, ZoneQuests("tutorialb"), Inventory(), True)
    assert again is not None
    assert again.kind == "task_talk"
    assert again.target == intent.target


def test_search_follows_the_live_npc_and_backtracks():
    centers = {
        (0, 0): (0.0, 0.0, 0.0),
        (0, 1): (10.0, 0.0, 0.0),
        (0, 2): (20.0, 0.0, 0.0),
        (0, 3): (10.0, 10.0, 0.0),
    }
    links_of = {
        (0, 0): [(0, 1)],
        (0, 1): [(0, 0), (0, 2), (0, 3)],
        (0, 2): [(0, 1)],
        (0, 3): [(0, 1)],
    }

    def locate(point):
        return min(centers, key=lambda poly: (centers[poly][0] - point[0]) ** 2 + (centers[poly][1] - point[1]) ** 2)

    def links(poly):
        return [(neighbor, centers[neighbor]) for neighbor in links_of[poly]]

    search = AreaSearch()
    first = search.advance((0.0, 0.0, 0.0), (20.0, 0.0, 0.0), locate, links, centers.get)
    assert first == (10.0, 0.0, 0.0)
    moved = search.advance((10.0, 0.0, 0.0), (10.0, 10.0, 0.0), locate, links, centers.get)
    assert moved == (10.0, 10.0, 0.0)
    search.advance((10.0, 10.0, 0.0), (10.0, 10.0, 0.0), locate, links, centers.get)
    # That branch is finished, so the walk returns toward the polygon still unvisited.
    back = search.advance((10.0, 0.0, 0.0), (20.0, 0.0, 0.0), locate, links, centers.get)
    assert back == (20.0, 0.0, 0.0)


def test_task_progress_clears_the_failed_approach():
    survey = Survey()
    _pace(survey)
    assert survey.looping()
    survey.note((0.0, -122.0, 10.0), ((1448, 0, 1),))
    assert not survey.looping()
    assert survey.avoid == set()
    assert survey.detour is None


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


def test_bags_hold_items_and_a_full_pack_still_reclaims():
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
    # Coin on the body is taken even when nothing else will fit.
    assert intent.kind == "reclaim"
    assert intent.where == (80.0, -40.0, 5.0)


def test_bags_short_and_trash_slots_for_sell():
    bag = Inventory()
    assert bags_short(bag) == 8
    bag.slots[22] = Held(BACKPACK_ITEM, 22, 1, "Backpack", "", bag_slots=8, bag_size=4)
    bag.slots[23] = Held(13068, 23, 1, "Rat Whiskers", "")
    bag.slots[24] = Held(13070, 24, 1, "Bread", "")
    bag.slots[251] = Held(13069, 251, 1, "Gnoll Fur", "")
    assert bags_short(bag) == 7
    assert has_loot_room(bag)  # empty general slots remain
    junk = trash_slots(bag, protect=set())
    assert 23 in junk and 251 in junk
    assert 22 not in junk  # backpack stays
    assert 24 not in junk  # a food word in the name is kept
    # Fill every pocket and general — no loot room, sell trash.
    for slot in range(24, 30):
        bag.slots[slot] = Held(slot, slot, 1, "fill", "")
    for index in range(8):
        bag.slots[251 + index] = Held(1000 + index, 251 + index, 1, "junk", "")
    assert not has_loot_room(bag)
    assert trash_slots(bag, protect=set())


def test_exhausted_headings_use_a_shorter_step():
    assert next_length(4.0) == 2.0
    assert next_length(2.0) == 1.0
    assert next_length(1.0) == 0.5
    assert next_length(0.5) is None
    here = (2.0, -146.0, 20.0)
    goal = (20.0, -146.0, 19.0)
    long = other_step(here, goal, set(), 4.0)
    short = other_step(here, goal, set(), 1.0)
    assert long is not None and short is not None
    assert abs(long[0] - here[0]) <= 4.01
    assert abs(short[0] - here[0]) <= 1.01
    # A one-yard drop fits the stride budget, so the step takes the ramp.
    assert long[2] == 19.0
    assert short[2] == 19.0
    assert refused(here, (4.0, -146.0, 20.0), here)
    assert blocks_step((6.0, -146.0), here, (10.0, -146.0, 20.0))
    assert not blocks_step((2.2, -146.0), here, (10.0, -146.0, 20.0))


def test_he_picks_the_option_that_finishes_the_open_step():
    script = parse_script(
        """
        if ($text=~/hail/i) {
          quest::say("be [blessed] or [review]");
        }
        elsif ($text=~/blessed/i) {
          quest::updatetaskactivity(1448, 5);
        }
        elsif ($text=~/review/i) {
          quest::say("again");
        }
        """,
        "Rytan.pl",
    )
    assert reply_order(["review", "blessed"], script, {(1448, 5)}, set()) == ["blessed", "review"]
    assert reply_order(["wish"], script, set(), {"wish"}) == []


def test_a_popup_names_the_next_person():
    arias = "Then click on Absor's Name under 'Weapons'. A glowing pathway will appear. " "Press 'OK' to continue."
    assert lesson_from(arias) == lesson_from("click on Absor's Name")
    found = lesson_from(arias)
    assert found is not None
    assert (found.kind, found.name) == ("talk", "Absor")
    rahtiz = lesson_from("Hail Guard Rahtiz if you have not done so already.")
    assert rahtiz is not None and (rahtiz.kind, rahtiz.name) == ("talk", "Guard Rahtiz")
    soul = lesson_from("Ask Rashere to 'bind my soul' to continue.")
    assert soul is not None and (soul.kind, soul.name, soul.text) == ("say", "Rashere", "bind my soul")
    assert lesson_from("Press 'OK' to continue.") is None
    weapon = lesson_from("Give your weapon to Absor to continue.")
    assert weapon is not None and (weapon.kind, weapon.name) == ("hand_in", "Absor")
    improved = lesson_from(
        "Pick up the improved weapon in your inventory and drop it on the rectangular icon "
        "in the middle of your inventory window. This will auto-equip the weapon back in "
        "your primary weapon slot. Use the find command (CTRL + F) to find the next npc."
    )
    assert improved is not None and (improved.kind, improved.name) == ("equip", "primary")
    tome = lesson_from(
        "Rytan has given you a skill tome! To learn this combat ability, simply find it "
        "in your inventory and right click on the tome."
    )
    assert tome is not None and (tome.kind, tome.name) == ("learn", "tome")
    assert server_slot(13) == 13
    assert server_slot(30) == 33
    assert server_slot(251) == 4010


def test_find_draws_the_path_past_where_he_stands():
    from eqclient.packets import find_destination

    def point(x, y, z):
        return struct.pack("<fff", y, x, z)

    destination = (-200.0, -94.0, 15.0)
    here = (-35.0, -141.0, 14.0)
    nxt = (-48.0, -137.0, 13.0)
    payload = (
        point(*destination)
        + point(*destination)
        + point(*here)
        + point(*nxt)
        + point(*destination)
        + point(*destination)
    )
    assert find_destination(payload) == destination
    route = guide_from(find_path(payload), here)
    assert route[0] == nxt
    assert route[-1] == destination
    npc, y, x, z = struct.unpack("<Ifff", find_person_request(42, *here))
    assert (npc, x, y, z) == (42, *here)


def test_a_quest_popup_is_answered_with_ok():
    packet = bytearray(4244)
    packet[:4] = b"Find"
    packet[128:160] = b'Press <c "#F07F00">OK</c> to continue.'
    struct.pack_into("<I", packet, 4232, 7)
    title, text, popup_id = popup_message(bytes(packet))
    assert title == "Find"
    assert text == "Press OK to continue."
    assert popup_id == 7
    assert popup_response(popup_id) == struct.pack("<II", 0, 7)


def _serialized(slot: int, item_id: int, name: str) -> bytes:
    instance = f"1|0|{slot}|0|1|0|0|0|0|0|0|"
    static = f"0|{name}|lore|IT{item_id}|{item_id}|" + "|".join("0" for _ in range(12))
    return (instance + '"' + static).encode("latin1") + b"\x00"


def test_login_inventory_lists_the_primary_weapon():
    payload = _serialized(13, 9998, "Short Sword") + _serialized(22, 1001, "Bread")
    rows = parse_inventory(payload)
    assert [(row[1], row[4], row[2]) for row in rows] == [(13, 9998, "Short Sword"), (22, 1001, "Bread")]
    bag = Inventory()
    bag.load_inventory(payload)
    assert bag.slots[13].name == "Short Sword"
    assert bag.slot_of(9998) == 13


def test_a_skill_tome_is_learned_before_the_next_hail():
    world = _world()
    world.spawns[2] = Spawn(2, "Xenaida", 1, 50, 1, -80.0, -40.0, 10.0, 1, 1)
    book = TaskBook()
    book.set_here("tutorialb")
    book.add(Activity(1448, 3, 1, SPEAK, "Xenaida"))
    bag = Inventory()
    bag.load_inventory(_serialized(30, 59973, "Tome of Throw Stone"))
    intent = choose(world, book, ZoneQuests("tutorialb"), bag, True)
    assert intent is not None
    assert intent.kind == "learn"
    assert intent.name == "Tome of Throw Stone"
    bag.failed_tomes.add(30)
    intent = choose(world, book, ZoneQuests("tutorialb"), bag, True)
    assert intent is None or intent.kind != "learn"


def test_an_open_step_follows_the_script_that_checks_it_off():
    world = _world()
    world.spawns[2] = Spawn(2, "Xenaida", 1, 50, 1, -80.0, -40.0, 10.0, 1, 1)
    world.spawns[3] = Spawn(3, "Vahlara", 1, 50, 1, -10.0, -20.0, 10.0, 1, 1)
    book = TaskBook()
    book.set_here("tutorialb")
    book.add(Activity(1448, 3, 1, DELIVER, "Xenaida"))
    quests = ZoneQuests("tutorialb")
    quests.scripts["vahlara"] = parse_script(
        "sub EVENT_SAY { if ($text=~/others/i) { quest::updatetaskactivity(1448, 3); } }",
        "Vahlara.pl",
    )
    intent = choose(world, book, quests, Inventory(), True)
    assert intent is not None
    assert (intent.kind, intent.target) == ("task_talk", 3)


def test_a_checked_off_stage_leaves_the_hail_that_did_not_finish():
    world = _world()
    world.spawns[1] = Spawn(1, "Arias", 1, 50, 1, -44.0, -119.0, 19.0, 1, 1)
    world.spawns[2] = Spawn(2, "Xenaida", 1, 50, 1, -80.0, -40.0, 10.0, 1, 1)
    book = TaskBook()
    book.set_here("tutorialb")
    book.add(Activity(1448, 0, 1, SPEAK, "Arias"))
    book.add(Activity(1448, 2, 1, SPEAK, "Vahlara", done=1))
    book.add(Activity(1448, 3, 1, SPEAK, "Xenaida"))
    intent = choose(world, book, ZoneQuests("tutorialb"), Inventory(), True, said={("arias", "hail")})
    assert intent is not None
    assert intent.target == 2


def test_a_hailed_npc_gets_the_weapon_from_that_list():
    world = _world()
    world.spawns[1] = Spawn(1, "Arias", 1, 50, 1, -44.0, -119.0, 19.0, 1, 1)
    world.spawns[2] = Spawn(2, "Absor000", 1, 50, 1, -200.0, -95.0, 15.0, 1, 1)
    book = TaskBook()
    book.set_here("tutorialb")
    book.add(Activity(1448, 0, 1, SPEAK, "Arias"))
    quests = ZoneQuests("tutorialb")
    quests.scripts["Absor"] = parse_script(
        "sub EVENT_ITEM { if (plugin::check_handin(\\%itemcount, 9998 => 1)) { quest::summonitem(59951); } }",
        "Absor.pl",
    )
    bag = Inventory()
    bag.load_inventory(_serialized(13, 9998, "Short Sword"))
    intent = choose(world, book, quests, bag, True, said={("absor000", "hail")})
    assert intent is not None
    assert (intent.kind, intent.target, intent.item_id) == ("hand_in", 2, 9998)


def test_a_saylink_is_the_word_to_say_back():
    body = "0FFFFF000070000000000000000000000000000000000"
    assert len(body) == 45
    text = "if you [\x12" + body + "wish\x12]."
    assert saylink_words(text) == ["wish"]


def test_a_refused_heading_tries_a_different_step():
    here = (2.0, -146.0, 20.0)
    goal = (-5.0, -142.0, 14.0)
    direct = other_step(here, goal, set())
    assert direct is not None
    # Six yards down equals the stride budget, so this step lands on the goal height.
    assert direct[2] == 14.0
    sunk = other_step((-326.0, -391.0, 20.0), (-326.0, -400.0, -38.0), set(), 4.0)
    # Fifty-eight yards down. A 4-yard stride may drop 6, not the whole cliff.
    assert sunk is not None and sunk[2] == 14.0
    used = {bearing(here, direct)}
    nxt = other_step(here, goal, used)
    assert nxt is not None
    assert bearing(here, nxt) not in used
    assert abs(nxt[0] - direct[0]) > 1.0 or abs(nxt[1] - direct[1]) > 1.0


def test_a_step_is_local_in_the_zone_it_names():
    book = TaskBook()
    book.set_here("poknowledge", 202)
    book.add(Activity(80, 1, 1, KILL, "a gnoll", zone_id=189))
    assert book.current() == []
    assert book.away_zone_id() == 189
    book.set_here("tutorialb", 189)
    assert book.current()[0].target_name == "a gnoll"
    assert book.away_zone_id() == 0


def test_a_step_with_no_zone_stays_where_the_packet_arrived():
    book = TaskBook()
    book.set_here("tutorialb", 189)
    book.add(Activity(80, 1, 1, KILL, "a gnoll"))
    book.set_here("poknowledge", 202)
    assert book.current() == []
    assert book.away_zone_id() == 189


def test_a_finished_local_list_uses_the_door_to_the_step_zone():
    world = _world()
    world.zone = "poknowledge"
    world.zone_id = 202
    book = TaskBook()
    book.set_here("poknowledge", 202)
    book.add(Activity(80, 1, 1, KILL, "a gnoll", zone_id=45))
    quests = ZoneQuests("poknowledge")
    quests.destinations[3] = [45]
    quests.destinations[9] = [9]
    world.doors[3] = Door(3, "qcat", 40.0, -80.0, 19.0, 5)
    world.doors[9] = Door(9, "elsewhere", 4.0, -140.0, 19.0, 5)
    intent = guide(world, book, quests, Inventory(), True)
    assert intent is not None
    assert intent.kind == "leave"
    assert intent.target == 3


def test_no_door_to_that_zone_does_not_take_another_exit():
    world = _world()
    world.zone = "poknowledge"
    world.zone_id = 202
    world.level = 5
    book = TaskBook()
    book.set_here("poknowledge", 202)
    book.add(Activity(80, 1, 1, KILL, "a gnoll", zone_id=45))
    quests = ZoneQuests("poknowledge")
    quests.exits = [4]
    quests.destinations[4] = [9]
    world.doors[4] = Door(4, "book", 10.0, -100.0, 19.0, 5)
    intent = guide(world, book, quests, Inventory(), True)
    assert intent is not None
    assert intent.kind != "leave"


def test_level_four_in_the_mines_still_looks_for_hobart():
    world = _world()
    world.zone_id = 189
    world.home_zone_id = 202
    quests = ZoneQuests("tutorialb")
    quests.destinations[11] = [202]
    world.doors[11] = Door(11, "exit", 10.0, -100.0, 19.0, 5)
    intent = guide(world, TaskBook(), quests, Inventory(), True)
    assert intent is not None
    assert intent.kind == "explore"
    assert intent.name == "Guard Hobart"


def test_an_empty_book_walks_through_the_door_home():
    world = _world()
    world.zone = "poknowledge"
    world.zone_id = 202
    world.level = 5
    world.home_zone_id = 45
    quests = ZoneQuests("poknowledge")
    quests.destinations[3] = [45]
    world.doors[3] = Door(3, "qcat", 10.0, -100.0, 19.0, 5)
    intent = guide(world, TaskBook(), quests, Inventory(), True)
    assert intent is not None
    assert intent.kind == "leave"
    assert intent.target == 3
    assert intent.name == "zone 45"


def test_home_with_nothing_to_do_stays_put():
    world = _world()
    world.zone = "poknowledge"
    world.zone_id = 202
    world.level = 5
    world.home_zone_id = 202
    quests = ZoneQuests("poknowledge")
    quests.exits = [4]
    quests.destinations[4] = [45]
    world.doors[4] = Door(4, "book", 10.0, -100.0, 19.0, 5)
    intent = guide(world, TaskBook(), quests, Inventory(), True)
    assert intent is not None
    assert intent.kind != "leave"


def test_the_profile_bind_is_home():
    blob = bytearray(2264)
    struct.pack_into("<I", blob, 24, 202)
    played = player_profile(bytes(blob))
    assert played is not None
    assert played.home_zone_id == 202
    world = ZoneModel("Mockone")
    world.apply_played(played)
    assert world.home_zone_id == 202


def test_a_door_script_records_each_zone_it_moves_to():
    text = """
    sub EVENT_CLICKDOOR {
      my $d_id = ($doorid % 256);
      if ($d_id == 11) {
        quest::movepc(9, 1, 2, 3);
        quest::movepc(202, -55, 44, -158.81);
      }
    }
    """
    assert door_destinations(text) == {11: [9, 202]}


def test_a_late_server_position_does_not_walk_him_backward():
    world = ZoneModel("Mockone")
    world.predict(2.0, -146.0, 20.0)
    world.arm_step((2.0, -146.0, 20.0), (6.0, -146.0, 20.0))
    world.predict(6.0, -146.0, 20.0)
    world.apply_server_position(2.0, -146.0, 20.0)
    assert world.position == (6.0, -146.0, 20.0)
    world.apply_server_position(4.0, -146.0, 20.0)
    assert world.position == (6.0, -146.0, 20.0)
    world.apply_server_position(6.1, -146.0, 20.0)
    assert world.step_state == "confirmed"
    assert abs(world.position[0] - 6.1) < 0.01
    world.arm_step((6.1, -146.0, 20.0), (10.1, -146.0, 20.0))
    world.predict(10.1, -146.0, 20.0)
    world.step_sent_at -= 0.2
    world.apply_server_position(6.1, -146.0, 20.0)
    assert world.step_state == "refused"
    assert abs(world.position[0] - 6.1) < 0.01


def test_a_missing_position_update_is_a_blocked_step():
    origin = (2.0, -146.0, 19.0)
    asked = (-6.0, -146.0, 19.0)
    assert refused(origin, asked, origin)
    assert not refused(origin, asked, asked)
    packet = movement_history(10.0, -20.0, 3.0, 1000)
    assert len(packet) == 17
    y, x, z, kind, stamp = struct.unpack("<fffBI", packet)
    assert (x, y, z, kind, stamp) == (10.0, -20.0, 3.0, 0, 1000)


def test_low_health_finishes_the_fight_before_sitting():
    assert recover(True, True, False) is None
    assert recover(True, False, False) == "safe"
    assert recover(True, False, True) == "rest"
    assert recover(True, False, False, sit_here=True) == "rest"
    assert recover(False, False, False) is None


def test_low_health_sits_until_he_is_nearly_full():
    world = ZoneModel("Mocktwo")
    # Sit at half the bar. Stay down until 90%.
    world.hp = 1
    world.max_hp = 40
    assert world.needs_rest(sitting=False)
    world.hp = 20  # 50%
    assert world.needs_rest(sitting=False)
    world.hp = 21  # above half — keep fighting
    assert not world.needs_rest(sitting=False)
    world.hp = 22
    assert not world.needs_rest(sitting=False)
    assert world.needs_rest(sitting=True)
    world.hp = 35  # still under 90%
    assert world.needs_rest(sitting=True)
    world.hp = 36  # 90% stands
    assert not world.needs_rest(sitting=True)
    world.hp = 0
    assert not world.needs_rest(sitting=False)
