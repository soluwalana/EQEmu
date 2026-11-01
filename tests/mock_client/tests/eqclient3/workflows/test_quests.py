"""expand, produce, and assign. These do not open a socket."""

from __future__ import annotations

from types import SimpleNamespace

from eqclient3.actions.quest_talk import (
    ExpectFaction,
    ExpectItem,
    ExpectMoney,
    Faction,
    Hand,
    Money,
    Need,
    Receive,
    Say,
)
from eqclient3.inventory.assign import assign
from eqclient3.quests.expand import conversation, expand, produced
from eqclient3.quests.graph import QuestGraph
from eqclient3.quests.produce import produce
from eqclient3.schedule import Schedule


def _graph() -> QuestGraph:
    graph = QuestGraph()
    graph.edges = [
        {
            "rel": "gives",
            "from": "erudnext/brianna falsruinay",
            "to": "item:100",
            "group": "erudnext/brianna falsruinay#hand:9",
        },
        {
            "rel": "receives",
            "from": "erudnext/brianna falsruinay",
            "to": "item:9",
            "group": "erudnext/brianna falsruinay#hand:9",
            "count": 1,
        },
        {"rel": "loots", "from": "qeynos/a rat", "to": "item:9", "zone": "qeynos"},
        {
            "rel": "gives",
            "from": "qeynos/a guard",
            "to": "item:8",
            "group": "qeynos/a guard#hand:7",
        },
        {
            "rel": "receives",
            "from": "qeynos/a guard",
            "to": "item:7",
            "group": "qeynos/a guard#hand:7",
            "count": 1,
        },
    ]
    graph.index()
    return graph


def test_expand_zones_then_fetches_then_hands_the_item():
    actions = expand(_graph().gives(100), here="freportw", graph=_graph())
    names = [type(action).__name__ for action in actions]
    assert names == ["Travel", "Fetch", "Zone", "QuestTalk"]
    travel, fetch, zone, talk = actions
    assert travel.destination == "qeynos"
    assert fetch.item_id == 9
    assert zone.destination == "erudnext"
    assert talk.steps == (Need(9), Hand(9), Receive(100))
    assert talk.expect == ExpectItem(100)


def test_expand_a_hand_in_only_component_is_the_giver_chain():
    graph = _graph()
    graph.edges.append(
        {
            "rel": "gives",
            "from": "erudnext/brianna falsruinay",
            "to": "item:200",
            "group": "erudnext/brianna falsruinay#hand:8",
        }
    )
    graph.edges.append(
        {
            "rel": "receives",
            "from": "erudnext/brianna falsruinay",
            "to": "item:8",
            "group": "erudnext/brianna falsruinay#hand:8",
            "count": 1,
        }
    )
    graph.index()
    actions = expand(graph.gives(200), here="erudnext", graph=graph)
    names = [type(action).__name__ for action in actions]
    assert names == ["Zone", "QuestTalk", "QuestTalk"]
    assert actions[0].destination == "qeynos"
    assert actions[1].steps == (Need(7), Hand(7), Receive(8))
    assert actions[1].expect == ExpectItem(8)
    assert actions[2].steps == (Need(8), Hand(8), Receive(200))
    assert actions[2].expect == ExpectItem(200)


def test_expand_a_say_word_is_a_quest_talk():
    graph = QuestGraph()
    graph.edges = [
        {
            "rel": "gives",
            "from": "freeporteast/kargek redblade",
            "to": "item:20673",
            "group": "freeporteast/kargek redblade#favor",
        }
    ]
    graph.index()
    actions = expand(graph.gives(20673), here="qeynos", graph=graph)
    names = [type(action).__name__ for action in actions]
    assert names == ["Zone", "QuestTalk"]
    talk = actions[1]
    assert talk.npc == "kargek redblade"
    assert talk.steps == (Say("favor"), Receive(20673))
    assert talk.expect == ExpectItem(20673)
    assert talk.priority == 280
    assert talk.source == "quest:freeporteast/kargek redblade#say:kargek redblade:favor"


