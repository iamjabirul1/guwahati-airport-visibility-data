# When Guwahati's airport sits in fog: half-hourly visibility observations at LGBI (VEGT), 2023–2026

**Author:** Hotel Shiny Grand, Shyam Nagar, VIP, near LGBI Airport, Borjhar, Guwahati, Assam 781015, India (corporate author; data compiled and analysed by the hotel's team).

**Version:** 1.0 · **Date:** 2026-10-27 · **Licence:** CC BY 4.0

## Summary

Guwahati's Lokpriya Gopinath Bordoloi International Airport (ICAO: VEGT; IATA: GAU) serves as the arrival point for travellers heading to Shillong, Kaziranga, Arunachal Pradesh and the Kamakhya temple, and it is the airport most affected by winter fog in Northeast India. This note publishes and summarises 63,573 routine half-hourly weather observations for the station from January 2023 to October 2026, and answers two practical questions with them: how often reported visibility falls below 2 km, and at what hours.

Findings:

1. **The season is sharp.** Across December, January and February, 49.7% of reports showed visibility below 1.5 statute miles (about 2 km), against 9.8% in all other months. Dense reports below 1.0 mile (about 1.5 km) ran at 15.9% in those three months against 1.1% elsewhere.
2. **The hour is sharp.** Low visibility concentrates between 04:00 and 09:00 local time, peaking at 06:00, when 38.5% of all reports in the series were below 1.5 miles.
3. **Coded fog is a December–January phenomenon.** Of all reports carrying the METAR fog code `FG`, 382 fell in January, 156 in December and 29 in February. Every other month combined accounted for 32 reports across three and a half years.
4. **A pre-dawn flight in the fog window is usually leaving through low visibility.** Between 1 December and 15 February, 79.8% of reports before 10:00 were below 1.5 miles (4,029 of 5,052).

## Data and method

- **Source.** Iowa Environmental Mesonet ASOS/METAR archive (`mesonet.agron.iastate.edu`), which republishes the original NOAA/NWS METAR records. Fetched 2026-10-27 with a plain HTTP request; no account or key is involved. The fetch request is preserved as `data/fetch_metar.py`, and the extraction and every number in this note are reproduced by `analysis/analyze_visibility.py` using only the Python standard library.
- **Station and window.** VEGT, 2023-01-01 to 2026-10-27, timestamps requested in Asia/Kolkata local time so the hours correspond to the airport's operating day.
- **Fields.** Reported visibility, lowest cloud layer amount, present-weather codes and air temperature.
- **Units.** The archive reports visibility in statute miles while the underlying METAR is metric. This was verified against the raw report text rather than assumed: 1.24 mi corresponds to a report of 2000 m, 1.55 mi to 2500 m and 3.11 mi to 5000 m. Throughout this note, 2 km means "below 1.5 mi" and 1.5 km means "below 1.0 mi".
- **Missing values.** 24 of 63,573 reports carried no visibility value (0.04%); they are excluded from the visibility shares and never counted as clear.
- **Coverage.** 1,392 observed days; 723 of them had at least one report below 1.5 miles.

## What the data does not say

- It is **not** a delay or cancellation record. A 2000 m report with mist is routine at this airport; CAT III capable aircraft and trained crews operate well below 1.5 km, and no operational minima, runway status or airline decision is modelled here.
- It is **not** a forecast, and the window is a specific period rather than a long-run climatology. The seasonal pattern is consistent year to year within the series, but the shares above should be read as descriptive.
- It contains **no passenger, flight or commercial data** of any kind.

## Practical reading for travellers

If your departure is before mid-morning between December and mid-February, the observations support three behaviours: stay on the airport side of the city the night before rather than crossing Guwahati in the dark; treat the last hour before your airline's reporting time as unusable, because the drive, the terminal and the queues all slow down together; and prefer a changeable booking over a tight connection on a separate ticket. In the other nine months the same morning looks close to normal, with 9.8% of reports below 2 km against 49.7% in the fog season.

For arrivals the pattern matters less: fog burns off through the morning, and a late-evening arrival is far more likely to meet clear conditions than a pre-dawn departure.

## Data availability

- Dataset, fetch script and analysis: the accompanying repository, `data/gau_metar_visibility_2023_2026.csv` and `analysis/analyze_visibility.py`.
- Source archive: Iowa Environmental Mesonet ASOS/METAR; original observations NOAA/NWS (US Government public domain).
- Data licence: CC BY 4.0.

## Suggested citation

> Hotel Shiny Grand (2026). *When Guwahati's airport sits in fog: half-hourly visibility observations at LGBI (VEGT), 2023–2026.* Zenodo. https://doi.org/&lt;DOI&gt;

## Disclosure

The author is a hotel near the airport, and the note is written for the practical decision
facing its guests: whether a pre-dawn departure needs an airport-side night. The data,
method and limits are published in full so the numbers can be checked and reused
independently of that interest.
