from backtesting import BacktestResult, summarize
from core import Trade
from datetime import datetime

def test_report_input() -> None:
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

    report = summarize(result)

    assert "Initial Equity" in report
    assert "Final Equity" in report
    assert "Total Return" in report
    assert "Win Rate" in report
    assert "Profit Factor" in report
    assert "Max Drawdown" in report

    assert "10000.00" in report