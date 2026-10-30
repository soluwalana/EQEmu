"""expand, produce, and assign. These do not open a socket."""

from __future__ import annotations

from types import SimpleNamespace

from eqclient3.inventory.assign import assign
from eqclient3.quests.expand import expand, produced
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


def test_expand_zones_then_hails_then_delivers_and_a_drop_is_a_fetch():
    actions = expand(_graph().gives(100), here="freportw", graph=_graph())
    names = [type(action).__name__ for action in actions]
    assert names == ["Travel", "Fetch", "Zone", "Talk", "Deliver"]
    travel, fetch, zone, talk, deliver = actions
    assert travel.destination == "qeynos"
    assert fetch.item_id == 9
    assert zone.destination == "erudnext"
    assert talk.line == "hail"
    assert talk.priority == 280
    assert deliver.item == 9


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
    assert names == ["Zone", "Talk", "Deliver", "Talk", "Deliver"]
    assert actions[0].destination == "qeynos"
    assert actions[1].priority == 280
    assert actions[2].item == 7
    assert actions[4].item == 8


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
