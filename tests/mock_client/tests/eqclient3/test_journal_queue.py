"""Open journal rows print in scheduler order."""

from eqclient3.action import Action
from eqclient3.actions.death import Death
from eqclient3.journal import Journal
from eqclient3.journal_queue import report


def test_open_rows_follow_priority_then_key():
    journal = Journal(":memory:")
    low = Action()
    low.source = "sell:1"
    low.priority = 0
    low.zone = "qeynos"
    low.durable = True
    death = Death()
    death.source = "death:qeynos"
    death.zone = "qeynos"
    death.durable = True
    journal.open_action("Hero", low)
    journal.open_action("Hero", death)
    journal.resolve_action("Hero", death)
    text = "\n".join(report(journal, "Hero"))
    assert text.splitlines()[0] == "Hero  open 1"
    assert "sell:1" in text
    assert "p410" not in text.split("resolved")[0]
    assert "Death" in text.split("resolved", 1)[1]
    assert "death:qeynos" in text
