import requests
from bs4 import BeautifulSoup
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

URL = "https://aktu.ac.in/circulars.html"

r = requests.get(URL)
soup = BeautifulSoup(r.text, "html.parser")

links = soup.find_all("a")

latest_title = None
latest_link = None

for a in links:
    href = a.get("href")
    text = a.get_text(strip=True)

    if href and ".pdf" in href.lower():
        latest_title = text
        latest_link = href
        break

if latest_link and not latest_link.startswith("http"):
    latest_link = "https://aktu.ac.in/" + latest_link.lstrip("/")

with open("last_notice.txt", "r") as f:
    old_notice = f.read().strip()

if latest_link != old_notice:

    msg = f"""🚨 New AKTU Circular

📄 {latest_title}

🔗 {latest_link}
"""

    requests.get(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        params={
            "chat_id": CHAT_ID,
            "text": msg
        }
    )

    with open("last_notice.txt", "w") as f:
        f.write(latest_link)

print("Done")
