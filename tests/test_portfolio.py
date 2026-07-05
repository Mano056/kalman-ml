from core.portfolio import Portfolio


def test_portfolio_initialisation() -> None:
    portfolio = Portfolio(
        cash=10_000.0,
        equity=10_000.0,
    )

    assert portfolio.position == 0.0
    assert portfolio.cash == 10_000.0
    assert portfolio.equity == 10_000.0


def test_update_equity_long_position() -> None:
    portfolio = Portfolio(
        cash=10_000.0,
        equity=10_000.0,
        position=1.0,
    )

    portfolio.update_equity(
        market_price=110.0,
        entry_price=100.0,
    )

    assert portfolio.equity == 10_010.0


def test_update_equity_short_position() -> None:
    portfolio = Portfolio(
        cash=10_000.0,
        equity=10_000.0,
        position=-1.0,
    )

    portfolio.update_equity(
        market_price=90.0,
        entry_price=100.0,
    )

    assert portfolio.equity == 10_010.0