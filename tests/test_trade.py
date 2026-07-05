from datetime import datetime

from core.trade import Trade


def test_trade_creation() -> None:
    trade = Trade(
        timestamp=datetime(2024, 1, 1),
        price=100.0,
        previous_position=0.0,
        new_position=1.0,
    )

    assert trade.price == 100.0
    assert trade.position_change == 1.0


def test_trade_reverse() -> None:
    trade = Trade(
        timestamp=datetime(2024, 1, 2),
        price=105.0,
        previous_position=1.0,
        new_position=-1.0,
    )

    assert trade.position_change == -2.0