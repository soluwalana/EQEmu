"""Talk: walk, one line, task text, then the follow-up fetch."""

import unittest

from harness import commands, fresh, inbox, kinds, mob

from eqclient3.actions.fetch import Fetch
from eqclient3.actions.talk import Talk


class TalkSteps(unittest.TestCase):
    def test_walk_line_task_text_follow_up(self):
        client, sheet = fresh()
        body = mob(sheet, 3, distance=40, targeted=True)
        sheet.follow_up = Fetch(12, 1, "bring the silk")
        action = Talk(3, "hail", "bring the silk")
        action.step(client, sheet)
        self.assertEqual(commands(client), [])
        body.position = (5.0, 0.0, 0.0)
        action.active_path = None
        action.step(client, sheet)
        self.assertEqual(commands(client), ["Hail, orc"])
        action.step(client, sheet)
        self.assertFalse(action.complete)
        self.assertNotIn("Fetch", kinds(client))
        inbox(action, "OP_ChannelMessage", {"text": "bring the silk"})
        action.step(client, sheet)
        self.assertIn("Fetch", kinds(client))
        action.step(client, sheet)
        self.assertTrue(action.complete)


if __name__ == "__main__":
    unittest.main()
