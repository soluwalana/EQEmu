"""QuestTalk walks a conversation: a reply between says, a Trade once the mob is targeted."""

import unittest

from harness import commands, fresh, inbox, kinds, mob

from eqclient3.actions.quest_talk import Hand, QuestTalk, Say


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
        action = QuestTalk("rilgor plegnog", (Say("insidious"),), expect=54303)
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
        action = QuestTalk("kargek redblade", (Say("favor"), Say("sword")), expect=20673)
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
        action = QuestTalk("kargek redblade", (Hand(20674),), expect=18083)
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
        action = QuestTalk("kargek redblade", (Hand(20674),), expect=18083)
        action.step(client, sheet)
        self.assertEqual(kinds(client), [])
        self.assertFalse(action.complete)


if __name__ == "__main__":
    unittest.main()
