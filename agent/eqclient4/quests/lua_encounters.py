"""Conservative, cross-file Lua encounter extraction for EQEmu quest graphs.

This module does not execute Lua. It recognizes concrete event registrations, branch
predicates, action calls and a bounded set of local helpers. A conditional loot
producer is exported only when its owner's spawn callback is reachable through an
explicit player action and the encounter's event lifecycle. Unknown predicates are
retained as guards; unknown callbacks / dynamic NPC ids are diagnostics, never roots.

Inputs use zone-relative filenames (``encounters/foo.lua``, ``player.lua``).
The returned edges use QuestGraph's existing rel/from/to/group vocabulary.
"""

from __future__ import annotations

import re
from collections import defaultdict, deque
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Registration:
    owner: str
    event: str
    npc: int | None
    callback: str
    source: str


@dataclass(frozen=True)
class Effect:
    kind: str
    value: int | str
    guards: tuple[str, ...]
    line: int
    receiver: str = ""
    alternatives: tuple[int, ...] = ()


@dataclass
class Callback:
    registration: Registration
    effects: list[Effect] = field(default_factory=list)


@dataclass
class EncounterAnalysis:
    edges: list[dict] = field(default_factory=list)
    diagnostics: list[str] = field(default_factory=list)
    owned_files: set[str] = field(default_factory=set)
    produced_items: set[int] = field(default_factory=set)
    cleared_npcs: set[int] = field(default_factory=set)


# Strip comments without breaking string literals. Keep newlines and positions.
def _without_comments(source: str) -> str:
    pattern = re.compile(
        r"""--\[\[.*?\]\]|--[^\n]*|"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*' """, re.DOTALL | re.VERBOSE
    )

    def replace(match: re.Match[str]) -> str:
        value = match.group()
        if value.startswith("--"):
            return "".join("\n" if ch == "\n" else " " for ch in value)
        return value

    return pattern.sub(replace, source)


def _calls(line: str, function: str) -> list[str]:
    """Balanced argument lists for a literal function name on one line."""
    result: list[str] = []
    for match in re.finditer(re.escape(function) + r"\s*\(", line):
        start = match.end()
        depth = 1
        quote = ""
        escape = False
        for i in range(start, len(line)):
            ch = line[i]
            if quote:
                if escape:
                    escape = False
                elif ch == "\\":
                    escape = True
                elif ch == quote:
                    quote = ""
                continue
            if ch in "\"'":
                quote = ch
            elif ch == "(":
                depth += 1
            elif ch == ")":
                depth -= 1
                if depth == 0:
                    result.append(line[start:i])
                    break
    return result


def _args(value: str) -> list[str]:
    parts: list[str] = []
    depth = 0
    quote = ""
    start = 0
    escape = False
    for i, ch in enumerate(value):
        if quote:
            if escape:
                escape = False
            elif ch == "\\":
                escape = True
            elif ch == quote:
                quote = ""
        elif ch in "\"'":
            quote = ch
        elif ch in "({[":
            depth += 1
        elif ch in ")}]":
            depth -= 1
        elif ch == "," and depth == 0:
            parts.append(value[start:i].strip())
            start = i + 1
    parts.append(value[start:].strip())
    return parts


def _literal(value: str) -> str:
    value = value.strip()
    return value[1:-1] if len(value) >= 2 and value[0] in "\"'" and value[-1] == value[0] else value


def _number(value: str) -> int | None:
    return int(value) if re.fullmatch(r"\d+", value.strip()) else None


@dataclass(frozen=True)
class _Function:
    name: str
    statements: tuple[tuple[int, str, tuple[str, ...]], ...]
    params: tuple[str, ...] = ()


def _function_params(fn_source: _Function) -> tuple[str, ...]:
    return fn_source.params


def _functions(text: str) -> dict[str, _Function]:
    """Track block ownership and guards (including nested anonymous functions).

    Intentionally conservative: unrecognized multiline syntax is left as a raw
    predicate. This is a statement scanner, not a general Lua parser.
    """
    code = _without_comments(text)
    functions: dict[str, _Function] = {}
    current: str | None = None
    statements: list[tuple[int, str, tuple[str, ...]]] = []
    params: tuple[str, ...] = ()
    frames: list[tuple[str, str]] = []
    for line_no, raw in enumerate(code.splitlines(), 1):
        line = raw.strip()
        if not line:
            continue
        definition = re.match(r"(?:local\s+)?function\s+([\w.:]+)\s*\(", line)
        if definition and current is None:
            current = definition.group(1)
            signature = re.search(r"\(([^)]*)\)", line[definition.end() - 1 :])
            params = (
                tuple(x.strip() for x in signature.group(1).split(",") if x.strip())
                if signature
                else ()
            )
            frames = [("function", "")]
            statements = []
            continue
        if current is None:
            continue
        # A line may end one branch and begin another.
        if re.match(r"^end\b", line):
            if frames:
                frames.pop()
            if not frames:
                functions[current] = _Function(current, tuple(statements), params)
                current = None
                continue
        if re.match(r"^until\b", line):
            if frames and frames[-1][0] == "repeat":
                frames.pop()
        elif re.match(r"^else\b", line):
            if frames and frames[-1][0] == "if":
                frames[-1] = ("if", "not (" + frames[-1][1] + ")")
        elif re.match(r"^elseif\b", line):
            if frames and frames[-1][0] == "if":
                condition = re.sub(r"^elseif\s+|\s+then\b.*$", "", line)
                frames[-1] = ("if", condition)
        guards = tuple(guard for kind, guard in frames if kind == "if" and guard)
        # Effects on a single-line conditional must not escape its predicate.
        one_line = re.match(r"^if\s+(.+?)\s+then\s+(.+?)\s+end\s*;?$", line)
        if one_line:
            guards += (one_line.group(1),)
        statements.append((line_no, line, guards))
        if re.search(r"\bfunction\s*\(", line) and not definition:
            frames.append(("function", ""))
        # Branch openers with a closing 'end' on the same line are handled as opaque.
        if re.match(r"^if\b.*\bthen\b", line) and not re.search(r"\bthen\b.*\bend\s*[;)]?$", line):
            condition = re.sub(r"^if\s+|\s+then\b.*$", "", line)
            frames.append(("if", condition))
        elif re.match(r"^(?:for|while)\b.*\bdo\b", line):
            frames.append(("loop", line))
        elif re.match(r"^repeat\b", line):
            frames.append(("repeat", ""))
        elif re.match(r"^do\b", line):
            frames.append(("do", ""))
    return functions


