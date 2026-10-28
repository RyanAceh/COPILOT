"""Download a published Google Sheets tab as CSV, without credentials."""
import csv
import io
from pathlib import Path
from urllib.request import Request, urlopen

PUBLISHED_ID = "2PACX-1vQ3j7zfdTYempd2LNk3RdYEoX3CZ5mf7wG7xGzz9RO_GXcJbNJ71ShWVEv2d7waA3nq4my4ACLw3Isx"
GID = "1991175050"
URL = f"https://docs.google.com/spreadsheets/d/e/{PUBLISHED_ID}/pub?gid={GID}&single=true&output=csv"
DESTINATION = Path("data/google_sheets.csv")


def main():
    request = Request(URL, headers={"User-Agent": "Mozilla/5.0 (compatible; GitHubActionsSync/1.0)"})
    with urlopen(request, timeout=60) as response:
        data = response.read()
        content_type = response.headers.get("Content-Type", "").lower()
    if not data or b"<html" in data[:512].lower() or "text/html" in content_type:
        raise RuntimeError("Google Sheets did not return CSV. Verify that the tab is published to the web.")
    decoded = data.decode("utf-8-sig")
    rows = list(csv.reader(io.StringIO(decoded)))
    if not rows or not any(cell.strip() for row in rows for cell in row):
        raise RuntimeError("Google Sheets returned an empty CSV.")
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_bytes(data)
    print(f"Saved {DESTINATION} ({len(rows)} rows, {len(data)} bytes)")


if __name__ == "__main__":
    main()
