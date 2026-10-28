"""The decisions in the smarter-agent plan, without a live zone."""

import struct
from pathlib import Path

from eqclient.builds import build_for, gear_value, next_train
from eqclient.conduct import Recipe, RecipeBook, ability_for, bar_needed, craft_for, ensure_recipes, order_of, recipe_ready, recipes_from_lines, role_of, write_recipes
from eqclient.explore import is_stair, _step_height
from eqclient.items import Held, Inventory, loot_picks
from eqclient.journal import Journal
from eqclient.packets import cast_packet, consume_packet, group_invite, memorize_packet, player_profile, profile_spells
from eqclient.agent import _turn_ids, pick_station
from eqclient.campaign import FARM, Campaign
from eqclient.drops import DropBook, drops_from_lines, ensure_drops, write_drops
from eqclient.merchants import ensure_merchants, merchants_from_lines
from eqclient.spells import SpellBook, SpellScroll, apply_spell_goals, ensure_spells, spell_step, spells_from_lines
from eqclient.plan import choose, guide, hub_goal
from eqclient.quests import QuestGraph, ZoneQuests, parse_chain, next_node
from eqclient.tasks import TaskBook
from eqclient.tactics import fight_tactic, may_melee
from eqclient.world import Door, Ground, Spawn, ZoneModel

from tests.test_progress import _world


def test_a_city_with_nothing_open_walks_to_a_named_npc_then_sits():
    world = _world()
    world.zone = "poknowledge"
    world.zone_id = 202
    world.safe = (0.0, 0.0, 0.0)
    world.predict(10.0, 10.0, 0.0)
    world.spawns[3] = Spawn(3, "a cleric", 1, 21, 1, 40.0, 40.0, 0.0, 1, 1)
    quests = ZoneQuests("poknowledge")
    quests.scripts["a cleric"] = object()
    intent = hub_goal(world, quests, set())
    assert intent.kind == "explore" and intent.name == "hub"
    world.predict(80.0, 0.0, 0.0)
    intent = hub_goal(world, quests, {"a cleric"})
    assert intent.kind == "explore" and intent.name == "safe"
    world.predict(1.0, 1.0, 0.0)
    intent = hub_goal(world, quests, {"a cleric"})
    assert intent.kind == "rest"


def test_ramps_follow_and_cliffs_ease_and_stairs_snap():
    # Cliff: ease down by stride budget, do not teleport 58 yd.
    assert _step_height(20.0, -38.0, 4.0) == 14.0
    # Ramp within budget follows mesh/goal Z.
    assert _step_height(-51.0, -45.0, 4.0) == -45.0
    assert not is_stair([(0, 0, 0), (1, 0, 20)])
    stairs = [(0, 0, 0), (4, 0, 4), (8, 0, 8), (12, 0, 12)]
    assert is_stair(stairs)
    assert _step_height(0.0, 4.0, 4.0, stair=True) == 4.0


def test_a_chain_waits_for_the_earlier_word_and_the_class():
    text = """
    sub EVENT_SAY {
      if ($text=~/hail/i) { quest::say("hello"); }
      if ($text=~/secret/i && $class == 2) { quest::setglobal("clericflag", 1, 5, "F"); quest::movepc(202, 0, 0, 0); }
    }
    if (plugin::check_handin(\\%itemcount, 1001 => 1\\)) { quest::say("done"); }
    """
    nodes = parse_chain(text, "Priest.pl")
    assert [node.word for node in nodes if node.kind == "say"] == ["hail", "secret"]
    assert next_node(nodes, set(), set(), 1, set()).word == "hail"
    assert next_node(nodes, {"hail"}, set(), 1, set()) is None
    cleric = next_node(nodes, {"hail"}, set(), 2, set())
    assert cleric.word == "secret" and cleric.zone_id == 202 and "clericflag" in cleric.grants
    hand = next_node(nodes, {"hail", "secret"}, {"clericflag"}, 2, {1001})
    assert hand.kind == "hand" and hand.item_id == 1001


def test_a_tell_is_an_order_and_a_half_empty_bar_wants_food():
    order = order_of("Mockone", "attack a spider")
    assert order.verb == "attack" and order.rest == "a spider"
    assert order_of("Mockone", "hello") is None
    assert bar_needed(20, 127) == "food"
    assert bar_needed(127, 127) == ""
    assert role_of("Minor Snare") == "snare"
    rows = [
        "INSERT INTO `tradeskill_recipe_entries` VALUES\n",
        "(1,9,100,1,0,0,0,0),\n",
        "(2,9,1,0,0,2,0,0),\n",
        "INSERT INTO `items` VALUES\n",
    ]
    recipes = recipes_from_lines(rows)
    assert craft_for({100}, {1: 2}, recipes) == 9
    assert recipe_ready(100, ((1, 2), (3, 1)), {1: 2, 3: 1})
    assert not recipe_ready(100, ((1, 2),), {1: 1})


def test_root_is_not_auto_attacked_and_a_group_uses_the_team_role():
    assert fight_tactic(11, False) == "pet"
    assert fight_tactic(11, True) == "assist"
    assert fight_tactic(1, True) == "tank"
    assert not may_melee("kite", rooted=True, snared=True, slowed=False, hp_ratio=1)
    assert may_melee("kite", rooted=False, snared=True, slowed=False, hp_ratio=0.8)
    assert not may_melee("slow", rooted=False, snared=False, slowed=False, hp_ratio=1)


def test_a_warrior_trains_defense_before_a_seed_and_a_cleric_values_a_weapon():
    warrior = build_for(1)
    assert next_train(warrior, {}, 4, set()) == warrior.spend[0]
    known = {skill: 40 for skill in warrior.spend}
    assert next_train(warrior, known, 4, set()) == warrior.seed[0]
    cleric = build_for(2)
    assert gear_value(cleric, ac=10, damage=2) > gear_value(cleric, ac=20, damage=0)
    assert gear_value(warrior, ac=20, damage=0) > gear_value(warrior, ac=0, damage=4)


def test_packets_match_the_titanium_layouts():
    assert len(consume_packet(22, 1)) == 16
    assert consume_packet(22, 1)[4:8] == b"\xff\xff\xff\xff"
    assert len(memorize_packet(0, 12, 1)) == 16
    assert len(cast_packet(0, 12, 9)) == 20
    assert len(group_invite("Mocktwo", "Mockone")) == 128


def test_a_scroll_is_written_into_the_book_before_it_can_be_gemmed():
    bag = Inventory()
    bag.slots[22] = Held(100, 22, 1, "Spell: Minor Healing", "", item_type=20, scroll_spell=15)
    bag.spell_names[15] = "Spell: Minor Healing"
    bag.slots[23] = Held(101, 23, 1, "Tome of Throw Stone", "", item_type=20, scroll_spell=0)
    step = spell_step(bag, 2)
    assert step is not None and step[0] == "scribe" and step[1] == 15
    assert spell_step(bag, 2)[0] != "memorize"
    bag.scribed.add(15)
    bag.book[0] = 15
    step = spell_step(bag, 2)
    assert step is not None and step[0] == "memorize" and step[1] == 15 and step[2] == "heal"
    profile = bytearray(5000)
    struct.pack_into("<I", profile, 2312, 15)
    struct.pack_into("<I", profile, 4360, 15)
    book, gems = profile_spells(bytes(profile))
    assert book[0] == 15 and gems[0] == 15


def _sql_row(width: int, values: dict[int, object]) -> str:
    fields = ["0"] * width
    for index, value in values.items():
        fields[index] = str(value)
    body = []
    for index, value in enumerate(fields):
        raw = values.get(index, 0)
        if isinstance(raw, str):
            body.append("'" + raw.replace("'", "''") + "'")
        else:
            body.append(fields[index])
    return "(" + ",".join(body) + "),"


def test_a_level_pushes_one_scroll_for_each_spell_still_missing(tmp_path):
    """Class, level, and name come from the dump. Each missing spell is one item on the stack."""
    levels = {104: 255, 105: 1, 106: 6, 107: 8, 109: 1}
    courage = {104 + index: 255 for index in range(16)}
    courage[105] = 5
    lines = [
        "INSERT INTO `spells_new` VALUES",
        _sql_row(120, {0: 200, 1: "Minor Healing", **levels}),
        _sql_row(120, {0: 201, 1: "Courage", **courage}),
        "INSERT INTO `items` VALUES",
        _sql_row(160, {0: 50, 2: "Ancient Minor Healing", 82: 20, 159: 200}),
        _sql_row(160, {0: 9993, 2: "Spell: Minor Healing", 82: 20, 159: 200}),
        _sql_row(160, {0: 9994, 2: "Tome of Minor Healing", 82: 20, 159: 200}),
        _sql_row(160, {0: 80, 2: "Spell: Courage", 82: 20, 159: 201}),
    ]
    book = spells_from_lines(lines)
    cleric = book.by_class[2]
    assert [(row.level, row.name, row.item_id) for row in cleric] == [
        (1, "Minor Healing", 9993),
        (5, "Courage", 80),
    ]
    assert book.missing(2, 4, set(), set())[0].item_id == 9993
    assert [row.item_id for row in book.missing(2, 5, {200}, set())] == [80]
    assert book.missing(4, 7, set(), set()) == []
    assert [row.level for row in book.missing(4, 8, set(), set())] == [8]
    assert book.missing(1, 10, set(), set()) == []

    campaign = Campaign(2)
    campaign.set_goal(60329)
    added = apply_spell_goals(campaign, book, 2, 5, set(), set())
    assert added is not None and added[1] == ["Minor Healing", "Courage"]
    assert campaign.stack == [60329, 9993, 80]
    assert apply_spell_goals(campaign, book, 2, 5, {200}, {80}) == (1, [])
    assert campaign.stack == [60329, 80]

    quiet = Campaign(2)
    assert apply_spell_goals(quiet, book, 2, 5, set(), set(), graph=type("G", (), {"items": {}, "edges": []})()) is None
    sourced = type(
        "G",
        (),
        {
            "items": {},
            "edges": [{"rel": "gives", "to": "item:9993", "from": "freporte/a priest#hail"}],
        },
    )()
    assert apply_spell_goals(quiet, book, 2, 5, set(), set(), graph=sourced) == (0, ["Minor Healing"])
    assert quiet.stack == [9993]

    path = tmp_path / "spells.jsonl"
    from eqclient.spells import write_spells

    write_spells(book, str(path))
    restored = ensure_spells(str(path), str(tmp_path / "missing.sql"))
    assert [(row.class_id, row.level, row.name, row.spell_id, row.item_id) for row in restored.rows] == [
        (row.class_id, row.level, row.name, row.spell_id, row.item_id) for row in book.rows
    ]
    assert restored.item_spell[9993] == 200


