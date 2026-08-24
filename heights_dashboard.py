#!/usr/bin/env python3
"""
Houston Heights Single-Family Home Value Dashboard Generator
=============================================================
Produces a mobile-friendly interactive HTML dashboard for
Houston Heights (ZIPs 77007/77008/77009) single-family values,
correlations, and simple predictive signals.

Requirements:  pip install pandas plotly
Usage:         python heights_dashboard.py
Output:        houston_heights_dashboard.html  (open on iPhone Safari)
"""

from pathlib import Path
from datetime import datetime

# ---------- Sample / research-derived series (late Aug 2026) ----------
dates = [
    "2018-01", "2018-07", "2019-01", "2019-07",
    "2020-01", "2020-07", "2021-01", "2021-07",
    "2022-01", "2022-07", "2023-01", "2023-07",
    "2024-01", "2024-07", "2025-01", "2025-07",
    "2026-01", "2026-06", "2026-08"
]
zhvi_77008 = [  # core Heights proxy
    385000, 395000, 410000, 425000,
    430000, 455000, 495000, 545000,
    585000, 610000, 595000, 580000,
    575000, 585000, 595000, 600000,
    598000, 592000, 590750
]
zhvi_houston = [  # metro comparison
    210000, 218000, 225000, 232000,
    235000, 250000, 275000, 310000,
    340000, 355000, 345000, 330000,
    325000, 320000, 315000, 310000,
    305000, 275000, 263500
]
mortgage_rates = [
    4.15, 4.55, 4.45, 3.75,
    3.60, 3.05, 2.75, 2.90,
    3.45, 5.50, 6.40, 6.85,
    6.70, 6.80, 6.90, 6.75,
    6.70, 6.55, 6.65
]
months_supply = [
    2.8, 3.1, 2.9, 2.5,
    2.2, 1.8, 1.4, 1.2,
    1.5, 2.8, 3.5, 4.0,
    4.2, 4.0, 3.8, 4.1,
    4.3, 4.5, 4.6
]
dom = [
    35, 38, 32, 28,
    25, 18, 12, 10,
    15, 35, 45, 50,
    48, 42, 40, 38,
    40, 41, 42
]
years_psf = list(range(2015, 2026))
psf = [288, 273, 258, 297, 303, 313, 345, 381, 385, 383, 410]

