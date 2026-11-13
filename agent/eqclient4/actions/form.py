import json
import os
import random
from collections import defaultdict
from pathlib import Path
from typing import TYPE_CHECKING

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

if TYPE_CHECKING:
    from eqclient4.world import World
    from eqclient4.loop import Loop

from eqclient4.action import Action
from eqclient4.bots import Bot
from eqclient4.data.items import ItemBook
from eqclient4.structs.messages import (
    SAY_CHANNEL,
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


class FormParty(Action):

    def __init__(self, world: World, loop: Loop, raid: bool = False, reform: bool = False) -> None:
        super().__init__(world, loop)
        self.priority = 290
        self.raid = raid
        self.built = False
        self.phase = "reform" if reform else "spawn"

        self.command_idx = 0
        self.pending_commands = []

    def opcodes(self) -> tuple[str, ...]:
        return tuple(
            set(super().opcodes() + ("OP_ChannelMessage", "OP_SpecialMesg", "OP_SimpleMessage"))
        )

    def step(self) -> None:
        self._loop.send(
            "OP_ChannelMessage",
            OP_ChannelMessage(
                "", self._world.character.name, 100, SAY_CHANNEL, 0, 0, 100, "Hello, world!"
            ).serialize(),
        )

        self._loop.send(
            "OP_ChannelMessage",
            OP_ChannelMessage(
                "", self._world.character.name, 100, SAY_CHANNEL, 0, 0, 100, "Hello, world! 2"
            ).serialize(),
        )

        self._loop.send(
            "OP_ChannelMessage",
            OP_ChannelMessage(
                "", self._world.character.name, 100, SAY_CHANNEL, 0, 0, 100, "Hello, world! 3"
            ).serialize(),
        )
        # Reconstitute or create the party
        self.complete = True

    def expecting_text(self) -> bool:
        return False
