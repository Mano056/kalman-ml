from datetime import datetime

import pytest

from core import Bar, PriceSeries
from indicators import IndicatorResult, IndicatorSet


def make_series() -> PriceSeries:
    return PriceSeries(
        [
            Bar(
                timestamp=datetime(2024, 1, 1),
                open=100,
                high=101,
                low=99,
                close=100,
                volume=1000,
            )
        ]
    )

def test_indicator_lookup() -> None:
    series = make_series()

    result = IndicatorResult(
        name="kalman_fast",
        outputs={"value": [100.0]},
        price_series=series,
    )

    indicators = IndicatorSet([result])

    assert "kalman_fast" in indicators
    assert indicators.get("kalman_fast") is result

def test_indicator_names() -> None:
    series = make_series()

    indicators = IndicatorSet(
        [
            IndicatorResult(
                "b",
                {"value": [1]},
                series,
            ),
            IndicatorResult(
                "a",
                {"value": [2]},
                series,
            ),
        ]
    )

    assert indicators.names == ["a", "b"]

def test_duplicate_names() -> None:
    series = make_series()

    result = IndicatorResult(
        "kalman",
        {"value": [1]},
        series,
    )

    with pytest.raises(ValueError):
        IndicatorSet(
            [
                result,
                result,
            ]
        )

def test_missing_indicator() -> None:
    indicators = IndicatorSet([])

    with pytest.raises(KeyError):
        indicators.get("missing")