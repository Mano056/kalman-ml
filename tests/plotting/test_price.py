import matplotlib
import pytest
import matplotlib.pyplot as plt

from plotting import plot_price
from core import Bar, PriceSeries
from datetime import datetime


def make_series() -> PriceSeries:
    return PriceSeries(
        [
            Bar(timestamp=datetime(2024, 1, 1), open=100, high=101, low=99,close=100, volume=1000),
            Bar(timestamp=datetime(2024, 1, 2), open=100, high=102, low=99, close=101, volume=1000),
            Bar(timestamp=datetime(2024, 1, 3), open=101, high=103, low=100, close=102, volume=1000),
        ]
    )

def test_plot_price_returns_figure() -> None:
    series = make_series()

    fig = plot_price(series)

    assert isinstance(fig, matplotlib.figure.Figure)

def test_plot_price_contains_single_axes() -> None:
    series = make_series()

    fig = plot_price(series)

    assert len(fig.axes) == 1

def test_plot_price_contains_single_line() -> None:
    series = make_series()

    fig = plot_price(series)

    ax = fig.axes[0]

    assert len(ax.lines) == 1

def test_plot_price_none_raises() -> None:
    with pytest.raises(TypeError):
        plot_price(None)

def test_plot_price_empty_series_raises() -> None:
    series = PriceSeries([])

    with pytest.raises(ValueError):
        plot_price(series)

