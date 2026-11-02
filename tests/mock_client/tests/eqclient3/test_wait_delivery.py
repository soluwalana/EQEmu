"""The mailbox an action is waiting on actually receives the packet."""

from types import SimpleNamespace

from check_wait_delivery import gaps, pairs
from eqclient3.action import Message
from eqclient3.actions.sell import Sell
from eqclient3.actions.talk import Talk
from eqclient3.actions.trade import Trade
from eqclient3.handlers.tasks import Activity
from eqclient3.structs import OP_SimpleMessage
from eqclient3.world import World
from handlers.support import Loop
from harness import fresh


def test_wait_delivery_holds():
    assert gaps() == []
    found = set(pairs())
    needed = (
        ("Attack", "TARGET", "OP_Consider", "ConsiderHandler"),
        ("Talk", "TARGET", "OP_Consider", "ConsiderHandler"),
        ("Talk", "HAIL", "OP_ChannelMessage", "MessagesHandler"),
        ("Talk", "HAIL", "OP_SpecialMesg", "MessagesHandler"),
        ("Talk", "HAIL", "OP_SimpleMessage", "MessagesHandler"),
        ("Cursor", "CURSOR", "OP_ItemPacket", "ItemsHandler"),
        ("Cursor", "CURSOR", "OP_DeleteItem", "ItemsHandler"),
        ("Attack", "CAST", "OP_SimpleMessage", "MessagesHandler"),
        ("Heal", "HEAL", "OP_HPUpdate", "MobsHandler"),
        ("Cure", "CURE", "OP_Buff", "BuffsHandler"),
        ("ScribeSpell", "SCRIBE", "OP_MemorizeSpell", "ProfileHandler"),
        ("ScribeSpell", "SCRIBE", "OP_SpecialMesg", "MessagesHandler"),
        ("Train", "TRAIN", "OP_GMTrainSkill", "bus"),
        ("Train", "TRAIN", "OP_GMEndTraining", "bus"),
        ("Trade", "TRADE", "OP_FinishTrade", "bus"),
        ("Trade", "TRADE", "OP_SimpleMessage", "MessagesHandler"),
        ("LootMob", "LOOT", "OP_MoneyOnCorpse", "LootHandler"),
        ("Reclaim", "LOOT", "OP_ItemPacket", "ItemsHandler"),
        ("Zone", "ZONE", "OP_NewZone", "ZoningHandler"),
        ("Craft", "CRAFT", "OP_TradeSkillCombine", "bus"),
        ("Summon", "SUMMON", "OP_ChannelMessage", "MessagesHandler"),
        ("Summon", "SUMMON", "OP_SpecialMesg", "MessagesHandler"),
        ("Reconstitute", "BOT", "OP_ChannelMessage", "MessagesHandler"),
        ("movement", "DOOR", "OP_MoveDoor", "DoorsHandler"),
    )
    missing = [row for row in needed if row not in found]
    assert missing == []


def test_a_tutorial_ending_hail_appends_the_epic_graph():
    client, sheet = fresh("tutorialb")
    sheet.class_id = 1
    sheet.race = 1
    sheet.tasks = SimpleNamespace(activities=[Activity(1, 1, 4, "Guard", "", "hail the guard", 1, 0, False)])
    talk = Talk(1, "hail", "")
    talk.sent = True
    talk.satisfied = True
    talk.step(client, sheet)
    assert talk.complete is True
    assert any(str(action.source).startswith("goal:item=") for action in client.queue)


def test_a_hail_with_no_follow_up_completes():
    world = World(name="Hero", zone="qeynos")
    loop = Loop()
    loop.character = "Hero"
    talk = Talk(1, "Hail", "")
    talk.step(loop, world)
    assert talk.complete is False
    for _ in range(3):
        talk.step(loop, world)
    assert talk.complete is True
    assert talk.finishes_tutorial is False


def test_a_merchant_refusal_completes_the_buy():
    trade = Trade(8, 1001)
    trade.waiting = ["TRADE"]
    trade.requested = True
    trade.accepted = True
    trade.add_message(Message(OP_SimpleMessage(1154, texts=("Human",))))
    trade.step(Loop(), World())
    assert trade.complete is True


def test_a_merchant_refusal_completes_the_sale():
    sell = Sell([1001])
    sell.add_message(Message(OP_SimpleMessage(1154)))
    sell.step(Loop(), World())
    assert sell.complete is True
