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

def test_single_output() -> None:
    series = make_series()

    result = IndicatorResult(
        name="EMA",
        outputs={
            "value": [1, 2, 3, 4, 5],
        },
        price_series=series,
    )

    assert result.output("value") == [1, 2, 3, 4, 5]

def test_multiple_outputs() -> None:
    series = make_series()

    result = IndicatorResult(
        name="Kalman",
        outputs={
            "fast": [1, 2, 3, 4, 5],
            "slow": [5, 4, 3, 2, 1],
        },
        price_series=series,
    )

    assert result.output_names == ["fast", "slow"]

    assert result.output("fast")[2] == 3
    assert result.output("slow")[2] == 3

def test_empt_outputs() -> None:
    series = make_series()

    with pytest.raises(ValueError):
        IndicatorResult(
            name="Bad",
            outputs={},
            price_series=series,
        )

def test_invalid_length() -> None:
    series = make_series()

    with pytest.raises(ValueError):
        IndicatorResult(
            name="Bad",
            outputs={
                "value": [1, 2],
            },
            price_series=series,
        )

def test_unknown_output() -> None:
    series = make_series()

    result = IndicatorResult(
        name="EMA",
        outputs={
            "value": [1, 2, 3, 4, 5],
        },
        price_series=series,
    )

    with pytest.raises(KeyError):
        result.output("missing")