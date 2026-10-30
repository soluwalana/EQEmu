"""Train walks, opens the window, spends one point, and completes when the points are gone."""

import unittest

from harness import fresh, inbox, mob, movement, opcodes

from eqclient3.actions.train import Train


class TrainTest(unittest.TestCase):
    def test_walk_open_point_answer(self):
        client, sheet = fresh()
        sheet.training_points = 1
        sheet.train_skill = 0
        mob(sheet, 7, distance=40, name="Guildmaster", targeted=True)
        action = Train(7)
        action.step(client, sheet)
        self.assertEqual(movement().advances[-1].mode, "run")
        sheet.position = (40.0, 0.0, 0.0)
        action.step(client, sheet)
        self.assertEqual(opcodes(client)[-1], "OP_GMTraining")
        self.assertEqual(len(client.outbound[-1][1]), 448)
        action.step(client, sheet)
        self.assertEqual(opcodes(client)[-1], "OP_GMTrainSkill")
        self.assertEqual(action.waiting, ["TRAIN"])
        action.step(client, sheet)
        self.assertFalse(action.complete)
        sheet.training_points = 0
        inbox(action, "OP_GMTrainSkill", b"")
        action.step(client, sheet)
        self.assertEqual(opcodes(client)[-1], "OP_GMEndTraining")
        self.assertTrue(action.complete)


if __name__ == "__main__":
    unittest.main()
