# data/data_loader.py
import pandas as pd
import numpy as np

def load_historical_data():
    """Generates sample water quality historical data."""
    date_range = pd.date_range(start="2023-01-01", periods=365, freq='D')
    np.random.seed(42)
    
    data = pd.DataFrame({
        'Date': date_range,
        'pH': np.random.normal(7, 0.5, len(date_range)),
        'D.O. (mg/l)': np.random.normal(7, 1, len(date_range)),
        'Turbidity (NTU)': np.random.normal(3, 1, len(date_range)),
        'Temperature (ºC)': np.random.normal(25, 3, len(date_range))
    }).set_index('Date')

    return data
