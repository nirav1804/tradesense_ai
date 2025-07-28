import streamlit as st
from logic.fetch_live_data import get_live_data
from logic.trend_ai import analyze_trend
from logic.strategy import generate_signals
import pandas as pd

# Page configuration
st.set_page_config(page_title="TradeSense AI", layout="wide")

# Title
st.title("📊 TradeSense AI – Real-time Stock Trading Assistant")

# User Inputs
script = st.text_input("Enter NSE/BSE script code (e.g., RELIANCE)", "RELIANCE")
segment = st.selectbox("Select Segment", ["Cash", "Futures"])

# Trigger on Analyze button
if st.button("Analyze") and script:
    data = get_live_data(script, segment)

    # Ensure valid data and required columns
    if isinstance(data, pd.DataFrame) and 'Close' in data.columns:
        st.subheader("📈 Trend Analysis")
        trend_summary = analyze_trend(data)
        st.write(trend_summary)

        st.subheader("📍 Entry/Exit Signals")
        signals = generate_signals(data)
        st.dataframe(signals)

        st.subheader("📊 Raw Price Data")
        st.dataframe(data.tail(10))
    else:
        st.error("⚠️ Could not fetch valid data. Please check the script code or try again.")
