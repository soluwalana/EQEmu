"""Queue a whole class epic from the quest graph and compare it to the epic notes.

The notes list each flag in the order a character meets it. For each step, the
first listed way to obtain an item comes before the say, hand-in, or combine.
Later loot lines, other recipes, and dump-only notes are the same item again.
produce appends the graph's actions for those items, then the step itself.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

import pytest

from eqclient3.action import Action
from eqclient3.actions.craft import Craft
from eqclient3.actions.deliver import Deliver
from eqclient3.actions.fetch import Fetch
from eqclient3.actions.kill import Kill
from eqclient3.actions.quest_talk import Hand, QuestTalk, Say
from eqclient3.actions.talk import Talk
from eqclient3.data.recipes import Recipe, _WORLD_CONTAINER
from eqclient3.loop import Loop
from eqclient3.quests.expand import conversation
from eqclient3.quests.graph import QuestGraph, load_graph, split_npc
from eqclient3.world import World
from eqclient3.quests.produce import produce
from eqclient3.schedule import Schedule

_EPICS = Path(__file__).resolve().parents[5] / ".epics"
_GRAPH = Path.home() / ".eqclient" / "quest_graph.jsonl"

Step = tuple[str, ...]
Edge = dict[str, object]

_GIVER = re.compile(
    r'^(?P<zone>[a-z0-9]+)/"(?P<npc>[^"]+)", (?P<act>say|hand) (?P<body>.*)\. Gives "[^"]+" \((?P<result>\d+)\)\.$'
)
_SAY = re.compile(r'^Say "([^"]+)" to ([a-z0-9]+)/"([^"]+)"\.$')
_HAND = re.compile(
    r'^Hand (?P<body>.+) to (?P<zone>[a-z0-9]+)/"(?P<npc>[^"]+)"\.(?: Spawns .+?)?(?: Loot "[^"]+" \((?P<loot>\d+)\) from .+?)?$'
)
_LOOT = re.compile(r'^Loot "[^"]+" \((\d+)\) from "[^"]+"(?: in `[^`]+`)?\.$')
_GROUND = re.compile(r'^Ground spawn of "[^"]+" \((\d+)\) in `[^`]+`\.$')
_KILL = re.compile(r'^Kill ([a-z0-9]+)/"([^"]+)"\.')
_PRODUCES = re.compile(r"Produces (?P<body>.+?)\.")
_ITEM_AT_END = re.compile(r"\((\d+)\)\s*\.?$")
_FLAG = re.compile(r"^(#{2,6}) `([^`]+)`\s*$")
_STEP = re.compile(r"^(#{3,6}) (\d+)\. (.+?) — (say .+|hand [0-9+]+|combine recipe \d+)\s*$")
_PREREQ = re.compile(r'^### "(.+)" \((\d+)\)\s*$')
_NUMBERED = re.compile(r"^\d+\. (?P<body>.+)$")
_SKIP_LINE = re.compile(
    r"^(?:\d+ other |Common item:|No quest step|\*\*Broken|Summon |Forage |Fish |Same item|Spawns )"
)


@dataclass
class _Chain:
    steps: list[Step] = field(default_factory=list)
    fetched: set[int] = field(default_factory=set)
    given: set[int] = field(default_factory=set)
    crafted: set[int] = field(default_factory=set)
    killed: set[str] = field(default_factory=set)


@dataclass
class _FlagStep:
    flag: str
    value: int
    npc: str
    word: str
    delivers: tuple[int, ...]
    recipe: int
    result: int
    items: list[int]
    inline: dict[int, list[Step]]


def _npc(name: object) -> str:
    return " ".join(str(name).replace("_", " ").lower().split())


def _ids(text: str) -> list[int]:
    return [int(raw) for raw in re.findall(r"\((\d+)\)", text)]


def _sentence(text: str) -> tuple[list[Step], str, int | str] | None:
    """Actions on one note line. None when the line is not a step."""
    if _SKIP_LINE.match(text):
        return None
    giver = _GIVER.match(text)
    if giver:
        npc = _npc(giver.group("npc"))
        result = int(giver.group("result"))
        steps: list[Step] = []
        if giver.group("act") == "say":
            word = giver.group("body").split(".", 1)[0].strip().strip('"').lower()
            steps.append(("talk", npc, word))
            handed = giver.group("body").split(".", 1)[1] if "." in giver.group("body") else ""
            for item_id in _ids(handed):
                steps.append(("deliver", npc, str(item_id)))
        else:
            for item_id in _ids(giver.group("body")):
                steps.append(("deliver", npc, str(item_id)))
        return steps, "give", result
    said = _SAY.match(text)
    if said:
        return ([("talk", _npc(said.group(3)), said.group(1).lower())], "talk", said.group(1).lower())
    handed = _HAND.match(text)
    if handed:
        npc = _npc(handed.group("npc"))
        rows: list[Step] = []
        for item_id in _ids(handed.group("body")):
            rows.append(("deliver", npc, str(item_id)))
        loot = handed.group("loot")
        if loot:
            rows.append(("fetch", loot))
            return rows, "fetch", int(loot)
        first = _ids(handed.group("body"))
        return rows, "give", first[0] if first else 0
    loot = _LOOT.match(text)
    if loot:
        item_id = int(loot.group(1))
        return ([("fetch", str(item_id))], "fetch", item_id)
    ground = _GROUND.match(text)
    if ground:
        item_id = int(ground.group(1))
        return ([("fetch", str(item_id))], "fetch", item_id)
    killed = _KILL.match(text)
    if killed:
        zone = killed.group(1)
        npc = _npc(killed.group(2))
        return ([("kill", zone, npc)], "kill", f"{zone}/{npc}")
    if text.startswith("Combine "):
        produced = _PRODUCES.search(text)
        if produced is None or "no new item" in produced.group("body"):
            return None
        made = _ids(produced.group("body"))
        if not made:
            return None
        return ([("craft", str(made[-1]))], "craft", made[-1])
    return None


def _absorb(text: str, chain: _Chain) -> None:
    parsed = _sentence(text)
    if parsed is None:
        return
    steps, kind, ident = parsed
    if kind == "fetch" and isinstance(ident, int) and ident in chain.fetched:
        return
    if kind == "give" and isinstance(ident, int) and ident in chain.given:
        return
    if kind == "craft" and isinstance(ident, int) and ident in chain.crafted:
        return
    if kind == "kill" and isinstance(ident, str) and ident in chain.killed:
        return
    chain.steps.extend(steps)
    if kind == "fetch" and isinstance(ident, int):
        chain.fetched.add(ident)
    elif kind == "give" and isinstance(ident, int):
        chain.given.add(ident)
    elif kind == "craft" and isinstance(ident, int):
        chain.crafted.add(ident)
    elif kind == "kill" and isinstance(ident, str):
        chain.killed.add(ident)


def _item_label(body: str) -> int:
    if body.startswith("Needs `"):
        return 0
    if body.startswith(
        (
            "Loot ",
            "Kill ",
            "Say ",
            "Hand ",
            "Combine ",
            "Ground ",
            "Common ",
            "No quest",
            "Summon ",
            "Forage ",
            "Fish ",
            "Spawns ",
            "Same ",
            "Gives ",
            "Sets ",
            "Loots ",
            "Hands ",
            "Produces ",
            "Requires ",
            "**",
        )
    ):
        return 0
    if re.match(r"^[a-z0-9]+/\"", body) or re.match(r"^\d+ other ", body):
        return 0
    if "combined in" in body:
        found = _ITEM_AT_END.search(body)
        if not found:
            return 0
        item_id = int(found.group(1))
        return item_id if item_id >= 1000 else 0
    found = _ITEM_AT_END.search(body)
    if not found:
        return 0
    return int(found.group(1))


def _heading_level(line: str) -> int:
    hashes = 0
    for char in line:
        if char != "#":
            break
        hashes += 1
    if hashes < 2 or not line.startswith("#" * hashes + " "):
        return 0
    return hashes


def _parse_notes(text: str, flags: tuple[str, ...]) -> tuple[dict[int, list[Step]], list[_FlagStep]]:
    prereqs: dict[int, list[Step]] = {}
    parsed: list[_FlagStep] = []
    in_prereqs = False
    current_flag = ""
    skip_level = 0
    chain: _Chain | None = None
    step: _FlagStep | None = None
    focus = 0
    inline: dict[int, _Chain] = {}

    def finish_prereq() -> None:
        nonlocal chain
        if chain is None:
            return
        chain = None

    def finish_step() -> None:
        nonlocal step, focus, inline
        if step is None:
            return
        step.inline = {item_id: list(block.steps) for item_id, block in inline.items()}
        parsed.append(step)
        step = None
        focus = 0
        inline = {}

    for raw in text.splitlines():
        line = raw.rstrip()
        level = _heading_level(line)
        if skip_level and level and level <= skip_level:
            skip_level = 0
        elif skip_level:
            continue
        if level and ("Steps on `" in line or line.split(" ", 1)[-1].startswith("Other flags")):
            finish_step()
            finish_prereq()
            skip_level = level
            continue
        flag = _FLAG.match(line)
        if flag and flag.group(2) in flags:
            finish_step()
            finish_prereq()
            in_prereqs = False
            current_flag = flag.group(2)
            continue
        if line.startswith("## 0. Prerequisites"):
            finish_step()
            finish_prereq()
            in_prereqs = True
            current_flag = ""
            continue
        if level == 2 and line.startswith("## "):
            finish_step()
            finish_prereq()
            in_prereqs = False
            current_flag = ""
            continue
        prereq = _PREREQ.match(line) if in_prereqs else None
        if prereq:
            finish_prereq()
            chain = _Chain()
            prereqs[int(prereq.group(2))] = chain.steps
            continue
        if chain is not None:
            numbered = _NUMBERED.match(line)
            if numbered:
                _absorb(numbered.group("body"), chain)
                continue
        step_head = _STEP.match(line)
        if step_head and current_flag:
            finish_step()
            action = step_head.group(4)
            delivers: tuple[int, ...] = ()
            word = ""
            recipe = 0
            if action.startswith("say "):
                word = action[4:].strip().lower()
            elif action.startswith("hand "):
                word = "hail"
                delivers = tuple(int(bit) for bit in action[5:].split("+") if bit.isdigit())
            elif action.startswith("combine recipe "):
                recipe = int(action.rsplit(" ", 1)[-1])
            step = _FlagStep(
                flag=current_flag,
                value=int(step_head.group(2)),
                npc=_npc(step_head.group(3)),
                word=word,
                delivers=delivers,
                recipe=recipe,
                result=0,
                items=[],
                inline={},
            )
            inline = {}
            focus = 0
            continue
        if step is None:
            continue
        if not line.startswith("-") and not line.startswith(" "):
            continue
        body = line.strip()
        if body.startswith("- "):
            body = body[2:]
        label = _item_label(body)
        if label:
            if label not in step.items:
                step.items.append(label)
            focus = label
            inline.setdefault(focus, _Chain())
            continue
        if body.startswith("Produces ") and "no new item" not in body:
            made = _ids(body)
            if made:
                step.result = made[-1]
            continue
        if focus and focus in inline:
            _absorb(body, inline[focus])
    finish_step()
    finish_prereq()
    return prereqs, parsed


def expected_steps(text: str, flags: tuple[str, ...]) -> list[Step]:
    """Flag order, then each step's first obtain chain, then the say, hand-in, or combine."""
    prereqs, parsed = _parse_notes(text, flags)
    order = {flag: index for index, flag in enumerate(flags)}
    chosen: dict[tuple[str, int], _FlagStep] = {}
    for step in parsed:
        chosen.setdefault((step.flag, step.value), step)
    ordered = sorted(chosen.values(), key=lambda step: (order[step.flag], step.value))
    emitted: set[int] = set()
    steps: list[Step] = []
    for step in ordered:
        for item_id in step.items:
            if item_id in emitted:
                continue
            emitted.add(item_id)
            chain = prereqs.get(item_id)
            if chain:
                steps.extend(chain)
            else:
                steps.extend(step.inline.get(item_id, []))
        steps.extend(_step_actions(step))
    return steps


