import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

requests.get(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    params={
        "chat_id": CHAT_ID,
        "text": "✅ AKTU Alert Bot Working"
    }
)

print("Done")
