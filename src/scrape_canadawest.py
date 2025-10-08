# src/scrape_canadawest.py
import csv
import os
import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/128.0.0.0 Safari/537.36"
}

@dataclass
class MatchRow:
    date: str
    home_team: str
    away_team: str
    home_goals: int
    away_goals: int
    season: str


def scrape_schedule(url: str, season: str, out_csv: str):
    print(f"Fetching schedule for {season}...")
    resp = requests.get(url, headers=HEADERS)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "lxml")

    matches = []
    games = soup.select("tr.event-row")

    for game in games:
        # Find the date from the nearest parent div with data-date
        date_el = game.find_previous("div", class_="section-event-date")
        date = date_el.get("data-date", "Unknown") if date_el else "Unknown"

        # Extract team names
        team_spans = game.select("span.flex-md-grow-1")
        result_spans = game.select("span.result")

        if len(team_spans) == 2 and len(result_spans) == 2:
            away_team = team_spans[0].get_text(strip=True)
            home_team = team_spans[1].get_text(strip=True)

            away_goals = result_spans[0].get_text(strip=True)
            home_goals = result_spans[1].get_text(strip=True)

            if away_goals.isdigit() and home_goals.isdigit():
                matches.append(
                    MatchRow(
                        date=date,
                        home_team=home_team,
                        away_team=away_team,
                        home_goals=int(home_goals),
                        away_goals=int(away_goals),
                        season=season
                    )
                )

    os.makedirs(os.path.dirname(out_csv), exist_ok=True)
    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=MatchRow.__dataclass_fields__.keys())
        writer.writeheader()
        for m in matches:
            writer.writerow(m.__dict__)

    print(f"✅ Saved {len(matches)} matches to {out_csv}")


if __name__ == "__main__":
    SEASON_URL = "https://canadawest.org/sports/msoc/2025-26/schedule"
    scrape_schedule(SEASON_URL, "2025-26", "data/matches_2025.csv")
