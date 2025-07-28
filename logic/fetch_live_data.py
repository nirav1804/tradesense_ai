# logic/fetch_live_data.py
import yfinance as yf

def get_live_data(ticker):
    data = yf.download(ticker, period='1d', interval='5m')
    return data
