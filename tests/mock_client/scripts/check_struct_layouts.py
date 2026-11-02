#!/usr/bin/env python3
"""Compare eqclient3 struct.pack calls with the C structs their comments name.

Each comment cites a header or source line. The script parses that struct
(packed to 1 byte, the way the packet headers are) or the encoder writes at
that line, then checks the format string, the pack_into offset, and the size.
"""

from __future__ import annotations

import ast
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

PRIMITIVE: dict[str, tuple[str, int]] = {
    "uint8": ("B", 1),
    "uint8_t": ("B", 1),
    "int8": ("b", 1),
    "int8_t": ("b", 1),
    "uint16": ("H", 2),
    "uint16_t": ("H", 2),
    "int16": ("h", 2),
    "int16_t": ("h", 2),
    "uint32": ("I", 4),
    "uint32_t": ("I", 4),
    "int32": ("i", 4),
    "int32_t": ("i", 4),
    "uint64": ("Q", 8),
    "uint64_t": ("Q", 8),
    "int64": ("q", 8),
    "int64_t": ("q", 8),
    "float": ("f", 4),
    "double": ("d", 8),
    "char": ("s", 1),
    "bool": ("B", 1),
    "unsigned char": ("B", 1),
    "signed char": ("b", 1),
    "unsigned short": ("H", 2),
    "short": ("h", 2),
    "unsigned int": ("I", 4),
    "unsigned long": ("I", 4),
    "long": ("i", 4),
    "int": ("i", 4),
    "signed": ("i", 4),
    "unsigned": ("I", 4),
}

WRITE_KIND: dict[str, tuple[str, int]] = {
    "UInt8": ("B", 1),
    "Int8": ("b", 1),
    "UInt16": ("H", 2),
    "Int16": ("h", 2),
    "UInt32": ("I", 4),
    "Int32": ("i", 4),
    "UInt64": ("Q", 8),
    "Int64": ("q", 8),
    "Float": ("f", 4),
    "Double": ("d", 8),
}

CODE_SIZE: dict[str, int] = {
    "x": 1,
    "c": 1,
    "b": 1,
    "B": 1,
    "?": 1,
    "h": 2,
    "H": 2,
    "i": 4,
    "I": 4,
    "l": 4,
    "L": 4,
    "q": 8,
    "Q": 8,
    "f": 4,
    "d": 8,
    "s": 1,
}

CITE = re.compile(r"#\s*((?:common|zone)/[A-Za-z0-9_./]+):(\d+)")
STRUCT_WORD = re.compile(r"\b([A-Za-z_][A-Za-z0-9_]*Struct)\b")
HELPER = re.compile(r"\b(struct\.pack_into|struct\.pack|_put_fixed|_fixed|_need)\s*\(")
WRITE = re.compile(r"\bWrite(UInt64|UInt32|UInt16|UInt8|Int64|Int32|Int16|Int8|Float|Double|String|LengthString)\b")
ENCODE_TYPE = re.compile(r"VARSTRUCT_ENCODE_TYPE\(\s*([A-Za-z0-9_:]+)")
ENCODE_STRING = re.compile(r"VARSTRUCT_ENCODE_STRING\b")
EQ_FIELD = re.compile(r"\beq->\s*([A-Za-z_][A-Za-z0-9_]*)")
OUT_FIELD = re.compile(r"\bOUT(?:_str)?\(\s*([A-Za-z_][A-Za-z0-9_]*)")
SIZEOF = re.compile(r"sizeof\(\s*(?:structs::)?([A-Za-z_][A-Za-z0-9_]*)\s*\)")
SETUP = re.compile(r"SETUP_DIRECT_ENCODE\(\s*[A-Za-z_][A-Za-z0-9_]*\s*,\s*structs::([A-Za-z_][A-Za-z0-9_]*)\s*\)")
FOR_BOUND = re.compile(r"for\s*\([^;]*;\s*[A-Za-z_][A-Za-z0-9_]*\s*<\s*(\d+)\s*;")
DEFINE_NUM = re.compile(r"^\s*#define\s+([A-Za-z_]\w*)\s+\(?\s*(0x[0-9A-Fa-f]+|\d+)\s*\)?\s*(?:$|//|/\*)")
DEFINE_NAME = re.compile(r"^\s*#define\s+([A-Za-z_]\w*)\s+([A-Za-z_]\w*)\s*$")
CONST_NUM = re.compile(
    r"\b(?:const|constexpr)\s+(?:unsigned\s+)?(?:int|uint32|uint16|uint8|int32|int16|int8|"
    r"size_t|uint32_t|uint16_t|uint8_t|int32_t|int16_t|int8_t)\s+"
    r"([A-Za-z_]\w*)\s*=\s*(0x[0-9A-Fa-f]+|\d+)"
)
OFFSET_ANN = re.compile(r"/\*\s*(\d+)\s*\*/")
FOR_HEADER = re.compile(r"for\s*\((?:[^;]*?\b(\w+)\s*=\s*([^;]+))?;\s*(\w+)\s*<\s*([^;&]+)")
SIZEOF_PRIMITIVE = re.compile(r"sizeof\(\s*(?:const\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*\)")
PTR_STORE = re.compile(r"\*\s*\(\s*(uint64_t|uint32_t|uint16_t|uint8_t|int32_t|int16_t|uint32|uint16|int32)\s*\*\s*\)")
FIELD_ASSIGN = re.compile(r"\beq(?:\[[^\]]+\])?\.([A-Za-z_]\w*)\s*=")
VAR_STRUCT = re.compile(r"(?:SETUP_VAR_ENCODE|ALLOC_VAR_ENCODE)\(\s*(?:structs::)?([A-Za-z_]\w*)")
CAST_STRUCT = re.compile(r"structs::([A-Za-z_]\w*)\s*\*")
APP_SIZE = re.compile(r"app->size\s*!=\s*(\d+)")
NAMED_VALUE = re.compile(r"\b([A-Za-z_]\w+)\s+\w+\s*;")


@dataclass(frozen=True)
class Field:
    name: str
    code: str
    size: int
    offset: int
    line: int
    type_name: str = ""
    bitfield: bool = False


@dataclass
class CStruct:
    name: str
    file: str
    start: int
    end: int
    fields: list[Field]
    size: int
    error: str = ""


@dataclass(frozen=True)
class Element:
    code: str
    size: int


@dataclass(frozen=True)
class Call:
    kind: str
    line: int
    fmt: str
    elements: tuple[Element, ...]
    offset: int | None
    size: int | None
    whole: bool


@dataclass(frozen=True)
class Cite:
    file: str
    line: int
    name: str
    py_file: str
    py_line: int


@dataclass(frozen=True)
class Result:
    status: str
    where: str
    detail: str


@dataclass
class Catalog:
    by_file: dict[str, dict[str, CStruct]] = field(default_factory=dict)
    by_name: dict[str, list[CStruct]] = field(default_factory=dict)
    lines: dict[str, list[str]] = field(default_factory=dict)
    defines: dict[str, int] = field(default_factory=dict)

    def get(self, filename: str, name: str) -> CStruct | None:
        found = self.by_file.get(filename, {}).get(name)
        if found is not None:
            return found
        rows = self.by_name.get(name, [])
        if len(rows) == 1:
            return rows[0]
        preferred = [row for row in rows if row.file == "common/patches/rof2_structs.h"]
        if len(preferred) == 1:
            return preferred[0]
        return rows[0] if rows else None

    def at(self, filename: str, line: int) -> CStruct | None:
        for struct in self.by_file.get(filename, {}).values():
            if struct.start <= line <= struct.end:
                return struct
        return None


