import re
import time
from dataclasses import dataclass
from typing import TYPE_CHECKING

from eqclient4.structs.constants import (
    CLASS_NAME_TO_ID,
    HEALER_CLASSES,
    TANK_CLASSES,
)
from eqclient4.structs.messages import _SAYLINK

if TYPE_CHECKING:
    from eqclient4.world import World
    from eqclient4.loop import Loop

from eqclient4.action import Action
from eqclient4.bots import Bot
from eqclient4.data.bot_spells import _BOT_ROLES, _CASTERS
from eqclient4.log import log
from eqclient4.structs import (
    SAY_CHANNEL,
    EQStruct,
    OP_ChannelMessage,
    OP_Consider,
    OP_GroupInvite,
    OP_SpecialMesg,
    OP_TargetMouse,
)

AGGRESSIVE = "5"
BURN = "7"
REPLY_TIMEOUT = 8.0

BOT_COUNT_RE = re.compile(r"(\d+) Of \d+ bots? shown, \d+ (?:are|is) owned by you\.")
NO_BOTS_RE = re.compile(r"You have no bots\.")
BOT_RESPONSE_RE = re.compile(
    r"Bot (\d+) \| (.*) is a Level (\d+) (\w+) (\w+(?:\s+\w+)?) (\w+) owned by (\w+)\."
)
RAID_FORMED_RE = re.compile(
    r"Bot raid formed\. (\d+) bots spawned, (\d+) newly joined, (\d+) left out\."
)


@dataclass
class _Command:
    text: str
    response_pattern: str
    failure_patterns: list[str]
    bot: Bot | None = None
    setting: str = ""
    value: str = ""
    target: bool = False
    sent: bool = False
    ticks_waited: int = 0
    recv: bool = False
    recv_response: re.Match | None = None
    failure_msg: str | None = None


