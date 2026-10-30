"""Each agent carries its own race, class, and quest journal."""

from __future__ import annotations

import pytest

from eqclient.agent import AgentSpec
from eqclient.items import Held, Inventory
from eqclient.journal import Journal
from eqclient.plan import choose
from eqclient.quests import Need, NpcScript, ZoneQuests
from eqclient.sheet import CharacterError
from eqclient.tasks import TaskBook
from eqclient.world import Spawn, ZoneModel


def test_a_dark_elf_is_not_a_human_warrior():
    human = AgentSpec("Mockone").sheet()
    elf = AgentSpec("Velkyn", race=6, class_id=1).sheet()
    assert human.stats == (110, 85, 80, 75, 75, 75, 75)
    assert human.start_zone == 1
    assert human.deity == 396
    assert elf.race_name == "dark elf"
    assert elf.start_zone == 5
    assert elf.deity == 206
    assert elf.stats == (95, 75, 95, 75, 83, 99, 60)
    assert elf.stats != human.stats


def test_a_dark_elf_cannot_be_a_paladin():
    with pytest.raises(CharacterError, match="dark elf cannot be a paladin"):
        AgentSpec("Velkyn", race=6, class_id=3).sheet()


def test_two_characters_keep_separate_quest_triggers(tmp_path):
    path = str(tmp_path / "journal.sqlite")
    first = Journal(path)
    second = Journal(path)
    first.record("Mockone", "tutorialb", "arias", "say", "hail")
    first.record("Mockone", "tutorialb", "arias", "say", "ready")
    assert first.triggers("Mockone", "tutorialb", "arias") == [("say", "hail"), ("say", "ready")]
    assert second.said("Mockone", "tutorialb") == {("arias", "hail"), ("arias", "ready")}
    assert second.said("Velkyn", "tutorialb") == set()

    world = ZoneModel("Velkyn")
    world.zone = "tutorialb"
    world.level = 5
    world.spawns[1] = Spawn(1, "Arias", 1, 50, 1, 4.0, -140.0, 19.0)
    quests = ZoneQuests("tutorialb")
    quests.scripts["arias"] = NpcScript("Arias", ["hail", "ready"], [Need(54234, 1, "Arias")])
    intent = choose(world, TaskBook(), quests, Inventory(), True, said=second.said("Velkyn", "tutorialb"))
    assert intent is not None
    assert intent.kind == "talk"
    assert intent.text == "hail"

    bag = Inventory()
    bag.slots[22] = Held(54234, 22, 1, "silk", "")
    done = first.handed("Mockone", "tutorialb")
    first.record("Mockone", "tutorialb", "arias", "handin", "54234")
    skipped = choose(
        world,
        TaskBook(),
        quests,
        bag,
        True,
        said={("arias", "hail"), ("arias", "ready")},
        handed=first.handed("Mockone", "tutorialb"),
    )
    assert skipped is None or skipped.kind != "hand_in"
    assert ("arias", "54234") not in done
    assert ("arias", "54234") in first.handed("Mockone", "tutorialb")
