import os

API_ID    = os.environ.get("27832158", "")
API_HASH  = os.environ.get("3192df7327280382ad95867194e3a7e6", "")
BOT_TOKEN = os.environ.get("7411606620:AAGKNoF6Gj1mR9Es_Cla0YMDAHzqQwBn0DA", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
