"""Trade requests, moves the item, accepts, and completes on the close."""

import struct
import unittest

from harness import fresh, inbox, opcodes

from eqclient3.actions.trade import Trade


class TradeTest(unittest.TestCase):
    def test_request_move_accept_close(self):
        client, sheet = fresh()
        sheet.bags[22] = 9
        action = Trade(5, 9)
        self.assertNotIn("OP_Assist", action.opcodes())
        action.step(client, sheet)
        self.assertEqual(opcodes(client), ["OP_TradeRequest"])
        action.step(client, sheet)
        self.assertEqual(opcodes(client)[-1], "OP_MoveItem")
        src, dest, _pad = struct.unpack("<III", client.outbound[-1][1])
        self.assertEqual((src, dest), (22, 30))
        sheet.cursor = 9
        action.step(client, sheet)
        self.assertEqual(opcodes(client)[-1], "OP_TradeAcceptClick")
        self.assertEqual(action.waiting, ["TRADE"])
        action.step(client, sheet)
        self.assertFalse(action.complete)
        inbox(action, "OP_FinishTrade", b"")
        action.step(client, sheet)
        self.assertTrue(action.complete)

    def test_buy_uses_the_merchant_window_slot(self):
        client, sheet = fresh()
        sheet.bags[22] = 1
        action = Trade(5, 9)
        action.slots[4] = (9, 12)
        action.step(client, sheet)
        self.assertEqual(opcodes(client), ["OP_ShopRequest"])
        action.step(client, sheet)
        _npc, _player, slot, _zero, qty, price = struct.unpack("<IIIIII", client.outbound[-1][1])
        self.assertEqual(opcodes(client)[-1], "OP_ShopPlayerBuy")
        self.assertEqual((slot, qty, price), (4, 1, 12))


if __name__ == "__main__":
    unittest.main()
