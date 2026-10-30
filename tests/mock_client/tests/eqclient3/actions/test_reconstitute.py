"""Reconstitute lists bots, respawns the dead, then rests. A second one inside 20 ticks is a no-op."""

import unittest

from harness import commands, fresh, inbox, kinds

from eqclient3.actions.bots.reconstitute import Reconstitute


class ReconstituteTest(unittest.TestCase):
    def test_list_spawn_rotation_then_rest(self):
        client, sheet = fresh()
        client.tick = 50
        action = Reconstitute(241)
        self.assertNotIn("OP_Assist", action.opcodes())
        action.step(client, sheet)
        self.assertEqual(commands(client), ["^botlist"])
        self.assertEqual(sheet.bots.reconstituted_at, 50)
        self.assertEqual(action.waiting, ["BOT"])
        inbox(
            action,
            "OP_ChannelMessage",
            {
                "text": "Cleric is a Level 1 Cleric and is dead",
                "bots": [{"name": "Cleric", "alive": False}],
            },
        )
        action.step(client, sheet)
        self.assertEqual(sheet.bots.roster[0].name, "Cleric")
        self.assertFalse(sheet.bots.roster[0].alive)
        self.assertEqual(commands(client)[-1], "^botspawn Cleric")
        inbox(action, "OP_ChannelMessage", {"text": "Cleric spawned"})
        action.step(client, sheet)
        self.assertTrue(sheet.bots.roster[0].alive)
        self.assertEqual(commands(client)[-1], "^healrotationlist")
        inbox(action, "OP_ChannelMessage", {"text": "Cleric -> Hero"})
        action.step(client, sheet)
        self.assertEqual(sheet.bots.rotation, ["Cleric -> Hero"])
        self.assertIn("Rest", kinds(client))
        self.assertTrue(action.complete)

    def test_second_inside_20_ticks_sends_nothing(self):
        client, sheet = fresh()
        sheet.bots.reconstituted_at = 50
        client.tick = 60
        action = Reconstitute(241)
        action.step(client, sheet)
        self.assertTrue(action.complete)
        self.assertEqual(commands(client), [])


if __name__ == "__main__":
    unittest.main()