def build_dashboard():
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    # 1. Value trajectory
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=dates, y=zhvi_77008, name="77008 ZHVI (Heights)",
                              line=dict(color="#1f77b4", width=3)))
    fig1.add_trace(go.Scatter(x=dates, y=zhvi_houston, name="Houston Metro ZHVI",
                              line=dict(color="#ff7f0e", width=2, dash="dot")))
    fig1.update_layout(title="Typical Home Value — Heights vs Metro",
                       yaxis_title="Typical Value ($)", template="plotly_white",
                       height=420, margin=dict(l=40, r=20, t=60, b=40),
                       legend=dict(orientation="h", yanchor="bottom", y=1.02))
    fig1.update_yaxes(tickprefix="$", tickformat=",.0f")

    # 2. Rate correlation
    value_chg = [0] + [(zhvi_77008[i] - zhvi_77008[i-1]) / zhvi_77008[i-1] * 100
                       for i in range(1, len(zhvi_77008))]
    fig2 = go.Figure(go.Scatter(
        x=mortgage_rates, y=value_chg, mode="markers+text",
        text=[d[-5:] for d in dates], textposition="top center",
        marker=dict(size=12, color=mortgage_rates, colorscale="RdYlGn_r", showscale=True,
                    colorbar=dict(title="Rate %")), name="Period change"))
    fig2.update_layout(title="Mortgage Rate vs Subsequent Value Change",
                       xaxis_title="30-yr Rate (%)", yaxis_title="Value Change (%)",
                       template="plotly_white", height=420)

    # 3. Inventory + DOM
    fig3 = make_subplots(specs=[[{"secondary_y": True}]])
    fig3.add_trace(go.Scatter(x=dates, y=months_supply, name="Months of Supply",
                              line=dict(color="#2ca02c")), secondary_y=False)
    fig3.add_trace(go.Scatter(x=dates, y=dom, name="Median DOM",
                              line=dict(color="#d62728", dash="dash")), secondary_y=True)
    fig3.add_trace(go.Scatter(x=dates, y=[v/10000 for v in zhvi_77008],
                              name="Value (scaled /10k)",
                              line=dict(color="#1f77b4", width=1, dash="dot")), secondary_y=False)
    fig3.update_layout(title="Inventory Tightness & DOM vs Value",
                       template="plotly_white", height=420,
                       legend=dict(orientation="h", y=1.1))
    fig3.update_yaxes(title_text="Months Supply / Value scaled", secondary_y=False)
    fig3.update_yaxes(title_text="Median DOM", secondary_y=True)

    # 4. $/sqft history
    fig4 = go.Figure(go.Bar(x=years_psf, y=psf, marker_color="#9467bd"))
    fig4.update_layout(title="Heights Median Sold $/SqFt (HAR-style)",
                       yaxis_title="$ / SqFt", template="plotly_white", height=380)

    # 5. Illustrative scenarios
    last = zhvi_77008[-1]
    future = ["2026-09", "2026-12", "2027-03", "2027-06",
              "2027-09", "2027-12", "2028-03", "2028-06"]
    scenarios = {
        "Base (~6.5%)": [last * (1 + 0.015 * i) for i in range(1, 9)],
        "Rates –50 bp": [last * (1 + 0.025 * i) for i in range(1, 9)],
        "Rates +50 bp": [last * (1 + 0.005 * i) for i in range(1, 9)]
    }
    fig5 = go.Figure()
    for name, vals in scenarios.items():
        fig5.add_trace(go.Scatter(x=future, y=vals, name=name, mode="lines+markers"))
    fig5.update_layout(title="Illustrative Forward Paths (not a formal forecast)",
                       yaxis_title="Projected Typical Value ($)",
                       template="plotly_white", height=400,
                       legend=dict(orientation="h", y=1.1))
    fig5.update_yaxes(tickprefix="$", tickformat=",.0f")

    # Build self-contained HTML
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Houston Heights SFH Dashboard</title>
<script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
<style>
body {{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
       margin:0;padding:12px;background:#f7f8fa;color:#1a1a1a;}}
h1 {{font-size:1.4rem;margin:8px 0 4px;}}
.kpi {{display:flex;flex-wrap:wrap;gap:10px;margin:12px 0;}}
.kpi-card {{background:white;border-radius:10px;padding:12px 16px;
            box-shadow:0 1px 3px rgba(0,0,0,.08);flex:1 1 140px;min-width:130px;}}
.kpi-label {{font-size:.75rem;color:#666;}}
.kpi-value {{font-size:1.25rem;font-weight:600;margin-top:2px;}}
.chart {{background:white;border-radius:10px;padding:8px;margin:12px 0;
         box-shadow:0 1px 3px rgba(0,0,0,.08);}}
.note {{font-size:.8rem;color:#555;margin:8px 0 16px;line-height:1.4;}}
footer {{font-size:.75rem;color:#888;margin-top:24px;padding-top:12px;border-top:1px solid #eee;}}
</style>
</head>
<body>
<h1>Houston Heights Single-Family Dashboard</h1>
<p class="note">Research view · Core ZIPs 77007/77008/77009 · Mobile-optimized · Aug 2026</p>
<div class="kpi">
  <div class="kpi-card"><div class="kpi-label">Typical Value (77008)</div><div class="kpi-value">~$591k</div></div>
  <div class="kpi-card"><div class="kpi-label">YoY Change</div><div class="kpi-value" style="color:#c0392b">~-1.0%</div></div>
  <div class="kpi-card"><div class="kpi-label">30-yr Rate</div><div class="kpi-value">~6.65%</div></div>
  <div class="kpi-card"><div class="kpi-label">Approx. MOS</div><div class="kpi-value">4.5–4.6</div></div>
</div>
"""
    for i, fig in enumerate([fig1, fig2, fig3, fig4, fig5], 1):
        div_id = f"chart{i}"
        html += f'<div class="chart"><div id="{div_id}"></div></div>\n'
        # Note: to_json is called twice in f-string for simplicity; in production cache it
        j = fig.to_json()
        html += f"<script>Plotly.newPlot('{div_id}', {j}.data, {j}.layout, {{responsive:true, displayModeBar:true}});</script>\n"

    html += f"""
<p class="note">
<strong>Key observations:</strong><br>
• Heights has shown relative resilience vs. broader Houston metro, supported by limited historic-district supply.<br>
• Mortgage rates remain the dominant short-term lever; local inventory tightness provides a buffer.<br>
• Scenario paths are illustrative only — not statistical forecasts.<br>
• Sources: Zillow ZHVI, HAR/MLS, Redfin, FRED.
</p>
<footer>Generated {datetime.now().strftime("%Y-%m-%d %H:%M")} · Research only · Not investment advice<br>
Push this HTML + the .py to GitHub and enable Pages for permanent iPhone access.</footer>
</body></html>
"""
    out = Path("houston_heights_dashboard.html")
    out.write_text(html, encoding="utf-8")
    print(f"Dashboard written → {out.resolve()}")
    return out

if __name__ == "__main__":
    build_dashboard()
