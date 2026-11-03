"""Faction graph edges, raise-faction planning, and underwater breath helpers."""

from eqclient.campaign import Campaign, _standing_ok
from eqclient.campaign import CampaignStep
from eqclient.plan import _faction_intention
from eqclient.quests import QuestGraph, _faction_gains, _faction_needs, link_script
from eqclient.water import swim_height
from eqclient.world import Spawn, ZoneModel


def test_faction_needs_primary_and_named():
    primary = "if ($faction <= 3) { quest::say('ok'); }"
    assert ("primary", "<=3") in _faction_needs(primary)

    named = (
        "sub EVENT_SAY {\n"
        "  $faction = $client->GetCharacterFactionLevel(404);\n"
        "  if ($text=~/Hail/i && $faction >= 43) { quest::say('hi'); }\n"
        "}\n"
    )
    assert ("404", ">=43") in _faction_needs("if ($faction >= 43) { }", named)
    assert ("404", 7) in _faction_gains("quest::faction(404, 7); # Faction: Truespirit")


def test_link_script_emits_faction_edges():
    text = (
        "sub EVENT_SAY {\n"
        "  if ($text=~/Hail/i && $faction <= 3) {\n"
        "    quest::say('Welcome');\n"
        "    quest::faction(326, 10);\n"
        "  }\n"
        "}\n"
    )
    edges = link_script(text, "Scout.pl", "gfaydark")
    needs = [e for e in edges if e.get("rel") == "needs" and str(e.get("to")).startswith("faction:")]
    gains = [e for e in edges if e.get("rel") == "sets" and str(e.get("to")).startswith("faction:")]
    assert any(e.get("to") == "faction:primary" and e.get("at") == "<=3" for e in needs)
    assert any(e.get("to") == "faction:326" and e.get("value") == 10 for e in gains)


def test_standing_ok_and_raise_nests_positive_sets():
    assert not _standing_ok("faction:404@>=43", {})
    assert _standing_ok("faction:404@>=43", {"faction:404": 50})
    assert _standing_ok("faction:primary@<=3", {"faction:primary:paineel/gerot kastane": 2}, "paineel", "gerot kastane")

    graph = QuestGraph()
    graph.items[90001] = {"name": "gated", "sources": []}
    graph.items[1001] = {"name": "raise_token", "sources": []}
    graph.edges = [
        {
            "kind": "edge",
            "rel": "gives",
            "from": "paineel/gerot kastane#hail",
            "to": "item:90001",
            "group": "paineel/gerot kastane#hail",
        },
        {
            "kind": "edge",
            "rel": "needs",
            "from": "paineel/gerot kastane#hail",
            "to": "faction:404",
            "at": ">=43",
            "group": "paineel/gerot kastane#hail",
            "faction": "404",
        },
        {
            "kind": "edge",
            "rel": "sets",
            "from": "firiona/nadia starfeast#hand:1001",
            "to": "faction:404",
            "value": 30,
            "group": "firiona/nadia starfeast#hand:1001",
        },
        {
            "kind": "edge",
            "rel": "receives",
            "from": "firiona/nadia starfeast",
            "to": "item:1001",
            "group": "firiona/nadia starfeast#hand:1001",
        },
        {
            "kind": "edge",
            "rel": "gives",
            "from": "poknowledge/vendor",
            "to": "item:1001",
            "group": "poknowledge/vendor",
        },
    ]
    camp = Campaign(class_id=1)
    camp.set_goal(90001, graph=graph)
    # Without standing, nest into the +30 Truespirit hand-in's missing item.
    step = camp.next_step(graph, {}, {}, level=50, here="paineel")
    assert 1001 in camp.stack
    assert step.kind in {"need_item", "travel", "hail", "hand", "buy"}
    assert step.item_id == 1001 or step.zone in {"firiona", "poknowledge"}
    # With standing already met, hail Gerot instead of farming him.
    camp = Campaign(class_id=1)
    camp.set_goal(90001, graph=graph)
    step = camp.next_step(graph, {}, {"faction:404": 50}, level=50, here="paineel")
    assert step.kind == "hail"
    assert "gerot" in step.npc.lower()
    assert step.kind != "faction"


