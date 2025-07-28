import pandas as pd
import requests
import os

# Dummy NSE data simulation (replace with real API if needed)
def fetch_data():
    data = {
        "symbol": ["RELIANCE", "TCS", "INFY"],
        "price": [2800, 3700, 1450],
        "volume": [100000, 80000, 120000]
    }
    df = pd.DataFrame(data)
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/latest_data.csv", index=False)
    print("Data fetched and saved.")

if __name__ == "__main__":
    fetch_data()
