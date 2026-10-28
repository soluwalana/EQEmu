"""Task windows and SpeakWith, Deliver, Kill, and Loot steps."""

from __future__ import annotations

import struct
from dataclasses import dataclass, field

from eqclient.packets import cstring
from eqclient.zones import remember, zone_id_of

DELIVER = 1
KILL = 2
LOOT = 3
SPEAK = 4

# Kept for the tutorial end-to-end check. The planner does not special-case them.
TUTORIAL_TASKS = (1448, 5166, 5102)


@dataclass
class Activity:
    task_id: int
    activity_id: int
    step: int
    kind: int
    target_name: str
    item_list: str = ""
    goal: int = 1
    done: int = 0
    optional: bool = False
    zone_id: int = 0

    @property
    def finished(self) -> bool:
        return self.done >= self.goal


@dataclass
class Offer:
    task_type: int
    task_id: int
    giver: int


class TaskBook:
    def __init__(self) -> None:
        self.activities: list[Activity] = []
        self.completed: set[int] = set()
        self.order: list[int] = []
        self.givers: dict[int, int] = {}
        self.pending: list[int] = []
        self.offer: Offer | None = None
        self.here: str = ""
        self.here_id: int = 0
        self.task_zone: dict[int, str] = {}

    def set_here(self, zone: str, zone_id: int = 0) -> None:
        self.here = zone
        self.here_id = zone_id or zone_id_of(zone)
        if zone and self.here_id:
            remember(zone, self.here_id)

    def add(self, activity: Activity) -> None:
        self._touch(activity.task_id)
        if activity.task_id not in self.task_zone and self.here:
            self.task_zone[activity.task_id] = self.here
        for index, current in enumerate(self.activities):
            if current.task_id == activity.task_id and current.activity_id == activity.activity_id:
                activity.done = max(activity.done, current.done)
                self.activities[index] = activity
                if not activity.optional and activity.done < activity.goal:
                    self.completed.discard(activity.task_id)
                return
        self.activities.append(activity)
        if not activity.optional and activity.done < activity.goal:
            self.completed.discard(activity.task_id)

    def in_zone(self, task_id: int) -> bool:
        """A task with no zone on its steps belongs where its activities arrived."""
        home = self.task_zone.get(task_id, "")
        return not home or not self.here or home == self.here

    def _step_local(self, activity: Activity) -> bool:
        """A step that names a zone is local only in that zone. The packet's arrival is the fallback."""
        if activity.zone_id and self.here_id:
            return activity.zone_id == self.here_id
        return self.in_zone(activity.task_id)

    def _ordered_ids(self) -> list[int]:
        ordered = [task_id for task_id in TUTORIAL_TASKS if task_id in self.order]
        ordered.extend(task_id for task_id in self.order if task_id not in ordered)
        return ordered

    def away_zone_id(self) -> int:
        """The zone of the next required step that is not local. Zero when every open step is here."""
        for task_id in self._ordered_ids():
            if task_id in self.completed:
                continue
            steps = [
                activity
                for activity in self.activities
                if activity.task_id == task_id and not activity.optional and not activity.finished and not self._step_local(activity)
            ]
            if not steps:
                continue
            chosen = min(steps, key=lambda activity: (activity.step, activity.activity_id))
            if chosen.zone_id:
                return chosen.zone_id
            return zone_id_of(self.task_zone.get(task_id, ""))
        return 0

    def has_open_work(self) -> bool:
        return any(
            not activity.optional and not activity.finished and activity.task_id not in self.completed
            for activity in self.activities
        )

    def current(self) -> list[Activity]:
        """Unfinished required activities of the tutorial task, then any other open task."""
        for task_id in self._ordered_ids():
            if task_id in self.completed:
                continue
            open_steps = [
                activity
                for activity in self.activities
                if activity.task_id == task_id
                and not activity.optional
                and not activity.finished
                and self._step_local(activity)
            ]
            if not open_steps:
                continue
            lowest = min(activity.step for activity in open_steps)
            return [activity for activity in open_steps if activity.step == lowest]
        return []

    def local_work_left(self) -> bool:
        return bool(self.current())

    def task_finished(self, task_id: int) -> bool:
        if task_id in self.completed:
            return True
        rows = [activity for activity in self.activities if activity.task_id == task_id and not activity.optional]
        return bool(rows) and all(activity.finished for activity in rows)

    def finish_if_done(self, task_id: int) -> None:
        if self.task_finished(task_id):
            self.completed.add(task_id)

    def tutorial_done(self) -> bool:
        if any(not activity.optional and not activity.finished for activity in self.activities):
            return False
        return all(self.task_finished(task_id) for task_id in TUTORIAL_TASKS)

    def on_select_window(self, payload: bytes) -> Offer | None:
        """Read the offered ids. The caller accepts one; the rest stay pending."""
        if len(payload) < 12:
            return None
        count, task_type, giver = struct.unpack_from("<III", payload)
        reader = _Reader(payload, 12)
        offers: list[int] = []
        for _index in range(count):
            if reader.remaining() < 4:
                break
            task_id = reader.u32()
            offers.append(task_id)
            self.givers[task_id] = giver
            if not reader.skip_selector():
                break
        if not offers:
            return None
        self._touch(offers[0])
        self.pending = [task_id for task_id in offers[1:] if task_id not in self.completed]
        self.offer = Offer(task_type, offers[0], giver)
        return self.offer

    def on_activity(self, payload: bytes) -> None:
        """Long OP_TaskActivity. A 25-byte short form is still locked, so it stays open."""
        if len(payload) <= 25:
            if len(payload) < 25:
                return
            task_id, activity_id = struct.unpack_from("<II", payload, 8)
            optional = bool(payload[24])
            # A later locked packet must not erase a step we already parsed.
            for current in self.activities:
                if current.task_id == task_id and current.activity_id == activity_id and current.target_name:
                    return
            self.add(
                Activity(
                    task_id=task_id,
                    activity_id=activity_id,
                    step=99,
                    kind=0,
                    target_name="",
                    done=0,
                    optional=optional,
                )
            )
            return
        reader = _Reader(payload)
        try:
            _client_index = reader.u32()
            _task_type = reader.u32()
            task_id = reader.u32()
            activity_id = reader.u32()
            _list_group = reader.u32()
            kind = reader.i32()
            optional = reader.i32()
            _request = reader.i32()
            target = reader.cstr()
            item_list = reader.cstr()
            goal = reader.i32()
            _skill = reader.i32()
            _spell = reader.i32()
            _zone = reader.i32()
            _dz = reader.i32()
            _description = reader.cstr()
            done = reader.i32()
        except (struct.error, ValueError, IndexError):
            return
        if not target:
            target = _named_in(_description)
        self.add(
            Activity(
                task_id=task_id,
                activity_id=activity_id,
                step=1,
                kind=kind,
                target_name=target,
                item_list=item_list,
                goal=max(goal, 1),
                done=max(done, 0),
                optional=bool(optional),
                zone_id=_zone,
            )
        )
        self.finish_if_done(task_id)

    def on_complete(self, payload: bytes) -> None:
        if len(payload) < 24:
            return
        _index, _task_type, task_id, activity_id, _task_completed, stage_complete = struct.unpack_from(
            "<IIIIII", payload
        )
        for activity in self.activities:
            if activity.task_id == task_id and activity.activity_id == activity_id and stage_complete:
                activity.done = max(activity.done, activity.goal)
        self.finish_if_done(task_id)

    def accept_bytes(self) -> bytes | None:
        if self.offer is None:
            return None
        offer = self.offer
        self.offer = None
        self._touch(offer.task_id)
        return struct.pack("<III", offer.task_type, offer.task_id, offer.giver)

    def _touch(self, task_id: int) -> None:
        if task_id not in self.order:
            self.order.append(task_id)


