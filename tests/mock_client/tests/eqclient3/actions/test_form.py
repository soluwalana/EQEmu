"""Form builds the group from the party size, creates a missing bot, then invites."""

import unittest

from harness import commands, fresh, inbox, mob

from eqclient3.actions.bots.form import Form
from eqclient3.bots.form import form_commands
from eqclient3.structs import OP_GroupInvite


class FormTest(unittest.TestCase):
    def test_a_missing_bot_is_created_then_spawned_and_invited(self):
        client, sheet = fresh()
        action = Form("qeynos", 2)
        self.assertNotIn("OP_Assist", action.opcodes())
        action.step(client, sheet)
        self.assertEqual([name for name, _class_id in action.roster], ["Herwar"])
        self.assertEqual(commands(client), ["^botspawn Herwar"])
        self.assertFalse(action.complete)
        inbox(action, "OP_ChannelMessage", {"text": "You don't own a bot named 'Herwar'."})
        action.step(client, sheet)
        self.assertEqual(commands(client), ["^botspawn Herwar", "^botcreate Herwar 1 1 0"])
        inbox(action, "OP_ChannelMessage", {"text": "Bot Created | Name: Herwar ID: 4 Race: Human Class: Warrior"})
        action.step(client, sheet)
        self.assertEqual(commands(client)[-1], "^botspawn Herwar")
        self.assertEqual(client.journal.bots("Hero"), [("Herwar", 1)])
        inbox(action, "OP_ChannelMessage", {"text": "I am ready to fight!"})
        action.step(client, sheet)
        invites = [
            OP_GroupInvite.deserialize(payload) for opcode, payload in client.outbound if opcode == "OP_GroupInvite"
        ]
        self.assertEqual([(row.invitee, row.inviter) for row in invites], [("Herwar", "Hero")])
        self.assertEqual([bot.name for bot in sheet.bots.roster], ["Herwar"])
        for _ in range(10):
            action.step(client, sheet)
            self.assertNotIn("^follow reset spawned", commands(client))
        action.step(client, sheet)
        self.assertEqual(commands(client)[-1], "^follow reset spawned")
        inbox(action, "OP_SpecialMesg", {"text": "1 of your bots are following you."})
        action.step(client, sheet)
        self.assertTrue(action.complete)

    def test_a_failed_spawn_means_the_bot_is_not_owned(self):
        client, sheet = fresh()
        action = Form("qeynos", 2)
        action.step(client, sheet)
        inbox(action, "OP_ChannelMessage", {"text": "Failed to spawn 'Herwar' (ID 44)"})
        action.step(client, sheet)
        self.assertEqual(commands(client), ["^botspawn Herwar", "^botcreate Herwar 1 1 0"])
        self.assertFalse(action.complete)

    def test_an_existing_bot_is_spawned_without_a_create(self):
        client, sheet = fresh()
        mob(sheet, 12, distance=5, name="Herwar", targeted=False)
        action = Form("qeynos", 2)
        action.step(client, sheet)
        inbox(action, "OP_ChannelMessage", {"text": "'Herwar' is already spawned."})
        action.step(client, sheet)
        self.assertEqual(commands(client), ["^botspawn Herwar"])
        self.assertIn("OP_TargetMouse", [opcode for opcode, _payload in client.outbound])
        invites = [
            OP_GroupInvite.deserialize(payload) for opcode, payload in client.outbound if opcode == "OP_GroupInvite"
        ]
        self.assertEqual(invites[0].invitee, "Herwar")
        for _ in range(10):
            action.step(client, sheet)
        action.step(client, sheet)
        self.assertEqual(commands(client)[-1], "^follow reset spawned")
        inbox(action, "OP_SpecialMesg", {"text": "1 of your bots are following you."})
        action.step(client, sheet)
        self.assertTrue(action.complete)

    def test_a_bot_missing_from_the_group_is_invited_again(self):
        client, sheet = fresh()
        action = Form("qeynos", 3)
        action.built = True
        action.roster = [("Herwar", 1), ("Herclr", 2)]
        action.spawned = ["Herwar", "Herclr"]
        action.phase = "invite"
        action.index = 2
        sheet.group.members = ["Hero", "Herwar"]
        for _ in range(10):
            action.step(client, sheet)
        action.step(client, sheet)
        invites = [
            OP_GroupInvite.deserialize(payload) for opcode, payload in client.outbound if opcode == "OP_GroupInvite"
        ]
        self.assertEqual(invites[-1].invitee, "Herclr")
        self.assertNotIn("^follow reset spawned", commands(client))
        sheet.group.members.append("Herclr")
        action.step(client, sheet)
        self.assertEqual(commands(client)[-1], "^follow reset spawned")

    def test_six_members_uses_the_group_template(self):
        client, sheet = fresh()
        action = Form("qeynos")
        action.step(client, sheet)
        self.assertEqual(
            [name for name, _class_id in action.roster],
            ["Herwar", "Herclr", "Hermag", "Herwiz", "Hermnk"],
        )
        self.assertEqual(commands(client), ["^botspawn Herwar"])

    def test_extra_groups_use_the_other_classes_and_end_on_a_dps(self):
        client, sheet = fresh()
        action = Form("qeynos", 15)
        action.step(client, sheet)
        names = [name for name, _class_id in action.roster]
        self.assertEqual(names[:5], ["Herwar", "Herclr", "Hermag", "Herwiz", "Hermnk"])
        self.assertEqual(names[5:11], ["Herpal", "Herdru", "Herrng", "Herbrd", "Herrog", "Hernec"])
        self.assertEqual(names[11:], ["Hershd", "Hershm", "Herenc"])

    def test_classes_a_human_cannot_be_use_a_race_guards_leave_alone(self):
        client, sheet = fresh()
        action = Form("qeynos", 24)
        action.step(client, sheet)
        expect = {
            5: "^botcreate Hershd 5 3 0",
            10: "^botcreate Hershm 10 330 0",
            16: "^botcreate Herber 16 8 0",
        }
        for class_id, command in expect.items():
            action.phase = "create"
            action.pending = ""
            action.index = next(index for index, (_name, found) in enumerate(action.roster) if found == class_id)
            action.step(client, sheet)
            self.assertEqual(commands(client)[-1], command)

    def test_a_saved_bot_keeps_its_name(self):
        client, sheet = fresh()
        client.journal.remember_bot("Hero", "Oldtank", 1)
        action = Form("qeynos", 2)
        action.step(client, sheet)
        self.assertEqual(commands(client), ["^botspawn Oldtank"])

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
            "war": {
                "stance": "5",
                "sit": "90",
                "stop_melee": "1",
                "follow": "10",
                "spells": "1",
            },
            "clr": {
                "sit": "1",
                "stop_melee": "1",
                "follow": "1",
                "spells": "1",
                "heal": "1",
            },
        }
        quiet = form_commands([("war", 1), ("clr", 2)], saved, healer="clr", rotation_saved=False)
        self.assertFalse(any("botstance" in line for line in quiet))
        self.assertFalse(any("sitmana" in line for line in quiet))
        self.assertFalse(any("healrotation" in line for line in quiet))
        self.assertFalse(any(line.startswith("^taunt") for line in quiet))


if __name__ == "__main__":
    unittest.main()
