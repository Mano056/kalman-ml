from .result import BacktestResult
from .metrics import total_return, win_rate, average_trade, profit_factor, max_drawdown

def summarize(result: BacktestResult) -> str:
    return f"""
========== BACKTEST SUMMARY ==========

Initial Equity : {result.initial_cash:.2f}
Final Equity   : {result.final_equity:.2f}

Total Return   : {total_return(result):.2%}
Win Rate       : {win_rate(result):.2%}
Average Trade  : {average_trade(result):.2%}
Profit Factor  : {profit_factor(result):.2f}
Max Drawdown   : {max_drawdown(result):.2%}

Trades         : {len(result.trades)}
"""