def _step_actions(step: _FlagStep) -> list[Step]:
    if step.recipe:
        token = str(step.result) if step.result else f"recipe:{step.recipe}"
        return [("craft", token)]
    rows: list[Step] = []
    if step.word and not (step.word == "hail" and step.delivers):
        rows.append(("talk", step.npc, step.word))
    for item_id in step.delivers:
        rows.append(("deliver", step.npc, str(item_id)))
    return rows


def _index(graph: QuestGraph) -> dict[str, list[Edge]]:
    found: dict[str, list[Edge]] = {}
    for edge in graph.edges:
        origin = edge.get("from")
        if isinstance(origin, str) and origin:
            found.setdefault(origin, []).append(edge)
        group = edge.get("group")
        if isinstance(group, str) and group and group != origin:
            found.setdefault(group, []).append(edge)
    return found


def _token_item(token: object) -> int:
    if not isinstance(token, str) or not token.startswith("item:"):
        return 0
    raw = token.split(":", 1)[1]
    return int(raw) if raw.isdigit() else 0


def _add(found: list[int], item_id: int) -> None:
    if item_id > 0 and item_id not in found:
        found.append(item_id)


def _flag_edges(graph: QuestGraph, flags: tuple[str, ...]) -> list[Edge]:
    order = {flag: index for index, flag in enumerate(flags)}
    chosen: dict[tuple[str, str], Edge] = {}
    for edge in graph.edges:
        if edge.get("rel") != "sets":
            continue
        flag = edge.get("flag")
        if not isinstance(flag, str) or flag not in order:
            continue
        value = edge.get("value")
        if not isinstance(value, str) or not value.isdigit():
            continue
        origin = edge.get("from")
        if not isinstance(origin, str):
            continue
        chosen.setdefault((flag, value), edge)
    return sorted(
        chosen.values(),
        key=lambda edge: (order[str(edge.get("flag"))], int(str(edge.get("value"))), str(edge.get("from"))),
    )


