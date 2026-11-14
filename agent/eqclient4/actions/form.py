import json
import os
import random
import re
import time
from collections import defaultdict
from pathlib import Path
from typing import TYPE_CHECKING, Sequence

from eqclient4.structs.constants import (
    CLASS_ID_TO_CODE,
    CLASS_ID_TO_NAME,
    CLASS_NAME_TO_ID,
    CREATE_COMBINATIONS_RACE_TO_BITMASK,
    DPS_CLASSES,
    GOOD_ALIGNED_RACES,
    HEALER_CLASSES,
    RACE_ID_TO_BIT,
    TANK_CLASSES,
)
from eqclient4.structs.messages import _SAYLINK

if TYPE_CHECKING:
    from eqclient4.world import World
    from eqclient4.loop import Loop

from eqclient4.action import Action
from eqclient4.bots import Bot
from eqclient4.data.items import ItemBook
from eqclient4.log import log
from eqclient4.structs import (
    SAY_CHANNEL,
    EQStruct,
    OP_ChannelMessage,
    OP_SimpleMessage,
    OP_SpecialMesg,
)

AGGRESSIVE = "5"

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

BOT_COUNT_RE = re.compile(r"(\d+) Of \d+ bots? shown, \d+ (?:are|is) owned by you.")
NO_BOTS_RE = re.compile(r"You have no bots.")
BOT_RESPONSE_RE = re.compile(
    r"Bot (\d+) \| (.*) is a Level (\d+) (\w+) (\w+) (\w+) owned by (\w+)\."
)


class FormParty(Action):

    def __init__(self, world: World, loop: Loop, raid: bool = False, reform: bool = False) -> None:
        super().__init__(world, loop)
        self.priority = 290
        self.raid = raid
        self.phase: str | None = None

    def opcodes(self) -> tuple[str, ...]:
        return tuple(
            set(super().opcodes() + ("OP_ChannelMessage", "OP_SpecialMesg", "OP_SimpleMessage"))
        )

    def has_response(self, texts: Sequence[str]) -> EQStruct | None:
        pop_idx: int | None = None
        for idx, msg in enumerate(self.messages):
            match msg:
                case OP_ChannelMessage():
                    if msg.text in texts:
                        pop_idx = idx
                        break
                case OP_SpecialMesg():
                    if msg.message in texts:
                        pop_idx = idx
                        break
                case _:
                    log.error(f"Unknown message type in inbox: {msg}")
                    return None

        if pop_idx is not None:
            ret = self.messages.pop(pop_idx)
            return ret

        return None

    def re_has_response(self, matcher: re.Pattern) -> re.Match | None:
        pop_idx: int | None = None
        m: re.Match | None = None
        for idx, msg in enumerate(self.messages):
            match msg:
                case OP_ChannelMessage():
                    m = matcher.match(msg.text)
                    if m:
                        pop_idx = idx
                        break
                case OP_SpecialMesg():
                    if matcher.match(msg.message):
                        pop_idx = idx
                        m = matcher.match(msg.message)
                        break
                case _:
                    log.error(f"Unknown message type in inbox: {msg}")
                    return None

        if pop_idx is not None:
            self.messages.pop(pop_idx)
            return m

        return None

    def create_missing_bots(self) -> None:
        for bot in self._world.bot_roster.all_bots():
            if bot.created:
                continue

            self._loop.send(
                "OP_ChannelMessage",
                OP_ChannelMessage(
                    "",
                    self._world.character.name,
                    100,
                    SAY_CHANNEL,
                    0,
                    0,
                    100,
                    f"^create {bot.name} {bot.class_id} {bot.race} {bot.gender}",
                ).serialize(),
            )
            self._loop._flush()
            time.sleep(0.2)

    def read_existing_bots(self) -> None:
        m: re.Match | None = self.re_has_response(BOT_RESPONSE_RE)

        while m:
            sl = _SAYLINK.match(m.group(2))
            bot_name = m.group(2)
            if sl:
                bot_name = sl.group(2)

            bot = self._world.bot_roster.bot_by_name(bot_name)
            if not bot:
                log.error(f"Bot {bot_name} not found in roster")
                continue

            bot.created = True
            m = self.re_has_response(BOT_RESPONSE_RE)

    def creation(self) -> None:
        if not self.waiting_for("botlist"):
            return

        count = self.re_has_response(BOT_COUNT_RE)
        log.info(f"Bot count: {count}")
        no_bots = self.re_has_response(NO_BOTS_RE)
        log.info(f"No bots: {no_bots}")

        if not count and not no_bots:
            log.info(f"No count or no bots - waiting")
            return

        if no_bots:
            log.info(f"No bots - creating missing bots")
            self.create_missing_bots()
            self.unwait("botlist")
            self.phase = None
            return

        if count:
            # Existing bots are sent before the count
            self.read_existing_bots()
            count_int = int(count.group(1))

            # Everyone exists, let's proceed
            if count_int >= len(list(self._world.bot_roster.all_bots())):
                log.info(f"Bot count matches roster count: {count}")
                self.unwait("botlist")
                self.phase = "spawn"
                self._world.bot_roster.save()
                return

            log.info(f"Creating missing bots - some existing")
            # Retrigger botlist command to ensure all bots exist
            self.create_missing_bots()
            self.unwait("botlist")
            self.phase = None
            return

    def send_list(self) -> bool:
        log.info(f"No phase")
        if any(not bot.created for bot in self._world.bot_roster.all_bots()):
            log.info(f"Some bots are not created - waiting for botlist")
            self.wait("botlist")

            self._loop.send(
                "OP_ChannelMessage",
                OP_ChannelMessage(
                    "",
                    self._world.character.name,
                    100,
                    SAY_CHANNEL,
                    0,
                    0,
                    100,
                    "^botlist",
                ).serialize(),
            )
            return True

        self.phase = "spawn"
        return False

    def spawn(self) -> None:
        log.info(f"Spawning bots")

        for bot in self._world.bot_roster.all_bots():
            if bot.spawned:
                continue
            self._loop.send(
                "OP_ChannelMessage",
                OP_ChannelMessage(
                    "",
                    self._world.character.name,
                    100,
                    SAY_CHANNEL,
                    0,
                    0,
                    100,
                    f"^spawn {bot.name}",
                ).serialize(),
            )
            self._loop._flush()
            time.sleep(0.1)

        self.phase = "confirm-spawn"

    def wait_on_spawns(self) -> bool:
        for bot in self._world.bot_roster.all_bots():
            if not bot.spawned:
                return True

        self.phase = "configure"

        return False

    def step(self) -> None:

        self.creation()

        if self.phase == "spawn":
            self.spawn()

        if not self.phase and self.send_list():
            return

        if self.wait_on_spawns():
            return

        log.info(f"Finishinng on {self.phase} seconds")

        # Reconstitute or create the party
        self.complete = True
