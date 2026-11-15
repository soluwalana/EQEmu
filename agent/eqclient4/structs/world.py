import re
import struct
from collections.abc import Collection
from dataclasses import dataclass, field
from enum import Enum, IntEnum

from eqclient4.structs.wire import (
    EQStruct,
    advance,
    cstring,
    fixed,
    need,
    put_cstr,
    put_fixed,
    read_u32,
    u32,
)

DOOR_SIZE = 100


class DoorAction(IntEnum):
    OPEN = 0x02
    CLOSE = 0x03

    OPEN_INVERTED = 0x03
    CLOSE_INVERTED = 0x02


class DoorOpenType(IntEnum):
    SWING_BACKWARD = 0
    SWING_FORWARD = 5
    STATIC_CLICK_ONCE = 9
    SLIDE_FORWARD = 10
    STATIC = 31
    SLIDE_SIDEWAYS = 45
    INVISIBLE = 50
    STATIC_56 = 56
    TELEPORTER = 57
    STATIC_INTERACTABLE = 58
    LIFT = 59
    LIFT_DRAWBRIDGE = 60
    ROTATE_HEADING = 100
    ROTATE_INCLINE = 105
    SAW_TRAP = 115
    SPEAR_TRAP_VERTICAL = 120
    SPEAR_TRAP_HORIZONTAL = 125
    PENDULUM_TRAP = 130
    BLADE_TRAP = 135
    CRUSH_TRAP = 140
    BUYER_STALL = 155


class DoorKind(str, Enum):
    """Visual classification, not a protocol field or navigation rule."""

    DOOR = "door"
    TREE = "tree"
    FURNITURE = "furniture"
    WEAPON = "weapon"
    PORTAL = "portal"
    LIFT = "lift"
    TRAP = "trap"
    MECHANISM = "mechanism"
    OBJECT = "object"


@dataclass
class Door(EQStruct):
    id: int
    name: str
    x: float
    y: float
    z: float
    open_type: int

    heading: float = 0.0
    incline: int = 0
    size: int = 100
    state_at_spawn: int = 0
    invert_state: int = 0
    door_param: int = 0xFFFFFFFF

    opened: bool = field(default=False, repr=False)

    def serialize(self) -> bytes:
        blob = bytearray(DOOR_SIZE)
        put_fixed(blob, 0, self.name, 32)

        struct.pack_into(
            "<ffffII",
            blob,
            32,
            self.y,
            self.x,
            self.z,
            self.heading,
            self.incline,
            self.size,
        )

        struct.pack_into(
            "<BBBBI",
            blob,
            60,
            self.id,
            self.open_type,
            self.state_at_spawn,
            self.invert_state,
            self.door_param,
        )

        blob[81] = 1
        blob[83] = 1

        return bytes(blob)

    @classmethod
    def deserialize(cls, data: bytes) -> Door:
        need(data, DOOR_SIZE, "door")

        y, x, z, heading, incline, size = struct.unpack_from(
            "<ffffII", data, 32
        )

        door_id, open_type, state, invert, param = (
            struct.unpack_from("<BBBBI", data, 60)
        )

        return cls(
            id=door_id,
            name=fixed(data, 0, 32),
            x=x,
            y=y,
            z=z,
            open_type=open_type,
            heading=heading,
            incline=incline,
            size=size,
            state_at_spawn=state,
            invert_state=invert,
            door_param=param,
            opened=bool(state) != bool(invert)
        )

    @staticmethod
    def normalize_model(name: str) -> str:
        """Normalize client model names and PEQ id_file strings for comparison."""
        return name.strip().upper().removesuffix("_ACTORDEF").removeprefix("OBJ_")

    @property
    def model_key(self) -> str:
        return self.normalize_model(self.name)

    @property
    def kind(self) -> DoorKind:
        return self.classify()

    def classify(self, weapon_models: Collection[str] = ()) -> DoorKind:
        """Classify the model for the debug map, without changing its wire type.

        OP_SpawnDoor includes props as well as doors. Open type specifies
        behavior, not the model's identity. The optional item-cache model
        index can identify opaque IT models; unknown models stay generic.
        """
        t = self.open_type
        if t == DoorOpenType.TELEPORTER:
            return DoorKind.PORTAL
        if t in (DoorOpenType.LIFT, DoorOpenType.LIFT_DRAWBRIDGE):
            return DoorKind.LIFT
        if t in (115, 116, 120, 125, 130, 135, 140, 142, 143, 144, 145, 146, 150, 151, 152):
            return DoorKind.TRAP

        model = self.model_key
        # Zone-specific names can embed the object token (e.g. TUTORIALDOOR1).
        # Separate numeric suffixes and punctuation, but keep model prefixes.
        parts = re.findall(r"[A-Z]+", model)
        if any(p.startswith(("TREE", "PALM", "SHRUB", "BUSH")) for p in parts):
            return DoorKind.TREE
        if t == DoorOpenType.BUYER_STALL or any(
            p.startswith(("TABLE", "CHAIR", "BENCH", "BED", "DESK", "BOOKCASE",
                          "CABINET", "SHELF", "STOOL", "THRONE")) for p in parts
        ):
            return DoorKind.FURNITURE
        if any(p.startswith(("SWORD", "SPEAR", "DAGGER", "AXE", "MACE", "LANCE",
                             "HALBERD", "WEAPON")) or p == "BOW" for p in parts):
            return DoorKind.WEAPON
        if model and model in weapon_models:
            return DoorKind.WEAPON
        if re.search(r"(?:DOOR|PORTCULLIS|DRAWBRIDGE|HATCH|GATE(?!KEEPER))", model):
            return DoorKind.DOOR
        # Only the documented moving/invisible door types; the gaps in
        # the sliding range are stationary props, not sliding doors.
        if 0 <= t <= 8 or t in (10, 11, 12, 15, 16, 17, 20, 21, 22,
                                25, 26, 27, 45, 50, 53, 54):
            return DoorKind.DOOR
        if t in (30, 35, 36, 40, 100, 101, 102, 105, 106, 107):
            return DoorKind.MECHANISM
        return DoorKind.OBJECT

    @property
    def position(self) -> tuple[float, float, float]:
        return (self.x, self.y, self.z)



