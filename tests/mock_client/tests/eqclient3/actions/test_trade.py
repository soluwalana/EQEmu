"""Trade requests, moves the item, accepts, and completes on the close."""

import struct
import unittest

from harness import fresh, inbox, opcodes

from eqclient3.actions.trade import Trade
from eqclient3.inventory.assign import release_cursor
from eqclient3.structs import OP_ShopPlayerBuy


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
        src = struct.unpack_from("<h", client.outbound[-1][1], 4)[0]
        dest = struct.unpack_from("<h", client.outbound[-1][1], 16)[0]
        self.assertEqual((src, dest), (23, 33))
        sheet.bags.pop(22)
        sheet.cursor = 9
        action.step(client, sheet)
        placed = client.outbound[-1][1]
        kind, _unknown, slot, sub = struct.unpack_from("<hhhh", placed, 12)
        self.assertEqual((kind, slot, sub), (3, 0, -1))
        for _ in range(9):
            action.step(client, sheet)
        self.assertNotIn("OP_TradeAcceptClick", opcodes(client))
        action.step(client, sheet)
        self.assertEqual(opcodes(client)[-1], "OP_TradeAcceptClick")
        self.assertEqual(action.waiting, ["TRADE"])
        action.step(client, sheet)
        self.assertFalse(action.complete)
        inbox(action, "OP_FinishTrade", b"")
        action.step(client, sheet)
        self.assertTrue(action.complete)

    def test_an_open_trade_keeps_the_item_on_the_cursor(self):
        client, sheet = fresh()
        sheet.cursor = 9
        trade = Trade(5, 9)
        client.queue.append(trade, sheet)
        release_cursor(client, sheet)
        self.assertEqual(opcodes(client), [])
        self.assertEqual(sheet.cursor, 9)

    def test_a_saved_trade_without_the_pickup_flag_still_sends_once(self):
        action = Trade(5, 9)
        del action.sent_move
        del action.move_from
        state = dict(action.__dict__)
        revived = Trade.__new__(Trade)
        revived.__setstate__(state)
        self.assertFalse(revived.sent_move)
        self.assertIsNone(revived.move_from)
        self.assertFalse(revived.sent_offer)
        self.assertFalse(revived.offered)

    def test_the_pickup_is_sent_once_and_silence_lands_it(self):
        client, sheet = fresh()
        sheet.bags[22] = 9
        action = Trade(5, 9)
        action.step(client, sheet)
        action.step(client, sheet)
        for _ in range(9):
            action.step(client, sheet)
        self.assertEqual(opcodes(client).count("OP_MoveItem"), 1)
        self.assertNotIn("OP_TradeAcceptClick", opcodes(client))
        action.step(client, sheet)
        self.assertEqual(opcodes(client).count("OP_MoveItem"), 2)
        kind, _unknown, slot, sub = struct.unpack_from("<hhhh", client.outbound[-1][1], 12)
        self.assertEqual((kind, slot, sub), (3, 0, -1))
        self.assertEqual(sheet.cursor, 9)
        self.assertNotIn(22, sheet.bags)
        for _ in range(9):
            action.step(client, sheet)
        action.step(client, sheet)
        self.assertEqual(opcodes(client)[-1], "OP_TradeAcceptClick")
        self.assertIsNone(sheet.cursor)

    def test_a_returned_item_is_picked_up_once_more(self):
        client, sheet = fresh()
        sheet.bags[22] = 9
        action = Trade(5, 9)
        action.step(client, sheet)
        action.step(client, sheet)
        inbox(action, "OP_ItemPacket", {"slot": 22, "item_id": 9})
        action.step(client, sheet)
        self.assertEqual(opcodes(client).count("OP_MoveItem"), 1)
        action.step(client, sheet)
        self.assertEqual(opcodes(client).count("OP_MoveItem"), 2)

    def test_a_close_that_keeps_the_item_asks_again(self):
        client, sheet = fresh()
        sheet.cursor = 9
        action = Trade(5, 9)
        action.requested = True
        action.accepted = True
        action.offered = True
        action.wait("TRADE")
        inbox(action, "OP_FinishTrade", b"")
        action.step(client, sheet)
        self.assertFalse(action.complete)
        self.assertFalse(action.requested)
        action.step(client, sheet)
        self.assertEqual(opcodes(client), ["OP_TradeRequest"])

    def test_a_missing_item_closes_the_trade(self):
        client, sheet = fresh()
        action = Trade(5, 9)
        action.requested = True
        action.step(client, sheet)
        self.assertTrue(action.complete)
        self.assertEqual(opcodes(client), [])

    def test_buy_uses_the_merchant_window_slot(self):
        client, sheet = fresh()
        sheet.bags[22] = 1
        action = Trade(5, 9)
        action.slots[4] = (9, 12)
        action.step(client, sheet)
        self.assertEqual(opcodes(client), ["OP_ShopRequest"])
        action.step(client, sheet)
        self.assertEqual(opcodes(client)[-1], "OP_ShopPlayerBuy")
        bought = OP_ShopPlayerBuy.deserialize(client.outbound[-1][1])
        self.assertEqual((bought.slot, bought.quantity, bought.price), (4, 1, 12))


if __name__ == "__main__":
    unittest.main()