def test_a_vendor_sells_the_item_and_a_short_purse_farms_first(tmp_path):
    """Terminal leaves buy from the merchant cache. Too little coin pushes a farm layer."""
    chesgard = ["0"] * 19
    chesgard[0], chesgard[1], chesgard[18] = "10", "'Chesgard_Sydwend'", "5"
    peran = ["0"] * 19
    peran[0], peran[1], peran[18] = "11", "'Peran'", "6"
    lines = [
        "INSERT INTO `zone` VALUES",
        "('qeynos',1,'','Qeynos',NULL,0,0,0,0,0,0,0,0,1),",
        "('freporte',2,'','Freeport',NULL,0,0,0,0,0,0,0,0,10),",
        "INSERT INTO `npc_types` VALUES",
        "(" + ",".join(chesgard) + "),",
        "(" + ",".join(peran) + "),",
        "INSERT INTO `spawnentry` VALUES",
        "(3,10),",
        "(4,11),",
        "INSERT INTO `spawn2` VALUES",
        "(1,3,'qeynos'),",
        "(2,4,'freporte'),",
        "INSERT INTO `merchantlist` VALUES",
        "(5,1,9993,0,0,0,0,0,0,100),",
        "(6,1,9993,0,0,0,0,0,0,100),",
        "(5,2,50,0,0,0,0,5,0,100),",
        "INSERT INTO `items` VALUES",
        _sql_row(50, {0: 9993, 49: 2500}),
        _sql_row(50, {0: 50, 49: 10}),
    ]
    book = merchants_from_lines(lines)
    assert book.by_npc[10]["zone"] == 1 and book.by_npc[10]["where"] == "qeynos"
    assert book.by_npc[10]["items"] == [9993]
    assert book.by_item[9993]["npcs"] == [10, 11] and book.by_item[9993]["cost"] == 2500
    assert 50 not in book.by_item
    seller, cost = book.best(9993, "freporte")
    assert seller.npc_id == 11 and seller.zone == "freporte" and cost == 2500
    seller, _cost = book.best(9993, "oot")
    assert seller.npc_id == 10

    path = tmp_path / "merchants.jsonl"
    from eqclient.merchants import write_merchants

    write_merchants(book, str(path))
    loaded = ensure_merchants(str(path))
    assert loaded.by_npc[10]["name"] == "Chesgard Sydwend"

    graph = type("G", (), {"edges": [], "items": {}})()
    camp = Campaign(2)
    camp.set_goal(9993)
    short = camp.next_step(graph, {}, {}, level=70, here="oot", copper=100, merchants=book)
    assert short.kind == "farm" and short.count == 2500
    assert camp.stack == [9993, FARM]
    paid = camp.next_step(graph, {}, {}, level=70, here="qeynos", copper=2500, merchants=book)
    assert paid.kind == "buy" and paid.npc == "Chesgard Sydwend" and paid.zone == "qeynos"
    assert camp.stack == [9993]

    spells = SpellBook()
    spells.rows = [SpellScroll(2, 1, "Minor Healing", 200, 9993)]
    spells.index()
    quiet = Campaign(2)
    added = apply_spell_goals(quiet, spells, 2, 1, set(), set(), graph=graph, merchants=book)
    assert added == (0, ["Minor Healing"])

    purse = bytearray(4464)
    struct.pack_into("<IIII", purse, 4448, 2, 5, 0, 0)
    played = player_profile(bytes(purse))
    assert played.coin_known and played.platinum == 2 and played.gold == 5


def test_a_certain_drop_sends_him_to_the_mob_when_no_quest_names_it(tmp_path):
    """Drop chances are cached. The kill target is the mob with the highest chance."""
    pup = ["0"] * 18
    pup[0], pup[1], pup[3], pup[17] = "40", "a_pup", "5", "7"
    kor = ["0"] * 18
    kor[0], kor[1], kor[3], kor[17] = "42", "a_kor", "20", "7"
    rat = ["0"] * 18
    rat[0], rat[1], rat[3], rat[17] = "44", "a_rat", "1", "9"
    gnoll = ["0"] * 18
    gnoll[0], gnoll[1], gnoll[3], gnoll[17] = "43", "a_gnoll", "10", "8"
    lines = [
        "INSERT INTO `zone` VALUES",
        "('qeynos',1,'','Qeynos',NULL,0,0,0,0,0,0,0,0,1),",
        "('unrest',2,'','Unrest',NULL,0,0,0,0,0,0,0,0,45),",
        "('freporte',3,'','Freeport',NULL,0,0,0,0,0,0,0,0,10),",
        "INSERT INTO `npc_types` VALUES",
        "(" + ",".join(pup) + "),",
        "(" + ",".join(kor) + "),",
        "(" + ",".join(gnoll) + "),",
        "(" + ",".join(rat) + "),",
        "INSERT INTO `spawnentry` VALUES",
        "(3,40),",
        "(4,42),",
        "(5,43),",
        "(6,44),",
        "INSERT INTO `spawn2` VALUES",
        "(1,3,'qeynos'),",
        "(2,4,'unrest'),",
        "(3,5,'unrest'),",
        "(4,6,'freporte'),",
        "INSERT INTO `loottable_entries` VALUES",
        "(7,1,1,0,0,100),",
        "(7,5,2,0,0,100),",
        "(9,2,1,0,0,100),",
        "(9,3,1,1,1,100),",
        "(8,4,1,0,0,50),",
        "(8,6,1,2,0,100),",
        "(8,7,1,0,0,100),",
        "INSERT INTO `lootdrop_entries` VALUES",
        "(1,10524,1,0,80,0,0,0,1,0,0),",
        "(1,10529,1,0,100,0,0,0,1,30,0),",
        "(2,10524,1,0,15),",
        "(2,10525,1,0,15),",
        "(3,10526,1,0,100),",
        "(3,10527,1,0,100),",
        "(4,10528,1,0,100),",
        "(5,10530,1,0,50),",
        "(6,10532,1,0,50),",
        "(7,10531,1,0,50,0,0,0,2),",
    ]
    book = drops_from_lines(lines)
    assert book.by_npc[42]["where"] == "unrest"
    assert book.chance(10524, 42) == 80
    assert book.chance(10524, 40) == 80
    assert book.chance(10524, 44) == 15
    assert book.chance(10525, 44) == 15
    assert book.chance(10526, 44) == 50
    assert book.chance(10527, 44) == 50
    assert book.chance(10528, 43) == 50
    assert book.chance(10530, 42) == 75
    assert book.chance(10531, 43) == 75
    assert book.chance(10532, 43) == 75
    assert 10529 not in book.by_item
    assert book.best(10524, "freporte").npc_id == 40
    assert book.best(10524, "unrest").name == "a kor"
    assert book.best(10524, "qeynos").npc_id == 40

    path = tmp_path / "drops.jsonl"
    write_drops(book, str(path))
    loaded = ensure_drops(str(path))
    assert loaded.by_npc[40]["name"] == "a pup"
    assert loaded.best(10524, "unrest").chance == 80

    graph = type("G", (), {"edges": [], "items": {}})()
    camp = Campaign(1)
    camp.set_goal(10524)
    away = camp.next_step(graph, {}, {}, level=70, here="freporte", drops=book)
    assert away.kind == "travel" and away.zone == "qeynos" and away.npc == "a pup"
    home = Campaign(1)
    home.set_goal(10524)
    kill = home.next_step(graph, {}, {}, level=70, here="unrest", drops=book)
    assert kill.kind == "loot" and kill.npc == "a kor" and kill.text == "kill"

    listed = type("G", (), {"edges": [{"rel": "loots", "to": "item:10524", "zone": "crushbone", "npc": "orc centurion"}], "items": {}})()
    named = Campaign(1)
    named.set_goal(10524)
    quest = named.next_step(listed, {}, {}, level=70, here="crushbone", drops=book)
    assert quest.kind == "loot" and quest.npc == "orc centurion"

    world = _world()
    world.zone = "unrest"
    world.level = 70
    intent = guide(world, TaskBook(), ZoneQuests("unrest"), Inventory(), True, graph=graph, campaign=home, drops=book)
    assert intent is not None and intent.kind == "explore" and intent.name == "a kor" and intent.text == "loot"

    spells = SpellBook()
    spells.rows = [SpellScroll(1, 1, "Minor Healing", 200, 10524)]
    spells.index()
    quiet = Campaign(1)
    added = apply_spell_goals(quiet, spells, 1, 1, set(), set(), graph=graph, drops=book)
    assert added == (0, ["Minor Healing"])