def _registrations(
    path: str,
    code: str,
    symbols: tuple[dict[str, str], dict[str, dict[str, str]]] | None = None,
) -> list[Registration]:
    found: list[Registration] = []
    scalars, tables = symbols if symbols is not None else _symbols(code)
    # Registration syntax occurs with and without encounter name, in live ProjectEQ.
    for func, owner_type in (
        ("eq.register_npc_event", "npc"),
        ("eq.register_player_event", "player"),
    ):
        for call in _calls(_without_comments(code), func):
            parts = _args(call)
            if parts and parts[0].startswith(('"', "'")):
                parts = parts[1:]
            if not parts or not re.fullmatch(r"Event\.\w+", parts[0]):
                continue
            event = parts[0].split(".", 1)[1].lower()
            if owner_type == "npc" and len(parts) >= 3:
                for npc in _resolve_ids(parts[1], scalars, tables):
                    found.append(Registration(path, event, npc, parts[2], path))
            elif owner_type == "player" and len(parts) >= 2:
                found.append(Registration(path, event, None, parts[1], path))
    # Event registrations frequently appear inside finite pairs()/ipairs()
    # loops (MPG Corruption registers every class-specific mob this way).
    # The ordinary expression resolver cannot see the loop's value alias.
    # Resolve it against the literal collection without executing Lua.
    clean = _without_comments(code)
    for loop in re.finditer(
        r"for\s+\w+\s*,\s*(\w+)\s+in\s+(?:pairs|ipairs)\s*" r"\(\s*(\w+)\s*\)\s+do(.*?)\n\s*end\b",
        clean,
        re.DOTALL,
    ):
        var, collection, body = loop.groups()
        context = dict(scalars)
        context[var] = f"{collection}[math.random(1,#{collection})]"
        for call in _calls(body, "eq.register_npc_event"):
            parts = _args(call)
            if parts and parts[0].startswith(('"', "'")):
                parts = parts[1:]
            if len(parts) < 3 or not re.fullmatch(r"Event\.\w+", parts[0]):
                continue
            for npc in _resolve_ids(parts[1], context, tables):
                reg = Registration(path, parts[0].split(".", 1)[1].lower(), npc, parts[2], path)
                if reg not in found:
                    found.append(reg)
    return found


def _event_node(zone: str, reg: Registration) -> str:
    if reg.npc is None:
        return f"{zone}/player#event:{reg.event}"
    return f"{zone}/npc:{reg.npc}#event:{reg.event}:{reg.npc}"


def _spawn_ids(expression: str) -> tuple[int, ...]:
    """Statically enumerate literal spawn alternatives, never arbitrary expressions."""
    single = _number(expression)
    if single is not None:
        return (single,)
    match = re.fullmatch(
        r"eq\.(?:ChooseRandom|choose_random)\s*\((.*)\)", expression.strip(), re.DOTALL
    )
    if not match:
        return ()
    values = [_number(arg) for arg in _args(match.group(1))]
    return (
        tuple(dict.fromkeys(v for v in values if v is not None))
        if all(v is not None for v in values)
        else ()
    )


# A bounded symbolic domain: each expression resolves to a finite set of NPC IDs
# or stays unknown. This deliberately does not evaluate arbitrary Lua.
_IDENTIFIER = re.compile(r"[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*")


def _balanced(text: str, pos: int, opening: str = "{") -> tuple[str, int] | None:
    closing = {"{": "}", "[": "]", "(": ")"}[opening]
    depth = 0
    quote = ""
    escape = False
    for i in range(pos, len(text)):
        ch = text[i]
        if quote:
            if escape:
                escape = False
            elif ch == chr(92):
                escape = True
            elif ch == quote:
                quote = ""
        elif ch in ('"', "'"):
            quote = ch
        elif ch == opening:
            depth += 1
        elif ch == closing:
            depth -= 1
            if depth == 0:
                return text[pos + 1 : i], i + 1
    return None


