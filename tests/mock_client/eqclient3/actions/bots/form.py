"""Band 290. A party size picks the template. Spawn each bot, create one the server says is missing, then invite.

members counts the player. The player's group is warrior, cleric, mage, wizard, and monk. Each extra group is a tank, a healer, and four damage classes, so its sixth seat is damage. Classes are used once before a repeat takes the next letter, a through z.
"""

from __future__ import annotations

import os
from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import World

from eqclient3.action import Action
from eqclient3.actions.support import character_name, message_text, send_command
from eqclient3.handlers.common import mob_named
from eqclient3.structs import OP_GroupInvite, OP_TargetMouse
from eqclient3.world import Bot

# Class, then a race city guards do not attack. Dark elf, troll, ogre, and iksar are killed on sight.
# A shadow knight can be erudite, gnome, froglok, or drakkin. Erudite is the one used here.
# A shaman can be froglok, vah shir, or barbarian. A beastlord can be vah shir or barbarian.
# A berserker can be dwarf, vah shir, or barbarian. Barbarians are killed in the elf cities, so they are not used.
# The player's group takes the first tank, the first healer, and the first three damage classes.
# An extra group takes the next tank, the next healer, and four damage classes.
_MALE = 0
_TANKS = (
    ("war", 1, 1),
    ("pal", 3, 1),
    ("shd", 5, 3),
)
_HEALS = (
    ("clr", 2, 1),
    ("dru", 6, 1),
    ("shm", 10, 330),
)
_DPS = (
    ("mag", 13, 1),
    ("wiz", 12, 1),
    ("mnk", 7, 1),
    ("rng", 4, 1),
    ("brd", 8, 1),
    ("rog", 9, 1),
    ("nec", 11, 1),
    ("enc", 14, 1),
    ("ber", 16, 8),
)
_RACE = {class_id: race for _code, class_id, race in (*_TANKS, *_HEALS, *_DPS)}
_COPIES = 27  # the bare class code, then a through z
_CORE = ("tank", "heal", "dps", "dps", "dps")
_EXTRA = ("tank", "heal", "dps", "dps", "dps", "dps")
_MISSING = ("don't own", "do not own", "failed to load", "failed to spawn")
_RENAME = ("prohibited", "already being used", "invalid name")
_BAD_SPAWN = ("invalid bot",)
_BAD_CLASS = ("invalid race-class", "invalid class")
_BAD_CREATE = ("failed to create",)
_LIMITS = (
    "create limit",
    "spawn limit",
    "cannot create",
    "cannot have more than",
    "your level",
    "level is too",
    "not high enough",
)


class _Reply(Enum):
    MISSING = 1
    UP = 2
    RENAME = 3
    CREATED = 4
    SKIP = 5
    STOP = 6


_READY = (
    "i am ready to fight",
    "a solid weapon is my ally",
    "the pious shall never die",
    "i am the symbol of light",
    "there are enemies near",
    "out of the shadows, i step",
    "nature's fury shall be wrought",
    "your punishment will be my fist",
    "music is the overture of battle",
    "daggers into the backs of my enemies",
    "more bones to grind",
    "death is only the beginning",
    "i am the harbinger of demise",
    "the elements are at my command",
    "no being can resist my charm",
    "battles are won by hand and paw",
    "my bloodthirst shall not be quenched",
)


