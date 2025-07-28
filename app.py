import streamlit as st
from logic.fetch_live_data import get_live_data
from logic.trend_ai import analyze_trend
from logic.strategy import generate_signals

st.set_page_config(page_title="TradeSense AI", layout="wide")

st.title("📊 TradeSense AI – Real-time Stock Trading Assistant")

script = st.text_input("Enter NSE/BSE script code (e.g., RELIANCE)", "RELIANCE")
segment = st.selectbox("Select Segment", ["Cash", "Futures"])
if st.button("Analyze") and script:
    data = get_live_data(script, segment)
    if data is not None:
        st.subheader("📈 Trend Analysis")
        trend_summary = analyze_trend(data)
        st.write(trend_summary)

        st.subheader("📍 Entry/Exit Signals")
        signals = generate_signals(data)
        st.dataframe(signals)
    else:
        st.error("⚠️ Could not fetch live data. Please try again.")