def repo_root() -> Path:
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "common" / "patches" / "rof2_structs.h").is_file():
            return parent
    raise SystemExit("EQEmu root not found from the script path")


def mock_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_defines(root: Path) -> dict[str, int]:
    values: dict[str, int] = {}
    aliases: list[tuple[str, str]] = []
    for directory in (root / "common", root / "zone"):
        if not directory.is_dir():
            continue
        for path in directory.rglob("*.h"):
            if "deprecated" in path.parts or "build" in path.parts:
                continue
            text = path.read_text(errors="replace")
            for line in text.splitlines():
                number = DEFINE_NUM.match(line)
                if number is not None:
                    values[number.group(1)] = int(number.group(2), 0)
                    continue
                alias = DEFINE_NAME.match(line)
                if alias is not None:
                    aliases.append((alias.group(1), alias.group(2)))
            for match in CONST_NUM.finditer(text):
                values[match.group(1)] = int(match.group(2), 0)
            absorb_enums(text, values)
    for name, alias in aliases:
        if alias in values and name not in values:
            values[name] = values[alias]
    return values


def strip_comments(text: str) -> str:
    out: list[str] = []
    index = 0
    block = False
    while index < len(text):
        if block:
            end = text.find("*/", index)
            if end < 0:
                out.append(re.sub(r"[^\n]", " ", text[index:]))
                break
            out.append(re.sub(r"[^\n]", " ", text[index:end]))
            index = end + 2
            block = False
            continue
        line = text.find("//", index)
        block_at = text.find("/*", index)
        if line < 0 and block_at < 0:
            out.append(text[index:])
            break
        if line >= 0 and (block_at < 0 or line < block_at):
            newline = text.find("\n", line)
            out.append(text[index:line])
            if newline < 0:
                break
            out.append("\n")
            index = newline + 1
            continue
        out.append(text[index:block_at])
        index = block_at + 2
        block = True
    return "".join(out)


def eval_int(expr: str, names: dict[str, int]) -> int | None:
    try:
        tree = ast.parse(expr.strip(), mode="eval")
    except SyntaxError:
        return None

    def walk(node: ast.AST) -> int:
        if isinstance(node, ast.Expression):
            return walk(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, int):
            return node.value
        if isinstance(node, ast.Name):
            if node.id not in names:
                raise KeyError(node.id)
            return names[node.id]
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.UAdd):
            return walk(node.operand)
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            return -walk(node.operand)
        if isinstance(node, ast.BinOp):
            left = walk(node.left)
            right = walk(node.right)
            if isinstance(node.op, ast.Add):
                return left + right
            if isinstance(node.op, ast.Sub):
                return left - right
            if isinstance(node.op, ast.Mult):
                return left * right
            if isinstance(node.op, ast.FloorDiv | ast.Div):
                return left // right
        raise ValueError(type(node).__name__)

    try:
        return walk(tree)
    except (KeyError, ValueError, ZeroDivisionError):
        return None


def primitive(type_name: str) -> tuple[str, int] | None:
    return PRIMITIVE.get(" ".join(type_name.split()))


def absorb_enums(text: str, values: dict[str, int]) -> None:
    """Enumerator values. textureBegin is 0 and materialCount is 9 in textures.h."""
    stripped = strip_comments(text)
    for match in re.finditer(r"\benum\b[^{;]*\{([^{}]*)\}", stripped, re.S):
        current = 0
        seen = False
        for piece in match.group(1).split(","):
            piece = piece.strip()
            if not piece:
                continue
            if "=" in piece:
                name, expr = piece.split("=", 1)
                name = name.split()[-1]
                value = eval_int(expr.strip().split("::")[-1], values)
                if value is None:
                    current = 0
                    seen = False
                    continue
                values[name] = value
                current = value + 1
                seen = True
                continue
            if not seen:
                current = 0
                seen = True
            name = piece.split()[-1]
            if name[:1].isalpha() or name[:1] == "_":
                values.setdefault(name, current)
                current += 1


def last_name(expr: str) -> str:
    return expr.strip().split("::")[-1].strip()


def eval_count(expr: str, names: dict[str, int]) -> int | None:
    value = eval_int(expr, names)
    if value is not None:
        return value
    # EQ::spells:: and RoF2::spells:: are different counts. Keep the EQ ones distinct
    # when the caller supplied them, and fall back to a bare name otherwise.
    qualified = expr.replace("EQ::spells::", "EQ_spells_")
    qualified = re.sub(r"\b[A-Za-z_]\w*::", "", qualified)
    value = eval_int(qualified, names)
    if value is not None:
        return value
    scrubbed = re.sub(r"\b[A-Za-z_]\w*::", "", expr)
    return eval_int(scrubbed, names)


def rof2_encode_names(names: dict[str, int]) -> dict[str, int]:
    """Constants the RoF2 encoder actually writes.

    Header scans keep the last patch that defined the name, so a walk of rof2.cpp
    would otherwise see Underfoot's buff count or the struct comment's 200 disciplines.
    The profile encoder writes RoF2::structs::MAX_PP_DISCIPLINES (300) and
    RoF2::spells::SPELL_GEM_COUNT (16), of which EQ::spells::SPELL_GEM_COUNT (12) are live.
    """
    local = dict(names)
    local["MAX_PP_SKILL"] = 100
    local["MAX_PP_INNATE_SKILL"] = 25
    local["MAX_PP_DISCIPLINES"] = 300
    local["BUFF_COUNT"] = 42
    local["MAX_RECAST_TYPES"] = 20
    local["SPELLBOOK_SIZE"] = 720
    local["EQ_spells_SPELLBOOK_SIZE"] = 720
    local["SPELL_GEM_COUNT"] = 16
    local["EQ_spells_SPELL_GEM_COUNT"] = 12
    return local


def same_code(left: str, right: str) -> bool:
    """WriteUInt32 and WriteSInt32 put the same 4 bytes on the wire."""
    signed = {"b": "B", "B": "b", "h": "H", "H": "h", "i": "I", "I": "i", "q": "Q", "Q": "q"}
    return left == right or signed.get(left) == right


def parse_format(fmt: str) -> tuple[Element, ...] | None:
    if not fmt or fmt[0] not in "<>=!@":
        return None
    index = 1
    elements: list[Element] = []
    while index < len(fmt):
        count_at = index
        while index < len(fmt) and fmt[index].isdigit():
            index += 1
        if index >= len(fmt):
            return None
        code = fmt[index]
        index += 1
        count_text = fmt[count_at : index - 1]
        count = int(count_text) if count_text else 1
        if code == "s":
            elements.append(Element("s", count))
            continue
        width = CODE_SIZE.get(code)
        if width is None:
            return None
        for _repeat in range(count):
            elements.append(Element(code, width))
    return tuple(elements)


def balanced(text: str, open_at: int) -> int:
    depth = 0
    quote = ""
    index = open_at
    while index < len(text):
        char = text[index]
        if quote:
            if char == "\\":
                index += 2
                continue
            if char == quote:
                quote = ""
            index += 1
            continue
        if char in "\"'":
            quote = char
            index += 1
            continue
        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
            if depth == 0:
                return index
        index += 1
    return len(text) - 1


