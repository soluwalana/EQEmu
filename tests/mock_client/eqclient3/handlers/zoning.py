"""Zone entry, an open ZoneChange, a closed session, and a reliable-stream hole."""
from __future__ import annotations

from eqclient3.actions.bots.form import Form
from eqclient3.actions.read_tasks import ReadTasks
from eqclient3.actions.zone import Zone
from eqclient3.handlers.common import call_transfer, character_name, form_commands, mobs_map, session_open, tutorial_done, zone_name
from eqclient3.handlers.common import enqueue_once as append_action
from eqclient3.structs import EQStruct, OP_NewZone, OP_ReliableHole, OP_RequestClientZoneChange, OP_ZoneChange
from eqclient3.handler import Handler
TUTORIAL = 'tutorialb'

class ZoningHandler(Handler):
    opcodes = ('OP_NewZone', 'OP_ZoneChange', 'OP_RequestClientZoneChange', 'OP_ReliableHole')

    def on(self, opcode: str, payload: EQStruct) -> None:
        if isinstance(payload, OP_ReliableHole):
            self.hole()
            return
        if isinstance(payload, OP_NewZone):
            self.new_zone(payload)
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
        zone_id = row.zone_id
        world.zone = short
        if zone_id:
            world.zone_id = zone_id
        world.safe = (x, y, z)
        world.ground.clear()
        self.drop_npc_corpses()
        if short.lower() == TUTORIAL:
            self.mark_started('tutorial_started')
            if not tutorial_done(self.loop, world):
                append_action(self.loop, world, ReadTasks(), 'read_tasks:tutorialb')
            return
        action = Form(short, form_commands(world, self.loop))
        append_action(self.loop, world, action, f'form:{short}')

    def mark_started(self, name: str) -> None:
        """Remember on the character, and in the journal, that this progress has started."""
        world = self.world
        if name == 'tutorial_started':
            world.tutorial_started = True
        elif name == 'quest_started':
            world.quest_started = True
        journal = self.loop.journal
        who = character_name(self.loop, world)
        if not journal or not who:
            return
        try:
            journal.set_flag(who, name, 1)
        except AttributeError:
            return

    def drop_npc_corpses(self) -> None:
        """A zone change drops a dead NPC. A body with a Reclaim on the queue stays."""
        world = self.world
        own = {action.corpse_id for action in self.loop.queue if type(action).__name__ == 'Reclaim'}
        own.add(world.self_id)
        for spawn_id, mob in list(mobs_map(world).items()):
            if mob.dead and spawn_id not in own:
                mobs_map(world).pop(spawn_id, None)

    def zone_change(self, row: OP_ZoneChange) -> None:
        zone_id, success = row.zone_id, row.success
        loop = self.loop
        if not session_open(loop):
            call_transfer(loop)
            return
        world = self.world
        if success != 1 or not zone_id:
            return
        if zone_id == world.zone_id and world.zone:
            return
        name = zone_name(world, zone_id)
        append_action(loop, world, Zone(name), f'zone:{name}')

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
        loop.send('OP_ZoneChange', OP_ZoneChange(character_name(loop, world), zone_id, x, y, z).serialize())
