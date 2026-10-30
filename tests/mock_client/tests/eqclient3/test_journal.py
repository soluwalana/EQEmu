"""Journal tables, open-row reload, and a source death can append again."""

import json
import sqlite3
from pathlib import Path
from eqclient3.action import Action
from eqclient3.actions.craft import Craft
from eqclient3.data.recipes import Recipe
from eqclient3.actions.reclaim import Reclaim
from eqclient3.actions.rez import Rez
from eqclient3.structs import OP_RezzRequest
from eqclient3.actions.sell import Sell
from eqclient3.journal import Journal
from eqclient3.schedule import Schedule
from eqclient3.world import World

TABLES = (
    "says",
    "handins",
    "flags",
    "soulbind",
    "tutorial",
    "corpses",
    "goals",
    "actions",
    "bot_worn",
    "bot_settings",
    "bots",
    "sell_marks",
)


def test_each_character_has_its_own_database(tmp_path, monkeypatch):
    monkeypatch.setattr("eqclient3.journal.JOURNAL_ROOT", tmp_path)
    monkeypatch.setattr("eqclient3.journal.catalog", tmp_path / "characters.json")
    hero = Journal(character="Hero")
    other = Journal(character="Mage")
    try:
        action = Action()
        action.source = "fetch:12"
        action.zone = "gfaydark"
        action.durable = True
        assert hero.open_action("Hero", action) is True
        assert Path(hero.db_path) == tmp_path / "Hero" / "journal-v3.sqlite3"
        assert Path(other.db_path) == tmp_path / "Mage" / "journal-v3.sqlite3"
        assert hero.db_path != other.db_path
        assert [row.source for row in hero.load_actions("Hero")] == ["fetch:12"]
        assert other.load_actions("Hero") == []
        assert other.load_actions("Mage") == []
    finally:
        hero.close()
        other.close()
    catalog = json.loads((tmp_path / "characters.json").read_text())
    assert Path(catalog["Hero"]["database"]) == tmp_path / "Hero" / "journal-v3.sqlite3"
    assert Path(catalog["Mage"]["database"]) == tmp_path / "Mage" / "journal-v3.sqlite3"
    hero_db = sqlite3.connect(tmp_path / "Hero" / "journal-v3.sqlite3")
    mage_db = sqlite3.connect(tmp_path / "Mage" / "journal-v3.sqlite3")
    try:
        assert hero_db.execute("SELECT COUNT(*) FROM actions").fetchone()[0] == 1
        assert mage_db.execute("SELECT COUNT(*) FROM actions").fetchone()[0] == 0
    finally:
        hero_db.close()
        mage_db.close()


PRIORITIES = (0, 100, 200, 210, 220, 230, 240, 250, 260, 270, 290, 300, 350, 400, 410)


def _run_order(actions) -> list[str]:
    ranked = sorted(actions, key=lambda action: (-action.priority, type(action).key(action)))
    return [action.source for action in ranked]


def test_recovered_queue_keeps_the_insert_order(tmp_path):
    world = World()
    world.zone = "qeynos"
    path = tmp_path / "journal-v3.sqlite"
    journal = Journal(path)
    queue = Schedule()
    queue.bind(journal, "Hero")
    try:
        for priority in PRIORITIES:
            for index in range(3):
                action = Action()
                action.priority = priority
                action.source = f"band:{priority}:{index}"
                action.durable = True
                assert queue.append(action, world) is True
        before = _run_order(queue)
        appended = [action.source for action in queue]
    finally:
        journal.close()

    again = Journal(path)
    try:
        loaded = again.load_actions("Hero")
        assert _run_order(loaded) == before
        recovered = Schedule()
        for action in loaded:
            assert recovered.restore(action) is True
        assert [action.source for action in recovered] == appended
        assert _run_order(recovered) == before
    finally:
        again.close()


def test_create_and_reload_open_row(tmp_path):
    path = tmp_path / "journal-v3.sqlite"
    journal = Journal(path)
    try:
        names = {row[0] for row in journal._db.execute("SELECT name FROM sqlite_master WHERE type = 'table'")}
        assert set(TABLES) <= names

        action = Action()
        action.source = "fetch:12"
        action.zone = "gfaydark"
        action.priority = 0
        action.durable = True
        action.target_id = 12
        action.waiting = ["HAIL"]
        assert journal.open_action("Hero", action) is True
    finally:
        journal.close()

    again = Journal(path)
    try:
        loaded = again.load_actions("Hero")
        assert len(loaded) == 1
        restored = loaded[0]
        assert restored.source == "fetch:12"
        assert restored.zone == "gfaydark"
        assert restored.priority == 0
        assert restored.durable is True
        assert restored.target_id == 12
        assert restored.waiting == ["HAIL"]
        assert restored.suspended is True
        assert restored.messages == []
        assert restored.active_path is None
        assert restored.completed is False
    finally:
        again.close()

    seen = sqlite3.connect(path)
    try:
        count = seen.execute("SELECT COUNT(*) FROM actions").fetchone()[0]
    finally:
        seen.close()
    assert count == 1


