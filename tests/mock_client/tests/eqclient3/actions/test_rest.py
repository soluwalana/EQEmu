"""Rest sits. Bot mana waits while a silk Fetch is the durable head."""

import struct
import unittest

from harness import commands, fresh, opcodes

from eqclient3.actions.fetch import Fetch
from eqclient3.actions.rest import Rest


class RestTest(unittest.TestCase):
    def test_sits(self):
        client, sheet = fresh()
        action = Rest("Hero")
        action.step(client, sheet)
        self.assertEqual(opcodes(client), ["OP_SpawnAppearance"])
        spawn, kind, value = struct.unpack("<HHI", client.outbound[0][1])
        self.assertEqual((spawn, kind, value), (1, 14, 110))
        self.assertEqual(commands(client), [])

    def test_bot_mana_waits_on_silk(self):
        client, sheet = fresh()
        silk = Fetch(54234, 1, "silk")
        client.queue.append(silk, sheet, client.journal, "Hero")
        action = Rest("Cleric")
        action.mana = True
        action.step(client, sheet)
        self.assertEqual(client.outbound, [])
        self.assertFalse(action.complete)


if __name__ == "__main__":
    unittest.main()
