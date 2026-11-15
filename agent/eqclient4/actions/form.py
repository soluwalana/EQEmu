import re
import time
from functools import partial
from typing import TYPE_CHECKING, Callable

from eqclient4.action import Action, Command
from eqclient4.bots import Bot
from eqclient4.data.bot_spells import _BOT_ROLES, _CASTERS
from eqclient4.log import log
from eqclient4.structs import (
    OP_Consider,
    OP_GroupDisband,
    OP_GroupInvite,
    OP_RaidInvite,
    OP_TargetMouse,
)
from eqclient4.structs.constants import (
    CLASS_NAME_TO_ID,
    HEALER_CLASSES,
    TANK_CLASSES,
)
from eqclient4.structs.messages import _SAYLINK

if TYPE_CHECKING:
    from eqclient4.loop import Loop
    from eqclient4.world import World

AGGRESSIVE = "5"
BURN = "7"
REPLY_TIMEOUT = 8.0

RAID_CLEAR_RE = re.compile(
    r"Bot raid roster will not form again until you .* The raid is unchanged\."
)
RAID_CLEAR_FAILURE_RE = re.compile(r"Could not update the bot raid roster\.")
RAID_CAMP_RE = re.compile(r"Bots camped\. Their raid seats are kept\.")

BOT_COUNT_RE = re.compile(r"(\d+) Of \d+ bots? shown, \d+ (?:are|is) owned by you\.")
NO_BOTS_RE = re.compile(r"You have no bots\.")
BOT_RESPONSE_RE = re.compile(
    r"Bot (\d+) \| (.*) is a Level (\d+) (\w+) (\w+(?:\s+\w+)?) (\w+(?:\s+\w+)?) owned by (\w+)\."
)
RAID_FORMED_RE = re.compile(
    r"Bot raid formed\. (\d+) bots spawned, (\d+) newly joined, (\d+) left out\."
)

BOT_COMMAND_FAILURES = [
    r"Bot commands not available\.",
    r"Your access level is not high enough to use this bot command\.",
    r"Bot command '[^']+' not recognized\.",
    r"Bot command \S+ is not enabled on this server\.",
    r"Undefined linker usage in \w+ \([^)]+\)",
    r"^[Uu]sage: ",
]

ACTIONABLE_FAILURES = [
    r"Command passed null 'ActionableBot' criteria",
    r"You have no spawned bots meeting this criteria - type: '[^']+'",
    r"This command does not allow 'ActionableBot' criteria '[^']+'",
]
HEAL_ROTATION_COMMON_FAILURES = [
    r"You must <target> or \[name\] a current member as a bot that you own to use this command",
    r"Error: Current member bot dereferenced to nullptr",
    r"\w+ is not a (?:current )?member of a Heal Rotation",
    *BOT_COMMAND_FAILURES,
]
BOT_LIST_FAILURE_RE = re.compile(
    "|".join(
        [
            r"You have no bots meeting this criteria\.",
            r"A numeric value or name is required to use the filter property of this command",
            *BOT_COMMAND_FAILURES,
        ]
    )
)
RAID_FORMATION_FAILURE_RE = re.compile(
    "|".join(
        [
            r"You do not own any bots\.",
            r"Could not save the bot raid roster\.",
            r"Bots are disabled on this server\.",
            r"The bot raid roster table is missing\.",
            r"You have no active bot raid roster\.",
            r"Leave your group before forming a bot raid\.",
            r"Could not create a raid\.",
            r"You must be level \d+ to spawn .*bots\.",
            r"You cannot camp or spawn bots while feigned\.",
            r"You cannot camp or spawn bots while your raid is engaged\.",
            r"You cannot camp or spawn bots while your group is engaged,",
            r"You cannot camp or spawn bots while you are engaged,",
            *BOT_COMMAND_FAILURES,
        ]
    )
)


