import struct
from dataclasses import dataclass, field

from eqclient4.structs.wire import (
    EQStruct,
    ItemLink,
    cstring,
    i8,
    i32,
    leading_int,
    lenstr,
    need,
    put_cstr,
    put_lenstr,
    read_u32,
)


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
            "<III",
            self.task_type & 0xFFFFFFFF,
            self.task_id & 0xFFFFFFFF,
            self.task_master_id & 0xFFFFFFFF,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_AcceptNewTask:
        need(data, 12, "OP_AcceptNewTask")
        task_type, task_id, master = struct.unpack_from("<III", data)
        return cls(int(task_id), int(master), int(task_type))


@dataclass
class OP_TaskSelectWindow(EQStruct):
    task_type: int = 0
    giver: int = 0
    tasks: list[TaskChoice] = field(default_factory=list)

    def serialize(self) -> bytes:
        # zone/task_manager.cpp:839 TaskCount
        out = struct.pack(
            "<III",
            len(self.tasks) & 0xFFFFFFFF,
            self.task_type & 0xFFFFFFFF,
            self.giver & 0xFFFFFFFF,
        )
        for task in self.tasks:
            # zone/task_manager.cpp:856 task_id
            out += struct.pack(
                "<IfII",
                task.task_id & 0xFFFFFFFF,
                1.0,
                task.duration & 0xFFFFFFFF,
                task.duration_code & 0xFFFFFFFF,
            )
            out += put_cstr(task.title)
            out += put_cstr(task.description)
            # common/tasks.h:254 SerializeSelector
            out += struct.pack("<BI", 0, len(task.elements) & 0xFFFFFFFF)
            for element in task.elements:
                zones = str(int(element.zone_id))
                # common/tasks.h:263 SerializeSelector
                out += struct.pack(
                    "<iii",
                    i32(element.activity_id),
                    i32(element.kind),
                    i32(element.request),
                )
                out += put_cstr(element.target)
                out += put_lenstr(element.item_list)
                # common/tasks.h:120 SerializeSelector
                out += struct.pack("<i", i32(element.goal))
                out += put_lenstr(str(int(element.skill)))
                out += put_lenstr(str(int(element.spell)))
                out += put_cstr(zones)
                out += put_cstr(element.description)
                out += put_cstr(zones)
        return out

    @classmethod
    def deserialize(cls, data: bytes) -> OP_TaskSelectWindow:
        need(data, 12, "OP_TaskSelectWindow")
        count, task_type, giver = struct.unpack_from("<III", data)
        offset = 12
        tasks: list[TaskChoice] = []
        for _index in range(int(count)):
            task_id, _reward, duration, duration_code = struct.unpack_from("<IfII", data, offset)
            offset += 16
            title, offset = cstring(data, offset)
            description, offset = cstring(data, offset)
            if offset >= len(data):
                raise ValueError("OP_TaskSelectWindow reward flag missing")
            offset += 1
            elements_n = read_u32(data, offset)
            offset += 4
            elements: list[TaskElement] = []
            for _element in range(int(elements_n)):
                activity_id, kind, request = struct.unpack_from("<iii", data, offset)
                offset += 12
                target, offset = cstring(data, offset)
                item_list, offset = lenstr(data, offset)
                goal = struct.unpack_from("<i", data, offset)[0]
                offset += 4
                skill, offset = lenstr(data, offset)
                spell, offset = lenstr(data, offset)
                zones, offset = cstring(data, offset)
                element_description, offset = cstring(data, offset)
                _zones_again, offset = cstring(data, offset)
                elements.append(
                    TaskElement(
                        int(activity_id),
                        int(kind),
                        int(request),
                        target,
                        item_list,
                        int(goal),
                        leading_int(skill),
                        leading_int(spell),
                        leading_int(zones),
                        element_description,
                    )
                )
            tasks.append(
                TaskChoice(
                    int(task_id),
                    int(duration),
                    int(duration_code),
                    title,
                    description,
                    elements,
                )
            )
        return cls(int(task_type), int(giver), tasks)


