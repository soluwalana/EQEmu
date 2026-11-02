"""ReadTasks appends open tutorial steps and writes the done mark on the way out."""

import struct
import unittest
from types import SimpleNamespace

from harness import fresh, inbox, kinds, place

from eqclient3.actions.read_tasks import ReadTasks
from eqclient3.handlers.tasks import Activity
from eqclient3.structs import OP_ChannelMessage


def book():
    hail = Activity(0, 1, 4, "", "", "hail the guard", 1)
    hail.npc = 3
    kill = Activity(0, 2, 2, "", "", "kill", 1)
    kill.spawn_id = 9
    loot = Activity(0, 3, 3, "", "", "loot", 2)
    loot.item_id = 12
    ground = Activity(0, 4, 0, "", "", "", 1)
    ground.ground = True
    ground.drop_id = 6
    ground.point = (1.0, 0.0, 0.0)
    locked = Activity(0, 5, 4, "", "", "locked", 1, locked=True)
    locked.npc = 1
    return SimpleNamespace(activities=[hail, kill, loot, ground, locked])


class ReadTasksTest(unittest.TestCase):
    def test_appends_open_steps_and_stays_in_the_mine(self):
        client, sheet = fresh("tutorialb")
        sheet.task_book = book()
        action = ReadTasks()
        place(client, action, "tutorialb", "read_tasks:tutorialb")
        self.assertTrue(action.durable)
        self.assertEqual(action.priority, 0)
        self.assertNotIn("OP_Assist", action.opcodes())
        action.step(client, sheet)
        self.assertEqual(kinds(client).count("Talk"), 1)
        self.assertEqual(kinds(client).count("Kill"), 0)
        self.assertTrue(action.yielding)
        self.assertFalse(action.complete)
        self.assertFalse(client.journal.tutorial_done("Hero"))
        action.yielding = False
        for item in list(client.queue):
            if type(item).__name__ == "Talk":
                client.queue.remove(item.insert)
                client.journal.resolve_action("Hero", item)
        action.step(client, sheet)
        self.assertEqual(kinds(client).count("Talk"), 1)
        self.assertEqual(kinds(client).count("Kill"), 0)
        self.assertFalse(client.journal.is_resolved("Hero", "task:0:1"))
        self.assertFalse(action.complete)
        self.assertFalse(client.journal.tutorial_done("Hero"))

    def test_a_deliver_with_no_item_fetches_what_the_npc_receives(self):
        from unittest.mock import patch

        client, sheet = fresh("tutorialb")
        step = Activity(1448, 3, 1, "Xenaida", "", "Hail Xenaida and Learn About Maps.", 1)
        sheet.task_book = SimpleNamespace(activities=[step])
        action = ReadTasks()
        place(client, action, "tutorialb", "read_tasks:tutorialb")
        with patch("eqclient3.actions.read_tasks._receipts_for", return_value=(59955,)):
            action.step(client, sheet)
        fetches = [row for row in client.queue if type(row).__name__ == "Fetch"]
        self.assertEqual(len(fetches), 1)
        self.assertEqual(fetches[0].item_id, 59955)

    def test_a_hail_fetches_the_one_item_the_npc_receives(self):
        from unittest.mock import patch

        client, sheet = fresh("tutorialb")
        step = Activity(1448, 6, 4, "Poxan", "", "Hail Poxan and Learn about Swimming", 1)
        sheet.task_book = SimpleNamespace(activities=[step])
        action = ReadTasks()
        place(client, action, "tutorialb", "read_tasks:tutorialb")
        with patch("eqclient3.actions.read_tasks._receipts_for", return_value=(59968,)):
            action.step(client, sheet)
        fetches = [row for row in client.queue if type(row).__name__ == "Fetch"]
        self.assertEqual([row.item_id for row in fetches], [59968])

    def test_an_open_find_hunt_drops_the_book_under_it(self):
        from eqclient3.actions.kill import Kill
        from eqclient3.actions.talk import Talk

        client, sheet = fresh("tutorialb")
        sheet.task_book = book()
        action = ReadTasks()
        place(client, action, "tutorialb", "read_tasks:tutorialb")
        talk = Talk(3, "hail", "hail the guard")
        talk.source = "task:0:1"
        talk.priority = -2
        client.queue.append(talk, sheet, client.journal, client.character)
        hunt = Kill(camp="Gloom Spiders")
        hunt.source = "find:gloomingdeep silk"
        hunt.priority = -1
        client.queue.append(hunt, sheet, client.journal, client.character)
        action.step(client, sheet)
        self.assertEqual(action.priority, -2)
        self.assertTrue(action.yielding)
        hunt.complete = True
        action.yielding = False
        action.step(client, sheet)
        self.assertEqual(action.priority, 0)
        self.assertEqual(talk.priority, 0)

    def test_empty_book_in_the_mine_does_not_complete(self):
        client, sheet = fresh("tutorialb")
        sheet.task_book = SimpleNamespace(activities=[])
        action = ReadTasks()
        place(client, action, "tutorialb", "read_tasks:tutorialb")
        action.step(client, sheet)
        self.assertFalse(action.complete)
        self.assertFalse(client.journal.tutorial_done("Hero"))

    def test_new_zone_out_writes_the_done_mark(self):
        client, sheet = fresh("tutorialb")
        sheet.task_book = book()
        action = ReadTasks()
        place(client, action, "tutorialb", "read_tasks:tutorialb")
        inbox(action, "OP_NewZone", {"zone": "freportw"})
        action.step(client, sheet)
        self.assertTrue(action.complete)
        self.assertTrue(client.journal.tutorial_done("Hero"))

    def test_a_named_line_appends_while_waiting_in_the_mine(self):
        client, sheet = fresh("tutorialb")
        action = ReadTasks()
        place(client, action, "tutorialb", "read_tasks:tutorialb")
        inbox(action, "OP_ChannelMessage", _channel("Guard", "kill the bat"))
        inbox(action, "OP_ChannelMessage", _channel("Guard", "hello there"))
        inbox(action, "OP_SimpleMessage", _simple(0, "open the door"))
        inbox(action, "OP_SimpleMessage", _simple(0, "hail the guard"))
        action.step(client, sheet)
        kills = [item for item in client.queue if type(item).__name__ == "Kill"]
        talks = [item for item in client.queue if type(item).__name__ == "Talk"]
        self.assertEqual(len(kills), 1)
        self.assertEqual(kills[0].camp, "bat")
        self.assertEqual(kills[0].source, "chat:kill:bat")
        self.assertEqual(len(talks), 1)
        self.assertEqual(talks[0].line, "guard")
        self.assertEqual(talks[0].source, "chat:talk:guard")
        self.assertFalse(action.complete)

    def test_activity_zero_keeps_its_task_id(self):
        client, sheet = fresh("tutorialb")
        hail = Activity(1448, 0, 4, "Arias", "", "Hail Arias and Learn About the Find Path.", 1)
        hail.npc = 3
        sheet.task_book = SimpleNamespace(activities=[hail])
        action = ReadTasks()
        place(client, action, "tutorialb", "read_tasks:tutorialb")
        action.step(client, sheet)
        talks = [item for item in client.queue if type(item).__name__ == "Talk"]
        self.assertEqual(len(talks), 1)
        self.assertEqual(talks[0].source, "task:1448:0")

    def test_a_special_line_appends_while_waiting_in_the_mine(self):
        client, sheet = fresh("tutorialb")
        action = ReadTasks()
        place(client, action, "tutorialb", "read_tasks:tutorialb")
        inbox(action, "OP_SpecialMesg", {"text": "kill the bat"})
        action.step(client, sheet)
        kills = [item for item in client.queue if type(item).__name__ == "Kill"]
        self.assertEqual(len(kills), 1)
        self.assertEqual(kills[0].camp, "bat")
        self.assertEqual(kills[0].source, "chat:kill:bat")

    def test_our_own_hail_is_not_a_new_step(self):
        client, sheet = fresh("tutorialb")
        action = ReadTasks()
        place(client, action, "tutorialb", "read_tasks:tutorialb")
        inbox(action, "OP_ChannelMessage", _channel("Hero", "Hail, Guard Rahtiz"))
        action.step(client, sheet)
        self.assertFalse(any(str(item.source).startswith("chat:") for item in client.queue))
        self.assertEqual(
            [item.source for item in client.queue if type(item).__name__ == "Talk"],
            ["hail:hobart"],
        )

    def test_a_saylink_is_not_a_new_step(self):
        client, sheet = fresh("tutorialb")
        action = ReadTasks()
        place(client, action, "tutorialb", "read_tasks:tutorialb")
        body = "0FFFFF000080000000000000000000000000000000000" + "0" * 11
        inbox(
            action,
            "OP_SpecialMesg",
            {"text": f"Would you like to be \x12{body}blessed\x12?"},
        )
        action.step(client, sheet)
        self.assertFalse(any(str(item.source).startswith("chat:") for item in client.queue))
        self.assertEqual(
            [item.source for item in client.queue if type(item).__name__ == "Talk"],
            ["hail:hobart"],
        )

    def test_say_before_a_link_is_not_a_new_step(self):
        client, sheet = fresh("tutorialb")
        action = ReadTasks()
        place(client, action, "tutorialb", "read_tasks:tutorialb")
        body = "0FFFFF00066000000000000000000000000000000000000000000000"
        inbox(
            action,
            "OP_ChannelMessage",
            _channel("Rashere", f"just say [\x12{body}bind my soul\x12]."),
        )
        action.step(client, sheet)
        self.assertFalse(any(str(item.source).startswith("chat:") for item in client.queue))
        self.assertEqual(
            [item.source for item in client.queue if type(item).__name__ == "Talk"],
            ["hail:hobart"],
        )

    def test_a_full_cursor_is_filed_instead_of_fetched(self):
        client, sheet = fresh("tutorialb")
        sheet.cursor = 9990
        action = ReadTasks()
        place(client, action, "tutorialb", "read_tasks:tutorialb")
        inbox(
            action,
            "OP_SpecialMesg",
            {"text": "You may not loot an item while you have an item on your cursor."},
        )
        action.step(client, sheet)
        self.assertFalse(any(str(item.source).startswith("chat:") for item in client.queue))
        moves = [item for item in client.queue if type(item).__name__ == "Cursor"]
        self.assertEqual(len(moves), 1)
        self.assertEqual(moves[0].move, (30, 22))

    def test_a_named_line_outside_the_mine_appends_nothing(self):
        client, sheet = fresh("qeynos")
        action = ReadTasks()
        place(client, action, "qeynos", "read_tasks:tutorialb")
        inbox(action, "OP_ChannelMessage", _channel("Guard", "kill the bat"))
        inbox(action, "OP_SimpleMessage", _simple(0, "hail the guard"))
        action.step(client, sheet)
        self.assertTrue(action.complete)
        self.assertFalse(any(str(item.source).startswith("chat:") for item in client.queue))


def _channel(sender, text):
    return OP_ChannelMessage("", sender, text=text).serialize()


def _simple(string_id, *texts):
    packet = struct.pack("<III", int(string_id), 0, 0)
    for text in texts:
        packet += text.encode("latin1") + b"\x00"
    return packet


if __name__ == "__main__":
    unittest.main()
