import pandas as pd

def get_live_data(script, segment):
    # Simulated dummy DataFrame for testing
    df = pd.DataFrame({
        'Date': pd.date_range(start='2023-01-01', periods=5, freq='D'),
        'Open': [100, 102, 105, 103, 104],
        'High': [105, 106, 107, 108, 110],
        'Low': [99, 101, 104, 102, 103],
        'Close': [104, 103, 106, 107, 109],
        'Volume': [1000, 1100, 1200, 1300, 1400]
    })
    return df
