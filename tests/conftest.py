import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pytest
from datetime import datetime

from indicators import KalmanIndicator
from config import KalmanConfig
from core import PositionSeries, PriceSeries, Bar
from backtesting import BacktestResult
from indicators import IndicatorResult


@pytest.fixture(autouse=True)
def close_figures():
    yield
    plt.close("all")

@pytest.fixture
def series():
    return PriceSeries(
        [
            Bar(timestamp=datetime(2024, 1, 1), open=100, high=101, low=99, close=100, volume=1000),
            Bar(timestamp=datetime(2024, 1, 2), open=101, high=102, low=100, close=101, volume=1000),
            Bar(timestamp=datetime(2024, 1, 3),open=102, high=103, low=101, close=102, volume=1000),
            Bar(timestamp=datetime(2024, 1, 4), open=103, high=104, low=102, close=103, volume=1000),
        ]
    )

@pytest.fixture
def portfolio():
    return BacktestResult(
        initial_cash=10_000,
        final_equity=10_500,
        trades=[],
        equity_curve=[
            10000,
            10100,
            10050,
            10300,
        ]
    )

@pytest.fixture
def indicator(series) -> IndicatorResult:
    indicator = KalmanIndicator(
        KalmanConfig(
            process_variance=0.01,
            measurement_variance=0.1,
            initial_estimate_error=1.0,
        )
    )
    return indicator.compute(series)

@pytest.fixture
def positions():
    return PositionSeries(
        [
            0, 
            1,
            1,
            0,
        ]
    )
