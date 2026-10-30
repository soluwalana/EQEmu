"""Hail an npc. Standing 8 or 9 starts a fight or a soulbind, by the level gap."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import Mob, World

import re
from eqclient3.action import Action
from eqclient3.actions.attack import Attack
from eqclient3.actions.support import HAIL, SPEAK, mark_tutorial, message_text, send_command, simple_id, soulbinder, standing_of, task_activities, walk, yards, yield_to
from eqclient3.handlers.common import attack_for, character_name, mark_fight, mob_named

_HAIL_NAME = re.compile(r'hail\s+(?:the\s+)?([A-Za-z][A-Za-z\']*)', re.IGNORECASE)

class Talk(Action):

    def __init__(self, npc: int, line: str, task_text: str, priority: int=0) -> None:
        super().__init__()
        self.priority = priority
        self.npc = npc
        self.target_id = int(npc) if isinstance(npc, int) else 0
        self.line = line
        self.task_text = task_text or ''
        self.active_path = None
        self.sent = False
        self.stride = None
        self.followed = False
        self.satisfied = False
        self.finishes_tutorial = False
        self.pad: tuple[float, float, float] | None = None
        self.bind_name = ""

    def opcodes(self) -> tuple[object, ...]:
        return ('OP_Consider', 'OP_ChannelMessage', 'OP_SpecialMesg', 'OP_SimpleMessage')

    def suspend(self) -> None:
        self.active_path = None
        self.suspended = True

    def task_text_satisfied(self) -> bool:
        if self.satisfied:
            return True
        # "Hail Absor and Learn About Weapons" is the objective, not a line the npc will say.
        if self.line == 'hail' and hail_name(self.task_text):
            self.satisfied = self.sent
            return self.sent
        if not self.task_text:
            self.satisfied = self.sent
            return self.sent
        needle = self.task_text.lower()
        heard = lambda message: needle in message_text(message).lower()
        for opcode in ('OP_ChannelMessage', 'OP_SpecialMesg', 'OP_SimpleMessage'):
            if self.consume(opcode, heard):
                self.satisfied = True
                return True
        return False

    def step(self, loop: Loop, world: World) -> None:
        self._bind_hail_target(world)
        self._shorter_stride()
        super().step(loop, world)

        if self.waiting_for('HAIL'):
            if not self.task_text_satisfied():
                return
            self.unwait('HAIL')
            self._after_reply(loop, world)
            return
        
        if self.waiting_for('TARGET'):
            return

        if not self.target_id and self.bind_name and self.pad is not None and yards(world, self.pad) > HAIL:
            walk(self, loop, world, self.pad, self.stride or 'run')
            return

        if not self.target_id and not hail_name(self.task_text) and not self.task_text and not self.bind_name:
            self.complete = True
            return

        if not self.target_id and hail_name(self.task_text):
            return

        mob = world.mobs.get(self.target_id, None)
        if mob and standing_of(mob) in (8, 9):
            gap = int(mob.level or 0) - int(world.level or 1)
            
            if gap <= 10:
                self._attack(loop, world, mob)
                return
            
            append_soulbind(self, loop, world)
            return
        
        if mob and float(mob.distance) > HAIL:
            walk(self, loop, world, mob.position, self.stride or 'run')
            return
        
        if self.followed:
            self.complete = True
            return
        
        if not self.sent:
            self._say(loop)
            self.sent = True
            self.wait('HAIL')
            self.suspended = False
            return
        
        self._after_reply(loop, world)

    def _after_reply(self, loop: Loop, world: World) -> None:
        self.suspended = False
        if self.followed:
            self.complete = True
            return
        
        follow = world.follow_up
        if follow is not None and yield_to(self, loop, world, follow, follow.source or 'talk:follow'):
            self.followed = True
            return
        
        if self.finishes_tutorial or _ends_tutorial(world):
            _finish_tutorial(self, loop, world)
        
        self.followed = True
        self.complete = True

    def _bind_hail_target(self, world: World) -> None:
        if self.target_id:
            return
        name = self.bind_name or hail_name(self.task_text)
        if not name:
            return
        mob = mob_named(world, name)
        if mob is None:
            return
        self.npc = int(mob.id)
        self.target_id = int(mob.id)

    def _shorter_stride(self) -> None:
        if self.consume('OP_SimpleMessage', lambda message: simple_id(message) == 124):
            self.stride = 'walk'
            self.active_path = None

    def _say(self, loop: Loop) -> None:
        send_command(loop, self.line)

    def _attack(self, loop: Loop, world: World, mob: Mob) -> None:
        spawn = int(mob.id or 0)
        if not spawn or attack_for(loop, Attack, spawn):
            return
        attack = Attack(spawn)
        mark_fight(world, spawn)
        attack.level = int(mob.level or 0)
        yield_to(self, loop, world, attack, f'aggro:{spawn}')

def hail_name(text: str) -> str:
    match = _HAIL_NAME.search(str(text or '').strip())
    if match is None:
        return ''
    return match.group(1)

def _ends_tutorial(world: World) -> bool:
    """The hail that finishes the mine. An empty book is the window not arriving yet."""
    if str(world.zone or "").lower() != "tutorialb":
        return False
    activities = task_activities(world)
    if not activities:
        return False
    open_steps = []
    for activity in activities:
        if activity.locked:
            continue
        if int(activity.done or 0) < int(activity.goal or 1):
            open_steps.append(activity)
    if not open_steps:
        return True
    return len(open_steps) == 1 and int(open_steps[0].kind or 0) == SPEAK

def _finish_tutorial(talk: Talk, loop: Loop, world: World) -> None:
    """Close the open mine reader, then append the epic graph."""
    # expand constructs Talk, so produce stays local to this call.
    from eqclient3.quests.produce import produce
    for action in list(loop.queue):
        if type(action).__name__ == "ReadTasks" and not action.complete:
            action.complete = True
            journal = loop.journal
            who = character_name(loop, world)
            if journal is not None and who:
                journal.resolve_action(who, action)
    mark_tutorial(loop, world)
    produce(loop, world, leaving_tutorial=True)

def append_soulbind(parent: Action, loop: Loop, world: World) -> bool:
    binder = soulbinder(world)
    if binder is None:
        return False
    name = str(getattr(binder, 'name', '') or '')
    mob = mob_named(world, name) if name else None
    npc = int(mob.id) if mob is not None else 0
    talk = Talk(npc, 'hail', 'soulbind')
    talk.bind_name = name
    talk.pad = (float(binder.x), float(binder.y), float(binder.z))
    zone = str(getattr(binder, 'zone', '') or world.zone or '')
    return yield_to(parent, loop, world, talk, f'soulbind:{zone}')
