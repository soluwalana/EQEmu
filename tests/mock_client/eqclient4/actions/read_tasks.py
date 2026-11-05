"""Band 0, durable. Read the stored task book in tutorialb and append the open steps.

A channel, special, or simple line that names work is heard here, while this
action is waiting in the mine. A saylink in that line is a reply for Talk, not
a new step.
"""

import re

from eqclient4.action import Action
from eqclient4.actions.deliver import Deliver
from eqclient4.actions.fetch import Fetch
from eqclient4.actions.kill import Kill
from eqclient4.actions.pickup import Pickup
from eqclient4.actions.talk import Talk, _receipts_for
from eqclient4.actions.visit import Visit
from eqclient4.actions.zone import Zone
from eqclient4.data.areas import box_for

# from eqclient4.actions.support import (
#     COLLECT,
#     DELIVER,
#     EXPLORE,
#     KILL,
#     LOOT,
#     SPEAK,
#     character_name,
#     line_of,
#     new_zone_name,
#     next_zoneline,
#     yield_to,
# )
from eqclient4.structs import OP_TaskActivity
from eqclient4.structs.messages import (
    OP_ChannelMessage,
    OP_SimpleMessage,
    OP_SpecialMesg,
)

# from eqclient4.inventory.assign import release_cursor
SPEAK = 4
KILL = 2
LOOT = 3
DELIVER = 1
COLLECT = 13
EXPLORE = 5


_KINDS = (
    (re.compile(r"\bkill\s+(?:the\s+)?(.+)", re.IGNORECASE), "kill"),
    (re.compile(r"\bhail\s+(?:the\s+)?(.+)", re.IGNORECASE), "talk"),
    (re.compile(r"\b(?:say|talk)\s+(?:to\s+)?(?:the\s+)?(.+)", re.IGNORECASE), "talk"),
    (re.compile(r"\b(?:fetch|loot)\s+(?:the\s+)?(.+)", re.IGNORECASE), "fetch"),
    (re.compile(r"\b(?:deliver|hand|give)\s+(.+)", re.IGNORECASE), "deliver"),
    (re.compile(r"\bpick\s*up\s+(?:the\s+)?(.+)", re.IGNORECASE), "pickup"),
    (re.compile(r"\bzone\s+(?:to\s+)?(.+)", re.IGNORECASE), "zone"),
)


