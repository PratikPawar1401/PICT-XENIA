# components/sidebar.py
import streamlit as st

def show_sidebar():
    st.sidebar.header("⚙️ Settings")
    
    # Select water quality parameter
    parameter = st.sidebar.selectbox("Select Parameter", ["pH", "D.O. (mg/l)", "Turbidity (NTU)", "Temperature (ºC)"])
    
    # Select date range
    date_range = st.sidebar.date_input("Select Date Range", [])
    
    # Refresh button
    if st.sidebar.button("Refresh Data"):
        st.experimental_rerun()

    return parameter, date_range
