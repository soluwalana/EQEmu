"""Opcode coverage for handlers/tasks.py."""

import struct

from eqclient3.handlers import tasks
from eqclient3.structs import OP_TaskActivity, OP_TaskSelectWindow
from support import (
    Loop,
    World,
    names,
    sources,
    task_activity,
    task_complete,
    task_window,
)


def _offer(short=False):
    steps = [
        (0, 4, "a guard", "", 1, "hail the guard"),
        (1, 2, "a bat", "", 1, "kill the bat"),
        (2, 3, "", "1001", 2, "loot the bone"),
    ]
    code = 1 if short else 0
    return task_window(8, [(15, code, "A Lesson", "Learn the yard.", steps)])


def test_opcodes():
    world = World(zone="qeynos")
    loop = Loop()
    tasks.TasksHandler().handle("OP_TaskSelectWindow", _offer(), world, loop)
    assert world.tasks.title == "A Lesson"
    assert world.tasks.description == "Learn the yard."
    assert len(world.tasks.activities) == 3
    assert loop.sent[0][0] == "OP_AcceptNewTask"
    assert names(loop) == ["Talk", "Kill", "Fetch"]
    assert sources(loop) == ["task:15:0", "task:15:1", "task:15:2"]
    assert all(action.priority == 0 for action in loop.queue)
    assert loop.queue[0].task_text == "hail the guard"
    assert loop.queue[2].item_id == 1001 and loop.queue[2].count == 2

    short = World(zone="qeynos")
    quiet = Loop()
    tasks.TasksHandler().handle("OP_TaskSelectWindow", _offer(short=True), short, quiet)
    assert short.tasks.title == "A Lesson"
    assert short.tasks.activities[0].locked is True
    assert quiet.queue == []

    tutorial = World(zone="tutorialb")
    stored = Loop()
    tasks.TasksHandler().handle("OP_TaskSelectWindow", _offer(), tutorial, stored)
    assert tutorial.tasks.title == "A Lesson"
    assert len(tutorial.tasks.activities) == 3
    assert names(stored) == ["Talk", "Kill", "Fetch"]
    assert sources(stored) == ["task:15:0", "task:15:1", "task:15:2"]
    assert [opcode for opcode, _payload in stored.sent] == ["OP_AcceptNewTask"]

    tasks.TasksHandler().handle(
        "OP_TaskActivity",
        task_activity(15, 1, 2, "a giant bat", "", 3, "kill the giant bat", done=1),
        world,
        loop,
    )
    updated = next(row for row in world.tasks.activities if row.activity_id == 1)
    assert updated.target_name == "a giant bat"
    assert updated.done == 1
    assert names(loop) == ["Talk", "Kill", "Fetch"]

    tasks.TasksHandler().handle("OP_TaskActivityComplete", task_complete(15, 1), world, loop)
    assert updated.done >= updated.goal
    assert names(loop) == ["Talk", "Kill", "Fetch"]
    task_type, task_id, master = struct.unpack("<III", loop.sent[0][1])
    assert (task_type, task_id, master) == (0, 15, 8)


def test_every_offer_on_the_window_is_queued():
    first = [
        (0, 4, "Guard Rahtiz", "", 1, "hail the guard"),
    ]
    second = [
        (0, 2, "a spider", "", 4, "kill the spiders"),
    ]
    window = task_window(
        9,
        [
            (5032, 0, "Arachnida", "Clear the spiders.", first),
            (5091, 0, "Vermin", "Clear the nests.", second),
        ],
    )
    world = World(zone="tutorialb")
    loop = Loop()
    tasks.TasksHandler().handle("OP_TaskSelectWindow", window, world, loop)
    assert [opcode for opcode, _payload in loop.sent] == ["OP_AcceptNewTask", "OP_AcceptNewTask"]
    taken = [struct.unpack("<III", payload) for _opcode, payload in loop.sent]
    assert taken == [(0, 5032, 9), (0, 5091, 9)]
    assert names(loop) == ["Talk", "Kill"]
    assert sources(loop) == ["task:5032:0", "task:5091:0"]
    assert [row.task_id for row in world.tasks.activities] == [5032, 5091]


def _cstr(text: str) -> bytes:
    return text.encode("latin1") + b"\x00"


def _lenstr(text: str) -> bytes:
    raw = text.encode("latin1")
    return struct.pack("<I", len(raw)) + raw


def test_rof2_select_window_matches_tasks_writer():
    """Bytes written by TaskInformation::SerializeSelector, not by our own serialize."""
    packet = struct.pack("<III", 1, 2, 9)
    packet += struct.pack("<IfII", 5166, 1.0, 0, 0)
    packet += _cstr("The Rare Flower") + _cstr("Bring the bloom from gloomingdeep.")
    packet += struct.pack("<BI", 0, 1)
    packet += struct.pack("<iii", 0, 4, 0)
    packet += _cstr("Guard Rahtiz")
    packet += _lenstr("")
    packet += struct.pack("<i", 1)
    packet += _lenstr("-1")
    packet += _lenstr("0")
    packet += _cstr("188")
    packet += _cstr("hail the guard")
    packet += _cstr("188")

    window = OP_TaskSelectWindow.deserialize(packet)
    assert window.task_type == 2 and window.giver == 9
    task = window.tasks[0]
    assert task.task_id == 5166 and task.title == "The Rare Flower"
    element = task.elements[0]
    assert element.activity_id == 0 and element.kind == 4
    assert element.target == "Guard Rahtiz" and element.goal == 1 and element.zone_id == 188
    assert element.skill == -1 and element.description == "hail the guard"
    again = OP_TaskSelectWindow.deserialize(window.serialize())
    assert again.tasks[0].elements[0].target == "Guard Rahtiz"

    activity = OP_TaskActivity.deserialize(
        struct.pack("<IIIII", 0, 2, 5166, 0, 0)
        + struct.pack("<iBi", 4, 0, 0)
        + _cstr("Guard Rahtiz")
        + _lenstr("")
        + struct.pack("<i", 1)
        + _lenstr("-1")
        + _lenstr("0")
        + _cstr("188")
        + struct.pack("<i", 0)
        + _cstr("hail the guard")
        + struct.pack("<iB", 1, 1)
        + _cstr("188")
    )
    assert activity.task_id == 5166 and activity.kind == 4 and activity.done == 1
    assert activity.target == "Guard Rahtiz" and activity.zone_id == 188