def test_a_drop_farm_asks_for_the_count_still_missing():
    """Two combines of three hides farm six, then only the ones still missing."""
    book = DropBook()
    book.by_npc[42] = {"zone": 45, "where": "unrest", "name": "a kor", "level": 20, "items": [[10524, 80.0]]}
    book.by_item[10524] = {"npcs": [[42, 80.0]]}
    recipes = RecipeBook()
    recipes.by_id[1] = Recipe(1, 50, ((10524, 3),), container=17, results=((50, 1),))
    recipes.index()
    graph = type("G", (), {"edges": [], "items": {}})()
    camp = Campaign(1)
    camp.set_goal(50, 2)
    step = camp.next_step(graph, {}, {}, level=70, here="unrest", recipes=recipes, drops=book)
    assert camp.counts[10524] == 6
    assert step.kind == "loot" and step.npc == "a kor" and step.count == 6
    short = camp.next_step(graph, {10524: 4}, {}, level=70, here="unrest", recipes=recipes, drops=book)
    assert short.kind == "loot" and short.count == 2
    made = camp.next_step(graph, {10524: 6}, {}, level=70, here="unrest", recipes=recipes, drops=book)
    assert made.kind == "craft" and made.recipe_id == 1

    world = _world()
    world.zone = "unrest"
    world.level = 70
    world.spawns[7] = Spawn(7, "a kor", 1, 1, 1, 10.0, 10.0, 0.0, 1, 1)
    hunting = Campaign(1)
    hunting.set_goal(10524, 4)
    intent = guide(world, TaskBook(), ZoneQuests("unrest"), Inventory(), True, graph=graph, campaign=hunting, drops=book)
    assert intent is not None and intent.kind == "task_kill" and intent.name == "a kor"
    world.spawns[7] = Spawn(7, "a kor", 2, 1, 1, 10.0, 10.0, 0.0, 1, 1)
    corpse = guide(world, TaskBook(), ZoneQuests("unrest"), Inventory(), True, graph=graph, campaign=hunting, drops=book)
    assert corpse is not None and corpse.kind == "loot" and corpse.target == 7

    waiting = _world()
    waiting.zone = "unrest"
    waiting.level = 70
    waiting.spawns[8] = Spawn(8, "a gnoll", 1, 10, 1, 30.0, -140.0, 0.0, 1, 1)
    waiting.faction[8] = 8
    idle = Campaign(1)
    idle.set_goal(10524)
    clear = guide(waiting, TaskBook(), ZoneQuests("unrest"), Inventory(), True, graph=graph, campaign=idle, drops=book)
    assert clear is not None and clear.kind == "fight" and clear.name == "a gnoll" and clear.text == "respawn"
    waiting.spawns[7] = Spawn(7, "a kor", 2, 1, 1, 12.0, -140.0, 0.0, 1, 1)
    first = guide(waiting, TaskBook(), ZoneQuests("unrest"), Inventory(), True, graph=graph, campaign=idle, drops=book)
    assert first is not None and first.kind == "loot" and first.target == 7
    waiting.faction[8] = 4
    del waiting.spawns[7]
    roam = guide(waiting, TaskBook(), ZoneQuests("unrest"), Inventory(), True, graph=graph, campaign=idle, drops=book)
    assert roam is not None and roam.kind == "explore" and roam.name == "a kor"
    assert loot_picks([(0, 10524, 1), (1, 10524, 1), (2, 10524, 1)], {}, {10524: 2}) == [0, 1]
    assert loot_picks([(0, 10524, 10), (1, 10524, 1)], {10524: 1}, {10524: 2}) == [0]
    assert loot_picks([(0, 10524, 1)], {10524: 2}, {10524: 2}) == []


def test_a_recipe_makes_the_item_when_nothing_else_yields_it(tmp_path):
    """A combine in the recipe cache is the leaf when the graph never names the item."""
    book = RecipeBook()
    book.by_id[7] = Recipe(7, 10909, ((10908, 1),), container=17859, results=((10909, 1),), name="Blade of Tactics")
    book.by_id[8] = Recipe(8, 10909, ((10909, 1), (1, 1)), name="refund")
    book.by_id[9] = Recipe(9, 50, ((3, 1),), container=17, name="forge")
    book.index()
    assert book.for_item(10909).id == 7
    assert book.for_item(50).id == 9
    path = tmp_path / "recipes.jsonl"
    write_recipes(book, str(path))
    assert ensure_recipes(str(path)).for_item(10909).components == ((10908, 1),)

    graph = type("G", (), {"edges": [], "items": {}})()
    camp = Campaign(1)
    camp.set_goal(10909)
    camp.next_step(graph, {}, {}, level=70, here="qeynos", recipes=book)
    assert camp.stack == [10909, 17859]
    camp.next_step(graph, {17859: 1}, {}, level=70, here="qeynos", recipes=book)
    assert camp.stack[-1] == 10908
    made = camp.next_step(graph, {17859: 1, 10908: 1}, {}, level=70, here="qeynos", recipes=book)
    assert made.kind == "craft" and made.recipe_id == 7

    forge = Campaign(1)
    forge.set_goal(50)
    forge.next_step(graph, {}, {}, level=70, here="qeynos", recipes=book)
    assert forge.stack == [50, 3]

    spells = SpellBook()
    spells.rows = [SpellScroll(1, 1, "Minor Healing", 200, 10909)]
    spells.index()
    quiet = Campaign(1)
    added = apply_spell_goals(quiet, spells, 1, 1, set(), set(), graph=graph, recipes=book)
    assert added == (0, ["Minor Healing"])


def test_a_forage_only_happens_when_he_is_hungry_and_has_the_skill():
    assert ability_for(6, {27: 5}, hungry=True, in_fight=False, leaving=False) == "OP_Forage"
    assert ability_for(6, {27: 0}, hungry=True, in_fight=False, leaving=False) == ""
    assert ability_for(7, {25: 5}, hungry=False, in_fight=False, leaving=True) == "OP_FeignDeath"


def test_a_corpse_survives_a_zone_change_and_a_camped_body_asks_for_a_summon():
    world = _world()
    world.zone = "qeynos"
    world.needs_corpse = True
    world.own_corpse_at = (10.0, 20.0, 5.0)
    world.own_corpse_zone = "qeynos"
    payload = bytearray(600)
    payload[64:75] = b"poknowledge"
    world.on_new_zone(bytes(payload))
    assert world.needs_corpse
    assert world.own_corpse_zone == "qeynos"
    world.zone = "qeynos"
    world.zone_id = 1
    world.predict(0.0, 0.0, 0.0)
    world.safe = (0.0, 0.0, 0.0)
    world.spawns[4] = Spawn(4, "a gnoll", 1, 1, 1, 12.0, 20.0, 5.0, 1, 1)
    world.faction[4] = 8
    intent = choose(world, TaskBook(), ZoneQuests("qeynos"), Inventory(), True)
    assert intent is not None and intent.kind == "tell" and intent.name == "summon"


def test_a_zone_is_stored_when_he_enters_it_and_a_chain_can_continue_elsewhere():
    from eqclient.quests import build_graph, read_graph, write_graph
    from eqclient.zones import zone_id_of, zone_name_of

    journal = Journal(":memory:")
    journal.remember_zone("freporte", 10)
    assert journal.zones()["freporte"] == 10
    assert zone_id_of("freporte") == 10
    assert zone_name_of(10) == "freporte"
    journal.remember_zone("zone10", 10)
    assert "zone10" not in journal.zones()
    journal.close()

    world = _world()
    payload = bytearray(700)
    payload[64:72] = b"freporte"
    struct.pack_into("<H", payload, 684, 10)
    world.on_new_zone(bytes(payload))
    assert world.zone == "freporte" and world.zone_id == 10

    root = Path("/tmp/eq-graph-fixture")
    if root.exists():
        import shutil
        shutil.rmtree(root)
    (root / "freporte").mkdir(parents=True)
    (root / "freporte" / "Priest.pl").write_text(
        'if ($text=~/hail/i) { quest::say("hi"); }\nif ($text=~/secret/i) { quest::say("go"); }\n',
        encoding="utf-8",
    )
    (root / "qeynos").mkdir()
    (root / "qeynos" / "player.pl").write_text(
        "sub EVENT_CLICKDOOR {\n if ($d_id == 4) { quest::movepc(10, 0, 0, 0); }\n}\n",
        encoding="utf-8",
    )
    graph = build_graph(str(root))
    path = root / "quest_graph.jsonl"
    write_graph(graph, str(path))
    loaded = read_graph(str(path))
    assert loaded.continuation("qeynos", {("freporte", "priest", "hail")}, set(), 1, set()).word == "secret"
    assert loaded.continuation("qeynos", set(), set(), 1, set()) is None
    quests = ZoneQuests("qeynos")
    loaded.apply(quests)
    assert 10 in quests.destinations[4]
    world.zone = "qeynos"
    world.zone_id = 1
    world.doors[4] = Door(4, "zone", 5.0, 5.0, 0.0, 0)
    intent = guide(world, TaskBook(), quests, Inventory(), True, graph=loaded, said_all={("freporte", "priest", "hail")})
    assert intent is not None and intent.kind == "leave" and intent.name == "freporte"


