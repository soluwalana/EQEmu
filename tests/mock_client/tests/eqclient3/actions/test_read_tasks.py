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
        self.assertEqual(kinds(client).count("Kill"), 1)
        self.assertEqual(kinds(client).count("Fetch"), 1)
        self.assertEqual(kinds(client).count("Pickup"), 1)
        self.assertTrue(action.yielding)
        self.assertFalse(action.complete)
        self.assertFalse(client.journal.tutorial_done("Hero"))
        action.yielding = False
        action.step(client, sheet)
        self.assertFalse(action.complete)
        self.assertFalse(client.journal.tutorial_done("Hero"))

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
