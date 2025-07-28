def generate_signals(data):
    signals = []
    for i in range(1, len(data)):
        if data['Close'].iloc[i] > data['Close'].iloc[i - 1]:
            signals.append("Buy")
        else:
            signals.append("Sell")
    return signals
