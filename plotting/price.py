from __future__ import annotations

from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from core import PriceSeries


def plot_price(series: PriceSeries) -> Figure:
    """
    Plot a PriceSeries.
    
    Parameters
    ----------
    series
        The price series to be plotted.
    
    Returns
    -------
    Figure
        A matplotlib Figure containing the price chart.
    """
    if series is None:
        raise TypeError("Series cannot be None.")
    
    if not isinstance(series, PriceSeries):
        raise TypeError("Series must be a PriceSeries.")
    
    if len(series) == 0:
        raise ValueError("PriceSeries is empty.")
    
    fig, ax = plt.subplots()

    ax.plot(series.closes)

    ax.set_title("Price")
    ax.set_xlabel("Bar")
    ax.set_ylabel("Close")

    fig.tight_layout()

    return fig