class Form(Action):
    def __init__(self, zone: str, members: int = 6) -> None:
        super().__init__()
        self.priority = 290
        self.zone = zone
        self.members = members
        self.roster: list[tuple[str, int]] = []
        self.built = False
        self.phase = "spawn"
        self.index = 0
        self.spawned: list[str] = []
        self.pending = ""
        self._retitles: dict[int, int] = {}

    def opcodes(self) -> tuple[str, ...]:
        return ("OP_ChannelMessage", "OP_SpecialMesg", "OP_SimpleMessage")

    def suspend(self) -> None:
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        self.suspended = False
        if not self.built:
            self._fill(loop, world)
        if self.pending:
            reply = self._take_reply()
            if not reply:
                return
            self._apply(loop, world, reply)
            self.pending = ""
        command = self._poll()
        if command is None:
            self.complete = True
            return
        if command.startswith("groupinvite "):
            self._invite(loop, world, command.split(" ", 1)[1])
            return
        send_command(loop, command)
        if command.startswith("^botspawn") or command.startswith("^botcreate"):
            self.pending = command

    def _fill(self, loop: Loop, world: World) -> None:
        self.built = True
        self.roster = _party(character_name(loop, world), self.members, _saved(loop, world))
        self.phase = "spawn" if self.roster else "done"

    def _poll(self) -> str | None:
        if self.phase == "spawn":
            if self.index >= len(self.roster):
                self.phase = "invite"
                self.index = 0
                return self._poll()
            name = self.roster[self.index][0]
            if name.lower() in {item.lower() for item in self.spawned}:
                self.index += 1
                return self._poll()
            return f"^botspawn {name}"
        if self.phase == "create":
            name, class_id = self.roster[self.index]
            if class_id <= 0:
                self.index += 1
                self.phase = "spawn"
                return self._poll()
            return f"^botcreate {name} {class_id} {_race(class_id)} {_MALE}"
        if self.phase == "invite":
            if self.index >= len(self.spawned):
                self.phase = "follow"
                return self._poll()
            name = self.spawned[self.index]
            self.index += 1
            return f"groupinvite {name}"
        if self.phase == "follow":
            self.phase = "done"
            if not self.spawned:
                return None
            return "^follow reset spawned"
        return None

    def _take_reply(self) -> str:
        for index, message in enumerate(self.messages):
            text = message_text(message)
            if _reply(self.pending, text) is None:
                continue
            self.messages.pop(index)
            return text
        return ""

    def _apply(self, loop: Loop, world: World, reply: str) -> None:
        kind = _reply(self.pending, reply)
        name = self.roster[self.index][0]
        if kind is _Reply.MISSING:
            self.phase = "create"
            return
        if kind is _Reply.UP:
            self._remember(loop, world, name)
            self._note(world, name)
            self.index += 1
            self.phase = "spawn"
            return
        if kind is _Reply.CREATED:
            self._remember(loop, world, name)
            self.phase = "spawn"
            return
        if kind is _Reply.RENAME:
            self._retitle(name)
            return
        if kind is _Reply.SKIP:
            self.index += 1
            self.phase = "spawn"
            return
        if kind is _Reply.STOP:
            self.phase = "invite"
            self.index = 0

    def _retitle(self, name: str) -> None:
        """The server rejected this name. Pick another and create that one."""
        tries = self._retitles.get(self.index, 0) + 1
        self._retitles[self.index] = tries
        if tries > 26:
            self.index += 1
            self.phase = "spawn"
            return
        taken = {row[0] for row in self.roster} | set(self.spawned)
        fresh = alternate_name(name, taken, tries)
        class_id = self.roster[self.index][1]
        self.roster[self.index] = (fresh, class_id)
        self.phase = "create"

    def _remember(self, loop: Loop, world: World, name: str) -> None:
        who = character_name(loop, world)
        journal = loop.journal
        if not journal or not who:
            return
        class_id = next((class_id for bot_name, class_id in self.roster if bot_name.lower() == name.lower()), 0)
        journal.remember_bot(who, name, class_id)

    def _note(self, world: World, name: str) -> None:
        if name.lower() not in {item.lower() for item in self.spawned}:
            self.spawned.append(name)
        class_id = next((class_id for bot_name, class_id in self.roster if bot_name.lower() == name.lower()), 0)
        for bot in world.bots.roster:
            if bot.name.lower() == name.lower():
                bot.alive = True
                if class_id:
                    bot.class_id = class_id
                return
        world.bots.roster.append(Bot(name, class_id, alive=True))

    def _invite(self, loop: Loop, world: World, name: str) -> None:
        who = character_name(loop, world)
        mob = mob_named(world, name)
        live = mob.spoken_name() if mob and mob.spoken_name() else name
        if mob:
            loop.send("OP_TargetMouse", OP_TargetMouse(mob.id & 65535).serialize())
        loop.send("OP_GroupInvite", OP_GroupInvite(live, who).serialize())


def _race(class_id: int) -> int:
    return _RACE[class_id]


def party_members() -> int:
    """Seats in the group, counting the player. EQEMU_PARTY overrides the group of six."""
    raw = os.environ.get("EQEMU_PARTY", "6")
    try:
        size = int(raw)
    except ValueError:
        size = 6
    if size < 1:
        return 1
    cap = 1 + _max_bots()
    if size > cap:
        return cap
    return size


def _party(character: str, members: int, saved: list[tuple[str, int]]) -> list[tuple[str, int]]:
    count = members - 1
    if count < 1:
        return []
    stem = _prefix(character)
    rows = [((stem + code)[:15], class_id) for code, class_id in _codes(count)]
    return _adopt(rows, saved)


class _Seats:
    """Walks one role. The second time a class comes up, its name gains a, then b."""

    def __init__(self, pool: tuple[tuple[str, int, int], ...]) -> None:
        self.pool = pool
        self.index = 0

    def take(self) -> tuple[str, int] | None:
        if self.index >= len(self.pool) * _COPIES:
            return None
        code, class_id, _race_id = self.pool[self.index % len(self.pool)]
        copy = self.index // len(self.pool)
        self.index += 1
        letter = "" if copy == 0 else chr(ord("a") + copy - 1)
        return (f"{code}{letter}", class_id)


def _codes(count: int) -> list[tuple[str, int]]:
    """The player's five, then groups of six whose last seat is damage."""
    seats = {"tank": _Seats(_TANKS), "heal": _Seats(_HEALS), "dps": _Seats(_DPS)}
    rows: list[tuple[str, int]] = []
    _fill(rows, count, seats, _CORE)
    while len(rows) < count:
        if not _fill(rows, count, seats, _EXTRA):
            break
    return rows