def _inputs(edge: Edge, indexed: dict[str, list[Edge]]) -> list[int]:
    source = str(edge.get("from") or "")
    found: list[int] = []
    if "#hand:" in source:
        for bit in source.split("#hand:", 1)[1].split("+"):
            if bit.isdigit():
                _add(found, int(bit))
    recipe_at = source.rfind("#recipe:")
    if recipe_at >= 0:
        recipe_id = source[recipe_at + 8 :]
        if recipe_id.isdigit():
            for row in indexed.get(f"recipe:{recipe_id}", []):
                if row.get("rel") == "consumes":
                    _add(found, _token_item(row.get("to")))
                elif row.get("rel") == "container":
                    _add(found, _token_item(row.get("to")))
    for row in indexed.get(source, []):
        if row.get("rel") != "needs":
            continue
        item = row.get("item")
        if isinstance(item, int):
            _add(found, item)
    return found


def _outputs(edge: Edge, indexed: dict[str, list[Edge]]) -> list[int]:
    source = str(edge.get("from") or "")
    found: list[int] = []
    for row in indexed.get(source, []):
        if row.get("rel") == "gives":
            _add(found, _token_item(row.get("to")))
    recipe_at = source.rfind("#recipe:")
    if recipe_at >= 0:
        recipe_id = source[recipe_at + 8 :]
        if recipe_id.isdigit():
            recipe = _recipe_of(indexed, int(recipe_id))
            if recipe is not None:
                _add(found, _fresh(recipe) or recipe.result)
    return found


