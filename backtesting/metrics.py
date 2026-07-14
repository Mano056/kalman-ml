from __future__ import annotations

from .result import BacktestResult


def total_return(result: BacktestResult) -> float:
    """
    Total return over the backtest.
    
    Returns:
        Decimal return (0.15 = +15%)
    """
    return (
        result.final_equity - result.initial_cash
    ) / result.initial_cash

def win_rate(result: BacktestResult) -> float:
    if not result.trades:
        return 0.0
    
    wins = sum(trade.return_pct > 0 for trade in result.trades)

    return wins / len(result.trades)

def average_trade(result: BacktestResult) -> float:
    if not result.trades:
        return 0.0
    
    ret = sum(trade.return_pct for trade in result.trades)

    return ret / len(result.trades)

def profit_factor(result: BacktestResult) -> float:
    if not result.trades:
        return 0.0
    
    profit = sum(
        trade.return_pct 
        for trade in result.trades
        if trade.return_pct > 0
    )

    loss = sum(
        trade.return_pct
        for trade in result.trades
        if trade.return_pct < 0
    )

    if loss == 0:
        return float("inf")
    
    if profit == 0:
        return 0.0
    
    return  profit / abs(loss)

def max_drawdown(result: BacktestResult) -> float:
    if not result.equity_curve:
        return 0.0
    
    peak = result.equity_curve[0]
    max_drawdown = 0.0

    for equity in result.equity_curve:
        if equity > peak:
            peak = equity

        drawdown = (equity - peak) / peak 

        if drawdown < max_drawdown:
            max_drawdown = drawdown
    
    return max_drawdown