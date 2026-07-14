from __future__ import annotations

from dataclasses import dataclass

from core import Trade


@dataclass(frozen=True, slots=True)
class BacktestResult:
    """
    Results produced by a completed backtest.
    """

    initial_cash: float
    final_equity: float
    trades: list[Trade]
    equity_curve: list[float]