def split_args(body: str) -> list[str]:
    args: list[str] = []
    start = 0
    depth = 0
    quote = ""
    for index, char in enumerate(body):
        if quote:
            if char == "\\":
                continue
            if char == quote:
                quote = ""
            continue
        if char in "\"'":
            quote = char
            continue
        if char in "([{":
            depth += 1
        elif char in ")]}":
            depth -= 1
        elif char == "," and depth == 0:
            args.append(body[start:index].strip())
            start = index + 1
    tail = body[start:].strip()
    if tail:
        args.append(tail)
    return args


def first_format(call: str) -> str:
    for match in re.finditer(r"(['\"])([<>=!@].*?)(\1)", call, re.S):
        return match.group(2)
    return ""


def literal_int(expr: str) -> int | None:
    text = expr.strip()
    if re.fullmatch(r"0x[0-9A-Fa-f]+|\d+", text):
        return int(text, 0)
    return None


def read_call(text: str, start: int) -> Call | None:
    kind_match = HELPER.search(text, start)
    if kind_match is None or kind_match.start() != start:
        found = HELPER.search(text, start)
        if found is None:
            return None
        start = found.start()
        kind_match = found
    kind = kind_match.group(1)
    open_at = text.find("(", kind_match.end() - 1)
    close_at = balanced(text, open_at)
    body = text[open_at + 1 : close_at]
    line = text[:start].count("\n") + 1
    args = split_args(body)
    before = text[text.rfind("\n", 0, start) + 1 : start]
    after = text[close_at + 1 : text.find("\n", close_at)]
    whole = before.strip().startswith("return") and not after.strip().startswith("+")
    if kind == "struct.pack_into":
        fmt = first_format(body)
        elements = parse_format(fmt)
        if elements is None:
            return None
        offset = literal_int(args[2]) if len(args) > 2 else None
        return Call(kind, line, fmt, elements, offset, sum(item.size for item in elements), whole)
    if kind == "struct.pack":
        fmt = first_format(body)
        elements = parse_format(fmt)
        if elements is None:
            return None
        return Call(kind, line, fmt, elements, 0 if whole else None, sum(item.size for item in elements), whole)
    if kind == "_need" and len(args) >= 2:
        size = literal_int(args[1])
        return Call(kind, line, "", (), None, size, False)
    if kind == "_put_fixed" and len(args) >= 4:
        return Call(kind, line, "", (), literal_int(args[1]), literal_int(args[3]), False)
    if kind == "_fixed" and len(args) >= 3:
        return Call(kind, line, "", (), literal_int(args[1]), literal_int(args[2]), False)
    return None


def cites_on(path: Path, line: str, number: int) -> list[Cite]:
    found: list[Cite] = []
    for match in CITE.finditer(line):
        tail = line[match.end() :].strip()
        token = tail.split()[0].strip(".,)") if tail else ""
        name = token if token.endswith("Struct") else ""
        if not name:
            named = STRUCT_WORD.findall(line)
            name = named[-1] if named else ""
        found.append(Cite(match.group(1), int(match.group(2)), name, str(path), number))
    return found


def matching_brace(lines: list[str], open_line: int) -> int:
    depth = 0
    started = False
    for index in range(open_line, len(lines)):
        for char in lines[index]:
            if char == "{":
                depth += 1
                started = True
            elif char == "}":
                depth -= 1
        if started and depth <= 0:
            return index
    return len(lines) - 1


def skip_statement(lines: list[str], index: int) -> int:
    if "{" in lines[index]:
        return matching_brace(lines, index) + 1
    brace = index + 1
    while brace < len(lines) and "{" not in lines[brace] and ";" not in lines[brace]:
        brace += 1
    if brace < len(lines) and "{" in lines[brace]:
        brace_at = lines[brace].find("{")
        semicolon = lines[brace].find(";")
        if semicolon < 0 or brace_at < semicolon:
            return matching_brace(lines, brace) + 1
    return index + 1


def parse_array_sizes(arrays: list[str], names: dict[str, int]) -> int | None:
    total = 1
    for array in arrays:
        size = eval_count(array, names)
        if size is None:
            return None
        total *= size
    return total


def split_type_and_name(left: str) -> tuple[str, str]:
    text = " ".join(left.replace("*", " ").split())
    if text.startswith("struct "):
        text = text[len("struct ") :]
    parts = text.split()
    if len(parts) < 2:
        return text, ""
    return " ".join(parts[:-1]), parts[-1]


def add_field(
    fields: list[Field],
    name: str,
    code: str,
    size: int,
    offset: int,
    line: int,
    type_name: str = "",
    bitfield: bool = False,
) -> int:
    fields.append(Field(name, code, size, offset, line, type_name, bitfield))
    return offset + size


def is_bitfield_text(text: str) -> bool:
    scrubbed = text.replace("::", "")
    return re.search(r":\s*\d+\s*$", scrubbed.rstrip(";").strip()) is not None


def annotation_of(line: str) -> int | None:
    match = OFFSET_ANN.search(line)
    if match is None:
        return None
    return int(match.group(1))


def parse_field_line(
    line: str,
    line_no: int,
    offset: int,
    fields: list[Field],
    names: dict[str, int],
    pending: dict[str, CStruct],
) -> tuple[int, str]:
    text = line.strip().rstrip(";")
    if not text or text.startswith("#") or text in {"public:", "private:", "protected:"}:
        return offset, ""
    if "(" in text:
        return offset, ""
    if is_bitfield_text(text):
        return parse_bitfield(text, line_no, offset, fields)
    arrays: list[str] = []
    while True:
        match = re.search(r"\[([^\]]+)\]\s*$", text)
        if match is None:
            break
        arrays.insert(0, match.group(1).strip())
        text = text[: match.start()].rstrip()
    type_name, field_name = split_type_and_name(text)
    if not field_name:
        return offset, f"unparsed field at line {line_no}: {line.strip()}"
    if "*" in line:
        return offset, f"pointer field {field_name} at line {line_no}"
    count = parse_array_sizes(arrays, names) if arrays else 1
    if count is None:
        return offset, f"unknown array size at line {line_no}: {line.strip()}"
    kind = primitive(type_name)
    if kind is not None:
        code, width = kind
        if arrays and code == "s":
            return add_field(fields, field_name, "s", width * count, offset, line_no, type_name), ""
        if arrays and code == "B":
            return add_field(fields, field_name, "B", width * count, offset, line_no, type_name), ""
        if arrays:
            step = offset
            for index in range(count):
                step = add_field(fields, f"{field_name}[{index}]", code, width, step, line_no, type_name)
            return step, ""
        return add_field(fields, field_name, code, width, offset, line_no, type_name), ""
    nested = pending.get(type_name)
    if nested is None or nested.error:
        return offset, f"unknown type {type_name} at line {line_no}"
    copies = count
    step = offset
    for index in range(copies):
        label = field_name if copies == 1 else f"{field_name}[{index}]"
        add_field(fields, label, "B", nested.size, step, line_no, type_name)
        for child in nested.fields:
            add_field(
                fields,
                f"{label}.{child.name}",
                child.code,
                child.size,
                step + child.offset,
                line_no,
                child.type_name,
                child.bitfield,
            )
        step += nested.size
    return step, ""