def _door_list(data: bytes) -> list[Door]:
    if len(data) < DOOR_SIZE:
        return []
    usable = data[: len(data) - len(data) % DOOR_SIZE]
    doors = []
    for offset in range(0, len(usable), DOOR_SIZE):
        doors.append(Door.deserialize(usable[offset : offset + DOOR_SIZE]))
    return doors


def _pack_doors(doors: list[Door]) -> bytes:
    return b"".join(door.serialize() for door in doors)


@dataclass
class OP_SpawnDoor(EQStruct):
    doors: list[Door] = field(default_factory=list)

    def serialize(self) -> bytes:
        return _pack_doors(self.doors)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_SpawnDoor:
        return cls(_door_list(data))


@dataclass
class OP_DoorSpawn(EQStruct):
    doors: list[Door] = field(default_factory=list)

    def serialize(self) -> bytes:
        return _pack_doors(self.doors)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_DoorSpawn:
        return cls(_door_list(data))


@dataclass
class OP_Doors(EQStruct):
    doors: list[Door] = field(default_factory=list)

    def serialize(self) -> bytes:
        return _pack_doors(self.doors)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_Doors:
        return cls(_door_list(data))


@dataclass
class OP_MoveDoor(EQStruct):
    door_id: int
    action: int = 0

    def serialize(self) -> bytes:
        return bytes((self.door_id & 0xFF, self.action & 0xFF))

    @classmethod
    def deserialize(cls, data: bytes) -> OP_MoveDoor:
        if not data:
            raise ValueError("OP_MoveDoor is empty")
        action = data[1] if len(data) > 1 else 0
        return cls(int(data[0]), int(action))


@dataclass
class OP_ClickDoor(EQStruct):
    door_id: int
    unknown1: int = 0
    unknown2: int = 0
    unknown3: int = 0
    pick_lock_skill: int = 0
    item_id: int = 0
    player_id: int = 0

    def serialize(self) -> bytes:
        packet = bytearray(16)
        packet[0] = self.door_id & 0xFF
        packet[1] = self.unknown1 & 0xFF
        packet[2] = self.unknown2 & 0xFF
        packet[3] = self.unknown3 & 0xFF
        packet[4] = self.pick_lock_skill & 0xFF
        # common/eq_packet_structs.h:2943
        struct.pack_into(
            "<IH",
            packet,
            8,
            self.item_id & 0xFFFFFFFF,
            self.player_id & 0xFFFF,
        )
        return bytes(packet)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ClickDoor:
        if not data:
            raise ValueError("OP_ClickDoor is empty")
        unknown1 = data[1] if len(data) > 1 else 0
        unknown2 = data[2] if len(data) > 2 else 0
        unknown3 = data[3] if len(data) > 3 else 0
        pick = data[4] if len(data) > 4 else 0
        item_id = read_u32(data, 8) if len(data) >= 12 else 0
        player_id = struct.unpack_from("<H", data, 12)[0] if len(data) >= 14 else 0
        return cls(
            int(data[0]),
            int(unknown1),
            int(unknown2),
            int(unknown3),
            int(pick),
            int(item_id),
            int(player_id),
        )


@dataclass
class OP_GroundSpawn(EQStruct):
    drop_id: int
    name: str
    x: float
    y: float
    z: float
    heading: float = 0.0

    def serialize(self) -> bytes:
        prefix = u32(self.drop_id) + put_cstr(self.name)
        # common/patches/rof2.cpp:1507
        return prefix + struct.pack(
            "<HHII4f3fi",
            0,
            0,
            self.drop_id & 0xFFFFFFFF,
            0,
            self.heading,
            0.0,
            0.0,
            1.0,
            self.y,
            self.x,
            self.z,
            0,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_GroundSpawn:
        need(data, 5, "OP_GroundSpawn")
        drop_id = read_u32(data)
        name, offset = cstring(data, 4)
        offset = advance(data, offset, 12 + 28, "OP_GroundSpawn")
        heading, _tilt_x, _tilt_y, _size, wire_y, wire_x, wire_z = struct.unpack_from(
            "<7f",
            data,
            offset - 28,
        )
        return cls(
            int(drop_id),
            name,
            float(wire_x),
            float(wire_y),
            float(wire_z),
            float(heading),
        )


@dataclass
class OP_ClickObject(EQStruct):
    drop_id: int
    player_id: int | None = None

    def serialize(self) -> bytes:
        player_id = 0 if self.player_id is None else self.player_id
        # common/eq_packet_structs.h:2853 ClickObject_Struct
        return struct.pack(
            "<II",
            self.drop_id & 0xFFFFFFFF,
            int(player_id) & 0xFFFFFFFF,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ClickObject:
        need(data, 4, "OP_ClickObject")
        drop_id = read_u32(data)
        if len(data) >= 8:
            return cls(drop_id, read_u32(data, 4))
        return cls(drop_id, None)
