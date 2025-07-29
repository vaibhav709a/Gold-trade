from data.get_data import get_xauusd_data
from model.train_model import train_model

if __name__ == "__main__":
    print("🔁 Downloading XAU/USD data...")
    df = get_xauusd_data()
    print("📊 Training model...")
    train_model(df)
    print("✅ Model trained and saved to model/model.pkl")
