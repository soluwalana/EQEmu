"""Hail an npc, then say each link that reply offers.

Standing 8 or 9 starts a fight or a soulbind, by the level gap. A reply is not
the end of the hail: the words inside its saylinks are said next, and the
answer to each of those is read before the hail is finished.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.action import Message
    from eqclient3.loop import Loop
    from eqclient3.world import Mob, World
    from eqclient3.camps import Soulbinder

import os
import re
from pathlib import Path
from eqclient3.action import Action
from eqclient3.actions.attack import Attack
from eqclient3.actions.support import (
    HAIL,
    SPEAK,
    line_of,
    mark_tutorial,
    message_text,
    send_command,
    simple_id,
    soulbinder,
    standing_of,
    task_activities,
    walk,
    yards,
    yield_to,
)
from eqclient3.handlers.common import attack_for, character_name, mark_fight, mob_named
from eqclient3.struct_helpers import saylink_words

_HAIL_NAME = re.compile(r"hail\s+(?:the\s+)?([A-Za-z][A-Za-z\']*)", re.IGNORECASE)


class Talk(Action):

    def __init__(self, npc: int | str, line: str, task_text: str, priority: int = 0) -> None:
        super().__init__()
        self.priority = priority
        self.npc: int | str = npc
        self.target_id = npc if isinstance(npc, int) else 0
        self.line = line
        self.task_text = task_text or ""
        self.active_path = None
        self.sent = False
        self.stride: str | None = None
        self.followed = False
        self.satisfied = False
        self.finishes_tutorial = False
        self.pad: tuple[float, float, float] | None = None
        self.bind_name = ""
        self.said: set[str] = set()
        self.pending: list[str] = []
        self.expect_reply = False
        self.quiet = 0
        self.heard: set[int] = set()
        self.depth = 0
        self.replied = False
        self.mark: tuple | None = None

    def opcodes(self) -> tuple[str, ...]:
        return (
            "OP_Consider",
            "OP_ChannelMessage",
            "OP_SpecialMesg",
            "OP_SimpleMessage",
        )

    def suspend(self) -> None:
        self.active_path = None
        self.suspended = True

    def task_text_satisfied(self) -> bool:
        if self.satisfied:
            return True
        # His answer is a message from him. A hail does not come back.
        if (self.line or "").strip().lower() == "hail" and self.sent and self.replied:
            self.satisfied = True
            return True
        # "Hail Absor and Learn About Weapons" is the objective, not a line the npc will say.
        if self.line == "hail" and hail_name(self.task_text):
            self.satisfied = self.sent
            return self.sent
        if not self.task_text:
            self.satisfied = self.sent
            return self.sent
        needle = self.task_text.lower()
        heard = lambda message: needle in message_text(message).lower()
        for opcode in ("OP_ChannelMessage", "OP_SpecialMesg", "OP_SimpleMessage"):
            if self.consume(opcode, heard):
                self.satisfied = True
                return True
        return False

    def step(self, loop: Loop, world: World) -> None:
        self._bind_hail_target(world)
        self._shorter_stride()
        super().step(loop, world)

        if self.waiting_for("HAIL"):
            self._ensure_chain()
            self._fold(loop, world)
            if self.expect_reply:
                self.quiet += 1
                if self.quiet < _QUIET:
                    return
                self.expect_reply = False
                if self.mark is not None and _book(world) != self.mark:
                    self.pending.clear()
            word = self._next_word(loop, world)
            if word:
                self._speak_link(loop, world, word)
                return
            if not self.task_text_satisfied():
                return
            self.unwait("HAIL")
            self._after_reply(loop, world)
            return

        if self.waiting_for("TARGET"):
            return

        if not self.target_id and self.bind_name and self.pad is not None and yards(world, self.pad) > HAIL:
            walk(self, loop, world, self.pad, self.stride or "run")
            return

        if not self.target_id and not self._search_name() and not self.task_text:
            self.complete = True
            return

        if not self.target_id and self._search_name() and (self.pad is None or yards(world, self.pad) > HAIL):
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
            walk(self, loop, world, mob.position, self.stride or "run")
            return

        if self.followed:
            self.complete = True
            return

        if not self.sent:
            self._ensure_chain()
            self._remember(loop, world, self.line)
            self.mark = _book(world)
            self.expect_reply = True
            self.quiet = 0
            self._say(loop, world)
            self.sent = True
            self.wait("HAIL")
            self.suspended = False
            return

        self._after_reply(loop, world)

    def _after_reply(self, loop: Loop, world: World) -> None:
        self.suspended = False
        if self.followed:
            self.complete = True
            return

        follow = world.follow_up
        if follow is not None and yield_to(self, loop, world, follow, follow.source or "talk:follow"):
            self.followed = True
            return

        if self.finishes_tutorial or _ends_tutorial(world):
            _finish_tutorial(self, loop, world)

        self.followed = True
        self.complete = True

    def _bind_hail_target(self, world: World) -> None:
        if self.target_id:
            return
        name = self._search_name()
        if not name:
            return
        mob = mob_named(world, name)
        if mob is None:
            return
        self.npc = int(mob.id)
        self.target_id = int(mob.id)

    def _shorter_stride(self) -> None:
        if self.consume("OP_SimpleMessage", lambda message: simple_id(message) == 124):
            self.stride = "walk"
            self.active_path = None

    def _say(self, loop: Loop, world: World) -> None:
        send_command(loop, hail_line(self.line, self._npc_name(world)))

    def _ensure_chain(self) -> None:
        """A talk restored from an older journal has none of the chain fields."""
        if not hasattr(self, "replied"):
            self.replied = False
        if isinstance(getattr(self, "pending", None), list) and isinstance(getattr(self, "heard", None), set):
            return
        self.said = set()
        self.pending = []
        self.expect_reply = False
        self.quiet = 0
        self.heard = set()
        self.depth = 0
        self.replied = False
        self.mark = None

    def _fold(self, loop: Loop, world: World) -> None:
        """Take every new reply since the last say. Links in it are said next.

        A reply that arrives after a link we said is that link's answer. If the
        task book moved, the other links from the previous reply are dropped.
        """
        unseen = self._unseen(loop, world)
        if not unseen:
            return
        self.replied = True
        for message in unseen:
            self.heard.add(id(message))
        if self.expect_reply and self.mark is not None and _book(world) != self.mark:
            self.pending.clear()
        offered: list[str] = []
        for message in unseen:
            _speaker, text = _reply(message) or ("", "")
            offered.extend(saylink_words(text))
        ordered = reply_order(
            offered,
            _advances(str(world.zone or ""), self._npc_name(world)),
            _open_steps(world),
            self._known_said(loop, world),
        )
        self.pending = ordered + self.pending
        self.expect_reply = False

    def _unseen(self, loop: Loop, world: World) -> list[Message]:
        found: list[Message] = []
        who = character_name(loop, world).lower()
        npc = self._npc_name(world)
        for message in self.messages:
            spoken = _reply(message)
            if spoken is None:
                continue
            if id(message) in self.heard:
                continue
            speaker, _text = spoken
            if who and speaker and speaker.lower() == who:
                self.heard.add(id(message))
                continue
            if speaker and not _same_voice(speaker, npc):
                self.heard.add(id(message))
                continue
            found.append(message)
        return found

    def _next_word(self, loop: Loop, world: World) -> str:
        if self.depth >= _DEPTH:
            self.pending.clear()
            return ""
        said = self._known_said(loop, world)
        while self.pending:
            word = self.pending.pop(0)
            if word.lower() in said or word.lower() == "hail":
                continue
            return word
        return ""

    def _speak_link(self, loop: Loop, world: World, word: str) -> None:
        self._remember(loop, world, word)
        self.mark = _book(world)
        self.expect_reply = True
        self.quiet = 0
        self.depth += 1
        self.suspended = False
        send_command(loop, word)

    def _remember(self, loop: Loop, world: World, text: str) -> None:
        word = (text or "").strip()
        if not word:
            return
        self.said.add(word.lower())
        journal = getattr(loop, "journal", None)
        npc = self._npc_name(world)
        who = character_name(loop, world)
        zone = str(getattr(world, "zone", "") or "")
        if journal is None or not who or not npc or not zone:
            return
        journal.remember_say(who, zone, npc, word.lower())

    def _known_said(self, loop: Loop, world: World) -> set[str]:
        said = set(self.said)
        journal = getattr(loop, "journal", None)
        npc = self._npc_name(world).lower()
        who = character_name(loop, world)
        zone = str(getattr(world, "zone", "") or "")
        if journal is None or not who or not npc or not zone:
            return said
        for name, text in journal.said(who, zone):
            if str(name).lower() == npc:
                said.add(str(text).lower())
        return said

    def _npc_name(self, world: World) -> str:
        mob = world.mobs.get(self.target_id) if self.target_id else None
        if mob is not None and mob.spoken_name():
            return mob.spoken_name()
        return self._search_name()

    def _search_name(self) -> str:
        """Who this hail is for. A task target is a name even when the line is only hail."""
        bound = " ".join((self.bind_name or "").replace("_", " ").split())
        if bound:
            return bound
        named = hail_name(self.task_text)
        if named:
            return named
        return _proper_name(self.task_text)

    def _attack(self, loop: Loop, world: World, mob: Mob) -> None:
        spawn = int(mob.id or 0)
        if not spawn or attack_for(loop, Attack, spawn):
            return
        attack = Attack(spawn)
        mark_fight(world, spawn)
        attack.level = int(mob.level or 0)
        yield_to(self, loop, world, attack, f"aggro:{spawn}")


_DIALOGUE = ("OP_ChannelMessage", "OP_SpecialMesg")
_SAYS = 1032
_QUIET = 3
_DEPTH = 8
_SAY = re.compile(r"""\$text\s*=~\s*/([^/]+)/i|findi\(\s*["']([^"']+)["']\s*\)""", re.IGNORECASE)
_UPDATE = re.compile(r"update_?task_?activity\s*\(\s*(\d+)\s*,\s*(\d+)", re.IGNORECASE)
_ADVANCES: dict[tuple[str, str], dict[str, set[tuple[int, int]]]] = {}


def reply_order(
    offered: list[str],
    advances: dict[str, set[tuple[int, int]]],
    open_steps: set[tuple[int, int]],
    said: set[str],
) -> list[str]:
    """Options from one reply. A word that finishes an open step comes first."""
    pending: list[str] = []
    seen: set[str] = set()
    for word in offered:
        key = word.lower()
        if not key or key == "hail" or key in said or key in seen:
            continue
        seen.add(key)
        pending.append(word)

    def rank(word: str) -> tuple[int, int]:
        hits = advances.get(word.lower(), set())
        return (0 if hits & open_steps else 1, pending.index(word))

    return sorted(pending, key=rank)


def _reply(message: Message) -> tuple[str, str] | None:
    """A line said back. Quest speech is string 1032, the character and what he said."""
    if simple_id(message):
        if simple_id(message) != _SAYS:
            return None
        texts = tuple(getattr(message.payload, "texts", ()) or ())
        speaker = str(texts[0]) if texts else ""
        text = str(texts[1]) if len(texts) > 1 else ""
        return speaker, text
    if message.opcode not in _DIALOGUE:
        return None
    return line_of(message.payload)


def _same_voice(speaker: str, npc: str) -> bool:
    """A reply with no speaker, or from this npc. A first name is enough."""
    left = " ".join((speaker or "").replace("_", " ").lower().split())
    right = " ".join((npc or "").replace("_", " ").lower().split())
    if not left or not right:
        return True
    if left == right or left.startswith(right) or right.startswith(left):
        return True
    return left.split()[0] == right.split()[0]


def _book(world: World) -> tuple:
    rows = []
    for activity in task_activities(world):
        rows.append(
            (
                int(getattr(activity, "task_id", 0) or 0),
                int(getattr(activity, "activity_id", 0) or 0),
                int(getattr(activity, "done", 0) or 0),
            )
        )
    return tuple(sorted(rows))


def _open_steps(world: World) -> set[tuple[int, int]]:
    found: set[tuple[int, int]] = set()
    for activity in task_activities(world):
        if getattr(activity, "locked", False) or getattr(activity, "optional", False):
            continue
        goal = int(getattr(activity, "goal", 1) or 1)
        if int(getattr(activity, "done", 0) or 0) >= goal:
            continue
        found.add(
            (
                int(getattr(activity, "task_id", 0) or 0),
                int(getattr(activity, "activity_id", 0) or 0),
            )
        )
    return found


def _advances(zone: str, npc: str) -> dict[str, set[tuple[int, int]]]:
    """Words in this npc's script that check off a task step. Offer order otherwise."""
    key = ((zone or "").lower(), (npc or "").lower())
    cached = _ADVANCES.get(key)
    if cached is not None:
        return cached
    found: dict[str, set[tuple[int, int]]] = {}
    path = _script_path(key[0], npc)
    if path is not None:
        try:
            found = _advances_in(path.read_text(encoding="utf-8", errors="replace"))
        except OSError:
            found = {}
    _ADVANCES[key] = found
    return found


