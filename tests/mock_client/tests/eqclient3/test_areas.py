"""Explore boxes are the centers of the task table's area rows."""

import unittest

from eqclient3.data.areas import read_areas


class AreaParseTest(unittest.TestCase):
    def test_an_explore_row_keeps_its_box(self):
        rows = [
            "INSERT INTO `task_activities` VALUES",
            "(5094,0,-1,1,5,'',0,1,'Jail',NULL,NULL,'',0,-730,175,20,-680,220,25,'-1','0','189',-1,0);",
            "(5094,1,-1,1,2,'key',0,1,'',NULL,NULL,'',0,0,0,0,0,0,0,'-1','0','189',-1,0);",
        ]
        found = read_areas(rows)
        box = found[(5094, 0)]
        self.assertEqual(box.center(), (-705.0, 197.5, 22.5))
        self.assertNotIn((5094, 1), found)
