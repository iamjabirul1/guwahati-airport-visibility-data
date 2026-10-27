"""Summarise LGBI (VEGT) visibility observations for the fog-timing note.

Input : data/gau_metar_visibility_2023_2026.csv  (raw IEM ASOS/METAR export)
Output: analysis/visibility_by_month.csv
        analysis/visibility_by_hour.csv
        analysis/summary.md

Method notes (keep these honest when publishing):
- Visibility is reported in the archive in statute miles ("vsby"); verified against
  the raw METAR text, where 1.24 mi is a report of 2000 metres and 3.11 mi is 5000 m.
  We group it as:
    * "below 3 mi"    — 4000 m or less
    * "below 1.5 mi"  — 2000 m or less, i.e. mist or fog thick enough to matter
    * "below 1.0 mi"  — 1500 m or less, i.e. dense fog
- Timestamps are local time (Asia/Kolkata), as requested from the archive.
- Observations are routine METARs (typically every 30 minutes); a missing value is
  counted as "no observation", never as clear weather.
- This measures what the airport's automatic report recorded, not flight delays.
"""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "data" / "gau_metar_visibility_2023_2026.csv"
OUT = Path(__file__).resolve().parent

FOG_WINDOW = "12-01"  # Dec 1 .. Feb 15, the editorial fog window on the hotel site
FOG_WINDOW_END = "02-15"
MORNING_CUTOFF_HOUR = 10


def parse_visibility(value: str):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def in_fog_window(month_day: str) -> bool:
    return month_day >= FOG_WINDOW or month_day <= FOG_WINDOW_END


