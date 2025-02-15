# data/satellite.py
import ee
import geemap.foliumap as geemap
from utils.authentication import authenticate

def get_satellite_data():
    authenticate()
    roi = ee.Geometry.Rectangle([78.0, 24.0, 88.0, 31.0])  # Ganga Basin

    dataset = ee.ImageCollection("COPERNICUS/S2") \
        .filterBounds(roi) \
        .filterDate("2024-01-01", "2024-12-31") \
        .median()

    # Compute Water Quality Indices
    ndwi = dataset.normalizedDifference(["B3", "B8"]).rename("NDWI")
    turbidity = dataset.expression("(B2 / B4)", {
        "B2": dataset.select("B2"),
        "B4": dataset.select("B4")
    }).rename("Turbidity")

    return dataset.addBands([ndwi, turbidity])

