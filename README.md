# Houston Heights Single-Family & $/SqFt Dashboard

Interactive charts for Houston Heights (77007 / 77008 / 77009) home values, $/sqft, and correlations with micro and macro drivers.

## Live pages (after enabling GitHub Pages)

- **Research briefing (default):** https://andykoswara.github.io/houston-heights-dashboard/
- Same briefing: https://andykoswara.github.io/houston-heights-dashboard/sqft_correlations.html
- Original value dashboard: https://andykoswara.github.io/houston-heights-dashboard/houston_heights_dashboard.html

## How the briefing is structured

1. Header description of the research
2. KPI strip
3. **Observations** — how to read the tape
4. **Summary of key observations** — six points, *before* any charts
5. Six charts with captions
6. **Expanded observations** — numbers, lags, and limits
7. **Disclosures**
8. **Sources**

## Files

- `index.html` / `sqft_correlations.html` — full research briefing (iPhone Safari friendly)
- `houston_heights_dashboard.html` — original value + rate + inventory charts
- `heights_dashboard.py` — generator script

## Data sources

- HAR MLS median sold $/sqft (1997–2025)
- FRED: MORTGAGE30US, MHITX48201A052NCEN, TXHARR1POP, ENU4820120510
- Census ACS/SAIPE; Houston Facts / Chronicle migration notes
- Redfin / heightscomps inventory
- TEA / GreatSchools / SchoolDigger / Niche

## Enable GitHub Pages

Settings → Pages → Deploy from branch `main` / root → Save.

Research / analytics only — not investment advice.
