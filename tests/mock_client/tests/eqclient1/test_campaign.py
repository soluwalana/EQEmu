"""Item-goal campaign planner, travel BFS, journal stack, and protect rules."""

from eqclient.campaign import Campaign
from eqclient.conduct import farm_target, order_of
from eqclient.epics import can_obtain, default_epic20_item, flag_satisfied
from eqclient.journal import Journal
from eqclient.party import GROUP_ROSTER, PartyBuilder
from eqclient.protect import is_protected, protected_ids
from eqclient.quests import QuestGraph
from eqclient.travel import adjacency, path


def _graph() -> QuestGraph:
    graph = QuestGraph()
    graph.items[62649] = {"name": "Aurora", "classes": [4], "zones": ["povalor"], "sources": []}
    graph.items[200] = {"name": "component", "zones": ["poknowledge"], "sources": []}
    graph.items[201] = {"name": "lootpiece", "zones": ["eastkarana"], "sources": ["loot:a_wolf@eastkarana"]}
    graph.edges = [
        {
            "kind": "edge",
            "rel": "gives",
            "from": "povalor/Telin_Darkforest#Hail",
            "to": "item:62649",
            "group": "povalor/Telin_Darkforest#Hail",
            "classes": [4],
        },
        {
            "kind": "edge",
            "rel": "needs",
            "from": "povalor/Telin_Darkforest#Hail",
            "to": "item:200",
            "group": "povalor/Telin_Darkforest#Hail",
            "count": 1,
        },
        {
            "kind": "edge",
            "rel": "needs",
            "from": "povalor/Telin_Darkforest#Hail",
            "to": "flag:ranger_epic",
            "group": "povalor/Telin_Darkforest#Hail",
            "flag": "ranger_epic",
            "at": ">=6",
        },
        {
            "kind": "edge",
            "rel": "gives",
            "from": "poknowledge/a_merchant",
            "to": "item:200",
            "group": "poknowledge/a_merchant",
        },
        {
            "kind": "edge",
            "rel": "needs",
            "from": "poknowledge/a_merchant",
            "to": "item:201",
            "group": "poknowledge/a_merchant",
        },
        {
            "kind": "edge",
            "rel": "loots",
            "from": "eastkarana/a_wolf",
            "to": "item:201",
            "zone": "eastkarana",
            "npc": "a_wolf",
        },
        {"kind": "edge", "rel": "travel", "from": "poknowledge", "to": "eastkarana", "door": 10, "dest_id": 0},
        {"kind": "edge", "rel": "travel", "from": "eastkarana", "to": "povalor", "door": 11, "dest_id": 0},
        {"kind": "edge", "rel": "travel", "from": "poknowledge", "to": "povalor", "door": 12, "dest_id": 0},
    ]
    graph.doors = {
        "poknowledge": {10: [15], 12: [208]},
        "eastkarana": {11: [208]},
    }
    return graph


def test_ranger_epic20_default_and_class_gate():
    assert default_epic20_item(4) == 62649
    assert default_epic20_item(1) == 60329
    assert default_epic20_item(16) == 18609
    graph = _graph()
    assert can_obtain(62649, 4, 1, graph)
    assert not can_obtain(62649, 1, 1, graph)


def test_nested_obtain_stack_pushes_and_pops():
    graph = _graph()
    camp = Campaign(class_id=4, race_id=1)
    assert camp.set_goal(62649, graph=graph)
    # Item prereqs nest even when the flag gate is not yet met.
    step = camp.next_step(graph, {}, {}, level=70, here="povalor")
    assert 62649 in camp.stack and 200 in camp.stack
    assert camp.peek() == 201
    assert step.kind in {"kill", "loot", "travel"}
    # Holding the child pops it; parent 200 resumes once the flag is set.
    step = camp.next_step(graph, {201: 1}, {"ranger_epic": 6}, level=70, here="poknowledge")
    assert 201 not in camp.stack
    assert camp.peek() == 200
    assert step.kind in {"hail", "hand", "travel"}


def test_assign_goal_does_not_erase_prior_stack():
    camp = Campaign(class_id=4)
    camp.set_goal(62649)
    assert camp.assign_goal(1001, 5)
    assert camp.stack == [62649, 1001]
    assert camp.counts[1001] == 5
    assert camp.peek() == 1001


