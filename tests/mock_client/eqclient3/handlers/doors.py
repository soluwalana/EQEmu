"""Doors and ground spawns. Pickup is Fetch's step. OP_ClickDoor is movement's send."""

from __future__ import annotations

from eqclient3.structs import (
    EQStruct,
    OP_ClickObject,
    OP_DoorSpawn,
    OP_Doors,
    OP_GroundSpawn,
    OP_MoveDoor,
    OP_SpawnDoor,
)
from eqclient3.handler import Handler
from eqclient3.world import Door, GroundSpawn


class DoorsHandler(Handler):
    opcodes = (
        "OP_SpawnDoor",
        "OP_DoorSpawn",
        "OP_Doors",
        "OP_GroundSpawn",
        "OP_MoveDoor",
        "OP_ClickObject",
    )

    def on(self, opcode: str, payload: EQStruct) -> None:
        del opcode
        if isinstance(payload, (OP_SpawnDoor, OP_DoorSpawn, OP_Doors)):
            self.doors(payload)
        elif isinstance(payload, OP_GroundSpawn):
            self.ground(payload)
        elif isinstance(payload, OP_MoveDoor):
            self.move(payload)
        elif isinstance(payload, OP_ClickObject):
            self.click(payload)

    def doors(self, row: OP_SpawnDoor | OP_DoorSpawn | OP_Doors) -> None:
        if not row.doors:
            return
        doors = self.world.doors
        for found in row.doors:
            door_id, name, x, y, z, open_type = (
                found.door_id,
                found.name,
                found.x,
                found.y,
                found.z,
                found.open_type,
            )
            previous = doors.get(door_id)
            door = Door(door_id, name, x, y, z, open_type)
            if previous:
                door.opened = bool(previous.opened)
            doors[door_id] = door

    def ground(self, row: OP_GroundSpawn) -> None:
        self.world.ground[row.drop_id] = GroundSpawn(row.drop_id, row.name, row.x, row.y, row.z)

    def move(self, row: OP_MoveDoor) -> None:
        door = self.world.doors.get(row.door_id)
        if door:
            door.opened = True

    def click(self, row: OP_ClickObject) -> None:
        ground = self.world.ground.get(row.drop_id)
        if ground:
            ground.used = True
