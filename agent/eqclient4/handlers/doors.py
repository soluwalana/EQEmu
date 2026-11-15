"""Doors and ground spawns. Pickup is Fetch's step. OP_ClickDoor is movement's send."""

from __future__ import annotations

from eqclient4.structs import (
    EQStruct,
    DoorAction,
    OP_DoorSpawn,
    OP_Doors,
    OP_MoveDoor,
    OP_SpawnDoor,
)
from eqclient4.handler import Handler
from eqclient4.log import log


class DoorsHandler(Handler):
    opcodes = (
        "OP_SpawnDoor",
        "OP_DoorSpawn",
        "OP_Doors",
        "OP_MoveDoor",
    )

    def on(self, opcode: str, payload: EQStruct) -> None:
        match payload:
            case OP_SpawnDoor() | OP_DoorSpawn() | OP_Doors():
                self.doors(payload)
            case OP_MoveDoor():
                self.move(payload)
    
    def doors(self, row: OP_SpawnDoor | OP_DoorSpawn | OP_Doors) -> None:
        if not row.doors:
            return
        
        doors = self.world.doors
        for found in row.doors:

            previous = doors.get(found.id)
            if not previous:
                doors[found.id] = found

            if found.opened:
                self.world.open_doors.add(found.id)
            else:
                self.world.open_doors.discard(found.id)

            doors[found.id].opened = found.opened

    def move(self, row: OP_MoveDoor) -> None:
        door_id = row.door_id
        door = self.world.doors.get(row.door_id)
        if not door:
            log.error(f"Door move sent to non existing door: {door_id}")
            return

        if row.action not in (DoorAction.OPEN, DoorAction.CLOSE):
            return

        if row.action == DoorAction.OPEN:
            door.opened = not bool(door.invert_state)
        else:
            door.opened = bool(door.invert_state)

        if door.opened:
            self.world.open_doors.add(door_id)
        else:
            self.world.open_doors.discard(door_id)

        self.world.clicked_doors.discard(door_id)