def _recipe_of(indexed: dict[str, list[Edge]], recipe_id: int) -> Recipe | None:
    rows = indexed.get(f"recipe:{recipe_id}", [])
    if not rows:
        return None
    # _recipe walks graph.edges. The indexed rows are the same edges, so build from them.
    components: list[tuple[int, int]] = []
    results: list[tuple[int, int]] = []
    container = 0
    skill = 0
    name = ""
    for edge in rows:
        rel = edge.get("rel")
        item_id = _token_item(edge.get("to"))
        count = edge.get("count")
        amount = count if isinstance(count, int) and count > 0 else 1
        if rel == "consumes" and item_id:
            components.append((item_id, amount))
        elif rel == "produces" and item_id:
            results.append((item_id, amount))
        elif rel == "container":
            container = _token_item(edge.get("to")) or _world_id(edge.get("to"))
        skill_value = edge.get("skill")
        if isinstance(skill_value, int) and not isinstance(skill_value, bool) and not skill:
            skill = skill_value
        name_value = edge.get("skill_name")
        if isinstance(name_value, str) and not name:
            name = name_value
    if not results:
        return None
    return Recipe(
        id=recipe_id,
        result=results[0][0],
        components=tuple(components),
        container=container,
        results=tuple(results),
        skill=skill,
        name=name,
    )


def _world_id(token: object) -> int:
    if not isinstance(token, str) or not token.startswith("world:"):
        return 0
    raw = token.split(":", 1)[1]
    return int(raw) if raw.isdigit() else 0


def _fresh(recipe: Recipe) -> int:
    used = {item_id for item_id, _count in recipe.components}
    if recipe.container and recipe.container not in _WORLD_CONTAINER:
        used.add(recipe.container)
    fresh = [item_id for item_id, _count in recipe.results if item_id not in used]
    if fresh:
        return fresh[-1]
    if recipe.result and recipe.result not in used:
        return recipe.result
    return 0


def _craft_token(recipe: Recipe) -> str:
    fresh = _fresh(recipe)
    if fresh:
        return str(fresh)
    return f"recipe:{recipe.id}"


def _from_action(action: Action) -> list[Step]:
    if isinstance(action, QuestTalk):
        npc = _npc(action.npc)
        rows: list[Step] = []
        for turn in action.steps:
            if isinstance(turn, Say):
                rows.append(("talk", npc, turn.word.lower()))
            elif isinstance(turn, Hand):
                rows.append(("deliver", npc, str(turn.item)))
        return rows
    if isinstance(action, Talk):
        return [("talk", _npc(action.npc), action.line.lower())]
    if isinstance(action, Deliver):
        return [("deliver", _npc(action.npc), str(action.item))]
    if isinstance(action, Fetch):
        return [("fetch", str(action.item_id))]
    if isinstance(action, Craft):
        return [("craft", _craft_token(action.recipe))]
    if isinstance(action, Kill):
        camp = action.camp if isinstance(action.camp, str) else ""
        return [("kill", camp, "")]
    return []


