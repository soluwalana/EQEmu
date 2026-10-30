"""Opcode coverage for handlers/messages.py."""

from eqclient3.handlers import messages
from eqclient3.world import Faction, Mob
from support import Loop, World, channel, names, simple, special


class _Active:

    def __init__(self):
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)


class _Journal:

    def __init__(self):
        self.flags = {"Coalition of Tradefolk": 20}
        self.setting = None

    def flag_values(self, character):
        return self.flags

    def set_flag(self, character, name, value):
        self.flags[name] = value

    def set_bot_setting(self, character, bot, key, value):
        self.setting = (bot, key, value)

    def resolved(self, character, source=None):
        del character, source
        return False

    def resolved_sources(self, character=None):
        del character
        return set()


def test_a_claimed_line_reaches_every_waiter_once():
    from eqclient3.actions.talk import Talk
    from eqclient3.bus import Bus

    world = World(name="Hero")
    loop = Loop()
    first = Talk(1, "hail", "")
    second = Talk(2, "hail", "")
    loop.queue = [first, second]
    loop.active = first
    Bus(loop.queue, world, loop).publish("OP_SimpleMessage", simple(124))
    assert len(first.messages) == 1
    assert len(second.messages) == 1
    assert first.messages[0].payload.string_id == 124
    assert second.messages[0].payload.string_id == 124


def test_opcodes():
    lines = []
    import eqclient3.handlers.common as common

    original = common.write

    def _capture(line, stream=None):
        del stream
        lines.append(line)

    common.write = _capture
    try:
        _messages(lines)
    finally:
        common.write = original


def _messages(lines) -> None:
    world = World(name="Hero", zone="qeynos")
    world.faction_names = {"coalition of tradefolk": 42}
    world.factions = {42: Faction(20)}
    loop = Loop()
    loop.journal = _Journal()
    loop.active = _Active()

    merchant = Mob(8, "a merchant")
    merchant.faction_id = 42
    world.mobs[8] = merchant
    messages.MessagesHandler().handle("OP_ChannelMessage", channel("Guard", "hello there"), world, loop)
    messages.MessagesHandler().handle("OP_SpecialMesg", special("a merchant", "well met"), world, loop)
    assert "Guard: hello there" in lines
    assert "a merchant: well met" in lines
    assert loop.queue == []
    messages.MessagesHandler().handle("OP_SimpleMessage", simple(124), world, loop)
    assert [item.opcode for item in loop.active.messages] == [
        "OP_ChannelMessage",
        "OP_SpecialMesg",
        "OP_SimpleMessage",
    ]
    assert loop.active.messages[-1].payload.string_id == 124
    assert loop.queue == []
    messages.MessagesHandler().handle("OP_SimpleMessage", simple(1166, "a merchant"), world, loop)
    messages.MessagesHandler().handle("OP_SimpleMessage", simple(1171, "a merchant"), world, loop)
    assert names(loop) == ["FetchFaction"]
    assert loop.queue[0].faction_id == 42
    assert loop.queue[0].source == "faction:42"
    assert loop.queue[0].priority == 0
    messages.MessagesHandler().handle("OP_SimpleMessage", simple(1154, "Human"), world, loop)
    assert names(loop) == ["FetchFaction"]
    assert loop.active.messages[-1].payload.string_id == 1154
    messages.MessagesHandler().handle(
        "OP_SimpleMessage",
        simple(
            472,
            "Coalition of Tradefolk",
            "Your faction standing with Coalition of Tradefolk has been adjusted by 5.",
        ),
        world,
        loop,
    )
    assert world.factions[42].amount == 25
    assert loop.journal.flags["Coalition of Tradefolk"] == 25
    blank = World()
    blank.faction_names = {"coalition of tradefolk": 42}
    blank.factions = {42: Faction()}
    messages.MessagesHandler().handle("OP_SimpleMessage", simple(470, "Coalition of Tradefolk"), blank, Loop())
    assert blank.factions[42].changed is True
    assert blank.factions[42].amount is None
    messages.MessagesHandler().handle("OP_SimpleMessage", simple(471, "Coalition of Tradefolk"), world, loop)
    assert world.factions[42].maxed == 1
    assert world.factions[42].changed is False
    messages.MessagesHandler().handle("OP_SimpleMessage", simple(469, "Coalition of Tradefolk"), world, loop)
    assert world.factions[42].maxed == -1
    fresh = World(name="Hero")
    fresh.faction_names = {"unknown circle": 3}
    fresh.factions = {3: Faction(0)}
    journal = _Journal()
    journal.flags = {"Unknown Circle": 0}
    quiet = Loop()
    quiet.journal = journal
    messages.MessagesHandler().handle(
        "OP_ChannelMessage",
        channel("Guard", "Your faction standing with Unknown Circle has been adjusted by 2."),
        fresh,
        quiet,
    )
    assert fresh.factions[3].amount == 2
    assert journal.flags["Unknown Circle"] == 0
    assert quiet.queue == []
    messages.MessagesHandler().handle(
        "OP_ChannelMessage",
        channel("Hero", "Successfully added spell setting for Clericbot."),
        world,
        loop,
    )
    assert loop.journal.setting == ("Clericbot", "spells", "1")
    assert names(loop) == ["FetchFaction"]
