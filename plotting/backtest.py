from __future__ import annotations

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from collections.abc import Sequence

from core import PositionSeries, PriceSeries
from indicators import IndicatorResult
from backtesting import BacktestResult

from .drawing import draw_equity, draw_indicator, draw_price, draw_signals


def plot_backtest(
        series: PriceSeries,
        positions: PositionSeries,
        result: BacktestResult,
        indicators: Sequence[IndicatorResult],
) -> Figure:
    """
    Plot a complete backtest consisting of:
    
    - Price
    - Indicator
    - Buy / sell markers
    - Equity curve
    """

    fig, (price_ax, equity_ax) = plt.subplots(
        2, 
        1, 
        sharex=True,
        height_ratios=[3, 1],
    )

    draw_price(price_ax, series)
    
    for indicator in indicators:
        draw_indicator(price_ax, indicator)
        
    draw_signals(price_ax, series, positions)

    draw_equity(equity_ax, result)

    price_ax.set_title("Backtest")
    price_ax.set_ylabel("Price")

    equity_ax.set_xlabel("Bar")
    equity_ax.set_ylabel("Equity")

    price_ax.legend()
    equity_ax.legend()

    fig.tight_layout()

    return fig