def test_a_say_names_an_item_and_a_flag_gates_the_hand_in():
    from eqclient.catalog import Catalog, catalog_from_lines
    from eqclient.quests import build_graph, read_graph, write_graph

    catalog = Catalog()
    catalog_from_lines(
        [
            "INSERT INTO `items` VALUES\n",
            "(10524,0,'Eye of Kor'),\n",
            "(11858,0,'Words of Collection'),\n",
            "INSERT INTO `lootdrop_entries` VALUES\n",
            "(1,10524,1),\n",
            "INSERT INTO `loottable_entries` VALUES\n",
            "(9,1),\n",
            "INSERT INTO `npc_types` VALUES\n",
            "(42,'a kor',''," + ",".join(["0"] * 14) + ",9,0),\n",
            "INSERT INTO `spawnentry` VALUES\n",
            "(4,42),\n",
            "INSERT INTO `spawn2` VALUES\n",
            "(1,4,'unrest',0),\n",
        ],
        catalog,
    )
    assert catalog.zones[10524] == ("unrest",)
    root = Path("/tmp/eq-graph-items")
    if root.exists():
        import shutil
        shutil.rmtree(root)
    (root / "neriaka").mkdir(parents=True)
    (root / "neriaka" / "X-Ta_Tempi.pl").write_text(
        """
        if($text=~/hail/i){ quest::say("We three are the Sisters Dark."); }
        if($text=~/words of collection/i){
          quest::say("bring a globe of darkness, an Eye of Kor and an amber gem.");
        }
        if(plugin::check_handin(\\%itemcount, 10524 => 1)){
          quest::summonitem(11858);
        }
        """,
        encoding="utf-8",
    )
    (root / "nedaria").mkdir()
    (root / "nedaria" / "Tweister.lua").write_text(
        """
        function event_trade(e)
          local qglobals = eq.get_qglobals(e.other);
          if(qglobals["cleric_epic"] ~= nil and qglobals["cleric_epic"] >= "3" and item_lib.check_turn_in(e.trade, {item1 = 56015})) then
            eq.set_global("cleric_epic","4",5,"F");
          end
        end
        """,
        encoding="utf-8",
    )
    graph = build_graph(str(root), catalog)
    say = next(node for nodes in graph.nodes.values() for node in nodes if node.word == "words of collection")
    assert "Eye of Kor" in say.text
    names = [edge for edge in graph.edges if edge["rel"] == "names" and edge["to"] == "item:10524"]
    assert names and names[0]["from"].endswith("#words of collection")
    assert graph.items[10524]["zones"] == ["unrest"]
    receives = [edge for edge in graph.edges if edge["rel"] == "receives" and edge["to"] == "item:10524"]
    gives = [edge for edge in graph.edges if edge["rel"] == "gives" and edge["to"] == "item:11858"]
    assert receives and gives and receives[0]["group"] == gives[0]["group"]
    needs = [edge for edge in graph.edges if edge["rel"] == "needs" and edge["flag"] == "cleric_epic"]
    sets = [edge for edge in graph.edges if edge["rel"] == "sets" and edge["flag"] == "cleric_epic"]
    assert needs and needs[0]["at"] == ">=3"
    assert sets and sets[0]["value"] == "4"
    path = root / "quest_graph.jsonl"
    write_graph(graph, str(path))
    loaded = read_graph(str(path))
    assert loaded.items[10524]["name"] == "Eye of Kor"
    assert any(edge["rel"] == "then" for edge in loaded.edges)
    assert any(node.text.startswith("We three") for nodes in loaded.nodes.values() for node in nodes)


def test_a_lua_branch_a_recipe_and_a_held_item_stay_on_their_own_step():
    from eqclient.quests import link_script

    officer = """
    function event_say(e)
      if(e.message:findi("hail") and qglobals["ranger_epic"] == "5") then
        e.self:Say("Hello hunter.");
        eq.set_global("ranger_epic","6",5,"F");
      end
    end
    function event_trade(e)
      if(qglobals["ranger_epic"] == "6" and item_lib.check_turn_in(e.trade, {item1 = 62629})) then
        eq.set_global("ranger_epic","7",5,"F");
        e.other:QuestReward(e.self,{itemid=62649, exp=50000});
      end
    end
    """
    edges = link_script(officer, "Officer.lua", "nedaria")
    hail_sets = [edge for edge in edges if edge["rel"] == "sets" and edge["from"].endswith("#hail")]
    hail_needs = [edge for edge in edges if edge["rel"] == "needs" and edge["from"].endswith("#hail")]
    assert hail_sets and hail_sets[0]["value"] == "6"
    assert {edge["at"] for edge in hail_needs} == {"==5"}
    hand = [edge for edge in edges if edge["rel"] == "sets" and "62629" in edge["from"]]
    assert hand and hand[0]["value"] == "7"
    assert any(edge["rel"] == "gives" and edge["to"] == "item:62649" for edge in edges)

    shana = """
    function event_trade(e)
      if(item_lib.check_turn_in(e.trade, {item1 = 9917, item2 = 9933})) then
        e.other:SummonItem(9938);
      elseif(item_lib.check_turn_in(e.trade, {item1 = 62617})) then
        eq.set_global("ranger_epic","2",5,"F");
      end
    end
    """
    edges = link_script(shana, "Shana.lua", "freportw")
    assert not [edge for edge in edges if edge["rel"] == "sets" and "9917" in edge["from"]]
    notes = [edge for edge in edges if edge["rel"] == "sets" and "62617" in edge["from"]]
    assert notes and notes[0]["value"] == "2"

    treant = """
    function event_say(e)
      if(e.message:findi("hail") and qglobals["ranger_epic"] == "3") then
        e.self:Emote("hands you the wood");
        e.other:SummonItem(62623);
      end
    end
    """
    edges = link_script(treant, "Treant.lua", "jaggedpine")
    assert any(edge["rel"] == "needs" and edge.get("at") == "==3" and edge["from"].endswith("#hail") for edge in edges)
    assert any(edge["rel"] == "gives" and edge["to"] == "item:62623" for edge in edges)

    althele = """
    if ($text=~/hail/i) {
      if($class eq "Ranger" && (plugin::check_hasitem($client, 20488) || plugin::check_hasitem($client, 62600))) {
        if($client->GetGlobal("ranger_epic") ==undef) {
          quest::setglobal("ranger_epic", "1", 5, "F");
        }
      }
    }
    """
    edges = link_script(althele, "Althele.pl", "eastkarana")
    assert any(edge["rel"] == "sets" and edge["value"] == "1" and edge["from"].endswith("#hail") for edge in edges)
    held = [edge for edge in edges if edge["rel"] == "needs" and edge.get("item") in {20488, 62600}]
    assert len(held) == 2 and all(edge.get("op") == "or" for edge in held)
    assert any(edge["rel"] == "needs" and edge.get("at") == "unset" for edge in edges)

    recipes = """
    function event_combine_success(e)
      if (e.recipe_id == 13412) then
        eq.set_global("ranger_epic","3",5,"F");
      elseif (e.recipe_id == 13413) then
        eq.set_global("ranger_epic","5",5,"F");
      end
    end
    """
    edges = link_script(recipes, "global_player.lua", "global")
    values = {edge["from"]: edge["value"] for edge in edges if edge["rel"] == "sets"}
    assert values["global/global player#recipe:13412"] == "3"
    assert values["global/global player#recipe:13413"] == "5"


def test_a_script_under_the_zone_folder_is_part_of_that_zone():
    from eqclient.quests import build_graph

    root = Path("/tmp/eq-graph-nested")
    if root.exists():
        import shutil
        shutil.rmtree(root)
    encounter = root / "dranik" / "encounters"
    encounter.mkdir(parents=True)
    (encounter / "ranger_1_5.lua").write_text(
        """
        function Uisima_Trade(e)
          if(item_lib.check_turn_in(e.trade, {item1 = 62623})) then
            e.other:SummonItem(62626);
          end
        end
        """,
        encoding="utf-8",
    )
    (root / "plugins").mkdir()
    (root / "plugins" / "ignored.lua").write_text(
        'if(item_lib.check_turn_in(e.trade, {item1 = 1})) then e.other:SummonItem(2); end\n',
        encoding="utf-8",
    )
    graph = build_graph(str(root))
    gives = [edge for edge in graph.edges if edge["rel"] == "gives" and edge["to"] == "item:62626"]
    assert gives and gives[0]["from"].startswith("dranik/")
    assert not any(edge["from"].startswith("plugins/") for edge in graph.edges)


def test_coins_held_items_grounds_loot_and_recipes_join_the_graph():
    from eqclient.catalog import Catalog
    from eqclient.quests import build_graph, link_script

    coin = """
    function event_trade(e)
      if(qglobals["paladin_epic"] == "9" and item_lib.check_turn_in(e.trade, {platinum = 500})) then
        e.other:SummonItem(69960);
      end
    end
    """
    edges = link_script(coin, "Ziska.lua", "qeynos2")
    assert any(edge["rel"] == "receives" and edge["to"] == "coin:platinum" and edge["count"] == 500 for edge in edges)
    assert any(edge["rel"] == "gives" and edge["to"] == "item:69960" for edge in edges)
    assert any(edge["rel"] == "needs" and edge.get("at") == "==9" for edge in edges)

    irak = """
    function event_say(e)
      if(e.message:findi("hail")) then
        if(e.other:HasItem(69941) and e.other:HasItem(69952) and e.other:HasItem(69942)) then
          eq.set_global("paladin_epic","6",5,"F");
        elseif(e.other:HasItem(10099) or e.other:HasItem(69913)) then
          eq.set_global("paladin_epic","1",5,"F");
        end
      end
    end
    """
    edges = link_script(irak, "Irak.lua", "hohonora")
    six = [edge for edge in edges if edge["rel"] == "sets" and edge["value"] == "6"]
    one = [edge for edge in edges if edge["rel"] == "sets" and edge["value"] == "1"]
    assert six and "69941" in six[0]["group"] and "69952" in six[0]["group"] and "69942" in six[0]["group"]
    assert "10099" not in six[0]["group"]
    held = [edge for edge in edges if edge["rel"] == "needs" and edge.get("group") == one[0]["group"]]
    assert {edge["item"] for edge in held} == {10099, 69913}
    assert all(edge.get("op") == "or" for edge in held)

    ground = """
    function event_say(e)
      if(e.message:findi("gem")) then
        eq.create_ground_object(69961, 0, 0, 0, 0, 300000);
      end
    end
    """
    edges = link_script(ground, "Arem.lua", "freeportwest")
    assert any(edge["rel"] == "grounds" and edge["to"] == "item:69961" and edge["zone"] == "freeportwest" for edge in edges)

    timer = """
    function event_timer(e)
      if(e.timer == "check_sit") then
        client_to_check:SummonItem(69966);
      end
    end
    """
    edges = link_script(timer, "Lewis.lua", "akanon")
    assert any(edge["rel"] == "gives" and edge["to"] == "item:69966" for edge in edges)

    zone = """
    function event_enter_zone(e)
      if (e.self:HasItem(69941) and e.self:HasItem(69952) and e.self:HasItem(69942) and e.self:HasItem(69983)) then
        eq.unique_spawn(300087,0,0,1,1,1);
      end
    end
    function event_loot(e)
      if(e.item:GetID() == 69971 and qglobals["paladin_epic"] == "6") then
        e.self:Message(15, "Take the sword.");
      end
    end
    """
    edges = link_script(zone, "player.lua", "wallofslaughter")
    enter = [edge for edge in edges if edge["from"].endswith("#enter")]
    assert {edge["item"] for edge in enter if edge["rel"] == "needs"} == {69941, 69952, 69942, 69983}
    assert any(edge["rel"] == "spawns" and edge["to"] == "npc:300087" for edge in enter)
    loot = [edge for edge in edges if edge["from"].endswith("#loot")]
    assert any(edge["rel"] == "needs" and edge["to"] == "item:69971" for edge in loot)
    assert any(edge["rel"] == "needs" and edge.get("at") == "==6" for edge in loot)

    root = Path("/tmp/eq-graph-recipes")
    if root.exists():
        import shutil
        shutil.rmtree(root)
    (root / "global").mkdir(parents=True)
    (root / "global" / "global_player.lua").write_text(
        """
        function event_combine_success(e)
          if (e.recipe_id == 10) then
            eq.set_global("paladin_epic","8",5,"F");
          end
        end
        """,
        encoding="utf-8",
    )
    catalog = Catalog()
    catalog.recipes[10] = {"components": [(1, 1), (2, 1)], "container": 3, "result": 4}
    catalog.recipes[9] = {"components": [], "container": 0, "result": 1}
    catalog.recipes[11] = {"components": [(8, 1)], "container": 0, "result": 9}
    graph = build_graph(str(root), catalog)
    made = [edge for edge in graph.edges if str(edge["from"]).startswith("recipe:")]
    assert any(edge["rel"] == "consumes" and edge["from"] == "recipe:10" and edge["to"] == "item:1" for edge in made)
    assert any(edge["rel"] == "consumes" and edge["from"] == "recipe:10" and edge["to"] == "item:2" for edge in made)
    assert any(edge["rel"] == "container" and edge["from"] == "recipe:10" and edge["to"] == "item:3" for edge in made)
    assert any(edge["rel"] == "produces" and edge["from"] == "recipe:10" and edge["to"] == "item:4" for edge in made)
    assert any(edge["rel"] == "produces" and edge["from"] == "recipe:9" and edge["to"] == "item:1" for edge in made)
    assert not any(edge["from"] == "recipe:11" for edge in made)