def _script_path(zone: str, npc: str) -> Path | None:
    root = os.environ.get("EQEMU_QUESTS", "")
    if not root or not zone or not npc:
        return None
    folder = Path(root) / zone
    if not folder.is_dir():
        return None
    first = npc.lower().split()[0]
    for path in folder.iterdir():
        if path.suffix.lower() not in {".pl", ".lua"}:
            continue
        stem = path.stem[1:] if path.stem.startswith("#") else path.stem
        label = stem.lower().replace("_", " ")
        if label == npc.lower() or label == first:
            return path
    return None


def _advances_in(text: str) -> dict[str, set[tuple[int, int]]]:
    found: dict[str, set[tuple[int, int]]] = {}
    for match in _SAY.finditer(text):
        word = (match.group(1) or match.group(2) or "").strip().lower()
        if not word:
            continue
        brace = text.find("{", match.end())
        block = _brace_block(text, brace + 1) if brace >= 0 else ""
        for task_id, activity_id in _UPDATE.findall(block):
            found.setdefault(word, set()).add((int(task_id), int(activity_id)))
    return found


def _brace_block(text: str, start: int) -> str:
    depth = 1
    index = start
    while index < len(text) and depth:
        if text[index] == "{":
            depth += 1
        elif text[index] == "}":
            depth -= 1
        index += 1
    return text[start:index]


