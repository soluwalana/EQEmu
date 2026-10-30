from __future__ import annotations

import struct
from dataclasses import dataclass, field

from eqclient3.structs.wire import (
    EQStruct,
    _cstring,
    _i32,
    _lenstr,
    _need,
    _put_cstr,
    _put_lenstr,
    _read_u32,
)


def _leading_int(text: str) -> int:
    """First integer in a RoF zone or skill list. Empty and non-numeric lists are 0."""
    raw = text or ""
    start = 0
    while start < len(raw) and not (
        raw[start].isdigit() or (raw[start] == "-" and start + 1 < len(raw) and raw[start + 1].isdigit())
    ):
        start += 1
    if start >= len(raw):
        return 0
    end = start + 1
    while end < len(raw) and raw[end].isdigit():
        end += 1
    return int(raw[start:end], 10)


@dataclass
class TaskElement(EQStruct):
    activity_id: int
    kind: int
    request: int
    target: str
    item_list: str
    goal: int
    skill: int
    spell: int
    zone_id: int
    description: str


@dataclass
class TaskChoice(EQStruct):
    task_id: int
    duration: int
    duration_code: int
    title: str
    description: str
    elements: list[TaskElement] = field(default_factory=list)


@dataclass
class OP_AcceptNewTask(EQStruct):
    task_id: int
    task_master_id: int
    task_type: int = 0

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:4621 AcceptNewTask_Struct
        return struct.pack(
            "<III", self.task_type & 0xFFFFFFFF, self.task_id & 0xFFFFFFFF, self.task_master_id & 0xFFFFFFFF
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_AcceptNewTask:
        _need(data, 12, "OP_AcceptNewTask")
        task_type, task_id, master = struct.unpack_from("<III", data)
        return cls(int(task_id), int(master), int(task_type))


@dataclass
class OP_TaskSelectWindow(EQStruct):
    task_type: int = 0
    giver: int = 0
    tasks: list[TaskChoice] = field(default_factory=list)

    def serialize(self) -> bytes:
        # zone/task_manager.cpp:839 TaskCount
        out = struct.pack("<III", len(self.tasks) & 0xFFFFFFFF, self.task_type & 0xFFFFFFFF, self.giver & 0xFFFFFFFF)
        for task in self.tasks:
            # zone/task_manager.cpp:856 task_id
            out += struct.pack(
                "<IfII", task.task_id & 0xFFFFFFFF, 1.0, task.duration & 0xFFFFFFFF, task.duration_code & 0xFFFFFFFF
            )
            out += _put_cstr(task.title)
            out += _put_cstr(task.description)
            # common/tasks.h:254 SerializeSelector
            out += struct.pack("<BI", 0, len(task.elements) & 0xFFFFFFFF)
            for element in task.elements:
                zones = str(int(element.zone_id))
                # common/tasks.h:263 SerializeSelector
                out += struct.pack("<iii", _i32(element.activity_id), _i32(element.kind), _i32(element.request))
                out += _put_cstr(element.target)
                out += _put_lenstr(element.item_list)
                # common/tasks.h:120 SerializeSelector
                out += struct.pack("<i", _i32(element.goal))
                out += _put_lenstr(str(int(element.skill)))
                out += _put_lenstr(str(int(element.spell)))
                out += _put_cstr(zones)
                out += _put_cstr(element.description)
                out += _put_cstr(zones)
        return out

    @classmethod
    def deserialize(cls, data: bytes) -> OP_TaskSelectWindow:
        _need(data, 12, "OP_TaskSelectWindow")
        count, task_type, giver = struct.unpack_from("<III", data)
        offset = 12
        tasks: list[TaskChoice] = []
        for _index in range(int(count)):
            task_id, _reward, duration, duration_code = struct.unpack_from("<IfII", data, offset)
            offset += 16
            title, offset = _cstring(data, offset)
            description, offset = _cstring(data, offset)
            if offset >= len(data):
                raise ValueError("OP_TaskSelectWindow reward flag missing")
            offset += 1
            elements_n = _read_u32(data, offset)
            offset += 4
            elements: list[TaskElement] = []
            for _element in range(int(elements_n)):
                activity_id, kind, request = struct.unpack_from("<iii", data, offset)
                offset += 12
                target, offset = _cstring(data, offset)
                item_list, offset = _lenstr(data, offset)
                goal = struct.unpack_from("<i", data, offset)[0]
                offset += 4
                skill, offset = _lenstr(data, offset)
                spell, offset = _lenstr(data, offset)
                zones, offset = _cstring(data, offset)
                element_description, offset = _cstring(data, offset)
                _zones_again, offset = _cstring(data, offset)
                elements.append(
                    TaskElement(
                        int(activity_id),
                        int(kind),
                        int(request),
                        target,
                        item_list,
                        int(goal),
                        _leading_int(skill),
                        _leading_int(spell),
                        _leading_int(zones),
                        element_description,
                    )
                )
            tasks.append(TaskChoice(int(task_id), int(duration), int(duration_code), title, description, elements))
        return cls(int(task_type), int(giver), tasks)


@dataclass
class OP_TaskActivity(EQStruct):
    task_id: int = 0
    activity_id: int = 0
    locked: bool = False
    client_index: int = 0
    task_type: int = 0
    list_group: int = 0
    kind: int = 0
    optional: int = 0
    request: int = 0
    target: str = ""
    item_list: str = ""
    goal: int = 0
    skill: int = 0
    spell: int = 0
    zone_id: int = 0
    dynamic_zone: int = 0
    description: str = ""
    done: int = 0

    def serialize(self) -> bytes:
        if self.locked:
            packet = bytearray(25)
            # zone/task_manager.cpp:979 SendTaskActivityShort
            struct.pack_into(
                "<IIIIIIB",
                packet,
                0,
                self.client_index & 0xFFFFFFFF,
                self.task_type & 0xFFFFFFFF,
                self.task_id & 0xFFFFFFFF,
                self.activity_id & 0xFFFFFFFF,
                self.list_group & 0xFFFFFFFF,
                0xFFFFFFFF,
                self.optional & 0xFF,
            )
            return bytes(packet)
        zones = str(int(self.zone_id))
        # zone/task_manager.cpp:1001 SendTaskActivityLong
        out = struct.pack(
            "<IIIII",
            self.client_index & 0xFFFFFFFF,
            self.task_type & 0xFFFFFFFF,
            self.task_id & 0xFFFFFFFF,
            self.activity_id & 0xFFFFFFFF,
            self.list_group & 0xFFFFFFFF,
        )
        # common/tasks.h:152 SerializeObjective
        out += struct.pack("<iBi", _i32(self.kind), self.optional & 0xFF, _i32(self.request))
        out += _put_cstr(self.target)
        out += _put_lenstr(self.item_list)
        # common/tasks.h:166 SerializeObjective
        out += struct.pack("<i", _i32(self.goal))
        out += _put_lenstr(str(int(self.skill)))
        out += _put_lenstr(str(int(self.spell)))
        out += _put_cstr(zones)
        # common/tasks.h:180 SerializeObjective
        out += struct.pack("<i", _i32(self.dynamic_zone))
        out += _put_cstr(self.description)
        # common/tasks.h:182 SerializeObjective
        out += struct.pack("<iB", _i32(self.done), 1)
        out += _put_cstr(zones)
        return out

    @classmethod
    def deserialize(cls, data: bytes) -> OP_TaskActivity:
        if len(data) < 25:
            raise ValueError(f"OP_TaskActivity is {len(data)} bytes")
        if len(data) == 25:
            client_index, task_type, task_id, activity_id, list_group, _hidden, optional = struct.unpack_from(
                "<IIIIIIB", data
            )
            return cls(
                int(task_id),
                int(activity_id),
                True,
                int(client_index),
                int(task_type),
                int(list_group),
                optional=int(optional),
            )
        offset = 0
        client_index, task_type, task_id, activity_id, list_group = struct.unpack_from("<IIIII", data, offset)
        offset += 20
        kind, optional, request = struct.unpack_from("<iBi", data, offset)
        offset += 9
        target, offset = _cstring(data, offset)
        item_list, offset = _lenstr(data, offset)
        goal = struct.unpack_from("<i", data, offset)[0]
        offset += 4
        skill, offset = _lenstr(data, offset)
        spell, offset = _lenstr(data, offset)
        zones, offset = _cstring(data, offset)
        dynamic_zone = struct.unpack_from("<i", data, offset)[0]
        offset += 4
        description, offset = _cstring(data, offset)
        done = struct.unpack_from("<i", data, offset)[0]
        offset += 4
        if offset >= len(data):
            raise ValueError("OP_TaskActivity trailer missing")
        offset += 1
        _zones_again, offset = _cstring(data, offset)
        return cls(
            int(task_id),
            int(activity_id),
            False,
            int(client_index),
            int(task_type),
            int(list_group),
            int(kind),
            int(optional),
            int(request),
            target,
            item_list,
            int(goal),
            _leading_int(skill),
            _leading_int(spell),
            _leading_int(zones),
            int(dynamic_zone),
            description,
            int(done),
        )


@dataclass
class OP_TaskActivityComplete(EQStruct):
    index: int
    task_type: int
    task_id: int
    activity_id: int
    task_completed: int
    stage_complete: int

    def serialize(self) -> bytes:
        # common/eq_packet_structs.h:4743 TaskActivityComplete_Struct
        return struct.pack(
            "<IIIIII",
            self.index & 0xFFFFFFFF,
            self.task_type & 0xFFFFFFFF,
            self.task_id & 0xFFFFFFFF,
            self.activity_id & 0xFFFFFFFF,
            self.task_completed & 0xFFFFFFFF,
            self.stage_complete & 0xFFFFFFFF,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_TaskActivityComplete:
        _need(data, 24, "OP_TaskActivityComplete")
        index, task_type, task_id, activity_id, task_completed, stage_complete = struct.unpack_from("<IIIIII", data)
        return cls(int(index), int(task_type), int(task_id), int(activity_id), int(task_completed), int(stage_complete))
