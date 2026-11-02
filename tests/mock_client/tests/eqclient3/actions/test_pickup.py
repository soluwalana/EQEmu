"""Pickup walks to a ground spawn and clicks it."""

import struct
import unittest

from harness import fresh, movement, opcodes

from eqclient3.actions.pickup import Pickup
from eqclient3.world import GroundSpawn


class PickupTest(unittest.TestCase):
    def test_walk_click_then_the_drop_is_gone(self):
        client, sheet = fresh()
        sheet.ground[4] = GroundSpawn(4, "silk", 40.0, 0.0, 0.0)
        action = Pickup(4, (40.0, 0.0, 0.0))
        action.item_id = 7
        action.step(client, sheet)
        self.assertEqual(movement().advances[-1].mode, "run")
        sheet.position = (40.0, 0.0, 0.0)
        action.step(client, sheet)
        self.assertEqual(opcodes(client)[-1], "OP_ClickObject")
        drop, who = struct.unpack("<II", client.outbound[-1][1])
        self.assertEqual((drop, who), (4, 1))
        self.assertFalse(action.complete)
        sheet.ground.pop(4)
        action.step(client, sheet)
        self.assertTrue(action.complete)

    def test_a_click_that_yields_nothing_gives_up_on_that_spawn(self):
        client, sheet = fresh()
        sheet.ground[4] = GroundSpawn(4, "silk", 0.0, 0.0, 0.0)
        action = Pickup(4, (0.0, 0.0, 0.0))
        action.item_id = 7
        action.step(client, sheet)
        self.assertFalse(action.complete)
        for _ in range(20):
            action.step(client, sheet)
        self.assertTrue(action.complete)
        self.assertTrue(sheet.ground[4].used)


if __name__ == "__main__":
    unittest.main()
