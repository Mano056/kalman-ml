from datetime import datetime, timedelta

from config import KalmanConfig
from core import Bar, PriceSeries
from indicators import KalmanIndicator 


def make_series() -> PriceSeries:
    bars = []

    closes = [
        100.0,
        101.0,
        102.0,
        103.0,
        104.0,
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

def test_output_length_matches_input() -> None:
    series = make_series()

    indicator = KalmanIndicator(
        KalmanConfig(
            process_variance=1e-5,
            measurement_variance=1e-2,
        )
    )

    result = indicator.compute(series)

    assert len(result.output("value")) == len(series)

def test_first_value_matches_first_close() -> None:
    series = make_series()

    indicator = KalmanIndicator(
        KalmanConfig(
            process_variance=1e-5,
            measurement_variance=1e-2,
        )
    )

    result = indicator.compute(series)

    assert result.output("value")[0] == 100.0

def test_filtered_series_is_monotonic() -> None:
    series = make_series()

    indicator = KalmanIndicator(
        KalmanConfig(
            process_variance=1e-5,
            measurement_variance=1e-2,
        )
    )

    values = indicator.compute(series).output("value")

    assert values[0] < values[-1]