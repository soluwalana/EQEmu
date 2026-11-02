"""An explore step walks to the box and finishes when the server marks it done."""

import unittest
from types import SimpleNamespace

from harness import fresh, kinds, movement, place

from eqclient3.actions.read_tasks import ReadTasks
from eqclient3.actions.visit import Visit
from eqclient3.data.areas import Box, read_areas
from eqclient3.handlers.tasks import Activity


class VisitTest(unittest.TestCase):
    def test_the_open_explore_step_walks_to_the_box(self):
        client, sheet = fresh("tutorialb")
        explore = Activity(5094, 0, 5, "", "", "Infiltrate the Gloomingdeep Jail", 1)
        sheet.task_book = SimpleNamespace(activities=[explore])
        action = ReadTasks()
        place(client, action, "tutorialb", "read_tasks:tutorialb")
        action.step(client, sheet)
        self.assertIn("Visit", kinds(client))
        visit = next(row for row in client.queue if type(row).__name__ == "Visit")
        box = read_areas(
            [
                "INSERT INTO `task_activities` VALUES",
                "(5094,0,-1,1,5,'',0,1,'Jail',NULL,NULL,'',0,-730,175,20,-680,220,25,'-1','0','189',-1,0);",
            ]
        )[(5094, 0)]
        self.assertEqual(visit.point, box.center())

    def test_standing_outside_the_box_plans_a_walk(self):
        client, sheet = fresh("tutorialb")
        action = Visit(5094, 0, (-705.0, 197.5, 22.5))
        action.step(client, sheet)
        self.assertFalse(action.complete)
        self.assertEqual(movement().plans[-1][0], (-705.0, 197.5, 22.5))

    def test_a_finished_activity_completes_the_walk(self):
        client, sheet = fresh("tutorialb")
        done = Activity(5094, 0, 5, "", "", "Jail", 1, done=1)
        sheet.task_book = SimpleNamespace(activities=[done])
        action = Visit(5094, 0, (-705.0, 197.5, 22.5))
        action.step(client, sheet)
        self.assertTrue(action.complete)


class BoxCenterTest(unittest.TestCase):
    def test_center_is_the_middle_of_the_box(self):
        box = Box(1, 0, -10, 0, 2, 10, 4, 6)
        self.assertEqual(box.center(), (0.0, 2.0, 4.0))
