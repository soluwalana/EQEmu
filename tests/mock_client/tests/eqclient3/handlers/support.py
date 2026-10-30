"""Packet builders and a scripted loop. World is the real sheet."""

from __future__ import annotations
import struct
from eqclient3.structs import (
    Door,
    Item,
    OP_ChannelMessage,
    OP_CharInventory,
    OP_Damage,
    OP_GroundSpawn,
    OP_HPUpdate,
    OP_MobUpdate,
    OP_NewZone,
    OP_OnLevelMessage,
    OP_PlayerProfile,
    OP_RequestClientZoneChange,
    OP_TaskActivity,
    OP_TaskSelectWindow,
    OP_ZoneChange,
    Spawn,
    TaskChoice,
    TaskElement,
)
from eqclient3.world import World


class Loop:

    def __init__(self):
        self.queue = []
        self.sent = []
        self.character = ""
        self.session = None
        self.closed = False
        self.journal = None
        self.client = None
        self.active = None
        self.current = None
        self.head = None

    def append(self, action):
        action.insert = len(self.queue) + 1
        action.started = 0
        self.queue.append(action)
        return action

    def send(self, opcode, payload):
        self.sent.append((opcode, bytes(payload)))


def names(loop):
    return [type(action).__name__ for action in loop.queue]


def sources(loop):
    return [action.source for action in loop.queue]


def spawn(spawn_id, name, npc=1, level=1, class_id=1, race=1, body=1, x=0.0, y=0.0, z=0.0) -> bytes:
    return Spawn(
        int(spawn_id),
        name,
        int(npc),
        int(level),
        int(body),
        float(x),
        float(y),
        float(z),
        int(class_id),
        int(race),
    ).serialize()


def position(spawn_id, x, y, z) -> bytes:
    return OP_MobUpdate(int(spawn_id), float(x), float(y), float(z)).serialize()


def damage(target, source, amount, dmg_type=0, spell=0) -> bytes:
    return OP_Damage(int(target), int(source), int(dmg_type), int(spell), int(amount)).serialize()


def hp(spawn_id, current, maximum) -> bytes:
    return OP_HPUpdate(int(current), int(maximum), int(spawn_id)).serialize()


def consider(player, target, faction, level_color=0) -> bytes:
    """Wire consider. Faction is the server value; deserialize undoes the 6/9 and 7/8 swap."""
    return struct.pack(
        "<IIIIBBBB",
        int(player),
        int(target),
        int(faction),
        int(level_color),
        0,
        0,
        0,
        0,
    )


def become_corpse(spawn_id, x, y, z) -> bytes:
    return struct.pack("<Ifff", int(spawn_id), float(y), float(x), float(z))


def death(spawn_id, killer=0, corpse_id=0) -> bytes:
    return struct.pack("<8I", int(spawn_id), int(killer), int(corpse_id), 0, 0, 0, 0, 0)


def new_zone(name, x, y, z, zone_id=0) -> bytes:
    return OP_NewZone(name, float(x), float(y), float(z), int(zone_id)).serialize()


def zone_change(zone_id, x, y, z, success=1, name="") -> bytes:
    return OP_ZoneChange(name, int(zone_id), float(x), float(y), float(z), success=int(success)).serialize()


def request_zone(zone_id, x, y, z) -> bytes:
    return OP_RequestClientZoneChange(int(zone_id), float(x), float(y), float(z)).serialize()


def channel(sender, text) -> bytes:
    return OP_ChannelMessage("", sender, text=text).serialize()


def special(speaker, text) -> bytes:
    return b"\x00" * 11 + speaker.encode("latin1") + b"\x00" + b"\x00" * 12 + text.encode("latin1") + b"\x00"


def simple(string_id, *texts) -> bytes:
    packet = struct.pack("<III", int(string_id), 0, 0)
    for text in texts:
        packet += text.encode("latin1") + b"\x00"
    return packet


def item_blob(kind, slot, item_id, name="Bone", stack=1, price=0, item_type=0) -> bytes:
    item = Item(
        0 if kind is None else int(kind),
        int(slot),
        name,
        "IT0",
        int(item_id),
        int(stack),
        item_type=int(item_type),
        price=int(price),
    )
    if kind is None:
        return OP_CharInventory([item]).serialize()
    return item.serialize()


def door(door_id, name, x, y, z, open_type=0) -> bytes:
    return Door(int(door_id), name, float(x), float(y), float(z), int(open_type)).serialize()


def ground(drop_id, name, x, y, z) -> bytes:
    return OP_GroundSpawn(int(drop_id), name, float(x), float(y), float(z)).serialize()


def task_window(giver, tasks) -> bytes:
    """tasks: (task_id, duration_code, title, description, activities).

    An activity is (activity_id, kind, target, item_list, goal, description).
    """
    choices = []
    for task_id, duration_code, title, description, activities in tasks:
        elements = [
            TaskElement(
                int(activity_id),
                int(kind),
                0,
                target,
                item_list,
                int(goal),
                0,
                0,
                0,
                text,
            )
            for activity_id, kind, target, item_list, goal, text in activities
        ]
        choices.append(TaskChoice(int(task_id), 0, int(duration_code), title, description, elements))
    return OP_TaskSelectWindow(0, int(giver), choices).serialize()


def task_activity(task_id, activity_id, kind, target, item_list, goal, description, done=0) -> bytes:
    return OP_TaskActivity(
        int(task_id),
        int(activity_id),
        False,
        kind=int(kind),
        target=target,
        item_list=item_list,
        goal=int(goal),
        description=description,
        done=int(done),
    ).serialize()


def task_complete(task_id, activity_id, stage=1) -> bytes:
    return struct.pack("<IIIIII", 0, 0, int(task_id), int(activity_id), 0, int(stage))


def group_update(your, members, leader, action=7) -> bytes:
    packet = bytearray(452)
    struct.pack_into("<I", packet, 0, int(action))
    _put(packet, 4, your)
    for index, name in enumerate(list(members)[:5]):
        _put(packet, 68 + index * 64, name)
    _put(packet, 388, leader)
    return bytes(packet)


def _put(packet: bytearray, offset: int, text: str) -> None:
    encoded = (text or "").encode("latin1")[:63]
    packet[offset : offset + len(encoded)] = encoded


def profile(name="Hero", level=2, skill=None, platinum=1, gold=2, silver=3, copper=4) -> bytes:
    skills = None
    if skill is not None:
        skill_id, value = skill
        skills = {int(skill_id): int(value)}
    return OP_PlayerProfile(
        name=name,
        level=int(level),
        race=1,
        class_id=1,
        platinum=int(platinum),
        gold=int(gold),
        silver=int(silver),
        copper=int(copper),
        coin_known=True,
        skills=skills,
    ).serialize()


def level_popup(popup_id) -> bytes:
    return OP_OnLevelMessage(popup_id=int(popup_id)).serialize()
