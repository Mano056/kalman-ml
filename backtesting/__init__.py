"""
Backtesting package.
"""

from .backtester import Backtester
from .result import BacktestResult
from .metrics import total_return, win_rate, average_trade, profit_factor, max_drawdown
from .report import summarize

__all__ = [
    "Backtester",
    "BacktestResult",
    "total_return",
    "win_rate",
    "average_trade",
    "profit_factor",
    "max_drawdown",
    "summarize",
]