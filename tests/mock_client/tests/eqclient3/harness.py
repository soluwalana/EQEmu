"""Mock world, schedule, and movement for one action at a time."""

from __future__ import annotations

import sys
import types
from pathlib import Path

MOCK = Path(__file__).resolve().parents[2]
if str(MOCK) not in sys.path:
    sys.path.insert(0, str(MOCK))


class PathDouble:
    def __init__(self, distance, mode, dest):
        self.distance = distance
        self.mode = mode
        self.dest = dest


class MovementDouble:
    def __init__(self):
        self.distance = 0
        self.visible = []
        self.on_path = []
        self.plans = []
        self.advances = []

    def plan(self, dest, mode="run"):
        self.plans.append((dest, mode))
        return PathDouble(self.distance, mode, dest)

    def advance(self, loop, world, path):
        self.advances.append(path)

    def visible_mobs(self):
        self.plans.append(("visible", None))
        return list(self.visible)

    def mobs_on_path(self, mobs):
        self.plans.append(("on_path", None))
        if self.on_path is None:
            return None
        return list(self.on_path)

    def reset(self):
        self.plans.clear()
        self.advances.clear()

    def bind(self, world):
        return None

    def hold_if_idle(self, loop, world=None):
        return None

    def snap(self, world, point):
        return None

    def opcodes(self):
        return ()

    def handle(self, opcode, payload, world=None):
        return None


_MOVEMENT = MovementDouble()
_MOVEMENT_FILE = MOCK / "eqclient3" / "movement.py"


def install_movement():
    """Actions call eqclient3.movement. A missing module gets this double.

    When the real module is already imported, its plan, advance, visible_mobs,
    and mobs_on_path are pointed at the double for this process only.
    """
    try:
        import eqclient3.movement as module
    except ImportError:
        module = types.ModuleType("eqclient3.movement")
        sys.modules["eqclient3.movement"] = module
        import eqclient3

        eqclient3.movement = module
    module.plan = _MOVEMENT.plan
    module.advance = _MOVEMENT.advance
    module.visible_mobs = _MOVEMENT.visible_mobs
    module.mobs_on_path = _MOVEMENT.mobs_on_path
    module.fake = _MOVEMENT
    return _MOVEMENT


install_movement()

from eqclient3.action import Message
from eqclient3.journal import Journal
from eqclient3.loop import Loop
from eqclient3.structs import OP_ChannelMessage
from eqclient3.schedule import Schedule
from eqclient3.world import GroundSpawn, Mob, World


def movement():
    return _MOVEMENT


def world(zone="qeynos", name="Hero"):
    sheet = World()
    sheet.zone = zone
    sheet.name = name
    sheet.self_id = 1
    sheet.level = 10
    sheet.hp = 100
    sheet.max_hp = 100
    sheet.position = (0.0, 0.0, 0.0)
    # A stand-in mesh keeps line of sight clear without loading a zone file.
    sheet.mesh = types.SimpleNamespace(clear=lambda *_args, **_kwargs: True)
    sheet.movement = _MOVEMENT
    return sheet


def fresh(zone="qeynos"):
    fake = movement()
    fake.reset()
    fake.distance = 0
    fake.visible = []
    fake.on_path = []
    return loop(world(zone))


def loop(sheet=None, tick=1):
    sheet = sheet or world()
    client = Loop()
    client.queue = Schedule()
    client.journal = Journal(":memory:")
    client.character = sheet.name
    client.queue.bind(client.journal, client.character)
    client.tick = tick
    client.session = types.SimpleNamespace(closed=False, open=True, needs_rezone=False)
    client.assign_calls = []
    client.assign = lambda *_args: client.assign_calls.append(1)
    return client, sheet


def say(text):
    return OP_ChannelMessage("", "Hero", text=text).serialize()


def commands(client):
    found = []
    for opcode, payload in client.outbound:
        if opcode == "OP_ChannelMessage":
            found.append(OP_ChannelMessage.deserialize(payload).text)
    return found


