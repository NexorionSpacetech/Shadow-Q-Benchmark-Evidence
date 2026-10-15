#!/usr/bin/env python3
"""Generate simple plots from curated public SHADOW-Q result summaries only."""
from pathlib import Path
import json
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
OUT = ROOT / "_generated"
OUT.mkdir(exist_ok=True)

# B1: site regret
b1 = json.loads((RESULTS / "b1_summary.json").read_text())
vals = b1["metrics"]["site_regret_mean"]
fig, ax = plt.subplots(figsize=(7, 4))
ax.bar(list(vals.keys()), list(vals.values()))
ax.set_ylabel("Mean site regret (lower is better)")
ax.set_title("B1 public result summary")
ax.tick_params(axis="x", rotation=25)
fig.tight_layout()
fig.savefig(OUT / "b1_site_regret.png", dpi=180)
plt.close(fig)

# B2: solver quality
b2 = json.loads((RESULTS / "b2_summary.json").read_text())
q = b2["metrics"]["utility_pct_of_optimum"]
fig, ax = plt.subplots(figsize=(7, 4))
ax.bar(list(q.keys()), list(q.values()))
ax.set_ylabel("Utility (% of optimum)")
ax.set_title("B2 public result summary")
ax.tick_params(axis="x", rotation=30)
fig.tight_layout()
fig.savefig(OUT / "b2_solver_quality.png", dpi=180)
plt.close(fig)

# B6: success vs cycle window
b6 = json.loads((RESULTS / "b6_summary.json").read_text())
windows = ["~2 cycles", "~5 cycles", "~10 cycles"]
series = {
    "fixed": [b6["metrics"]["48h_approx_2_cycles_success_pct"]["fixed_timeline"], b6["metrics"]["120h_approx_5_cycles_success_pct"]["fixed_timeline"], b6["metrics"]["240h_approx_10_cycles_success_pct"]["fixed_timeline"]],
    "bisection": [b6["metrics"]["48h_approx_2_cycles_success_pct"]["bisection"], b6["metrics"]["120h_approx_5_cycles_success_pct"]["bisection"], b6["metrics"]["240h_approx_10_cycles_success_pct"]["bisection"]],
    "Value-of-Drill": [b6["metrics"]["48h_approx_2_cycles_success_pct"]["value_of_drill"], b6["metrics"]["120h_approx_5_cycles_success_pct"]["value_of_drill"], b6["metrics"]["240h_approx_10_cycles_success_pct"]["value_of_drill"]]
}
fig, ax = plt.subplots(figsize=(7, 4))
for name, ys in series.items():
    ax.plot(windows, ys, marker="o", label=name)
ax.set_ylabel("Decision success (%)")
ax.set_title("B6 public result summary")
ax.legend()
fig.tight_layout()
fig.savefig(OUT / "b6_cycle_budget.png", dpi=180)
plt.close(fig)

# B7: exact solve time and quality
b7 = json.loads((RESULTS / "b7_summary.json").read_text())
sizes = b7["sizes"]
x = [s["decision_variables"] for s in sizes]
y = [s["exact_workstation_s"] for s in sizes]
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(x, y, marker="o")
ax.set_yscale("log")
ax.set_xlabel("Decision variables")
ax.set_ylabel("Exact solve time on development workstation (s)")
ax.set_title("B7 public timing summary")
fig.tight_layout()
fig.savefig(OUT / "b7_scaling.png", dpi=180)
plt.close(fig)

print(f"Wrote summary plots to {OUT}")
