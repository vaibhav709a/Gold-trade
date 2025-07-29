### FILE: signals/signal_logic.py
def safe_trade_signal(df):
    latest = df.iloc[-1]

    if latest["rsi"] < 30 and latest["macd"] > 0 and latest["close"] > latest["ema20"]:
        return "Buy", latest["close"] - 1.5, latest["close"] + 3, 95
    elif latest["rsi"] > 70 and latest["macd"] < 0 and latest["close"] < latest["ema20"]:
        return "Sell", latest["close"] + 1.5, latest["close"] - 3, 95
    else:
        return "No Trade", None, None, 0