class ReadTasks(Action):

    def __init__(self, task_id: int) -> None:
        super().__init__()
        self.priority = 0
        self.durable = True
        self.seen: list[tuple[int, int]] = []
        self.idle_count = 0

    def opcodes(self) -> tuple[str, ...]:
        return ("OP_NewZone", "OP_ChannelMessage", "OP_SpecialMesg", "OP_SimpleMessage")

    def suspend(self) -> None:
        self.suspended = True

    def current_activity(self) -> OP_TaskActivity | None:
        activities = self._world.tasks.activities.get(self.task_id)
        if not activities:
            return None
        for activity in sorted(activities.values(), key=lambda x: x.sequence):
            if not activity.done and not activity.locked:
                return activity
        return None

    def step(self) -> None:

        self.suspended = False

        activity = self.current_activity()
        if not activity:
            self.idle_count += 1
            return

        if self.idle_count > 120:
            self.complete = True
            return

        if self._listen():
            return

        source = f"task:{activity.task_id}:{activity.activity_id}"

        action = self._action_for(activity)
        if not action:
            return

        if self._loop.journal.is_resolved(source):
            self._loop.journal.clear_source(source)

        if self.yield_to(action, source):
            return

        point = self.next_zoneline("freportw")
        if not point:
            return

        if self.active_path_dest != point:
            self.active_path = self._world.movement.plan(point, "run")
            self.active_path_dest = point

        self._world.movement.advance(self.active_path)

    def _append(
        self,
        kind: str,
        subject: str,
        text: str,
        speaker: str,
    ) -> None:
        source = f"chat:{kind}:{subject.lower()}"
        if self._loop.journal.is_resolved(source):
            self._loop.journal.clear_source(source)

        action: Action
        if kind == "talk":
            npc = self._world.mobs.mob_named(subject) or self._world.mobs.mob_named(speaker)
            if not npc:
                return
            action = Talk(npc.id, subject, text)
            action.description = text
            self.yield_to(action, source)

        elif kind == "kill":
            npc = self._world.mobs.mob_named(subject)
            if not npc:
                action = Kill(None, subject, None)
            else:
                action = Kill(npc.id, None, None)
            action.description = text
            action.task_text = text
            self.yield_to(action, source)

        elif kind == "fetch":
            action = Fetch(_item_id(subject), 1, text)
            action.description = text
            self.yield_to(action, source)

        elif kind == "deliver":
            item_name, npc_name = _deliver(subject)
            item_id = _item_id(item_name)
            if not item_id:
                return
            npc = self._world.mobs.mob_named(npc_name)
            action = Deliver(item_id, npc.id if npc else npc_name)
            action.description = text
            self.yield_to(action, source)

        elif kind == "pickup":
            drop_id, point = self._ground(subject)
            action = Pickup(drop_id, point)
            action.description = text
            self.yield_to(action, source)

        elif kind == "zone":
            self.yield_to(Zone(subject), source)

    def _ground(self, subject: str) -> tuple[int, tuple[float, float, float]]:
        want = subject.lower()
        for row in self._world.ground.values():
            name = row.name.lower()
            if want in name or name in want:
                return (int(row.id), (float(row.x), float(row.y), float(row.z)))
        return (0, (0.0, 0.0, 0.0))

    def _action_for(self, activity: OP_TaskActivity) -> Action | None:
        text = activity.description
        if activity.kind == SPEAK:
            if not activity.target:
                return None

            npc = self._world.mobs.mob_named(activity.target)
            if not npc:
                return None

            item_id = _sole_receipt(activity.target_name, str(world.zone or ""))
            if item_id and world.held(item_id) < 1:
                return Fetch(item_id, 1, text)
            talk = Talk(activity.npc, "hail", text)
            talk.bind_name = activity.target_name or ""
            return talk

        if activity.kind == KILL:
            return Kill(spawn_id=activity.spawn_id or None, camp=activity.target_name or None)

        if activity.kind == EXPLORE:
            box = box_for(int(activity.task_id), int(activity.activity_id))
            if box is None:
                return None
            return Visit(int(activity.task_id), int(activity.activity_id), box.center())

        if activity.kind in (LOOT, DELIVER, COLLECT):
            item_id = activity.item_id or _first_receipt(activity.target_name, str(world.zone or ""))
            if item_id and world.held(item_id) < (activity.goal or 1):
                return Fetch(item_id, activity.goal or 1, text)
            if activity.target_name or text:
                talk = Talk(activity.npc, "hail", text)
                talk.bind_name = activity.target_name or ""
                return talk
            return None
        return None

    def _listen(self) -> bool:
        if str(self._world.zone or "").lower() != "tutorialb":
            while (
                self.consume("OP_ChannelMessage") or self.consume("OP_SpecialMesg") or self.consume("OP_SimpleMessage")
            ):
                pass
            return False
        heard = False
        while True:
            message = (
                self.consume("OP_ChannelMessage") or self.consume("OP_SpecialMesg") or self.consume("OP_SimpleMessage")
            )
            if not message:
                return heard
            text, speaker = _line(message)

            if speaker and speaker.lower() == self._world.character.name.lower():
                continue

            if "on your cursor" in text.lower():
                release_cursor(loop, world)
                heard = True
                continue
            for kind, subject in _named(text):
                _append(self, loop, world, kind, subject, text, speaker)
                heard = True


# A saylink is a reply for the talk already running. The brackets around it are
# not part of a "say …" order, so the link is removed before the patterns run.
_WRAPPED_LINK = re.compile(r"\[?\x12.{56}[^\x12]*?\x12\]?")


def _named(text: str) -> list[tuple[str, str]]:
    plain = saylink_plain(_WRAPPED_LINK.sub(" ", text or ""))
    found: list[tuple[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for pattern, kind in _KINDS:
        match = pattern.search(plain)
        if match is None:
            continue
        subject = match.group(1).strip(" .\"'")
        if not subject:
            continue
        key = (kind, subject.lower())
        if key in seen:
            continue
        seen.add(key)
        found.append(key)
    return found


def _item_id(subject: str) -> int:
    match = re.search(r"\d+", subject or "")
    return int(match.group(0)) if match else 0


def _deliver(subject: str) -> tuple[str, str]:
    match = re.search(r"(.+?)\s+to\s+(.+)", subject, re.IGNORECASE)
    if match is None:
        return (subject, "")
    return (match.group(1).strip(), match.group(2).strip(" ."))
