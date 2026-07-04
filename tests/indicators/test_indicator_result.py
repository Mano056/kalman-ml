from datetime import datetime, timedelta

import pytest

from core import Bar, PriceSeries
from indicators import IndicatorResult

def make_series() -> PriceSeries:
    bars = []

    for i in range(5):
        bars.append(
            Bar(
                timestamp=datetime(2024, 1, 1) + timedelta(minutes=i),
                open=100 + i,
                high=101 + i,
                low=99 +i,
                close=100.5 + i,
                volume=1000,
            )
        )
    
    return PriceSeries(bars)

def test_indicator_result_creation() -> None:
    series = make_series()

    result = IndicatorResult(
        name="Test",
        values=[1, 2, 3, 4, 5],
        price_series=series,
    )

    assert result.name == "Test"
    assert result.values == [1, 2, 3, 4, 5]

def test_indicator_result_lenght_validation() -> None:
    series = make_series()

    with pytest.raises(ValueError):
        IndicatorResult(
            name="Bad",
            values=[1, 2],
            price_series=series,
        )