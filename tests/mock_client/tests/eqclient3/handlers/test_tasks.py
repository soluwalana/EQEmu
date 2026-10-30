"""Opcode coverage for handlers/tasks.py."""

from eqclient3.handlers import tasks
from support import Loop, World, names, sources, task_activity, task_complete, task_window


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
    assert stored.queue == [] and stored.sent == []

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
