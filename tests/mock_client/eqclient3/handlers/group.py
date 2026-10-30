"""Group and raid membership. An invite appends Seat for the player being given one."""
from __future__ import annotations

from eqclient3.actions.seat import Seat
from eqclient3.handlers.common import bot_rows, character_name, enqueue_once
from eqclient3.structs import EQStruct, OP_GroupInvite, OP_GroupInvite2, OP_GroupUpdate, OP_RaidJoin, OP_RaidUpdate
from eqclient3.world import GroupRoster
from eqclient3.handler import Handler
JOIN = 0
LEAVE = 1
DISBAND = 6
UPDATE = 7
MAKE_LEADER = 8
INVITE = 9

class GroupHandler(Handler):
    opcodes = ('OP_GroupUpdate', 'OP_RaidUpdate', 'OP_RaidJoin', 'OP_GroupInvite', 'OP_GroupInvite2')

    def on(self, opcode: str, payload: EQStruct) -> None:
        del opcode
        if isinstance(payload, (OP_GroupInvite, OP_GroupInvite2)):
            self.invite(payload)
            return
        if isinstance(payload, (OP_RaidUpdate, OP_RaidJoin)):
            self.roster(payload, self.world.raid)
            return
        if isinstance(payload, OP_GroupUpdate):
            self.roster(payload, self.world.group)

    def roster(self, row: OP_GroupUpdate | OP_RaidUpdate | OP_RaidJoin, sheet: GroupRoster) -> None:
        if isinstance(row, OP_GroupUpdate) and row.full:
            action = row.action
            your = row.your_name
            members = list(row.members)
            leader = row.leader
            names = [name for name in [your, *members] if name]
            if action == DISBAND:
                sheet.members = []
                sheet.leader = ''
                return
            if action == LEAVE:
                leaving = members[0] if members and members[0] else your
                sheet.members = [name for name in sheet.members if name.lower() != leaving.lower()]
                return
            if action in (JOIN, UPDATE, INVITE, MAKE_LEADER) or names:
                sheet.members = _unique(names)
            if leader:
                sheet.leader = leader
            elif action == MAKE_LEADER and your:
                sheet.leader = your
            return
        if row.your_name or row.leader:
            player = row.your_name
            leader = row.leader
            if player and player not in sheet.members:
                sheet.members.append(player)
            if leader:
                sheet.leader = leader
                if leader not in sheet.members:
                    sheet.members.append(leader)

    def invite(self, row: OP_GroupInvite | OP_GroupInvite2) -> None:
        invitee = row.invitee
        inviter = row.inviter
        world = self.world
        me = character_name(self.loop, world).lower()
        if me and invitee.lower() == me:
            name = inviter
            accept = True
        else:
            name = invitee or inviter
            accept = False
        if not name:
            return
        enqueue_once(self.loop, world, Seat(name, self.commands(name, accept)), f'seat:{name}')

    def commands(self, name: str, accept: bool) -> list[str]:
        bot = ''
        for row in bot_rows(self.world):
            if isinstance(row, str):
                bot = row
                break
            class_id = int(row[1]) if isinstance(row, (tuple, list)) and len(row) > 1 else 0
            who = str(row[0]) if isinstance(row, (tuple, list)) and row else str(row.name or '')
            if who and class_id not in (1, 2):
                bot = who
                break
            if who and (not bot):
                bot = who
        commands = []
        if bot:
            commands.append(f'^botcamp byname {bot}')
        commands.append(f'follow {name}' if accept else f'invite {name}')
        return commands

def _unique(names: list[str]) -> list[str]:
    found = []
    seen = set()
    for name in names:
        key = name.lower()
        if key in seen:
            continue
        seen.add(key)
        found.append(name)
    return found
