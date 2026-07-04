from core import PositionSeries


def test_position_series() -> None:
    positions = PositionSeries(
        [0.0, 1.0, 1.0, -1.0]
    )

    assert len(positions) == 4
    assert positions[2] == 1.0
    assert positions.values == [0.0, 1.0, 1.0, -1.0]