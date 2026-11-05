"""Zone entry, an open ZoneChange, a closed session, and a reliable-stream hole."""

from eqclient4.handler import Handler
from eqclient4.log import log

# from eqclient4.actions.bots.form import queue_form
# from eqclient4.actions.level_up import queue_level_gear
from eqclient4.quests.produce import produce
from eqclient4.structs import (
    EQStruct,
    OP_ClientReady,
    OP_NewZone,
    OP_ReliableHole,
    OP_RequestClientZoneChange,
    OP_ZoneChange,
)

TUTORIAL = "tutorialb"


class ZoningHandler(Handler):
    opcodes = (
        "OP_NewZone",
        "OP_ClientReady",
        "OP_ZoneChange",
        "OP_RequestClientZoneChange",
        "OP_ReliableHole",
    )

    def on(self, opcode: str, payload: EQStruct) -> None:
        match payload:
            case OP_ReliableHole():
                # A reliable-stream hole rezones on the copied session and does not append Zone.
                self.loop.client.transfer_zone()
                return

            case OP_NewZone():
                self.new_zone(payload)

            case OP_ClientReady():
                self.form_party()

            case OP_ZoneChange():
                self.zone_change(payload)

            case OP_RequestClientZoneChange():
                self.request(payload)

            case _:
                log.error("unknown opcode: %s", opcode)

    def new_zone(self, row: OP_NewZone) -> None:
        short, x, y, z = row.short_name, row.x, row.y, row.z
        world = self.world
        previous = str(world.zone or "")
        previous_id = int(world.zone_id or 0)

        zone_id = row.zone_id
        world.zone = short
        world.zone_id = zone_id

        world.safe = (x, y, z)
        world.ground.clear()
        self.drop_npc_corpses()

        moved = (short.lower() != previous.lower()) or (zone_id != previous_id)

        if not moved:
            return

        world.zone_formed = short

        if short.lower() == TUTORIAL:
            if self.loop.journal.get_flag(world.character.name, "tutorial_state") == "started":
                return

            world.tutorial_started = True
            self.loop.journal.set_flag(
                world.character.name,
                "tutorial_state",
                "started",
            )
            log.error("Need to implement queue_level_gear(self.loop, self.world)")

        tutorial_done = world.journal.get_flag(world.character.name, "tutorial_state") == "done"
        if not tutorial_done:
            self.loop.journal.set_flag(
                world.character.name,
                "tutorial_state",
                "done",
            )
            produce(self.loop, world, leaving_tutorial=True)

    def form_party(self) -> None:
        """Login and rezone. A same-zone OP_ClientReady is the weather refresh."""
        log.error("Need to implement queue_form(self.loop, self.world)")

    def drop_npc_corpses(self) -> None:
        """A zone change drops a dead NPC. A body with a Reclaim on the queue stays."""
        own = {action.corpse_id for action in self.loop.queue if type(action).__name__ == "Reclaim"}
        own.add(self.world.self_id)
        for spawn_id, mob in list(self.world.mobs.items()):
            if mob.dead and spawn_id not in own:
                self.world.mobs.pop(spawn_id, None)

    def zone_change(self, payload: OP_ZoneChange) -> None:
        """Cross-zone success reconnects. Sending another OP_ZoneChange cancels it.

        The packet's coordinates are a cancel or a same-zone move. A successful
        cross-zone packet leaves them at zero, and applying that walks the next
        zone from the origin.
        """
        zone_id, success = payload.zone_id, payload.success
        if not self.loop.session_open():
            self.loop.client.transfer_zone()
            return

        if success == 1 and zone_id and zone_id != self.world.zone_id:
            self.world.zone_id = zone_id
            self.loop.client.transfer_zone()
            return

        payload_point = (payload.x, payload.y, payload.z)
        # A cross-zone success leaves x, y, z at zero. Snapping that walks the new zone from the origin.
        if success == 1 and not payload_point:
            return

        self.world.movement.snap(payload_point)

    def request(self, payload: OP_RequestClientZoneChange) -> None:
        """The server asked us to move. A different zone is confirmed with OP_ZoneChange.

        The same zone is a position. The server leaves that unanswered, and a reply drops the socket.
        """
        zone_id, x, y, z = payload.zone_id, payload.x, payload.y, payload.z
        if zone_id and zone_id == self.world.zone_id:
            self.world.movement.snap((x, y, z))
            return

        if not zone_id:
            return

        if not self.loop.session_open():
            self.loop.client.transfer_zone()
            return
        self.loop.send(
            "OP_ZoneChange",
            OP_ZoneChange(self.world.character.name, zone_id, x, y, z).serialize(),
        )