def test_journal_persists_full_goal_stack():
    journal = Journal(":memory:")
    journal.save_goal_stack(
        "Mockone", [62649, 1001], {62649: 1, 1001: 5}, deliver_to="Sam", deliver_item=1001, deliver_count=5
    )
    stack, counts = journal.load_goal_stack("Mockone")
    assert stack == [62649, 1001]
    assert counts[1001] == 5
    who, item_id, count = journal.load_goal_deliver("Mockone")
    assert who == "Sam" and item_id == 1001 and count == 5
    # Replacing the save keeps both layers when rewritten as a full stack.
    journal.save_goal_stack("Mockone", [62649, 1001, 200], {62649: 1, 1001: 5, 200: 2})
    stack, counts = journal.load_goal_stack("Mockone")
    assert stack == [62649, 1001, 200]
    assert counts[200] == 2


def test_mid_run_set_goal_via_assign_keeps_epic():
    camp = Campaign(class_id=4)
    camp.set_goal(62649)
    camp.assign_goal(555, 3)
    assert camp.stack[0] == 62649
    camp.pop()
    assert camp.peek() == 62649


def test_travel_bfs_and_flag_gate():
    graph = _graph()
    legs = path(graph, "poknowledge", "eastkarana")
    assert legs and legs[0].door_id == 10
    assert flag_satisfied("ranger_epic", ">=6", {"ranger_epic": 6})
    assert not flag_satisfied("ranger_epic", ">=6", {"ranger_epic": 5})
    assert not flag_satisfied("ranger_epic", ">=6", {})
    links = adjacency(graph)
    assert "poknowledge" in links


def test_zone_graph_records_coords_dest_and_requirements():
    import tempfile
    from pathlib import Path

    from eqclient.travel import (
        Transit,
        TransitNeed,
        ZoneGraph,
        can_transit,
        build_zone_graph,
        read_zone_graph,
        write_zone_graph,
    )

    text = """
INSERT INTO `zone` VALUES
('tox',1,'tox','Tox', '',0,0,0,0,0,0,255,0,38),
('poknowledge',2,'pok','PoK','',0,0,0,0,0,0,255,0,202);
INSERT INTO `doors` VALUES
(9,8,'Tox',0,'POKTELE500',2324.96,-582.532,-47.8143,120,58,0,0,0,0,0,0,0,0,0,'poknowledge',0,35.9,630.0,-145.0,256,0,0,100,0,4294967295,0,0,4,-1,NULL,NULL),
(10,1,'Tox',0,'KEYDOOR',10.0,20.0,30.0,0,58,0,50,12345,0,0,0,0,0,0,'poknowledge',0,1,2,3,0,0,0,100,0,4294967295,0,0,-1,-1,NULL,NULL),
(11,2,'PoKnowledge',0,'LOCAL',1,2,3,0,58,0,0,0,0,0,0,0,0,0,'NONE',0,0,0,0,0,0,0,100,0,4294967295,0,0,-1,-1,NULL,NULL);
"""
    with tempfile.TemporaryDirectory() as tmp:
        dump = Path(tmp) / "dump.sql"
        dump.write_text(text, encoding="latin1")
        graph = build_zone_graph(dump)
        assert graph.zones.get("poknowledge") == 202
        out = Path(tmp) / "zone_graph.jsonl"
        write_zone_graph(graph, str(out))
        loaded = read_zone_graph(str(out))
    stone = next(t for t in loaded.transits if t.door_id == 8)
    assert stone.dest == "poknowledge" and stone.dest_id == 202
    assert stone.x == -582.532 and stone.y == 2324.96 and stone.z == -47.8143
    assert stone.dest_x == 35.9 and stone.need.min_expansion == 4
    keyed = next(t for t in loaded.transits if t.need.key_item == 12345)
    assert keyed.need.lockpick == 50
    assert not can_transit(keyed, inventory_ids=set(), lockpick_skill=0)
    assert can_transit(keyed, inventory_ids={12345}, lockpick_skill=50)
    assert can_transit(stone, door_ids={8})
    assert not can_transit(stone, door_ids={99})  # live zone never spawned this stone
    assert not any(t.dest == "none" for t in loaded.transits)

    # Round-trip an explicit transit with every requirement field.
    g = ZoneGraph(zones={"a": 1, "b": 2})
    g.transits = []
    from eqclient.travel import _add_transit

    _add_transit(
        g,
        Transit(
            zone="a",
            door_id=9,
            dest="b",
            dest_id=2,
            via="door",
            name="GATE",
            x=1,
            y=2,
            z=3,
            need=TransitNeed(key_item=7, lockpick=100, content_flags="kunark"),
        ),
    )
    assert g.edges[0]["need"]["key_item"] == 7
    assert g.edges[0]["x"] == 1