def test_conversation_follows_then_until_the_flag_gate():
    graph = QuestGraph()
    home = "draniksscar/korbuk brimblade"
    graph.edges = [
        {"rel": "sets", "from": f"{home}#work", "to": "flag:warrior_pre", "flag": "warrior_pre", "value": "1"},
        {"rel": "then", "from": f"{home}#work", "to": f"{home}#errands"},
        {"rel": "needs", "from": f"{home}#errands", "to": "flag:warrior_pre", "flag": "warrior_pre", "at": "==1"},
        {"rel": "then", "from": f"{home}#errands", "to": f"{home}#plans"},
        {"rel": "needs", "from": f"{home}#plans", "to": "flag:warrior_pre", "flag": "warrior_pre", "at": "==1"},
        {"rel": "then", "from": f"{home}#plans", "to": f"{home}#shank"},
        {"rel": "needs", "from": f"{home}#shank", "to": "flag:warrior_pre", "flag": "warrior_pre", "at": "==2"},
    ]
    steps, done = conversation(graph, f"{home}#work", 0)
    assert steps == (Say("work"), Say("errands"), Say("plans"))
    assert done is None


def test_conversation_stops_when_the_say_gives_the_item():
    graph = QuestGraph()
    home = "freeporteast/kargek redblade"
    graph.edges = [
        {"rel": "gives", "from": home, "to": "item:20673", "group": f"{home}#favor"},
        {"rel": "then", "from": f"{home}#favor", "to": f"{home}#sent me to help"},
        {"rel": "then", "from": f"{home}#sent me to help", "to": f"{home}#sword"},
    ]
    steps, done = conversation(graph, f"{home}#favor", 20673)
    assert steps == (Say("favor"), Receive(20673))
    assert done == ExpectItem(20673)


def test_conversation_with_no_item_expects_the_faction_it_raises():
    graph = QuestGraph()
    home = "abysmal/pandula bubundu#hand:52179"
    graph.edges = [
        {"rel": "sets", "from": home, "to": "faction:1770", "faction": "1770", "value": 10, "group": home},
        {"rel": "sets", "from": home, "to": "faction:1771", "faction": "1771", "value": -10, "group": home},
    ]
    steps, done = conversation(graph, home, 0)
    assert steps == (Need(52179), Hand(52179), Faction(1770, 10), Faction(1771, -10))
    assert done == ExpectFaction(1770, 10)


def test_conversation_expects_the_coin_it_pays():
    graph = QuestGraph()
    home = "qeynos/a guard#hail"
    graph.edges = [
        {"rel": "gives", "from": "qeynos/a guard", "to": "coin:platinum", "count": 5, "group": home},
    ]
    steps, done = conversation(graph, home, 0)
    assert steps == (Say("hail"), Money(5))
    assert done == ExpectMoney(5)


def test_expand_a_produced_item_fetches_then_zones_then_crafts():
    graph = QuestGraph()
    graph.world[17] = {"name": "Forge", "zones": ["freportw"]}
    graph.edges = [
        {
            "rel": "produces",
            "from": "recipe:9",
            "to": "item:8",
            "count": 1,
            "skill": 60,
            "trivial": 15,
            "skill_name": "Blacksmithing",
        },
        {"rel": "consumes", "from": "recipe:9", "to": "item:7", "count": 2},
        {"rel": "container", "from": "recipe:9", "to": "world:17"},
        {"rel": "loots", "from": "qeynos/a rat", "to": "item:7", "zone": "qeynos"},
        {"rel": "produces", "from": "recipe:2", "to": "item:8"},
        {"rel": "consumes", "from": "recipe:2", "to": "item:8", "count": 1},
    ]
    graph.index()
    edge = produced(graph, 8)
    assert edge is not None
    assert edge["from"] == "recipe:9"
    actions = expand(edge, here="qeynos", graph=graph)
    names = [type(action).__name__ for action in actions]
    assert names == ["Fetch", "Zone", "Craft"]
    fetch, zone, made = actions
    assert fetch.item_id == 7
    assert fetch.count == 2
    assert zone.destination == "freportw"
    assert made.recipe.id == 9
    assert made.recipe.result == 8
    assert made.recipe.components == ((7, 2),)
    assert made.recipe.container == 17
    assert made.recipe.skill == 60
    assert made.recipe.name == "Blacksmithing"
    assert made.source == "recipe:9#craft:9"


