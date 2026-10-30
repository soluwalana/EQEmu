"""Schedule order: band 0 is newest insert, and a higher priority wins."""

import time

from eqclient3.action import Action
from eqclient3.schedule import Schedule
from eqclient3.world import World


class OlderFirst(Action):
    @staticmethod
    def key(action):
        return (action.insert,)


def test_band_zero_newest_insert_runs_first():
    world = World()
    world.zone = "qeynos"
    queue = Schedule()
    older = Action()
    newer = Action()
    before = time.time()

    assert queue.append(older, world) is True
    assert queue.append(newer, world) is True

    assert older.insert < newer.insert
    assert older.zone == "qeynos"
    assert newer.zone == "qeynos"
    assert older.started >= before
    assert queue.winner() is newer


def test_higher_priority_wins_and_suspends_the_loser():
    world = World()
    queue = Schedule()
    grunt = Action()
    grunt.priority = 0
    fight = Action()
    fight.priority = 300

    queue.append(fight, world)
    queue.append(grunt, world)
    grunt.suspended = False

    winner = queue.winner()
    queue.suspend_loser(winner)

    assert winner is fight
    assert grunt.insert > fight.insert
    assert grunt.suspended is True
    assert fight.suspended is True


def test_same_band_uses_the_action_key():
    world = World()
    queue = Schedule()
    first = OlderFirst()
    second = OlderFirst()
    queue.append(first, world)
    queue.append(second, world)

    assert queue.winner() is first


def test_refused_source_does_not_take_an_insert():
    world = World()
    queue = Schedule()
    first = Action()
    first.source = "fetch:1"
    duplicate = Action()
    duplicate.source = "fetch:1"
    other = Action()
    other.source = "fetch:2"

    assert queue.append(first, world) is True
    assert queue.append(duplicate, world) is False
    assert queue.append(other, world) is True

    assert duplicate.insert == 0
    assert [action.source for action in queue] == ["fetch:1", "fetch:2"]
    assert other.insert == first.insert + 1