def parse_bitfield(text: str, line_no: int, offset: int, fields: list[Field]) -> tuple[int, str]:
    pieces = [piece.strip() for piece in text.split(",")]
    type_name = ""
    widths: list[int] = []
    container: tuple[str, int] | None = None
    for piece in pieces:
        if ":" not in piece:
            return offset, f"unparsed bitfield at line {line_no}"
        left, width_text = piece.rsplit(":", 1)
        width = eval_int(width_text.strip(), {})
        if width is None:
            return offset, f"unparsed bitfield width at line {line_no}"
        left = left.strip()
        if len(left.split()) >= 2:
            type_name, _name = split_type_and_name(left)
            container = primitive(type_name)
            if container is None:
                return offset, f"unknown bitfield type {type_name} at line {line_no}"
        widths.append(width)
    if container is None:
        return offset, f"bitfield missing a type at line {line_no}"
    code, width_bytes = container
    capacity = width_bytes * 8
    used = 0
    step = offset
    for width in widths:
        if used + width > capacity:
            step = add_field(fields, f"bitfield@{step}", code, width_bytes, step, line_no, type_name, True)
            used = 0
        used += width
    if used:
        step = add_field(fields, f"bitfield@{step}", code, width_bytes, step, line_no, type_name, True)
    return step, ""


def base_names(header: str) -> list[str]:
    head = header.split("{", 1)[0]
    if ":" not in head:
        return []
    names: list[str] = []
    for part in head.split(":", 1)[1].split(","):
        token = part.strip().split()[-1] if part.strip() else ""
        if token:
            names.append(token)
    return names


def following_annotation(raw: list[str], lines: list[str], index: int, end: int, offset: int) -> int | None:
    """The next field's /*offset*/ when it is a real wire offset, not a /*0000*/ placeholder."""
    depth = 0
    for cursor in range(index + 1, end):
        for char in lines[cursor]:
            if char == "{":
                depth += 1
            elif char == "}":
                depth = max(0, depth - 1)
        if depth:
            continue
        stripped = lines[cursor].strip()
        if not stripped or stripped.startswith("#") or stripped.startswith("//"):
            continue
        ann = annotation_of(raw[cursor]) if cursor < len(raw) else None
        if ann is not None and ann > offset:
            return ann
        if stripped.endswith(";") or stripped.endswith("{") or is_bitfield_text(stripped):
            return None
    return None


def fit_array(text: str, offset: int, next_ann: int | None, names: dict[str, int]) -> str:
    """Prefer the annotated span when a primitive array's declared count does not fill it."""
    if next_ann is None or "[" not in text:
        return text
    gap = next_ann - offset
    if gap <= 0:
        return text
    brackets = list(re.finditer(r"\[([^\]]+)\]", text))
    if len(brackets) != 1:
        return text
    match = brackets[0]
    base = re.sub(r"\[[^\]]+\]", "", text).rstrip().rstrip(";")
    type_name, _field_name = split_type_and_name(base)
    kind = primitive(type_name)
    if kind is None or gap % kind[1] != 0:
        return text
    count = gap // kind[1]
    resolved = eval_count(match.group(1), names)
    if resolved is not None and resolved * kind[1] == gap:
        return text
    return text[: match.start()] + f"[{count}]" + text[match.end() :]


def shift_fields(fields: list[Field], delta: int) -> list[Field]:
    if delta == 0:
        return fields
    return [
        Field(field.name, field.code, field.size, field.offset + delta, field.line, field.type_name, field.bitfield)
        for field in fields
    ]


def layout_union(
    raw: list[str],
    lines: list[str],
    open_at: int,
    close_at: int,
    names: dict[str, int],
    pending: dict[str, CStruct],
) -> tuple[list[Field], int, str]:
    """Every alternative starts at 0. The union is as wide as its largest alternative."""
    fields: list[Field] = []
    size = 0
    index = open_at + 1
    while index < close_at:
        current = lines[index].strip()
        if not current or current.startswith("#") or current.startswith("//"):
            index += 1
            continue
        if current.startswith("struct") or current.startswith("union"):
            open_inner = index
            while open_inner < close_at and "{" not in lines[open_inner]:
                open_inner += 1
            if open_inner >= close_at:
                return [], 0, f"unclosed aggregate at line {index + 1}"
            close_inner = matching_brace(lines, open_inner)
            if current.startswith("union"):
                inner, inner_size, error = layout_union(raw, lines, open_inner, close_inner, names, pending)
            else:
                inner, inner_size, error = layout_body(raw, lines, open_inner + 1, close_inner, names, pending, 0)
            if error:
                return [], 0, error
            fields.extend(inner)
            size = max(size, inner_size)
            index = close_inner + 1
            continue
        statement, line_no, index = take_statement(lines, index, close_at)
        if not statement:
            continue
        member: list[Field] = []
        member_end, error = parse_field_line(statement, line_no, 0, member, names, pending)
        if error:
            return [], 0, error
        fields.extend(member)
        size = max(size, member_end)
    return fields, size, ""


def take_statement(lines: list[str], index: int, end: int) -> tuple[str, int, int]:
    current = lines[index].strip()
    if ";" in current or "{" in current:
        return current, index + 1, index + 1
    parts = [current]
    cursor = index
    while cursor + 1 < end and ";" not in parts[-1] and "{" not in parts[-1] and "(" not in parts[-1]:
        cursor += 1
        parts.append(lines[cursor].strip())
    return " ".join(parts), cursor + 1, cursor + 1


def layout_body(
    raw: list[str],
    lines: list[str],
    start: int,
    end: int,
    names: dict[str, int],
    pending: dict[str, CStruct],
    base: int,
) -> tuple[list[Field], int, str]:
    fields: list[Field] = []
    offset = base
    index = start
    while index < end:
        current = lines[index].strip()
        if not current or current.startswith("#") or current.startswith("//"):
            index += 1
            continue
        if current.startswith(("template", "public:", "private:", "protected:", "using ")):
            index += 1
            continue
        if "(" in current:
            index = skip_statement(lines, index)
            continue
        if current.startswith("union") or (
            current.startswith("struct") and "{" in current and ":" not in current.split("{", 1)[0]
        ):
            open_at = index
            while open_at < end and "{" not in lines[open_at]:
                open_at += 1
            if open_at >= end:
                return fields, offset, f"unclosed aggregate at line {index + 1}"
            close_at = matching_brace(lines, open_at)
            if current.startswith("union"):
                inner, inner_size, error = layout_union(raw, lines, open_at, close_at, names, pending)
            else:
                inner, inner_size, error = layout_body(raw, lines, open_at + 1, close_at, names, pending, 0)
            if error:
                return fields, offset, error
            fields.extend(shift_fields(inner, offset))
            offset += inner_size
            index = close_at + 1
            continue
        if is_bitfield_text(current):
            group = [index]
            index += 1
            while index < end and is_bitfield_text(lines[index].strip()):
                group.append(index)
                index += 1
            text = ", ".join(lines[item].strip().rstrip(";") for item in group)
            new_offset, error = parse_bitfield(text, group[0] + 1, offset, fields)
            if error:
                return fields, offset, error
            offset = new_offset
            continue
        statement, line_no, index = take_statement(lines, index, end)
        if not statement or statement == "{":
            continue
        ann = annotation_of(raw[line_no - 1]) if line_no - 1 < len(raw) else None
        if ann == 0 and offset > 0:
            ann = None
        # Trust a /*offset*/ only when it jumps past the previous field. A comment that
        # overlaps the type layout, or pads the first byte, is not what pack(1) does.
        if ann is not None and ann > offset and fields and ann - offset > fields[-1].size:
            offset = ann
        next_ann = following_annotation(raw, lines, line_no - 1, end, offset)
        statement = fit_array(statement, offset, next_ann, names)
        placed: list[Field] = []
        new_offset, error = parse_field_line(statement, line_no, offset, placed, names, pending)
        if error:
            return fields, offset, error
        fields.extend(placed)
        offset = new_offset
    return fields, offset, ""


