"""Recover speech text from Perl/Lua EQ quest expressions without executing scripts.

Handles literal concatenations and quest::saylink/eq.say_link in speech
calls. Dynamic expressions remain in the output as placeholders, so this
is a conservative static renderer, not a Perl/Lua evaluator.
"""
from __future__ import annotations

import re
from collections.abc import Iterator

_SPEECH_CALL = re.compile(
    r"(?<![\w:])(?P<call>quest::say|quest:say|quest::emote|quest:emote|e\.self:Say|e\.self:Emote|e\.self:QuestSay|eq\.say|eq\.emote|e\.other:Message|\$client->Message)\s*\(",
    re.IGNORECASE,
)
_STRING = re.compile(r'''"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*' ''', re.X | re.S)
_VARIABLE = re.compile(r"\$[A-Za-z_]\w*(?:\{[^}]+\})?")


def _end_call(text: str, opener: int) -> int:
    """Closing parenthesis, ignoring parentheses within quoted literals/comments."""
    depth = 0
    quote = None
    i = opener
    while i < len(text):
        ch = text[i]
        if quote:
            if ch == "\\":
                i += 2
                continue
            if ch == quote:
                quote = None
        elif ch in ('"', "'"):
            quote = ch
        elif ch == "(" :
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth == 0:
                return i
        elif ch == "#" and (i == 0 or text[i-1].isspace()):
            # Perl line comments outside strings.
            end = text.find("\n", i)
            i = end if end >= 0 else len(text)
            continue
        i += 1
    return -1


def _unquote(value: str) -> str:
    quote = value[0]
    inner = value[1:-1]
    # Keep unknown escapes verbatim, but unescape literal quote/backslash.
    inner = inner.replace('\\' + quote, quote).replace('\\\\', '\\')
    if quote == '"':
        inner = inner.replace(r'\n', '\n').replace(r'\t', '\t')
    return inner

# A say link contains a target, a boolean flag, and optionally an explicit
# visible label. It contributes ONE visible phrase, not each argument.
_SAY_LINK = re.compile(r"(?<![\w:])(?:quest::saylink|eq\.say_link|eq\.saylink)\s*\(", re.I)
_CALL = re.compile(r"[A-Za-z_][\w:]*(?:(?:\.|->|:)[A-Za-z_]\w*)*\s*\(")


def _literal_link(expr: str) -> str:
    """A static saylink argument; never mistake a dynamic expression for text."""
    expr = expr.strip()
    match = _STRING.fullmatch(expr)
    return _unquote(expr) if match else ""


def _say_links(expr: str) -> list[dict[str, str]]:
    """Return link command and displayed text independently, in source order."""
    result: list[dict[str, str]] = []
    for found in _SAY_LINK.finditer(expr):
        end = _end_call(expr, found.end() - 1)
        if end < 0:
            continue
        args = _top_level_arguments(expr[found.end():end])
        if not args:
            continue
        target = _literal_link(args[0])
        label = _literal_link(args[2]) if len(args) >= 3 else target
        if target:
            result.append({'target': target, 'label': label or target})
    return result


def _render(expr: str) -> str:
    """Concatenate quoted fragments and simple Perl interpolations in source order.

    Only literal strings and $variables are emitted; saylink labels are
    ordinary nested literals. Dynamic calls that generate text are NOT resolved.
    """
    out: list[str] = []
    i = 0
    while i < len(expr):
        string = _STRING.match(expr, i)
        if string:
            out.append(_unquote(string.group()))
            i = string.end()
            continue
        link = _SAY_LINK.match(expr, i)
        if link:
            close = _end_call(expr, link.end() - 1)
            if close >= 0:
                arguments = _top_level_arguments(expr[link.end():close])
                # The third argument is the display label, not a second link.
                # If it is dynamic, fall back to the link's first argument.
                shown = (arguments[2] if len(arguments) >= 3 else arguments[0]) if arguments else ""
                rendered = _literal_link(shown)
                if not rendered and arguments:
                    rendered = _literal_link(arguments[0])
                out.append(rendered)
                i = close + 1
                continue
        call = _CALL.match(expr, i)
        if call:
            close = _end_call(expr, call.end() - 1)
            if close >= 0:
                # Unknown functions may evaluate to text at runtime; don't
                # accidentally present their argument literals as NPC speech.
                i = close + 1
                continue
        variable = _VARIABLE.match(expr, i)
        if variable:
            out.append(variable.group())
            i = variable.end()
            continue
        i += 1
    return ''.join(out)


def _top_level_arguments(expr: str) -> list[str]:
    """Split a call's arguments without splitting nested calls or quoted commas."""
    parts: list[str] = []
    start = 0
    depth = 0
    quote: str | None = None
    i = 0
    while i < len(expr):
        char = expr[i]
        if quote:
            if char == "\\":
                i += 2
                continue
            if char == quote:
                quote = None
        elif char in ('"', "'"):
            quote = char
        elif char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
        elif char == ',' and depth == 0:
            parts.append(expr[start:i].strip())
            start = i + 1
        i += 1
    parts.append(expr[start:].strip())
    return parts



def iter_speech_calls(text: str, lo: int = 0, hi: int | None = None) -> Iterator[dict]:
    """Yield full static speech records with original source offsets."""
    hi = len(text) if hi is None else hi
    for match in _SPEECH_CALL.finditer(text, lo, hi):
        opener = match.end() - 1
        end = _end_call(text, opener)
        if end < 0 or end >= hi:
            continue
        name = match.group('call').lower()
        expression = text[opener + 1:end]
        # Player-directed messages have a leading color/type argument.
        # e.other:Message(MT.DarkGray, "NPC says ...")
        # $client->Message(15, "NPC says ...")
        # QuestSay(client, text) is another NPC speech API. Its first
        # argument selects the recipient and is not part of the dialogue.
        if name.endswith('message') or name.endswith('questsay'):
            arguments = _top_level_arguments(expression)
            if len(arguments) < 2:
                continue
            expression = arguments[1]
        
        msg = 'say'
        if name.endswith('message'):
            msg = 'message'
        elif name.endswith('emote'):
            msg = 'emote'
        yield {
            'offset': match.start(),
            'channel': msg,
            'text': _render(expression),
            'links': _say_links(expression),
        }
