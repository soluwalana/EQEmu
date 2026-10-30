"""Form sends its command list. bots/form.py builds that list."""

import unittest

from harness import commands, fresh

from eqclient3.actions.bots.form import Form
from eqclient3.bots.form import form_commands


class FormTest(unittest.TestCase):
    def test_each_command_once_then_complete(self):
        client, sheet = fresh()
        action = Form("qeynos", ["^botspawn a", "groupinvite a"])
        self.assertNotIn("OP_Assist", action.opcodes())
        action.step(client, sheet)
        action.step(client, sheet)
        action.step(client, sheet)
        self.assertEqual(commands(client), ["^botspawn a", "groupinvite a"])
        self.assertTrue(action.complete)

    def test_command_list_skips_saved_settings_and_never_taunts(self):
        cmds = form_commands(
            [("war", 1), ("clr", 2)],
            {},
            healer="clr",
            heal_target="Hero",
            members=("war", "clr"),
            spell_lines={"clr": ["^spellsettings load byname clr"]},
        )
        self.assertIn("^botcreate war 1 1 0", cmds)
        self.assertIn("^botspawn war", cmds)
        self.assertIn("groupinvite war", cmds)
        self.assertTrue(any(line.startswith("^botstance 5 byname war") for line in cmds))
        self.assertFalse(any(line.startswith("^taunt") for line in cmds))
        self.assertTrue(any(line.startswith("^healrotationcreate clr") for line in cmds))
        self.assertIn("^spellsettings load byname clr", cmds)
        saved = {
            "war": {"stance": "5", "sit": "90", "stop_melee": "1", "follow": "10", "spells": "1"},
            "clr": {"sit": "1", "stop_melee": "1", "follow": "1", "spells": "1", "heal": "1"},
        }
        quiet = form_commands([("war", 1), ("clr", 2)], saved, healer="clr", rotation_saved=False)
        self.assertFalse(any("botstance" in line for line in quiet))
        self.assertFalse(any("sitmana" in line for line in quiet))
        self.assertFalse(any("healrotation" in line for line in quiet))
        self.assertFalse(any(line.startswith("^taunt") for line in quiet))


if __name__ == "__main__":
    unittest.main()
