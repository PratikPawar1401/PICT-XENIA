import streamlit as st
import plotly.express as px
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

def display_time_series(filtered_data):
    st.subheader("📊 Time-Series Analysis")
    fig = px.line(filtered_data, x=filtered_data.index, y=['pH', 'Turbidity (NTU)'])
    st.plotly_chart(fig)

def display_ets(filtered_data):
    st.subheader("🔍 ETS Decomposition")
    selected_metric = st.selectbox('Choose Metric for ETS', ['pH', 'Turbidity (NTU)'])
    result = seasonal_decompose(filtered_data[selected_metric], model='multiplicative')

    fig, axs = plt.subplots(4, 1, figsize=(10, 10))
    result.observed.plot(ax=axs[0])
    result.trend.plot(ax=axs[1])
    result.seasonal.plot(ax=axs[2])
    result.resid.plot(ax=axs[3])
    plt.tight_layout()
    st.pyplot(fig)