def _proper_name(text: str) -> str:
    """Guard Rahtiz is a name. A sentence is not."""
    words = " ".join((text or "").replace("_", " ").split()).split()
    if not words or len(words) > 4:
        return ""
    for word in words:
        if not word[:1].isupper():
            return ""
        if not all(ch.isalpha() or ch in "'-" for ch in word):
            return ""
    return " ".join(words)


def hail_line(line: str, name: str) -> str:
    """A bare hail is the default script. The target's name selects his own."""
    text = (line or "").strip()
    if text.lower() != "hail":
        return line
    spoken = " ".join((name or "").replace("_", " ").split())
    if not spoken:
        return line
    return f"Hail, {spoken}"


def hail_name(text: str) -> str:
    match = _HAIL_NAME.search(str(text or "").strip())
    if match is None:
        return ""
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

    queue = loop.queue
    for action in list(queue) if queue is not None else []:
        if type(action).__name__ == "ReadTasks" and not action.complete:
            action.complete = True
            journal = loop.journal
            who = character_name(loop, world)
            if journal is not None and who:
                journal.resolve_action(who, action)
    mark_tutorial(loop, world)
    produce(loop, world, leaving_tutorial=True)


def append_soulbind(parent: Action, loop: Loop, world: World) -> bool:
    binder: Soulbinder | None = soulbinder(world)
    if not binder:
        return False
    name = str(binder.name or "")
    mob = mob_named(world, name) if name else None
    npc = mob.id if mob else 0
    talk = Talk(npc, "hail", "soulbind")
    talk.bind_name = name
    talk.pad = (binder.x, binder.y, binder.z)
    zone = str(binder.zone or world.zone or "")
    return yield_to(parent, loop, world, talk, f"soulbind:{zone}")
