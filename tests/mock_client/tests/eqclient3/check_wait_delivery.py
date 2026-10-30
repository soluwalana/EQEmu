"""Every action wait must be paired with the opcode that releases it.

The bus mails a packet to an action only when that action lists the opcode.
A wait that returns while its mailbox is empty deadlocks when the reply opcode
is missing from that list. The handler that owns the opcode is the reply.
A session packet with no handler still arrives, and the pair names the bus.
"""
from __future__ import annotations

import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / "eqclient3"
ACTIONS = ROOT / "actions"
HANDLERS = ROOT / "handlers"
BUS = ROOT / "bus.py"
MOVEMENT = ROOT / "movement.py"
ACTION_BASE = ROOT / "action.py"


def _strings(node: ast.AST) -> set[str]:
    found: set[str] = set()
    for child in ast.walk(node):
        if isinstance(child, ast.Constant) and isinstance(child.value, str) and child.value.startswith("OP_"):
            found.add(child.value)
    return found


def _consumes(node: ast.AST) -> set[str]:
    found: set[str] = set()
    for child in ast.walk(node):
        if isinstance(child, ast.Call) and isinstance(child.func, ast.Attribute) and child.func.attr == "consume":
            if child.args and isinstance(child.args[0], ast.Constant) and isinstance(child.args[0].value, str):
                found.add(child.args[0].value)
    return found


def _tokens(node: ast.AST) -> set[str]:
    found: set[str] = set()
    for child in ast.walk(node):
        if isinstance(child, ast.Call) and isinstance(child.func, ast.Attribute) and child.func.attr in ("wait", "unwait", "waiting_for"):
            if child.args and isinstance(child.args[0], ast.Constant) and isinstance(child.args[0].value, str):
                found.add(child.args[0].value)
        if isinstance(child, ast.Assign):
            for target in child.targets:
                if isinstance(target, ast.Attribute) and target.attr == "waiting" and isinstance(child.value, ast.Constant) and isinstance(child.value.value, str):
                    found.add(child.value.value)
        if isinstance(child, ast.Compare):
            sides = [child.left, *child.comparators]
            attrs = [side.attr for side in sides if isinstance(side, ast.Attribute)]
            constants = [side.value for side in sides if isinstance(side, ast.Constant) and isinstance(side.value, str)]
            if "waiting" in attrs:
                found.update(constants)
    found.discard("")
    return found


def _self_calls(node: ast.AST) -> set[str]:
    found: set[str] = set()
    for child in ast.walk(node):
        if not isinstance(child, ast.Call) or not isinstance(child.func, ast.Attribute):
            continue
        owner = child.func.value
        if isinstance(owner, ast.Name) and owner.id == "self":
            found.add(child.func.attr)
        if isinstance(owner, ast.Call) and isinstance(owner.func, ast.Name) and owner.func.id == "super" and child.func.attr == "step":
            found.add("super.step")
    return found


def _reads_text(node: ast.AST) -> bool:
    for child in ast.walk(node):
        if isinstance(child, ast.Attribute) and child.attr in ("messages", "text"):
            return True
        if isinstance(child, ast.Name) and child.id in ("message_text", "task_text_satisfied"):
            return True
        if isinstance(child, ast.Attribute) and child.attr in ("message_text", "task_text_satisfied"):
            return True
    return False


def _methods(node: ast.ClassDef) -> dict[str, ast.FunctionDef]:
    return {item.name: item for item in node.body if isinstance(item, ast.FunctionDef)}


def _closure(start: str, methods: dict[str, ast.FunctionDef]) -> list[ast.FunctionDef]:
    seen: list[ast.FunctionDef] = []
    pending = [start]
    names: set[str] = set()
    while pending:
        name = pending.pop()
        if name in names or name not in methods:
            continue
        names.add(name)
        method = methods[name]
        seen.append(method)
        for called in _self_calls(method):
            if called not in names:
                pending.append(called)
    return seen


def _classes(path: Path) -> list[tuple[str, ast.ClassDef]]:
    tree = ast.parse(path.read_text())
    return [(node.name, node) for node in tree.body if isinstance(node, ast.ClassDef)]


def handler_owners() -> dict[str, str]:
    """Opcode -> handler class that receives it. Movement is included."""
    owned: dict[str, str] = {}
    for path in sorted(HANDLERS.glob("*.py")):
        for name, node in _classes(path):
            for item in node.body:
                if isinstance(item, ast.Assign):
                    for target in item.targets:
                        if isinstance(target, ast.Name) and target.id == "opcodes":
                            for opcode in _strings(item.value):
                                owned.setdefault(opcode, name)
    movement = ast.parse(MOVEMENT.read_text())
    for node in movement.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "OPCODES":
                    for opcode in _strings(node.value):
                        owned.setdefault(opcode, "movement")
    return owned


def _message_opcodes(owners: dict[str, str]) -> set[str]:
    return {opcode for opcode, owner in owners.items() if owner == "MessagesHandler"}


