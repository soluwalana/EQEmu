"""Packet builders and a scripted loop. World is the real sheet."""
from __future__ import annotations
import struct
from eqclient3.structs import Door, OP_ChannelMessage, OP_MobUpdate, Spawn
from eqclient3.world import World

class Loop:

    def __init__(self):
        self.queue = []
        self.sent = []
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
    return Spawn(int(spawn_id), name, int(npc), int(level), int(body), float(x), float(y), float(z), int(class_id), int(race)).serialize()

def position(spawn_id, x, y, z) -> bytes:
    return OP_MobUpdate(int(spawn_id), float(x), float(y), float(z)).serialize()

def damage(target, source, amount, dmg_type=0, spell=0) -> bytes:
    return struct.pack('<HHBHi', int(target), int(source), int(dmg_type), int(spell), int(amount))

def hp(spawn_id, current, maximum) -> bytes:
    return struct.pack('<IiH', int(current), int(maximum), int(spawn_id))

def consider(player, target, faction, level_color=0) -> bytes:
    return struct.pack('<IIII', int(player), int(target), int(faction), int(level_color))

def become_corpse(spawn_id, x, y, z) -> bytes:
    return struct.pack('<Ifff', int(spawn_id), float(y), float(x), float(z))

def death(spawn_id, killer=0, corpse_id=0) -> bytes:
    return struct.pack('<8I', int(spawn_id), int(killer), int(corpse_id), 0, 0, 0, 0, 0)

def new_zone(name, x, y, z, zone_id=0) -> bytes:
    packet = bytearray(686 if zone_id else 504)
    encoded = name.encode('latin1')[:31]
    packet[64:64 + len(encoded)] = encoded
    struct.pack_into('<fff', packet, 492, float(y), float(x), float(z))
    if zone_id:
        struct.pack_into('<H', packet, 684, int(zone_id))
    return bytes(packet)

def zone_change(zone_id, x, y, z, success=1, name='') -> bytes:
    packet = bytearray(88)
    encoded = name.encode('latin1')[:63]
    packet[:len(encoded)] = encoded
    struct.pack_into('<HH', packet, 64, int(zone_id), 0)
    struct.pack_into('<fff', packet, 68, float(y), float(x), float(z))
    struct.pack_into('<i', packet, 84, int(success))
    return bytes(packet)

def request_zone(zone_id, x, y, z) -> bytes:
    return struct.pack('<H2xfff', int(zone_id), float(y), float(x), float(z))

def channel(sender, text) -> bytes:
    return OP_ChannelMessage('', sender, text=text).serialize()

def special(speaker, text) -> bytes:
    return b'\x00' * 11 + speaker.encode('latin1') + b'\x00' + b'\x00' * 12 + text.encode('latin1') + b'\x00'

def simple(string_id, *texts) -> bytes:
    packet = struct.pack('<III', int(string_id), 0, 0)
    for text in texts:
        packet += text.encode('latin1') + b'\x00'
    return packet

def item_blob(kind, slot, item_id, name='Bone', stack=1, price=0, item_type=0) -> bytes:
    static = ['0'] * 57
    static[1] = name
    static[3] = 'IT0'
    static[4] = str(int(item_id))
    static[56] = str(int(item_type))
    body = f'{int(stack)}|0|{int(slot)}|{int(price)}"' + '|'.join(static)
    prefix = b'' if kind is None else struct.pack('<I', int(kind))
    return prefix + body.encode('latin1') + b'\x00'

def door(door_id, name, x, y, z, open_type=0) -> bytes:
    return Door(int(door_id), name, float(x), float(y), float(z), int(open_type)).serialize()

def ground(drop_id, name, x, y, z) -> bytes:
    blob = bytearray(44 + len(name) + 1)
    struct.pack_into('<I', blob, 12, int(drop_id))
    struct.pack_into('<ffff', blob, 28, 0.0, float(z), float(x), float(y))
    encoded = name.encode('latin1')
    blob[44:44 + len(encoded)] = encoded
    return bytes(blob)

def _cstr(text: str) -> bytes:
    return text.encode('latin1') + b'\x00'

def task_window(giver, tasks) -> bytes:
    """tasks: (task_id, duration_code, title, description, activities).

    An activity is (activity_id, kind, target, item_list, goal, description).
    """
    packet = struct.pack('<III', len(tasks), 0, int(giver))
    for task_id, duration_code, title, description, activities in tasks:
        packet += struct.pack('<III', int(task_id), 0, int(duration_code))
        packet += _cstr(title) + _cstr(description)
        packet += struct.pack('<I', len(activities))
        for activity_id, kind, target, item_list, goal, text in activities:
            packet += struct.pack('<iii', int(activity_id), int(kind), 0)
            packet += _cstr(target) + _cstr(item_list)
            packet += struct.pack('<iiii', int(goal), 0, 0, 0)
            packet += _cstr(text)
    return packet

def task_activity(task_id, activity_id, kind, target, item_list, goal, description, done=0) -> bytes:
    packet = struct.pack('<IIIII', 0, 0, int(task_id), int(activity_id), 0)
    packet += struct.pack('<iii', int(kind), 0, 0)
    packet += _cstr(target) + _cstr(item_list)
    packet += struct.pack('<iiiii', int(goal), 0, 0, 0, 0)
    packet += _cstr(description)
    packet += struct.pack('<i', int(done))
    return packet

def task_complete(task_id, activity_id, stage=1) -> bytes:
    return struct.pack('<IIIIII', 0, 0, int(task_id), int(activity_id), 0, int(stage))

def group_update(your, members, leader, action=7) -> bytes:
    packet = bytearray(452)
    struct.pack_into('<I', packet, 0, int(action))
    _put(packet, 4, your)
    for index, name in enumerate(list(members)[:5]):
        _put(packet, 68 + index * 64, name)
    _put(packet, 388, leader)
    return bytes(packet)

def _put(packet: bytearray, offset: int, text: str) -> None:
    encoded = (text or '').encode('latin1')[:63]
    packet[offset:offset + len(encoded)] = encoded

def profile(name='Hero', level=2, skill=None, platinum=1, gold=2, silver=3, copper=4) -> bytes:
    packet = bytearray(13004)
    struct.pack_into('<III', packet, 4, 0, 1, 1)
    packet[20] = int(level)
    encoded = name.encode('latin1')[:63]
    packet[12940:12940 + len(encoded)] = encoded
    struct.pack_into('<IIII', packet, 4428, int(platinum), int(gold), int(silver), int(copper))
    if skill is not None:
        skill_id, value = skill
        struct.pack_into('<I', packet, 4460 + int(skill_id) * 4, int(value))
    return bytes(packet)

def level_popup(popup_id) -> bytes:
    packet = bytearray(4244)
    struct.pack_into('<I', packet, 4232, int(popup_id))
    return bytes(packet)
