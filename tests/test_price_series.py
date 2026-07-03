"""
Tests for the PriceSeries container.
"""

from datetime import datetime, timedelta

import pytest

from core import Bar, PriceSeries

def make_bar(index: int) -> Bar:
    """Create a valid test bar."""

    return Bar(
        timestamp=datetime(2024, 1, 1) + timedelta(minutes=index),
        open=100 + index,
        high=101 + index,
        low=99 + index,
        close=100.5 + index,
        volume=1000,
    )

def test_length() -> None:
    series = PriceSeries([make_bar(i) for i in range(5)])

    assert len(series) == 5

def test_indexing() -> None:
    series = PriceSeries([make_bar(i) for i in range(3)])

    assert series[1].close == 101.5

def test_iteration() -> None:
    series = PriceSeries([make_bar(i) for i in range(4)])

    closes = [bar.close for bar in series]

    assert closes == [100.5, 101.5, 102.5, 103.5]

def test_close_property() -> None:
    series = PriceSeries([make_bar(i) for i in range(3)])

    assert series.closes == [100.5, 101.5, 102.5]

def test_timestamp_order_validation() -> None:
    bars = [make_bar(1), make_bar(0)]

    with pytest.raises(ValueError):
        PriceSeries(bars)