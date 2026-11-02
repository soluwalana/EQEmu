"""One conversation with a quest npc.

A step says a line, hands an item, waits to receive an item, coin, or faction
change, or fetches an item the step needs. Each say waits for the npc to answer
before the next line. A hand-in spawns a Trade once this mob is targeted. A
needed item spawns a Fetch. expect ends the conversation early: an item, money,
or a faction change. An empty expect ends it when the last step is done.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import World

from eqclient3.action import Action
from eqclient3.actions.fetch import Fetch
from eqclient3.actions.support import (
    HAIL,
    character_name,
    in_tutorial,
    line_of,
    send_command,
    task_activities,
    walk,
    yield_to,
)
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


@dataclass(frozen=True)
class Need:
    """Fetch this item before the conversation continues."""

    item: int


@dataclass(frozen=True)
class Money:
    """Coin this step waits to receive. Zeroes mean any increase since the step started."""

    platinum: int = 0
    gold: int = 0
    silver: int = 0
    copper: int = 0


@dataclass(frozen=True)
class Faction:
    """Standing this step waits for. Positive is better, negative is worse."""

    faction: int
    delta: int


Turn = Say | Hand | Receive | Need | Money | Faction


@dataclass(frozen=True)
class ExpectItem:
    item: int


@dataclass(frozen=True)
class ExpectMoney:
    """Coin the npc pays. Zeroes mean any increase from the coin we had at the start."""

    platinum: int = 0
    gold: int = 0
    silver: int = 0
    copper: int = 0


@dataclass(frozen=True)
class ExpectFaction:
    """quest::faction delta. Positive is better standing, negative is worse."""

    faction: int
    delta: int


Expect = ExpectItem | ExpectMoney | ExpectFaction


def _book_open(world: World) -> bool:
    """A tutorial activity is still open, so the mine book keeps the turn."""
    if not in_tutorial(world):
        return False
    for activity in task_activities(world):
        if activity.locked:
            continue
        if activity.done < (activity.goal or 1):
            return True
    return False


class QuestTalk(Action):

    def __init__(self, npc: str, steps: tuple[Turn, ...], *, expect: Expect | None = None) -> None:
        super().__init__()
        self.priority = 280
        self.durable = True
        self.npc = npc
        self.steps = steps
        self.expect = expect
        self.cursor = 0
        self.sent = False
        self.handed = False
        self.money_mark: dict[int, tuple[int, int, int, int] | None] = {}
        self.faction_amount_mark: dict[int, int | None] = {}
        self.faction_changed_mark: dict[int, bool] = {}
        self.active_path = None

    def opcodes(self) -> tuple[str, ...]:
        return ("OP_Consider", "OP_ChannelMessage", "OP_SpecialMesg", "OP_SimpleMessage")

    def suspend(self) -> None:
        self.active_path = None
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        if _book_open(world):
            # The mine book is the pass bar. A gear conversation waits.
            self.priority = -1
            return
        if mob_named(world, self.npc) is None:
            # He is in another zone. A travel or zone step has to be able to win.
            self.priority = -1
            return
        self.priority = 280
        if self._met(world):
            self.complete = True
            return
        if self.cursor >= len(self.steps):
            if self.expect is None:
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
        if isinstance(turn, Need):
            self._need(loop, world, turn.item)
            return
        if isinstance(turn, Money):
            self._await_money(world, turn)
            return
        if isinstance(turn, Faction):
            self._await_faction(world, turn)
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

    def _need(self, loop: Loop, world: World, item: int) -> None:
        """Spawn a Fetch until the item is held, then continue the conversation."""
        if world.held(item) > 0:
            self._advance()
            return
        if self._kind_pending(loop, Fetch, f"{self.source}#fetch:{item}"):
            self.yielding = True
            return
        fetch = Fetch(item, 1, str(item))
        if yield_to(self, loop, world, fetch, f"{self.source}#fetch:{item}"):
            self.yielding = True

    def _await_money(self, world: World, step: Money) -> None:
        if self._money_since(world, ExpectMoney(step.platinum, step.gold, step.silver, step.copper), self.cursor):
            self._advance()

    def _await_faction(self, world: World, step: Faction) -> None:
        if self._faction_since(world, ExpectFaction(step.faction, step.delta), self.cursor):
            self._advance()

    def _kind_pending(self, loop: Loop, kind: type[Fetch] | type[Trade], source: str) -> bool:
        queue = loop.queue
        if queue is None:
            return False
        for action in queue:
            if isinstance(action, kind) and action.source == source and not action.complete:
                return True
        return False

    def _trade_pending(self, loop: Loop, item: int) -> bool:
        return self._kind_pending(loop, Trade, f"{self.source}#trade:{item}")

    def _advance(self) -> None:
        self.cursor += 1
        self.sent = False
        self.handed = False
        if self.cursor >= len(self.steps) and self.expect is None:
            self.complete = True

    def _met(self, world: World) -> bool:
        expect = self.expect
        if expect is None:
            return False
        if isinstance(expect, ExpectItem):
            return world.held(expect.item) > 0
        if isinstance(expect, ExpectMoney):
            return self._money_since(world, expect, -1)
        return self._faction_since(world, expect, -1)

    def _money_since(self, world: World, expect: ExpectMoney, mark: int) -> bool:
        coin = world.coin
        if mark not in self.money_mark:
            self.money_mark[mark] = coin
            return False
        opened = self.money_mark[mark]
        if coin is None or opened is None:
            return False
        gained = _copper(coin) - _copper(opened)
        need = expect.platinum * 1000 + expect.gold * 100 + expect.silver * 10 + expect.copper
        if need <= 0:
            return gained > 0
        return gained >= need

    def _faction_since(self, world: World, expect: ExpectFaction, mark: int) -> bool:
        row = world.factions.get(expect.faction)
        if mark not in self.faction_amount_mark:
            self.faction_amount_mark[mark] = row.amount if row else None
            self.faction_changed_mark[mark] = row.changed if row else False
            return False
        if row is None:
            return False
        if row.changed and not self.faction_changed_mark[mark]:
            return True
        opened = self.faction_amount_mark[mark]
        if row.amount is None or opened is None:
            return False
        if expect.delta >= 0:
            return row.amount >= opened + expect.delta
        return row.amount <= opened + expect.delta

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


def _copper(coin: tuple[int, int, int, int]) -> int:
    platinum, gold, silver, copper = coin
    return platinum * 1000 + gold * 100 + silver * 10 + copper


def _spoken(word: str, name: str) -> str:
    """A hail names the npc. Any other graph word is the script match, said as stored."""
    text = word.strip()
    if text.lower() != "hail":
        return text
    spoken = " ".join(name.replace("_", " ").split())
    if not spoken:
        return text
    return f"Hail, {spoken}"
