"""Recent progress and another way to reach the same goal.

A repeated handful of cells means the last walk failed. The task stays. The
next attempt stands somewhere new, then heads for that same place again.
"""

from __future__ import annotations

from collections.abc import Callable, Iterable
from typing import Protocol


import heapq
import math

CELL = 10.0


def cell_of(x: float, y: float) -> tuple[int, int]:
    return (int(round(x / CELL)), int(round(y / CELL)))


class _Progress(Protocol):
    task_id: int
    activity_id: int
    done: int


_Link = Callable[[tuple[int, int]], Iterable[tuple[tuple[int, int], tuple[float, float, float]]]]


def signature_of(activities: list[_Progress]) -> tuple[tuple[int, int, int], ...]:
    return tuple(sorted((item.task_id, item.activity_id, item.done) for item in activities))


class AreaSearch:
    """A* toward the live target, then backtrack through polygons not yet walked.

    The target point is passed in every tick, so a moving NPC pulls the next
    branch. A dead end pops the stack and the walk returns to the last polygon
    that still has an unvisited neighbor.
    """

    def __init__(self) -> None:
        self.visited: set[tuple[int, int]] = set()
        self.stack: list[tuple[int, int]] = []
        self.aim: tuple[float, float, float] | None = None
        self.goal_poly: tuple[int, int] | None = None
        self.blocked: set[tuple[int, int]] = set()

    def reset(self) -> None:
        self.visited.clear()
        self.stack.clear()
        self.aim = None
        self.goal_poly = None
        self.blocked.clear()

    def block(self, point: tuple[float, float, float]) -> None:
        """The server never granted this point, so the next branch goes around it."""
        self.blocked.add(cell_of(point[0], point[1]))
        self.aim = None

    def advance(
        self,
        position: tuple[float, float, float],
        goal: tuple[float, float, float],
        locate: Callable[[tuple[float, float, float]], tuple[int, int] | None],
        links: _Link,
        center_of: Callable[[tuple[int, int]], tuple[float, float, float] | None],
    ) -> tuple[float, float, float]:
        goal_id = locate(goal)
        if self.aim is not None and self._held(self.aim):
            self.aim = None
        # Stay on this polygon until he arrives. Repicking a closer center turns him around.
        if self.aim is not None and goal_id == self.goal_poly and _span(position, self.aim) > 1.0:
            return self.aim
        self.goal_poly = goal_id
        here = locate(position)
        if here is None:
            if self._held(goal):
                self.aim = None
                return position
            self.aim = goal
            return goal
        self.visited.add(here)
        if goal_id is not None and here == goal_id:
            self.aim = goal
            return goal
        if not self.stack or self.stack[-1] != here:
            self.stack.append(here)
        route = _route(here, goal_id, links, self.visited, center_of) if goal_id is not None else []
        previous = self.stack[-2] if len(self.stack) >= 2 else None
        if len(route) >= 2 and route[1][0] != previous and not self._held(route[1][1]):
            self.aim = route[1][1]
            return self.aim
        opened = self._open(here, goal, links, previous)
        if opened is not None:
            self.aim = opened
            return opened
        while self.stack:
            self.stack.pop()
            if not self.stack:
                break
            parent = self.stack[-1]
            opened = self._open(parent, goal, links, None)
            if opened is not None:
                self.aim = opened
                return opened
        self.visited.clear()
        self.stack.clear()
        if self._held(goal):
            self.aim = None
            return position
        self.aim = goal
        return goal

    def _open(
        self,
        poly_id: tuple[int, int],
        goal: tuple[float, float, float],
        links: _Link,
        skip: tuple[int, int] | None,
    ) -> tuple[float, float, float] | None:
        choices = []
        for neighbor, center in links(poly_id):
            if neighbor in self.visited or neighbor == skip or self._held(center):
                continue
            choices.append((_span(center, goal), center))
        if not choices:
            return None
        choices.sort(key=lambda item: item[0])
        return choices[0][1]

    def _held(self, point: tuple[float, float, float]) -> bool:
        return cell_of(point[0], point[1]) in self.blocked


def bearing(here: tuple[float, float, float], there: tuple[float, float, float]) -> int:
    """Eight headings around here. A refused step rules out one of them."""
    angle = math.atan2(there[1] - here[1], there[0] - here[0])
    return int(round(angle / (math.pi / 4.0))) % 8


LENGTHS = (24.5, 14.0, 8.0, 4.0, 2.0, 1.0, 0.5)


def next_length(length: float) -> float | None:
    """The next shorter step once every heading at this distance has failed."""
    for item in LENGTHS:
        if item < length - 1e-6:
            return item
    return None


def other_step(
    here: tuple[float, float, float],
    goal: tuple[float, float, float],
    refused_dirs: set[int],
    length: float = 4.0,
    turn_offset: float = 0.0,
) -> tuple[float, float, float] | None:
    """The next place to ask for. A used heading yields the next angle.

    Height follows the waypoint. A ramp changes about as fast as he walks.
    A gap of more than a few yards means he has left the floor, so the step
    puts him back on it. The move packet still sends no vertical speed.
    """
    dx = goal[0] - here[0]
    dy = goal[1] - here[1]
    dist = math.hypot(dx, dy)
    if dist < 0.3:
        if abs(goal[2] - here[2]) > 6.0:
            return (goal[0], goal[1], goal[2])
        return None
    base = math.atan2(dy, dx) + math.radians(turn_offset)
    for turn in (0, 45, -45, 90, -90, 135, -135, 180):
        angle = base + math.radians(turn)
        if bearing(here, (here[0] + math.cos(angle), here[1] + math.sin(angle), here[2])) in refused_dirs:
            continue
        travel = min(length, dist)
        return (
            here[0] + math.cos(angle) * travel,
            here[1] + math.sin(angle) * travel,
            _step_height(here[2], goal[2], travel),
        )
    return None


