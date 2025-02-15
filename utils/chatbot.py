# utils/chatbot.py
import requests
import config

def ask_chatbot(query):
    response = requests.post(config.CHATBOT_API_URL, json={"message": query})
    return response.json().get("response", "Sorry, I couldn't understand.")
