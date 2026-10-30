"""Opcode coverage for handlers/trade.py."""

import struct

from eqclient3.handlers import trade
from support import Loop, World, names


class Trade:
    """Queue stand-in. The handler matches the class name and does not import Trade."""

    def __init__(self, partner, item):
        self.partner = partner
        self.item = item
        self.complete = False
        self.source = ""


def test_opcodes():
    world = World()
    closed = Loop()
    trade.TradeHandler().handle("OP_TradeRequest", struct.pack("<II", 9, 7), world, closed)
    assert closed.queue == []
    assert closed.sent[0][0] == "OP_CancelTrade"
    assert "FetchFaction" not in names(closed)

    open_trade = Loop()
    deal = Trade(9, 100)
    open_trade.append(deal)
    trade.TradeHandler().handle("OP_TradeRequest", struct.pack("<II", 9, 7), world, open_trade)
    assert open_trade.sent[0][0] == "OP_TradeRequestAck"
    assert open_trade.sent[0][1] == struct.pack("<II", 7, 9)
    trade.TradeHandler().handle("OP_ShopRequest", struct.pack("<IIIf", 9, 7, 0, 1.0), world, open_trade)
    assert deal.complete is True
    assert names(open_trade) == ["Trade"]
