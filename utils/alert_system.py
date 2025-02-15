# utils/alert_system.py
from twilio.rest import Client
import config

client = Client(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN)

def send_sms_alert(to_phone_number, message):
    client.messages.create(
        body=message,
        from_=config.TWILIO_PHONE_NUMBER,
        to=to_phone_number
    )

def check_for_alerts(data):
    latest = data.iloc[-1]
    alerts = []
    
    if latest['pH'] < 6 or latest['pH'] > 8:
        alerts.append(f"⚠️ pH is out of range: {latest['pH']:.2f}")
    if latest['D.O. (mg/l)'] < 5:
        alerts.append(f"⚠️ Dissolved Oxygen is too low: {latest['D.O. (mg/l)']:.2f}")
    if latest['Turbidity (NTU)'] > 5:
        alerts.append(f"⚠️ High turbidity detected: {latest['Turbidity (NTU)']:.2f}")

    return alerts
