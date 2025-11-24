# events_to_calendar.py
import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime
from ics import Calendar, Event
import os

URL = "https://www.sportpalace.co.il/bloomfield/%d7%9c%d7%95%d7%97-%d7%90%d7%a8%d7%95%d7%a2%d7%99%d7%9d/"

def fetch_page():
    response = requests.get(URL, timeout=15)
    response.raise_for_status()
    return response.text

def scrape_events():
    html = fetch_page()
    soup = bs(html, "html.parser")

    time_tags = soup.find_all("time", class_="value-title")
    title_divs = soup.find_all("div", class_="longdesc")

    events = []
    for time_tag, title_div in zip(time_tags, title_divs):
        raw_datetime = time_tag.get("datetime")
        # handle timezone Z or no timezone
        if raw_datetime.endswith("Z"):
            raw_datetime = raw_datetime.replace("Z", "+00:00")
        event_datetime = datetime.fromisoformat(raw_datetime)
        title = title_div.get_text(strip=True)
        events.append({"title": title, "datetime": event_datetime})
    return events

def generate_ics(events, out_path="bloomfield_events.ics"):
    calendar = Calendar()
    for ev in events:
        e = Event()
        e.name = ev["title"]
        e.begin = ev["datetime"]
        e.duration = {"hours": 2}
        calendar.events.add(e)

    # Ensure UTF-8 and overwrite
    with open(out_path, "w", encoding="utf-8") as f:
        f.writelines(calendar.serialize())

def main():
    events = scrape_events()
    if not events:
        print("No events found — exiting.")
        return 1
    generate_ics(events)
    print("✅ Created:", os.path.abspath("bloomfield_events.ics"))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
