from pathlib import Path

from data import CsvDataLoader

def test_csv_loader() -> None:
    path = Path("tests/sample_data/sample_prices.csv")

    loader = CsvDataLoader(path)

    series = loader.load()

    assert len(series) == 3
    assert series.closes == [100.5, 101.5, 102.5]
    assert series.opens == [100.0, 101.0, 102.0]