def _table_entries(text: str) -> dict[str, str]:
    """Read simple Lua array / keyed-table entries without interpreting code."""
    rows = _args(text)
    result: dict[str, str] = {}
    index = 0
    for row in rows:
        m = re.match(r"^\s*(?:\[\s*([^]]+)\s*\]|([A-Za-z_]\w*))\s*=\s*(.*)$", row, re.DOTALL)
        if m:
            key = (m.group(1) or m.group(2)).strip().strip("\"'")
            result[key] = m.group(3).strip()
        elif row.strip():
            index += 1
            result[str(index)] = row.strip()
    return result


def _symbols(code: str) -> tuple[dict[str, str], dict[str, dict[str, str]]]:
    """Capture literal scalar and table assignments, including multiline tables."""
    clean = _without_comments(code)
    scalars: dict[str, str] = {}
    tables: dict[str, dict[str, str]] = {}
    pattern = re.compile(r"(?m)^\s*(?:local\s+)?([A-Za-z_]\w*)\s*=\s*")
    for m in pattern.finditer(clean):
        name = m.group(1)
        at = m.end()
        if at < len(clean) and clean[at] == "{":
            chunk = _balanced(clean, at)
            if chunk:
                tables[name] = _table_entries(chunk[0])
        else:
            line = (
                clean[at : clean.find("\n", at) if "\n" in clean[at:] else len(clean)]
                .strip()
                .rstrip(";")
            )
            # Only bounded, simple expressions; prefer no inference to a wrong ID.
            if line and not re.search(r"\b(?:if|then|end|return)\b", line):
                scalars[name] = line
    return scalars, tables


def _resolve_ids(
    expr: str,
    scalars: dict[str, str],
    tables: dict[str, dict[str, str]],
    depth: int = 0,
    seen: frozenset[str] = frozenset(),
    functions: dict[str, _Function] | None = None,
    context: dict[str, str] | None = None,
    self_npc: int | None = None,
) -> tuple[int, ...]:
    """Finite, non-executing Lua expression evaluation for NPC IDs.

    Supports nested array/table selectors, local aliases, bounded random
    indices, and literal-return helpers. Unknown values contribute no IDs.
    The result is a *may* set, not an assertion that every candidate spawns.
    """
    context = context or {}

    def eval_expr(value: str, level: int, trail: frozenset[str]) -> list[str]:
        if level > 14:
            return []
        value = value.strip().rstrip(";")
        if not value or value in trail:
            return []
        trail = trail | {value}
        if value.isdecimal() or value == "nil":
            return [value]
        if value == "e.self:GetNPCTypeID()":
            return [str(self_npc)] if self_npc is not None else []
        if value.startswith("{"):
            chunk = _balanced(value, 0)
            if chunk and not value[chunk[1] :].strip():
                return [value]
        choose = re.fullmatch(r"eq\.(?:ChooseRandom|choose_random)\s*\((.*)\)", value, re.DOTALL)
        if choose:
            return [v for arg in _args(choose.group(1)) for v in eval_expr(arg, level + 1, trail)]
        helper = re.fullmatch(r"([A-Za-z_]\w*)\s*\(\s*\)", value)
        if helper and functions and helper.group(1) in functions:
            fn = functions[helper.group(1)]
            env = dict(context)
            output = []
            for _, line, _ in fn.statements:
                assignment = re.match(r"(?:local\s+)?([A-Za-z_]\w*)\s*=\s*(.*)", line)
                if assignment:
                    env[assignment.group(1)] = assignment.group(2).strip().rstrip(";")
                ret = re.match(r"^return\s+(.+?)\s*;?$", line)
                if ret:
                    output.extend(_resolve_values(ret.group(1), env, level + 1, trail))
            return output
        return _resolve_values(value, context, level, trail)

    def _resolve_values(
        value: str, env: dict[str, str], level: int, trail: frozenset[str]
    ) -> list[str]:
        # Resolve a dotted/bracketed chain starting at a symbol. All suffixes
        # are interpreted on the *selected* table, not on the outer table.
        match = re.match(r"^([A-Za-z_]\w*)", value)
        if not match:
            return []
        root = match.group(1)
        if root in env:
            roots = eval_expr(env[root], level + 1, trail) if env[root] != value else []
        elif root in scalars:
            roots = eval_expr(scalars[root], level + 1, trail)
        elif root in tables:
            roots = ["{" + ",".join(f"[{k}]={v}" for k, v in tables[root].items()) + "}"]
        else:
            return []
        tail = value[match.end() :].strip()
        while tail:
            if tail.startswith("."):
                key = re.match(r"^\.([A-Za-z_]\w*)", tail)
                if not key:
                    return []
                selector = key.group(1)
                tail = tail[key.end() :].strip()
                dynamic = False
            elif tail.startswith("["):
                chunk = _balanced(tail, 0, "[")
                if not chunk:
                    return []
                index = chunk[0].strip()
                tail = tail[chunk[1] :].strip()
                index_vals = eval_expr(index, level + 1, trail)
                # math.random or runtime integer indexing is a finite union
                # of the table's entries; never interpret the index as an ID.
                dynamic = not index_vals or not all(x.isdecimal() for x in index_vals)
                selector = index_vals if not dynamic else []
            else:
                return []
            next_values: list[str] = []
            for node in roots:
                if not node.startswith("{"):
                    continue
                chunk = _balanced(node, 0)
                if not chunk:
                    continue
                entries = _table_entries(chunk[0])
                if dynamic:
                    next_values.extend(entries.values())
                else:
                    for k in ([selector] if isinstance(selector, str) else selector):
                        if str(k) in entries:
                            next_values.append(entries[str(k)])
            roots = [x for node in next_values for x in eval_expr(node, level + 1, frozenset())]
        return roots

    values = eval_expr(expr, depth, seen)
    return tuple(dict.fromkeys(int(v) for v in values if v.isdecimal() and int(v) > 0))


