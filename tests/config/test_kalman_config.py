import pytest

from config import KalmanConfig


def test_create_config() -> None:
    config = KalmanConfig(
        process_variance=1e-5,
        measurement_variance=1e-2,
    )

    assert config.process_variance == 1e-5
    assert config.measurement_variance == 1e-2
    assert config.initial_estimate_error == 1.0

def test_invalid_process_variance() -> None:
    with pytest.raises(ValueError):
        KalmanConfig(
            process_variance=0.0,
            measurement_variance=1e-2,
        )

def test_invalid_measurement_variance() -> None:
    with pytest.raises(ValueError):
        KalmanConfig(
            process_variance=1e-5,
            measurement_variance=0.0,
        )

def test_invalid_initial_error() -> None:
    with pytest.raises(ValueError):
        KalmanConfig(
            process_variance=1e-5,
            measurement_variance=1e-2,
            initial_estimate_error=0.0,
        )