def test_produce_appends_a_craft_for_a_recipe_goal():
    graph = QuestGraph()
    graph.edges = [
        {"rel": "produces", "from": "recipe:9", "to": "item:8", "count": 1},
        {"rel": "consumes", "from": "recipe:9", "to": "item:7", "count": 1},
        {"rel": "loots", "from": "qeynos/a rat", "to": "item:7", "zone": "qeynos"},
    ]
    graph.index()
    world = SimpleNamespace(zone="qeynos", class_id=1, race=1, level=1, bags={}, name="Mockone")
    queue = Schedule()
    loop = SimpleNamespace(queue=queue, character="Mockone", current=None)
    produce(loop, world, item_id=8, graph=graph)
    actions = list(queue)
    names = [type(action).__name__ for action in actions]
    assert names == ["Fetch", "Craft"]
    assert actions[0].item_id == 7
    made = actions[-1]
    assert made.recipe.id == 9
    assert made.recipe.components == ((7, 1),)
    assert made.source == "goal:item=8#craft:9"


def test_produce_waits_while_tutorial_readtasks_is_open():
    class ReadTasks:
        source = "read_tasks:tutorialb"
        complete = False

    queue = [ReadTasks()]
    loop = SimpleNamespace(queue=queue, character="Mockone")
    world = SimpleNamespace(zone="tutorialb", class_id=1, level=1, bags={}, name="Mockone")
    produce(loop, world, leaving_tutorial=True, graph=QuestGraph())
    assert list(loop.queue) == queue


def test_produce_appends_kit_kill_and_camp_and_skips_a_resolved_source(tmp_path):
    from eqclient3.journal import Journal

    journal = Journal(tmp_path / "journal-v3.sqlite")
    world = SimpleNamespace(
        zone="qeynos",
        class_id=1,
        race=1,
        level=1,
        bags={},
        cursor=None,
        name="Mockone",
        bots=SimpleNamespace(roster=()),
    )
    queue = Schedule()
    loop = SimpleNamespace(queue=queue, character="Mockone")
    done = SimpleNamespace(source="gear:5013", zone="qeynos", priority=0, durable=True)
    journal.resolve_action("Mockone", done)
    produce(loop, world, journal, leaving_tutorial=True, graph=QuestGraph())
    sources = [action.source for action in queue]
    assert "gear:5013" not in sources
    assert any(source.startswith("gear:") for source in sources)
    assert "kill:after_tutorial" in sources
    assert any(source.startswith("level:") for source in sources)


def test_assign_skips_an_empty_pulse_and_sells_a_leftover():
    world = SimpleNamespace(
        zone="qeynos",
        class_id=1,
        race=1,
        level=1,
        bags={22: SimpleNamespace(item_id=4242, slots=0, classes=65535, races=65535, nodrop=255)},
        cursor=None,
        name="Mockone",
        bots=SimpleNamespace(roster=()),
        quest_items=(),
    )
    queue = Schedule()
    loop = SimpleNamespace(queue=queue, character="Mockone")
    assign(loop, world, applied=False)
    assert list(queue) == []
    assign(loop, world, applied=True)
    assert [type(action).__name__ for action in queue] == ["Sell"]
    assert queue.head().item_ids == [4242]


def test_assign_keeps_a_quest_item_and_upgrades_the_player_without_a_distribute():
    loose = SimpleNamespace(item_id=50, slots=1 << 4, classes=65535, races=65535, nodrop=255, ac=8)
    quest = SimpleNamespace(item_id=77, slots=0, classes=65535, races=65535, nodrop=255)
    world = SimpleNamespace(
        zone="qeynos",
        class_id=1,
        race=1,
        level=10,
        bags={4: 0, 22: loose, 23: quest},
        cursor=None,
        name="Mockone",
        bots=SimpleNamespace(roster=(("helper", 1, 10),)),
        quest_items={77},
    )
    queue = Schedule()
    loop = SimpleNamespace(queue=queue, character="Mockone")
    assign(loop, world)
    names = [type(action).__name__ for action in queue]
    assert "Sell" not in names
    assert "Distribute" not in names
