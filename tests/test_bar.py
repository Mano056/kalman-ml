"""
Tests for the Bar domain model.
"""

from datetime import datetime

import pytest

from core import Bar

def test_bar_creation() -> None:
    """
    A valid bar should be created successfully.
    """

    bar = Bar(
        timestamp=datetime(2024, 1, 1),
        open=100.0,
        high=110.0,
        low=95.0,
        close=108.0,
        volume=1500.0,
    )

    assert bar.open == 100.0
    assert bar.high == 110.0
    assert bar.low == 95.0
    assert bar.close == 108.0
    assert bar.volume == 1500.0

def test_bar_is_immutable() -> None:
    """
    Bar instances should be immutable.
    """

    bar = Bar(
        timestamp=datetime(2024, 1, 1),
        open=100.0,
        high=101.0,
        low=99.0,
        close=100.5,
        volume=1000.0,
    )

    with pytest.raises(AttributeError):
        bar.close = 200.0

def test_invalid_high_low() -> None:
    """
    High must not be below low.
    """

    with pytest.raises(ValueError):
        Bar(
            timestamp=datetime.now(),
            open=100.0,
            high=90.0,
            low=95.0,
            close=92.0,
            volume=100,
        )

def test_negative_volume() -> None:
    """
    Volume cannot be negative.
    """

    with pytest.raises(ValueError):
        Bar(
            timestamp=datetime.now(),
            open=100.0,
            high=105.0,
            low=95.0,
            close=100.0,
            volume=-1,
        )