def _named_in(description: str) -> str:
    """'Kill 5 Gloomingdeep Grunts' carries the target when the mob field is blank."""
    parts = description.strip().split(None, 2)
    if len(parts) == 3 and parts[0].lower() == "kill" and parts[1].isdigit():
        return parts[2]
    return description.strip()


class _Reader:
    def __init__(self, data: bytes, offset: int = 0) -> None:
        self.data = data
        self.i = offset

    def remaining(self) -> int:
        return len(self.data) - self.i

    def u32(self) -> int:
        value = struct.unpack_from("<I", self.data, self.i)[0]
        self.i += 4
        return value

    def i32(self) -> int:
        value = struct.unpack_from("<i", self.data, self.i)[0]
        self.i += 4
        return value

    def cstr(self) -> str:
        text, self.i = cstring(self.data, self.i)
        return text

    def skip_selector(self) -> bool:
        """Titanium task selector: duration, code, title, description, elements."""
        try:
            self.u32()
            self.u32()
            self.cstr()
            self.cstr()
            count = self.u32()
            for _index in range(count):
                self.i32()
                self.i32()
                self.i32()
                self.cstr()
                self.cstr()
                self.i32()
                self.i32()
                self.i32()
                self.i32()
                self.cstr()
            return True
        except (struct.error, ValueError, IndexError):
            return False
