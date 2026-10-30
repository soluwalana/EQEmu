"""Trade: request, move onto the cursor, accept, then the close."""

import unittest

from harness import fresh, inbox, opcodes

from eqclient3.actions.trade import Trade


class TradeSteps(unittest.TestCase):
    def test_request_move_accept_close(self):
        client, sheet = fresh()
        sheet.bags[22] = 9
        action = Trade(5, 9)
        action.step(client, sheet)
        self.assertEqual(opcodes(client), ["OP_TradeRequest"])
        action.step(client, sheet)
        self.assertEqual(opcodes(client)[-1], "OP_MoveItem")
        sheet.cursor = 9
        action.step(client, sheet)
        self.assertEqual(opcodes(client)[-1], "OP_TradeAcceptClick")
        self.assertEqual(action.waiting, ["TRADE"])
        action.step(client, sheet)
        self.assertFalse(action.complete)
        inbox(action, "OP_FinishTrade", b"")
        action.step(client, sheet)
        self.assertTrue(action.complete)


if __name__ == "__main__":
    unittest.main()
