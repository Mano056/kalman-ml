from backtesting import BacktestResult, total_return, win_rate, average_trade, profit_factor, max_drawdown
from core import Trade
from datetime import datetime
import pytest


def test_total_return() -> None:
    result = BacktestResult(
        initial_cash=10_000,
        final_equity=11_500,
        trades=[],
        equity_curve=[],
    )

    assert total_return(result) == 0.15

def test_negative_total_return() -> None:
    result = BacktestResult(
        initial_cash=10_000,
        final_equity=8_000,
        trades=[],
        equity_curve=[],
    )

    assert total_return(result) == -0.20

def test_flat_total_return() -> None:
    result = BacktestResult(
        initial_cash=10_000,
        final_equity=10_000,
        trades=[],
        equity_curve=[],
    )

    assert total_return(result) == 0.0

def test_win_rate_mix_wins_losses() -> None:
    trades = [
        Trade(datetime(2024,1,1), datetime(2024,1,2), 1.0, 100, 110, 0.10),
        Trade(datetime(2024,1,4), datetime(2024,1,5), -1.0, 101, 101.5, -0.05),
        Trade(datetime(2024,1,10), datetime(2024,1,11), 1.0, 100, 120, 0.20),
        Trade(datetime(2024,1,20), datetime(2024,1,21), 1.0, 100, 101, 0.01),
    ]

    result = BacktestResult(
        initial_cash=10_000,
        final_equity=10_000,
        trades=trades,
        equity_curve=[],
    )

    assert win_rate(result) == 0.75

def test_win_rate_mix_all_wins() -> None:
    trades = [
        Trade(datetime(2024,1,1), datetime(2024,1,2), 1.0, 100, 110, 0.10),
        Trade(datetime(2024,1,4), datetime(2024,1,5), -1.0, 101, 100.5, 0.05),
        Trade(datetime(2024,1,10), datetime(2024,1,11), 1.0, 100, 120, 0.20),
        Trade(datetime(2024,1,20), datetime(2024,1,21), 1.0, 100, 101, 0.01),
    ]

    result = BacktestResult(
        initial_cash=10_000,
        final_equity=10_000,
        trades=trades,
        equity_curve=[],
    )

    assert win_rate(result) == 1.0

def test_win_rate_all_losses() -> None:
    trades = [
        Trade(datetime(2024,1,1), datetime(2024,1,2), 1.0, 110, 100, -0.10),
        Trade(datetime(2024,1,4), datetime(2024,1,5), -1.0, 101, 101.5, -0.05),
        Trade(datetime(2024,1,10), datetime(2024,1,11), 1.0, 120, 100, -0.20),
        Trade(datetime(2024,1,20), datetime(2024,1,21), 1.0, 101, 100, -0.01),
    ]

    result = BacktestResult(
        initial_cash=10_000,
        final_equity=10_000,
        trades=trades,
        equity_curve=[],
    )

    assert win_rate(result) == 0.0

def test_win_rate_no_trades() -> None:

    result = BacktestResult(
        initial_cash=10_000,
        final_equity=10_000,
        trades=[],
        equity_curve=[],
    )

    assert win_rate(result) == 0.0

def test_average_trade_mixed_trades() -> None:
    trades = [
        Trade(datetime(2024,1,1), datetime(2024,1,2), 1.0, 100, 110, 0.10),
        Trade(datetime(2024,1,4), datetime(2024,1,5), -1.0, 101, 100.5, -0.05),
        Trade(datetime(2024,1,10), datetime(2024,1,11), 1.0, 100, 115, 0.15),
    ]

    result = BacktestResult(
        initial_cash=10_000,
        final_equity=10_000,
        trades=trades,
        equity_curve=[],
    )

    expected = (0.10 - 0.05 + 0.15) / 3

    assert average_trade(result) == pytest.approx(expected)

def test_average_trade_all_winners() -> None:
    trades = [
        Trade(datetime(2024,1,1), datetime(2024,1,2), 1.0, 100, 110, 0.10),
        Trade(datetime(2024,1,4), datetime(2024,1,5), -1.0, 100, 80, 0.20),
        Trade(datetime(2024,1,10), datetime(2024,1,11), 1.0, 100, 130, 0.30),
    ]

    result = BacktestResult(
        initial_cash=10_000,
        final_equity=10_000,
        trades=trades,
        equity_curve=[],
    )

    expected = (0.10 + 0.20 + 0.30) / 3

    assert average_trade(result) == pytest.approx(expected)