def test_an_action_that_is_not_durable_is_not_reloaded(tmp_path):
    path = tmp_path / "journal-v3.sqlite"
    journal = Journal(path)
    try:
        action = Action()
        action.source = "hail:absor"
        action.zone = "tutorialb"
        assert journal.open_action("Hero", action) is True
        assert journal.load_actions("Hero") == []
        assert journal.is_open("Hero", "hail:absor") is False
        journal.resolve_action("Hero", action)
        assert journal.is_resolved("Hero", "hail:absor") is True
        assert journal.load_actions("Hero") == []
    finally:
        journal.close()

    again = Journal(path)
    try:
        assert again.load_actions("Hero") == []
        assert again.is_resolved("Hero", "hail:absor") is True
    finally:
        again.close()


def test_resolved_source_is_not_reloaded_or_appended(tmp_path):
    journal = Journal(tmp_path / "journal-v3.sqlite")
    try:
        done = Action()
        done.source = "task:1"
        done.zone = "qeynos"
        done.durable = True
        journal.resolve_action("Hero", done)

        assert journal.load_actions("Hero") == []
        assert journal.is_resolved("Hero", "task:1") is True
        assert journal.open_action("Hero", done) is False

        world = World()
        queue = Schedule()
        queue.bind(journal, "Hero")
        again = Action()
        again.source = "task:1"
        assert queue.append(again, world) is False
        assert len(queue) == 0
    finally:
        journal.close()


def test_clear_source_is_neither_open_nor_resolved(tmp_path):
    journal = Journal(tmp_path / "journal-v3.sqlite")
    try:
        action = Action()
        action.source = "form:qeynos"
        action.zone = "qeynos"
        action.durable = True
        assert journal.open_action("Hero", action) is True
        journal.clear_source("Hero", "form:qeynos")

        assert journal.load_actions("Hero") == []
        assert journal.is_open("Hero", "form:qeynos") is False
        assert journal.is_resolved("Hero", "form:qeynos") is False
        assert "form:qeynos" not in journal.resolved_sources("Hero")

        fresh = Action()
        fresh.source = "form:qeynos"
        fresh.zone = "qeynos"
        fresh.durable = True
        assert journal.open_action("Hero", fresh) is True
        assert [row.source for row in journal.load_actions("Hero")] == ["form:qeynos"]
    finally:
        journal.close()


def test_reload_restores_each_actions_own_fields(tmp_path):
    journal = Journal(tmp_path / "journal-v3.sqlite")
    try:
        body = Reclaim(15, (4.0, 5.0, 6.0))
        body.source = "reclaim:15"
        spell = Rez(15, OP_RezzRequest(zone_id=3, corpse_name="Hero"))
        spell.source = "rez:15"
        shop = Sell([9])
        shop.source = "sell:9"
        shop.slots = {3: (9, 100)}
        shop.merchant_id = 8
        shop.merchant_point = (1.0, 2.0, 3.0)
        recipe = Recipe(id=9, result=8, components=((7, 1),), container=17)
        made = Craft(recipe)
        made.source = "craft:9"
        assert journal.open_action("Hero", body) is True
        assert journal.open_action("Hero", spell) is True
        assert journal.open_action("Hero", shop) is True
        assert journal.open_action("Hero", made) is True
        loaded = journal.load_actions("Hero")
    finally:
        journal.close()

    assert [type(action) for action in loaded] == [Reclaim, Rez, Sell, Craft]
    assert loaded[0].corpse_id == 15
    assert loaded[0].where == (4.0, 5.0, 6.0)
    assert loaded[0].requested is False
    assert loaded[1].payload.zone_id == 3
    assert loaded[1].payload.corpse_name == "Hero"
    assert loaded[2].slots == {3: (9, 100)}
    assert loaded[2].merchant_id == 8
    assert loaded[2].merchant_point == (1.0, 2.0, 3.0)
    assert loaded[2].window is False
    assert loaded[3].recipe.id == 9
    assert loaded[3].recipe.result == 8
    assert loaded[3].recipe.components == ((7, 1),)
    assert loaded[3].recipe.container == 17
