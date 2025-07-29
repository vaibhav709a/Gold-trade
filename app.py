### FILE: streamlit_app.py
import streamlit as st
import pandas as pd
import joblib
from indicators.indicators import add_indicators
from signals.signal_logic import safe_trade_signal
from model.train_model import load_model
from data.get_data import get_xauusd_data

st.set_page_config(page_title="XAU/USD AI Signal", layout="wide")
st.title("🧠 AI XAU/USD Signal Generator")

# Get Data
df = get_xauusd_data()
df = add_indicators(df)

# Load model
model = load_model()

# Predict using latest data
latest = df.iloc[-1:][["rsi", "macd", "ema20"]]
prediction = model.predict(latest)[0]

# Generate signal
signal, sl, tp, confidence = safe_trade_signal(df)

st.subheader("📈 Latest Trade Signal")
st.metric("AI Prediction", "Buy" if prediction == 1 else "Sell")
st.metric("Final Signal", signal)
if signal != "No Trade":
    st.metric("Confidence", f"{confidence}%")
    st.metric("Stop Loss", f"{sl:.2f}")
    st.metric("Take Profit", f"{tp:.2f}")
else:
    st.warning("No safe trade available at the moment.")