def _fill(
    rows: list[tuple[str, int]],
    count: int,
    seats: dict[str, _Seats],
    pattern: tuple[str, ...],
) -> bool:
    for role in pattern:
        if len(rows) >= count:
            break
        row = seats[role].take()
        if not row:
            return False
        rows.append(row)
    return True


def _max_bots() -> int:
    """How many bots fit before a role runs out of letters."""
    extra = min(
        len(_TANKS) * _COPIES - 1,
        len(_HEALS) * _COPIES - 1,
        (len(_DPS) * _COPIES - 3) // 4,
    )
    if extra < 1:
        return len(_CORE)
    return len(_CORE) + extra * len(_EXTRA)


def _saved(loop: Loop, world: World) -> list[tuple[str, int]]:
    journal = loop.journal
    who = character_name(loop, world)
    if not journal or not who:
        return []
    return journal.bots(who)


def _adopt(rows: list[tuple[str, int]], saved: list[tuple[str, int]]) -> list[tuple[str, int]]:
    """A bot already owned for that class keeps its name. The template fills the rest."""
    owned = {name.lower() for name, _class_id in saved}
    by_class: dict[int, str] = {}
    for name, class_id in saved:
        by_class.setdefault(class_id, name)
    used: set[str] = set()
    chosen: list[tuple[str, int]] = []
    for name, class_id in rows:
        picked = name
        if name.lower() not in owned:
            adopted = by_class.get(class_id, "")
            if adopted and adopted.lower() not in used:
                picked = adopted
        used.add(picked.lower())
        chosen.append((picked, class_id))
    return chosen


def _prefix(character: str) -> str:
    raw = os.environ.get("EQEMU_BOT_PREFIX", character[:3])
    letters = "".join(ch for ch in raw if ch.isalpha())
    if not letters:
        letters = "Bot"
    return (letters[:1].upper() + letters[1:].lower())[:12]


def alternate_name(name: str, taken: set[str], attempt: int) -> str:
    """A nearby name the server will accept. Three identical letters in a row are prohibited."""
    used = {item.lower() for item in taken}
    broken = _shape(_break_runs(name))
    if attempt <= 1 and broken.lower() not in used and not _long_run(broken) and broken.lower() != name.lower():
        return broken
    stem = broken if not _long_run(broken) else _shape(name)
    for offset in range(26):
        suffix = chr(ord("a") + (max(attempt, 1) - 1 + offset) % 26)
        trial = _shape(_break_runs(stem + suffix))
        if trial.lower() not in used and not _long_run(trial):
            return trial
    return _shape(stem + "x")


def _reply(pending: str, text: str) -> _Reply | None:
    """What this server line means for the command we just sent."""
    lowered = (text or "").lower()
    if not pending or lowered.strip() == pending.lower().strip():
        return None
    spawning = pending.startswith("^botspawn")
    creating = pending.startswith("^botcreate")
    if spawning and _has(lowered, _MISSING):
        return _Reply.MISSING
    if spawning and _spawned(lowered):
        return _Reply.UP
    if (spawning or creating) and _has(lowered, _RENAME):
        return _Reply.RENAME
    if creating and "bot created" in lowered:
        return _Reply.CREATED
    if creating and _has(lowered, _BAD_CLASS):
        return _Reply.SKIP
    if (spawning or creating) and (_limited(lowered) or _has(lowered, _BAD_SPAWN if spawning else _BAD_CREATE)):
        return _Reply.STOP
    return None


def _has(text: str, phrases: tuple[str, ...]) -> bool:
    return any(phrase in text for phrase in phrases)


def _spawned(text: str) -> bool:
    if "already spawned" in text:
        return True
    return any(line in text for line in _READY)


def _limited(text: str) -> bool:
    """Server create/spawn limit. A botlist line that says 'is a Level' is not one."""
    if "is a level" in text:
        return False
    if _has(text, _LIMITS):
        return True
    return "level" in text and _has(text, ("create", "spawn", "bot"))


def _long_run(name: str) -> bool:
    """The server rejects a name with the same letter three times in a row."""
    run = 1
    for previous, current in zip(name, name[1:]):
        if previous.lower() == current.lower():
            run += 1
            if run > 2:
                return True
        else:
            run = 1
    return False


def _break_runs(name: str) -> str:
    chars = list(name)
    index = 0
    while index < len(chars):
        end = index + 1
        while end < len(chars) and chars[end].lower() == chars[index].lower():
            end += 1
        if end - index > 2:
            neighbor = chars[end].lower() if end < len(chars) else ""
            chars[index + 2] = _breaker(chars[index], neighbor)
        index = end if end > index else index + 1
    return "".join(chars)


def _breaker(repeated: str, neighbor: str) -> str:
    for letter in "xyzqab":
        if letter != repeated.lower() and letter != neighbor.lower():
            return letter
    return "x"


def _shape(name: str) -> str:
    letters = "".join(ch for ch in name if ch.isalpha())
    if len(letters) < 4:
        letters = (letters + "botx")[:4]
    return (letters[:1].upper() + letters[1:].lower())[:15]