def _effects(
    function: _Function,
    symbols: tuple[dict[str, str], dict[str, dict[str, str]]] | None = None,
    functions: dict[str, _Function] | None = None,
    context: dict[str, str] | None = None,
    self_npc: int | None = None,
) -> list[Effect]:
    """Collect directly attributable operations with their local branch predicates."""
    found: list[Effect] = []
    aliases: dict[str, tuple[int, ...]] = {}
    scalars, tables = symbols if symbols is not None else ({}, {})
    # Include function-local scalar assignments without treating the assignment
    # as unconditional proof of its guarded branch.
    local_scalars = dict(scalars)
    if context:
        local_scalars.update(context)
    for number, line, guards in function.statements:
        # Loop aliases are finite sets of the traversed collection. Retain the
        # symbolic table path so nested selectors (guard.npcs, etc.) work.
        loop = re.match(r"for\s+(.+?)\s+in\s+(?:ipairs|pairs)\s*\((.*?)\)\s+do", line)
        if loop:
            variables = [v.strip() for v in loop.group(1).split(",")]
            variable = variables[-1]
            if variable != "_":
                local_scalars[variable] = f"{loop.group(2)}[math.random(1,#{loop.group(2)})]"
        assignment = re.match(r"(?:local\s+)?([A-Za-z_]\w*)\s*=\s*(.*)$", line)
        if assignment and not assignment.group(2).startswith("eq.spawn"):
            candidate = assignment.group(2).strip().rstrip(";")
            local_scalars[assignment.group(1)] = candidate
        # Spawn handles may be assigned to local variables before AddItem.
        assign = re.match(r"(?:local\s+)?(\w+)\s*=\s*eq\.(?:spawn2|unique_spawn|spawn)\s*\(", line)
        if assign:
            op = re.search(r"eq\.(?:spawn2|unique_spawn|spawn)", line)
            if op:
                calls = _calls(line, op.group())
                if calls:
                    values = _resolve_ids(
                        _args(calls[0])[0],
                        local_scalars,
                        tables,
                        functions=functions,
                        self_npc=self_npc,
                    )
                    if values:
                        aliases[assign.group(1)] = values

        for op1 in ("eq.spawn2", "eq.unique_spawn", "eq.spawn"):
            for arguments in _calls(line, op1):
                args = _args(arguments)
                if not args:
                    continue
                choices = _resolve_ids(
                    args[0], local_scalars, tables, functions=functions, self_npc=self_npc
                )
                if not choices:
                    found.append(Effect("unresolved_spawn", args[0], guards, number, op1))
                for npc in choices:
                    found.append(Effect("spawn", npc, guards, number, alternatives=choices))

        for op2, kind in (
            ("eq.set_timer", "timer"),
            ("eq.signal", "signal"),
            ("eq.set_next_hp_event", "hp"),
            ("eq.spawn_condition", "spawn_condition"),
            ("eq.set_global", "set_flag"),
            ("eq.target_global", "set_flag"),
            ("eq.depop", "depop"),
            ("eq.depop_all", "depop"),
            ("eq.stop_timer", "stop_timer"),
            ("eq.stop_all_timers", "stop_all_timers"),
        ):
            for arguments in _calls(line, op2):
                args = _args(arguments)
                if not args:
                    if kind in {"depop", "stop_all_timers"}:
                        found.append(Effect(kind, "*", guards, number))
                    continue
                key = _literal(args[0])
                if kind == "signal" and len(args) > 1:
                    key = f"{key}:{_literal(args[1])}"
                if kind == "spawn_condition" and len(args) >= 4:
                    key = ":".join(_literal(a) for a in (args[0], args[2], args[3]))
                found.append(Effect(kind, key, guards, number))

        for match in re.finditer(
            r"((?:e\.(?:self|corpse|killed)|\w+)(?::CastToNPC\(\))?)\s*:\s*AddItem\s*\(\s*(\d+)",
            line,
        ):
            receiver = match.group(1)
            bare = receiver.split(":", 1)[0]
            receivers = aliases.get(bare)
            if receivers:
                for npc in receivers:
                    found.append(
                        Effect(
                            "add_item",
                            int(match.group(2)),
                            guards,
                            number,
                            str(npc),
                            alternatives=receivers,
                        )
                    )
            else:
                found.append(Effect("add_item", int(match.group(2)), guards, number, receiver))
        for match in re.finditer(r'\b(?:e\.self|\w+)\s*:\s*DelGlobal\s*\(\s*["\']([^"\']+)', line):
            found.append(Effect("delete_flag", match.group(1), guards, number))
        for match in re.finditer(r'\be\.message:findi\s*\(\s*["\']([^"\']+)', line):
            found.append(Effect("say", match.group(1).lower(), guards, number))
        if re.search(r"SetSpecialAbility\s*\(|SetLocked\s*\(", line):
            found.append(Effect("activate", "encounter", guards, number))
    return found


