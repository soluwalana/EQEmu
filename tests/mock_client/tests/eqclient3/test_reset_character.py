"""Reset clears the queue and the started marks. Stats live on the character."""

from eqclient3.action import Action
from eqclient3.journal import Journal
from eqclient3.reset_character import reset
from eqclient3.world import World


def test_reset_clears_the_queue_and_the_started_flags():
    journal = Journal(":memory:")
    action = Action()
    action.source = "reclaim:278"
    action.zone = "tutorialb"
    journal.open_action("Mockvthree", action)
    journal.push_goal("Mockvthree", 60329, 1)
    journal.mark_tutorial_done("Mockvthree")
    journal.set_flag("Mockvthree", "tutorial_started", 1)
    journal.set_flag("Mockvthree", "quest_started", 1)
    counts = reset(journal, "Mockvthree")
    assert counts == {"actions": 1, "goals": 1, "tutorial": 1}
    assert journal.load_actions("Mockvthree") == []
    assert journal.load_goals("Mockvthree") == []
    assert journal.tutorial_done("Mockvthree") is False
    assert journal.flag_values("Mockvthree")["tutorial_started"] == 0
    assert journal.flag_values("Mockvthree")["quest_started"] == 0


def test_player_stats_and_inventory_live_on_the_character():
    world = World(name="Mockvthree", self_id=7, level=4, exp=9, points=2)
    world.race = 1
    world.bags[22] = 1001
    world.cursor = 1001
    world.items[1001] = "Rusty Sword"
    world.tutorial_started = True
    assert world.character.self_id == 7
    assert world.character.level == 4
    assert world.character.exp == 9
    assert world.character.points == 2
    assert world.character.training_points == 2
    assert world.character.race == 1
    assert world.character.bags[22] == 1001
    assert world.character.cursor == 1001
    assert world.character.items[1001] == "Rusty Sword"
    assert world.character.tutorial_started is True
    assert world.character.quest_started is False