def is_stair(points: list[tuple[float, float, float]]) -> bool:
    """A run of centers climbing/descending the same way — stairs get a steeper budget."""
    if len(points) < 2:
        return False
    n = min(3, len(points) - 1)
    deltas = [points[i + 1][2] - points[i][2] for i in range(n)]
    # Gentle ramps (~0.5) count; huge cliffs do not.
    if any(abs(delta) < 0.5 or abs(delta) > 12.0 for delta in deltas):
        return False
    return all(delta > 0 for delta in deltas) or all(delta < 0 for delta in deltas)


def _step_height(here_z: float, goal_z: float, travel: float, stair: bool = False) -> float:
    """Follow mesh/goal Z each stride — ramps gradually, stairs a bit steeper.

    Returning here_z for non-stairs left him glued to the flat (z=-51 on ecommons
    hills) while goto climbed. Budget scales with horizontal travel so a normal
    step can take a ~45° ramp without needing stair detection.
    """
    gap = goal_z - here_z
    if abs(gap) < 0.2:
        return goal_z
    travel = max(float(travel), 0.5)
    # Stairs: up to 10 yd/step. Ramps: about as steep as the stride is long.
    budget = 10.0 if stair else min(10.0, max(2.0, travel * 1.5))
    if abs(gap) <= budget:
        return goal_z
    return here_z + (budget if gap > 0 else -budget)


def refused(
    origin: tuple[float, float, float],
    asked: tuple[float, float, float],
    actual: tuple[float, float, float],
) -> bool:
    """True when the server left him where he was after a move packet.

    An invalid step gets no position update and no log line. A granted step
    moves him off the point he sent the packet from.
    """
    return _span(actual, origin) <= 0.4 and _span(origin, asked) > 0.4


def _route(
    start: tuple[int, int],
    goal: tuple[int, int],
    links: _Link,
    visited: set[tuple[int, int]],
    center_of: Callable[[tuple[int, int]], tuple[float, float, float] | None],
) -> list[tuple[tuple[int, int], tuple[float, float, float]]]:
    """A* over polygon ids. Visited polygons are closed, except the ends."""
    if start == goal:
        return []
    start_at = center_of(start)
    goal_at = center_of(goal)
    if start_at is None or goal_at is None:
        return []
    came: dict[tuple[int, int], tuple[int, int] | None] = {start: None}
    cost = {start: 0.0}
    centers = {start: start_at, goal: goal_at}
    open_heap = [(0.0, start)]
    while open_heap:
        _score, current = heapq.heappop(open_heap)
        if current == goal:
            chain: list[tuple[tuple[int, int], tuple[float, float, float]]] = []
            node: tuple[int, int] | None = current
            while node is not None:
                chain.append((node, centers[node]))
                node = came[node]
            chain.reverse()
            return chain
        for neighbor, center in links(current):
            centers[neighbor] = center
            if neighbor in visited and neighbor != goal:
                continue
            step = cost[current] + _span(centers[current], center)
            if step < cost.get(neighbor, 1e18):
                cost[neighbor] = step
                came[neighbor] = current
                heapq.heappush(open_heap, (step + _span(center, goal_at), neighbor))
    return []


def _span(a: tuple[float, float, float], b: tuple[float, float, float]) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])


class Survey:
    def __init__(self) -> None:
        self.signature: str | None = None
        self.samples: list[tuple[int, int]] = []
        self.visited: set[tuple[int, int]] = set()
        self.avoid: set[tuple[int, int]] = set()
        self.tried: set[tuple[int, int]] = set()
        self.detour: tuple[float, float, float] | None = None

    def reset(self) -> None:
        self.signature = None
        self.samples.clear()
        self.visited.clear()
        self.avoid.clear()
        self.tried.clear()
        self.detour = None

    def note(self, position: tuple[float, float, float], signature: str) -> None:
        if signature != self.signature:
            self.signature = signature
            self.samples.clear()
            self.avoid.clear()
            self.tried.clear()
            self.detour = None
        landed = cell_of(position[0], position[1])
        self.visited.add(landed)
        self.samples.append(landed)
        if len(self.samples) > 12:
            del self.samples[0]

    def looping(self) -> bool:
        window = self.samples[-8:]
        if len(window) < 8:
            return False
        return len(set(window)) <= 2

    def new_approach(
        self, here: tuple[float, float, float], goal: tuple[float, float, float]
    ) -> tuple[float, float, float] | None:
        """A new place to stand on the way to goal. Goal itself does not change."""
        self.avoid.update(self.samples[-8:])
        dx = here[0] - goal[0]
        dy = here[1] - goal[1]
        base = math.atan2(dy, dx) if dx or dy else 0.0
        distance = math.hypot(dx, dy)
        for extra in (0, 15, 30):
            radius = max(20.0, distance) + extra
            for step in range(1, 7):
                token = (step, extra)
                if token in self.tried:
                    continue
                angle = base + step * math.pi / 3
                point = (
                    goal[0] + math.cos(angle) * radius,
                    goal[1] + math.sin(angle) * radius,
                    goal[2],
                )
                landed = cell_of(point[0], point[1])
                if landed in self.visited or landed in self.avoid:
                    continue
                self.tried.add(token)
                return point
        return None