def _called_names(node: ast.AST) -> set[str]:
    found: set[str] = set()
    for child in ast.walk(node):
        if isinstance(child, ast.Call) and isinstance(child.func, ast.Name):
            found.add(child.func.id)
    return found


def _helper_consumes() -> dict[str, set[str]]:
    """consume() opcodes inside action helpers the class calls by name."""
    tree = ast.parse((ACTIONS / "support.py").read_text())
    found: dict[str, set[str]] = {}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            found[node.name] = _consumes(node)
    return found


def action_waits() -> list[tuple[str, str, set[str], set[str]]]:
    """(class, token, listed opcodes, reply opcodes)."""
    owners = handler_owners()
    messages = _message_opcodes(owners)
    helpers = _helper_consumes()
    rows: list[tuple[str, str, set[str], set[str]]] = []
    paths = [ACTION_BASE, *sorted(ACTIONS.rglob("*.py"))]
    for path in paths:
        if path.name == "__init__.py":
            continue
        for name, node in _classes(path):
            if name == "Action":
                continue
            methods = _methods(node)
            listed: set[str] = set()
            if "opcodes" in methods:
                listed = _strings(methods["opcodes"])
            mentioned: dict[str, set[str]] = {}
            for method_name, method in methods.items():
                if method_name == "opcodes":
                    continue
                for token in _tokens(method):
                    mentioned.setdefault(token, set()).add(method_name)
            if "super.step" in {call for method in methods.values() for call in _self_calls(method)} or "TARGET" in mentioned:
                mentioned.setdefault("TARGET", set()).add("step")
            for token, starters in sorted(mentioned.items()):
                body: list[ast.FunctionDef] = []
                for starter in starters:
                    body.extend(_closure(starter, methods))
                replies: set[str] = set()
                reads = False
                for method in body:
                    replies |= _consumes(method)
                    reads = reads or _reads_text(method)
                    for called in _called_names(method):
                        replies |= helpers.get(called, set())
                if token == "TARGET" or any("super.step" in _self_calls(method) for method in body):
                    replies.add("OP_Consider")
                if reads:
                    replies |= listed & messages
                rows.append((name, token, listed, replies))
    rows.append(_door_wait(owners))
    return rows


def _door_wait(owners: dict[str, str]) -> tuple[str, str, set[str], set[str]]:
    del owners
    movement = ast.parse(MOVEMENT.read_text())
    listed: set[str] = set()
    for node in movement.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "OPCODES":
                    listed |= _strings(node.value)
    return ("movement", "DOOR", listed, {"OP_MoveDoor"})


def pairs() -> list[tuple[str, str, str, str]]:
    """Action, wait token, reply opcode, handler or bus."""
    owners = handler_owners()
    found: list[tuple[str, str, str, str]] = []
    for name, token, _listed, replies in action_waits():
        for opcode in sorted(replies):
            found.append((name, token, opcode, owners.get(opcode, "bus")))
    return found


def gaps() -> list[str]:
    problems: list[str] = []
    bus = BUS.read_text()
    if "add_message(Message(parsed))" not in bus:
        problems.append("bus.publish does not mail a decoded object to subscribers")
    messages = (HANDLERS / "messages.py").read_text()
    if "exclusive = opcodes" not in messages:
        problems.append("messages does not claim its opcodes")
    simple = messages.split("def simple(", 1)[-1].split("\n    def ", 1)[0]
    hand_at = simple.find("deliver_waiters(")
    for name in ("TOO_FAR", "DEEDS", "WONT_SELL", "WORST"):
        branch = simple.find(name)
        if branch < 0 or hand_at < 0 or hand_at > branch:
            problems.append(f"messages.simple returns through {name} before deliver_waiters")
    if "opcode in handler.exclusive" not in bus:
        problems.append("bus.publish still mails an opcode a handler claimed")
    door = MOVEMENT.read_text().split("def _on_move_door", 1)[-1].split("\ndef ", 1)[0]
    opened = door.find("open_ids.add")
    empty = door.find("if not payload")
    if opened < 0 or (empty >= 0 and opened < empty):
        problems.append("movement door wait returns before recording OP_MoveDoor")
    seen: set[tuple[str, str]] = set()
    for name, token, listed, replies in action_waits():
        seen.add((name, token))
        if not replies:
            problems.append(f"{name} waits on {token} and consumes no reply")
            continue
        for opcode in sorted(replies):
            if opcode not in listed:
                problems.append(f"{name} waits on {token} for {opcode} and does not list it")
    required = {
        "TARGET", "CURSOR", "HAIL", "CAST", "HEAL", "CURE", "SCRIBE", "TRAIN",
        "TRADE", "LOOT", "ZONE", "CRAFT", "SUMMON", "BOT", "DOOR",
    }
    have = {token for _name, token in seen}
    for token in sorted(required - have):
        problems.append(f"no action wait named {token}")
    return problems


def main() -> int:
    found = gaps()
    if found:
        print("\n".join(found))
        return 1
    for action, token, opcode, owner in pairs():
        print(f"{action} {token} <- {opcode} ({owner})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
