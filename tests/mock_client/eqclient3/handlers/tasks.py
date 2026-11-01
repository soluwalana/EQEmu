"""Task windows. Every offer on the window is accepted and its steps are queued.

A short offer stays in the book and is not taken.
"""

from __future__ import annotations

import re
from eqclient3.action import Action
from eqclient3.actions.fetch import Fetch
from eqclient3.actions.kill import Kill
from eqclient3.actions.talk import Talk
from eqclient3.handlers.common import mob_named, enqueue_once
from eqclient3.structs import (
    EQStruct,
    OP_AcceptNewTask,
    OP_TaskActivity,
    OP_TaskActivityComplete,
    OP_TaskSelectWindow,
)
from eqclient3.handler import Handler

SPEAK = 4
KILL = 2
LOOT = 3
DELIVER = 1
COLLECT = 13
SHORT = 1


class Activity:

    def __init__(
        self,
        task_id: int,
        activity_id: int,
        kind: int,
        target_name: str,
        item_list: str,
        description: str,
        goal: int,
        done: int = 0,
        locked: bool = False,
    ) -> None:
        self.task_id = task_id
        self.activity_id = activity_id
        self.kind = kind
        self.target_name = target_name or ""
        self.item_list = item_list or ""
        self.description = description or ""
        self.text = self.description
        self.goal = max(goal or 1, 1)
        self.done = max(done or 0, 0)
        self.locked = locked
        self.optional = False
        self.zone_id = 0
        self.ground = False
        self.drop_id = 0
        self.point: tuple[float, float, float] = (0.0, 0.0, 0.0)
        self.npc = 0
        self.spawn_id = 0
        self.item_id = _first_id(self.item_list)

    @property
    def finished(self) -> bool:
        return self.done >= self.goal


class Book:

    def __init__(self) -> None:
        self.title = ""
        self.description = ""
        self.activities: list[Activity] = []


class TasksHandler(Handler):
    opcodes = ("OP_TaskSelectWindow", "OP_TaskActivity", "OP_TaskActivityComplete")

    def on(self, opcode: str, payload: EQStruct) -> None:
        del opcode
        if isinstance(payload, OP_TaskSelectWindow):
            self.window(payload)
        elif isinstance(payload, OP_TaskActivity):
            self.activity(payload)
        elif isinstance(payload, OP_TaskActivityComplete):
            self.complete(payload)

    def window(self, row: OP_TaskSelectWindow) -> None:
        book = self.book()
        stored = []
        accepted: set[int] = set()
        giver = int(row.giver or 0)
        for task in row.tasks:
            if task.title and not book.title:
                book.title = task.title
            if task.description and not book.description:
                book.description = task.description
            locked = task.duration_code == SHORT
            for element in task.elements:
                activity = Activity(
                    task.task_id,
                    element.activity_id,
                    element.kind,
                    element.target,
                    element.item_list,
                    element.description or task.description,
                    element.goal,
                    locked=locked,
                )
                activity.zone_id = element.zone_id
                _put(book, activity)
                if not locked:
                    stored.append((activity, giver))
            if locked or int(task.task_id) in accepted:
                continue
            self.loop.send(
                "OP_AcceptNewTask",
                OP_AcceptNewTask(int(task.task_id), giver, row.task_type).serialize(),
            )
            accepted.add(int(task.task_id))
        for activity, _master in stored:
            if not _is_step(activity):
                continue
            self.append_step(activity)

    def activity(self, row: OP_TaskActivity) -> None:
        book = self.book()
        if row.locked:
            current = _find(book, row.task_id, row.activity_id)
            if current and current.target_name and (not current.locked):
                return
            if not current:
                _put(
                    book,
                    Activity(row.task_id, row.activity_id, 0, "", "", "", 1, locked=True),
                )
            else:
                current.locked = True
            return
        activity = Activity(
            row.task_id,
            row.activity_id,
            row.kind,
            row.target,
            row.item_list,
            row.description,
            row.goal,
            row.done,
            locked=False,
        )
        activity.optional = bool(row.optional)
        activity.zone_id = row.zone_id
        _put(book, activity)

    def complete(self, row: OP_TaskActivityComplete) -> None:
        task_id, activity_id, stage_complete = (
            row.task_id,
            row.activity_id,
            row.stage_complete,
        )
        if not stage_complete:
            return
        book = self.book()
        activity = _find(book, task_id, activity_id)
        if not activity:
            activity = Activity(task_id, activity_id, 0, "", "", "", 1, done=1)
            book.activities.append(activity)
        activity.done = max(activity.done, activity.goal)

    def append_step(self, activity: Activity) -> None:
        world = self.world
        source = f"task:{activity.task_id}:{activity.activity_id}"
        description = activity.description or activity.target_name
        action: Action
        if activity.kind in (SPEAK, DELIVER):
            npc = 0
            mob = mob_named(world, activity.target_name)
            if mob:
                npc = mob.id
            line = "hail" if activity.kind == SPEAK else description
            action = Talk(npc, line, description)
            action.bind_name = activity.target_name or ""
        elif activity.kind == KILL:
            spawn_id = 0
            mob = mob_named(world, activity.target_name)
            if mob:
                spawn_id = mob.id
            action = Kill(spawn_id or None, None if spawn_id else activity.target_name, None)
        elif activity.kind in (LOOT, COLLECT):
            action = Fetch(_first_id(activity.item_list), activity.goal, description)
        else:
            return
        action.description = description
        action.task_text = description
        enqueue_once(self.loop, world, action, source)

    def book(self) -> Book:
        current = self.world.tasks
        if isinstance(current, Book):
            return current
        book = Book()
        self.world.tasks = book
        return book


def _is_step(activity: Activity) -> bool:
    if activity.locked or activity.optional or activity.finished:
        return False
    if activity.kind not in (SPEAK, KILL, LOOT, DELIVER, COLLECT):
        return False
    if activity.kind in (LOOT, COLLECT):
        return bool(activity.item_list or activity.target_name or activity.description)
    return bool(activity.target_name or activity.description)


def _put(book: Book, activity: Activity) -> None:
    current = _find(book, activity.task_id, activity.activity_id)
    if not current:
        book.activities.append(activity)
        return
    done = max(current.done, activity.done)
    activity.done = done
    if current.target_name and (not activity.target_name):
        activity.target_name = current.target_name
    index = book.activities.index(current)
    book.activities[index] = activity


def _find(book: Book, task_id: int, activity_id: int) -> Activity | None:
    for activity in book.activities:
        if activity.task_id == task_id and activity.activity_id == activity_id:
            return activity
    return None


def _first_id(item_list: str) -> int:
    match = re.search("\\d+", item_list or "")
    return int(match.group(0)) if match else 0
