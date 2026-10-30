"""Journal tables, open-row reload, and a source death can append again."""

import sqlite3
from types import SimpleNamespace

import pytest

from eqclient3.action import Action
from eqclient3.actions.craft import Craft
from eqclient3.actions.reclaim import Reclaim
from eqclient3.actions.rez import Rez
from eqclient3.structs import OP_RezzRequest
from eqclient3.actions.sell import Sell
from eqclient3.journal import DEFAULT_PATH, Journal
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


def test_default_path_is_v3_and_v2_is_refused(tmp_path):
    assert DEFAULT_PATH.endswith("/.eqclient/journal-v3.sqlite")
    blocked = tmp_path / "journal-v2.sqlite"
    with pytest.raises(ValueError):
        Journal(blocked)
    assert not blocked.exists()


def test_create_and_reload_open_row(tmp_path):
    path = tmp_path / "journal-v3.sqlite"
    journal = Journal(path)
    try:
        names = {
            row[0]
            for row in journal._db.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
        }
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
    assert path != DEFAULT_PATH


def test_a_string_wait_reloads_as_a_list(tmp_path):
    journal = Journal(tmp_path / "journal-v3.sqlite")
    try:
        action = Action()
        action.source = "fetch:12"
        action.zone = "gfaydark"
        action.waiting = ["HAIL"]
        assert journal.open_action("Hero", action) is True
        journal._db.execute(
            "UPDATE actions SET payload = ? WHERE character = ? AND source = ?",
            ('{"waiting": "HAIL", "target_id": 12}', "Hero", "fetch:12"),
        )
        journal._db.commit()
        restored = journal.load_actions("Hero")[0]
        assert restored.waiting == ["HAIL"]
        assert restored.target_id == 12
    finally:
        journal.close()


def test_resolved_source_is_not_reloaded_or_appended(tmp_path):
    journal = Journal(tmp_path / "journal-v3.sqlite")
    try:
        done = Action()
        done.source = "task:1"
        done.zone = "qeynos"
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
        assert journal.open_action("Hero", action) is True
        journal.clear_source("Hero", "form:qeynos")

        assert journal.load_actions("Hero") == []
        assert journal.is_open("Hero", "form:qeynos") is False
        assert journal.is_resolved("Hero", "form:qeynos") is False
        assert "form:qeynos" not in journal.resolved_sources("Hero")

        fresh = Action()
        fresh.source = "form:qeynos"
        fresh.zone = "qeynos"
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
        recipe = SimpleNamespace(components=((7, 1),), combine_slot=9, point=(1.0, 2.0, 3.0))
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
    assert loaded[3].recipe.components == ((7, 1),)
    assert loaded[3].recipe.combine_slot == 9
    assert loaded[3].recipe.point == (1.0, 2.0, 3.0)
