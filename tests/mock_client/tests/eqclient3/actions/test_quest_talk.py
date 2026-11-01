"""QuestTalk walks a conversation: a reply between says, a Trade once the mob is targeted."""

import unittest

from harness import commands, fresh, inbox, kinds, mob

from eqclient3.actions.quest_talk import (
    ExpectFaction,
    ExpectItem,
    ExpectMoney,
    Faction,
    Hand,
    Money,
    Need,
    QuestTalk,
    Receive,
    Say,
)


class QuestTalkTest(unittest.TestCase):
    def test_waits_for_a_reply_before_the_next_say(self) -> None:
        client, sheet = fresh()
        mob(sheet, 6, distance=5, name="Korbuk Brimblade", targeted=True)
        action = QuestTalk("korbuk brimblade", (Say("work"), Say("errands")))
        action.step(client, sheet)
        self.assertEqual(commands(client), ["work"])
        self.assertFalse(action.complete)
        action.step(client, sheet)
        self.assertEqual(commands(client), ["work"])
        self.assertFalse(action.complete)
        inbox(action, "OP_ChannelMessage", {"sender": "Korbuk Brimblade", "text": "Run a couple errands."})
        action.step(client, sheet)
        self.assertFalse(action.complete)
        action.step(client, sheet)
        self.assertEqual(commands(client), ["work", "errands"])
        self.assertFalse(action.complete)
        inbox(action, "OP_ChannelMessage", {"sender": "Korbuk Brimblade", "text": "Recover the plans."})
        action.step(client, sheet)
        self.assertTrue(action.complete)
        self.assertEqual(commands(client), ["work", "errands"])

    def test_a_reply_with_a_saylink_is_not_the_next_line(self) -> None:
        client, sheet = fresh()
        mob(sheet, 4, distance=5, name="Rilgor Plegnog", targeted=True)
        action = QuestTalk("rilgor plegnog", (Say("insidious"),), expect=ExpectItem(54303))
        action.step(client, sheet)
        self.assertEqual(commands(client), ["insidious"])
        inbox(
            action,
            "OP_ChannelMessage",
            {"sender": "Rilgor Plegnog", "text": "Say [supply] if you need another."},
        )
        action.step(client, sheet)
        self.assertFalse(action.complete)
        self.assertEqual(commands(client), ["insidious"])

    def test_the_expected_item_ends_the_conversation(self) -> None:
        client, sheet = fresh()
        mob(sheet, 6, distance=5, name="Kargek Redblade", targeted=True)
        action = QuestTalk("kargek redblade", (Say("favor"), Say("sword")), expect=ExpectItem(20673))
        action.step(client, sheet)
        sheet.bags[0] = 20673
        action.step(client, sheet)
        self.assertTrue(action.complete)
        self.assertEqual(commands(client), ["favor"])

    def test_a_hail_names_the_npc(self) -> None:
        client, sheet = fresh()
        mob(sheet, 6, distance=5, name="Korbuk Brimblade", targeted=True)
        action = QuestTalk("korbuk brimblade", (Say("hail"),))
        action.step(client, sheet)
        self.assertEqual(commands(client), ["Hail, Korbuk Brimblade"])

    def test_walks_closer_before_saying(self) -> None:
        client, sheet = fresh()
        body = mob(sheet, 6, distance=40, name="Kargek Redblade", targeted=True)
        body.distance = 40
        action = QuestTalk("kargek redblade", (Say("favor"),))
        action.step(client, sheet)
        self.assertEqual(commands(client), [])
        self.assertFalse(action.complete)

    def test_a_hand_spawns_a_trade_once_the_mob_is_targeted(self) -> None:
        client, sheet = fresh()
        mob(sheet, 6, distance=5, name="Kargek Redblade", targeted=True)
        sheet.bags[0] = 20674
        action = QuestTalk("kargek redblade", (Hand(20674),), expect=ExpectItem(18083))
        action.source = "quest:kargek"
        action.step(client, sheet)
        self.assertEqual(kinds(client), ["Trade"])
        self.assertEqual(client.queue.head().partner, 6)
        self.assertEqual(client.queue.head().item, 20674)
        self.assertTrue(action.yielding)
        self.assertFalse(action.complete)

    def test_a_hand_waits_until_the_mob_is_targeted(self) -> None:
        client, sheet = fresh()
        mob(sheet, 6, distance=5, name="Kargek Redblade", targeted=False)
        sheet.bags[0] = 20674
        action = QuestTalk("kargek redblade", (Hand(20674),), expect=ExpectItem(18083))
        action.step(client, sheet)
        self.assertEqual(kinds(client), [])
        self.assertFalse(action.complete)

    def test_a_need_spawns_a_fetch_before_the_hand_back(self) -> None:
        client, sheet = fresh()
        mob(sheet, 6, distance=5, name="Kargek Redblade", targeted=True)
        action = QuestTalk(
            "kargek redblade",
            (Say("favor"), Receive(20673), Need(20676), Hand(20673), Hand(20676), Receive(18083)),
            expect=ExpectItem(18083),
        )
        action.source = "quest:kargek"
        action.step(client, sheet)
        inbox(action, "OP_ChannelMessage", {"sender": "Kargek Redblade", "text": "Take this note."})
        sheet.bags[0] = 20673
        action.step(client, sheet)
        action.step(client, sheet)
        self.assertEqual(action.steps[action.cursor], Need(20676))
        action.step(client, sheet)
        self.assertEqual(kinds(client), ["Fetch"])
        self.assertEqual(client.queue.head().item_id, 20676)
        self.assertTrue(action.yielding)
        sheet.bags[1] = 20676
        action.step(client, sheet)
        self.assertEqual(action.steps[action.cursor], Hand(20673))

    def test_money_and_faction_are_steps_the_talk_waits_on(self) -> None:
        client, sheet = fresh()
        mob(sheet, 6, distance=5, name="Pandula Bubundu", targeted=True)
        sheet.set_coin(0, 0, 0, 0)
        sheet.faction(1770).amount = 50
        action = QuestTalk("pandula bubundu", (Money(platinum=1), Faction(1770, 10), Say("done")))
        action.step(client, sheet)
        self.assertFalse(action.complete)
        self.assertEqual(commands(client), [])
        sheet.set_coin(1, 0, 0, 0)
        action.step(client, sheet)
        self.assertEqual(action.steps[action.cursor], Faction(1770, 10))
        action.step(client, sheet)
        sheet.faction(1770).amount = 60
        action.step(client, sheet)
        action.step(client, sheet)
        self.assertEqual(commands(client), ["done"])

    def test_money_ends_it_once_the_coin_arrives(self) -> None:
        client, sheet = fresh()
        mob(sheet, 6, distance=5, name="A Guard", targeted=True)
        sheet.set_coin(1, 0, 0, 0)
        action = QuestTalk("a guard", (Say("hail"),), expect=ExpectMoney(platinum=5))
        action.step(client, sheet)
        self.assertFalse(action.complete)
        sheet.set_coin(6, 0, 0, 0)
        action.step(client, sheet)
        self.assertTrue(action.complete)
        self.assertEqual(commands(client), ["Hail, A Guard"])

    def test_faction_standing_ends_it(self) -> None:
        client, sheet = fresh()
        mob(sheet, 6, distance=5, name="Pandula Bubundu", targeted=True)
        sheet.faction(1770).amount = 100
        action = QuestTalk("pandula bubundu", (Hand(52179),), expect=ExpectFaction(1770, 10))
        action.step(client, sheet)
        self.assertFalse(action.complete)
        sheet.faction(1770).amount = 110
        action.step(client, sheet)
        self.assertTrue(action.complete)


if __name__ == "__main__":
    unittest.main()