def _append_step(
    queue: Schedule, world: World, edge: Edge, indexed: dict[str, list[Edge]], graph: QuestGraph
) -> None:
    source = str(edge.get("from") or "")
    npc = _npc(split_npc(source)[1])
    flag = str(edge.get("flag") or "")
    value = str(edge.get("value") or "")
    label = f"epic:{flag}:{value}"
    recipe_at = source.rfind("#recipe:")
    if recipe_at >= 0 and source[recipe_at + 8 :].isdigit():
        recipe = _recipe_of(indexed, int(source[recipe_at + 8 :]))
        if recipe is None:
            return
        made = Craft(recipe)
        made.source = f"{label}#craft:{recipe.id}"
        queue.append(made, world)
        return
    outputs = _outputs(edge, indexed)
    expect = outputs[0] if outputs else 0
    steps = conversation(graph, source, expect)
    if not steps:
        tail = source.split("#", 1)[1] if "#" in source else ""
        if "#holds:" in tail:
            tail = tail.split("#holds:", 1)[0]
        if tail.startswith("hand:"):
            steps = tuple(Hand(int(bit)) for bit in tail[5:].split("+") if bit.isdigit())
        else:
            steps = (Say(tail or "hail"),)
    if not steps:
        return
    talk = QuestTalk(npc, steps, expect=expect)
    said = [turn.word for turn in steps if isinstance(turn, Say)]
    talk.source = f"{label}#say:{npc}:{said[0]}" if said else f"{label}#hand:{npc}"
    queue.append(talk, world)


def queued_steps(graph: QuestGraph, flags: tuple[str, ...]) -> list[Step]:
    """Append each flag step's items through produce, then the step, in flag order."""
    world = World(name="Mockone", zone="")
    queue = Schedule()
    loop = Loop()
    loop.queue = queue
    loop.character = "Mockone"
    loop.world = world
    indexed = _index(graph)
    got: set[int] = set()
    for edge in _flag_edges(graph, flags):
        for item_id in _inputs(edge, indexed):
            if item_id in got:
                continue
            produce(loop, world, item_id=item_id, graph=graph)
            got.add(item_id)
        _append_step(queue, world, edge, indexed, graph)
        for item_id in _outputs(edge, indexed):
            got.add(item_id)
    steps: list[Step] = []
    for action in queue:
        steps.extend(_from_action(action))
    return steps


def _show(rows: list[Step], start: int, stop: int) -> str:
    shown = []
    for offset, row in enumerate(rows[start:stop]):
        shown.append(f"  {start + offset}: {' '.join(row)}")
    return "\n".join(shown)


def assert_same_order(name: str, expected: list[Step], actual: list[Step]) -> None:
    if expected == actual:
        return
    length = min(len(expected), len(actual))
    index = length
    for cursor in range(length):
        if expected[cursor] != actual[cursor]:
            index = cursor
            break
    start = max(0, index - 3)
    stop = index + 12
    raise AssertionError(
        f"{name} epic actions are not in the markdown order\n"
        f"markdown has {len(expected)} steps, the queue has {len(actual)}, first difference at {index}\n"
        f"markdown:\n{_show(expected, start, stop)}\n"
        f"queue:\n{_show(actual, start, stop)}"
    )


@pytest.fixture(scope="module")
def quest_graph() -> QuestGraph:
    if not _GRAPH.is_file():
        pytest.skip("quest graph is not built")
    return load_graph(_GRAPH)


@pytest.mark.parametrize(
    ("name", "flags"),
    [
        ("warrior", ("warrior_pre", "warrior_epic")),
        ("enchanter", ("EnchPre", "ench_epic")),
    ],
    ids=("warrior", "enchanter"),
)
def test_epic_queue_matches_the_markdown(
    name: str,
    flags: tuple[str, ...],
    quest_graph: QuestGraph,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    notes = _EPICS / f"{name}.md"
    if not notes.is_file():
        pytest.skip(f"{notes} is missing")
    monkeypatch.setattr("eqclient3.quests.produce._is_reward", lambda _graph, _item_id: False)
    expected = expected_steps(notes.read_text(encoding="utf-8"), flags)
    actual = queued_steps(quest_graph, flags)
    assert expected, f"{name} markdown produced no steps"
    assert actual, f"{name} quest graph queued no steps"
    assert_same_order(name, expected, actual)
