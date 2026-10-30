"""Train: walk, open the window, one point, the answer, then the points are spent."""

import unittest

from harness import fresh, inbox, mob, opcodes

from eqclient3.actions.train import Train


class TrainSteps(unittest.TestCase):
    def test_walk_open_point_answer_complete(self):
        client, sheet = fresh()
        sheet.training_points = 2
        sheet.train_skill = 15
        mob(sheet, 7, distance=30, targeted=True)
        action = Train(7)
        action.step(client, sheet)
        self.assertEqual(opcodes(client), [])
        sheet.position = (30.0, 0.0, 0.0)
        action.step(client, sheet)
        self.assertEqual(opcodes(client)[-1], "OP_GMTraining")
        action.step(client, sheet)
        self.assertEqual(opcodes(client)[-1], "OP_GMTrainSkill")
        self.assertEqual(action.waiting, ["TRAIN"])
        action.step(client, sheet)
        self.assertFalse(action.complete)
        sheet.training_points = 0
        inbox(action, "OP_GMEndTraining", b"")
        action.step(client, sheet)
        self.assertTrue(action.complete)
        self.assertEqual(opcodes(client)[-1], "OP_GMEndTraining")


if __name__ == "__main__":
    unittest.main()
