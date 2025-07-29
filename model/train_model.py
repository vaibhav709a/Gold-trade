### FILE: model/train_model.py
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from indicators.indicators import add_indicators

def train_model(df):
    df = add_indicators(df)
    df.dropna(inplace=True)
    df["target"] = (df["close"].shift(-3) > df["close"]).astype(int)
    X = df[["rsi", "macd", "ema20"]]
    y = df["target"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    joblib.dump(model, "model/model.pkl")

def load_model():
    return joblib.load("model/model.pkl")
