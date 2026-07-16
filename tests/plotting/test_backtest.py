import matplotlib.pyplot as plt
from datetime import datetime
import pytest
from matplotlib.figure import Figure

from core import Bar, PositionSeries, PriceSeries
from backtesting import BacktestResult
from indicators import KalmanIndicator
from config import KalmanConfig
from indicators import IndicatorResult
from plotting.drawing import draw_signals, draw_equity, draw_indicator,draw_price
from plotting.backtest import plot_backtest


def test_plot_backtest_returns_figure(
        series,
        positions,
        portfolio,
        indicator,
):
    fig = plot_backtest(
        series,
        positions,
        portfolio,
        [indicator],
    )

    assert isinstance(fig, Figure)

def test_plot_backtest_contains_two_axes(
        series,
        positions,
        portfolio,
        indicator,
):
    fig = plot_backtest(
        series,
        positions,
        portfolio,
        [indicator],
    )

    assert len(fig.axes) == 2

def test_plot_backtest_price_axis(
        series,
        positions,
        portfolio,
        indicator,
):
    fig = plot_backtest(
        series,
        positions,
        portfolio,
        [indicator],
    )

    ax = fig.axes[0]

    assert len(ax.lines) >= 2

def test_plot_backtest_equity_axis(
        series,
        positions,
        portfolio,
        indicator,
):
    fig = plot_backtest(
        series,
        positions,
        portfolio,
        [indicator],
    ) 

    ax = fig.axes[1]

    assert len(ax.lines) == 1

def test_plot_backtest_multiple_indicators(
        series,
        positions,
        portfolio,
        indicator,
):
    fig = plot_backtest(
        series,
        positions,
        portfolio,
        [indicator, indicator]
    )

    price_ax = fig.axes[0]

    assert len(price_ax.lines) >= 3