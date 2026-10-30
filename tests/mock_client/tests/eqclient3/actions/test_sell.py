"""Sell opens the merchant and sells the bag slot. Another zone appends Zone."""

import unittest

from harness import fresh, kinds, opcodes

from eqclient3.actions.sell import Sell
from eqclient3.structs import OP_ShopPlayerSell


class SellTest(unittest.TestCase):
    def test_open_then_sell_the_bag_slot(self):
        client, sheet = fresh()
        sheet.bags[22] = 9
        sheet.zone = "qeynos"
        action = Sell([9])
        action.merchant_id = 5
        action.merchant_zone = "qeynos"
        action.merchant_point = (0.0, 0.0, 0.0)
        action.step(client, sheet)
        self.assertEqual(opcodes(client), ["OP_ShopRequest"])
        action.step(client, sheet)
        self.assertEqual(opcodes(client)[-1], "OP_ShopPlayerSell")
        sold = OP_ShopPlayerSell.deserialize(client.outbound[-1][1])
        self.assertEqual((sold.slot, sold.quantity), (22, 1))
        sheet.bags.pop(22)
        action.step(client, sheet)
        self.assertTrue(action.complete)

    def test_vendor_elsewhere_appends_zone(self):
        client, sheet = fresh()
        sheet.bags[22] = 9
        sheet.zone = "qeynos"
        action = Sell([9])
        action.merchant_id = 5
        action.merchant_zone = "freportw"
        action.merchant_point = (0.0, 0.0, 0.0)
        action.step(client, sheet)
        self.assertIn("Zone", kinds(client))
        self.assertNotIn("OP_ShopPlayerSell", opcodes(client))


if __name__ == "__main__":
    unittest.main()
