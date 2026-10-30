"""Band 0, durable. Read the stored task book in tutorialb and append the open steps.

A channel or simple line that names work is heard here, while this action is
waiting in the mine.
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
from eqclient3.actions.pickup import Pickup
from eqclient3.actions.talk import Talk
from eqclient3.actions.zone import Zone
from eqclient3.actions.support import DELIVER, KILL, LOOT, SPEAK, line_of, mark_tutorial, new_zone_name, task_activities, yield_to
from eqclient3.quests.produce import produce
from eqclient3.handlers.common import mob_named, tutorial_done
from eqclient3.handlers.tasks import Activity
from eqclient3.struct_helpers import saylink_plain, saylink_words

_KINDS = (
    (re.compile(r'\bkill\s+(?:the\s+)?(.+)', re.IGNORECASE), 'kill'),
    (re.compile(r'\bhail\s+(?:the\s+)?(.+)', re.IGNORECASE), 'talk'),
    (re.compile(r'\b(?:say|talk)\s+(?:to\s+)?(?:the\s+)?(.+)', re.IGNORECASE), 'talk'),
    (re.compile(r'\b(?:fetch|loot)\s+(?:the\s+)?(.+)', re.IGNORECASE), 'fetch'),
    (re.compile(r'\b(?:deliver|hand|give)\s+(.+)', re.IGNORECASE), 'deliver'),
    (re.compile(r'\bpick\s*up\s+(?:the\s+)?(.+)', re.IGNORECASE), 'pickup'),
    (re.compile(r'\bzone\s+(?:to\s+)?(.+)', re.IGNORECASE), 'zone'),
)

class ReadTasks(Action):

    def __init__(self) -> None:
        super().__init__()
        self.priority = 0
        self.durable = True
        self.seen = []

    def opcodes(self) -> tuple[str, ...]:
        return ('OP_NewZone', 'OP_ChannelMessage', 'OP_SimpleMessage')

    def suspend(self) -> None:
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        message = self.consume('OP_NewZone')
        zone = new_zone_name(message, world) if message else world.zone
        if message and zone and zone != 'tutorialb':
            mark_tutorial(loop, world)
            produce(loop, world)
            self.complete = True
            return
        if world.zone and world.zone != 'tutorialb':
            mark_tutorial(loop, world)
            produce(loop, world)
            self.complete = True
            return
        self.suspended = False
        self._hear(loop, world)
        pushed = False
        for activity in task_activities(world):
            if activity.locked:
                continue
            if activity.done >= (activity.goal or 1):
                continue
            key = activity.activity_id or id(activity)
            source = f'task:{key}'
            if key in self.seen or any((action.source == source for action in loop.queue)):
                continue
            action = _action_for(activity)
            if not action:
                continue
            if yield_to(self, loop, world, action, source):
                self.seen.append(key)
                pushed = True
        if pushed:
            self.yielding = True

    def _hear(self, loop: Loop, world: World) -> None:
        if str(world.zone or '').lower() != 'tutorialb' or tutorial_done(loop, world):
            while self.consume('OP_ChannelMessage') or self.consume('OP_SimpleMessage'):
                pass
            return
        while True:
            message = self.consume('OP_ChannelMessage') or self.consume('OP_SimpleMessage')
            if not message:
                return
            text, speaker = _line(message)
            for kind, subject in _named(text):
                _append(self, loop, world, kind, subject, text, speaker)

def _action_for(activity: Activity) -> Action | None:
    if activity.ground:
        return Pickup(activity.drop_id, tuple(activity.point))
    text = activity.text or activity.description
    if activity.kind == SPEAK:
        if not activity.npc and not text and not activity.target_name:
            return None
        return Talk(activity.npc, "hail", text)
    if activity.kind == KILL:
        return Kill(spawn_id=activity.spawn_id or None, camp=activity.target_name or None)
    if activity.kind in (LOOT, DELIVER):
        return Fetch(activity.item_id, activity.goal or 1, text)
    return None

def _line(message: Message) -> tuple[str, str]:
    speaker, text = line_of(message.payload)
    return (text, speaker)

def _named(text: str) -> list[tuple[str, str]]:
    plain = saylink_plain(text or '')
    found: list[tuple[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for word in saylink_words(text or ''):
        key = ('talk', word.lower())
        if key not in seen:
            seen.add(key)
            found.append(key)
    for pattern, kind in _KINDS:
        match = pattern.search(plain)
        if match is None:
            continue
        subject = match.group(1).strip(' ."\'')
        if not subject:
            continue
        key = (kind, subject.lower())
        if key in seen:
            continue
        seen.add(key)
        found.append(key)
    return found

def _append(parent: ReadTasks, loop: Loop, world: World, kind: str, subject: str, text: str, speaker: str) -> None:
    source = f'chat:{kind}:{subject.lower()}'
    if kind == 'talk':
        npc = _npc(world, subject) or _npc(world, speaker)
        action = Talk(npc, subject, text)
        action.description = text
        yield_to(parent, loop, world, action, source)
    elif kind == 'kill':
        spawn_id = _npc(world, subject)
        action = Kill(spawn_id or None, None if spawn_id else subject, None)
        action.description = text
        action.task_text = text
        yield_to(parent, loop, world, action, source)
    elif kind == 'fetch':
        action = Fetch(_item_id(subject), 1, text)
        action.description = text
        yield_to(parent, loop, world, action, source)
    elif kind == 'deliver':
        item, npc_name = _deliver(subject)
        action = Deliver(item, _npc(world, npc_name) or npc_name)
        action.description = text
        yield_to(parent, loop, world, action, source)
    elif kind == 'pickup':
        drop_id, point = _ground(world, subject)
        action = Pickup(drop_id, point)
        action.description = text
        yield_to(parent, loop, world, action, source)
    elif kind == 'zone':
        yield_to(parent, loop, world, Zone(subject), source)

def _npc(world: World, name: str) -> int:
    mob = mob_named(world, name)
    if mob is None:
        return 0
    return int(mob.id or 0)

def _item_id(subject: str) -> int:
    match = re.search(r'\d+', subject or '')
    return int(match.group(0)) if match else 0

def _deliver(subject: str) -> tuple[str, str]:
    match = re.search(r'(.+?)\s+to\s+(.+)', subject, re.IGNORECASE)
    if match is None:
        return (subject, '')
    return (match.group(1).strip(), match.group(2).strip(' .'))

def _ground(world: World, subject: str) -> tuple[int, tuple[float, float, float]]:
    want = subject.lower()
    for row in world.ground.values():
        name = row.name.lower()
        if want in name or name in want:
            return (int(row.id), (float(row.x), float(row.y), float(row.z)))
    return (0, (0.0, 0.0, 0.0))
