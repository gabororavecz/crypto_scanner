from data import fetch_ohlcv
from indicators import add_indicators
from scanner import scan_market, market_regime, trade_score
from derivatives import get_funding_rate, funding_signal


symbols = [
    'BTC/USDT',
    'ETH/USDT',
    'SOL/USDT',
    'BNB/USDT',
    'XRP/USDT'
]

for symbol in symbols:
    df = fetch_ohlcv(symbol)
    df = add_indicators(df)

    regime = market_regime(df)
    signals = scan_market(df)
    score = trade_score(df)
    symbol_futures = symbol.replace("/", "")
    funding = get_funding_rate(symbol_futures)
    positioning = funding_signal(funding)

    print(f"\n{symbol}")
    print(f"Regime: {regime}")
    print(f"Trade Score: {score}")
    print(f"Funding: {funding:.5f}")
    print(f"Positioning: {positioning}")

    for s in signals:
        print("  -", s)





