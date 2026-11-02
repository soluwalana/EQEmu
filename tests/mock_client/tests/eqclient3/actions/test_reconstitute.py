"""Reconstitute lists bots, respawns the dead, then rests. A second one inside 20 ticks is a no-op."""

import struct
import unittest

from harness import commands, fresh, inbox, kinds, mob, opcodes

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
        inbox(action, "OP_ChannelMessage", {"text": "Cleric saved."})
        mob(sheet, 4, distance=1, name="Cleric", targeted=False)
        action.step(client, sheet)
        self.assertTrue(sheet.bots.roster[0].alive)
        self.assertEqual(opcodes(client)[-2:], ["OP_TargetMouse", "OP_Consider"])
        inbox(
            action,
            "OP_Consider",
            struct.pack("<IIIIIIBBBB", 0, 4, 0, 0, 0, 0, 0, 0, 0, 0),
        )
        action.step(client, sheet)
        self.assertTrue(sheet.mobs[4].targeted)
        self.assertEqual(commands(client)[-1], "^healrotationlist Cleric")
        inbox(action, "OP_ChannelMessage", {"text": "Cleric -> Hero"})
        action.step(client, sheet)
        self.assertEqual(sheet.bots.rotation, ["Cleric -> Hero"])
        self.assertIn("Rest", kinds(client))
        self.assertTrue(action.complete)

    def test_a_special_bot_list_is_the_reply(self):
        client, sheet = fresh()
        client.tick = 50
        action = Reconstitute(241)
        action.step(client, sheet)
        body = "0FFFFF" + ("0" * 50)
        link = "\x12" + body + "Entwar" + "\x12"
        inbox(
            action,
            "OP_SpecialMesg",
            {
                "message": (
                    f"Bot 1 | {link} is a Level 3 Male Human Warrior owned by You.\n"
                    "5 Of 5 bots shown, 5 are owned by you."
                )
            },
        )
        action.step(client, sheet)
        self.assertEqual(sheet.bots.roster[0].name, "Entwar")
        self.assertFalse(sheet.bots.roster[0].alive)
        self.assertEqual(commands(client), ["^botlist", "^botspawn Entwar"])

    def test_second_inside_20_ticks_sends_nothing(self):
        client, sheet = fresh()
        sheet.bots.reconstituted_at = 50
        client.tick = 60
        action = Reconstitute(241)
        action.step(client, sheet)
        self.assertTrue(action.complete)
        self.assertEqual(commands(client), [])
        self.assertIn("Rest", kinds(client))


if __name__ == "__main__":
    unittest.main()