def test_a_perl_comment_an_or_gate_a_kill_and_a_spawned_corpse_stay_on_the_step():
    from eqclient.catalog import Catalog
    from eqclient.quests import build_graph, link_script

    muada = """
    sub EVENT_ITEM {
      quest::summonitem(52930); #Elders' Totem Mold
      if ($client->GetGlobal("beast_epic") == 6) {
        if (plugin::check_handin(\\%itemcount, 57009 => 1, 57995 => 1)) {
          quest::setglobal("beast_epic", 7, 5, "F");
        }
      }
      if (plugin::check_handin(\\%itemcount, 52900 => 1)) {
        quest::setglobal("beast_epic", 9, 5, "F");
      }
    }
    """
    edges = link_script(muada, "Muada.pl", "sharvahl")
    seven = [edge for edge in edges if edge["rel"] == "sets" and edge.get("value") == "7"]
    nine = [edge for edge in edges if edge["rel"] == "sets" and edge.get("value") == "9"]
    assert seven and "57009" in seven[0]["from"] and "57995" in seven[0]["from"]
    assert nine and "52900" in nine[0]["from"]
    assert not any(edge["rel"] == "needs" and edge.get("at") == "==6" and "52900" in edge["from"] for edge in edges)

    tavon = """
    function event_say(e)
      if(e.message:findi("hail")) then
        if(e.other:HasItem(5532) or qglobals["cleric15pre"] == "1") then
          if(qglobals["cleric_epic"] == nil) then
            eq.set_global("cleric_epic","1",5,"F");
          end
        end
      end
    end
    """
    edges = link_script(tavon, "Tavon.lua", "nedaria")
    hail = [edge for edge in edges if edge["rel"] == "needs" and edge["from"].endswith("#hail")]
    held = [edge for edge in hail if edge.get("item") == 5532]
    flag = [edge for edge in hail if edge.get("flag") == "cleric15pre"]
    assert held and held[0].get("op") == "or"
    assert flag and flag[0].get("op") == "or" and flag[0].get("at") == "==1"
    assert any(edge["rel"] == "sets" and edge.get("value") == "1" for edge in edges)

    merit = """
    function event_killed_merit(e)
      if (qglobals["cleric20_darkdisciples"] ~= nil and qglobals["cleric20_robedropped"] == nil) then
        local mob = eq.spawn2(eq.ChooseRandom(300072, 300073), 0, 0, 1, 1, 1, 0);
        mob:CastToNPC():AddItem(12433, 1);
        eq.set_global("cleric20_robedropped", "1", 1, "H1");
      end
    end
    """
    edges = link_script(merit, "default.lua", "wallofslaughter")
    kill = [edge for edge in edges if edge["from"].endswith("#kill")]
    assert any(edge["rel"] == "needs" and edge.get("flag") == "cleric20_darkdisciples" and edge.get("at") == "set" for edge in kill)
    assert any(edge["rel"] == "needs" and edge.get("flag") == "cleric20_robedropped" and edge.get("at") == "unset" for edge in kill)
    assert {edge["to"] for edge in kill if edge["rel"] == "spawns"} == {"npc:300072", "npc:300073"}
    assert any(edge["rel"] == "loots" and edge["to"] == "item:12433" for edge in kill)
    assert any(edge["rel"] == "sets" and edge.get("flag") == "cleric20_robedropped" and edge.get("value") == "1" for edge in kill)

    chest = """
    function event_loot(e)
      if (e.item:GetID() == 9954 and qglobals["cleric_epic"] >= "5") then
        eq.set_global("cleric_epic_wakeningchest","1",5,"F");
      end
    end
    """
    edges = link_script(chest, "player.lua", "wakening")
    assert any(edge["rel"] == "sets" and edge.get("flag") == "cleric_epic_wakeningchest" and edge["from"].endswith("#loot") for edge in edges)

    root = Path("/tmp/eq-graph-spawn-loot")
    if root.exists():
        import shutil
        shutil.rmtree(root)
    (root / "lavastorm").mkdir(parents=True)
    (root / "lavastorm" / "Laura.lua").write_text(
        """
        function event_trade(e)
          if(item_lib.check_turn_in(e.trade, {item1 = 56010})) then
            eq.spawn2(27128, 0, 0, 1, 1, 1, 0); -- NPC: High_Priestess_Shima
          end
        end
        """,
        encoding="utf-8",
    )
    catalog = Catalog()
    catalog.npc_drops[27128] = (5768,)
    graph = build_graph(str(root), catalog)
    looted = [edge for edge in graph.edges if edge["rel"] == "loots" and edge["to"] == "item:5768"]
    assert looted and looted[0]["npc"] == 27128 and looted[0]["from"].startswith("lavastorm/")
    assert graph.items[5768]["zones"] == ["lavastorm"]


def test_a_say_keyword_and_a_turn_in_can_spawn_the_next_npc():
    from eqclient.quests import link_script, parse_chain

    madman = """
    function event_say(e)
      if(qglobals["druid_epic"] == "3" and e.message:findi("Geadin")) then
        e.self:Emote("looks down and his features crinkle in concentration.");
      elseif(qglobals["druid_epic"] == "3" and e.message:findi("will do")) then
        eq.set_timer("start",5000);
      end
    end
    function event_timer(e)
      if(e.timer=="start") then
        eq.spawn2(392104,0,0,1,1,1,0); -- NPC: a_haunt
      end
    end
    """
    nodes = parse_chain(madman, "#a_madman.lua", "nro")
    assert [node.word for node in nodes] == ["Geadin", "will do"]
    edges = link_script(madman, "#a_madman.lua", "nro")
    assert any(edge["rel"] == "needs" and edge.get("flag") == "druid_epic" and edge.get("at") == "==3" and edge["from"].endswith("#geadin") for edge in edges)
    spawned = [edge for edge in edges if edge["rel"] == "spawns"]
    assert spawned and spawned[0]["from"].endswith("#will do") and spawned[0]["to"] == "npc:392104" and spawned[0]["name"] == "a haunt"

    ogre = """
    function event_trade(e)
      if(item_lib.check_turn_in(e.trade, {item1 = 1685})) then
        eq.spawn2(107161,0,0,1,1,1,0):AddToHateList(e.other,1); --Trunt
      end
    end
    """
    edges = link_script(ogre, "a_sleeping_ogre.lua", "nurga")
    spawned = [edge for edge in edges if edge["rel"] == "spawns"]
    assert spawned and spawned[0]["to"] == "npc:107161" and spawned[0]["name"] == "Trunt"
    assert "1685" in spawned[0]["from"]

    dalini = """
    sub EVENT_ITEM {
      if (plugin::check_handin(\\%itemcount, 29851 => 1)) {
        quest::unique_spawn(161077,0,0,-372,-95,10,176); # NPC: #Bregun_Dorey
      }
    }
    """
    edges = link_script(dalini, "#Legionnaire_Dalini.pl", "netherbian")
    spawned = [edge for edge in edges if edge["rel"] == "spawns"]
    assert spawned and spawned[0]["to"] == "npc:161077" and spawned[0]["name"] == "Bregun Dorey"
    assert "29851" in spawned[0]["from"]


