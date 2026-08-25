# Houston Heights Single-Family & $/SqFt Dashboard

Interactive charts for Houston Heights (77007/77008/77009) home values, $/sqft, and correlations with micro/macro drivers.

## Live pages (after enabling GitHub Pages)
- Main value dashboard: https://andykoswara.github.io/houston-heights-dashboard/
- **New** $/SqFt correlations: https://andykoswara.github.io/houston-heights-dashboard/sqft_correlations.html

## Files
- `index.html` / `houston_heights_dashboard.html` — original value + rate + inventory charts
- `sqft_correlations.html` — **new** set correlating median sold $/sqft with:
  - Mortgage rates
  - Harris County median household income
  - Population / migration context
  - Business establishments
- `heights_dashboard.py` — generator script

## Data sources
- HAR MLS median sold $/sqft (1997–2025)
- FRED: MORTGAGE30US, MHITX48201A052NCEN (Harris income), TXHARR1POP, QCEW establishments
- Census ACS/SAIPE, Houston Facts / Chronicle migration notes

## Enable GitHub Pages
Settings → Pages → Deploy from branch `main` / root → Save.

Research / analytics only — not investment advice.
