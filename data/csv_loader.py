"""
CSV implementation of the market data loader.
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

import pandas as pd

from core import Bar, PriceSeries

from .loader import DataLoader

class CsvDataLoader(DataLoader):
    """
    Load OHLCV data from a CSV file.
    
    Expected columns:
    
    timestamp
    open
    high
    low
    close
    volume
    """

    def __init__(self, path: str | Path) -> None:
        self._path = Path(path)
    
    def load(self) -> PriceSeries:
        df = pd.read_csv(self._path)

        required = {
            "timestamp",
            "open",
            "high",
            "low",
            "close",
            "volume",
        }

        missing = required.difference(df.columns)

        if missing:
            raise ValueError(
                f"Missing required columns: {sorted(missing)}"
            )
        
        bars: list[Bar] = []

        for row in df.itertuples(index=False):
            bars.append(
                Bar(
                    timestamp=datetime.fromisoformat(str(row.timestamp)),
                    open=float(row.open),
                    high=float(row.high),
                    low=float(row.low),
                    close=float(row.close),
                    volume=float(row.volume),
                )
            )
        
        return PriceSeries(bars)