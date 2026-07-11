from pathlib import Path
from datetime import datetime

from data import CsvDataLoader

def test_csv_loader() -> None:
    path = Path("tests/sample_data/mt5_sample.csv")

    loader = CsvDataLoader(path)

    series = loader.load()

    assert len(series) == 5
    assert series[0].close == 0.65700
    assert series[0].volume == 13
    assert series[0].timestamp == datetime(2000, 1, 3, 0, 0)