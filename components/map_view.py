# components/map_view.py
import streamlit as st
import geemap.foliumap as geemap
from data.satellite import get_satellite_data

def show_map():
    st.subheader("🗺 Interactive Water Quality Map")
    
    # Create map
    m = geemap.Map(center=[27.0, 82.0], zoom=6)
    
    # Load Satellite Data
    dataset = get_satellite_data()
    m.addLayer(dataset, {"bands": ["NDWI"], "min": -1, "max": 1, "palette": ["blue", "white"]}, "NDWI")
    
    # Risk Level Color Coding
    stations = [
        {"name": "Kanpur", "lat": 26.4499, "lon": 80.3319, "risk": "High"},
        {"name": "Varanasi", "lat": 25.3176, "lon": 82.9739, "risk": "Moderate"},
        {"name": "Haridwar", "lat": 29.9457, "lon": 78.1642, "risk": "Low"},
    ]
    
    for station in stations:
        color = "red" if station["risk"] == "High" else "orange" if station["risk"] == "Moderate" else "green"
        m.add_marker(location=[station["lat"], station["lon"]], popup=f"{station['name']} ({station['risk']} Risk)", icon=color)
    
    m.to_streamlit(height=500)