class FormParty(Action):

    def __init__(self, world: World, loop: Loop, raid: bool = False) -> None:
        super().__init__(world, loop)
        self.priority = 290
        self.raid = raid
        self.start_time = time.time()
        self._commands: list[_Command] = []
        self.wait("init")

    def opcodes(self) -> tuple[str, ...]:
        return (
            "OP_ChannelMessage",
            "OP_SpecialMesg",
            "OP_SimpleMessage",
            "OP_TargetMouse",
            "OP_Consider",
        )

    def bot_target(self) -> None:
        if not self.target_id:
            return

        bot = self._world.bot_roster.bot_by_spawn_id(self.target_id)
        if not bot:
            return

        if self.mob_targeted != self.target_id:
            previous = self._world.bot_roster.bot_by_spawn_id(self.mob_targeted)
            if previous:
                previous.targeted = False
            self.wait("bot-target")

        if not self._world.line_of_sight(bot.position):
            self.send_channel_message(f"^botsummon byname {bot.name}")
            return

        if self.mob_targeted == self.target_id:
            return

        if not self.target_sent:
            self._loop.send(
                "OP_TargetMouse",
                OP_TargetMouse(int(self.target_id) & 65535).serialize(),
            )
            self.target_sent = True
            return

        if not self._consider_sent:
            self._loop.send(
                "OP_Consider",
                OP_Consider(
                    player_id=int(self._world.self_id or 0), target_id=int(self.target_id) & 65535
                ).serialize(),
            )
            self._consider_sent = True
            return

        message = self.consume("OP_Consider", self.con_matcher)
        if message:
            bot.targeted = True
            self.mob_targeted = self.target_id
            self.unwait("bot-target")
            self.target_sent = False
            self._consider_sent = False
            return

    def step(self) -> None:
        self.bot_target()
        if self.waiting_for("bot-target"):
            return

        if self.waiting_for("init"):
            self.send_list()
            return

        if self.waiting_for("botlist"):
            self.creation()
            return

        if self.waiting_for("spawn"):
            self.spawn()
            return

        if self.waiting_for("spawn-confirm"):
            self.wait_on_spawns()
            return

        if self.waiting_for("group-formation"):
            self.group_formation()
            return

        if self.waiting_for("configure"):
            self.configure()
            return

        if self.waiting_for("send-commands"):
            self.send_commands()
            return

        log.info(f"Finished forming party in {time.time() - self.start_time} seconds")
        # Reconstitute or create the party
        self.complete = True

    def send_list(self) -> None:
        """State transition: init -> botlist | spawn

        botlist when a bot hasn't been saved with created=True
        spawn when all bots have been previously created
        """
        self.unwait("init")

        if any(not bot.created for bot in self._world.bot_roster.all_bots()):
            log.info(f"Some bots are not created - waiting for botlist")
            self.wait("botlist")

            self.send_channel_message("^botlist")
            return

        self.wait("spawn")

    def creation(self) -> None:
        """State transition: botlist -> init | spawn

        init after creation has been sent in order to ensure all of the bots have been created
           Bot creation is updated in the MobHandler after server confirmation

        spawn after we have have fully read a botlist command and confirmed all bots exist
        """
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
            self.wait("init")  # Triggers new botlist -> read_existing_bots -> creation
            return

        if count:
            # Existing bots are sent before the count
            self.read_existing_bots()

            # Everyone exists, let's proceed
            if all(bot.created for bot in self._world.bot_roster.all_bots()):
                log.info(f"Bot count matches roster count: {count}")
                self.unwait("botlist")
                self.wait("spawn")
                self._world.bot_roster.save()
                return

            log.info(f"Creating missing bots - some existing")

            # Retrigger botlist command to ensure all bots exist
            self.create_missing_bots()
            self.unwait("botlist")
            self.wait("init")
            return

    def spawn(self) -> None:
        """State transition: spawn -> spawn-confirm

        spawn-confirm after all bots have had their spawn sent
        """
        log.info(f"Spawning bots")
        for bot in self.action_bots():
            if bot.spawned:
                continue

            self.send_channel_message(f"^spawn {bot.name}")

        self.unwait("spawn")
        self.wait("spawn-confirm")

    def wait_on_spawns(self) -> None:
        """State transition: spawn-confirm -> configure

        configure after all bots have had their spawn confirmed,
        spawn is set in the MobHandler
        """
        for bot in self.action_bots():
            if not bot.spawned:
                return

        self.unwait("spawn-confirm")
        self.wait("group-formation")

    def group_formation(self) -> None:
        """State transition:
            1. group-formation -> raid-formation -> configure
            2. group-formation -> target x6 -> configure


        complete after all bots have had their group formation sent
        """

        # Raid formation
        if self.raid:
            if self.waiting_for("raid-formation"):
                reply = self.re_has_response(RAID_FORMED_RE)
                if not reply:
                    return

                if int(reply.group(3)):
                    log.warning(
                        f"Raid formation did not seat all spawned roster bots: {reply.group(0)}"
                    )
                self.unwait("raid-formation")
                self.unwait("group-formation")
                self.wait("configure")
                return

            self.send_channel_message("^raidform all")
            self.wait("raid-formation")
            return

        # Group Formation
        bot_ids = sorted([bot.spawn_id for bot in self.action_bots()])

        first_bot_not_in_group: int | None = None
        for bot_id in bot_ids:
            if bot_id not in self._world.active_group:
                first_bot_not_in_group = bot_id
                break

        log.info(
            f"First bot not in group: {first_bot_not_in_group} {self._world.active_group} - mob targeted: {self.mob_targeted}"
        )

        if first_bot_not_in_group is None:
            # All bots are in the group
            self.unwait("group-formation")
            self.unwait("group-invite")
            self.wait("configure")
            return

        if self.mob_targeted is not None and self.mob_targeted == first_bot_not_in_group:
            # target succeeded
            if self.waiting_for("group-invite"):
                return
            target = self._world.bot_roster.bot_by_spawn_id(self.mob_targeted)

            assert target
            self._loop.send(
                "OP_GroupInvite",
                OP_GroupInvite(
                    target.name,
                    self._world.character.name,
                ).serialize(),
            )
            self.wait("group-invite")
            return

        log.info(f"Targeting bot: {self.target_id}")
        self.target_id = first_bot_not_in_group
        self.unwait("group-invite")
        return

    def configure(self) -> None:
        """State transition: configure -> complete

        complete after all bots have had their configuration sent
        """
        self._commands.append(
            _Command(
                "^follow reset spawned",
                r"(?:\d+ of your bots are following you\.|\w+ says, 'Following [^']+\.')",
                []
            )
        )

        clerics = sorted(
            self.filter_by_class("Cleric"),
            key=lambda x: x.id
        )
        if clerics:
            clr = clerics[0]
        
            self._commands.extend([
                _Command(
                    f"^healrotationstop {clr.name}",
                    rf"{clr.name}'s Heal Rotation is now inactive|{clr.name}'s Heal Rotation is already inactive",
                    [
                        rf"{clr.name}'s is not a current member of a Heal Rotation",
                        rf"Failed to stop {clr.name}'s Heal Rotation",
                    ],
                    clr,
                ),
                _Command(
                    f"^healrotationcleartargets {clr.name}",
                    rf"All targets have been cleared from {clr.name}'s Heal Rotation",
                    [
                        rf"{clr.name}'s is not a current member of a Heal Rotation",
                        rf"Failed to clear all targets from {clr.name}'s Heal Rotation",
                    ],
                    clr,
                ),
                _Command(
                    f"^healrotationremovemember {clr.name}",
                    rf"{clr.name} has been removed from their Heal Rotation",
                    [
                        rf"{clr.name} is not a current member of a Heal Rotation",
                        rf"Failed to remove {clr.name} from their Heal Rotation",
                    ],
                    clr,
                ),
                _Command(
                    f"^healrotationdelete {clr.name}",
                    rf"Succeeded in deleting {clr.name}'s heal rotation",
                    [rf"Failed to delete {clr.name}'s heal rotation"],
                    clr,
                ),
                _Command(
                    f"^healrotationcreate {clr.name} 3 on on on",
                    rf"Successfully added {clr.name} as a current member to a new Heal Rotation",
                    [
                        rf"Successfully loaded {clr.name}'s Heal Rotation",
                        rf"{clr.name} is already a current member of a Heal Rotation",
                    ],
                    clr,
                )
            ])

        for bot in self.action_bots():
            if not bot.spawned:
                continue

            self.bot_commands(bot)

        self.unwait("configure")
        self.wait("send-commands")

    def send_commands(self) -> None:
        """State transition: send-commands -> complete

        complete after all commands have been sent
        """
        for command in self._commands:

            if command.recv or command.failure_msg:
                continue

            if command.target:
                assert command.bot
                if not self.mob_targeted == command.bot.spawn_id:
                    self.target_id = command.bot.spawn_id
                    return

            if not command.sent:
                self.send_channel_message(command.text)
                command.sent = True
            
            success_pattern = re.compile(command.response_pattern)
            success = self.re_has_response(success_pattern)


            failure = None
            if len(command.failure_patterns) > 0:
                failure_pattern = re.compile(f"({'|'.join(command.failure_patterns)})")
                failure = self.re_has_response(failure_pattern)
            else:
                log.warning(f"No failure patterns provided for command: {command.text}")

            if command.ticks_waited > 40:
                log.error(f"Command {command.text} timed out after 30 ticks")
                command.failure_msg = "fail: timeout"
                return

            command.ticks_waited += 1

            if not failure and not success:
                return

            if failure:
                command.failure_msg = failure.group(0)
                return

            if not success:
                log.debug(f"Waiting for response to command: {command.text}")
                return

            command.recv = True
            command.recv_response = success

            if command.bot and command.text.startswith("^healrotationcreate"):
                self.rotation_commands(command.bot, success.group(0))

            if command.bot and command.setting:
                settings = command.bot.settings or {}
                if command.setting == "stance":
                    for key in ("spellholds", "sit", "stop_melee", "follow"):
                        settings.pop(key, None)
                settings[command.setting] = command.value
                command.bot.settings = settings
                self._world.bot_roster.save()

        self.unwait("send-commands")

    def bot_commands(self, bot: Bot) -> None:

        name = bot.name
        saved = bot.settings or {}

        stance = (
            AGGRESSIVE if bot.class_id in TANK_CLASSES else BURN if bot.class_id in _CASTERS else ""
        )
        changed_stance = bool(stance and saved.get("stance") != stance)
        if changed_stance:
            label = "Aggressive" if stance == AGGRESSIVE else "Burn"
            self._commands.append(
                _Command(
                    f"^botstance {stance} byname {name}",
                    rf"{name} says, 'I am now set to the stance \[{label}\]",
                    [],  # fill in
                    bot,
                    "stance",
                    stance,
                )
            )

        if bot.class_id in _CASTERS:
            # Stance changes load stance-specific defaults, so reapply these settings.
            for key, value, command, response in (
                (
                    "spellholds",
                    "0",
                    f"^spellholds 0 0 byname {name}",
                    r"My \[[^\]]+\] spell hold was \[disabled\]",
                ),
                (
                    "sit",
                    "90",
                    f"^sitmanapercent 90 byname {name}",
                    r"I will now sit in combat whe[mn] at or below \[90%\] mana",
                ),
                (
                    "stop_melee",
                    "1",
                    f"^botstopmeleelevel 1 byname {name}",
                    r"My stop melee level was set to 1\.",
                ),
                (
                    "follow",
                    "10",
                    f"^botfollowdistance set 10 byname {name}",
                    r"Following [^']+ at a distance of 10(?:\.0+)?\.",
                ),
            ):
                if not changed_stance and saved.get(key) == value:
                    continue

                self._commands.append(
                    _Command(
                        command,
                        rf"{name} says, '{response}",
                        [],  # fill in
                        bot,
                        key,
                        value,
                    )
                )

            # spellsettingsadd is target-only. Remember each confirmed spell, rather
            # than a single flag that would miss spells unlocked at later levels.
            roles = _BOT_ROLES.get(bot.class_id, set())
            level = bot.level or self._world.character.level or 1
            for spell in self._world.bot_spells.roles_available(bot.class_id, level, roles):
                key = f"spell:{spell.spell_id}"
                if key in saved:
                    continue

                spell_id = spell.spell_id
                self._commands.append(
                    _Command(
                        f"^spellsettingsadd {spell_id} {max(1, spell.priority)} 0 100",
                        rf"Spell Setting Added \| Spell: .* \({spell_id}\)",
                        [
                            rf"{name} already has a spell setting for .* \({spell_id}\)",
                        ],
                        bot,
                        key,
                        "1",
                        target=True,
                    )
                )

    def rotation_commands(self, healer: Bot, response: str) -> None:
        loaded = "successfully loaded" in response.lower()
        if loaded:
            # Don't recreate a loaded rotation
            return

        # existing = "already a current member" in response.lower()

        # A fresh rotation has no persisted server-side members or targets.
        for bot in self.action_bots():
            if not bot.spawned:
                continue

            if bot is healer or bot.class_id not in HEALER_CLASSES:
                continue

            self._commands.append(
                _Command(
                    f"^healrotationaddmember {bot.name} {healer.name}",
                    rf"Successfully added {bot.name} as a current member of this Heal Rotation",
                    [
                        rf"{bot.name} is already a current member",
                        rf"Failed to add {bot.name} as a current member to a new Heal Rotation",
                    ],
                )
            )

        targets = [self._world.character.name] + [
            bot.name for bot in self.action_bots() if bot.class_id in TANK_CLASSES
        ]

        for target in targets:
            self._commands.append(
                _Command(
                    f"^healrotationaddtarget {target} {healer.name}",
                    rf"Successfully added heal target {target} to {healer.name}'s Heal Rotation",
                    [
                        rf"Failed to add heal target with a name of '{target}'",
                        rf"No target exists by the name '{target}'",
                    ],
                )
            )

        _adjust_map = {
            0: (60, 85),
            1: (70, 90),
            2: (65, 85),
            3: (60, 80),
            4: (55, 80),
        }
        for armor, (critical, safe) in _adjust_map.items():
            self._commands.extend([
                _Command(
                    f"^healrotationadjustsafe {armor} {safe} {healer.name}",
                    rf"Class Armor Type \d+ safe value \d+(?:\.\d+)? set for {healer.name}'s Heal Rotation",
                    [rf"Safe value \d+(?:\.\d+)?%(\d+) does not exceed critical value \d+(?:\.\d+)?%(\d+) for {healer.name}'s Heal Rotation"],
                    healer,
                ),
                _Command(
                    f"^healrotationadjustcritical {armor} {critical} {healer.name}",
                    rf"Class Armor Type \d+ critical value \d+(?:\.\d+)? set for {healer.name}'s Heal Rotation",
                    [rf"Critical value \d+(?:\.\d+)?%(\d+) exceeds safe value \d+(?:\.\d+)?%(\d+) for {healer.name}'s Heal Rotation"],
                    healer,
                ),
            ])

        self._commands.append(
            _Command(
                f"^healrotationsave {healer.name}",
                rf"Succeeded in saving {healer.name}'s heal rotation",
                [
                    rf"Failed to save heal rotation members",
                    rf"Failed to save heal rotation targets",
                    rf"{healer.name} is not a current member of a Heal Rotation",
                ],
                healer,
                "heal",
                "1",
            )
        )

        # A saved rotation is loaded by healrotationcreate, but is not active
        # until started. Do not recreate or overwrite an existing live rotation.
        self._commands.append(
            _Command(
                f"^healrotationstart {healer.name}",
                rf"{healer.name}'s Heal Rotation is (?:now|already) active",
                [
                    rf"Failed to start {healer.name}'s Heal Rotation", 
                    rf"{healer.name} is not a current member of a Heal Rotation",
                ],
                healer if loaded else None,
                "heal" if loaded else "",
                "1",
            )
        )
        self._commands.append(_Command(
            f"^healrotationlist {healer.name}",
            r"^Heal Rotation Targets:$",
            [
                rf"{healer.name} is not a current member of a Heal Rotation",
                r"\(0\) None",
            ],
            healer,
        ))

    def re_has_response(self, matcher: re.Pattern) -> re.Match | None:
        def _message_text(msg: EQStruct) -> str:
            match msg:
                case OP_ChannelMessage():
                    return msg.text
                case OP_SpecialMesg():
                    return msg.message
                case _:
                    return ""

        for idx, msg in enumerate(self.messages):
            text = _message_text(msg)
            if m := matcher.search(text):
                self.messages.pop(idx)
                return m
        return None

    def action_bots(self) -> list[Bot]:
        bots = list(self._world.bot_roster.group.values())
        if self.raid:
            bots = list(self._world.bot_roster.all_bots())
        return bots

    def filter_by_class(self, class_name: str) -> list[Bot]:
        output :list[Bot] = []
        for bot in self.action_bots():
            if bot.class_id == CLASS_NAME_TO_ID[class_name]:
                output.append(bot)
        return output

    def create_missing_bots(self) -> None:
        for bot in self._world.bot_roster.all_bots():
            if bot.created:
                continue

            self.send_channel_message(f"^create {bot.name} {bot.class_id} {bot.race} {bot.gender}")

    def read_existing_bots(self) -> None:
        m: re.Match | None = self.re_has_response(BOT_RESPONSE_RE)

        while m:
            log.info(f"Reading existing bot: {m.group(0)}")

            bot_number = int(m.group(1))

            sl = _SAYLINK.match(m.group(2))
            bot_name = m.group(2)
            if sl:
                bot_name = sl.group(2)

            bot = self._world.bot_roster.bot_by_name(bot_name)
            if not bot:
                log.error(f"Bot {bot_name} not found in roster")
                m = self.re_has_response(BOT_RESPONSE_RE)
                continue

            log.info(f"Bot {bot_name} found in roster setting created to True")
            bot.id = bot_number
            bot.created = True
            bot.level = int(m.group(3))
            m = self.re_has_response(BOT_RESPONSE_RE)

    def send_channel_message(self, message: str) -> None:
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
                message,
            ).serialize(),
        )
        self._loop._flush()
        time.sleep(0.1)
        self._loop.pump()
