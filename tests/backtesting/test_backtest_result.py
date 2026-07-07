from backtesting import BacktestResult

def test_total_return() -> None:
    result = BacktestResult(
        initial_cash=10000,
        final_equity=11000,
        trades=[],
        equity_curve=[10000,11000],
    )

    assert result.total_return == 0.10