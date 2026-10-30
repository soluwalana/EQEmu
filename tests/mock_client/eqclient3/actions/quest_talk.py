"""One conversation with a quest npc.

The steps are the say, the hand-in, and the item the script gives along the way.
Each say waits for the npc to answer before the next line. A hand-in spawns a
Trade once this mob is targeted. expect is the item that ends the conversation.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import World

from eqclient3.action import Action
from eqclient3.actions.support import HAIL, character_name, line_of, send_command, walk, yield_to
from eqclient3.actions.trade import Trade
from eqclient3.handlers.common import mob_named


@dataclass(frozen=True)
class Say:
    word: str


@dataclass(frozen=True)
class Hand:
    item: int


@dataclass(frozen=True)
class Receive:
    item: int


Turn = Say | Hand | Receive


class QuestTalk(Action):

    def __init__(self, npc: str, steps: tuple[Turn, ...], *, expect: int = 0) -> None:
        super().__init__()
        self.priority = 280
        self.durable = True
        self.npc = npc
        self.steps = steps
        self.expect = expect
        self.cursor = 0
        self.sent = False
        self.handed = False
        self.active_path = None

    def opcodes(self) -> tuple[str, ...]:
        return ("OP_Consider", "OP_ChannelMessage", "OP_SpecialMesg", "OP_SimpleMessage")

    def suspend(self) -> None:
        self.active_path = None
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        if self.expect and world.held(self.expect) > 0:
            self.complete = True
            return
        if self.cursor >= len(self.steps):
            if not self.expect:
                self.complete = True
            return
        if self.waiting_for("SAY"):
            if self._heard(loop, world):
                self.unwait("SAY")
                self._advance()
            return
        turn = self.steps[self.cursor]
        if isinstance(turn, Receive):
            if world.held(turn.item) > 0:
                self._advance()
            return
        self._bind(world)
        super().step(loop, world)
        if self.waiting_for("TARGET") or not self.target_id:
            return
        mob = world.mobs.get(self.target_id)
        if not mob or not mob.targeted:
            return
        if mob.distance > HAIL:
            walk(self, loop, world, mob.position, "run")
            return
        if isinstance(turn, Say):
            self._say(loop, turn.word, mob.spoken_name())
            return
        if isinstance(turn, Hand):
            self._hand(loop, world, turn.item)

    def _say(self, loop: Loop, word: str, name: str) -> None:
        if self.sent:
            return
        send_command(loop, _spoken(word, name))
        self.sent = True
        self.waited = 0
        self.wait("SAY")
        self.suspended = False

    def _hand(self, loop: Loop, world: World, item: int) -> None:
        """Trade this item once the mob is targeted. The next hand follows immediately."""
        if world.held(item) <= 0:
            return
        if self._trade_pending(loop, item):
            self.yielding = True
            return
        if self.handed:
            nxt = self.steps[self.cursor + 1] if self.cursor + 1 < len(self.steps) else None
            if isinstance(nxt, Hand):
                self.cursor += 1
                self.handed = False
                return
            self.wait("SAY")
            return
        trade = Trade(self.target_id, item)
        if yield_to(self, loop, world, trade, f"{self.source}#trade:{item}"):
            self.handed = True

    def _trade_pending(self, loop: Loop, item: int) -> bool:
        queue = loop.queue
        if queue is None:
            return False
        source = f"{self.source}#trade:{item}"
        for action in queue:
            if isinstance(action, Trade) and action.source == source and not action.complete:
                return True
        return False

    def _advance(self) -> None:
        self.cursor += 1
        self.sent = False
        self.handed = False
        if self.cursor >= len(self.steps) and not self.expect:
            self.complete = True

    def _bind(self, world: World) -> None:
        if self.target_id:
            return
        mob = mob_named(world, self.npc)
        if not mob:
            return
        self.target_id = int(mob.id)

    def _heard(self, loop: Loop, world: World) -> bool:
        who = character_name(loop, world).lower()
        for opcode in ("OP_ChannelMessage", "OP_SpecialMesg", "OP_SimpleMessage"):
            while True:
                message = self.consume(opcode)
                if not message:
                    break
                speaker, _text = line_of(message.payload)
                if who and speaker and speaker.lower() == who:
                    continue
                return True
        return False


def _spoken(word: str, name: str) -> str:
    """A hail names the npc. Any other graph word is the script match, said as stored."""
    text = word.strip()
    if text.lower() != "hail":
        return text
    spoken = " ".join(name.replace("_", " ").split())
    if not spoken:
        return text
    return f"Hail, {spoken}"