def test_average_trade_all_losers() -> None:
    trades = [
        Trade(datetime(2024,1,1), datetime(2024,1,2), 1.0, 110, 100, -0.10),
        Trade(datetime(2024,1,4), datetime(2024,1,5), -1.0, 100, 80, -0.20),
    ]

    result = BacktestResult(
        initial_cash=10_000,
        final_equity=10_000,
        trades=trades,
        equity_curve=[],
    )

    expected = (-0.10 - 0.20) / 2
    assert average_trade(result) == pytest.approx(expected)

def test_average_trade_no_trade() -> None:
    result = BacktestResult(
        initial_cash=10_000,
        final_equity=10_000,
        trades=[],
        equity_curve=[],
    )

    assert average_trade(result) == 0.0

def test_profit_factor_mixed_trades() -> None:
    trades = [
        Trade(datetime(2024,1,1), datetime(2024,1,2), 1.0, 100, 110, 0.10),
        Trade(datetime(2024,1,4), datetime(2024,1,5), -1.0, 101, 100.5, -0.05),
        Trade(datetime(2024,1,10), datetime(2024,1,11), 1.0, 100, 120, 0.20),
        Trade(datetime(2024,1,20), datetime(2024,1,21), 1.0, 100, 101, 0.01),
    ]

    result = BacktestResult(
        initial_cash=10_000,
        final_equity=10_000,
        trades=trades,
        equity_curve=[],
    )

    expected = (0.10 + 0.20 + 0.01) / 0.05

    assert profit_factor(result) == pytest.approx(expected)

def test_profit_factor_all_winners() -> None:
    trades = [
        Trade(datetime(2024,1,1), datetime(2024,1,2), 1.0, 100, 110, 0.10),
        Trade(datetime(2024,1,4), datetime(2024,1,5), -1.0, 100, 80, 0.20),
        Trade(datetime(2024,1,10), datetime(2024,1,11), 1.0, 100, 130, 0.30),
    ]

    result = BacktestResult(
        initial_cash=10_000,
        final_equity=10_000,
        trades=trades,
        equity_curve=[],
    )

    assert profit_factor(result) == float("inf")

def test_profit_factor_all_lossers() -> None:
    trades = [
        Trade(datetime(2024,1,1), datetime(2024,1,2), 1.0, 110, 100, -0.10),
        Trade(datetime(2024,1,4), datetime(2024,1,5), -1.0, 100, 80, -0.20),
    ]

    result = BacktestResult(
        initial_cash=10_000,
        final_equity=10_000,
        trades=trades,
        equity_curve=[],
    )

    assert profit_factor(result) == 0.0

def test_profit_factor_no_trades() -> None:
    result = BacktestResult(
        initial_cash = 10_000,
        final_equity=10_000,
        trades=[],
        equity_curve=[],
    )

    assert profit_factor(result) == 0.0

def test_max_dd_flat_equity() -> None:
    equity_curve = [
        10000,
        10000,
        10000,
    ]

    result = BacktestResult(
        initial_cash=10_000,
        final_equity=10_000,
        trades=[],
        equity_curve=equity_curve,
    )

    assert max_drawdown(result) == 0.0

def test_max_dd_increasing_equity() -> None:
    equity_curve = [
        10000,
        11000,
        12000,
        13000,
    ]

    result = BacktestResult(
        initial_cash=10_000,
        final_equity=10_000,
        trades=[],
        equity_curve=equity_curve,
    )

    assert max_drawdown(result) == 0.0

def test_max_dd_one_drawdown() -> None:
    equity_curve = [
        10000,
        11000,
        12000,
        10000,
        13000,
    ]

    result = BacktestResult(
        initial_cash=10_000,
        final_equity=10_000,
        trades=[],
        equity_curve=equity_curve,
    )

    expected = (10000 - 12000) / 12000

    assert max_drawdown(result) == pytest.approx(expected)

def test_max_dd_multiple_dd() -> None:
    equity_curve = [
        10000,
        12000,
        11000,
        9000,
        13000,
        12500,
    ]

    result = BacktestResult(
        initial_cash=10_000,
        final_equity=10_000,
        trades=[],
        equity_curve=equity_curve,
    )

    expected = (9000 - 12000) / 12000
    assert max_drawdown(result) == pytest.approx(expected)