def _expand_effects(
    name: str,
    functions: dict[str, _Function],
    stack: frozenset[str] = frozenset(),
    inherited_guards: tuple[str, ...] = (),
    symbols: tuple[dict[str, str], dict[str, dict[str, str]]] | None = None,
    context: dict[str, str] | None = None,
    self_npc: int | None = None,
) -> list[Effect]:
    """Inline bounded, direct calls to local Lua helpers, preserving caller guards.

    Recursive / unresolved calls are intentionally not evaluated. A helper
    reached through a guarded branch must inherit that branch's conditions.
    """
    if name in stack or name not in functions or len(stack) >= 8:
        return []
    fn = functions[name]
    direct = _effects(fn, symbols, functions, context, self_npc)
    expanded = [
        Effect(e.kind, e.value, inherited_guards + e.guards, e.line, e.receiver, e.alternatives)
        for e in direct
    ]
    known = set(functions) - {name}
    local_env = dict(context or {})
    for _line, statement, guards in fn.statements:
        assign = re.match(r"(?:local\s+)?([A-Za-z_]\w*)\s*=\s*(.*)$", statement)
        if assign:
            local_env[assign.group(1)] = assign.group(2).strip().rstrip(";")
        # Avoid matching method / namespace calls, or function declarations.
        if re.match(r"^(?:local\s+)?function\b", statement):
            continue
        for call in re.finditer(r"(?<![\w.:])([A-Za-z_]\w*)\s*\(", statement):
            callee = call.group(1)
            if callee in known and callee not in stack:
                args = _calls(statement, callee)
                params = _function_params(fn_source=functions[callee])
                mapped = dict(local_env)
                if args:
                    for parameter, argument in zip(params, _args(args[0])):
                        mapped[parameter] = local_env.get(argument.strip(), argument.strip())
                expanded.extend(
                    _expand_effects(
                        callee,
                        functions,
                        stack | {name},
                        inherited_guards + guards,
                        symbols,
                        mapped,
                        self_npc,
                    )
                )
    return expanded


def _flag_guards(guards: tuple[str, ...]) -> list[tuple[str, str, str]]:
    found: list[tuple[str, str, str]] = []
    for cond in guards:
        for match in re.finditer(
            r'(?P<target>e\.self|client|v|\w+)\s*:\s*GetGlobal\s*\(\s*["\'](?P<name>[^"\']+)["\']\s*\)\s*==\s*["\']?(?P<value>\w+)',
            cond,
        ):
            subject = "player" if match["target"] == "e.self" else "any_client"
            found.append((match["name"], match["value"], subject))
    return found


def _scoped(effect: Effect, kind: str, value: str) -> bool:
    """Match an effect to the enclosing SAY, timer or signal branch."""
    for guard in effect.guards:
        if kind == "say" and re.search(
            r'e\.message:findi\s*\(\s*["\']' + re.escape(value) + r'["\']', guard, re.IGNORECASE
        ):
            return True
        if kind == "timer" and re.search(
            r'e\.timer\s*==\s*["\']' + re.escape(value) + r'["\']', guard
        ):
            return True
        if kind == "signal" and re.search(r"e\.signal\s*==\s*" + re.escape(value) + r"\b", guard):
            return True
    return False


def _separate_branches(callbacks: list[Callback]) -> list[Callback]:
    """Timer and signal handlers must not merge mutually exclusive branches."""
    result: list[Callback] = []
    for cb in callbacks:
        event = cb.registration.event
        if event == "say":
            values = list(dict.fromkeys(str(e.value) for e in cb.effects if e.kind == "say"))
        elif event == "timer":
            values = list(
                dict.fromkeys(
                    m.group(1)
                    for e in cb.effects
                    for cond in e.guards
                    for m in re.finditer(r'e\.timer\s*==\s*["\']([^"\']+)', cond)
                )
            )
        elif event == "signal":
            values = list(
                dict.fromkeys(
                    m.group(1)
                    for e in cb.effects
                    for cond in e.guards
                    for m in re.finditer(r"e\.signal\s*==\s*(\d+)", cond)
                )
            )
        else:
            result.append(cb)
            continue
        if not values:
            # Unpartitioned callbacks remain distinct but aren't automatically
            # promoted from another value-specific event.
            result.append(cb)
            continue
        for value in values:
            selected = [
                e
                for e in cb.effects
                if _scoped(e, event, value)
                or (event == "say" and e.kind == "say" and str(e.value) == value)
            ]
            reg = cb.registration
            result.append(
                Callback(
                    Registration(reg.owner, f"{event}:{value}", reg.npc, reg.callback, reg.source),
                    selected,
                )
            )
    return result


def _loot_policies(function: _Function) -> dict[tuple[int, int], tuple[list[str], list[str]]]:
    """Conservatively recognize the explicit player.lua EVENT_LOOT authorization pattern.

    Do not infer that an item is permitted from GetID alone. A denied item does
    not become a producer; guards are associated with its exact corpse type.
    """
    text = "\n".join(line for _, line, _ in function.statements)
    predicates = re.findall(
        r"e\.item:GetID\(\)\s*==\s*(\d+)\s+and\s+e\.corpse:GetNPCTypeID\(\)\s*==\s*(\d+)", text
    )
    policies: dict[tuple[int, int], tuple[list[str], list[str]]] = {}
    for item, npc in predicates:
        # Use only the corresponding branch, not other unrelated EVENT_LOOT clauses.
        candidate = next(
            (
                i
                for i, (_, line, _) in enumerate(function.statements)
                if f"e.item:GetID() == {item}" in line
                and f"e.corpse:GetNPCTypeID() == {npc}" in line
            ),
            None,
        )
        if candidate is None:
            continue
        remaining = function.statements[candidate + 1 :]
        stop = next(
            (
                i
                for i, (_, line, _) in enumerate(remaining)
                if re.match(r"^(?:elseif|else)\b", line)
            ),
            len(remaining),
        )
        part = "\n".join(line for _, line, _ in remaining[:stop])
        flags = re.findall(
            r'e\.self:GetGlobal\(\s*["\']([^"\']+)["\']\s*\)\s*==\s*["\']([^"\']+)', part
        )
        clears = re.findall(r'e\.self:DelGlobal\(\s*["\']([^"\']+)', part)
        if flags:
            policies[int(item), int(npc)] = (
                [f"{name} == {value}" for name, value in flags],
                clears,
            )
    return policies


