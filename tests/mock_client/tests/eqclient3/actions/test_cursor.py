"""Cursor waits on the outstanding token, then writes the bag."""

import struct
import unittest

from harness import fresh, inbox, opcodes

from eqclient3.actions.cursor import Cursor


class CursorTest(unittest.TestCase):
    def test_token_outstanding_then_real_item(self):
        client, sheet = fresh()
        action = Cursor(22)
        self.assertNotIn("OP_Assist", action.opcodes())
        action.step(client, sheet)
        self.assertEqual(action.waiting, ["CURSOR"])
        self.assertNotIn("OP_MoveItem", opcodes(client))
        inbox(action, "OP_ItemPacket", {"slot": 22, "item_id": 22292})
        action.step(client, sheet)
        self.assertFalse(action.complete)
        self.assertNotIn(22, sheet.bags)
        inbox(action, "OP_ItemPacket", {"slot": 22, "item_id": 1001})
        action.step(client, sheet)
        self.assertTrue(action.complete)
        self.assertEqual(sheet.bags[22], 1001)

    def test_delete_for_the_slot_writes_the_bag(self):
        client, sheet = fresh()
        sheet.bags[22] = 1001
        sheet.cursor = 22292
        action = Cursor(22)
        action.waiting = ["CURSOR"]
        inbox(action, "OP_DeleteItem", struct.pack("<I", 22))
        action.step(client, sheet)
        self.assertTrue(action.complete)
        self.assertNotIn(22, sheet.bags)
        self.assertIsNone(sheet.cursor)

    def test_timeout_retries_the_same_move(self):
        client, sheet = fresh()
        sheet.cursor_move = (22, 30)
        action = Cursor(22)
        action.step(client, sheet)
        for _ in range(9):
            action.step(client, sheet)
        self.assertNotIn("OP_MoveItem", opcodes(client))
        action.step(client, sheet)
        self.assertEqual(opcodes(client), ["OP_MoveItem"])
        src = struct.unpack_from("<h", client.outbound[0][1], 4)[0]
        dest = struct.unpack_from("<h", client.outbound[0][1], 16)[0]
        self.assertEqual((src, dest), (23, 33))
        self.assertEqual(action.waiting, ["CURSOR"])

    def test_a_quiet_move_lands_and_clears_the_cursor(self):
        client, sheet = fresh()
        sheet.cursor = 59964
        action = Cursor(22, (30, 22))
        action.step(client, sheet)
        self.assertEqual(opcodes(client), ["OP_MoveItem"])
        for _ in range(10):
            action.step(client, sheet)
        self.assertTrue(action.complete)
        self.assertIsNone(sheet.cursor)
        self.assertEqual(sheet.bags[22], 59964)
        self.assertNotIn(22, sheet.refused_slots)


if __name__ == "__main__":
    unittest.main()
