def analyze_trend(data):
    # Dummy AI logic for trend detection
    if data['Close'].iloc[-1] > data['Close'].iloc[0]:
        return "Uptrend"
    else:
        return "Downtrend"
