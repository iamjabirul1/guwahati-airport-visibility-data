# Guwahati airport (LGBI / VEGT): visibility and transfer reference data

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23699996.svg)](https://doi.org/10.5281/zenodo.23699996)

Open data about Lokpriya Gopinath Bordoloi International Airport, Guwahati, published by
[Hotel Shiny Grand](https://hotelshinygrand.online), a 35-room hotel in Borjhar, 1.7 km from
Terminal 2. Two things live here: three and a half years of routine airport visibility
observations, and the terminal-transfer reference the hotel uses when guests ask what time
to leave.

## What the visibility data shows

From **63,573 half-hourly routine reports** (January 2023 to October 2026, local time):

| Period | Reports below 1.5 mi (2.4 km) | Reports below 1.0 mi (1.6 km) |
|---|---:|---:|
| December, January, February | 49.7% | 15.9% |
| All other months | 9.8% | 1.1% |

- Low visibility concentrates between **04:00 and 09:00 local time**, peaking at 06:00.
- METAR **fog (`FG`) codes appear almost only in December and January** across the series
  (382 January reports, 156 December, 29 February, single digits in every other month).
- Inside the December 1 – February 15 window, **79.8% of reports before 10:00 were below
  1.5 mi (about 2.4 km)**.

That is the observational basis for the pre-dawn advice on the hotel's trip planner: if you
are flying out of Guwahati before mid-morning between December and mid-February, plan for the
airport to be slow, and stay on the airport side rather than crossing the city.

**What this is not:** reported visibility is not a delay, cancellation or runway record. A
2000 m report with mist is common and does not by itself stop flights; CAT III equipped
aircraft and trained crews land in conditions well below that. Read the numbers as "how often
the airport looks like this", not "how often your flight is late".

## Files

| Path | What |
|---|---|
| `data/gau_metar_visibility_2023_2026.csv` | The observations (63,573 rows) |
| `data/fetch_metar.py` | Reproduces the download from the Iowa Environmental Mesonet archive |
| `data/airport_transfer_reference.csv` | Distances, drive-time basis and reporting-time buffers, each with its basis stated |
| `data/README.md` | Column definitions and the units trap (`vsby` is in statute miles, not metres) |
| `analysis/analyze_visibility.py` | Produces the by-month and by-hour tables and `analysis/summary.md` |
| `analysis/summary.md` | The generated summary with every headline number above |
| `paper/visibility-note.md` | The short write-up (the same note is deposited on Zenodo for citation) |
| `tool/northeast-trip-planner.html` | A static copy of the free Northeast India trip planner this data feeds |
| `privacy.md` | Privacy policy for the companion Chrome extension |
| `decks/index.html` | Twenty travel decks (PDF and HTML) built from this data and the hotel's notes: fog behaviour, the 2026-27 events, routes, transfers and wedding planning |
| `CITATION.cff`, `.zenodo.json` | Citation metadata: GitHub's "Cite this repository" and the Zenodo deposit form |

## Reproduce it

```bash
python3 data/fetch_metar.py 2023-01-01 2026-10-27 > data/gau_metar_visibility_2023_2026.csv
python3 analysis/analyze_visibility.py
```

No API key, no account and no build step. The analysis uses only the Python standard library.

## Source and attribution

Observations come from the [Iowa Environmental Mesonet](https://mesonet.agron.iastate.edu/)
ASOS/METAR archive, which republishes the original NOAA/NWS METAR records (US Government
public domain). If you reuse the numbers, credit the archive and the original observations:

> Iowa Environmental Mesonet ASOS/METAR archive; original observations NOAA/NWS.

## Licence

- **Code** (`fetch_metar.py`, `analyze_visibility.py`): MIT — see `LICENSE`.
- **Data and the note** (`data/`, `analysis/`, `paper/`): CC BY 4.0 —
  https://creativecommons.org/licenses/by/4.0/

## Citing

The data and the note are deposited on Zenodo: **[10.5281/zenodo.23699996](https://doi.org/10.5281/zenodo.23699996)**
— the concept DOI, which always resolves to the newest version. The current version, v1.1.0, is
[10.5281/zenodo.23699997](https://doi.org/10.5281/zenodo.23699997).

Suggested citation for the release:

> Hotel Shiny Grand (2026). *Guwahati airport (LGBI / VEGT) visibility observations and
> terminal-transfer reference, 2023–2026* (v1.1.0) [Data set]. Zenodo.
> https://doi.org/10.5281/zenodo.23699997
