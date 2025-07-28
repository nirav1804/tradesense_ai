import pandas as pd

def generate_signals(df):
    df['signal'] = ['Buy' if price < 2000 else 'Sell' for price in df['price']]
    return df[['symbol', 'price', 'signal']]
