"""^botlist, respawn the dead, read the heal rotation, then Rest."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.action import Message
    from eqclient3.loop import Loop
    from eqclient3.world import Bot, Bots, World

from types import SimpleNamespace
from eqclient3.action import Action
from eqclient3.actions.rest import Rest
from eqclient3.actions.support import message_text, yield_to, send_command


class Reconstitute(Action):

    def __init__(self, priority: int) -> None:
        super().__init__()
        self.priority = priority
        self.phase = "list"
        self.sent = False
        self.limit = 10
        self._reply: Message | None = None
        self._spawn_name = ""

    def opcodes(self) -> tuple[str, ...]:
        return ("OP_ChannelMessage",)

    def suspend(self) -> None:
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        bots = world.bots
        stamp = int(bots.reconstituted_at or 0)
        tick = int(loop.tick or 0)
        if stamp and self.phase == "list" and (not self.sent) and (0 <= tick - stamp < 20):
            self.complete = True
            return
        if self._wait(loop):
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
            bots.roster = _bots_from(self._reply)
            self._reply = None
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
                send_command(loop, "^healrotationlist")
                self.sent = True
                self.wait("BOT")
                self.suspended = False
                return
            if self._reply is None:
                return
            text = message_text(self._reply)
            bots.rotation = [line for line in text.splitlines() if line] or ([text] if text else [])
            self._reply = None
            who = world.name or "self"
            yield_to(self, loop, world, Rest(who), "rest:reconstitute")
            self.complete = True

    def _wait(self, loop: Loop) -> bool:
        if not self.waiting_for("BOT"):
            return False
        message = self.consume("OP_ChannelMessage")
        if message:
            self._reply = message
            self.waited = 0
            self.unwait("BOT")
            return False
        self.waited += 1
        limit = self.limit
        if limit is None or self.waited < limit:
            return True
        self.waited = 0
        self.sent = False
        self.unwait("BOT")
        self._reply = None
        return False


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


def _parse(text: str) -> list:
    found = []
    for line in (text or "").splitlines():
        parts = line.split()
        if len(parts) < 5 or parts[1].lower() != "is":
            continue
        name = parts[0]
        lowered = line.lower()
        alive = "dead" not in lowered and "not spawned" not in lowered
        found.append(SimpleNamespace(name=name, alive=alive, class_id=0, hp=0, max_hp=0, id=0))
    return found


def _dead(bots: Bots) -> list[Bot]:
    return [bot for bot in bots.roster if not bot.alive]


def _mark_alive(bots: Bots, name: str) -> None:
    for bot in bots.roster or []:
        if str(bot.name) == name:
            bot.alive = True