def test_a_spell_a_forage_and_a_callback_still_create_the_item():
    from eqclient.catalog import catalog_from_lines
    from eqclient.quests import link_script

    spell = ["0"] * 98
    spell[0] = "668"
    spell[1] = "Enchant Electrum"
    spell[20] = "16505"
    spell[86] = "32"
    quoted = ",".join(f"'{field}'" if index == 1 else field for index, field in enumerate(spell))

    def zone_row(short, row_id, number, last=False):
        fields = [f"'{short}'", str(row_id), "''", f"'{short}'"] + ["0"] * 10
        fields[13] = str(number)
        end = ");" if last else "),"
        return "(" + ",".join(fields) + end

    lines = [
        "INSERT INTO `zone` VALUES",
        zone_row("bloodfields", 25, 301),
        zone_row("qey2hh1", 301, 12),
        zone_row("pojustice", 286, 201),
        zone_row("lakerathe", 201, 51, last=True),
        "INSERT INTO `forage` VALUES",
        "(786,301,62601,0,3,-1,-1,NULL,NULL),",
        "INSERT INTO `fishing` VALUES",
        "(135,203,11299,50,100,0,0,-1,-1,NULL,NULL),",
        "INSERT INTO `ground_spawns` VALUES",
        "(1,201,0,0,0,0,0,0,0,0,52934),",
        "(2,89,0,0,0,0,0,0,0,0,11433);",
        "INSERT INTO `spells_new` VALUES",
        f"({quoted}),",
    ]
    catalog = catalog_from_lines(lines)
    assert "lakerathe" in catalog.short_names
    assert catalog.client_zones[201] == "pojustice"
    assert catalog.row_ids[201] == "lakerathe"
    assert "forage:bloodfields" in catalog.sources[62601]
    assert "qey2hh1" not in catalog.sources[62601][0]
    assert "bloodfields" in catalog.zones[62601]
    assert catalog.sources[11299] == ("fishing:zone 203",)
    assert "spell:Enchant Electrum" in catalog.sources[16505]
    assert catalog.zones[52934] == ("pojustice",)
    assert "ground:pojustice" in catalog.sources[52934]
    from eqclient.catalog import audit_zones
    report = audit_zones(catalog, {"lakerathe", "plugins", "missingzone"})
    assert report["quest_without_zone"] == ["missingzone"]
    assert (201, "lakerathe", "pojustice") in report["id_collisions"]
    assert (89, "no zone row") in report["ground_unresolved"]

    handed = """
    sub EVENT_ITEM {
      if (plugin::takeItems(57008 => 1)) {
        if ($client->GetGlobal("beast_epic") == 1) {
          quest::setglobal("beast_epic", "2", 5, "F");
        }
      }
      if ($platinum >= 2000) {
        quest::summonitem(52931);
      }
      if (plugin::check_handin(\\%itemcount, 1 => 1)) {
        $client->SummonItem(10651);
      }
    }
    sub Check5GlobalSerk {
      if ($client->GetGlobal("berserk_epic_ore") == 1) {
        quest::summonitem(15793);
      }
    }
    """
    edges = link_script(handed, "Rahoul.pl", "sharvahl")
    assert any(edge["rel"] == "sets" and edge.get("flag") == "beast_epic" and edge.get("value") == "2" for edge in edges)
    assert any(edge["rel"] == "receives" and edge["to"] == "item:57008" for edge in edges)
    assert any(edge["rel"] == "gives" and edge["to"] == "item:52931" for edge in edges)
    assert any(edge["rel"] == "receives" and edge["to"] == "coin:platinum" and edge.get("count") == 2000 for edge in edges)
    assert any(edge["rel"] == "gives" and edge["to"] == "item:10651" for edge in edges)
    assert any(edge["rel"] == "gives" and edge["to"] == "item:15793" for edge in edges)

    reward = """
    function event_trade(e)
      if(item_lib.check_turn_in(e.trade, {item1 = 1})) then
        e.other:QuestReward(e.self,0,0,0,0,1678,50000);
      end
    end
    """
    edges = link_script(reward, "Sentinel.lua", "emeraldjungle")
    assert any(edge["rel"] == "gives" and edge["to"] == "item:1678" for edge in edges)

    callback = """
    function Protector_Timer(e)
      if(e.timer=="checkaxe") then
        e.self:ForeachHateList(
          function(ent, hate, damage, frenzy)
            if(ent:IsClient()) then
              currclient:SummonItem(17833);
              eq.target_global("berserk_epic", "4", "F", 0, currclient:CharacterID(), 0);
            end
          end
        );
      end
    end
    function event_death_complete(e)
      eq.spawn2(303129,0,0,1,1,1,0);
    end
    """
    edges = link_script(callback, "berserkerepic_1_5.lua", "sebilis")
    assert any(edge["rel"] == "gives" and edge["to"] == "item:17833" for edge in edges)
    assert any(edge["rel"] == "sets" and edge.get("flag") == "berserk_epic" and edge.get("value") == "4" for edge in edges)
    assert any(edge["rel"] == "spawns" and edge["to"] == "npc:303129" for edge in edges)


def test_a_local_spawn_and_a_world_station_are_not_missing_items():
    from eqclient.catalog import catalog_from_lines
    from eqclient.quests import QuestGraph, _add_recipes, link_script

    leech = """
    local dragon_id = 83249
    function event_hp(e)
      eq.spawn2(dragon_id, 0, 0, 1, 1, 1, 0)
    end
    """
    edges = link_script(leech, "a_dire_leech.lua", "swampofnohope")
    assert any(edge["rel"] == "spawns" and edge["to"] == "npc:83249" and edge["from"].endswith("#event_hp") for edge in edges)

    twice = """
    local dragon_id = 1
    local dragon_id = 2
    function event_hp(e)
      eq.spawn2(dragon_id, 0, 0, 1, 1, 1, 0)
    end
    """
    edges = link_script(twice, "a_dire_panda.lua", "stonebrunt")
    assert not any(edge["rel"] == "spawns" for edge in edges)

    griffon = """
    my $dragon_id = 13130;
    sub EVENT_HP {
      quest::spawn2($dragon_id, 0, 0, 1, 1, 1, 0);
    }
    """
    edges = link_script(griffon, "a_dire_griffon.pl", "northkarana")
    assert any(edge["rel"] == "spawns" and edge["to"] == "npc:13130" for edge in edges)

    fields = ["'commons'", "51", "''", "'commons'"] + ["0"] * 10
    fields[13] = "21"
    lines = [
        "INSERT INTO `zone` VALUES",
        "(" + ",".join(fields) + ");",
        "INSERT INTO `object` VALUES",
        "(1,21,0,0,0,0,0,0,0,'IT66',17),",
        "(2,21,0,0,0,0,0,0,0,'IT69',15);",
        "INSERT INTO `items` VALUES",
        "(17762,0,'Planar Fletching Kit',0),",
        "INSERT INTO `tradeskill_recipe_entries` VALUES",
        "(1,9,17,0,0,0,0,1),",
        "(2,9,100,1,0,0,0,0),",
        "(3,9,50,0,0,1,0,0),",
        "(4,10,17762,0,0,0,0,1),",
        "(5,10,101,1,0,0,0,0);",
    ]
    catalog = catalog_from_lines(lines)
    assert catalog.world_containers[17]["name"] == "Forge"
    assert catalog.world_containers[17]["zones"] == ("commons",)
    assert catalog.world_containers[15]["name"] == "Oven"
    graph = QuestGraph()
    graph.edges.append({"kind": "edge", "rel": "sets", "from": "global/x#recipe:9", "to": "flag:x", "flag": "x", "value": "1"})
    graph.edges.append({"kind": "edge", "rel": "sets", "from": "global/x#recipe:10", "to": "flag:x", "flag": "x", "value": "1"})
    _add_recipes(graph, catalog, set())
    assert any(edge["rel"] == "container" and edge["to"] == "world:17" and edge["from"] == "recipe:9" for edge in graph.edges)
    assert any(edge["rel"] == "container" and edge["to"] == "item:17762" for edge in graph.edges)
    assert not any(edge.get("to") == "item:17" for edge in graph.edges)
    assert 17 not in graph.items


def test_dump_loot_and_ground_name_the_npc_or_zone():
    from eqclient.catalog import catalog_from_lines
    from eqclient.quests import link_script

    def zone_row(short, row_id, number, last=False):
        fields = [f"'{short}'", str(row_id), "''", f"'{short}'"] + ["0"] * 10
        fields[13] = str(number)
        end = ");" if last else "),"
        return "(" + ",".join(fields) + end

    def npc_row(npc_id, name, loottable, last=False):
        fields = [str(npc_id), f"'{name}'"] + ["0"] * 20
        fields[17] = str(loottable)
        fields[18] = "0"
        end = ");" if last else "),"
        return "(" + ",".join(fields) + end

    lines = [
        "INSERT INTO `zone` VALUES",
        zone_row("ponightmare", 1, 221),
        zone_row("dranik", 2, 336, last=True),
        "INSERT INTO `npc_types` VALUES",
        npc_row(204053, "Hobgoblin_Horrorfiend", 101578, last=True),
        "INSERT INTO `loottable_entries` VALUES",
        "(101578,142752,1,1,1,100),",
        "INSERT INTO `lootdrop_entries` VALUES",
        "(142752,11474,1,0,96.296,0,0,0,1,0,0),",
        "INSERT INTO `spawnentry` VALUES",
        "(9001,204053,100),",
        "INSERT INTO `spawn2` VALUES",
        "(1,9001,'ponightmare',0,0,0,0,0,0,0,0,0,0,1,0,-1,-1,NULL,NULL),",
        "INSERT INTO `ground_spawns` VALUES",
        "(1713,336,0,0,0,0,0,0,0,'IT',11576,1,'Default',7200,-1,-1,NULL,NULL);",
    ]
    catalog = catalog_from_lines(lines)
    assert "loot:Hobgoblin Horrorfiend@ponightmare" in catalog.sources[11474]
    assert "ground:dranik" in catalog.sources[11576]
    assert catalog.zones[11474] == ("ponightmare",)
    assert catalog.zones[11576] == ("dranik",)

    trap = """
    sub EVENT_ENTER {
      quest::spawn2(quest::ChooseRandom(171051,171063),0,0,1,1,1,0);
    }
    """
    edges = link_script(trap, "a_creature.pl", "thegrey")
    assert {edge.get("npc") for edge in edges if edge["rel"] == "spawns"} == {171051, 171063}


