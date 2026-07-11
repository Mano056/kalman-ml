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
    
    def _parse_standard(self, df: pd.DataFrame) -> PriceSeries:

        
        bars: list[Bar] = []

        for _, row in df.iterrows():
            bars.append(
                Bar(
                    timestamp=datetime.fromisoformat(str(row["timestamp"])),
                    open=float(row["open"]),
                    high=float(row["high"]),
                    low=float(row["low"]),
                    close=float(row["close"]),
                    volume=float(row["volume"]),
                )
            )
        
        return PriceSeries(bars)
    
    def _parse_mt5(self, df: pd.DataFrame) -> PriceSeries:

        
        bars: list[Bar] = []

        for _, row in df.iterrows():
            timestamp = datetime.strptime(
                f"{row['<DATE>']} {row['<TIME>']}",
                "%Y.%m.%d %H:%M:%S",
            )

            bars.append(
                Bar(
                    timestamp=timestamp,
                    open=float(row['<OPEN>']),
                    high=float(row['<HIGH>']),
                    low=float(row['<LOW>']),
                    close=float(row['<CLOSE>']),
                    volume=float(row['<TICKVOL>']),
                )
            )
        
        return PriceSeries(bars)
    
    def load(self) -> PriceSeries:
        df = pd.read_csv(self._path, sep=None, engine="python")

        standard_columns = {
            "timestamp",
            "open",
            "high",
            "low",
            "close",
            "volume",
        }

        mt5_columns = {
            "<DATE>",
            "<TIME>",
            "<OPEN>",
            "<HIGH>",
            "<LOW>",
            "<CLOSE>",
            "<TICKVOL>",
        }

        if standard_columns.issubset(df.columns):
            return self._parse_standard(df)
        
        if mt5_columns.issubset(df.columns):
            return self._parse_mt5(df)
        
        raise ValueError(
            f"Unsupported CSV format. Columns found: {list(df.columns)}"
        )