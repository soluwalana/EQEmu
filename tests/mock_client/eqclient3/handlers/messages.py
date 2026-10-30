"""Channel and special lines go to the log. SimpleMessage updates the sheet.

A line that names work is appended by ReadTasks while it is waiting in the mine.
Deeds strings 1166-1171 append FetchFaction. Race and class refusals do not.

These three opcodes are exclusive. The parsed line is handed to every waiter.
"""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.world import Faction
    from eqclient3.action import Action

import re
from eqclient3.log import log
from eqclient3.actions.fetch_faction import FetchFaction
from eqclient3.data.factions import ensure_factions
from eqclient3.actions.support import line_of
from eqclient3.handlers.common import character_name, find_mob, mob_named, enqueue_once, queue_of, write_log
from eqclient3.structs import EQStruct, OP_ChannelMessage, OP_SimpleMessage, OP_SpecialMesg
from eqclient3.handler import Handler
TOO_FAR = 124
DEEDS = range(1166, 1172)
WONT_SELL = range(1154, 1166)
WORST = 469
WORSE = 470
BEST = 471
BETTER = 472
_SPELL_SETTING = 'successfully added spell setting for'
_FACTION = re.compile('your faction standing with (.+) has been adjusted by (-?\\d+)\\.', re.IGNORECASE)

class MessagesHandler(Handler):
    opcodes = ('OP_ChannelMessage', 'OP_SpecialMesg', 'OP_SimpleMessage')
    exclusive = opcodes

    def on(self, opcode: str, payload: EQStruct) -> None:
        del opcode
        if isinstance(payload, (OP_ChannelMessage, OP_SpecialMesg)):
            self.deliver_waiters(payload)
            speaker, text = line_of(payload)
            self.log(speaker, text)
            self.spell_setting(text)
            self.adjusted(text)
        elif isinstance(payload, OP_SimpleMessage):
            self.simple(payload)

    def log(self, speaker: str, text: str) -> None:
        if speaker:
            write_log(f'{speaker}: {text}')
        elif text:
            write_log(text)

    def spell_setting(self, text: str) -> None:
        stripped = (text or '').strip()
        if not stripped.lower().startswith(_SPELL_SETTING):
            return
        bot = stripped[len(_SPELL_SETTING):].rstrip('.').strip()
        journal = self.loop.journal
        if not journal or not bot:
            return
        journal.set_bot_setting(character_name(self.loop, self.world), bot, 'spells', '1')

    def simple(self, row: OP_SimpleMessage) -> None:
        self.deliver_waiters(row)
        string_id = int(row.string_id)
        texts = list(row.texts)
        text = ' '.join(texts)
        if string_id == TOO_FAR:
            return
        if string_id in DEEDS:
            self.deeds(texts)
            return
        if string_id in WONT_SELL:
            return
        if string_id in (WORST, WORSE, BEST, BETTER):
            name = texts[0] if texts else ''
            self.faction_message(string_id, name, text)

    def deeds(self, texts: list[str]) -> None:
        faction_id = self.deeds_faction(texts)
        if not faction_id:
            return
        enqueue_once(self.loop, self.world, FetchFaction(faction_id), f'faction:{faction_id}')

    def deeds_faction(self, texts: list[str]) -> int:
        world = self.world
        if texts:
            mob = mob_named(world, texts[0])
            if mob and mob.faction_id:
                return mob.faction_id
        trade = self.open_trade()
        if not trade:
            return 0
        partner = trade.partner
        mob = find_mob(world, partner) if isinstance(partner, int) or str(partner).isdigit() else mob_named(world, str(partner))
        if not mob and not isinstance(partner, int):
            mob = mob_named(world, str(partner))
        if not mob:
            return 0
        return mob.faction_id

    def open_trade(self) -> Action | None:
        for action in queue_of(self.loop):
            if type(action).__name__ == 'Trade' and (not action.complete):
                return action
        return None

    def faction_message(self, string_id: int, name: str, text: str) -> None:
        faction_id = self.faction_id(name)
        if not faction_id:
            return
        row = self.faction(faction_id, name)
        if string_id == BEST:
            row.maxed = 1
            row.changed = False
            return
        if string_id == WORST:
            row.maxed = -1
            row.changed = False
            return
        delta = _delta(text)
        if row.maxed:
            if delta is not None and row.amount is not None:
                row.amount = row.amount + delta
                self.journal_delta(name, delta)
            return
        if delta is not None and row.amount is not None:
            row.amount = row.amount + delta
            self.journal_delta(name, delta)
            return
        row.changed = True

    def adjusted(self, text: str) -> None:
        match = _FACTION.search((text or '').strip())
        if not match:
            return
        name = match.group(1).strip()
        delta = int(match.group(2))
        faction_id = self.faction_id(name)
        if not faction_id:
            return
        row = self.faction(faction_id, name)
        if row.maxed:
            return
        if row.amount is None:
            row.changed = True
            return
        row.amount = row.amount + delta
        self.journal_delta(name, delta)

    def faction_id(self, name: str) -> int:
        key = ' '.join((name or '').lower().split())
        if not key:
            return 0
        names = self.world.faction_names or {}
        if key in names:
            return int(names[key])
        try:
            book = ensure_factions()
        except Exception:
            log.error("faction book failed to load", exc_info=True)
            book = None
        if book:
            table = book.by_name or book.names
            if isinstance(table, dict) and key in table:
                return int(table[key])
        return 0

    def faction(self, faction_id: int, name: str) -> Faction:
        row = self.world.faction(faction_id)
        key = ' '.join((name or '').lower().split())
        if key:
            self.world.faction_names[key] = faction_id
        return row

    def journal_delta(self, name: str, delta: int) -> None:
        """An absolute is stored only when the journal already has one. A delta is not written onto 0."""
        journal = self.loop.journal
        if not journal or not name:
            return
        flags = journal.flag_values(character_name(self.loop, self.world))
        if name not in flags or flags[name] == 0:
            return
        journal.set_flag(character_name(self.loop, self.world), name, int(flags[name]) + delta)

def _delta(text: str) -> int | None:
    match = _FACTION.search(text or '')
    if not match:
        found = re.search('adjusted by (-?\\d+)', text or '', re.IGNORECASE)
        if not found:
            return None
        return int(found.group(1))
    return int(match.group(2))
