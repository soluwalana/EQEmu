from enum import IntEnum

from eqclient4.handler import Handler
from eqclient4.log import log
from eqclient4.structs import (
    EQStruct,
    OP_GroupDisbandOther,
    OP_GroupDisbandYou,
    OP_GroupUpdate,
    OP_GroupUpdateB,
    OP_RaidUpdate,
)


class GroupAction(IntEnum):
    JOIN = 0
    LEAVE = 1
    DISBAND = 6
    UPDATE = 7
    MAKE_LEADER = 8
    INVITE_INITIAL = 9
    AA_UPDATE = 10


class RaidAction(IntEnum):
    ADD = 0
    REMOVE_2 = 1
    MEMBER_NAME_CHANGE = 2
    REMOVE_1 = 3
    NO_LONGER_LEADER = 4
    DISBAND = 5
    MEMBERS = 6
    NO_ASSIGN_LEADERSHIP = 7
    CREATE = 8
    UNKNOWN = 9
    NO_RAID = 10
    CHANGE_LOOT_TYPE = 11
    STRING_ID = 12
    CHANGE_GROUP_LEADER = 13
    SET_LEADER_ABILITIES = 14
    SET_LEADER_DATA = 15
    CHANGE_GROUP = 16
    LOCK = 17
    UNLOCK = 18
    RED_STRING_ID = 19
    SET_LEADER = 20
    MAKE_LEADER = 30
    SET_MOTD = 35
    SET_NOTE = 36


class GroupingHandler(Handler):
    opcodes = (
        "OP_GroupUpdate",
        "OP_GroupUpdateB",
        "OP_GroupDisbandOther",
        "OP_GroupDisbandYou",
        "OP_RaidUpdate",
    )

    def on(self, opcode: str, payload: EQStruct) -> None:
        match payload:
            case OP_GroupUpdate() | OP_GroupUpdateB():
                members = payload.members
                if payload.full:
                    self.world.active_group.clear()
                    for member in members:
                        bot = self.world.bot_roster.bot_by_name(member)
                        if bot:
                            log.info(f"Adding bot to active group: {bot.name}")
                            self.world.active_group[bot.spawn_id] = bot
                        else:
                            log.error(f"Bot not found: {member}")
                elif payload.action == GroupAction.JOIN and payload.your_name:
                    bot = self.world.bot_roster.bot_by_name(payload.your_name)
                    if bot:
                        log.info(f"Adding bot to active group: {bot.name}")
                        self.world.active_group[bot.spawn_id] = bot
                    else:
                        log.error(f"Bot not found: {payload.your_name}")

                return

            case OP_GroupDisbandOther():
                bot = self.world.bot_roster.bot_by_name(payload.member_name)
                if bot:
                    log.info(f"Removing bot from active group: {bot.name}")
                    self.world.active_group.pop(bot.spawn_id)
                else:
                    log.error(f"Bot not found: {payload.member_name}")
                return

            case OP_GroupDisbandYou():
                self.world.active_group.clear()
                return

            case OP_RaidUpdate():
                bot = self.world.bot_roster.bot_by_name(payload.your_name)
                if not bot:
                    log.error(f"Bot not found: {payload.your_name}")
                    return
                # common/raid.h: raidAdd=0, raidRemove2=1, raidRemove1=3,
                # raidDisband=5, raidCreate=8, raidNoRaid=10.
                if payload.action == RaidAction.ADD and payload.your_name:
                    log.info(f"Adding bot to active group: {bot.name}")
                    self.world.active_group[bot.spawn_id] = bot
                elif payload.action in (RaidAction.REMOVE_2, RaidAction.REMOVE_1):
                    log.info(f"Removing bot from active group: {bot.name}")
                    self.world.active_group.pop(bot.spawn_id)
                elif payload.action in (RaidAction.DISBAND, RaidAction.CREATE, RaidAction.NO_RAID):
                    log.info(f"Clearing active group")
                    self.world.active_group.clear()
                return

            case _:
                log.error(f"Unknown opcode: {opcode}")
