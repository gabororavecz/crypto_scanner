def scan_market(df):
    latest = df.iloc[-1]

    signals = []

    if latest['rsi'] < 30:
        signals.append("OVERSOLD → Long candidate")

    if latest['rsi'] > 70:
        signals.append("OVERBOUGHT → Short candidate")

    if latest['close'] > latest['ema20'] > latest['ema50']:
        signals.append("Bullish momentum")

    if latest['close'] < latest['ema20'] < latest['ema50']:
        signals.append("Bearish momentum")

    return signals
