# Houston Heights Single-Family Home Value Dashboard

Interactive charts and indicators for **Houston Heights** (primarily ZIPs 77007 / 77008 / 77009) single-family home values, correlations with mortgage rates / inventory, and simple predictive signals.

**Live Pages URL (once enabled):**  
https://andykoswara.github.io/houston-heights-dashboard/

## Quick access on iPhone
1. Open the HTML file (or the GitHub Pages link after enabling).
2. In Safari → Share → Add to Home Screen.
3. Charts are fully interactive (pinch-zoom, hover, toggle series).

## Files
- `houston_heights_dashboard.html` — Fully self-contained interactive dashboard (works offline).
- `heights_dashboard.py` — Python generator script (run to refresh data / regenerate HTML).
- `README.md` — This file.

## Enable GitHub Pages (one-time)
1. Go to the repository **Settings** → **Pages**.
2. Under "Source" select **Deploy from a branch**.
3. Branch: `main` / Folder: `/ (root)` → Save.
4. Wait 1–2 minutes. Your permanent mobile-friendly URL will be live.

## Regenerating / updating data
```bash
pip install pandas plotly
python heights_dashboard.py
```
Then commit and push the new HTML.

## Data notes (as of late August 2026)
- Zillow ZHVI for 77008 typical home value ≈ $591k (≈ –1% YoY).
- Heights has shown relative resilience vs. broader Houston metro due to constrained historic-district supply.
- Key correlates: 30-year mortgage rates (inverse), months of supply / DOM, local inventory tightness.
- Sources: Zillow Research, HAR/MLS, Redfin, FRED (Freddie Mac rates).

**Research / analytics only — not investment advice.**
