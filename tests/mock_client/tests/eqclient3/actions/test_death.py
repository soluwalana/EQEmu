"""Death drops every ephemeral action, including work tagged for another zone."""

import unittest

from harness import fresh, place

from eqclient3.actions.attack import Attack
from eqclient3.actions.bots.form import Form
from eqclient3.actions.bots.summon import Summon
from eqclient3.actions.cure import Cure
from eqclient3.actions.cursor import Cursor
from eqclient3.actions.death import Death
from eqclient3.actions.deliver import Deliver
from eqclient3.actions.fetch import Fetch
from eqclient3.actions.field import Field
from eqclient3.actions.follow import Follow
from eqclient3.actions.heal import Heal
from eqclient3.actions.hold import Hold
from eqclient3.actions.kill import Kill
from eqclient3.actions.loot_mob import LootMob
from eqclient3.actions.reclaim import Reclaim
from eqclient3.actions.rest import Rest
from eqclient3.actions.talk import Talk
from eqclient3.actions.trade import Trade


class DeathTest(unittest.TestCase):
    def test_ephemeral_work_is_removed(self):
        client, sheet = fresh("crushbone")
        gone = [
            Attack(1),
            Hold(2),
            Talk(3, "hail", ""),
            Follow(4),
            Heal("Hero"),
            Cure(1, "poison"),
            Rest("Hero"),
            Kill(spawn_id=5),
            Field("forage"),
            Form("crushbone"),
            Summon(271),
        ]
        stay = [
            Fetch(9, 1, "keep"),
            Trade(6, 9),
            Deliver(9, 6),
            Cursor(22),
            LootMob(8, (0, 0, 0)),
            Reclaim(8, (0, 0, 0)),
            Attack(11),
        ]
        for index, action in enumerate(gone):
            place(client, action, "crushbone", f"gone:{index}")
        for index, action in enumerate(stay[:-1]):
            place(client, action, "crushbone", f"stay:{index}")
        place(client, stay[-1], "freportw", "gone:other-zone")
        death = Death()
        death.zone = "crushbone"
        death.insert = 900
        self.assertNotIn("OP_Assist", death.opcodes())
        death.step(client, sheet)
        self.assertTrue(death.complete)
        left = {action.source for action in client.queue}
        for index in range(len(gone)):
            self.assertNotIn(f"gone:{index}", left)
            self.assertFalse(client.journal.is_open("Hero", f"gone:{index}"))
        for index in range(len(stay) - 1):
            self.assertIn(f"stay:{index}", left)
        self.assertNotIn("gone:other-zone", left)
        self.assertFalse(client.journal.is_open("Hero", "gone:other-zone"))


if __name__ == "__main__":
    unittest.main()
