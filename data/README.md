# Data files

## `gau_metar_visibility_2023_2026.csv`

Routine half-hourly weather observations for Lokpriya Gopinath Bordoloi
International Airport, Guwahati (ICAO **VEGT**, IATA GAU), from the Iowa
Environmental Mesonet ASOS/METAR archive. Fetched 2026-10-27 for the window
2023-01-01 to 2026-10-27. 63,573 rows.

| Column | Meaning |
|---|---|
| `station` | Always `VEGT` |
| `valid` | Observation time, **local (Asia/Kolkata)** |
| `vsby` | Reported visibility in **statute miles** (see note) |
| `skyc1` | Lowest cloud layer amount (FEW, SCT, BKN, OVC) |
| `wxcodes` | Present-weather codes from the METAR (for example `BR` mist, `FG` fog) |
| `tmpf` | Air temperature in Fahrenheit (the archive's unit) |

**Units matter here.** `vsby` is in statute miles while the raw METAR reports
metres. Spot-checked against the raw text: `1.24` mi = `2000` m, `1.55` mi =
`2500` m, `3.11` mi = `5000` m. Treat 1.5 mi as roughly 2 km and 1.0 mi as
roughly 1.6 km.

Reproduce with:

```bash
python3 data/fetch_metar.py 2023-01-01 2026-10-27 > data/gau_metar_visibility_2023_2026.csv
```

Summary numbers and the by-month / by-hour tables come from
`analysis/analyze_visibility.py`.

## `airport_transfer_reference.csv`

Distances and drive-time basis for the two terminals, as stated by the hotel
(owner-confirmed 2026-10-23). This is a reference table, **not** an independent
measurement: the drive time is the hotel's stated figure for normal conditions,
and the reporting-time column follows airline general guidance, not an airport
authority.

Anyone citing either file should keep those limits in the text.
