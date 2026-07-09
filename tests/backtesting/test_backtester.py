from datetime import datetime

from backtesting import Backtester
from core import Bar, PositionSeries, PriceSeries


def test_flat_strategy_preserves_cash() -> None:
    bars = [
        Bar(
            timestamp=datetime(2024, 1, 1),
            open=100,
            high=100,
            low=100,
            close=100,
            volume=1000,
        ),
        Bar(
            timestamp=datetime(2024, 1, 2),
            open=101,
            high=101,
            low=101,
            close=101,
            volume=1000,
        ),
    ]

    series = PriceSeries(bars)

    position = PositionSeries([
        0.0,
        0.0,
    ])

    result = Backtester(initial_cash=10_000).run(
        series,
        position,
    )

    assert result.initial_cash == 10_000
    assert result.final_equity == 10_000
    assert result.trades == []
    assert result.equity_curve == [10_000, 10_000]

def test_position_change_creates_trade() -> None:
    bars = [
        Bar(
            timestamp=datetime(2024, 1, 1), 
            open=100, 
            high=100, 
            low=100, 
            close=100, 
            volume=1000
        ),
        Bar(
            timestamp=datetime(2024, 1, 2), 
            open=101, 
            high=101, 
            low=101, 
            close=101, 
            volume=1000
        ),
    ]

    series = PriceSeries(bars)

    positions = PositionSeries([
        0.0,
        1.0,
    ])

    result = Backtester().run(series, positions)

    assert len(result.trades) == 1

    trade = result.trades[0]

    assert trade.timestamp == bars[1].timestamp
    assert trade.price == 101
    assert trade.previous_position == 0.0
    assert trade.new_position == 1.0

def test_profitable_long_trade_increase_equity() -> None:
    bars = [
        Bar(datetime(2024, 1, 1), 100, 100, 100, 100, 1000),
        Bar(datetime(2024, 1, 2), 100, 100, 100, 100, 1000),
        Bar(datetime(2024, 1, 3), 110, 110, 110, 110, 1000),
        Bar(datetime(2024, 1, 4), 110, 110, 110, 110, 1000),
    ]

    series = PriceSeries(bars)

    positions = PositionSeries([
        0.0,
        1.0,
        1.0,
        0.0, 
    ])

    result = Backtester(initial_cash=10_000).run(
        series,
        positions,
    )

    assert result.final_equity == 11_000