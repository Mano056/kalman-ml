from __future__ import annotations

import matplotlib.pyplot as plt
from matplotlib.figure import Figure


from indicators import IndicatorResult
from .drawing import draw_price, draw_indicator


def plot_indicator(
        result: IndicatorResult,
) -> Figure:
    """
    Plot a PriceSeries with an indicator overlay.
    """
    if result is None:
        raise TypeError("Result cannot be None.")
    
    if not isinstance(result, IndicatorResult):
        raise TypeError("Result must be a IndicatorResult.")
    
    series = result.price_series

    fig, ax = plt.subplots()

    draw_price(
        ax,
        result.price_series,
    )

    draw_indicator(
        ax,
        result,
    )

    ax.set_title(result.name)
    ax.set_xlabel("Bar")
    ax.set_ylabel("Output")
    ax.legend()

    fig.tight_layout()

    return fig