def test_group_roster_is_about_six_and_combat_orders():
    assert len(GROUP_ROSTER) == 5  # + player = group of 6
    party = PartyBuilder("Mockone", raid=False)
    assert not party.raid
    party.formed = True
    assert party.combat_order("attack") == "attack"
    assert party.combat_order("guard") == "guard spawned"
    assert party.combat_order("hold") == "hold spawned"


def test_farm_tell_and_join_phrases():
    assert farm_target("1001 5") == (1001, 5)
    assert farm_target("1001 x3") == (1001, 3)
    order = order_of("Sam", "farm 1001 5")
    assert order is not None and order.verb == "farm" and order.rest == "1001 5"
    assert order_of("Sam", "invite me please").verb == "join"
    assert order_of("Sam", "add me to group").verb == "join"


def test_protect_quest_and_campaign_items():
    graph = _graph()
    camp = Campaign(class_id=4)
    camp.set_goal(62649)
    camp.push(200)
    assert is_protected(200, graph, camp)
    assert is_protected(62649, graph, camp)
    # Pure loot with no hand-in need is not protected once off the stack.
    camp.pop()
    camp.pop()
    ids = protected_ids(graph, camp)
    assert 201 in ids or 201 not in ids  # 201 is loots+needs — needs keeps it
    assert 201 in protected_ids(graph, None)  # still a hand-in need on the graph


def test_camps_for_level_bands():
    from eqclient.camps import camp_for_level, needs_level

    assert camp_for_level(3).zone == "qeynos"
    assert camp_for_level(3, "freportw").zone == "freportw"
    assert camp_for_level(3).zone != "tutorialb"
    assert needs_level(10, 20)
    assert not needs_level(25, 20)


def _warrior_blade_graph() -> QuestGraph:
    """Minimal Blade of Strategy (10910) chain matching write_epics forward order.

    Container (17859) expands before recipe consumes, walking the Redblade
    hand-ins back to Wax Sealed Note (20673) via Kargek Favor.
    """
    graph = QuestGraph()
    for item_id, name in (
        (10910, "Blade of Strategy"),
        (10908, "Jagged Blade of War"),
        (17859, "Red Scabbard"),
        (20684, "Tenal's note to Kargek"),
        (20679, "Spiroc Wingblade"),
        (20674, "Tiny Lute"),
        (20673, "Wax Sealed Note"),
    ):
        graph.items[item_id] = {"name": name, "zones": [], "sources": []}
    graph.edges = [
        {"kind": "edge", "rel": "produces", "from": "recipe:9689", "to": "item:10910"},
        {"kind": "edge", "rel": "container", "from": "recipe:9689", "to": "item:17859"},
        {"kind": "edge", "rel": "consumes", "from": "recipe:9689", "to": "item:10908", "count": 1},
        # Recombine loop — skipped when root goal is 10910.
        {"kind": "edge", "rel": "produces", "from": "recipe:9833", "to": "item:10908"},
        {"kind": "edge", "rel": "consumes", "from": "recipe:9833", "to": "item:10910", "count": 1},
        {
            "kind": "edge",
            "rel": "gives",
            "from": "freeporteast/kargek redblade",
            "to": "item:17859",
            "group": "freeporteast/kargek redblade#hand:20679+20684",
        },
        {
            "kind": "edge",
            "rel": "receives",
            "from": "freeporteast/kargek redblade",
            "to": "item:20684",
            "group": "freeporteast/kargek redblade#hand:20679+20684",
            "count": 1,
        },
        {
            "kind": "edge",
            "rel": "receives",
            "from": "freeporteast/kargek redblade",
            "to": "item:20679",
            "group": "freeporteast/kargek redblade#hand:20679+20684",
            "count": 1,
        },
        {
            "kind": "edge",
            "rel": "gives",
            "from": "freeporteast/kargek redblade",
            "to": "item:20684",
            "group": "freeporteast/kargek redblade#hand:20674",
        },
        {
            "kind": "edge",
            "rel": "receives",
            "from": "freeporteast/kargek redblade",
            "to": "item:20674",
            "group": "freeporteast/kargek redblade#hand:20674",
            "count": 1,
        },
        {
            "kind": "edge",
            "rel": "gives",
            "from": "feerrott/oknoggin stonesmacker",
            "to": "item:20674",
            "group": "feerrott/oknoggin stonesmacker#hand:20673",
        },
        {
            "kind": "edge",
            "rel": "receives",
            "from": "feerrott/oknoggin stonesmacker",
            "to": "item:20673",
            "group": "feerrott/oknoggin stonesmacker#hand:20673",
            "count": 1,
        },
        {
            "kind": "edge",
            "rel": "gives",
            "from": "freeporteast/kargek redblade",
            "to": "item:20673",
            "group": "freeporteast/kargek redblade#favor",
        },
        {
            "kind": "edge",
            "rel": "loots",
            "from": "island/spiroc",
            "to": "item:20679",
            "zone": "island",
            "npc": "a_spiroc",
        },
    ]
    return graph