def _wave_protocol(
    zone: str,
    path: str,
    source: str,
    registrations: list[Registration],
) -> tuple[int, dict[int, int]] | None:
    """Detect a counted, signalled wave state machine (not a general Lua evaluator).

    Accept only a single signal receiver, a monotonically incremented kill
    counter, and literal wave/count comparisons. The thresholds are required
    for progression; a mere comparison does not make a later wave reachable.
    """
    if not re.search(r"\bSpawn_Wave\s*\(\s*this_wave\s*\)", source):
        return None
    if not re.search(r"\bthis_wave\s*=\s*this_wave\s*\+\s*1", source):
        return None
    if not re.search(r"\bmobs_slain\s*=\s*mobs_slain\s*\+\s*1", source):
        return None
    thresholds = {
        int(wave): int(kills)
        for wave, kills in re.findall(
            r"\bthis_wave\s*==\s*(\d+)\s+and\s+mobs_slain\s*==\s*(\d+)",
            source,
        )
    }
    if not thresholds or sorted(thresholds) != list(range(1, max(thresholds) + 1)):
        return None
    # Only the registered SIGNAL owner can advance these counters.
    definitions = _functions(source)
    signals = {
        r.npc
        for r in registrations
        if r.event == "signal"
        and r.npc is not None
        and r.callback in definitions
        and any("mobs_slain" in line for _, line, _ in definitions[r.callback].statements)
    }
    if len(signals) != 1:
        return None
    controller = next(iter(signals))
    # A counter is an encounter death count only when registered mob-death
    # callbacks actually signal this controller. Otherwise its advancement is
    # unknown and the wave path must not be presented as established.
    witnessed = any(
        r.event == "death_complete"
        and r.callback in definitions
        and any(
            re.search(r"eq\.signal\s*\(\s*" + str(controller) + r"\s*,", line)
            for _, line, _ in definitions[r.callback].statements
        )
        for r in registrations
    )
    if not witnessed:
        return None
    return controller, thresholds


def _cleared_mobs(source: str, registrations: list[Registration]) -> set[int]:
    """NPC item lists explicitly wiped on spawn/death invalidate static loot.

    Do not treat ClearItemList on an unrelated player or controller as a
    reason to suppress other NPC loot tables.
    """
    functions = _functions(source)
    return {
        int(r.npc)
        for r in registrations
        if r.npc is not None
        and r.event in {"spawn", "death", "death_complete"}
        and r.callback in functions
        and any(
            not guards and re.search(r"\be\.self:ClearItemList\s*\(", line)
            for _number, line, guards in functions[r.callback].statements
        )
    }


