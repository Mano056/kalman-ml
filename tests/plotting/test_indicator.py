from datetime import datetime
import matplotlib
import pytest

from core import Bar, PriceSeries
from indicators import IndicatorResult
from plotting import plot_indicator
from indicators import KalmanIndicator
from config import KalmanConfig
from plotting.drawing import draw_indicator, draw_price


def make_series() -> PriceSeries:
    return PriceSeries(
        [
            Bar(timestamp=datetime(2024, 1, 1), open=100, high=101, low=99,close=100, volume=1000),
            Bar(timestamp=datetime(2024, 1, 2), open=100, high=102, low=99, close=101, volume=1000),
            Bar(timestamp=datetime(2024, 1, 3), open=101, high=103, low=100, close=102, volume=1000),
        ]
    )

def make_result() -> IndicatorResult:
    series = make_series()

    indicator = KalmanIndicator(
        KalmanConfig(
            process_variance=0.01,
            measurement_variance=0.1,
            initial_estimate_error=1.0,
        )
    )
    return indicator.compute(series)

def test_plot_indicator_returns_figure():
    fig = plot_indicator(make_result())

    assert isinstance(fig, matplotlib.figure.Figure)

def test_plot_indicator_contains_single_axes():
    fig = plot_indicator(make_result())

    assert len(fig.axes) == 1

def test_plot_indicator_contains_two_lines():
    fig = plot_indicator(make_result())

    ax = fig.axes[0]

    assert len(ax.lines) == 2

def test_plot_indicator_none_raises():
    with pytest.raises(TypeError):
        plot_indicator(None)

def test_plot_indicator_invalid_type_raises():
    with pytest.raises(TypeError):
        plot_indicator([])