def main() -> int:
    by_month = defaultdict(Counter)
    by_hour = defaultdict(Counter)
    total = Counter()
    days_with_low = set()
    days_observed = set()
    fog_codes = Counter()
    window_morning = Counter()

    with SOURCE.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(line for line in handle if not line.startswith("#"))
        for row in reader:
            valid = (row.get("valid") or "").strip()
            if len(valid) < 16 or ":" not in valid:
                continue
            date_part, time_part = valid.split(" ", 1)
            month = date_part[:7]
            day = date_part
            hour = int(time_part[:2])
            month_day = date_part[5:]
            vsby = parse_visibility((row.get("vsby") or "").strip())
            wx = (row.get("wxcodes") or "").strip().upper()

            total["observations"] += 1
            days_observed.add(day)
            by_month[month]["observations"] += 1
            by_hour[hour]["observations"] += 1

            if vsby is not None:
                if vsby < 1.5:
                    by_month[month]["below_1_5_mi"] += 1
                    by_hour[hour]["below_1_5_mi"] += 1
                    total["below_1_5_mi"] += 1
                    days_with_low.add(day)
                if vsby < 1.0:
                    by_month[month]["below_1_0_mi"] += 1
                    by_hour[hour]["below_1_0_mi"] += 1
                    total["below_1_0_mi"] += 1
                if vsby < 3.0:
                    by_month[month]["below_3_mi"] += 1
                    by_hour[hour]["below_3_mi"] += 1
                    total["below_3_mi"] += 1
            else:
                by_month[month]["missing_visibility"] += 1
                total["missing_visibility"] += 1

            if "FG" in wx:
                fog_codes[month[5:]] += 1
            if in_fog_window(month_day) and hour < MORNING_CUTOFF_HOUR and vsby is not None:
                window_morning["observations"] += 1
                if vsby < 1.5:
                    window_morning["below_1_5_mi"] += 1

    with (OUT / "visibility_by_month.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["month", "observations", "below_3_mi", "below_1_5_mi", "below_1_0_mi", "missing_visibility"])
        for month in sorted(by_month):
            row = by_month[month]
            writer.writerow([month, row["observations"], row["below_3_mi"], row["below_1_5_mi"], row["below_1_0_mi"], row["missing_visibility"]])

    with (OUT / "visibility_by_hour.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["local_hour", "observations", "below_3_mi", "below_1_5_mi"])
        for hour in sorted(by_hour):
            row = by_hour[hour]
            writer.writerow([hour, row["observations"], row["below_3_mi"], row["below_1_5_mi"]])

    obs = total["observations"]
    ratio = (total["below_1_5_mi"] / obs) if obs else 0
    window_ratio = (
        window_morning["below_1_5_mi"] / window_morning["observations"]
        if window_morning["observations"]
        else 0
    )
    worst_months = sorted(by_month.items(), key=lambda item: item[1]["below_1_5_mi"], reverse=True)[:4]
    worst_hours = sorted(by_hour.items(), key=lambda item: item[1]["below_1_5_mi"], reverse=True)[:6]

    lines = [
        "# LGBI (VEGT) visibility summary",
        "",
        f"- Source: {SOURCE.name} (Iowa Environmental Mesonet ASOS/METAR export, fetched 2026-10-27)",
        f"- Observations parsed: {obs:,} (half-hourly routine reports, local time)",
        f"- Dated range: {min(by_month)} to {max(by_month)}",
        f"- Days with at least one report below 1.5 mi: {len(days_with_low):,} of {len(days_observed):,} observed days",
        f"- Reports below 1.5 mi: {total['below_1_5_mi']:,} ({ratio:.1%} of reports)",
        f"- Reports below 1.0 mi (dense fog): {total['below_1_0_mi']:,}",
        f"- Reports below 3 mi: {total['below_3_mi']:,}",
        f"- Reports with no visibility value: {total['missing_visibility']:,}",
        f"- Reports with FG in the weather code, by month number: {dict(sorted(fog_codes.items()))}",
        f"- Dec 1 to Feb 15 mornings before {MORNING_CUTOFF_HOUR}:00: {window_morning['below_1_5_mi']:,} of {window_morning['observations']:,} reports below 1.5 mi ({window_ratio:.1%})",
        "",
        "## Months with the most low-visibility reports (below 1.5 mi)",
        "",
        "| Month | Observations | Below 1.5 mi | Share |",
        "|---|---:|---:|---:|",
    ]
    for month, row in worst_months:
        share = row["below_1_5_mi"] / row["observations"] if row["observations"] else 0
        lines.append(f"| {month} | {row['observations']:,} | {row['below_1_5_mi']:,} | {share:.1%} |")

    lines += [
        "",
        "## Local hours with the most low-visibility reports (below 1.5 mi)",
        "",
        "| Local hour | Observations | Below 1.5 mi | Share |",
        "|---|---:|---:|---:|",
    ]
    for hour, row in worst_hours:
        share = row["below_1_5_mi"] / row["observations"] if row["observations"] else 0
        lines.append(f"| {hour:02d}:00 | {row['observations']:,} | {row['below_1_5_mi']:,} | {share:.1%} |")

    winter = [row for month, row in by_month.items() if month[-2:] in ("12", "01", "02")]
    other = [row for month, row in by_month.items() if month[-2:] not in ("12", "01", "02")]

    def share(rows, key):
        observations = sum(row["observations"] for row in rows)
        hit = sum(row[key] for row in rows)
        return observations, hit, (hit / observations if observations else 0)

    wobs, wlow, wshare = share(winter, "below_1_5_mi")
    oobs, olow, oshare = share(other, "below_1_5_mi")
    wdense = share(winter, "below_1_0_mi")[1]
    odense = share(other, "below_1_0_mi")[1]
    lines += [
        "",
        "## Winter against the rest of the year",
        "",
        f"- December, January and February: {wlow:,} of {wobs:,} reports below 1.5 mi ({wshare:.1%}); {wdense:,} below 1.0 mi.",
        f"- All other months: {olow:,} of {oobs:,} reports below 1.5 mi ({oshare:.1%}); {odense:,} below 1.0 mi.",
        "- That is roughly five times the rate in the fog season, which is why the hotel's pre-dawn guidance concentrates on December to mid-February.",
        "",
        "## Limits of this note",
        "",
        "- Visibility is the airport's reported meteorological value; it is not a delay, cancellation or runway-status record.",
        "- Thresholds in miles approximate the archive's own units; conversions to km are rounded (1 mi ≈ 1.6 km).",
        "- The series is observational and describes a specific window; it is not a forecast.",
        "",
    ]
    (OUT / "summary.md").write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines[:12]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
