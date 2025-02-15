# utils/authentication.py
import ee

def authenticate():
    try:
        ee.Initialize()
    except Exception:
        ee.Authenticate()
        ee.Initialize()