def test_faction_intention_farms_hostile_not_quest_npc():
    world = ZoneModel("Mock")
    world.zone = "gfaydark"
    world.x, world.y, world.z = 0.0, 0.0, 0.0
    quest = Spawn(spawn_id=1, name="Scout_Firebush", npc=1, level=10, body=0, x=10, y=0, z=0)
    foe = Spawn(spawn_id=2, name="an_orc_pawn", npc=1, level=5, body=0, x=5, y=0, z=0)
    world.spawns = {1: quest, 2: foe}
    # Quest NPC already considered (unmet); farm the scowling orc — never the scout.
    world.faction = {1: 5, 2: 9}
    step = CampaignStep(kind="faction", zone="gfaydark", npc="Scout Firebush", text="faction:primary@<=3")
    intent = _faction_intention(world, step)
    assert intent.kind == "fight"
    assert intent.target == 2
    assert intent.name == "an_orc_pawn"


def test_faction_farm_picks_densest_zone_and_named_hits():
    from eqclient.factions import FactionBook, FactionHit

    book = FactionBook()
    book.by_faction[326] = [
        FactionHit(326, 5, 1, "a crushbone orc", "crushbone", 58),
        FactionHit(326, 5, 2, "an orc pawn", "crushbone", 58),
        FactionHit(326, 5, 3, "an orc centurion", "crushbone", 58),
        FactionHit(326, 30, 4, "Emperor Crush", "crushbone", 58),
        FactionHit(326, 11, 5, "a faerie", "gfaydark", 54),
    ]
    assert book.densest_zone(326) == "crushbone"
    hit = book.farm(326, here="gfaydark")
    assert hit is not None
    assert hit.zone == "crushbone"
    assert hit.name == "Emperor Crush"

    graph = QuestGraph()
    graph.items[90002] = {"name": "gated", "sources": []}
    graph.edges = [
        {
            "kind": "edge",
            "rel": "gives",
            "from": "gfaydark/Scout Firebush#hail",
            "to": "item:90002",
            "group": "gfaydark/Scout Firebush#hail",
        },
        {
            "kind": "edge",
            "rel": "needs",
            "from": "gfaydark/Scout Firebush#hail",
            "to": "faction:326",
            "at": ">=100",
            "group": "gfaydark/Scout Firebush#hail",
            "faction": "326",
        },
    ]
    camp = Campaign(class_id=1)
    camp.set_goal(90002, graph=graph)
    step = camp.next_step(graph, {}, {}, level=50, here="gfaydark", factions=book)
    assert step.kind == "travel"
    assert step.zone == "crushbone"
    assert "crush" in step.npc.lower() or "orc" in step.npc.lower()

    world = ZoneModel("Mock")
    world.zone = "crushbone"
    world.x = world.y = world.z = 0.0
    orc = Spawn(spawn_id=10, name="a_crushbone_orc", npc=1, level=5, body=0, x=3, y=0, z=0)
    other = Spawn(spawn_id=11, name="a_wolf", npc=1, level=5, body=0, x=1, y=0, z=0)
    world.spawns = {10: orc, 11: other}
    world.faction = {10: 5, 11: 9}
    farm_step = CampaignStep(
        kind="faction",
        zone="crushbone",
        npc="Emperor Crush",
        word="@gfaydark/Scout Firebush",
        text="faction:326@>=100",
    )
    intent = _faction_intention(world, farm_step, book)
    assert intent.kind == "fight"
    assert intent.target == 10


