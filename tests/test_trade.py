from datetime import datetime

from core.trade import Trade


def test_trade_creation() -> None:
    trade = Trade(
        entry_time=datetime(2024, 1, 1),
        exit_time=datetime(2024, 1, 2),
        entry_price=100.0,
        exit_price=101.0,
        direction=1.0,
        return_pct=0.15
    )

    assert trade.entry_price == 100.0
    assert trade.direction == 1.0