def test_trap_npc_zones_from_quest_scripts(tmp_path):
    from eqclient.catalog import _sources, _trap_npc_zones

    grey = tmp_path / "thegrey"
    grey.mkdir()
    (grey / "a_creature.pl").write_text(
        "sub EVENT_ENTER {\n"
        "  quest::spawn2(quest::ChooseRandom(171051,171063,171064,171069),0,0,1,1,1,0);\n"
        "}\n"
    )
    feer = tmp_path / "feerrott"
    feer.mkdir()
    (feer / "#druid_epic_trap.pl").write_text(
        "sub EVENT_ENTER { quest::spawn2(47208,0,0,1,1,1,0); }\n"
    )
    zones = _trap_npc_zones(tmp_path)
    assert zones[171051] == ("thegrey",)
    assert zones[171069] == ("thegrey",)
    assert zones[47208] == ("feerrott",)

    sources = _sources(
        {},
        {},
        {},
        {},
        None,
        {171051: (9052,), 47208: (62818,)},
        {171051: "a stone beast", 47208: "Swamp Terror"},
        {},
        {},
        zones,
    )
    assert "loot:a stone beast@thegrey" in sources[9052]
    assert "loot:Swamp Terror@feerrott" in sources[62818]


def test_a_combine_can_return_two_items_and_names_its_skill():
    from eqclient.catalog import catalog_from_lines
    from eqclient.quests import QuestGraph, _add_recipes

    lines = [
        "INSERT INTO `items` VALUES",
        "(66175,0,'Hilt',0),",
        "(66176,0,'Blade of Tactics',0),",
        "(66177,0,'Blade of Strategy',0),",
        "(17869,0,'Augment Distiller',0);",
        "INSERT INTO `tradeskill_recipe` VALUES",
        "(10347,'Blade Of Tactics And Strategy (aug)',69,0,0,1,0,'Warrior Epic 1.0 (Aug) - Split',0,0,0,1,-1,-1,NULL,NULL),",
        "(200,'Hardened Edge',63,200,252,0,0,NULL,1,0,0,1,-1,-1,NULL,NULL),",
        "(201,'Disabled Edge',63,200,252,0,0,NULL,0,0,0,0,-1,-1,NULL,NULL);",
        "INSERT INTO `tradeskill_recipe_entries` VALUES",
        "(78004,10347,66175,0,0,1,1,0),",
        "(78005,10347,66176,1,0,0,0,0),",
        "(78006,10347,66177,1,0,0,0,0),",
        "(78007,10347,17869,0,0,0,0,1),",
        "(1,200,66176,0,0,1,1,0),",
        "(2,200,50,1,0,0,0,0),",
        "(3,201,66176,0,0,1,1,0),",
        "(4,201,51,1,0,0,0,0);",
    ]
    catalog = catalog_from_lines(lines)
    made = catalog.recipes[10347]
    assert made["results"] == [(66176, 1), (66177, 1)]
    assert made["components"] == [(66175, 1)]
    assert made["container"] == 17869
    assert made["skill_name"] == "Pottery"
    assert made["nofail"] == 1
    assert catalog.recipes[200]["skillneeded"] == 200
    assert catalog.recipes[200]["trivial"] == 252
    assert catalog.recipes[200]["must_learn"] == 1
    graph = QuestGraph()
    graph.edges.append({"kind": "edge", "rel": "needs", "from": "qeynos/a#hail", "to": "item:66176", "item": 66176})
    graph.edges.append({"kind": "edge", "rel": "sets", "from": "global/x#recipe:200", "to": "flag:x", "flag": "x", "value": "1"})
    graph.edges.append({"kind": "edge", "rel": "sets", "from": "global/x#recipe:201", "to": "flag:x", "flag": "x", "value": "1"})
    _add_recipes(graph, catalog, {66176})
    produced = [edge for edge in graph.edges if edge["rel"] == "produces" and edge["from"] == "recipe:10347"]
    assert {edge["to"] for edge in produced} == {"item:66176", "item:66177"}
    assert produced[0]["skill_name"] == "Pottery" and produced[0]["trivial"] == 0 and produced[0]["nofail"] == 1
    hard = [edge for edge in graph.edges if edge["rel"] == "produces" and edge["from"] == "recipe:200"]
    assert hard and hard[0]["skillneeded"] == 200 and hard[0]["trivial"] == 252 and hard[0]["skill_name"] == "Blacksmithing"
    assert not any(edge.get("from") == "recipe:201" for edge in graph.edges)


def test_a_combine_keeps_its_own_gives_and_spawns_in_script_order():
    from eqclient.quests import link_script

    text = """
    function event_combine_success(e)
      if (e.recipe_id == 13412) then
        eq.set_global("ranger_epic","3",5,"F");
        if (eq.get_zone_short_name()=="jaggedpine") then
          eq.spawn2(181222, 0, 0, 1, 1, 1, 0); -- NPC: Red_Dogwood_Treant
        else
          e.self:SummonItem(72091);
        end
      elseif (e.recipe_id == 19460) then
        e.self:SummonItem(67704);
        eq.set_global("cleric_epic","7",5,"F");
      end
    end
    """
    edges = link_script(text, "global_player.lua", "global")
    ranger = [edge for edge in edges if edge.get("flag") == "ranger_epic" and edge.get("value") == "3"]
    assert len(ranger) == 1
    assert ranger[0]["from"].endswith("#recipe:13412")
    group = ranger[0]["group"]
    ordered = sorted(
        (edge.get("order"), edge.get("rel"), edge.get("to"))
        for edge in edges
        if edge.get("group") == group and edge.get("rel") in {"sets", "gives", "spawns"}
    )
    assert [item[1:] for item in ordered] == [
        ("sets", "flag:ranger_epic"),
        ("spawns", "npc:181222"),
        ("gives", "item:72091"),
    ]
    assert ordered[0][0] < ordered[1][0] < ordered[2][0]
    cleric = [edge for edge in edges if edge.get("group", "").endswith("#recipe:19460")]
    assert {edge.get("to") for edge in cleric} == {"item:67704", "flag:cleric_epic"}
    assert not any(edge.get("to") == "item:67704" and edge.get("group") == group for edge in edges)


def test_a_timer_can_summon_through_a_client_lookup_and_add_loot_to_a_spawn():
    from eqclient.quests import link_script

    perl = """
    sub EVENT_TIMER {
      if ($timer eq "giveitem") {
        $entity_list->GetClientByName("$questclient")->SummonItem(62828); #Animating Heads
      }
    }
    """
    edges = link_script(perl, "38016.pl", "tox")
    assert any(
        edge["rel"] == "gives" and edge["to"] == "item:62828" and edge.get("group", "").endswith("#event_timer")
        for edge in edges
    )

    lua = """
    function King_Timer(e)
      if (e.timer == "spawn_hiders") then
        eq.spawn2(92202, 0, 0, 1, 1, 1, 0); -- NPC: Goblin_Hider
        local npc_list = eq.get_entity_list():GetNPCList();
        for npc in npc_list.entries do
          if (npc.valid and npc:GetNPCTypeID() == 92202) then
            npc:AddItem(62826, 1);
            break;
          end
        end
      end
    end
    """
    edges = link_script(lua, "druid_1_5.lua", "frontiermtns")
    assert any(edge["rel"] == "spawns" and edge["to"] == "npc:92202" for edge in edges)
    assert any(
        edge["rel"] == "loots" and edge["to"] == "item:62826" and edge.get("npc") == 92202
        for edge in edges
    )


def test_event_loot_getid_is_a_gate_and_numeric_npc_files_take_dump_names():
    from eqclient.catalog import Catalog
    from eqclient.quests import link_script

    loot_gate = """
    function event_loot(e)
      if(e.self:Class() == "Ranger" and e.item:GetID() == 76999) then
        eq.set_global("rng_wos_chest","1",5,"F");
      end
    end
    function event_enter_zone(e)
      if(qglobals["ranger_epic"] == "8") then
        eq.unique_spawn(300057,0,0,1,1,1,0); --#Herrian_Warfrost
      end
    end
    """
    edges = link_script(loot_gate, "player.lua", "wallofslaughter")
    assert any(edge["rel"] == "needs" and edge["to"] == "item:76999" and edge["from"].endswith("#loot") for edge in edges)
    assert not any(edge["rel"] == "loots" and edge["to"] == "item:76999" and "player#loot" in str(edge.get("from")) for edge in edges)
    assert any(edge["rel"] == "spawns" and edge.get("npc") == 300057 for edge in edges)

    catalog = Catalog()
    catalog.npc_names[90005] = "a black reaver"
    edges = link_script(
        """
        function event_death_complete(e)
          eq.spawn2(90005, 0, 0, 1, 1, 1, 0)
        end
        """,
        "90005.lua",
        "citymist",
        catalog,
    )
    assert any(edge["from"].startswith("citymist/a black reaver") for edge in edges)

    encounter = """
    function Uisima_Trade(e)
      if(item_lib.check_turn_in(e.trade, {item1 = 62623})) then
        e.other:SummonItem(62626);
      end
    end
    """
    edges = link_script(encounter, "ranger_1_5.lua", "dranik")
    assert any(edge["rel"] == "gives" and edge["to"] == "item:62626" and "hand:62623" in str(edge.get("group")) for edge in edges)
    assert not any(edge["rel"] == "gives" and edge["to"] == "item:62626" and "uisima_trade" in str(edge.get("group") or "").lower() for edge in edges)


def test_a_quoted_summon_a_lua_handin_spawn_and_a_deferred_trade_reward():
    from eqclient.quests import link_script

    perl = """
    sub EVENT_ITEM {
      if (plugin::check_handin(\\%itemcount, 20696 => 1)) {
        quest::summonitem("20699");
      }
    }
    """
    edges = link_script(perl, "Nekexin_Virulence.pl", "overthere")
    assert any(edge["rel"] == "gives" and edge["to"] == "item:20699" for edge in edges)

    lua_spawn = """
    function event_trade(e)
      if (eq.handin({[28051] = 1})) then
        eq.spawn2(80042,0,0,1,1,1,0):AddToHateList(e.other,1); -- NPC: a_plasmatic_priest
      end
    end
    """
    edges = link_script(lua_spawn, "80002.lua", "soltemple")
    assert any(edge["rel"] == "receives" and edge["to"] == "item:28051" for edge in edges)
    assert any(edge["rel"] == "spawns" and edge["to"] == "npc:80042" for edge in edges)

    deferred = """
    function event_trade(e)
      local morechampagne = 0;
      if(item_lib.check_turn_in(e.trade, {item1 = 13829,item2 = 13829,item3 = 13829,item4 = 13829})) then
        morechampagne = 1;
      elseif(item_lib.check_turn_in(e.trade, {item1 = 13829})) then
        morechampagne = 0;
      end
      if(morechampagne == 1) then
        e.other:SummonItem(12196);
        morechampagne = 0;
      end
    end
    """
    edges = link_script(deferred, "Tykar_Renlin.lua", "freeporteast")
    four = [
        edge
        for edge in edges
        if edge["rel"] == "gives"
        and edge["to"] == "item:12196"
        and "13829+13829+13829+13829" in str(edge.get("group") or "")
    ]
    one = [
        edge
        for edge in edges
        if edge["rel"] == "gives"
        and edge["to"] == "item:12196"
        and str(edge.get("group") or "").endswith("#hand:13829")
    ]
    assert four and not one


