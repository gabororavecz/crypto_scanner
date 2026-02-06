from data import fetch_ohlcv
from indicators import add_indicators
from scanner import scan_market

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
    signals = scan_market(df)

    print(f"\n{symbol}")
    for s in signals:
        print("  -", s)
