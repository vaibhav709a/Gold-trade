### FILE: data/get_data.py
import requests
import pandas as pd

def get_xauusd_data():
    url = "https://api.twelvedata.com/time_series"
    params = {
        "symbol": "XAU/USD",
        "interval": "15min",
        "apikey": "806dd29a09244737ae6cd1a305061557",
        "outputsize": 500
    }
    r = requests.get(url, params=params)
    data = r.json()["values"]
    df = pd.DataFrame(data)
    df["datetime"] = pd.to_datetime(df["datetime"])
    df = df.sort_values("datetime")
    df = df.rename(columns={"close": "close", "open": "open", "high": "high", "low": "low"})
    df[["close", "open", "high", "low"]] = df[["close", "open", "high", "low"]].astype(float)
    return df