def test_skill_gate_blocks_craft_below_trivial():
    from eqclient.conduct import Recipe, RecipeBook

    book = RecipeBook()
    book.by_id[1] = Recipe(
        id=1,
        result=5000,
        components=((100, 1),),
        container=17809,
        skill=63,
        skillneeded=0,
        trivial=100,
        name="Blacksmithing",
    )
    book.by_id[2] = Recipe(
        id=2,
        result=5001,
        components=((101, 1),),
        container=17809,
        skill=63,
        skillneeded=0,
        trivial=20,
        name="Blacksmithing",
    )
    book.index()
    # Already-trivial recipes must not be chosen for skillups (skill >= trivial).
    assert book.practice(63, current=0, want=100).id == 2
    assert book.practice(63, current=20, want=100).id == 1  # skip trivial-20; climb on goal
    assert book.practice(63, current=100, want=100) is None  # nothing left below/at want

    graph = QuestGraph()
    graph.items[5000] = {"name": "sword", "sources": []}
    graph.items[100] = {"name": "ore", "sources": []}
    graph.items[101] = {"name": "bits", "sources": []}
    graph.edges = [
        {"kind": "edge", "rel": "gives", "from": "poknowledge/vendor", "to": "item:100", "group": "poknowledge/vendor"},
        {"kind": "edge", "rel": "gives", "from": "poknowledge/vendor", "to": "item:101", "group": "poknowledge/vendor"},
    ]
    camp = Campaign(class_id=1)
    camp.set_goal(5000, graph=graph)
    from eqclient.campaign import _SKILL_PRACTICE, _skill_gate

    # Skill short → stack practice RESULT (~50); comps nest as practice × recipe.
    step = camp.next_step(graph, {17809: 1}, {}, level=50, recipes=book, skills={})
    assert 5001 in camp.stack
    assert camp.counts.get(5001) == _SKILL_PRACTICE
    assert 5001 in camp.sell_after
    # Nested obtain for practice comps (buy/farm/craft — here vendor hail).
    assert 101 in camp.stack or step.kind in {"need_item", "travel", "hail", "buy"}
    assert (camp.counts.get(101) or 0) >= _SKILL_PRACTICE or step.item_id in {101, 5001}
    # Practice product on stack with mats → craft that recipe many times.
    camp = Campaign(class_id=1)
    camp.set_goal(5000, graph=graph)
    step = camp.next_step(graph, {101: _SKILL_PRACTICE, 17809: 1}, {}, level=50, recipes=book, skills={})
    assert 5001 in camp.stack
    step = camp.next_step(graph, {101: _SKILL_PRACTICE, 17809: 1}, {}, level=50, recipes=book, skills={})
    # After push, expand 5001 → craft recipe 2 (no recursive skill gate).
    assert step.kind == "craft"
    assert step.recipe_id == 2
    # Finished practice wave → sell the products before popping back to the goal.
    camp = Campaign(class_id=1)
    camp.set_goal(5000, graph=graph)
    camp.push(5001, _SKILL_PRACTICE)
    camp.sell_after.add(5001)
    step = camp.next_step(
        graph,
        {5001: _SKILL_PRACTICE, 101: _SKILL_PRACTICE, 17809: 1},
        {},
        level=50,
        recipes=book,
        skills={},
    )
    assert step.kind == "sell" and step.item_id == 5001 and step.count == _SKILL_PRACTICE
    assert 5001 not in camp.stack
    # Bags full mid-practice → sell held products and credit the wave.
    camp = Campaign(class_id=1)
    camp.set_goal(5000, graph=graph)
    camp.push(5001, _SKILL_PRACTICE)
    camp.sell_after.add(5001)
    step = camp.next_step(graph, {5001: 20, 17809: 1}, {}, level=50, recipes=book, skills={}, bag_full=True)
    assert step.kind == "sell" and step.item_id == 5001 and step.count == 20
    assert camp.counts.get(5001) == _SKILL_PRACTICE - 20
    # Skill met, leftover practice comps → burn (not the goal recipe).
    gate = _skill_gate(book, 1, {63: 100}, 5000, {100: 50, 101: 50, 17809: 1}, [])
    assert gate is not None and gate.kind == "skill" and gate.recipe_id == 2
    assert _skill_gate(book, 1, {63: 100}, 5000, {100: 1, 17809: 1}, []) is None
    camp = Campaign(class_id=1)
    camp.set_goal(5000, graph=graph)
    step = camp.next_step(graph, {100: 1, 17809: 1}, {}, level=50, recipes=book, skills={63: 100})
    assert step.kind == "craft"
    assert step.recipe_id == 1


def test_breath_defaults_and_swim_height():
    model = ZoneModel("Mock")
    assert model.air == 60
    assert swim_height(-50.0, -47.0) == -47.0
    assert swim_height(-50.0, -20.0) == -46.0
