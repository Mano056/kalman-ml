from datetime import datetime, timedelta
import pytest

from core import Bar, PositionSeries, PriceSeries
from backtesting import Backtester


def make_series(closes: list[float]) -> PriceSeries:
    bars = []

    for i, close in enumerate(closes):
        bars.append(
            Bar(
                timestamp=datetime(2024, 1, 1) + timedelta(hours=i),
                open=close,
                high=close,
                low=close,
                close=close,
                volume=1000,
            )
        )

    return PriceSeries(bars)

def test_winning_long_trade() -> None:
    series = make_series([
        100,
        100,
        110,
        110,
    ])

    positions = PositionSeries([
        0,
        1,
        1,
        0,
    ])

    result = Backtester().run(
        series,
        positions,
    )

    expected = Backtester().initial_cash * (110 / 100)

    assert result.final_equity == pytest.approx(expected)
    assert len(result.equity_curve) == len(series)

def test_losing_long_trade() -> None:
    series = make_series([
        100,
        100,
        90,
        90,
    ])

    positions = PositionSeries([
        0,
        1,
        1,
        0,
    ])

    result = Backtester().run(
        series,
        positions,
    )

    expected = Backtester().initial_cash * (90 / 100)

    assert result.final_equity == pytest.approx(expected)
    assert len(result.equity_curve) == len(series)

def test_winning_short_trade() -> None:
    series = make_series([
        100,
        100,
        90,
        90,
    ])

    positions = PositionSeries([
        0,
        -1,
        -1,
        0,
    ])

    result = Backtester().run(
        series,
        positions,
    )

    expected = Backtester().initial_cash * (100 / 90)

    assert result.final_equity == pytest.approx(expected)
    assert len(result.equity_curve) == len(series)

def test_losing_short_trade() -> None:
    series = make_series([
        100,
        100,
        110,
        110,
    ])

    positions = PositionSeries([
        0,
        -1,
        -1,
        0
    ])

    result = Backtester().run(
        series,
        positions,
    )

    expected = Backtester().initial_cash * (100 / 110)

    assert result.final_equity == pytest.approx(expected)
    assert len(result.equity_curve) == len(series)

def test_market_equity_curve() -> None:
    series = make_series([
        100,
        100,
        110,
        120,
        120,
    ])

    postions = PositionSeries([
        0,
        1,
        1,
        1,
        0,
    ])

    result = Backtester().run(
        series,
        postions,
    )

    assert result.equity_curve == pytest.approx([
        10000,
        10000,
        11000,
        12000,
        12000,
    ])