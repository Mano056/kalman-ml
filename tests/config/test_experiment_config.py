from pathlib import Path

import pytest

from config import ExperimentConfig

def test_create_config() -> None:
    config = ExperimentConfig(
        name="Kalman Research",
        data_path=Path("data/btc.csv"),
    )

    assert config.name == "Kalman Research"
    assert config.data_path == Path("data/btc.csv")

def test_empty_name() -> None:
    with pytest.raises(ValueError):
        ExperimentConfig(
            name="",
            data_path=Path("data/test.csv"),
        )

def test_config_is_immutable() -> None:
    config = ExperimentConfig(
        name="Experiment",
        data_path=Path("data.csv"),
    )

    with pytest.raises(AttributeError):
        config.name = "Changed"