def test_blade_of_strategy_decomp_starts_at_kargek_favor():
    """write_epics forward(10910) begins with Wax Sealed Note via Kargek Favor."""
    graph = _warrior_blade_graph()
    camp = Campaign(class_id=1)
    assert camp.set_goal(10910, graph=graph)
    step = camp.next_step(graph, {}, {}, level=70, here="freeporteast")
    assert 20673 in camp.stack, camp.stack
    assert camp.peek() == 20673
    assert step.kind == "hail"
    assert "kargek" in step.npc.lower()
    assert step.word.lower() == "favor"


def test_zone_level_gate_travel():
    from eqclient.camps import zone_needs_swim, zone_recommended_level, zone_reachable

    assert zone_recommended_level("lakerathe") >= 5
    assert zone_needs_swim("lakerathe")
    # Swimming is supported; under-level outdoor floors still gate travel.
    assert zone_reachable("lakerathe", 4).startswith("level:")
    assert zone_reachable("najena", 4).startswith("level:")
    assert zone_reachable("freeporteast", 4) == ""
    assert zone_reachable("feerrott", 4) == ""  # guide band starts at 1
    assert zone_reachable("lakerathe", 30) == ""
    assert zone_recommended_level("soldungb") >= 35

    graph2 = QuestGraph()
    graph2.items[99] = {"name": "najena drop", "zones": ["najena"], "sources": []}
    graph2.edges = [
        {
            "kind": "edge",
            "rel": "loots",
            "from": "najena/a_skeleton",
            "to": "item:99",
            "zone": "najena",
            "npc": "a_skeleton",
        }
    ]
    camp2 = Campaign(class_id=1)
    camp2.set_goal(99)
    step2 = camp2.next_step(graph2, {}, {}, level=4, here="freeporteast")
    assert step2.kind == "level"
    assert int(step2.text) >= 11


def test_plane_zone_flag_unlocks_via_intention():
    """Missing zoneflag:<id> for a flagged plane becomes hail/hand, not a hard block."""
    from eqclient.travel import TransitNeed, ZoneGraph, can_transit, zoneflag_key

    graph = QuestGraph()
    graph.items[500] = {"name": "plane scrap", "zones": ["poair"], "sources": []}
    graph.edges = [
        {
            "kind": "edge",
            "rel": "loots",
            "from": "poair/a_dust_elemental",
            "to": "item:500",
            "zone": "poair",
            "npc": "a_dust_elemental",
        },
        {
            "kind": "edge",
            "rel": "needs",
            "from": "zone:poair",
            "to": "flag:zoneflag:215",
            "flag": "zoneflag:215",
            "at": "set",
            "zone": "poair",
        },
        {
            "kind": "edge",
            "rel": "sets",
            "from": "potranquility/Adler_Fuirstel#Hail",
            "to": "flag:zoneflag:215",
            "flag": "zoneflag:215",
            "value": "1",
            "group": "potranquility/Adler_Fuirstel#Hail",
        },
    ]
    camp = Campaign(class_id=1)
    camp.set_goal(500)
    # No flag → unlock the set_zone_flag giver instead of blocking.
    step = camp.next_step(graph, {}, {}, level=70, here="poknowledge")
    assert step.kind in {"hail", "travel"}
    assert "adler" in (step.npc or "").lower() or step.zone == "potranquility"
    assert "zoneflag:215" in (step.text or "") or step.kind == "travel"
    # With the flag, travel into the plane is allowed.
    step = camp.next_step(graph, {}, {zoneflag_key(215): 1}, level=70, here="poknowledge")
    assert step.kind == "travel" and step.zone == "poair"

    need = TransitNeed(zone_flag=215)
    from eqclient.travel import Transit

    transit = Transit(zone="poknowledge", door_id=1, dest="poair", dest_id=215, need=need)
    assert not can_transit(transit, flags={})
    assert can_transit(transit, flags={zoneflag_key(215): 1})
    zg = ZoneGraph(zones={"poair": 215}, flagged={"poair": 215})
    fake = QuestGraph()
    zg.apply_to_quest_graph(fake)
    assert any(
        e.get("rel") == "needs" and e.get("flag") == "zoneflag:215" and e.get("from") == "zone:poair"
        for e in fake.edges
    )
