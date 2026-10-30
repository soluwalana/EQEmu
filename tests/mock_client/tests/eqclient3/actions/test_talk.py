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
        self.assertEqual(commands(client), ["hail orc"])
        self.assertEqual(action.waiting, ["HAIL"])
        action.step(client, sheet)
        self.assertEqual(commands(client), ["hail orc"])
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
        self.assertEqual(commands(client), ["hail Poxan"])
        self.assertFalse(action.complete)
        for _ in range(3):
            action.step(client, sheet)
        self.assertTrue(action.complete)
        self.assertEqual(commands(client), ["hail Poxan"])

    def test_a_hail_names_the_target(self):
        from eqclient3.actions.talk import hail_line

        self.assertEqual(hail_line("hail", "Prathun Stumblebum"), "hail Prathun Stumblebum")
        self.assertEqual(hail_line("hail", "Prathun_Stumblebum"), "hail Prathun Stumblebum")
        self.assertEqual(hail_line("blessed", "Rytan"), "blessed")
        client, sheet = fresh()
        mob(sheet, 5, distance=5, name="Prathun_Stumblebum", targeted=True)
        action = Talk(5, "hail", "Hail Prathun and Learn About Communication.")
        action.step(client, sheet)
        self.assertEqual(commands(client), ["hail Prathun Stumblebum"])

    def test_a_hail_says_the_link_then_reads_the_next_reply(self):
        client, sheet = fresh("tutorialb")
        mob(sheet, 4, distance=5, name="Rytan", targeted=True)
        action = Talk(4, "hail", "Hail Rytan and Learn About Spells.")
        action.step(client, sheet)
        self.assertEqual(commands(client), ["hail Rytan"])
        inbox(action, "OP_SpecialMesg", {"sender": "Rytan", "text": f"Would you like to be {_saylink('blessed')}?"})
        action.step(client, sheet)
        self.assertEqual(commands(client), ["hail Rytan", "blessed"])
        self.assertFalse(action.complete)
        inbox(action, "OP_SpecialMesg", {"sender": "Rytan", "text": "There you go."})
        action.step(client, sheet)
        self.assertEqual(commands(client), ["hail Rytan", "blessed"])
        self.assertTrue(action.complete)

    def test_the_next_link_is_said_when_the_step_stays_open(self):
        client, sheet = fresh("tutorialb")
        mob(sheet, 4, distance=5, name="Guide", targeted=True)
        action = Talk(4, "hail", "Hail Guide and Learn About Spells.")
        action.step(client, sheet)
        inbox(action, "OP_SpecialMesg", {"sender": "Guide", "text": f"Be {_saylink('blessed')} or {_saylink('review')}."})
        action.step(client, sheet)
        self.assertEqual(commands(client), ["hail Guide", "blessed"])
        inbox(action, "OP_SpecialMesg", {"sender": "Guide", "text": "Again."})
        action.step(client, sheet)
        self.assertEqual(commands(client), ["hail Guide", "blessed", "review"])
        self.assertFalse(action.complete)
        inbox(action, "OP_SpecialMesg", {"sender": "Guide", "text": "Done."})
        action.step(client, sheet)
        self.assertTrue(action.complete)
        self.assertEqual(commands(client), ["hail Guide", "blessed", "review"])

    def test_a_finished_step_drops_the_other_link(self):
        from types import SimpleNamespace
        from eqclient3.handlers.tasks import Activity

        client, sheet = fresh("tutorialb")
        mob(sheet, 4, distance=5, name="Rytan", targeted=True)
        step = Activity(1448, 5, 4, "Rytan", "", "Hail Rytan and Learn About Spells.", 1)
        sheet.tasks = SimpleNamespace(activities=[step])
        action = Talk(4, "hail", "Hail Rytan and Learn About Spells.")
        action.step(client, sheet)
        inbox(action, "OP_SpecialMesg", {"sender": "Rytan", "text": f"Be {_saylink('blessed')} or {_saylink('review')}?"})
        action.step(client, sheet)
        self.assertEqual(commands(client), ["hail Rytan", "blessed"])
        step.done = 1
        inbox(action, "OP_SpecialMesg", {"sender": "Rytan", "text": "There you go."})
        action.step(client, sheet)
        self.assertEqual(commands(client), ["hail Rytan", "blessed"])
        self.assertTrue(action.complete)

    def test_the_word_that_finishes_the_open_step_is_said_first(self):
        from eqclient3.actions.talk import reply_order

        ordered = reply_order(["review", "blessed"], {"blessed": {(1448, 5)}}, {(1448, 5)}, set())
        self.assertEqual(ordered, ["blessed", "review"])
        self.assertEqual(reply_order(["wish"], {}, set(), {"wish"}), [])

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
    body = "0FFFFF000080000000000000000000000000000000000"
    return f"\x12{body}{word}\x12"


if __name__ == "__main__":
    unittest.main()