def opcodes(client):
    return [opcode for opcode, _payload in client.outbound]


def mob(sheet, spawn_id, *, distance=10, level=1, name="orc", standing=0, targeted=True):
    body = Mob(spawn_id, name, npc=1, level=level, position=(float(distance), 0.0, 0.0))
    if standing:
        body.consider = types.SimpleNamespace(standing=standing)
    body.targeted = targeted
    sheet.mobs[spawn_id] = body
    return body


def inbox(action, opcode, payload):
    action.add_message(Message(_mailbox(opcode, payload)))


def _mailbox(opcode, payload):
    """Turn a test fixture into the struct the mailbox stores."""
    import struct

    from eqclient3.net.decode import body
    from eqclient3.structs import (
        EQStruct,
        Item,
        OP_BecomeCorpse,
        OP_Buff,
        OP_ChannelMessage,
        OP_FinishTrade,
        OP_GMEndTraining,
        OP_GMTrainSkill,
        OP_ItemPacket,
        OP_NewZone,
        OP_SimpleMessage,
        OP_SpecialMesg,
        OP_TradeSkillCombine,
        SpellBuff,
    )

    if isinstance(payload, EQStruct):
        return payload
    if isinstance(payload, (bytes, bytearray)):
        parsed = body(opcode, bytes(payload))
        if parsed is not None:
            return parsed
        if opcode == "OP_BecomeCorpse" and len(payload) >= 4:
            spawn = struct.unpack_from("<I", payload)[0]
            return OP_BecomeCorpse(int(spawn), 0.0, 0.0, 0.0)
        empty = {
            "OP_FinishTrade": OP_FinishTrade(),
            "OP_GMEndTraining": OP_GMEndTraining(0, 0),
            "OP_GMTrainSkill": OP_GMTrainSkill(0, 0),
            "OP_TradeSkillCombine": OP_TradeSkillCombine(0),
        }
        if opcode in empty:
            return empty[opcode]
        raise AssertionError(f"{opcode} fixture did not decode")
    if isinstance(payload, dict):
        if opcode == "OP_ItemPacket":
            item = Item(
                0,
                int(payload.get("slot") or 0),
                str(payload.get("name") or ""),
                "",
                int(payload.get("item_id") or 0),
                int(payload.get("stack") or 1),
            )
            return OP_ItemPacket(item)
        if opcode == "OP_ChannelMessage":
            return OP_ChannelMessage(sender=str(payload.get("sender") or ""), text=str(payload.get("text") or ""))
        if opcode == "OP_NewZone":
            return OP_NewZone(str(payload.get("zone") or payload.get("short_name") or ""), 0.0, 0.0, 0.0)
        if opcode == "OP_SimpleMessage":
            texts = payload.get("texts") or ()
            if "text" in payload:
                texts = (str(payload["text"]),)
            return OP_SimpleMessage(int(payload.get("string_id") or 0), texts=tuple(texts))
        if opcode == "OP_SpecialMesg":
            return OP_SpecialMesg(message=str(payload.get("text") or payload.get("message") or ""))
        if opcode == "OP_Buff":
            return OP_Buff(0, SpellBuff(counters=int(payload.get("counters") or 0)), fade=int(payload.get("fade") or 0))
        if opcode == "OP_MobUpdate":
            from eqclient3.structs import OP_MobUpdate
            point = payload.get("point") or (0.0, 0.0, 0.0)
            return OP_MobUpdate(int(payload.get("spawn_id") or 0), float(point[0]), float(point[1]), float(point[2]))
    raise TypeError(f"{opcode} fixture is {type(payload).__name__}")


def kinds(client):
    return [type(action).__name__ for action in client.queue]


def place(client, action, zone, source):
    """Restore without letting append overwrite the zone the action started in."""
    action.zone = zone
    action.source = source
    client.journal.open_action(client.character, action)
    client.queue.restore(action)
    return action


MOVEMENT_PRESENT = _MOVEMENT_FILE.is_file()
