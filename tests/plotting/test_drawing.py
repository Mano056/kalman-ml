import matplotlib.pyplot as plt
from datetime import datetime
import pytest

from core import Bar, PositionSeries, PriceSeries
from backtesting import BacktestResult
from plotting.drawing import draw_signals, draw_equity

def make_series():
    return PriceSeries(
        [
            Bar(timestamp=datetime(2024, 1, 1), open=100, high=101, low=99, close=100, volume=1000),
            Bar(timestamp=datetime(2024, 1, 2), open=101, high=102, low=100, close=101, volume=1000),
            Bar(timestamp=datetime(2024, 1, 3),open=102, high=103, low=101, close=102, volume=1000),
            Bar(timestamp=datetime(2024, 1, 4), open=103, high=104, low=102, close=103, volume=1000),
        ]
    )

def test_draw_signals_no_markers():
    _, ax = plt.subplots()

    positions = PositionSeries([0, 0, 0, 0])

    draw_signals(
        ax, 
        make_series(),
        positions,
    )

    assert len(ax.lines) == 0

def test_draw_signals_buy_marker():
    _, ax = plt.subplots()

    positions = PositionSeries([0, 1, 1, 1])

    draw_signals(
        ax, 
        make_series(),
        positions,
    )

    assert len(ax.lines) == 1

def test_draw_signals_buy_and_sell():
    _, ax = plt.subplots()

    positions = PositionSeries([0, 1, 1, 0])

    draw_signals(
        ax, 
        make_series(),
        positions,
    )

    assert len(ax.lines) == 2

def test_draw_signals_length_mismatch():
    _, ax = plt.subplots()

    positions = PositionSeries([0,1])

    with pytest.raises(ValueError):
        draw_signals(
            ax,
            make_series(),
            positions,
        )

def make_backtest_result():
    return BacktestResult(
        initial_cash=10_000,
        final_equity=10_500,
        trades=[],
        equity_curve=[
            10000,
            10100,
            10050,
            10300,
            10500,
        ]
    )

def test_draw_equity_draws_line():
    _, ax = plt.subplots()

    draw_equity(
        ax,
        make_backtest_result(),
    )

    assert len(ax.lines) == 1
    assert ax.lines[0].get_label() == "Equity"

def test_draw_equity_empty_curve_raises():
    _, ax = plt.subplots()

    result = BacktestResult(
        initial_cash=10000,
        final_equity=10000,
        trades=[],
        equity_curve=[],
    )

    with pytest.raises(ValueError):
        draw_equity(
            ax,
            result,
        )