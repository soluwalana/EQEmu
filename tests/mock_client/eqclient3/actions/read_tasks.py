"""Band 0, durable. Read the stored task book in tutorialb and append the open steps.

A channel, special, or simple line that names work is heard here, while this
action is waiting in the mine. A saylink in that line is a reply for Talk, not
a new step.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.action import Message
    from eqclient3.loop import Loop
    from eqclient3.world import World

import re
from eqclient3.action import Action
from eqclient3.actions.deliver import Deliver
from eqclient3.actions.fetch import Fetch
from eqclient3.actions.kill import Kill
from eqclient3.actions.level_up import queue_level_gear
from eqclient3.actions.pickup import Pickup
from eqclient3.actions.talk import Talk
from eqclient3.actions.zone import Zone
from eqclient3.actions.support import (
    COLLECT,
    DELIVER,
    KILL,
    LOOT,
    SPEAK,
    character_name,
    line_of,
    mark_tutorial,
    new_zone_name,
    next_zoneline,
    task_activities,
    yield_to,
)
from eqclient3.quests.produce import produce
from eqclient3.handlers.common import mob_named, tutorial_done
from eqclient3.handlers.tasks import Activity
from eqclient3.inventory.assign import release_cursor
from eqclient3.struct_helpers import saylink_plain

_KINDS = (
    (re.compile(r"\bkill\s+(?:the\s+)?(.+)", re.IGNORECASE), "kill"),
    (re.compile(r"\bhail\s+(?:the\s+)?(.+)", re.IGNORECASE), "talk"),
    (re.compile(r"\b(?:say|talk)\s+(?:to\s+)?(?:the\s+)?(.+)", re.IGNORECASE), "talk"),
    (re.compile(r"\b(?:fetch|loot)\s+(?:the\s+)?(.+)", re.IGNORECASE), "fetch"),
    (re.compile(r"\b(?:deliver|hand|give)\s+(.+)", re.IGNORECASE), "deliver"),
    (re.compile(r"\bpick\s*up\s+(?:the\s+)?(.+)", re.IGNORECASE), "pickup"),
    (re.compile(r"\bzone\s+(?:to\s+)?(.+)", re.IGNORECASE), "zone"),
)


class ReadTasks(Action):

    def __init__(self) -> None:
        super().__init__()
        self.priority = 0
        self.durable = True
        self.seen: list[tuple[int, int]] = []

    def opcodes(self) -> tuple[str, ...]:
        return ("OP_NewZone", "OP_ChannelMessage", "OP_SpecialMesg", "OP_SimpleMessage")

    def suspend(self) -> None:
        self.suspended = True

    def _hear(self, loop: Loop, world: World) -> None:
        """A line that names work is taken on the pulse it arrives, even when this step is waiting."""
        self._listen(loop, world)

    def step(self, loop: Loop, world: World) -> None:
        message = self.consume("OP_NewZone")
        zone = new_zone_name(message, world) if message else world.zone
        if message and zone and zone != "tutorialb":
            mark_tutorial(loop, world)
            queue_level_gear(loop, world)
            produce(loop, world, leaving_tutorial=True)
            self.complete = True
            return
        if world.zone and world.zone != "tutorialb":
            mark_tutorial(loop, world)
            queue_level_gear(loop, world)
            produce(loop, world, leaving_tutorial=True)
            self.complete = True
            return
        self.suspended = False
        if self._listen(loop, world):
            return
        for activity in task_activities(world):
            if activity.locked:
                continue
            if activity.done >= (activity.goal or 1):
                continue
            key = (int(activity.task_id), int(activity.activity_id))
            source = f"task:{key[0]}:{key[1]}"
            queue = loop.queue
            if queue is not None and any(action.source == source for action in queue):
                # A find hunt is priority -1. This book and the talk that started
                # it have to sit under that hunt, then the talk comes back to hand
                # the item over once the hunt leaves the queue.
                if _side_hunt(loop):
                    self.priority = -2
                else:
                    self.priority = 0
                    for queued in queue:
                        if queued.source == source and queued.priority < 0:
                            queued.priority = 0
                self.yielding = True
                return
            # A step the book still lists is queued again. A resolved journal row is cleared.
            action = _action_for(activity)
            if not action:
                continue
            _reopen(loop, world, source)
            if yield_to(self, loop, world, action, source):
                if key not in self.seen:
                    self.seen.append(key)
                self.yielding = True
                return
        if _side_hunt(loop):
            self.priority = -1
            self.yielding = True
            return
        self.priority = 0
        self._when_idle(loop, world)

    def _when_idle(self, loop: Loop, world: World) -> None:
        """Hobart assigns the battle. With nothing left open, the exit rock leaves the mine."""
        if not _said(loop, world, "Guard Hobart", "hail"):
            if _open(loop, "hail:hobart"):
                self.yielding = True
                return
            talk = Talk(0, "hail", "Hail Guard Hobart")
            talk.bind_name = "Guard Hobart"
            if yield_to(self, loop, world, talk, "hail:hobart"):
                return
        point = next_zoneline(world, "freportw")
        if point is None:
            return
        path = world.movement.plan(point, "run")
        world.movement.advance(loop, world, path)

    def _listen(self, loop: Loop, world: World) -> bool:
        if str(world.zone or "").lower() != "tutorialb" or tutorial_done(loop, world):
            while (
                self.consume("OP_ChannelMessage") or self.consume("OP_SpecialMesg") or self.consume("OP_SimpleMessage")
            ):
                pass
            return False
        heard = False
        while True:
            message = (
                self.consume("OP_ChannelMessage") or self.consume("OP_SpecialMesg") or self.consume("OP_SimpleMessage")
            )
            if not message:
                return heard
            text, speaker = _line(message)
            who = character_name(loop, world).lower()
            if who and speaker and speaker.lower() == who:
                continue
            if "on your cursor" in text.lower():
                release_cursor(loop, world)
                heard = True
                continue
            for kind, subject in _named(text):
                _append(self, loop, world, kind, subject, text, speaker)
                heard = True


def _action_for(activity: Activity) -> Action | None:
    if activity.ground:
        return Pickup(activity.drop_id, activity.point)
    text = activity.text or activity.description
    if activity.kind == SPEAK:
        if not activity.npc and not text and not activity.target_name:
            return None
        talk = Talk(activity.npc, "hail", text)
        talk.bind_name = activity.target_name or ""
        return talk
    if activity.kind == KILL:
        return Kill(spawn_id=activity.spawn_id or None, camp=activity.target_name or None)
    if activity.kind in (LOOT, DELIVER, COLLECT):
        return Fetch(activity.item_id, activity.goal or 1, text)
    return None


def _line(message: Message) -> tuple[str, str]:
    speaker, text = line_of(message.payload)
    return (text, speaker)


# A saylink is a reply for the talk already running. The brackets around it are
# not part of a "say …" order, so the link is removed before the patterns run.
_WRAPPED_LINK = re.compile(r"\[?\x12.{56}[^\x12]*?\x12\]?")


def _named(text: str) -> list[tuple[str, str]]:
    plain = saylink_plain(_WRAPPED_LINK.sub(" ", text or ""))
    found: list[tuple[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for pattern, kind in _KINDS:
        match = pattern.search(plain)
        if match is None:
            continue
        subject = match.group(1).strip(" .\"'")
        if not subject:
            continue
        key = (kind, subject.lower())
        if key in seen:
            continue
        seen.add(key)
        found.append(key)
    return found


def _said(loop: Loop, world: World, npc: str, text: str) -> bool:
    journal = loop.journal
    who = character_name(loop, world)
    zone = str(world.zone or "")
    if journal is None or not who or not zone:
        return False
    want_npc = npc.lower()
    want_text = text.lower()
    for name, line in journal.said(who, zone):
        if str(name).lower() == want_npc and str(line).lower() == want_text:
            return True
    return False


def _side_hunt(loop: Loop) -> bool:
    """A find-item hunt is underway. The exit waits until that hunt is done."""
    queue = loop.queue
    if queue is None:
        return False
    return any(str(action.source).startswith("find:") and not action.complete for action in queue)


def _open(loop: Loop, source: str) -> bool:
    queue = loop.queue
    if queue is None:
        return False
    return any(action.source == source and not action.complete for action in queue)


def _reopen(loop: Loop, world: World, source: str) -> None:
    """Drop a resolved row so an activity that is still open can be queued again."""
    journal = loop.journal
    who = character_name(loop, world)
    if journal is None or not who or not source:
        return
    if journal.is_resolved(who, source):
        journal.clear_source(who, source)


def _append(
    parent: ReadTasks,
    loop: Loop,
    world: World,
    kind: str,
    subject: str,
    text: str,
    speaker: str,
) -> None:
    source = f"chat:{kind}:{subject.lower()}"
    _reopen(loop, world, source)
    action: Action
    if kind == "talk":
        npc = _npc(world, subject) or _npc(world, speaker)
        action = Talk(npc, subject, text)
        action.description = text
        yield_to(parent, loop, world, action, source)
    elif kind == "kill":
        spawn_id = _npc(world, subject)
        action = Kill(spawn_id or None, None if spawn_id else subject, None)
        action.description = text
        action.task_text = text
        yield_to(parent, loop, world, action, source)
    elif kind == "fetch":
        action = Fetch(_item_id(subject), 1, text)
        action.description = text
        yield_to(parent, loop, world, action, source)
    elif kind == "deliver":
        item_name, npc_name = _deliver(subject)
        npc = _npc(world, npc_name)
        action = Deliver(_item_id(item_name), npc if npc else npc_name)
        action.description = text
        yield_to(parent, loop, world, action, source)
    elif kind == "pickup":
        drop_id, point = _ground(world, subject)
        action = Pickup(drop_id, point)
        action.description = text
        yield_to(parent, loop, world, action, source)
    elif kind == "zone":
        yield_to(parent, loop, world, Zone(subject), source)


def _npc(world: World, name: str) -> int:
    mob = mob_named(world, name)
    if mob is None:
        return 0
    return int(mob.id or 0)


def _item_id(subject: str) -> int:
    match = re.search(r"\d+", subject or "")
    return int(match.group(0)) if match else 0


def _deliver(subject: str) -> tuple[str, str]:
    match = re.search(r"(.+?)\s+to\s+(.+)", subject, re.IGNORECASE)
    if match is None:
        return (subject, "")
    return (match.group(1).strip(), match.group(2).strip(" ."))


def _ground(world: World, subject: str) -> tuple[int, tuple[float, float, float]]:
    want = subject.lower()
    for row in world.ground.values():
        name = row.name.lower()
        if want in name or name in want:
            return (int(row.id), (float(row.x), float(row.y), float(row.z)))
    return (0, (0.0, 0.0, 0.0))
