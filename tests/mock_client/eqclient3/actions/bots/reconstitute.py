"""^botlist, respawn the dead, read the heal rotation, then Rest."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.action import Message
    from eqclient3.loop import Loop
    from eqclient3.world import Bots, World

import re
from types import SimpleNamespace
from eqclient3.action import Action, _consider_id
from eqclient3.actions.bots.form import _READY
from eqclient3.actions.rest import Rest
from eqclient3.actions.support import message_text, yield_to, send_command
from eqclient3.handlers.common import mob_named
from eqclient3.struct_helpers import saylink_plain
from eqclient3.structs import OP_Consider, OP_TargetMouse
from eqclient3.world import Bot, Mob

_LEVEL = re.compile(r"([A-Za-z][\w']*)\s+is\s+a\s+level\b", re.IGNORECASE)
_LINK = re.compile(r"\x12.{56}([^\x12]+)\x12")


class Reconstitute(Action):

    def __init__(self, priority: int) -> None:
        super().__init__()
        self.priority = priority
        self.phase = "list"
        self.sent = False
        self.limit = 10
        self.tries = 0
        self._reply: Message | None = None
        self._spawn_name = ""

    def opcodes(self) -> tuple[str, ...]:
        return ("OP_ChannelMessage", "OP_SpecialMesg", "OP_Consider")

    def suspend(self) -> None:
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        bots = world.bots
        stamp = int(bots.reconstituted_at or 0)
        tick = int(loop.tick or 0)
        if stamp and self.phase == "list" and (not self.sent) and (0 <= tick - stamp < 20):
            # The roster was just rebuilt. Sitting is still the step this action owes.
            if not _resting(loop):
                self._sit(loop, world)
            self.complete = True
            return
        if self._wait(loop):
            return
        if self.tries >= 2:
            self._sit(loop, world)
            self.complete = True
            return
        if self.phase == "list":
            if not self.sent:
                bots.reconstituted_at = tick
                send_command(loop, "^botlist")
                self.sent = True
                self.wait("BOT")
                self.suspended = False
                return
            if self._reply is None:
                return
            reply = self._reply
            self._reply = None
            _merge(bots, _bots_from(reply))
            if not _list_done(reply):
                self.wait("BOT")
                return
            self.sent = False
            self.phase = "spawn" if _dead(bots) else "rotation"
        if self.phase == "spawn":
            dead = _dead(bots)
            if not dead:
                self.phase = "rotation"
            elif not self.sent:
                bot = dead[0]
                self._spawn_name = str(bot.name or "")
                send_command(loop, f"^botspawn {self._spawn_name}")
                self.sent = True
                self.wait("BOT")
                self.suspended = False
                return
            else:
                if self._reply is None:
                    return
                _mark_alive(bots, self._spawn_name)
                self._reply = None
                self.sent = False
                if _dead(bots):
                    return
                self.phase = "rotation"
        if self.phase == "rotation":
            if not self.sent:
                if not self._aimed(loop, world, bots):
                    return
                send_command(loop, f"^healrotationlist {_member_name(bots, self.target_id)}")
                self.sent = True
                self.wait("BOT")
                self.suspended = False
                return
            if self._reply is None:
                return
            text = message_text(self._reply)
            bots.rotation = [line for line in text.splitlines() if line] or ([text] if text else [])
            self._reply = None
            self._sit(loop, world)
            self.complete = True

    def _aimed(self, loop: Loop, world: World, bots: Bots) -> bool:
        """Target one spawned bot. The consider reply, or a short wait after it was asked, lands it."""
        mob = _member(world, bots)
        if mob is None:
            self.waited += 1
            if self.waited < 30:
                return False
            self.waited = 0
            self._sit(loop, world)
            self.complete = True
            return False
        if self.target_id != int(mob.id):
            self.target_id = int(mob.id)
            self.waited = 0
            self.unwait("TARGET")
            loop.send("OP_TargetMouse", OP_TargetMouse(int(mob.id) & 65535).serialize())
            spawn = int(world.self_id or 0)
            loop.send("OP_Consider", OP_Consider(spawn, int(mob.id)).serialize())
            self.wait("TARGET")
            return False
        reply = self.consume("OP_Consider")
        if reply is not None and _consider_id(reply) == int(self.target_id):
            mob.targeted = True
            self.unwait("TARGET")
            self.waited = 0
            return True
        self.waited += 1
        if self.waited < 10:
            return False
        mob.targeted = True
        self.unwait("TARGET")
        self.waited = 0
        return True

    def _sit(self, loop: Loop, world: World) -> None:
        who = world.name or "self"
        yield_to(self, loop, world, Rest(who), "rest:reconstitute")

    def _wait(self, loop: Loop) -> bool:
        if not self.waiting_for("BOT"):
            return False
        message = _prefer(self.phase, self.consume("OP_ChannelMessage"), self.consume("OP_SpecialMesg"))
        if message:
            self._reply = message
            self.waited = 0
            self.tries = 0
            self.unwait("BOT")
            return False
        self.waited += 1
        limit = self.limit
        if limit is None or self.waited < limit:
            return True
        # One more ask, then sit. A missed reply must not send ^botlist forever.
        self.waited = 0
        self.tries += 1
        self.sent = False
        self.unwait("BOT")
        self._reply = None
        return self.tries >= 2


def _resting(loop: Loop) -> bool:
    queue = loop.queue
    if queue is None:
        return False
    return any(not action.complete and str(action.source) == "rest:reconstitute" for action in queue)


def _bots_from(message: Message) -> list:
    payload = message.payload
    rows = None
    if isinstance(payload, dict):
        rows = payload.get("bots")
    if rows is None:
        rows = _parse(message_text(message))
    roster = []
    for row in rows or []:
        if isinstance(row, dict):
            roster.append(SimpleNamespace(**row))
        else:
            roster.append(row)
    return roster


def _prefer(phase: str, channel: Message | None, special: Message | None) -> Message | None:
    """The bot list arrives as a special message. A say of the command is not the reply."""
    for message in (special, channel):
        if message is not None and _for_phase(phase, message_text(message)):
            return message
    return None


def _for_phase(phase: str, text: str) -> bool:
    plain = saylink_plain(text or "").strip()
    lowered = plain.lower()
    if not plain or lowered.startswith("^"):
        return False
    if phase == "list":
        return " is a level" in lowered or "bots shown" in lowered
    if phase == "spawn":
        return _spawn_ack(lowered)
    if phase == "rotation":
        return "must" not in lowered or "target" not in lowered
    return True


def _spawn_ack(lowered: str) -> bool:
    """A spawn result. The rest of the bot list is not one."""
    if "is a level" in lowered or "bots shown" in lowered:
        return False
    if "saved" in lowered or "already spawned" in lowered or "failed to spawn" in lowered:
        return True
    if "don't own" in lowered or "do not own" in lowered:
        return True
    return any(line in lowered for line in _READY)


def _list_done(message: Message) -> bool:
    """The roster is complete. One 'Bot N' line is not the whole list."""
    payload = message.payload
    if isinstance(payload, dict) and payload.get("bots"):
        return True
    text = saylink_plain(message_text(message)).lower().lstrip()
    if "bots shown" in text:
        return True
    return " is a level" in text and not text.startswith("bot ")


def _merge(bots: Bots, rows: list) -> None:
    by_name = {str(bot.name).lower(): bot for bot in bots.roster if bot.name}
    for row in rows:
        name = str(row.name or "")
        if name:
            by_name[name.lower()] = row
    bots.roster = list(by_name.values())


def _member_name(bots: Bots, spawn_id: int) -> str:
    del spawn_id
    for bot in bots.roster:
        if bot.alive and bot.name:
            if _class_id(bot) == 2:
                return str(bot.name)
    for bot in bots.roster:
        if bot.alive and bot.name:
            return str(bot.name)
    return ""


def _parse(text: str) -> list:
    found = []
    for raw in (text or "").splitlines():
        line = saylink_plain(raw)
        match = _LEVEL.search(line)
        if match is None:
            continue
        name = match.group(1)
        lowered = line.lower()
        # The server wraps the name in a ^spawn link only while that bot is not in the zone.
        linked = _LINK.search(raw)
        absent = linked is not None and linked.group(1).strip().lower() == name.lower()
        alive = not absent and "dead" not in lowered and "not spawned" not in lowered
        found.append(SimpleNamespace(name=name, alive=alive, class_id=0, hp=0, max_hp=0, id=0))
    return found


def _class_id(bot: Bot) -> int:
    if isinstance(bot, Bot):
        return int(bot.class_id)
    return 0


def _member(world: World, bots: Bots) -> Mob | None:
    """A bot that is already in the zone. A cleric is the heal rotation's member."""
    names = [str(bot.name) for bot in bots.roster if bot.alive and bot.name]
    clerics = [str(bot.name) for bot in bots.roster if bot.alive and bot.name and _class_id(bot) == 2]
    for name in clerics + names:
        mob = mob_named(world, name)
        if mob is not None and not mob.dead:
            return mob
    return None


def _dead(bots: Bots) -> list[Bot]:
    return [bot for bot in bots.roster if not bot.alive]


def _mark_alive(bots: Bots, name: str) -> None:
    for bot in bots.roster or []:
        if str(bot.name) == name:
            bot.alive = True
