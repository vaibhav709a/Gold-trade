from data.get_data import get_xauusd_data
from model.train_model import train_model

df = get_xauusd_data()
train_model(df)
print("✅ Model trained and saved.")