@dataclass
class OP_TaskDescription(EQStruct):
    sequence: int
    task_id: int
    title: str
    description: str
    open_window: int = 0
    task_type: int = 0
    reward_type: int = 0
    duration: int = 0
    duration_code: int = 0
    elapsed: int = 0
    has_rewards: int = 0
    coin_reward: int = 0
    xp_reward: int = 0
    faction_reward: int = 0
    reward: str = ""
    item_link: ItemLink | str | None = None
    points: int = 0
    has_reward_selection: int = 0

    def serialize(self) -> bytes:
        if isinstance(self.item_link, ItemLink):
            link = self.item_link.serialize()
        elif self.item_link:
            link = self.item_link
        else:
            link = ""

        return (
            struct.pack(
                "<IIBII",
                self.sequence,
                self.task_id,
                self.open_window,
                self.task_type,
                self.reward_type,
            )
            + put_cstr(self.title)
            + struct.pack(
                "<III",
                self.duration,
                self.duration_code,
                self.elapsed,
            )
            + put_cstr(self.description)
            + struct.pack(
                "<BIII",
                self.has_rewards,
                self.coin_reward,
                self.xp_reward,
                self.faction_reward,
            )
            + put_cstr(self.reward)
            + put_cstr(link)
            + struct.pack(
                "<IB",
                self.points,
                self.has_reward_selection,
            )
        )

    @classmethod
    def deserialize(cls, data: bytes) -> "OP_TaskDescription":
        off = 0
        seq, tid, opened, task_type, reward_type = struct.unpack_from("<IIBII", data, off)
        off += 17

        title, off = cstring(data, off)

        duration, duration_code, elapsed = struct.unpack_from("<III", data, off)
        off += 12

        description, off = cstring(data, off)

        has_rewards, coin, xp, faction = struct.unpack_from("<BIII", data, off)
        off += 13

        reward, off = cstring(data, off)
        raw_link, off = cstring(data, off)

        item_link: ItemLink | str | None = None
        if raw_link.startswith("\x12"):
            item_link = ItemLink.deserialize(raw_link)
        elif raw_link:
            item_link = raw_link

        if len(data) != off + 5:
            raise ValueError("Invalid task trailer length")

        points, selection = struct.unpack_from("<IB", data, off)

        return cls(
            seq,
            tid,
            title,
            description,
            opened,
            task_type,
            reward_type,
            duration,
            duration_code,
            elapsed,
            has_rewards,
            coin,
            xp,
            faction,
            reward,
            item_link,
            points,
            selection,
        )


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
        # common/tasks.h:152 SerializeObjective. RoF writes the optional flag as int8.
        out += struct.pack("<ibi", i32(self.kind), i8(self.optional), i32(self.request))
        out += put_cstr(self.target)
        out += put_lenstr(self.item_list)
        # common/tasks.h:166 SerializeObjective real_goal_count
        out += struct.pack("<i", i32(self.goal))
        out += put_lenstr(str(int(self.skill)))
        out += put_lenstr(str(int(self.spell)))
        out += put_cstr(zones)
        # common/tasks.h:180 SerializeObjective
        out += struct.pack("<i", i32(self.dynamic_zone))
        out += put_cstr(self.description)
        # common/tasks.h:182 SerializeObjective done_count, then int8 1
        out += struct.pack("<ib", i32(self.done), 1)
        out += put_cstr(zones)
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
        target, offset = cstring(data, offset)
        item_list, offset = lenstr(data, offset)
        goal = struct.unpack_from("<i", data, offset)[0]
        offset += 4
        skill, offset = lenstr(data, offset)
        spell, offset = lenstr(data, offset)
        zones, offset = cstring(data, offset)
        dynamic_zone = struct.unpack_from("<i", data, offset)[0]
        offset += 4
        description, offset = cstring(data, offset)
        done = struct.unpack_from("<i", data, offset)[0]
        offset += 4
        if offset >= len(data):
            raise ValueError("OP_TaskActivity trailer missing")
        offset += 1
        _zones_again, offset = cstring(data, offset)
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
            leading_int(skill),
            leading_int(spell),
            leading_int(zones),
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
        need(data, 24, "OP_TaskActivityComplete")
        index, task_type, task_id, activity_id, task_completed, stage_complete = struct.unpack_from("<IIIIII", data)
        return cls(int(index), int(task_type), int(task_id), int(activity_id), int(task_completed), int(stage_complete))
