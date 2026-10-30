"""Band table. Higher priority first, then type(action).key(action), smaller first.

append stamps insert from a monotonic counter, started from the clock, and zone
from the world. A higher band suspends the loser. Bands are each action's priority.
"""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterator
    from eqclient3.action import Action
    from eqclient3.journal import Journal
    from eqclient3.world import World

import time

class Schedule:

    def __init__(self) -> None:
        self._next = 0
        self._actions: list = []
        self.journal = None
        self.character = ''

    def __iter__(self) -> Iterator[Action]:
        return iter(list(self._actions))

    def __len__(self) -> int:
        return len(self._actions)

    def __getitem__(self, index: int) -> Action:
        return self._actions[index]

    def bind(self, journal: Journal, character: str) -> None:
        """Journal and character used when append is not given them."""
        self.journal = journal
        self.character = character or ''

    def has_source(self, source: str) -> bool:
        if not source:
            return False
        return any((action.source == source for action in self._actions))

    def append(self, action: Action, world: World, journal: Journal | None = None, character: str | None = None) -> bool:
        """Stamp insert, started, and zone. A known source is not queued twice.

        A source already on this queue, or already resolved in the journal, is
        refused. An empty source is always queued and is not written to the journal.
        """
        journal = self.journal if journal is None else journal
        who = self.character if character is None else character
        source = str(action.source or '')
        if source and self.has_source(source):
            return False
        if source and journal is not None and who and journal.is_resolved(who, source):
            return False
        if source and journal is not None and who and journal.is_open(who, source):
            return False
        self._next += 1
        action.insert = self._next
        action.started = time.time()
        action.zone = str(world.zone or '')
        action._world = world
        if source and journal is not None and who:
            if not journal.open_action(who, action):
                return False
        self._actions.append(action)
        return True

    def restore(self, action: Action) -> bool:
        """Put a journal row back. Keeps zone and started. Stamps insert when it is 0."""
        source = str(action.source or '')
        if source and self.has_source(source):
            return False
        if action.insert:
            self._next = max(self._next, int(action.insert))
        else:
            self._next += 1
            action.insert = self._next
        if not action.started:
            action.started = time.time()
        self._actions.append(action)
        return True

    def remove(self, insert: int) -> None:
        self._actions = [action for action in self._actions if action.insert != insert]

    def winner(self) -> Action | None:
        if not self._actions:
            return None
        return min(self._actions, key=lambda action: (-action.priority, type(action).key(action)))

    def suspend_loser(self, winner: Action) -> None:
        """A higher band suspends the action that was running. The subject stays."""
        if winner is None:
            return
        for action in self._actions:
            if action is winner or action.suspended:
                continue
            if winner.priority > action.priority:
                action.suspend()

    def head(self) -> Action | None:
        chosen = self.winner()
        self.suspend_loser(chosen)
        return chosen
