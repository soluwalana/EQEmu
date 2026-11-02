"""Hail an npc, then say each link that reply offers.

Standing 8 or 9 starts a fight or a soulbind, by the level gap. A reply is not
the end of the hail: the words inside its saylinks are said next, and the
answer to each of those is read before the hail is finished.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, runtime_checkable

if TYPE_CHECKING:
    from eqclient3.action import Message
    from eqclient3.loop import Loop
    from eqclient3.world import Mob, World
    from eqclient3.camps import Soulbinder

import os
import re
from pathlib import Path
from eqclient3.action import Action
from eqclient3.log import log
from eqclient3.nav.navmesh import load_nav
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
from eqclient3.structs import OP_TargetMouse
from eqclient3.struct_helpers import saylink_words

_HAIL_NAME = re.compile(r"hail\s+(?:the\s+)?([A-Za-z][A-Za-z\']*)", re.IGNORECASE)

# spawn2 65801. The camp sits one floor above the tunnel that paths to it.
_PADS = {
    "guard hobart": (-574.0, -518.0, -2.67),
    "guard rahtiz": (-110.53, -210.0, 13.75),
}


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
        self.sought = False
        self.heard_text = ""
        self.mark: tuple | None = None
        self.where: tuple[float, float, float] | None = None
        self.anchor: tuple[float, float] | None = None
        self.still = 0
        self.roaming = False

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
        if not self.sent and self._stuck(world):
            self.roaming = True
            self.target_id = 0
        if not self.roaming:
            self._bind_hail_target(world)
        elif self.anchor is not None and _moved(world, self.anchor) > 40:
            self.roaming = False
            self._bind_hail_target(world)
        self._shorter_stride()
        super().step(loop, world)

        if self.waiting_for("HAIL"):
            self._ensure_chain()
            self._fold(loop, world)
            if str(self.source).startswith("task:") and _step_done(world, str(self.source)):
                self.waited = 0
                self.unwait("HAIL")
                self._after_reply(loop, world)
                return
            if self.expect_reply:
                self.quiet += 1
                if self.quiet < _QUIET:
                    return
                self.expect_reply = False
                if self.mark is not None and _book(world) != self.mark:
                    self.pending.clear()
            word = self._next_word(loop, world)
            if word:
                self.waited = 0
                self._speak_link(loop, world, word)
                return
            if self._offer_find(loop, world):
                return
            if str(self.source).startswith("task:") and not _step_done(world, str(self.source)):
                self.waited += 1
                if self.waited < _STALL:
                    return
                self.waited = 0
                self.sent = False
                self.unwait("HAIL")
                return
            if not self.task_text_satisfied():
                self.waited += 1
                if self.waited < _STALL:
                    return
            self.waited = 0
            self.unwait("HAIL")
            self._after_reply(loop, world)
            return

        if self.waiting_for("TARGET"):
            body = world.mobs.get(self.target_id) if self.target_id else None
            if body is not None and _beside(world, body.position):
                self.unwait("TARGET")
            elif self.waited < 15:
                return
            else:
                self.unwait("TARGET")
                self.target_id = 0
                self.active_path = None

        if self.target_id and not _same_npc(world, self.target_id, self._search_name()):
            self.target_id = 0
            self.active_path = None

        if not self.target_id and not self._search_name() and not self.task_text:
            self.complete = True
            return

        if self.pad is None:
            spot = _PADS.get(self._search_name().lower())
            if spot is not None:
                self.pad = spot

        if not self.target_id and self._search_name():
            if self.pad is not None and not _beside(world, self.pad):
                walk(self, loop, world, self.pad, self.stride or "run")
                return
            if self.pad is None:
                self._wander(loop, world)
                return

        mob = world.mobs.get(self.target_id, None)
        if mob and standing_of(mob) in (8, 9):
            gap = int(mob.level or 0) - int(world.level or 1)

            if gap <= 10:
                self._attack(loop, world, mob)
                return

            append_soulbind(self, loop, world)
            return

        if mob and not _beside(world, mob.position):
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
        # A task hail stays open until the server book marks that activity done.
        if str(self.source or "").startswith("task:") and _open_step(world, str(self.source)):
            self.sent = False
            return
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

    def _stuck(self, world: World) -> bool:
        """Five seconds on one spot means this route will not reach the npc."""
        here = (round(world.x, 1), round(world.y, 1))
        if here == self.anchor:
            self.still += 1
        else:
            self.anchor = here
            self.still = 0
        if self.still < 50:
            return False
        mob = world.mobs.get(self.target_id) if self.target_id else None
        if mob is not None and _beside(world, mob.position):
            self.still = 0
            return False
        if self.pad is not None and _beside(world, self.pad):
            self.still = 0
            return False
        mesh = load_nav(str(world.zone or ""))
        point = self.where
        if mesh is not None and point is not None:
            spot = mesh.locate(point)
            if spot is not None:
                mesh.visited.add(spot)
        log.info("talk unstick %s", self._search_name())
        self.where = None
        self.active_path = None
        self.still = 0
        return True

    def _wander(self, loop: Loop, world: World) -> None:
        """The named npc is not spawned. Walk the next unvisited patch until they are."""
        if self.where is not None and yards(world, self.where) > HAIL:
            walk(self, loop, world, self.where, self.stride or "run")
            return
        mesh = load_nav(str(world.zone or ""))
        point = None if mesh is None else mesh.unvisited(world.position)
        if point is None:
            return
        if self.where is None:
            log.info("talk search %s", self._search_name())
        self.where = point
        self.active_path = None
        walk(self, loop, world, point, self.stride or "run")

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
        if self.target_id:
            loop.send("OP_TargetMouse", OP_TargetMouse(int(self.target_id) & 65535).serialize())
        send_command(loop, hail_line(self.line, self._npc_name(world)))

    def _ensure_chain(self) -> None:
        """A talk restored from an older journal has none of the chain fields."""
        if not hasattr(self, "replied"):
            self.replied = False
        if not hasattr(self, "sought"):
            self.sought = False
        if not hasattr(self, "heard_text"):
            self.heard_text = ""
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
        lines: list[str] = []
        for message in unseen:
            _speaker, text = _reply(message) or ("", "")
            if text:
                lines.append(text)
            offered.extend(saylink_words(text))
        if lines:
            self.heard_text = " ".join(lines)
        ordered = reply_order(
            offered,
            _advances(str(world.zone or ""), self._npc_name(world)),
            _open_steps(world),
            self._known_said(loop, world),
            repeat=str(self.source).startswith("task:") and not _step_done(world, str(self.source)),
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

    def _stand_aside(self) -> None:
        """The find hunt is priority -1 and newer talks win that band. Drop below it."""
        self.priority = -2
        self.yielding = True

    def _offer_find(self, loop: Loop, world: World) -> bool:
        """A reply that says find a person. That person is a walk, then a hail.

        An item named in the line is a produce fetch, already queued with the gear.
        """
        if self.sought:
            if _find_open(loop):
                self._stand_aside()
                return True
            # The find had the turn. This talk takes its band again once that find leaves.
            self.priority = 0
            return False
        name = find_name(self.heard_text)
        if not name:
            return False
        source = f"find:{name.lower()}"
        if _find_open(loop, source):
            self.sought = True
            self._stand_aside()
            return True
        self.sought = True
        mob = mob_named(world, name)
        if mob is None and not _proper_name(name):
            return False
        npc = int(mob.id) if mob is not None else 0
        talk = Talk(npc, "hail", name)
        talk.bind_name = name
        return yield_to(self, loop, world, talk, source)

    def _next_word(self, loop: Loop, world: World) -> str:
        if self.depth >= _DEPTH:
            self.pending.clear()
            return ""
        said = self._known_said(loop, world)
        # A step still open in the book has to hear the link again. The first say did not finish it.
        again = str(self.source).startswith("task:") and not _step_done(world, str(self.source))
        while self.pending:
            word = self.pending.pop(0)
            if word.lower() == "hail":
                continue
            if word.lower() in said and not again:
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
        if self.target_id:
            loop.send("OP_TargetMouse", OP_TargetMouse(int(self.target_id) & 65535).serialize())
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
_FIND = re.compile(r"\bfind\s+(?:any\s+|the\s+)?([A-Za-z][A-Za-z' ]*[A-Za-z])", re.IGNORECASE)
_QUIET = 3
_STALL = 50
_DEPTH = 8
_SAY = re.compile(r"""\$text\s*=~\s*/([^/]+)/i|findi\(\s*["']([^"']+)["']\s*\)""", re.IGNORECASE)
_UPDATE = re.compile(r"update_?task_?activity\s*\(\s*(\d+)\s*,\s*(\d+)", re.IGNORECASE)
_ADVANCES: dict[tuple[str, str], dict[str, set[tuple[int, int]]]] = {}


def reply_order(
    offered: list[str],
    advances: dict[str, set[tuple[int, int]]],
    open_steps: set[tuple[int, int]],
    said: set[str],
    repeat: bool = False,
) -> list[str]:
    """Options from one reply. A word that finishes an open step comes first.

    repeat says a link again when that earlier say left the task step open.
    """
    pending: list[str] = []
    seen: set[str] = set()
    for word in offered:
        key = word.lower()
        if not key or key == "hail" or key in seen:
            continue
        if key in said and not repeat:
            continue
        seen.add(key)
        pending.append(word)

    def rank(word: str) -> tuple[int, int]:
        hits = advances.get(word.lower(), set())
        return (0 if hits & open_steps else 1, pending.index(word))

    return sorted(pending, key=rank)


def find_name(text: str) -> str:
    """The thing or person after find. The rest of the sentence stays out."""
    match = _FIND.search(text or "")
    if match is None:
        return ""
    kept = []
    for word in match.group(1).split():
        if word.lower() in {"and", "then", "bring", "to", "so"}:
            break
        kept.append(word)
    return " ".join(kept)


def _same_npc(world: World, spawn_id: int, name: str) -> bool:
    mob = world.mobs.get(spawn_id)
    if mob is None:
        return False
    if not name:
        return True
    spoken = " ".join(mob.spoken_name().replace("_", " ").lower().split())
    want = " ".join(name.replace("_", " ").lower().split())
    return spoken == want or want in spoken or spoken in want


def _find_open(loop: Loop, source: str = "") -> bool:
    queue = loop.queue
    if queue is None:
        return False
    for action in queue:
        if action.complete or not str(action.source).startswith("find:"):
            continue
        if source and action.source != source:
            continue
        return True
    return False


def _step_done(world: World, source: str) -> bool:
    """A task hail is finished when the server book shows that activity done."""
    for activity in task_activities(world):
        key = f"task:{int(activity.task_id)}:{int(activity.activity_id)}"
        if key != source:
            continue
        return int(activity.done or 0) >= int(activity.goal or 1)
    return False


def _open_step(world: World, source: str) -> bool:
    """True when the book still lists this activity and it is not done."""
    for activity in task_activities(world):
        key = f"task:{activity.task_id}:{activity.activity_id}"
        if key != source:
            continue
        return activity.done < activity.goal
    return False


def _beside(world: World, point: tuple[float, float, float]) -> bool:
    """Close enough to speak. A ledge counts when the floor under it is in hail range."""
    if yards(world, point) <= HAIL:
        return True
    dx = float(point[0]) - float(world.x)
    dy = float(point[1]) - float(world.y)
    return (dx * dx + dy * dy) ** 0.5 <= HAIL


def _moved(world: World, anchor: tuple[float, float]) -> float:
    dx = float(world.x) - anchor[0]
    dy = float(world.y) - anchor[1]
    return (dx * dx + dy * dy) ** 0.5


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


@runtime_checkable
class _Step(Protocol):
    task_id: int
    activity_id: int
    done: int
    goal: int
    locked: bool


def _book(world: World) -> tuple[tuple[int, int, int], ...]:
    rows: list[tuple[int, int, int]] = []
    for activity in task_activities(world):
        if not isinstance(activity, _Step):
            continue
        rows.append((activity.task_id, activity.activity_id, activity.done))
    return tuple(sorted(rows))


def _open_steps(world: World) -> set[tuple[int, int]]:
    found: set[tuple[int, int]] = set()
    for activity in task_activities(world):
        if not isinstance(activity, _Step):
            continue
        if activity.locked or activity.done >= (activity.goal or 1):
            continue
        found.add((activity.task_id, activity.activity_id))
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
    if text.startswith("[") and text.endswith("]") and len(text) > 2:
        text = text[1:-1].strip()
        line = text
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
