"""Fetch LGBI (VEGT) routine weather observations for the visibility note.

Source: Iowa Environmental Mesonet (IEM) ASOS/METAR archive
        https://mesonet.agron.iastate.edu/request/download.phtml
        Original observations: NOAA/NWS METAR archive (public domain).

Usage:
    python3 data/fetch_metar.py 2023-01-01 2026-10-27 > data/gau_metar_visibility_2023_2026.csv

Notes for anyone reusing this:
- The archive reports visibility in statute miles; the raw METAR carries metres
  (1.24 mi = 2000 m, 3.11 mi = 5000 m).
- Timestamps are requested in Asia/Kolkata local time so hours line up with the
  airport's operating day.
- The fetch is a plain HTTP GET; no account or key is involved.
"""

from __future__ import annotations

import sys
import urllib.parse
import urllib.request

BASE = "https://mesonet.agron.iastate.edu/cgi-bin/request/asos.py"
STATION = "VEGT"  # Lokpriya Gopinath Bordoloi International Airport, Guwahati
FIELDS = ("vsby", "skyc1", "wxcodes", "tmpf")


def build_url(start: str, end: str) -> str:
    start_year, start_month, start_day = (int(part) for part in start.split("-"))
    end_year, end_month, end_day = (int(part) for part in end.split("-"))
    query = {
        "station": STATION,
        "data": list(FIELDS),
        "year1": start_year,
        "month1": start_month,
        "day1": start_day,
        "year2": end_year,
        "month2": end_month,
        "day2": end_day,
        "tz": "Asia/Kolkata",
        "format": "csv",
        "latlon": "no",
        "direct": "no",
    }
    return BASE + "?" + urllib.parse.urlencode(query, doseq=True)


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(__doc__)
        return 2
    url = build_url(argv[1], argv[2])
    with urllib.request.urlopen(url, timeout=300) as response:
        body = response.read().decode("utf-8", "replace")
    for line in body.splitlines():
        if line.startswith("#") and not line.startswith("#DEBUG: Time"):
            continue
        print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
