"""Follow walks to the leader. A spawn update refreshes the point."""

import unittest

from harness import fresh, mob, movement

from eqclient3.action import Message
from eqclient3.actions.follow import Follow
from eqclient3.structs import OP_MobUpdate


class FollowTest(unittest.TestCase):
    def test_walks_and_refreshes(self):
        client, sheet = fresh()
        mob(sheet, 4, distance=30, name="Leader")
        action = Follow(4)
        action.step(client, sheet)
        self.assertEqual(movement().advances[-1].dest, (30.0, 0.0, 0.0))
        action.add_message(Message(OP_MobUpdate(4, 8.0, 1.0, 0.0)))
        action.step(client, sheet)
        self.assertEqual(movement().advances[-1].dest, (8.0, 1.0, 0.0))
        self.assertFalse(action.complete)


if __name__ == "__main__":
    unittest.main()
