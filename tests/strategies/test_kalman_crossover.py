from datetime import datetime, timedelta

from config import KalmanConfig
from core import Bar, PriceSeries
from strategies import KalmanCrossoverStrategy


def make_series() -> PriceSeries:
    bars = []

    closes = [
        100,
        101,
        102,
        103,
        102,
        101,
        100,
    ]

    for i, close in enumerate(closes):
        bars.append(
            Bar(
                timestamp=datetime(2024, 1, 1) + timedelta(minutes=i),
                open=close,
                high=close,
                low=close,
                close=close,
                volume=1000,
            )
        )

    return PriceSeries(bars)

def test_strategy_returns_position_series() -> None:
    strategy = KalmanCrossoverStrategy(
        fast_config=KalmanConfig(
            process_variance=1e-3,
            measurement_variance=1e-2,
        ),
        slow_config=KalmanConfig(
            process_variance=1e-5,
            measurement_variance=1e-2,
        ),
    )

    positions = strategy.compute_positions(make_series())

    assert len(positions) == 7

    assert all(position in (-1.0, 0.0, 1.0) for position in positions)