def copy_base(base: CStruct, offset: int, fields: list[Field]) -> int:
    for child in base.fields:
        fields.append(
            Field(
                child.name,
                child.code,
                child.size,
                offset + child.offset,
                child.line,
                child.type_name,
                child.bitfield,
            )
        )
    return offset + base.size


def parse_structs(filename: str, text: str, names: dict[str, int]) -> list[CStruct]:
    raw = text.splitlines()
    lines = strip_comments(text).splitlines()
    found: list[tuple[str, int, int, list[str]]] = []
    index = 0
    while index < len(lines):
        line = lines[index].strip()
        match = re.match(r"(?:typedef\s+)?struct\s+([A-Za-z_]\w*)\b", line)
        if match is None or (";" in line and "{" not in line):
            index += 1
            continue
        name = match.group(1)
        open_at = index if "{" in line else index + 1
        if open_at >= len(lines) or "{" not in lines[open_at]:
            index += 1
            continue
        end = matching_brace(lines, open_at)
        header = lines[index] if "{" in line else f"{lines[index]} {lines[open_at]}"
        found.append((name, index + 1, end + 1, base_names(header)))
        index = end + 1
    pending: dict[str, CStruct] = {}
    ordered: list[CStruct] = []
    spans: dict[tuple[str, int], tuple[int, int, list[str]]] = {}
    for name, start, end, bases in found:
        struct = CStruct(name, filename, start, end, [], 0)
        pending[name] = struct
        ordered.append(struct)
        spans[(name, start)] = (start - 1, end - 1, bases)
    remaining = ordered[:]
    for _pass in range(len(ordered) + 1):
        later: list[CStruct] = []
        for struct in remaining:
            open_at, close_at, bases = spans[(struct.name, struct.start)]
            fields: list[Field] = []
            offset = 0
            error = ""
            for base_name in bases:
                base = pending.get(base_name)
                if base is None or base.error or (not base.fields and base.size == 0):
                    error = f"unknown type {base_name} at line {struct.start}"
                    break
                offset = copy_base(base, offset, fields)
            if not error:
                body, offset, error = layout_body(raw, lines, open_at + 1, close_at, names, pending, offset)
                fields.extend(body)
            if error.startswith("unknown type") and _pass < len(ordered):
                later.append(struct)
                continue
            struct.fields = [] if error else fields
            struct.size = 0 if error else offset
            struct.error = error
        if not later:
            break
        remaining = later
    return ordered


def build_catalog(root: Path) -> Catalog:
    catalog = Catalog(defines=load_defines(root))
    headers = [
        "common/patches/rof2_structs.h",
        "common/eq_packet_structs.h",
        "common/tasks.h",
        "common/net/reliable_stream_structs.h",
    ]
    for filename in headers:
        path = root / filename
        text = path.read_text(errors="replace")
        catalog.lines[filename] = text.splitlines()
        for struct in parse_structs(filename, text, catalog.defines):
            catalog.by_file.setdefault(filename, {})[struct.name] = struct
            catalog.by_name.setdefault(struct.name, []).append(struct)
    return catalog


def source_lines(catalog: Catalog, root: Path, filename: str) -> list[str]:
    cached = catalog.lines.get(filename)
    if cached is not None:
        return cached
    path = root / filename
    if not path.is_file():
        return []
    lines = path.read_text(errors="replace").splitlines()
    catalog.lines[filename] = lines
    return lines


def field_at(struct: CStruct, line: int) -> Field | None:
    for item in struct.fields:
        if item.line == line:
            return item
    return None


def field_named(struct: CStruct, name: str) -> Field | None:
    for item in struct.fields:
        if item.name == name:
            return item
    return None


def match_elements(struct: CStruct, start: int, elements: tuple[Element, ...]) -> str:
    cursor = start
    for element in elements:
        if cursor + element.size > struct.size:
            return f"overruns {struct.name} at {cursor}: format needs {element.size}, struct is {struct.size}"
        if element.code == "x":
            cursor += element.size
            continue
        if element.code == "s":
            covered = cover_bytes(struct, cursor, element.size)
            if covered:
                return covered
            cursor += element.size
            continue
        owner = covering(struct, cursor)
        if (
            owner is not None
            and element.size == 1
            and element.code in {"B", "b"}
            and owner.code == element.code
            and owner.size > 1
        ):
            cursor += 1
            continue
        if owner is None:
            return f"no field at offset {cursor} in {struct.name}"
        if owner.offset != cursor:
            return f"offset {cursor} splits {owner.name} which starts at {owner.offset}"
        if owner.bitfield and owner.size == element.size and owner.code.lower() == element.code.lower():
            cursor += element.size
            continue
        if owner.size != element.size or owner.code != element.code:
            return (
                f"{struct.name}.{owner.name} at {owner.offset} is {owner.code} x {owner.size}, "
                f"format is {element.code} x {element.size}"
            )
        cursor += element.size
    return ""


def covering(struct: CStruct, offset: int) -> Field | None:
    found: Field | None = None
    for item in struct.fields:
        if item.offset <= offset < item.offset + item.size and (found is None or item.size < found.size):
            found = item
    return found


def cover_bytes(struct: CStruct, offset: int, size: int) -> str:
    cursor = offset
    end = offset + size
    while cursor < end:
        owner = covering(struct, cursor)
        if owner is None or owner.code not in {"s", "B"}:
            got = owner.name if owner is not None else "end"
            return f"offset {cursor} expected bytes, found {got}"
        cursor = min(end, owner.offset + owner.size)
    return ""


def cstring_prefix(struct: CStruct) -> int:
    """char Name[1] is the variable-length name. The rest of the struct follows its NUL."""
    if not struct.fields:
        return 0
    first = struct.fields[0]
    if first.offset == 0 and first.code == "s" and first.size == 1:
        return 1
    return 0


def parent_match(catalog: Catalog, struct: CStruct, call: Call, cited_field: Field) -> str:
    """A nested struct's field offset plus the parent's field offset is the packet offset."""
    if call.offset is None:
        return "no parent"
    for rows in catalog.by_name.values():
        for parent in rows:
            if parent.error:
                continue
            for field in parent.fields:
                if field.type_name != struct.name:
                    continue
                if field.offset + cited_field.offset != call.offset:
                    continue
                problem = match_elements(parent, call.offset, call.elements)
                if not problem:
                    return ""
    return "no parent"


def layout_result(
    struct: CStruct,
    call: Call,
    cited_field: Field | None,
    whole_struct: bool,
    catalog: Catalog | None = None,
) -> str:
    if struct.error:
        return f"unresolved: {struct.error}"
    if call.kind == "_need":
        if call.size is None:
            return "unresolved: _need size is not a literal"
        if call.size != struct.size:
            return f"_need {call.size} bytes, {struct.name} is {struct.size}"
        return ""
    if call.kind in {"_put_fixed", "_fixed"}:
        if call.offset is None or call.size is None:
            return "unresolved: fixed-string offset is not a literal"
        if cited_field is not None and (cited_field.offset != call.offset or cited_field.size != call.size):
            return (
                f"{struct.name}.{cited_field.name} is {cited_field.size} bytes at {cited_field.offset}, "
                f"helper uses {call.size} at {call.offset}"
            )
        problem = cover_bytes(struct, call.offset, call.size)
        return problem
    if call.offset is None:
        start = cited_field.offset if cited_field is not None else 0
    else:
        start = call.offset
    packed = sum(item.size for item in call.elements)
    prefix = cstring_prefix(struct)
    if (
        cited_field is not None
        and call.offset is not None
        and prefix
        and call.offset + prefix == cited_field.offset
        and not match_elements(struct, cited_field.offset, call.elements)
    ):
        return ""
    if (
        cited_field is not None
        and catalog is not None
        and call.offset is not None
        and call.offset != cited_field.offset
        and not parent_match(catalog, struct, call, cited_field)
    ):
        return ""
    if cited_field is not None and call.offset is not None and call.offset != cited_field.offset:
        if call.offset <= cited_field.offset < call.offset + packed:
            start = call.offset
        else:
            at_field = match_elements(struct, cited_field.offset, call.elements)
            if at_field:
                return (
                    f"{struct.name}.{cited_field.name} is at {cited_field.offset}, "
                    f"{call.kind} writes at {call.offset}; {at_field}"
                )
            return (
                f"{struct.name}.{cited_field.name} is at {cited_field.offset}, " f"{call.kind} writes at {call.offset}"
            )
    problem = match_elements(struct, start, call.elements)
    if problem:
        return problem
    if whole_struct and call.whole and start == 0 and packed != struct.size:
        return f"pack is {packed} bytes, {struct.name} is {struct.size}"
    return ""


