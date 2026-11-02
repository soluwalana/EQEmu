"""Talk walks, hails once, and turns a standing 8 or 9 into a fight or a soulbind."""

import unittest
from types import SimpleNamespace

from harness import commands, fresh, inbox, kinds, mob, movement

from eqclient3.actions.fetch import Fetch
from eqclient3.actions.talk import Talk


class TalkTest(unittest.TestCase):
    def test_plans_sends_the_line_and_waits_on_task_text(self):
        client, sheet = fresh()
        body = mob(sheet, 3, distance=40, targeted=True)
        action = Talk(3, "hail", "the task", priority=280)
        self.assertEqual(action.priority, 280)
        self.assertIn("OP_Consider", action.opcodes())
        action.step(client, sheet)
        self.assertEqual(movement().advances[-1].mode, "run")
        self.assertEqual(commands(client), [])
        body.position = (5.0, 0.0, 0.0)
        action.active_path = None
        action.step(client, sheet)
        self.assertEqual(commands(client), ["Hail, orc"])
        self.assertEqual(action.waiting, ["HAIL"])
        action.step(client, sheet)
        self.assertEqual(commands(client), ["Hail, orc"])
        self.assertFalse(action.complete)
        sheet.follow_up = Fetch(12, 1, "the task")
        inbox(action, "OP_ChannelMessage", {"text": "You have the task now"})
        action.step(client, sheet)
        self.assertIn("Fetch", kinds(client))
        self.assertTrue(action.yielding)
        self.assertFalse(action.complete)

    def test_hostile_gap_appends_attack(self):
        client, sheet = fresh()
        mob(sheet, 3, distance=5, level=15, standing=8, targeted=True)
        action = Talk(3, "hail", "")
        action.step(client, sheet)
        attacks = [row for row in client.queue if type(row).__name__ == "Attack"]
        self.assertEqual(len(attacks), 1)
        self.assertEqual(attacks[0].spawn_id, 3)
        self.assertEqual(commands(client), [])

    def test_gap_over_10_appends_soulbind(self):
        client, sheet = fresh()
        sheet.soulbinder = SimpleNamespace(name="Soulbinder", zone="qeynos", x=1.0, y=2.0, z=3.0)
        mob(sheet, 3, distance=5, level=30, standing=9, targeted=True)
        action = Talk(3, "hail", "")
        action.step(client, sheet)
        talks = [row for row in client.queue if type(row).__name__ == "Talk"]
        self.assertEqual(len(talks), 1)
        self.assertEqual(talks[0].task_text, "soulbind")
        self.assertNotIn("Attack", kinds(client))

    def test_hail_objective_targets_the_named_npc_and_finishes(self):
        client, sheet = fresh()
        mob(sheet, 8, distance=5, name="Poxan", targeted=True)
        action = Talk(0, "hail", " Hail Poxan and Learn about Swimming")
        action.step(client, sheet)
        self.assertEqual(action.target_id, 8)
        self.assertEqual(commands(client), ["Hail, Poxan"])
        self.assertFalse(action.complete)
        for _ in range(3):
            action.step(client, sheet)
        self.assertTrue(action.complete)
        self.assertEqual(commands(client), ["Hail, Poxan"])

    def test_a_task_hail_stays_open_until_the_book_records_it(self):
        from eqclient3.handlers.tasks import Activity, Book

        client, sheet = fresh()
        mob(sheet, 8, distance=5, name="Poxan", targeted=True)
        book = Book()
        book.activities.append(Activity(1448, 6, 4, "Poxan", "", "Hail Poxan", 1, done=0))
        sheet.tasks = book
        action = Talk(0, "hail", " Hail Poxan and Learn about Swimming")
        action.source = "task:1448:6"
        action.step(client, sheet)
        for _ in range(3):
            action.step(client, sheet)
        self.assertFalse(action.complete)
        book.activities[0].done = 1
        action.step(client, sheet)
        self.assertTrue(action.complete)

    def test_an_open_task_says_a_link_that_was_already_said(self):
        from eqclient3.handlers.tasks import Activity, Book

        client, sheet = fresh()
        sheet.zone = "tutorialb"
        sheet.name = "Entoen"
        mob(sheet, 8, distance=5, name="Vahlara", targeted=True)
        book = Book()
        book.activities.append(Activity(1448, 2, 4, "Vahlara", "", "Hail Vahlara", 1, done=0))
        sheet.tasks = book
        action = Talk(8, "hail", "Hail Vahlara and Learn About Armor.")
        action.source = "task:1448:2"
        action.said.add("others")
        action.sent = True
        action.wait("HAIL")
        link = "\x12" + ("0FFFFF" + "0" * 50) + "others\x12"
        inbox(action, "OP_ChannelMessage", {"sender": "Vahlara", "text": f"many [{link}]"})
        action.step(client, sheet)
        self.assertEqual(commands(client), ["others"])
        self.assertFalse(action.complete)

    def test_a_hail_names_the_target(self):
        from eqclient3.actions.talk import hail_line

        self.assertEqual(hail_line("hail", "Prathun Stumblebum"), "Hail, Prathun Stumblebum")
        self.assertEqual(hail_line("hail", "Prathun_Stumblebum"), "Hail, Prathun Stumblebum")
        self.assertEqual(hail_line("blessed", "Rytan"), "blessed")
        client, sheet = fresh()
        mob(sheet, 5, distance=5, name="Prathun_Stumblebum", targeted=True)
        action = Talk(5, "hail", "Hail Prathun and Learn About Communication.")
        action.step(client, sheet)
        self.assertEqual(commands(client), ["Hail, Prathun Stumblebum"])

    def test_a_task_target_name_is_the_hail(self):
        client, sheet = fresh()
        body = mob(sheet, 9, distance=40, name="Guard_Rahtiz000", targeted=True)
        body.last_name = "Beginner Missions"
        action = Talk(0, "hail", "Guard Rahtiz")
        action.step(client, sheet)
        self.assertEqual(action.target_id, 9)
        self.assertEqual(commands(client), [])
        body.position = (5.0, 0.0, 0.0)
        action.active_path = None
        action.step(client, sheet)
        self.assertEqual(commands(client), ["Hail, Guard Rahtiz"])

    def test_a_hail_drops_the_unique_suffix_and_the_title(self):
        client, sheet = fresh()
        body = mob(sheet, 6, distance=5, name="Guard_Rahtiz000", targeted=True)
        body.last_name = "Beginner Missions"
        action = Talk(6, "hail", "")
        action.step(client, sheet)
        self.assertEqual(commands(client), ["Hail, Guard Rahtiz"])

    def test_an_outgoing_say_is_printed_when_it_is_sent(self):
        import io
        from contextlib import redirect_stderr
        from eqclient3.net.client import _print_say
        from eqclient3.structs import OP_ChannelMessage, SAY_CHANNEL

        payload = OP_ChannelMessage("", "Mockvthree", channel=SAY_CHANNEL, text="Hail, Guard Rahtiz").serialize()
        caught = io.StringIO()
        with redirect_stderr(caught):
            _print_say(payload, "Mockvthree")
        self.assertEqual(caught.getvalue(), "> Mockvthree: Hail, Guard Rahtiz\n")

    def test_find_silk_hunts_the_spiders(self):
        client, sheet = fresh()
        mob(sheet, 9, distance=5, name="Vahlara", targeted=True)
        action = Talk(9, "hail", "Hail Vahlara and Learn About Armor.")
        action.step(client, sheet)
        inbox(
            action,
            "OP_SimpleMessage",
            {
                "string_id": 1032,
                "texts": (
                    "Vahlara",
                    "If you can find any gloomingdeep silk, bring it to me and I can make more bandages.",
                ),
            },
        )
        action.step(client, sheet)
        hunts = [row for row in client.queue if type(row).__name__ == "Kill"]
        self.assertEqual(len(hunts), 1)
        self.assertEqual(hunts[0].camp, "Gloom Spiders")
        self.assertEqual(hunts[0].until_item, 54234)
        self.assertEqual(hunts[0].until_count, 1)
        self.assertEqual(hunts[0].source, "find:gloomingdeep silk")
        self.assertEqual(hunts[0].priority, -1)
        self.assertFalse(any(type(row).__name__ == "Fetch" for row in client.queue))
        self.assertEqual(commands(client), ["Hail, Vahlara"])

    def test_an_open_silk_hunt_is_given_the_turn(self):
        from eqclient3.actions.kill import Kill

        client, sheet = fresh()
        mob(sheet, 9, distance=5, name="Vahlara", targeted=True)
        hunt = Kill(camp="Gloom Spiders")
        hunt.source = "find:gloomingdeep silk"
        client.queue.append(hunt, sheet, client.journal, client.character)
        action = Talk(9, "hail", "Hail Vahlara and Learn About Armor.")
        action.source = "task:1448:2"
        action.step(client, sheet)
        inbox(
            action,
            "OP_SimpleMessage",
            {
                "string_id": 1032,
                "texts": (
                    "Vahlara",
                    "If you can find any gloomingdeep silk, bring it to me and I can make more bandages.",
                ),
            },
        )
        action.step(client, sheet)
        self.assertTrue(action.yielding)
        self.assertEqual(action.priority, -2)
        self.assertEqual(
            [row.source for row in client.queue if type(row).__name__ == "Kill"],
            ["find:gloomingdeep silk"],
        )

    def test_silk_already_held_is_handed_to_vahlara(self):
        client, sheet = fresh()
        mob(sheet, 9, distance=5, name="Vahlara", targeted=True)
        sheet.bags[22] = 54234
        action = Talk(9, "hail", "Hail Vahlara and Learn About Armor.")
        action.step(client, sheet)
        inbox(
            action,
            "OP_SimpleMessage",
            {
                "string_id": 1032,
                "texts": (
                    "Vahlara",
                    "If you can find any gloomingdeep silk, bring it to me and I can make more bandages.",
                ),
            },
        )
        action.step(client, sheet)
        hands = [row for row in client.queue if type(row).__name__ == "Trade"]
        self.assertEqual(len(hands), 1)
        self.assertEqual(hands[0].item, 54234)
        self.assertEqual(hands[0].partner, 9)
        self.assertFalse(any(type(row).__name__ == "Kill" for row in client.queue))

    def test_a_finished_silk_hunt_hands_the_silk(self):
        client, sheet = fresh()
        mob(sheet, 9, distance=5, name="Vahlara", targeted=True)
        action = Talk(9, "hail", "Hail Vahlara and Learn About Armor.")
        action.source = "task:1448:2"
        action.step(client, sheet)
        action.sought = True
        action.priority = -2
        action.expect_reply = False
        sheet.bags[22] = 54234
        action.step(client, sheet)
        hands = [row for row in client.queue if type(row).__name__ == "Trade"]
        self.assertEqual(len(hands), 1)
        self.assertEqual(hands[0].item, 54234)
        self.assertEqual(action.priority, 0)

    def test_find_a_person_queues_a_hail(self):
        client, sheet = fresh()
        mob(sheet, 4, distance=5, name="Vahlara", targeted=True)
        mob(sheet, 8, distance=5, name="Xenaida", targeted=True)
        action = Talk(4, "hail", "Hail Vahlara and Learn About Armor.")
        action.step(client, sheet)
        inbox(
            action,
            "OP_SimpleMessage",
            {"string_id": 1032, "texts": ("Vahlara", "Find Xenaida and learn about maps.")},
        )
        action.step(client, sheet)
        talks = [row for row in client.queue if type(row).__name__ == "Talk"]
        self.assertEqual(len(talks), 1)
        self.assertEqual(talks[0].bind_name, "Xenaida")
        self.assertEqual(talks[0].target_id, 8)
        self.assertEqual(talks[0].source, "find:xenaida")
        talks[0].step(client, sheet)
        self.assertEqual(commands(client), ["Hail, Vahlara", "Hail, Xenaida"])
        inbox(
            talks[0],
            "OP_SimpleMessage",
            {"string_id": 1032, "texts": ("Xenaida", f"Let me show you the {_saylink('maps')}.")},
        )
        talks[0].step(client, sheet)
        self.assertEqual(commands(client), ["Hail, Vahlara", "Hail, Xenaida", "maps"])
        self.assertFalse(talks[0].complete)

    def test_an_item_link_is_not_a_quest_link(self):
        client, sheet = fresh()
        mob(sheet, 9, distance=5, name="Vahlara", targeted=True)
        action = Talk(9, "hail", "Hail Vahlara and Learn About Armor.")
        action.step(client, sheet)
        inbox(
            action,
            "OP_SimpleMessage",
            {
                "string_id": 1032,
                "texts": (
                    "Vahlara",
                    f"Take these {_item_link('Gloomingdeep Kobold Plate Vambraces')}. "
                    f"There are many {_saylink('others')} who were not as lucky.",
                ),
            },
        )
        action.step(client, sheet)
        self.assertEqual(commands(client), ["Hail, Vahlara", "others"])

    def test_his_message_answers_the_hail(self):
        client, sheet = fresh()
        mob(sheet, 9, distance=5, name="Guard_Rahtiz000", targeted=True)
        action = Talk(9, "hail", "Guard Rahtiz")
        action.step(client, sheet)
        self.assertEqual(commands(client), ["Hail, Guard Rahtiz"])
        self.assertEqual(action.waiting, ["HAIL"])
        inbox(
            action,
            "OP_SimpleMessage",
            {
                "string_id": 1032,
                "texts": (
                    "Guard Rahtiz",
                    "Greetings, Mockvthree. We're glad you found your way to our camp.",
                ),
            },
        )
        action.step(client, sheet)
        self.assertEqual(commands(client), ["Hail, Guard Rahtiz"])
        self.assertTrue(action.complete)
        self.assertFalse(action.waiting)

    def test_a_saylink_in_his_message_is_said(self):
        client, sheet = fresh("tutorialb")
        mob(sheet, 4, distance=5, name="Rytan", targeted=True)
        action = Talk(4, "hail", "Hail Rytan and Learn About Spells.")
        action.step(client, sheet)
        inbox(
            action,
            "OP_SimpleMessage",
            {
                "string_id": 1032,
                "texts": ("Rytan", f"Would you like to be {_saylink('blessed')}?"),
            },
        )
        action.step(client, sheet)
        self.assertEqual(commands(client), ["Hail, Rytan", "blessed"])
        self.assertFalse(action.complete)

    def test_a_hail_says_the_link_then_reads_the_next_reply(self):
        client, sheet = fresh("tutorialb")
        mob(sheet, 4, distance=5, name="Rytan", targeted=True)
        action = Talk(4, "hail", "Hail Rytan and Learn About Spells.")
        action.step(client, sheet)
        self.assertEqual(commands(client), ["Hail, Rytan"])
        inbox(
            action,
            "OP_SpecialMesg",
            {"sender": "Rytan", "text": f"Would you like to be {_saylink('blessed')}?"},
        )
        action.step(client, sheet)
        self.assertEqual(commands(client), ["Hail, Rytan", "blessed"])
        self.assertFalse(action.complete)
        inbox(action, "OP_SpecialMesg", {"sender": "Rytan", "text": "There you go."})
        action.step(client, sheet)
        self.assertEqual(commands(client), ["Hail, Rytan", "blessed"])
        self.assertTrue(action.complete)

    def test_the_next_link_is_said_when_the_step_stays_open(self):
        client, sheet = fresh("tutorialb")
        mob(sheet, 4, distance=5, name="Guide", targeted=True)
        action = Talk(4, "hail", "Hail Guide and Learn About Spells.")
        action.step(client, sheet)
        inbox(
            action,
            "OP_SpecialMesg",
            {
                "sender": "Guide",
                "text": f"Be {_saylink('blessed')} or {_saylink('review')}.",
            },
        )
        action.step(client, sheet)
        self.assertEqual(commands(client), ["Hail, Guide", "blessed"])
        inbox(action, "OP_SpecialMesg", {"sender": "Guide", "text": "Again."})
        action.step(client, sheet)
        self.assertEqual(commands(client), ["Hail, Guide", "blessed", "review"])
        self.assertFalse(action.complete)
        inbox(action, "OP_SpecialMesg", {"sender": "Guide", "text": "Done."})
        action.step(client, sheet)
        self.assertTrue(action.complete)
        self.assertEqual(commands(client), ["Hail, Guide", "blessed", "review"])

    def test_a_finished_step_drops_the_other_link(self):
        from types import SimpleNamespace
        from eqclient3.handlers.tasks import Activity

        client, sheet = fresh("tutorialb")
        mob(sheet, 4, distance=5, name="Rytan", targeted=True)
        step = Activity(1448, 5, 4, "Rytan", "", "Hail Rytan and Learn About Spells.", 1)
        sheet.tasks = SimpleNamespace(activities=[step])
        action = Talk(4, "hail", "Hail Rytan and Learn About Spells.")
        action.step(client, sheet)
        inbox(
            action,
            "OP_SpecialMesg",
            {
                "sender": "Rytan",
                "text": f"Be {_saylink('blessed')} or {_saylink('review')}?",
            },
        )
        action.step(client, sheet)
        self.assertEqual(commands(client), ["Hail, Rytan", "blessed"])
        step.done = 1
        inbox(action, "OP_SpecialMesg", {"sender": "Rytan", "text": "There you go."})
        action.step(client, sheet)
        self.assertEqual(commands(client), ["Hail, Rytan", "blessed"])
        self.assertTrue(action.complete)

    def test_the_word_that_finishes_the_open_step_is_said_first(self):
        from eqclient3.actions.talk import reply_order

        ordered = reply_order(["review", "blessed"], {"blessed": {(1448, 5)}}, {(1448, 5)}, set())
        self.assertEqual(ordered, ["blessed", "review"])
        self.assertEqual(reply_order(["wish"], {}, set(), {"wish"}), [])
        self.assertEqual(reply_order(["wish"], {}, set(), {"wish"}, repeat=True), ["wish"])

    def test_reply_is_read_while_a_target_wait_is_open(self):
        client, sheet = fresh()
        mob(sheet, 3, distance=5, targeted=True)
        action = Talk(3, "hail", "the task")
        action.step(client, sheet)
        self.assertEqual(action.waiting, ["HAIL"])
        action.wait("TARGET")
        sheet.follow_up = Fetch(12, 1, "the task")
        inbox(action, "OP_ChannelMessage", {"text": "You have the task now"})
        action.step(client, sheet)
        self.assertNotIn("HAIL", action.waiting)
        self.assertIn("TARGET", action.waiting)
        self.assertIn("Fetch", kinds(client))

    def test_blank_hail_with_no_target_finishes(self):
        client, sheet = fresh()
        action = Talk(0, "hail", "")
        action.step(client, sheet)
        self.assertTrue(action.complete)
        self.assertEqual(commands(client), [])

    def test_string_124_shortens_the_stride(self):
        client, sheet = fresh()
        mob(sheet, 3, distance=40, targeted=True)
        action = Talk(3, "hail", "")
        inbox(action, "OP_SimpleMessage", {"string_id": 124})
        action.step(client, sheet)
        self.assertEqual(action.stride, "walk")
        self.assertEqual(movement().advances[-1].mode, "walk")


def _saylink(word):
    body = "0FFFFF000080000000000000000000000000000000000" + "0" * 11
    return f"\x12{body}{word}\x12"


def _item_link(name):
    body = "010620" + "0" * 50
    return f"\x12{body}{name}\x12"


if __name__ == "__main__":
    unittest.main()
