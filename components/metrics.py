# components/metrics_dashboard.py
import streamlit as st
import pandas as pd

def show_metrics(data):
    st.subheader("📊 Water Quality Metrics")
    
    latest = data.iloc[-1]  # Get latest values
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("💧 pH Level", f"{latest['pH']:.2f}")
    col2.metric("🌱 Dissolved Oxygen (mg/l)", f"{latest['D.O. (mg/l)']:.2f}")
    col3.metric("🌊 Turbidity (NTU)", f"{latest['Turbidity (NTU)']:.2f}")
    col4.metric("🌡 Temperature (°C)", f"{latest['Temperature (ºC)']:.2f}")