def wire_struct_name(lines: list[str], line: int) -> str:
    start = max(0, line - 160)
    chosen = ""
    for index in range(start, line):
        match = SETUP.search(lines[index])
        if match is not None:
            chosen = match.group(1)
    return chosen


def looks_like_function(line: str) -> bool:
    if re.match(r"\s*ENCODE\(", line) or re.match(r"\s*DECODE\(", line):
        return True
    head = line.split("(", 1)[0]
    if "=" in head:
        return False
    return (
        re.match(
            r"\s*(?:virtual\s+|static\s+)?(?:void|bool|int|auto|unsigned|size_t|uint32_t)\s+[\w:]+\s*$",
            head,
        )
        is not None
    )


def function_open(lines: list[str], line: int) -> int:
    for index in range(line - 1, max(-1, line - 1200), -1):
        if not looks_like_function(lines[index]):
            continue
        opened = index if "{" in lines[index] else None
        if opened is None and index + 1 < len(lines) and lines[index + 1].strip().startswith("{"):
            opened = index + 1
        if opened is None:
            continue
        if matching_brace(lines, opened) >= line - 1:
            return opened
    return max(0, line - 1)


def write_of(line: str) -> tuple[str, int] | None:
    match = WRITE.search(line)
    if match is not None:
        kind = match.group(1)
        if kind in {"String", "LengthString"}:
            return None
        return WRITE_KIND[kind]
    encoded = ENCODE_TYPE.search(line)
    if encoded is not None:
        kind = primitive(encoded.group(1).split("::")[-1])
        if kind is None:
            return None
        return kind
    if ENCODE_STRING.search(line) is not None:
        return None
    return None


def code_only(line: str) -> str:
    return line.split("//", 1)[0]


def loop_bound(line: str, names: dict[str, int]) -> tuple[bool, int | None]:
    match = FOR_HEADER.search(line)
    if match is None:
        return False, None
    bound = eval_count(match.group(4), names)
    start_name, start_expr, cond_name = match.group(1), match.group(2), match.group(3)
    if bound is None:
        return True, None
    if start_name and start_name == cond_name:
        start = eval_count(start_expr, names)
        if start is None:
            return True, None
        if bound < start:
            return True, 0
        return True, bound - start
    return True, bound


def rof_codes(condition: str, if_codes: list[str], else_codes: list[str]) -> list[str] | None:
    """This client is RoF2. Take the branch that encode selects for RoF."""
    if "ClientVersion::RoF" in condition or ("Titanium" in condition and "!=" in condition):
        return if_codes
    if "Titanium" in condition and "==" in condition:
        return else_codes
    if if_codes == else_codes:
        return if_codes
    return None


def task_header_lines() -> list[str]:
    path = repo_root() / "common" / "tasks.h"
    return path.read_text(errors="replace").splitlines()


def selector_span(lines: list[str], call_line: str) -> tuple[list[str], int, int] | None:
    source = (
        lines if any(re.search(r"\bvoid\s+SerializeSelector\s*\(", line) for line in lines) else task_header_lines()
    )
    defs = [index for index, line in enumerate(source) if re.search(r"\bvoid\s+SerializeSelector\s*\(", line)]
    if not defs:
        return None
    chosen = defs[0] if "activity_information" in call_line else defs[-1]
    opened = chosen
    for brace in range(chosen, min(len(source), chosen + 8)):
        if "{" in source[brace]:
            opened = brace
            break
    return source, opened + 1, matching_brace(source, opened)


def _brace_at(lines: list[str], index: int) -> int | None:
    if index < len(lines) and "{" in code_only(lines[index]):
        return index
    nxt = index + 1
    if nxt < len(lines) and code_only(lines[nxt]).strip().startswith("{"):
        return nxt
    return None


def _statement_end(lines: list[str], index: int) -> int:
    """Exclusive end of the statement at index."""
    if index >= len(lines):
        return index
    stripped = code_only(lines[index]).strip()
    brace = _brace_at(lines, index)
    opens = stripped.startswith(("for ", "for(", "if ", "if(", "else", "while", "{"))
    if brace is not None and (opens or "{" in code_only(lines[index])):
        return matching_brace(lines, brace) + 1
    if stripped.startswith(("for ", "for(", "if ", "if(", "while", "else")):
        return _statement_end(lines, index + 1)
    return index + 1


def _branch_size(lines: list[str], header: int, names: dict[str, int]) -> tuple[int, bool, int]:
    """Bytes written by one if or else, and the line to resume after it."""
    brace = _brace_at(lines, header)
    if brace is not None:
        close = matching_brace(lines, brace)
        size, ok = walk_cursor(lines, brace + 1, close, names)
        return size, ok, close + 1
    body = header + 1
    end = _statement_end(lines, body)
    size, ok = walk_cursor(lines, body, end, names)
    return size, ok, end


def walk_cursor(lines: list[str], start: int, target: int, names: dict[str, int]) -> tuple[int, bool]:
    cursor = 0
    certain = True
    index = start
    while index < target and index < len(lines):
        line = code_only(lines[index])
        is_loop, bound = loop_bound(line, names)
        if is_loop and index < target:
            brace = _brace_at(lines, index)
            if brace is not None:
                content_start = brace + 1
                content_end = matching_brace(lines, brace)
                resume = content_end + 1
            else:
                content_start = index + 1
                resume = _statement_end(lines, content_start)
                content_end = resume
            if target < resume:
                inner, inner_ok = walk_cursor(lines, content_start, target, names)
                return cursor + inner, certain and inner_ok and bound is not None
            if bound is None or bound > 4096:
                return cursor, False
            body_size, body_ok = walk_cursor(lines, content_start, content_end, names)
            cursor += body_size * bound
            certain = certain and body_ok
            index = resume
            continue
        stripped = line.strip()
        if stripped.startswith("//") or stripped.startswith("*") or stripped.startswith("/*"):
            index += 1
            continue
        if stripped.startswith("if ") or stripped.startswith("if("):
            brace = _brace_at(lines, index)
            if brace is not None and target <= matching_brace(lines, brace):
                inner, inner_ok = walk_cursor(lines, brace + 1, target, names)
                return cursor + inner, certain and inner_ok
            taken, taken_ok, resume = _branch_size(lines, index, names)
            else_size, else_ok = 0, True
            if resume < len(lines) and code_only(lines[resume]).strip().startswith("else"):
                else_size, else_ok, resume = _branch_size(lines, resume, names)
            if "ClientVersion::RoF" in stripped or ("Titanium" in stripped and "!=" in stripped):
                cursor += taken
                certain = certain and taken_ok
            elif "Titanium" in stripped and "==" in stripped:
                cursor += else_size
                certain = certain and else_ok
            elif taken_ok and else_ok and taken == else_size:
                cursor += taken
            else:
                cursor += taken
                certain = False
            index = resume
            continue
        written_name = WRITE.search(line)
        if ENCODE_STRING.search(line) or (
            written_name is not None and written_name.group(1) in {"String", "LengthString"}
        ):
            return cursor, False
        written = write_of(line)
        if written is not None:
            cursor += written[1]
        index += 1
    return cursor, certain


