### FILE: indicators/indicators.py
import ta

def add_indicators(df):
    df["rsi"] = ta.momentum.RSIIndicator(df["close"]).rsi()
    df["macd"] = ta.trend.MACD(df["close"]).macd_diff()
    df["ema20"] = ta.trend.EMAIndicator(df["close"], window=20).ema_indicator()
    return df