def analyze_encounters(zone: str, scripts: dict[str, str]) -> EncounterAnalysis:
    """Connect registered callbacks only through actionable, demonstrated paths.

    Roots are explicit player SAY commands. Event-driven effects are attached
    only to the matching event branch. Other callback kinds are indexed and
    reported, but not promoted without a proven trigger.
    """
    result = EncounterAnalysis()
    zone = zone.lower()
    if not scripts:
        return result
    loaded: set[str] = set()
    for path, text in scripts.items():
        if path.rsplit("/", 1)[-1] == "script_init.lua":
            loaded.update(
                re.findall(
                    r'eq\.load_encounter\s*\(\s*["\']([^"\']+)', _without_comments(text).lower()
                )
            )
    callbacks: list[Callback] = []
    wave_protocols: dict[str, tuple[int, dict[int, int]]] = {}
    for path, content in scripts.items():
        if not path.startswith("encounters/"):
            continue
        name = path.rsplit("/", 1)[-1].removesuffix(".lua").lower()
        if name not in loaded:
            continue
        result.owned_files.add(path)
        definitions = _functions(content)
        symbols = _symbols(content)
        registrations = _registrations(path, content, symbols)
        result.cleared_npcs.update(_cleared_mobs(content, registrations))
        protocol = _wave_protocol(zone, path, content, registrations)
        if protocol:
            wave_protocols[path] = protocol
        for reg in registrations:
            fn = definitions.get(reg.callback)
            if fn is None:
                variants = [name for name in definitions if name.lower() == reg.callback.lower()]
                hint = f" (case mismatch: defined {variants[0]})" if variants else ""
                result.diagnostics.append(f"{zone}/{path}: missing callback {reg.callback}{hint}")
            else:
                effects = _expand_effects(
                    reg.callback, definitions, symbols=symbols, self_npc=reg.npc
                )
                for eff in effects:
                    if eff.kind == "unresolved_spawn":
                        detail = f"{zone}/{path}:{eff.line}: unresolved {eff.receiver} target in {reg.callback}: {eff.value}"
                        if detail not in result.diagnostics:
                            result.diagnostics.append(detail)
                callbacks.append(Callback(reg, effects))
    if not callbacks:
        return result
    callbacks = _separate_branches(callbacks)

    outgoing: dict[str, list[tuple[str, dict]]] = defaultdict(list)
    by_spawn: dict[int, list[str]] = defaultdict(list)
    by_death: dict[int, list[str]] = defaultdict(list)
    by_timer: dict[tuple[int, str], list[str]] = defaultdict(list)
    by_signal: dict[tuple[int, str], list[str]] = defaultdict(list)
    by_callback: dict[str, Callback] = {}
    roots: set[str] = set()

    def connect(source: str, target: str, relation: str = "triggers", **extra: object) -> None:
        outgoing[source].append(
            (target, {"kind": "edge", "rel": relation, "from": source, "to": target, **extra})
        )

    for cb in callbacks:
        node = _event_node(zone, cb.registration)
        # Distinct event IDs include the owner NPC, event branch and callback.
        if node in by_callback:
            # Multiple encounters may legitimately register the same zone-level
            # event. Keep each callback separate without changing stable IDs
            # for the common single-owner case.
            stem = cb.registration.source.removesuffix(".lua").replace("/", ":")
            node = f"{node}#registered:{stem}"
            if node in by_callback:
                result.diagnostics.append(
                    f"{zone}/{cb.registration.source}: duplicate registration {node}"
                )
                continue
        by_callback[node] = cb
        npc = cb.registration.npc
        event = cb.registration.event
        if npc is not None:
            if event == "spawn":
                by_spawn[npc].append(node)
            elif event in {"death_complete", "death"}:
                by_death[npc].append(node)
            elif event.startswith("timer:"):
                by_timer[npc, event[6:]].append(node)
            elif event.startswith("signal:"):
                by_signal[npc, event[7:]].append(node)
            elif event == "signal":
                by_signal[npc, "*"].append(node)
        if event.startswith("say:") and npc is not None:
            keyword = event[4:]
            source = f"{zone}/npc:{npc}#{keyword}"
            connect(source, node, npc=npc, action="say", keyword=keyword)
            roots.add(source)

    # A counted wave is a sequence of *gated* stages, not a union of all
    # Spawn_Wave() expansions from the SAY callback. The kill counts refer to
    # qualifying EVENT_DEATH_COMPLETE signals, not arbitrary player kills.
    for path, (controller, thresholds) in wave_protocols.items():
        say_callbacks = [
            node
            for node, cb in by_callback.items()
            if cb.registration.source == path
            and cb.registration.npc == controller
            and cb.registration.event.startswith("say:")
            # A SAY callback can serve multiple keywords. Only the
            # branch that actually expands Spawn_Wave may initiate
            # the first wave; a HAIL in the same function cannot.
            and any(e.kind == "spawn" for e in cb.effects)
            and any(
                "Spawn_Wave" in line
                for _n, line, _g in _functions(scripts[path])
                .get(cb.registration.callback, _Function("", ()))
                .statements
            )
        ]
        if not say_callbacks:
            continue
        for say in say_callbacks:
            connect(say, f"{zone}/npc:{controller}#event:wave:1", action="wave_start", wave=1)
        for wave, count in sorted(thresholds.items()):
            source = f"{zone}/npc:{controller}#event:wave:{wave}"
            dest = (
                f"{zone}/npc:{controller}#event:wave:{wave + 1}"
                if wave < max(thresholds)
                else f"{zone}/npc:{controller}#event:wave_complete:{wave}"
            )
            connect(
                source,
                dest,
                action="defeat_wave",
                wave=wave,
                required_kills=count,
                counter="mobs_slain",
                source_script=path,
            )

    for node, cb in by_callback.items():
        npc = cb.registration.npc
        event = cb.registration.event
        activated = any(
            e.kind in {"activate", "spawn_condition", "timer"}
            and not (e.kind == "spawn_condition" and str(e.value).endswith(":0"))
            for e in cb.effects
        )
        if event.startswith("say:") and npc is not None and activated:
            for death in by_death.get(npc, ()):
                kill = f"{zone}/npc:{npc}#kill:{npc}"
                connect(node, kill, npc=npc, combat=True, action="defeat")
                connect(kill, death, npc=npc, combat=True)
        for eff in cb.effects:
            if eff.kind == "spawn":
                # Interprocedural expansion retains the callee's wave_number
                # guard. Reparent each spawn to its actual counted wave.
                effect_owner = node
                protocol = wave_protocols.get(cb.registration.source)
                if protocol and cb.registration.npc == protocol[0]:
                    wave_matches = [
                        int(m.group(1))
                        for guard in eff.guards
                        for m in re.finditer(r"\bwave_number\s*==\s*(\d+)", guard)
                    ]
                    if wave_matches:
                        # Root SAY starts wave 1. A qualifying signal advances
                        # this_wave first and then calls Spawn_Wave(this_wave),
                        # so guard `this_wave == N` can only produce wave N+1.
                        expected_wave: int | None = None
                        if cb.registration.event.startswith("say:"):
                            expected_wave = 1
                        elif cb.registration.event.startswith("signal"):
                            current = [
                                int(m.group(1))
                                for guard in eff.guards
                                for m in re.finditer(r"\bthis_wave\s*==\s*(\d+)", guard)
                            ]
                            expected_wave = current[-1] + 1 if current else None
                        else:
                            expected_wave = None
                        if expected_wave is None or wave_matches[-1] != expected_wave:
                            continue
                        effect_owner = f"{zone}/npc:{protocol[0]}#event:wave:{expected_wave}"
                    elif cb.registration.event.startswith("signal"):
                        completed = [
                            int(m.group(1))
                            for guard in eff.guards
                            for m in re.finditer(r"\bthis_wave\s*==\s*(\d+)", guard)
                        ]
                        if completed and completed[-1] == max(protocol[1]):
                            effect_owner = (
                                f"{zone}/npc:{protocol[0]}#event:wave_complete:{completed[-1]}"
                            )
                spawned = int(eff.value)
                spawned_node = f"{zone}/npc:{spawned}#event:spawned:{spawned}"
                scoped_guards = [
                    g
                    for g in eff.guards
                    if not (effect_owner != node and re.search(r"e\.message:findi\s*\(", g))
                ]
                connect(
                    effect_owner,
                    spawned_node,
                    "spawns",
                    npc=spawned,
                    group=effect_owner,
                    guards=scoped_guards,
                    zone=zone,
                    alternative=bool(len(eff.alternatives) > 1),
                )
                for target in by_spawn.get(spawned, ()):
                    connect(spawned_node, target, npc=spawned)
            elif eff.kind == "timer" and npc is not None:
                timer = str(eff.value)
                destination = f"{zone}/npc:{npc}#timer:{timer}"
                connect(node, destination, timer=timer, guards=list(eff.guards))
                for target in by_timer.get((npc, timer), ()):
                    connect(destination, target, timer=timer)
            elif eff.kind == "signal":
                parts = str(eff.value).split(":")
                if len(parts) == 2 and all(x.isdigit() for x in parts):
                    recipient, value = int(parts[0]), parts[1]
                    for target in by_signal.get((recipient, value), []) + by_signal.get(
                        (recipient, "*"), []
                    ):
                        connect(
                            node, target, npc=recipient, signal=int(value), guards=list(eff.guards)
                        )
    # Rewards can only travel from reached callback nodes.
    reached = set(roots)
    queue = deque(sorted(roots))
    proof_edges: list[dict] = []
    seen: set[tuple[str, str, str]] = set()
    while queue:
        source = queue.popleft()
        for target, edge in outgoing.get(source, ()):
            key = (edge["from"], edge["to"], edge["rel"])
            if key not in seen:
                seen.add(key)
                proof_edges.append(edge)
            if target not in reached:
                reached.add(target)
                queue.append(target)
    result.edges.extend(proof_edges)

    # Player zone scripts and encounter-registered player loot callbacks can
    # both deny acquisition. Their predicates apply to the looting player.
    loot_policy: dict[tuple[int, int], tuple[list[str], list[str]]] = {}
    for path, content in scripts.items():
        if path.rsplit("/", 1)[-1] == "player.lua":
            fn = _functions(content).get("event_loot")
            if fn:
                loot_policy.update(_loot_policies(fn))
    for cb in callbacks:
        if cb.registration.npc is None and cb.registration.event == "loot":
            fn = _functions(scripts[cb.registration.source]).get(cb.registration.callback)
            if fn:
                loot_policy.update(_loot_policies(fn))

    for node, cb in by_callback.items():
        if node not in reached:
            continue
        npc = cb.registration.npc
        for eff in cb.effects:
            if eff.kind != "add_item":
                continue
            owner: int | None = None
            if eff.receiver.isdigit():
                owner = int(eff.receiver)
            elif eff.receiver.startswith(("e.self", "e.corpse")):
                owner = npc
            else:
                owner = None
            if owner is None:
                result.diagnostics.append(
                    f"{zone}/{cb.registration.source}:{eff.line}: unbound AddItem receiver {eff.receiver}"
                )
                continue
            item = int(eff.value)
            if event := cb.registration.event:
                if event == "spawn" and owner != npc:
                    continue
            group = f"{node}#reward:{item}"
            policy_guards, clears = loot_policy.get((item, owner), ([], []))
            result.edges.append(
                {
                    "kind": "edge",
                    "rel": "loots",
                    "from": node,
                    "to": f"item:{item}",
                    "npc": owner,
                    "zone": zone,
                    "group": group,
                    "guards": list(eff.guards),
                    "loot_guards": policy_guards,
                    "after_loot_clear": clears,
                    "reachable": True,
                    "source_script": cb.registration.source,
                    "conditional": bool(eff.guards or policy_guards or len(eff.alternatives) > 1),
                    "alternatives": list(eff.alternatives),
                }
            )
            for flag, value, subject in _flag_guards(eff.guards):
                result.edges.append(
                    {
                        "kind": "edge",
                        "rel": "needs",
                        "from": node,
                        "to": f"flag:{flag}",
                        "flag": flag,
                        "at": value,
                        "subject": subject,
                        "group": group,
                    }
                )
            for requirement in policy_guards:
                flag, value = requirement.split(" == ", 1)
                result.edges.append(
                    {
                        "kind": "edge",
                        "rel": "needs",
                        "from": node,
                        "to": f"flag:{flag}",
                        "flag": flag,
                        "at": value,
                        "subject": "looting_player",
                        "group": group,
                    }
                )
            result.produced_items.add(item)
    return result