def test_the_journal_keeps_a_hub_a_flag_and_a_corpse():
    journal = Journal(":memory:")
    journal.record("Mockone", "poknowledge", "a cleric", "hub", "hail")
    journal.record("Mockone", "", "", "flag", "clericflag")
    journal.remember_corpse("Mockone", "qeynos", 1.0, 2.0, 3.0)
    assert journal.hubs("Mockone", "poknowledge") == {"a cleric"}
    assert "clericflag" in journal.flags("Mockone")
    assert journal.corpse("Mockone")[0] == "qeynos"
    journal.close()


def test_journal_tracks_each_death_until_collected():
    """Outstanding corpses == deaths − collections (FIFO reclaim)."""
    journal = Journal(":memory:")
    journal.remember_corpse("Mockone", "ecommons", 10.0, 20.0, 1.0)
    journal.remember_corpse("Mockone", "ecommons", 100.0, 200.0, 2.0)
    journal.remember_corpse("Mockone", "qeynos", 5.0, 5.0, 0.0)
    assert journal.outstanding_corpses("Mockone") == 3
    oldest = journal.corpse("Mockone")
    assert oldest is not None and oldest[0] == "ecommons" and oldest[1] == 10.0
    left = journal.collect_corpse("Mockone", "ecommons", 100.0, 200.0, 2.0)
    assert left == 2
    # Nearest match removed the second ecommons death; oldest is now the first.
    assert journal.corpse("Mockone")[1] == 10.0
    left = journal.collect_corpse("Mockone")
    assert left == 1
    assert journal.corpse("Mockone")[0] == "qeynos"
    assert journal.collect_corpse("Mockone") == 0
    assert journal.corpse("Mockone") is None
    journal.close()


def _goal(item_id: int, **items) -> tuple[QuestGraph, Campaign]:
    graph = QuestGraph()
    graph.items[item_id] = {"name": "goal", "sources": []}
    for other, info in items.items():
        graph.items[other] = info
    camp = Campaign(class_id=1, race_id=1)
    camp.stack = [item_id]
    camp.counts = {item_id: 1}
    return graph, camp


def test_a_blocked_layer_is_set_aside_and_the_root_keeps_going():
    graph, camp = _goal(1)
    graph.items[1] = {"name": "epic", "sources": ["loot:a orc@qeynos"]}
    graph.items[9993] = {"name": "scroll", "sources": []}
    camp.stack = [1, 9993]
    camp.counts = {1: 1, 9993: 1}
    step = camp.next_step(graph, {}, {}, level=10, here="qeynos")
    assert 9993 not in camp.stack and 9993 in camp.skipped
    assert step.kind in {"kill", "loot"}
    assert camp.assign_goal(9993) is False
    stuck, lone = _goal(9993)
    stuck.items[9993] = {"name": "scroll", "sources": []}
    blocked = lone.next_step(stuck, {}, {}, level=10, here="qeynos")
    assert blocked.kind == "blocked" and lone.stack == [9993]


def test_a_level_gate_fights_at_the_camp():
    graph, camp = _goal(50)
    graph.items[50] = {"name": "bit", "sources": ["loot:a gnoll@unrest"]}
    world = _world()
    world.zone = "tutorialb"
    world.level = 1
    world.spawns[7] = Spawn(7, "a rat", 1, 1, 1, 4.0, -140.0, 19.0, 1, 1)
    world.faction[7] = 8
    intent = guide(world, TaskBook(), ZoneQuests("tutorialb"), Inventory(), True, graph=graph, campaign=camp)
    assert intent is not None and intent.kind == "fight" and intent.target == 7


def test_a_hand_in_lists_every_item_and_a_hail_keeps_its_word():
    graph = QuestGraph()
    group = "thurgadina/Dardek_Bladewright#Hail"
    graph.items[60292] = {"name": "hilt", "sources": []}
    graph.edges = [
        {"kind": "edge", "rel": "gives", "from": group, "to": "item:60292", "group": group},
        {"kind": "edge", "rel": "receives", "from": group, "to": "item:60285", "group": group},
        {"kind": "edge", "rel": "receives", "from": group, "to": "item:60286", "group": group},
        {"kind": "edge", "rel": "receives", "from": group, "to": "item:60288", "group": group},
    ]
    camp = Campaign(class_id=1)
    camp.stack = [60292]
    camp.counts = {60292: 1}
    held = Inventory()
    for slot, item_id in ((22, 60285), (23, 60286), (24, 60288)):
        held.slots[slot] = Held(item_id, slot, 1, str(item_id), "")
    world = _world()
    world.zone = "thurgadina"
    world.level = 60
    world.spawns[9] = Spawn(9, "Dardek Bladewright", 1, 60, 1, 3.0, -140.0, 19.0, 1, 1)
    intent = guide(world, TaskBook(), ZoneQuests("thurgadina"), held, True, graph=graph, campaign=camp)
    assert intent is not None and intent.kind == "hand_in"
    assert _turn_ids(intent.text, intent.item_id) == [60285, 60286, 60288]
    word = QuestGraph()
    hail = "thurgadina/Korbuk_Brimblade#work"
    word.items[1] = {"name": "epic", "sources": []}
    word.edges = [{"kind": "edge", "rel": "gives", "from": hail, "to": "item:1", "group": hail}]
    spoken = Campaign(class_id=1)
    spoken.stack = [1]
    spoken.counts = {1: 1}
    world.spawns[10] = Spawn(10, "Korbuk Brimblade", 1, 60, 1, 5.0, -140.0, 19.0, 1, 1)
    hail_intent = guide(world, TaskBook(), ZoneQuests("thurgadina"), Inventory(), True, graph=word, campaign=spoken)
    assert hail_intent is not None and hail_intent.kind == "task_talk" and hail_intent.text == "work"


def test_a_ground_spawn_is_clicked_and_a_boss_is_fought():
    graph, camp = _goal(70)
    graph.items[70] = {"name": "shard", "sources": ["ground:qeynos"]}
    world = _world()
    world.zone = "qeynos"
    world.level = 20
    world.ground[3] = Ground(3, "a glowing shard", 6.0, -140.0, 19.0)
    intent = guide(world, TaskBook(), ZoneQuests("qeynos"), Inventory(), True, graph=graph, campaign=camp)
    assert intent is not None and intent.kind == "fetch" and intent.target == 3
    raid = QuestGraph()
    raid.items[60285] = {"name": "head", "sources": []}
    raid.edges = [{"kind": "edge", "rel": "boss", "from": "potactics/Diaku_Overseer", "to": "item:60285"}]
    hunting = Campaign(class_id=1)
    hunting.stack = [60285]
    hunting.counts = {60285: 1}
    world.zone = "potactics"
    world.spawns[11] = Spawn(11, "Diaku Overseer", 1, 60, 1, 8.0, -140.0, 19.0, 1, 1)
    kill = guide(world, TaskBook(), ZoneQuests("potactics"), Inventory(), True, graph=raid, campaign=hunting)
    assert kill is not None and kill.kind == "task_kill" and kill.target == 11


def test_a_key_clicks_its_door_and_an_instance_uses_the_zone_door():
    graph = QuestGraph()
    graph.items[50] = {"name": "key", "sources": []}
    graph.edges = [{"kind": "edge", "rel": "key", "from": "qeynos", "to": "item:50", "zone": "qeynos", "door": 4}]
    camp = Campaign(class_id=1)
    camp.stack = [50]
    camp.counts = {50: 1}
    world = _world()
    world.zone = "qeynos"
    world.level = 20
    world.doors[4] = Door(4, "a locked gate", 6.0, -140.0, 19.0, 0)
    intent = guide(world, TaskBook(), ZoneQuests("qeynos"), Inventory(), True, graph=graph, campaign=camp)
    assert intent is not None and intent.kind == "pick_lock" and intent.target == 4
    inst = QuestGraph()
    inst.items[80] = {"name": "raid", "sources": []}
    inst.edges = [{"kind": "edge", "rel": "instance", "from": "potactics/a_keeper", "to": "item:80"}]
    camp.stack = [80]
    camp.counts = {80: 1}
    world.zone = "potactics"
    world.doors[8] = Door(8, "potactics", 9.0, -140.0, 19.0, 0)
    entered = guide(world, TaskBook(), ZoneQuests("potactics"), Inventory(), True, graph=inst, campaign=camp)
    assert entered is not None and entered.kind == "leave" and entered.target == 8


def test_practice_goods_are_sold_to_a_merchant_and_a_forge_is_a_station():
    graph, camp = _goal(99)
    camp.sell_after.add(99)
    held = Inventory()
    held.slots[22] = Held(99, 22, 1, "practice", "")
    world = _world()
    world.zone = "qeynos"
    world.level = 10
    world.spawns[12] = Spawn(12, "a merchant", 1, 20, 1, 4.0, -140.0, 19.0, 1, 1)
    intent = guide(world, TaskBook(), ZoneQuests("qeynos"), held, True, graph=graph, campaign=camp)
    assert intent is not None and intent.kind == "shop" and intent.text == "sell" and intent.item_id == 99
    forge = Door(1, "a forge", 1.0, 1.0, 0.0, 0)
    picked = pick_station(17, [forge], [], (0.0, 0.0, 0.0))
    assert picked is not None and picked[0] == "door" and picked[1].name == "a forge"
