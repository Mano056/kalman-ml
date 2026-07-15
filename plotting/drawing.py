from __future__ import annotations

from matplotlib.axes import Axes

from core import PriceSeries
from indicators import IndicatorResult


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