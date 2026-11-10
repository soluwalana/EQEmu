import time
from dataclasses import asdict

from eqclient4.data.ground import LiveGroundSpawn
from eqclient4.handler import Handler
from eqclient4.log import log
from eqclient4.structs import EQStruct, OP_ClickObject, OP_GroundSpawn


class SpawnsHandler(Handler):
    opcodes = (
        "OP_GroundSpawn",
        "OP_ClickObject",
    )

    def on(self, opcode: str, payload: EQStruct) -> None:
        match payload:
            case OP_GroundSpawn():
                potential_spawns = self.world.ground_book.spawns_at_coordinates(
                    payload.x, payload.y, payload.z
                )
                for spawn in potential_spawns:
                    self.world.ground_spawns.setdefault(spawn.item_id, []).append(
                        LiveGroundSpawn(
                            **asdict(spawn),
                            instance_id=payload.drop_id,
                            observed_x=payload.x,
                            observed_y=payload.y,
                            observed_z=payload.z,
                            observed_time=int(time.time()),
                        )
                    )

            case OP_ClickObject():
                item_ids = []
                for item_id, spawns in self.world.ground_spawns.items():
                    for spawn in spawns:
                        if spawn.instance_id == payload.drop_id:
                            item_ids.append(item_id)

                for item_id in item_ids:
                    if item_id not in self.world.ground_spawns:
                        continue

                    indices = []
                    for index, spawn in enumerate(self.world.ground_spawns[item_id]):
                        if spawn.instance_id == payload.drop_id:
                            indices.append(index)

                    for index in reversed(indices):
                        self.world.ground_spawns[item_id].pop(index)

            case _:
                log.error(f"Unknown spawn opcode: {opcode}")
