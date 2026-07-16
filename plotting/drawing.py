from __future__ import annotations

from matplotlib.axes import Axes

from core import PriceSeries, PositionSeries
from indicators import IndicatorResult
from backtesting import BacktestResult


def draw_price(
        ax: Axes,
        series: PriceSeries,
) -> None:
    """
    Draw a price series.
    """
    ax.plot(series.closes, label="Price")

def draw_indicator(
        ax: Axes,
        result: IndicatorResult,
) -> None:
    """
    Draw all outputs from an indicator.
    """
    for name in result.output_names:
        ax.plot(result.output(name), label=name)

def draw_signals(
        ax: Axes,
        series: PriceSeries,
        positions: PositionSeries,
) -> None:
    """
    Draw buy and sell markers.
    """
    if len(series) != len(positions):
        raise ValueError("PriceSeries and PositionSeries must have the same length.")
    
    previous = 0

    for i, (bar, position) in enumerate(zip(series, positions)):
        
        # Buy
        if previous == 0 and position == 1:
            ax.plot(
                i, 
                bar.close, 
                marker="^",
                linestyle="None",
            )
        
        # Sell
        elif previous == 1 and position == 0:
            ax.plot(
                i,
                bar.close,
                marker="v",
                linestyle="None"
            )
        
        # Short
        elif previous == 0 and position == -1:
            ax.plot(
                i,
                bar.close,
                marker="v",
                linestyle="None"
            )

        # Cover
        elif previous == -1 and position == 0:
            ax.plot(
                i,
                bar.close,
                marker="^",
                linestyle="None"
            )

        # Reversal to short
        elif previous == 1 and position == -1:
            ax.plot(
                i,
                bar.close,
                marker="v",
                linestyle="None"
            )

        # Reversal to long
        elif previous == -1 and position == 1:
            ax.plot(
                i,
                bar.close,
                marker="^",
                linestyle="None"
            )

        previous = position

def draw_equity(
        ax: Axes,
        result: BacktestResult,     
) -> None:
    """
    Draw the equity curve for a backtest.
    """
    if len(result.equity_curve) == 0:
        raise ValueError("BacktestResult contains an empty equity curve.")
    
    ax.plot(result.equity_curve, label="Equity")