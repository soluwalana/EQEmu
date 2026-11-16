"""The action superclass. The scheduler and the bus only know this type."""

import re
import time
from collections.abc import Callable, Collection
from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient4.loop import Loop
    from eqclient4.nav.path import EQPath
    from eqclient4.world import World

from eqclient4.bots import Bot
from eqclient4.log import log
from eqclient4.mob import Mob
from eqclient4.nav.travel import first_leg
from eqclient4.structs import (
    SAY_CHANNEL,
    EQStruct,
    OP_ChannelMessage,
    OP_Consider,
    OP_SpecialMesg,
    OP_TargetMouse,
)

REPLY_TIMEOUT = 8.0

SEND_COMMANDS = "SEND_COMMANDS"
TARGET = "TARGET"
    


@dataclass
class Command:
    """A command to be processed and waited on."""

    text: str
    response_pattern: str
    failure_patterns: list[str]
    target_id: int | None = None
    sent_at: float | None = None
    recv_response: re.Match | None = None
    failure_msg: str | None = None
    success_callback: Callable[[], None] | None = None
    failure_callback: Callable[[], None] | None = None


class Action:
    def __init__(self, world: World, loop: Loop) -> None:
        self.source = ""
        self.priority = 0
        self.insert = 0
        self.started = 0.0
        self.world: World = world
        self.loop: Loop = loop
        self.zone = self.world.zone or ""
        self.failed = False

        self.durable = False
        self.complete = False
        self.suspended = True
        self.yielding = False
        self.messages: list[EQStruct] = []
        self.waiting: list[str] = []

        self.waited = 0
        self.active_path: EQPath | None = None
        self.active_path_dest: tuple[float, float, float] | Mob | None = None

        # Targeting helper fields
        self.target_id = 0
        self.target_sent = False
        self.mob_targeted = 0
        self._consider_sent = False

        # Movement helper fields
        self.zoneline: tuple[float, float, float] | None = None
        self.zoneline_dest: str | None = None

        self.commands: list[Command] = []

    def opcodes(self) -> tuple[str, ...]:
        return ("OP_Consider", "OP_ChannelMessage", "OP_SpecialMesg")

    def step(self) -> None:
        self.suspended = False
        self.handle_targeting()

        if self.waiting_for(SEND_COMMANDS):
            self.send_commands()
            return

    def _send_target_mouse(self) -> None:
        self.loop.send(
            "OP_TargetMouse",
            OP_TargetMouse(int(self.target_id) & 65535).serialize(),
        )
        self.target_sent = True
        return

    def _send_consider(self) -> None:
        self.loop.send(
            "OP_Consider",
            OP_Consider(
                player_id=int(self.world.self_id or 0), target_id=int(self.target_id) & 65535
            ).serialize(),
        )
        self._consider_sent = True
        return

    def handle_mob_targeting(self, mob: Mob) -> None:
        if self.mob_targeted != self.target_id:
            self.wait(TARGET)

        if not self.can_see_mob(mob):
            return

        if mob.is_treasure and float(mob.distance) > 25:
            self.move_closer(mob)
            return

        if self.mob_targeted == self.target_id:
            return

        if not self.target_sent:
            self._send_target_mouse()
            return

        if mob.is_treasure:
            mob.targeted = True
            self.mob_targeted = self.target_id
            self.unwait(TARGET)
            self.target_sent = False
            self._consider_sent = False
            return

        # Treasures don't send considers back
        if not self._consider_sent:
            self._send_consider()
            return

        message = self.consume("OP_Consider", self.con_matcher)
        if message:
            mob.targeted = True
            self.mob_targeted = self.target_id
            self.unwait(TARGET)
            self.target_sent = False
            self._consider_sent = False
            return

    def handle_bot_targeting(self, bot: Bot) -> None:
        if self.mob_targeted != self.target_id:
            previous = self.world.bot_roster.bot_by_spawn_id(self.mob_targeted)
            if previous:
                previous.targeted = False
            self.wait(TARGET)

        if not self.world.line_of_sight(bot):
            self.send_channel_message(f"^botsummon byname {bot.name}")
            return

        if self.mob_targeted == self.target_id:
            return

        if not self.target_sent:
            self._send_target_mouse()
            return

        if not self._consider_sent:
            self._send_consider()
            return

        message = self.consume("OP_Consider", self.con_matcher)
        if message:
            bot.targeted = True
            self.mob_targeted = self.target_id
            self.unwait(TARGET)
            self.target_sent = False
            self._consider_sent = False
            return

    def handle_targeting(self) -> None:
        if not self.target_id:
            return

        if mob := self.world.mobs.find_mob(self.target_id):
            self.handle_mob_targeting(mob)
            return

        if bot := self.world.bot_roster.bot_by_spawn_id(self.target_id):
            self.handle_bot_targeting(bot)
            return

    def send_commands(self) -> None:
        """Complete after all commands have been sent and response or timeout has occurred.
        
        Trigger by waiting for "SEND_COMMANDS" and returning from step().
        """
        for command in self.commands:
            if command.recv_response or command.failure_msg:
                continue

            if command.sent_at is None:
                if command.target_id and self.mob_targeted != command.target_id:
                    self.target_id = command.target_id
                    return
                
                self.messages.clear()  # Discard previous replies
                command.sent_at = time.monotonic()
                self.send_channel_message(command.text, sleep_time=0.025)
                return

            failure_patterns = []
            if len(command.failure_patterns) > 0:
                failure_patterns = command.failure_patterns
            else:
                log.warning(f"No failure patterns provided for command: {command.text}")

            failure = None
            if failure_patterns:
                failure_pattern = re.compile("(" + "|".join(failure_patterns) + ")")
                failure = self.re_has_response(failure_pattern)

            if failure:
                command.failure_msg = failure.group(0)
                log.error(f"Command Failed: {command.failure_msg}")
                if command.failure_callback:
                    command.failure_callback()
                return

            if time.monotonic() - command.sent_at >= REPLY_TIMEOUT:
                log.error(f"Command {command.text} timed out after {REPLY_TIMEOUT} seconds")
                command.failure_msg = "fail: timeout"
                if command.failure_callback:
                    command.failure_callback()
                return

            success_pattern = re.compile(command.response_pattern)
            success = self.re_has_response(success_pattern)

            if success:
                command.recv_response = success
                if command.success_callback:
                    command.success_callback()

            return

        self.unwait(SEND_COMMANDS)

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

    def send_channel_message(self, message: str, sleep_time: float = 0.1) -> None:
        self.loop.send(
            "OP_ChannelMessage",
            OP_ChannelMessage(
                "",
                self.world.character.name,
                100,
                SAY_CHANNEL,
                0,
                0,
                100,
                message,
            ).serialize(),
        )
        self.loop._flush()
        time.sleep(sleep_time)
        self.loop.pump()

    def con_matcher(self, message: EQStruct) -> bool:
        if isinstance(message, OP_Consider):
            return message.target_id == (self.target_id or 0)
        return False

    def can_see_mob(self, mob: Mob) -> bool:
        if self.world.line_of_sight(mob):
            return True
        self.move_closer(mob)
        return False

    def wait(self, kind: str) -> None:
        pending = self._pending()
        if kind not in pending:
            pending.append(kind)

    def unwait(self, kind: str) -> None:
        pending = self._pending()
        if kind in pending:
            pending.remove(kind)

    def waiting_for(self, *kinds: str) -> bool:
        return any(kind in self._pending() for kind in kinds)

    def wait_label(self) -> str:
        return ",".join(self._pending())

    def _pending(self) -> list[str]:
        pending = self.waiting
        if isinstance(pending, list):
            return pending
        if isinstance(pending, str) and pending:
            self.waiting = [pending]
            return self.waiting
        self.waiting = []
        return self.waiting

    def consume(
        self, opcode: str | Collection[str], match: Callable[[EQStruct], bool] | None = None
    ) -> EQStruct | None:
        for index, message in enumerate(self.messages):
            match opcode:
                case str():
                    if message.opcode != opcode:
                        continue
                case Collection():
                    if message.opcode not in opcode:
                        continue

            if match and not match(message):
                continue
            return self.messages.pop(index)
        return None

    @property
    def completed(self) -> bool:
        return self.complete

    def add_message(self, payload: EQStruct) -> None:
        self.messages.append(payload)

    @staticmethod
    def key(action: Action) -> tuple[object, ...]:
        # Within one band, smaller runs first. Newest insert is the default.
        return (-action.insert,)

    def forget(self) -> None:
        self.loop.queue.remove(self.insert)
        self.loop.journal.clear_source(self.source)

    def yield_to(self, new: Action) -> bool:
        """Queue the next piece of work. Same-band handoff waits until the next pulse."""
        if not self.loop.queue.append(new):
            return False

        self.yielding = True
        return True

    def move_closer(self, dest: tuple[float, float, float] | Mob, mode: str = "run") -> None:
        dest_location = dest
        if isinstance(dest, Mob):
            dest_location = dest.position

        if not self.active_path or self.active_path_dest != dest_location:
            self.active_path = self.world.movement.plan(dest_location, mode)
            self.active_path_dest = dest_location

        self.world.movement.advance(self.loop, self.active_path)

    def face(self, dest: tuple[float, float, float] | Mob) -> None:
        match dest:
            case (_, _, _):
                self.world.movement.face(self.loop, dest)
            case Mob():
                self.world.movement.face(self.loop, dest.position)
            case _:
                raise ValueError(
                    f"Invalid destination type: {type(dest)}, expected tuple[float, float, float] or Mob"
                )

    def next_zoneline(self, destination: str) -> tuple[float, float, float] | None:
        """Where to walk to leave this zone toward `destination`.

        A saved zoneline wins. Otherwise the zone graph's next transit. A zone
        with no graph hop, such as tutorialb, walks to the one scripted exit door.
        """

        # Cached
        if destination == self.zoneline_dest:
            return self.zoneline

        self.zoneline_dest = destination

        here = (self.world.zone or "").lower()
        dest = (destination or "").lower()
        leg = first_leg(self.world.zone_graph, here, dest)
        if leg:
            spot = self._transit_point(leg.zone, leg.door_id, leg.dest)
            if spot:
                self.zoneline = spot
                return spot

        self.zoneline = self._script_exit(here, dest)
        return self.zoneline

    def _transit_point(
        self,
        zone: str,
        door_id: int,
        dest: str = "",
    ) -> tuple[float, float, float] | None:
        transit = self.world.zone_graph.transit_at(zone, door_id)
        if transit and (transit.x or transit.y or transit.z):
            return (transit.x, transit.y, transit.z)

        arrived = self._return_landing(zone, dest)
        if arrived:
            return arrived

        return self._door_point(door_id)

    def _return_landing(self, here: str, dest: str) -> tuple[float, float, float] | None:
        """A zone point stored with no origin. The reverse hop's landing is that point."""
        home = (here or "").lower()
        target = (dest or "").lower()
        if not home or not target:
            return None

        for transit in self.world.zone_graph.transits_from(target):
            if transit.dest != home:
                continue
            if transit.dest_x or transit.dest_y or transit.dest_z:
                return (transit.dest_x, transit.dest_y, transit.dest_z)

        return None

    def _script_exit(self, here: str, destination: str) -> tuple[float, float, float] | None:
        """The live door a quest script uses to leave, when the zone graph has no hop."""
        exits = self.world.exit_doors.get(here, {})
        if not exits:
            return None

        dest_id = self.world.zone_graph.zones.get(destination, 0)

        chosen = 0
        if dest_id:
            for door_id, targets in exits.items():
                if dest_id in targets:
                    chosen = door_id
                    break

        if not chosen and len(exits) == 1:
            chosen = next(iter(exits))

        if not chosen:
            return None

        return self._door_point(chosen)

    def _door_point(self, door_id: int) -> tuple[float, float, float] | None:
        door = self.world.doors.get(door_id)
        if door is None and door_id < 256:
            for live in self.world.doors.values():
                if live.id % 256 == door_id:
                    door = live
                    break

        if door is None:
            return None

        return (door.x, door.y, door.z)

    def exit_kind(self, destination: str) -> str:
        """How the next hop leaves: door, stone, or point. Empty when the graph has no hop."""
        graph = self.world.zone_graph

        leg = first_leg(graph, (self.world.zone or "").lower(), (destination or "").lower())
        if not leg:
            return ""
        transit = graph.transit_at(leg.zone, leg.door_id)
        if not transit:
            return ""
        return transit.via

    def painted_line(self, anchor: tuple[float, float, float]) -> tuple[float, float, float] | None:
        """A watermap zone-line sample near a zone point. Outdoor lines are volumes, not the row."""
        if not self.world.zone:
            return None
        water = self.world.get_water_map(self.world.zone)
        if not water:
            return None
        if water.in_zone_line(anchor[0], anchor[1], anchor[2]):
            return anchor
        here = self.world.position
        return water.nearest_zone_line(here[0], here[1], here[2], anchor=anchor, reach=300, step=10)

    def crash(self) -> None:
        """Immediately crash the action, stopping the loop."""
        raise Exception(f"Action {self.source} crashed")

    def suspend(self) -> None:
        """Override for custom suspension behavior."""
        self.active_path = None
        self.suspended = True

    def report(self) -> str:

        wait_str = ""
        wait_label = self.wait_label()
        if wait_label:
            wait_str = f" (WAITING {wait_label})"

        return f"[{type(self).__name__}]{wait_str} source={self.source} priority={self.priority} "
