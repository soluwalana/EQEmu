"""Build one bot raid with the commands the server already accepts."""

from __future__ import annotations

import os

# Class codes the ^botcreate command already accepts. Human, male.
ROSTER = (
    ("war", 1),
    ("clr", 2),
    ("enc", 14),
    ("wiz", 12),
    ("rog", 9),
    ("shm", 10),
    ("pal", 3),
    ("dru", 6),
    ("brd", 8),
    ("mag", 13),
    ("mnk", 7),
    ("ber", 16),
)

READY = (
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


def bot_prefix(character: str, prefix: str | None = None) -> str:
    raw = prefix if prefix is not None else os.environ.get("EQEMU_BOT_PREFIX", character[:3])
    letters = "".join(ch for ch in raw if ch.isalpha())
    if not letters:
        letters = "Bot"
    return (letters[:1].upper() + letters[1:].lower())[:12]


def is_limit(message: str) -> bool:
    """Server create/spawn limit. A botlist line that says 'is a Level' is not one."""
    text = message.lower()
    if "is a level" in text:
        return False
    if any(phrase in text for phrase in ("create limit", "spawn limit", "cannot create", "cannot have more than")):
        return True
    if "your level" in text or "level is too" in text or "not high enough" in text:
        return True
    return "level" in text and any(word in text for word in ("create", "spawn", "bot"))


def is_spawned(message: str) -> bool:
    text = message.lower()
    if "already spawned" in text:
        return True
    return any(line in text for line in READY)


class PartyBuilder:
    """botlist, then botcreate and botspawn for each name, then raidform all.

    `already being used` is owned when a following botlist line contains the
    name and `owned by`. The first limit message stops creation. Bots that
    already spawned are still formed into the raid.
    """

    def __init__(self, character: str, prefix: str | None = None) -> None:
        stem = bot_prefix(character, prefix)
        self.character = character
        self.roster = [((stem + code)[:15], class_id) for code, class_id in ROSTER]
        self.owned: set[str] = set()
        self.spawned: set[str] = set()
        self.index = 0
        self.phase = "list"
        self.waiting = ""
        self.formed = False
        self.stopped = False
        self._list: list[str] = []

    def poll(self) -> str | None:
        if self.waiting or self.formed:
            return None
        if self.stopped and self.phase != "raid":
            return None
        if self.phase == "list":
            self._list = []
            self.waiting = "botlist"
            return "botlist"
        if self.phase == "confirm":
            self._list = []
            self.waiting = "botlist"
            return "botlist"
        if self.phase == "create":
            return self._create_or_advance()
        if self.phase == "spawn":
            name = self.roster[self.index][0]
            self.waiting = f"botspawn {name}"
            return self.waiting
        if self.phase == "raid":
            if not self.spawned:
                self.formed = False
                self.phase = "done"
                return None
            self.formed = True
            self.phase = "done"
            return "raidform all"
        return None

    def push(self, message: str) -> None:
        if self.waiting == "botlist":
            self._list.append(message)
            self._finish_list()
            return
        if not self.waiting:
            return
        if self.waiting.startswith("botcreate") and self._on_create(message):
            self.waiting = ""
            return
        if self.waiting.startswith("botspawn") and self._on_spawn(message):
            self.waiting = ""

    def _create_or_advance(self) -> str | None:
        while self.index < len(self.roster) and self.roster[self.index][0] in self.spawned:
            self.index += 1
        if self.index >= len(self.roster):
            self.phase = "raid"
            return self.poll()
        name, class_id = self.roster[self.index]
        if name in self.owned:
            self.phase = "spawn"
            return self.poll()
        self.waiting = f"botcreate {name} {class_id} 1 0"
        return self.waiting

    def _finish_list(self) -> None:
        blob = "\n".join(self._list)
        self.waiting = ""
        lowered = blob.lower()
        if self.phase == "confirm":
            name = self.roster[self.index][0]
            if name.lower() in lowered and "owned by" in lowered:
                self.owned.add(name)
                self.phase = "spawn"
            else:
                self.index += 1
                self.phase = "create" if self.index < len(self.roster) else "raid"
            return
        for name, _class_id in self.roster:
            if name.lower() in lowered and "owned by" in lowered:
                self.owned.add(name)
        self.phase = "create"

    def _on_create(self, message: str) -> bool:
        name = self.roster[self.index][0]
        text = message.lower()
        if "already being used" in text:
            self.phase = "confirm"
            return True
        if "bot created" in text:
            self.owned.add(name)
            self.phase = "spawn"
            return True
        if is_limit(message):
            self._hit_limit()
            return True
        return False

    def _on_spawn(self, message: str) -> bool:
        name = self.roster[self.index][0]
        if is_spawned(message):
            self.spawned.add(name)
            self.index += 1
            self.phase = "create" if self.index < len(self.roster) else "raid"
            return True
        if is_limit(message):
            self._hit_limit()
            return True
        return False

    def _hit_limit(self) -> None:
        self.stopped = True
        self.phase = "raid" if self.spawned else "done"
