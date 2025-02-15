import streamlit as st
import pandas as pd
import components.sidebar as sidebar
import components.metrics_dashboard as metrics
import components.trends as trends
import components.predictions as predictions
import components.map_view as map_view
from data.data_loader import load_historical_data
from data.satellite import get_satellite_data
from utils.authentication import authenticate
from utils.alert_system import check_for_alerts, send_sms_alert
from utils.chatbot import ask_chatbot
import config

# Initialize Google Earth Engine
authenticate()

# Load Historical Data
historical_data = load_historical_data()

# Layout
st.set_page_config(layout="wide")
left_col, right_col = st.columns([1, 2])

# Sidebar & Filters
sidebar.show_sidebar()

# Water Quality Metrics
tab1, tab2 = st.tabs(["Metrics Dashboard", "Predictions & Reports"])
with tab1:
    with left_col:
        metrics.show_metrics(historical_data)
    with right_col:
        map_view.show_map()

with tab2:
    predictions.show_predictions(historical_data)

# Trend Analysis
trends.show_trends(historical_data)

# Twilio Alert System
if st.button("Check for Alerts"):
    alerts = check_for_alerts(historical_data)
    for alert in alerts:
        send_sms_alert(config.TO_PHONE_NUMBER, alert)
        st.warning(alert)

# Chatbot Integration
st.markdown("### 🤖 Chatbot")
chat_input = st.text_input("Ask me anything about water quality:")
if chat_input:
    response = ask_chatbot(chat_input)
    st.write(response)

st.markdown("---")
st.write("Developed for real-time Ganga River monitoring 🚀")
