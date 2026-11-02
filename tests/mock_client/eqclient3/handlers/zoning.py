"""Zone entry, an open ZoneChange, a closed session, and a reliable-stream hole."""

from __future__ import annotations

from eqclient3.log import log
from eqclient3.actions.bots.form import queue_form
from eqclient3.actions.read_tasks import ReadTasks
from eqclient3.quests.produce import produce
from eqclient3.handlers.common import (
    call_transfer,
    character_name,
    mobs_map,
    session_open,
    tutorial_done,
)
from eqclient3.handlers.common import enqueue_once as append_action
from eqclient3.structs import (
    EQStruct,
    OP_ClientReady,
    OP_NewZone,
    OP_ReliableHole,
    OP_RequestClientZoneChange,
    OP_ZoneChange,
)
from eqclient3.handler import Handler

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
        if isinstance(payload, OP_ReliableHole):
            self.hole()
            return
        if isinstance(payload, OP_NewZone):
            self.new_zone(payload)
        elif isinstance(payload, OP_ClientReady):
            self.form_party()
        elif isinstance(payload, OP_ZoneChange):
            self.zone_change(payload)
        elif isinstance(payload, OP_RequestClientZoneChange):
            self.request(payload)

    def hole(self) -> None:
        """A reliable-stream hole rezones on the copied session and does not append Zone."""
        call_transfer(self.loop)

    def new_zone(self, row: OP_NewZone) -> None:
        short, x, y, z = row.short_name, row.x, row.y, row.z
        world = self.world
        previous = str(world.zone or "")
        previous_id = int(world.zone_id or 0)
        zone_id = row.zone_id
        world.zone = short
        if zone_id:
            world.zone_id = zone_id
        world.safe = (x, y, z)
        world.ground.clear()
        self.drop_npc_corpses()
        moved = short.lower() != previous.lower() or (
            bool(zone_id) and bool(previous_id) and int(zone_id) != previous_id
        )
        if moved:
            world.formed_for = ""
        # Weather and zone-data edits resend OP_NewZone. Remember the first one.
        if world.form_return is None:
            world.form_return = bool(world.tutorial_started)
        if short.lower() == TUTORIAL:
            self.mark_started("tutorial_started")
            if not tutorial_done(self.loop, world):
                append_action(self.loop, world, ReadTasks(), "read_tasks:tutorialb")
        elif tutorial_done(self.loop, world):
            produce(self.loop, world, leaving_tutorial=True)

    def form_party(self) -> None:
        """Login and rezone. A same-zone OP_ClientReady is the weather refresh."""
        queue_form(self.loop, self.world)

    def mark_started(self, name: str) -> None:
        """Remember on the character, and in the journal, that this progress has started."""
        world = self.world
        if name == "tutorial_started":
            world.tutorial_started = True
        elif name == "quest_started":
            world.quest_started = True
        journal = self.loop.journal
        who = character_name(self.loop, world)
        if not journal or not who:
            return
        try:
            journal.set_flag(who, name, 1)
        except AttributeError:
            log.error("progress flag %s was not saved", name, exc_info=True)
            return

    def drop_npc_corpses(self) -> None:
        """A zone change drops a dead NPC. A body with a Reclaim on the queue stays."""
        world = self.world
        queue = self.loop.queue
        own = (
            {action.corpse_id for action in queue if type(action).__name__ == "Reclaim"} if queue is not None else set()
        )
        own.add(world.self_id)
        for spawn_id, mob in list(mobs_map(world).items()):
            if mob.dead and spawn_id not in own:
                mobs_map(world).pop(spawn_id, None)

    def zone_change(self, row: OP_ZoneChange) -> None:
        """Cross-zone success reconnects. Sending another OP_ZoneChange cancels it.

        The packet's coordinates are a cancel or a same-zone move. A successful
        cross-zone packet leaves them at zero, and applying that walks the next
        zone from the origin.
        """
        zone_id, success = row.zone_id, row.success
        loop = self.loop
        world = self.world
        if not session_open(loop):
            call_transfer(loop)
            return
        if success == 1 and zone_id and zone_id != world.zone_id:
            world.zone_id = zone_id
            call_transfer(loop)
            return
        # A cross-zone success leaves x, y, z at zero. Snapping that walks the new zone from the origin.
        if success == 1 and not (row.x or row.y or row.z):
            return
        world.movement.snap(world, (row.x, row.y, row.z))

    def request(self, payload: OP_RequestClientZoneChange) -> None:
        """The server asked us to move. A different zone is confirmed with OP_ZoneChange.

        The same zone is a position. The server leaves that unanswered, and a reply drops the socket.
        """
        row = payload
        zone_id, x, y, z = row.zone_id, row.x, row.y, row.z
        world = self.world
        if zone_id and zone_id == world.zone_id:
            world.movement.snap(world, (x, y, z))
            return
        if not zone_id:
            return
        loop = self.loop
        if not session_open(loop):
            call_transfer(loop)
            return
        loop.send(
            "OP_ZoneChange",
            OP_ZoneChange(character_name(loop, world), zone_id, x, y, z).serialize(),
        )
