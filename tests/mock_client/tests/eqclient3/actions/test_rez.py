"""Rez accepts once. OP_DeleteSpawn finishes it. Seat follows Rez in the band."""

import struct
import unittest

from harness import fresh, inbox

from eqclient3.actions.rez import Rez
from eqclient3.structs import OP_RezzAnswer


class RezTest(unittest.TestCase):
    def test_accept_once_then_delete(self):
        client, sheet = fresh()
        action = Rez(7, b"\x00\x00\x00\x00")
        self.assertEqual(Rez.key(action), (0,))
        action.step(client, sheet)
        self.assertEqual(opcodes_of(client), ["OP_RezzAnswer"])
        self.assertEqual(OP_RezzAnswer.deserialize(client.outbound[0][1]).action, 1)
        action.step(client, sheet)
        self.assertEqual(len(client.outbound), 1)
        inbox(action, "OP_DeleteSpawn", struct.pack("<I", 7))
        action.step(client, sheet)
        self.assertTrue(action.complete)


def opcodes_of(client):
    return [opcode for opcode, _payload in client.outbound]


if __name__ == "__main__":
    unittest.main()