class FormParty(Action):

    def __init__(self, world: World, loop: Loop, raid: bool = False) -> None:
        super().__init__(world, loop)
        self.priority = 290
        self.raid = raid
        self.start_time = time.time()
        self._reply_started = 0.0
        self.wait("formation-check")

    def opcodes(self) -> tuple[str, ...]:
        return (
            "OP_ChannelMessage",
            "OP_SpecialMesg",
            "OP_SimpleMessage",
            "OP_TargetMouse",
            "OP_Consider",
        )

    def step(self) -> None:
        super().step()
        if self.waiting_for("TARGET"):
            return

        if self.waiting_for("formation-check"):
            self.prepare_formation()
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

    def prepare_formation(self) -> None:
        """Leave an incompatible party before spawning or inviting bots."""
        mode = self.world.party_mode
        desired = "raid" if self.raid else "group"

        if self.waiting_for("raid-clear"):
            if not self.re_has_response(RAID_CLEAR_RE):
                self.check_failure(RAID_CLEAR_FAILURE_RE)
                return
            self.unwait("raid-clear")
            # Camp before disbanding: disband removes seats, not live bots.
            self.messages.clear()
            self._reply_started = time.monotonic()
            self.wait("raid-camp")
            self.send_channel_message("^raidform camp")
            return

        elif self.waiting_for("raid-camp"):
            if not self.re_has_response(RAID_CAMP_RE):
                self.check_failure(RAID_FORMATION_FAILURE_RE)
                return
            self.unwait("raid-camp")
            self.wait("raid-camp-despawn")
            self._reply_started = time.monotonic()
            return

        elif self.waiting_for("raid-camp-despawn"):
            # The acknowledgement can precede OP_DeleteSpawn. Do not reuse
            # stale spawn IDs when the existing group formation runs.
            if any(bot.spawned for bot in self.world.bot_roster.all_bots()):
                self.check_failure(RAID_FORMATION_FAILURE_RE)
                return
            self.unwait("raid-camp-despawn")

        elif self.waiting_for("party-disband"):
            if mode is not None:
                if time.monotonic() - self._reply_started >= REPLY_TIMEOUT:
                    log.error("Timed out leaving %s", mode)
                    self.waiting.clear()
                    self.failed = True
                    self.complete = True
                return
            self.unwait("party-disband")

        elif mode == "raid" and desired == "group":
            # Clear only the persisted auto-form flag, not the saved roster.
            self.messages.clear()
            self._reply_started = time.monotonic()
            self.wait("raid-clear")
            self.send_channel_message("^raidform clear")
            return

        if mode is not None and mode != desired:
            name = self.world.character.name
            self._reply_started = time.monotonic()
            self.wait("party-disband")
            if mode == "raid":
                # RaidCommandDisband (5): remove the owner and owned bots.
                self.loop.send("OP_RaidInvite", OP_RaidInvite(5, name, name).serialize())
            else:
                # The server uses the current target for group disband.
                # Clear it so the leader disbands rather than kicking a bot.
                self.loop.send("OP_TargetMouse", OP_TargetMouse(0).serialize())
                self.loop.send("OP_GroupDisband", OP_GroupDisband(name, name).serialize())
            return

        self.unwait("formation-check")
        self.wait("init")

    def send_list(self) -> None:
        """State transition: init -> botlist | spawn

        botlist when a bot hasn't been saved with created=True
        spawn when all bots have been previously created
        """
        self.unwait("init")

        if any(not bot.created for bot in self.world.bot_roster.all_bots()):
            log.info(f"Some bots are not created - waiting for botlist")
            self.wait("botlist")
            self._reply_started = time.monotonic()
            self.send_channel_message("^botlist")
            return

        self.wait("spawn")

    def check_failure(self, pattern: re.Pattern) -> None:
        failure = self.re_has_response(pattern)
        if failure or time.monotonic() - self._reply_started >= REPLY_TIMEOUT:
            log.error(f"Command Failed: {failure.group(0) if failure else 'reply timeout'}")
            self.waiting.clear()
            self.complete = True
            self.failed = True

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
            self.check_failure(BOT_LIST_FAILURE_RE)
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
            if all(bot.created for bot in self.world.bot_roster.all_bots()):
                log.info(f"Bot count matches roster count: {count}")
                self.unwait("botlist")
                self.wait("spawn")
                self.world.bot_roster.save()
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
                    self.check_failure(RAID_FORMATION_FAILURE_RE)
                    return

                if int(reply.group(3)):
                    log.warning(
                        f"Raid formation did not seat all spawned roster bots: {reply.group(0)}"
                    )
                self.unwait("raid-formation")
                self.unwait("group-formation")
                self.wait("configure")
                return

            self._reply_started = time.monotonic()
            self.send_channel_message("^raidform all")
            self.wait("raid-formation")
            return

        # Group Formation
        bot_ids = sorted([bot.spawn_id for bot in self.action_bots()])

        first_bot_not_in_group: int | None = None
        for bot_id in bot_ids:
            if bot_id not in self.world.active_group:
                first_bot_not_in_group = bot_id
                break

        log.info(
            f"First bot not in group: {first_bot_not_in_group} {self.world.active_group} - mob targeted: {self.mob_targeted}"
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
            target = self.world.bot_roster.bot_by_spawn_id(self.mob_targeted)

            assert target
            self.loop.send(
                "OP_GroupInvite",
                OP_GroupInvite(
                    target.name,
                    self.world.character.name,
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
        self.commands.append(
            Command(
                text="^follow reset spawned",
                response_pattern=r"(?:\d+ of your bots are following you\.|\w+ says, 'Following [^']+\.')",
                failure_patterns=[
                    r"You must <target> a friendly player, bot or merc within your group or raid to use this command",
                    r"\w+ says, 'I cannot follow myself, you want me to run circles\?",
                    *ACTIONABLE_FAILURES,
                    *BOT_COMMAND_FAILURES,
                ],
                success_callback=partial(log.info, "Follow reset spawned"),
                failure_callback=partial(log.error, "Failed to reset follow"),
            )
        )

        clerics = sorted(self.filter_by_class("Cleric"), key=lambda x: x.id)
        if clerics:
            clr = clerics[0]

            self.commands.extend(
                [
                    Command(
                        text=f"^healrotationstop {clr.name}",
                        response_pattern=rf"{clr.name}'s Heal Rotation is (?:now|already) inactive",
                        failure_patterns=[
                            rf"Failed to stop {clr.name}'s Heal Rotation",
                            *HEAL_ROTATION_COMMON_FAILURES,
                        ],
                        success_callback=partial(log.info, f"Heal rotation stopped for {clr.name}"),
                        failure_callback=partial(
                            log.error, f"Failed to stop heal rotation for {clr.name}"
                        ),
                    ),
                    Command(
                        text=f"^healrotationcleartargets {clr.name}",
                        response_pattern=rf"All targets have been cleared from {clr.name}'s Heal Rotation",
                        failure_patterns=[
                            rf"Failed to clear all targets from {clr.name}'s Heal Rotation",
                            *HEAL_ROTATION_COMMON_FAILURES,
                        ],
                    ),
                    Command(
                        text=f"^healrotationremovemember {clr.name}",
                        response_pattern=rf"{clr.name} has been removed from their Heal Rotation",
                        failure_patterns=[
                            rf"Failed to remove {clr.name} from their Heal Rotation",
                            *HEAL_ROTATION_COMMON_FAILURES,
                        ],
                        success_callback=partial(
                            log.info, f"Heal rotation cleared targets for {clr.name}"
                        ),
                        failure_callback=partial(
                            log.error, f"Failed to clear targets for {clr.name}"
                        ),
                    ),
                    Command(
                        text=f"^healrotationdelete {clr.name}",
                        response_pattern=rf"Succeeded in deleting {clr.name}'s heal rotation",
                        failure_patterns=[
                            rf"Failed to delete {clr.name}'s heal rotation",
                            *HEAL_ROTATION_COMMON_FAILURES,
                        ],
                        success_callback=partial(log.info, f"Heal rotation deleted for {clr.name}"),
                        failure_callback=partial(
                            log.error, f"Failed to delete heal rotation for {clr.name}"
                        ),
                    ),
                    Command(
                        text=f"^healrotationcreate {clr.name} 3 on on on",
                        response_pattern=rf"(?:"
                        + "|".join(
                            (
                                rf"Successfully added {clr.name} as a current member to a new Heal Rotation",
                                rf"Successfully loaded {clr.name}'s Heal Rotation",
                                rf"{clr.name} is already a current member of a Heal Rotation",
                            )
                        )
                        + ")",
                        failure_patterns=[
                            rf"Failed to add {clr.name} as a current member to a new Heal Rotation",
                            r"You must <target> or \[name\] a creator as a bot that you own to use this command",
                            r"Error: Creator bot dereferenced to nullptr",
                            *BOT_COMMAND_FAILURES,
                        ],
                        success_callback=lambda: self.rotation_commands(clr),
                        failure_callback=partial(
                            log.error, f"Failed to create heal rotation for {clr.name}"
                        ),
                    ),
                ]
            )

        for bot in self.action_bots():
            if not bot.spawned:
                continue

            self.bot_commands(bot)

        self.unwait("configure")
        self.wait("send-commands")

    def settings_saver(self, bot: Bot, setting: str, value: str) -> Callable[[], None]:
        def closure() -> None:
            settings = bot.settings or {}
            if setting == "stance":
                for key in ("spellholds", "sit", "stop_melee", "follow"):
                    settings.pop(key, None)
            log.info(f"Saving settings for {bot.name}: {setting} -> {value}")
            settings[setting] = value
            bot.settings = settings
            self.world.bot_roster.save()

        return closure

    def bot_commands(self, bot: Bot) -> None:

        name = bot.name
        saved = bot.settings or {}

        stance = (
            AGGRESSIVE if bot.class_id in TANK_CLASSES else BURN if bot.class_id in _CASTERS else ""
        )
        changed_stance = bool(stance and saved.get("stance") != stance)
        if changed_stance:
            label = "Aggressive" if stance == AGGRESSIVE else "Burn"
            self.commands.append(
                Command(
                    text=f"^botstance {stance} byname {name}",
                    response_pattern=rf"{name} says, 'I am now set to the stance \[{label}\]",
                    failure_patterns=[
                        r"You must choose a valid stance ID, use .* for information regarding this command\.",
                        r"Incorrect argument, use .* for information regarding this command\.",
                        *ACTIONABLE_FAILURES,
                        *BOT_COMMAND_FAILURES,
                    ],
                    success_callback=self.settings_saver(bot, "stance", stance),
                    failure_callback=partial(log.error, f"Failed to set stance for {name}"),
                )
            )

        if bot.class_id in _CASTERS:
            # Stance changes load stance-specific defaults, so reapply these settings.
            for key, value, command, response, failures in (
                (
                    "spellholds",
                    "0",
                    f"^spellholds 0 0 byname {name}",
                    r"My \[[^\]]+\] spell hold was \[disabled\]",
                    [
                        r"You must choose a valid spell type\. Spell types range from \d+ to \d+",
                        r"You must enter either 0 for disabled or 1 for enabled\.",
                        *BOT_COMMAND_FAILURES,
                    ],
                ),
                (
                    "sit",
                    "90",
                    f"^sitmanapercent 90 byname {name}",
                    r"I will now sit in combat whe[mn] at or below \[90%\] mana",
                    [
                        r"You must enter a value between 0-100 \(0% to 100% of health\)\.",
                        *BOT_COMMAND_FAILURES,
                    ],
                ),
                (
                    "stop_melee",
                    "1",
                    f"^botstopmeleelevel 1 byname {name}",
                    r"My stop melee level was set to 1\.",
                    [
                        r"You must provide a value between 0-255\.",
                        *BOT_COMMAND_FAILURES,
                    ],
                ),
                (
                    "follow",
                    "10",
                    f"^botfollowdistance set 10 byname {name}",
                    r"Following [^']+ at a distance of 10(?:\.0+)?\.",
                    [
                        r"You must enter a value between 1 and \d+\.",
                        *BOT_COMMAND_FAILURES,
                    ],
                ),
            ):
                if not changed_stance and saved.get(key) == value:
                    continue

                self.commands.append(
                    Command(
                        text=command,
                        response_pattern=rf"{name} says, '{response}",
                        failure_patterns=[
                            *failures,
                            r"Incorrect argument, use .* for information regarding this command\.",
                            *ACTIONABLE_FAILURES,
                            *BOT_COMMAND_FAILURES,
                        ],
                        success_callback=self.settings_saver(bot, key, value),
                        failure_callback=partial(log.error, f"Failed to set {key} for {name}"),
                    )
                )

            # spellsettingsadd is target-only. Remember each confirmed spell, rather
            # than a single flag that would miss spells unlocked at later levels.
            roles = _BOT_ROLES.get(bot.class_id, set())
            level = bot.level or self.world.character.level or 1
            for spell in self.world.bot_spells.roles_available(bot.class_id, level, roles):
                key = f"spell:{spell.spell_id}"
                if key in saved:
                    continue

                spell_id = spell.spell_id
                self.commands.append(
                    Command(
                        text=f"^spellsettingsadd {spell_id} {max(1, spell.priority)} 0 100",
                        response_pattern=rf"(?:{'|'.join([
                            rf'Spell Setting Added \| Spell: .* \({spell_id}\)',
                            rf'{name} already has a spell setting for .* \({spell_id}\)'
                        ])})",
                        failure_patterns=[
                            r"You must target a bot that you own to use this command\.",
                            rf"Spell ID {spell_id} is invalid or could not be found\.",
                            rf"Failed to add spell setting for {name}\.",
                            *BOT_COMMAND_FAILURES,
                        ],
                        success_callback=self.settings_saver(bot, key, "1"),
                        target=True,
                        target_id=bot.spawn_id,
                    )
                )

    def rotation_commands(self, healer: Bot) -> None:

        # A fresh rotation has no persisted server-side members or targets.
        for bot in self.action_bots():
            if not bot.spawned:
                continue

            if bot is healer or bot.class_id not in HEALER_CLASSES:
                continue

            self.commands.append(
                Command(
                    text=f"^healrotationaddmember {bot.name} {healer.name}",
                    response_pattern=rf"Successfully added {bot.name} as a current member of this Heal Rotation",
                    failure_patterns=[
                        rf"{bot.name} is already a current member",
                        rf"Failed to add {bot.name} as a current member of this Heal Rotation",
                        r"You must \[name\] a new member as a bot that you own to use this command",
                        r"Error: New member bot dereferenced to nullptr",
                        *HEAL_ROTATION_COMMON_FAILURES,
                    ],
                    success_callback=partial(log.info, f"Heal rotation added member {bot.name}"),
                    failure_callback=partial(
                        log.error, f"Failed to add member {bot.name} to heal rotation"
                    ),
                )
            )

        targets = [self.world.character.name] + [
            bot.name for bot in self.action_bots() if bot.class_id in TANK_CLASSES
        ]

        for target in targets:
            self.commands.append(
                Command(
                    text=f"^healrotationaddtarget {target} {healer.name}",
                    response_pattern=rf"Successfully added heal target {target} to {healer.name}'s Heal Rotation",
                    failure_patterns=[
                        rf"Failed to add heal target with a name of '{target}'",
                        rf"No target exists by the name '{target}'",
                        rf"{target}'s entity type is not an allowable heal target",
                        *HEAL_ROTATION_COMMON_FAILURES,
                    ],
                    success_callback=partial(
                        log.info, f"Heal rotation added target {target} to {healer.name}"
                    ),
                    failure_callback=partial(
                        log.error,
                        f"Failed to add target {target} to heal rotation for {healer.name}",
                    ),
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
            self.commands.extend(
                [
                    Command(
                        text=f"^healrotationadjustsafe {armor} {safe} {healer.name}",
                        response_pattern=rf"Class Armor Type \d+ safe value \d+(?:\.\d+)?% set for {healer.name}'s Heal Rotation",
                        failure_patterns=[
                            rf"Safe value \d+(?:\.\d+)?%\({armor}\) does not exceed critical value \d+(?:\.\d+)?%\({armor}\) for {healer.name}'s Heal Rotation",
                            r"You must specify a valid \[armor_type: \d+-\d+\] to use this command",
                            *HEAL_ROTATION_COMMON_FAILURES,
                        ],
                        success_callback=partial(
                            log.info, f"Heal rotation adjusted safe for {healer.name}"
                        ),
                        failure_callback=partial(
                            log.error, f"Failed to adjust safe for {healer.name}"
                        ),
                    ),
                    Command(
                        text=f"^healrotationadjustcritical {armor} {critical} {healer.name}",
                        response_pattern=rf"Class Armor Type \d+ critical value \d+(?:\.\d+)?% set for {healer.name}'s Heal Rotation",
                        failure_patterns=[
                            rf"Critical value \d+(?:\.\d+)?%\({armor}\) exceeds safe value \d+(?:\.\d+)?%\({armor}\) for {healer.name}'s Heal Rotation",
                            r"You must specify a valid \[armor_type: \d+-\d+\] to use this command",
                            *HEAL_ROTATION_COMMON_FAILURES,
                        ],
                        success_callback=partial(
                            log.info, f"Heal rotation adjusted critical for {healer.name}"
                        ),
                        failure_callback=partial(
                            log.error, f"Failed to adjust critical for {healer.name}"
                        ),
                    ),
                ]
            )

        self.commands.append(
            Command(
                text=f"^healrotationsave {healer.name}",
                response_pattern=rf"Succeeded in saving {healer.name}'s heal rotation",
                failure_patterns=[
                    rf"Failed to save heal rotation members",
                    rf"Failed to save heal rotation targets",
                    rf"{healer.name} is not a current member of a Heal Rotation",
                    *HEAL_ROTATION_COMMON_FAILURES,
                ],
                success_callback=self.settings_saver(healer, "heal", "1"),
                failure_callback=partial(
                    log.error, f"Failed to save heal rotation for {healer.name}"
                ),
            )
        )

        # A saved rotation is loaded by healrotationcreate, but is not active
        # until started. Do not recreate or overwrite an existing live rotation.
        self.commands.append(
            Command(
                text=f"^healrotationstart {healer.name}",
                response_pattern=rf"{healer.name}'s Heal Rotation is (?:now|already) active",
                failure_patterns=[
                    rf"Failed to start {healer.name}'s Heal Rotation",
                    rf"{healer.name} is not a current member of a Heal Rotation",
                    *HEAL_ROTATION_COMMON_FAILURES,
                    *BOT_COMMAND_FAILURES,
                ],
                success_callback=self.settings_saver(healer, "heal", "1"),
                failure_callback=partial(
                    log.error, f"Failed to start heal rotation for {healer.name}"
                ),
            )
        )
        self.commands.append(
            Command(
                text=f"^healrotationlist {healer.name}",
                response_pattern=r"^Heal Rotation Targets:$",
                failure_patterns=[
                    rf"{healer.name} is not a current member of a Heal Rotation",
                    r"\(0\) None",
                    *HEAL_ROTATION_COMMON_FAILURES,
                    *BOT_COMMAND_FAILURES,
                ],
                success_callback=partial(log.info, f"Heal rotation listed for {healer.name}"),
                failure_callback=partial(
                    log.error, f"Failed to list heal rotation for {healer.name}"
                ),
            )
        )

    def action_bots(self) -> list[Bot]:
        bots = list(self.world.bot_roster.group.values())
        if self.raid:
            bots = list(self.world.bot_roster.all_bots())
        return bots

    def filter_by_class(self, class_name: str) -> list[Bot]:
        output: list[Bot] = []
        for bot in self.action_bots():
            if bot.class_id == CLASS_NAME_TO_ID[class_name]:
                output.append(bot)
        return output

    def create_missing_bots(self) -> None:
        for bot in self.world.bot_roster.all_bots():
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

            bot = self.world.bot_roster.bot_by_name(bot_name)
            if not bot:
                log.error(f"Bot {bot_name} not found in roster")
                m = self.re_has_response(BOT_RESPONSE_RE)
                continue

            log.info(f"Bot {bot_name} found in roster setting created to True")
            bot.id = bot_number
            bot.created = True
            bot.level = int(m.group(3))
            m = self.re_has_response(BOT_RESPONSE_RE)