def write_sequence(
    lines: list[str],
    start: int,
    end: int,
    count: int,
    names: dict[str, int],
    depth: int = 0,
) -> tuple[list[str], bool]:
    codes: list[str] = []
    certain = True
    index = start
    while index < end and index < len(lines) and len(codes) < count:
        line = code_only(lines[index])
        stripped = line.strip()
        if stripped.startswith("//") or stripped.startswith("*") or stripped.startswith("/*"):
            index += 1
            continue
        is_loop, bound = loop_bound(line, names)
        if is_loop:
            body_open = index if "{" in line else index + 1
            body_end = matching_brace(lines, body_open)
            body, body_ok = write_sequence(lines, body_open + 1, body_end, 10000, names, depth)
            repeats = 1 if bound is None else bound
            if repeats > 4096:
                return codes, False
            for _repeat in range(repeats):
                if len(codes) >= count:
                    break
                codes.extend(body[: count - len(codes)])
            certain = certain and body_ok and bound is not None
            index = body_end + 1
            continue
        if stripped.startswith("if ") or stripped.startswith("if("):
            brace = _brace_at(lines, index)
            if brace is not None:
                close = matching_brace(lines, brace)
                if_codes, if_ok = write_sequence(lines, brace + 1, close, 10000, names, depth)
                next_index = close + 1
            else:
                then_end = _statement_end(lines, index + 1)
                if_codes, if_ok = write_sequence(lines, index + 1, then_end, 10000, names, depth)
                next_index = then_end
            else_codes: list[str] = []
            else_ok = True
            if next_index < end and next_index < len(lines) and code_only(lines[next_index]).strip().startswith("else"):
                else_brace = _brace_at(lines, next_index)
                if else_brace is not None:
                    else_close = matching_brace(lines, else_brace)
                    else_codes, else_ok = write_sequence(lines, else_brace + 1, else_close, 10000, names, depth)
                    next_index = else_close + 1
                else:
                    else_end = _statement_end(lines, next_index + 1)
                    else_codes, else_ok = write_sequence(lines, next_index + 1, else_end, 10000, names, depth)
                    next_index = else_end
            chosen = rof_codes(stripped, if_codes, else_codes)
            if chosen is not None:
                codes.extend(chosen[: count - len(codes)])
            certain = certain and if_ok and else_ok and chosen is not None
            index = next_index
            continue
        if depth < 2 and "SerializeSelector(" in line and "void" not in line:
            span = selector_span(lines, line)
            if span is not None:
                source, body_start, body_end = span
                extra, extra_ok = write_sequence(source, body_start, body_end, count - len(codes), names, depth + 1)
                codes.extend(extra)
                certain = certain and extra_ok
                index += 1
                continue
        written_name = WRITE.search(line)
        if ENCODE_STRING.search(line) or (
            written_name is not None and written_name.group(1) in {"String", "LengthString"}
        ):
            codes.append("s")
            index += 1
            continue
        written = write_of(line)
        if written is not None:
            codes.append(written[0])
        index += 1
        if index > start + 200 and not codes:
            break
    return codes, certain


def fixed_string_width(lines: list[str], line_index: int) -> int | None:
    """WriteString followed by SetWritePosition(CurrentPosition + N) is N bytes, not a cstring."""
    if "WriteString" not in lines[line_index]:
        return None
    window = "\n".join(lines[line_index : line_index + 6])
    match = re.search(r"SetWritePosition\s*\(\s*CurrentPosition\s*\+\s*(\d+)\s*\)", window)
    if match is None:
        return None
    return int(match.group(1))


def check_writes(lines: list[str], cite: Cite, call: Call, names: dict[str, int]) -> str:
    if call.kind == "_put_fixed":
        width = fixed_string_width(lines, cite.line - 1)
        if width is None or width != call.size:
            return "unresolved: encoder does not fix the string width"
        cursor, certain = walk_cursor(lines, function_open(lines, cite.line) + 1, cite.line - 1, names)
        if certain and cursor != call.offset:
            return f"encoder cursor is {cursor}, helper writes at {call.offset}"
        return ""
    if not call.elements:
        return "unresolved: helper has no format to compare with encoder writes"
    opened = function_open(lines, cite.line)
    end = matching_brace(lines, opened)
    codes, _certain = write_sequence(lines, cite.line - 1, end, len(call.elements), names)
    if len(codes) < len(call.elements):
        return "unresolved: encoder writes do not cover the format"
    for index, element in enumerate(call.elements):
        if element.code == "x":
            continue
        if element.code == "s" and codes[index] == "s":
            continue
        if not same_code(codes[index], element.code):
            return f"encoder write {index} is {codes[index]}, format is {element.code}"
    if call.offset is None:
        return ""
    cursor, certain = walk_cursor(lines, opened + 1, cite.line - 1, names)
    if not certain:
        return ""
    if cursor != call.offset:
        return f"encoder cursor is {cursor}, {call.kind} writes at {call.offset}"
    return ""


def check_field_assign(catalog: Catalog, lines: list[str], cite: Cite, call: Call) -> str:
    line = lines[cite.line - 1]
    named = EQ_FIELD.search(line)
    if named is None:
        named = OUT_FIELD.search(line)
    sizeof = SIZEOF.search(line)
    wire = wire_struct_name(lines, cite.line)
    if named is None and sizeof is not None:
        wire = sizeof.group(1)
    if not wire and cite.name:
        wire = cite.name
    struct = catalog.get("common/patches/rof2_structs.h", wire) if wire else None
    if struct is None and wire:
        struct = catalog.get(cite.file, wire)
    if struct is None:
        return "unresolved: no wire struct for the encoder line"
    if named is None:
        return layout_result(struct, call, None, True, catalog)
    owner = field_named(struct, named.group(1))
    if owner is None:
        return f"unresolved: {struct.name} has no field {named.group(1)}"
    return layout_result(struct, call, owner, False, catalog)


def primitive_write(source: str) -> tuple[str, int] | None:
    stored = PTR_STORE.search(source)
    if stored is not None:
        return primitive(stored.group(1))
    sized = SIZEOF_PRIMITIVE.search(source)
    if sized is None:
        return None
    return primitive(sized.group(1))


def check_primitive_write(source: str, call: Call) -> str:
    kind = primitive_write(source)
    if kind is None:
        return "unresolved: sizeof type is not a primitive"
    if len(call.elements) != 1:
        return f"write is 1 value, format has {len(call.elements)}"
    code, width = kind
    element = call.elements[0]
    if element.code != code or element.size != width:
        return f"write is {code} x {width}, format is {element.code} x {element.size}"
    return ""


