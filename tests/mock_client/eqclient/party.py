"""Build a bot group (default) or raid with commands the server already accepts."""

from __future__ import annotations

import os
import time

# Class codes the ^botcreate command already accepts. Human, male.
# Corpse-clear / tough camps: 30 bots (player + raid).
# Letter suffixes only — digits are prohibited in bot names. No Human Shaman.
ROSTER = (
    ("war", 1),
    ("wara", 1),
    ("warb", 1),
    ("warc", 1),
    ("clr", 2),
    ("clra", 2),
    ("clrb", 2),
    ("clrc", 2),
    ("pal", 3),
    ("pala", 3),
    ("palb", 3),
    ("enc", 14),
    ("enca", 14),
    ("encb", 14),
    ("wiz", 12),
    ("wiza", 12),
    ("wizb", 12),
    ("mag", 13),
    ("maga", 13),
    ("magb", 13),
    ("dru", 6),
    ("drua", 6),
    ("drub", 6),
    ("shd", 5),
    ("shda", 5),
    ("rog", 9),
    ("roga", 9),
    ("mnk", 7),
    ("mnka", 7),
    ("brd", 8),
)

# Regular content: tank, heal, mez, dps (group of 6 including the player → 5 bots).
GROUP_ROSTER = (
    ("war", 1),
    ("clr", 2),
    ("enc", 14),
    ("wiz", 12),
    ("rog", 9),
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
    """botlist, botcreate, botspawn, then group invite (or raidform when raid=True)."""

    def __init__(self, character: str, prefix: str | None = None, *, raid: bool = False) -> None:
        stem = bot_prefix(character, prefix)
        codes = ROSTER if raid else GROUP_ROSTER
        self.character = character
        self.raid = raid
        self.roster = [((stem + code)[:15], class_id) for code, class_id in codes]
        self.owned: set[str] = set()
        self.spawned: set[str] = set()
        self.index = 0
        self.invite_index = 0
        # Camp leftovers first — old raid spawns would all ^attack and starve XP.
        self.phase = "camp"
        self.waiting = ""
        self.waiting_at = 0.0
        self.formed = False
        self.stopped = False
        self.blocked = False  # camp/spawn refused (raid/group engaged)
        self._list: list[str] = []
        self._roster_names = {name for name, _ in self.roster}

    def poll(self) -> str | None:
        if self.formed:
            return None
        # Stale waiting (spawn reply drowned by combat chat) — clear and retry.
        if self.waiting and self.waiting_at and (time.monotonic() - self.waiting_at) > 8.0:
            print(f"party wait timeout → {self.waiting}", flush=True)
            self.waiting = ""
            self.waiting_at = 0.0
            if self.phase == "spawn":
                self.phase = "create"
        if self.waiting:
            return None
        if self.stopped and self.phase not in {"raid", "group", "follow", "summon"}:
            return None
        if self.blocked:
            return None
        if self.phase == "summon":
            # Same dynamic zone re-login keeps bots spawned — pull them in first.
            self.phase = "list"
            return "botsummon spawned"
        if self.phase == "camp":
            # Drop every spawned bot, then recreate only the group/raid roster.
            self.spawned.clear()
            self.phase = "list"
            return "botcamp spawned"
        if self.phase == "list":
            self._list = []
            self.waiting = "botlist"
            self.waiting_at = time.monotonic()
            return "botlist"
        if self.phase == "confirm":
            self._list = []
            self.waiting = "botlist"
            self.waiting_at = time.monotonic()
            return "botlist"
        if self.phase == "create":
            return self._create_or_advance()
        if self.phase == "spawn":
            name = self.roster[self.index][0]
            self.waiting = f"botspawn {name}"
            self.waiting_at = time.monotonic()
            return self.waiting
        if self.phase == "raid":
            if not self.spawned:
                self.formed = False
                self.phase = "done"
                return None
            self.phase = "follow"
            return "raidform all"
        if self.phase == "group":
            names = sorted(self.spawned)
            if self.invite_index >= len(names):
                self.phase = "follow"
                return self.poll()
            name = names[self.invite_index]
            self.invite_index += 1
            # Agent turns this into OP_GroupInvite (bots accept via ProcessBotGroupInvite).
            return f"groupinvite {name}"
        if self.phase == "follow":
            self.formed = True
            self.phase = "done"
            # Reset follow to owner for every spawned bot (bare `follow` is invalid).
            return "follow reset spawned"
        return None

    def on_zone_enter(self) -> None:
        """Same-zone re-login keeps bots — summon first, then list/fill gaps (no camp)."""
        self.formed = False
        self.spawned.clear()
        self.invite_index = 0
        self.index = 0
        self.waiting = ""
        self.waiting_at = 0.0
        self.stopped = False
        self.blocked = False
        self.phase = "summon"

    def note_blocked(self, message: str) -> bool:
        """Camp/spawn refused while raid/group is engaged — pause until agent clears it."""
        text = message.lower()
        if "cannot camp or spawn" not in text:
            return False
        self.blocked = True
        self.waiting = ""
        self.waiting_at = 0.0
        self.phase = "camp"
        print(f"party blocked: {message.strip()[:80]}", flush=True)
        return True

    def clear_block(self) -> None:
        """Resume after leaving raid / combat ended."""
        if not self.blocked:
            return
        self.blocked = False
        self.phase = "camp"
        self.waiting = ""
        self.waiting_at = 0.0
        self.spawned.clear()
        self.invite_index = 0
        self.index = 0
        print("party unblocked → camp", flush=True)

    def combat_order(self, verb: str, target: str = "") -> str | None:
        """Bot command after the group is up: attack, guard, hold, follow.

        Bare `follow`/`guard`/`hold` default to ActionableBot `target`, which
        `follow` rejects — always pass `spawned` (and `reset` so follow is the owner).
        """
        if not self.formed:
            return None
        verb = verb.lower().strip()
        if verb not in {"attack", "guard", "hold", "follow"}:
            return None
        if verb == "attack" and target:
            return f"attack {target}"
        if verb == "follow":
            return "follow reset spawned"
        if verb in {"guard", "hold"}:
            return f"{verb} spawned"
        return verb

    def push(self, message: str) -> None:
        if self.note_blocked(message):
            return
        if self.waiting == "botlist":
            # Accumulate the full botlist; finishing on the first line missed owned bots.
            self._list.append(message)
            lowered = message.lower()
            if (
                "bots shown" in lowered
                or "creation limits" in lowered
                or "you have no bots" in lowered
                or "do not own any bots" in lowered
            ):
                self._finish_list()
            return
        if not self.waiting:
            return
        if self.waiting.startswith("botcreate") and self._on_create(message):
            self.waiting = ""
            self.waiting_at = 0.0
            return
        if self.waiting.startswith("botspawn") and self._on_spawn(message):
            self.waiting = ""
            self.waiting_at = 0.0

    def _form_phase(self) -> str:
        return "raid" if self.raid else "group"

    def _create_or_advance(self) -> str | None:
        while self.index < len(self.roster) and self.roster[self.index][0] in self.spawned:
            self.index += 1
        if self.index >= len(self.roster):
            self.phase = self._form_phase()
            return self.poll()
        name, class_id = self.roster[self.index]
        if name in self.owned:
            self.phase = "spawn"
            return self.poll()
        self.waiting = f"botcreate {name} {class_id} 1 0"
        self.waiting_at = time.monotonic()
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
                self.phase = "create" if self.index < len(self.roster) else self._form_phase()
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
        if "invalid race-class" in text:
            self.index += 1
            self.phase = "create" if self.index < len(self.roster) else self._form_phase()
            return True
        if is_limit(message):
            self._hit_limit()
            return True
        return False

    def _on_spawn(self, message: str) -> bool:
        name = self.roster[self.index][0]
        text = message.lower()
        if is_spawned(message):
            self.spawned.add(name)
            self.index += 1
            self.phase = "create" if self.index < len(self.roster) else self._form_phase()
            return True
        # Name exists but spawn did not land — treat as owned and keep going.
        if "already being used" in text or "prohibited" in text:
            self.owned.add(name)
            self.index += 1
            self.phase = "create" if self.index < len(self.roster) else self._form_phase()
            return True
        if is_limit(message):
            self._hit_limit()
            return True
        return False

    def _hit_limit(self) -> None:
        self.stopped = True
        self.phase = self._form_phase() if self.spawned else "done"
