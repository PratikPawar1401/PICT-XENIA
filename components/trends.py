# components/trends.py
import streamlit as st
import matplotlib.pyplot as plt

def show_trends(data):
    st.subheader("📈 Trend Analysis")
    
    fig, ax = plt.subplots(figsize=(10, 5))
    for col in ["pH", "D.O. (mg/l)", "Turbidity (NTU)", "Temperature (ºC)"]:
        ax.plot(data.index, data[col], label=col)
    
    ax.set_xlabel("Date")
    ax.set_ylabel("Value")
    ax.legend()
    st.pyplot(fig)