def assigned_struct(catalog: Catalog, lines: list[str], cite: Cite) -> tuple[CStruct | None, str]:
    wire = ""
    for index in range(max(0, cite.line - 80), cite.line):
        found = VAR_STRUCT.search(lines[index])
        if found is not None:
            wire = found.group(1)
    if not wire:
        return None, ""
    struct = catalog.get("common/patches/rof2_structs.h", wire)
    if struct is None:
        struct = catalog.get(cite.file, wire)
    return struct, wire


def declared_wire(lines: list[str], line: int) -> str:
    for index in range(line - 1, min(len(lines), line + 24)):
        match = re.search(r"\b(ReliableStream[A-Za-z0-9_]+)\b", lines[index])
        if match is not None:
            return match.group(1)
    return ""


def shift_width(lines: list[str], line: int) -> int | None:
    window = "\n".join(lines[line - 1 : min(len(lines), line + 6)])
    if "<< 24" in window:
        return 4
    if "<< 8" in window:
        return 2
    return None


def check_one(catalog: Catalog, root: Path, cite: Cite, call: Call | None) -> Result:
    where = f"{Path(cite.py_file).relative_to(mock_root())}:{cite.py_line}"
    label = f"{cite.file}:{cite.line}"
    if cite.name:
        label = f"{label} {cite.name}"
    if call is None:
        return Result("unresolved", where, f"{label} has no pack under it")
    helper = call.kind
    if call.fmt:
        helper = f"{helper} {call.fmt}"
    if call.offset is not None and call.kind != "struct.pack":
        helper = f"{helper} at {call.offset}"
    lines = source_lines(catalog, root, cite.file)
    if not lines or cite.line < 1 or cite.line > len(lines):
        return Result("unresolved", where, f"{label} is outside {cite.file}; {helper}")
    source = strip_comments(lines[cite.line - 1]).strip()
    if primitive_write(source) is not None and "structs::" not in source:
        problem = check_primitive_write(source, call)
        return classify(where, label, helper, problem, "primitive write")
    if EQ_FIELD.search(source) or OUT_FIELD.search(source) or SIZEOF.search(source):
        problem = check_field_assign(catalog, lines, cite, call)
        return classify(where, label, helper, problem, "field assign")
    names = rof2_encode_names(catalog.defines) if cite.file == "common/patches/rof2.cpp" else catalog.defines
    is_loop, _bound = loop_bound(source, names)
    if is_loop or WRITE.search(source) or ENCODE_TYPE.search(source) or ENCODE_STRING.search(source):
        problem = check_writes(lines, cite, call, names)
        return classify(where, label, helper, problem, "encoder writes")
    assigned = FIELD_ASSIGN.search(source)
    if assigned is not None:
        struct, wire = assigned_struct(catalog, lines, cite)
        if struct is None:
            return Result("unresolved", where, f"{label} field {assigned.group(1)} has no wire struct; {helper}")
        owner = field_named(struct, assigned.group(1))
        if owner is None:
            return Result("unresolved", where, f"{label} {wire} has no field {assigned.group(1)}; {helper}")
        problem = layout_result(struct, call, owner, False, catalog)
        return classify(where, label, helper, problem, f"{struct.name}.{owner.name}")
    cast = CAST_STRUCT.search(source)
    if cast is not None:
        struct = catalog.get("common/patches/rof2_structs.h", cast.group(1))
        if struct is None:
            return Result("unresolved", where, f"{label} unknown struct {cast.group(1)}; {helper}")
        problem = layout_result(struct, call, None, True, catalog)
        return classify(where, label, helper, problem, f"{struct.size} bytes")
    if "PutSerialize" in "\n".join(lines[cite.line - 1 : cite.line + 12]) or "SendOutOfOrderAck" in source:
        wire = declared_wire(lines, cite.line)
        struct = catalog.get(cite.file, wire) if wire else None
        if struct is None and wire:
            struct = catalog.get("common/net/reliable_stream_structs.h", wire)
        if struct is not None:
            problem = layout_result(struct, call, None, True, catalog)
            return classify(where, label, helper, problem, f"{struct.size} bytes")
    sized = APP_SIZE.search(source)
    if sized is not None:
        expected = int(sized.group(1))
        packed = sum(item.size for item in call.elements)
        if packed != expected:
            return Result("fail", where, f"{label} handler expects {expected} bytes, pack is {packed}; {helper}")
        return Result("ok", where, f"{label} {expected} bytes; {helper}")
    if "subpacket_length" in source or ("<<" in source and "current" in source):
        width = shift_width(lines, cite.line)
        if width is not None and len(call.elements) == 1 and call.elements[0].size == width:
            return Result("ok", where, f"{label} {width}-byte length; {helper}")
    if "ENCODE(" in source:
        for index in range(cite.line - 1, min(len(lines), cite.line + 12)):
            match = SETUP.search(lines[index])
            if match is None:
                continue
            struct = catalog.get("common/patches/rof2_structs.h", match.group(1))
            if struct is None:
                break
            problem = layout_result(struct, call, None, True, catalog)
            return classify(where, label, helper, problem, f"{struct.size} bytes")
    struct = catalog.at(cite.file, cite.line)
    if cite.name and (struct is None or struct.name != cite.name):
        named = catalog.get(cite.file, cite.name)
        if named is None:
            return Result("unresolved", where, f"{label} is not a parsed struct; {helper}")
        if not (named.start - 5 <= cite.line <= named.end):
            return Result(
                "fail",
                where,
                f"{label} is line {cite.line}, {cite.name} is lines {named.start}-{named.end}; {helper}",
            )
        struct = named
    if struct is not None:
        cited_field = field_at(struct, cite.line)
        whole = cited_field is None
        problem = layout_result(struct, call, cited_field, whole, catalog)
        return classify(where, label, helper, problem, f"{struct.size} bytes")
    return Result("unresolved", where, f"{label} is not a struct field or an encoder write; {helper}")


def classify(where: str, label: str, helper: str, problem: str, ok_note: str) -> Result:
    if problem.startswith("unresolved"):
        return Result("unresolved", where, f"{label} {problem}; {helper}")
    if problem:
        return Result("fail", where, f"{label} {problem}; {helper}")
    return Result("ok", where, f"{label} {ok_note}; {helper}")


def collect(catalog: Catalog, root: Path) -> list[Result]:
    results: list[Result] = []
    structs = mock_root() / "eqclient3" / "structs"
    for path in sorted(structs.glob("*.py")):
        text = path.read_text()
        pending: list[Cite] = []
        lines = text.splitlines()
        for number, line in enumerate(lines, start=1):
            cites = cites_on(path, line, number)
            if cites:
                pending.extend(cites)
                continue
            if not line.strip():
                continue
            match = HELPER.search(line)
            if match is not None and pending:
                call = read_call(text, sum(len(item) + 1 for item in lines[: number - 1]) + match.start())
                for cite in pending:
                    results.append(check_one(catalog, root, cite, call))
                pending = []
                continue
            if not line.strip().startswith("#"):
                pending = []
    return results


def main() -> int:
    root = repo_root()
    catalog = build_catalog(root)
    broken = [struct for rows in catalog.by_name.values() for struct in rows if struct.error]
    results = collect(catalog, root)
    counts = {"ok": 0, "fail": 0, "unresolved": 0}
    for result in results:
        counts[result.status] += 1
        if result.status != "ok":
            print(f"{result.status.upper():11} {result.where}  {result.detail}")
    print(
        f"\n{counts['ok']} ok, {counts['fail']} fail, {counts['unresolved']} unresolved "
        f"({len(results)} cited packs, {len(broken)} structs the parser could not size)"
    )
    return 1 if counts["fail"] or counts["unresolved"] else 0


if __name__ == "__main__":
    sys.exit(main())
