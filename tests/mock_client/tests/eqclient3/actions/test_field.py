"""Field eats, forages, fishes, or bandages. An empty forage at water starts fishing."""

import unittest

from harness import fresh, kinds, opcodes

from eqclient3.actions.field import Field


class FieldTest(unittest.TestCase):
    def test_forage_at_water_appends_fish(self):
        client, sheet = fresh()
        sheet.forage_found = False
        sheet.at_water = True
        action = Field("forage")
        action.step(client, sheet)
        self.assertEqual(opcodes(client), ["OP_Forage"])
        self.assertTrue(action.complete)
        self.assertIn("Field", kinds(client))
        fish = next(row for row in client.queue if type(row).__name__ == "Field")
        self.assertEqual(fish.kind, "fish")

    def test_eat_and_bandage(self):
        client, sheet = fresh()
        Field("eat", slot=22).step(client, sheet)
        self.assertEqual(opcodes(client)[-1], "OP_Consume")
        Field("bandage").step(client, sheet)
        self.assertEqual(opcodes(client)[-1], "OP_Bind_Wound")


if __name__ == "__main__":
    unittest.main()
