# SHADOW-Q Benchmark Evidence

Public, non-flight research evidence supporting Nexorion Spacetech Ltd's **SHADOW-Q** lunar decision-intelligence work.

## Scope

This repository is deliberately limited to **public benchmark evidence**: curated result summaries, figures, assumptions, limitations, and utilities for inspecting the published data.

It **does not contain** the production SHADOW-Q software or the internal implementations of:

- Value-of-Drill decision logic;
- application-specific QUBO construction, constraint pruning, penalty design, or decomposition;
- Mission Assurance Boundary implementation details;
- internal solver-orchestration and tuning logic;
- proprietary drill-planning, coordination, or quantum warm-start pipelines;
- customer, partner, or mission-specific interfaces.

The repository is therefore suitable for technical review of the stated evidence without representing the commercial product codebase.

## Status

- Research / engineering benchmark evidence only.
- Simulation results are **not flight-performance claims**.
- SHADOW-Q remains classical-first: conventional computing is the operational baseline; quantum and photonic approaches are experimental acceleration paths.
- Figures and numerical summaries correspond to the public benchmark narrative used in the SHADOW-Q technical proposal.

## Benchmark catalogue

| ID | Public question | Headline public evidence |
|---|---|---|
| B1 | Can scarce drill cycles be spent more intelligently? | Value-of-Drill reduces site-selection regret versus random drilling while retaining useful map quality. |
| B2 | Does optimised fleet assignment beat a greedy rule, and what accelerator quality is required? | Best-of classical portfolio reaches 95.7% of optimum versus 79.7% for greedy on the reported 44-variable study; useful analog acceleration requires high coefficient precision and low noise. |
| B3 | Can a fleet avoid false failovers and agree on a new coordinator under packet loss? | A longer timeout with relay suppresses false failovers; epoch-based election produced 100% agreement in the reported study. |
| B4 | Does time-aware illumination planning avoid darkness? | Shadow Clock reported zero planned dark exposure and 95.7% route success in the stated simulation. |
| B5 | Can cooperative localisation remain accurate without GNSS? | Robust EKF fusion reported 0.23 m RMSE and 0.42 m p95 error in the stated simulation. |
| B6 | Can drill-cycle decisions improve scarce-cycle resource identification? | With about two cycles available, Value-of-Drill reported 68.5% success versus 50% for a fixed timeline; illumination forecasting removed simulated aborts. |
| B7 | Where does classical onboard optimisation begin to struggle? | Exact solving scales poorly; greedy remains fast but loses value; naive penalty-QUBO annealing degrades at larger sizes. |
| B8 | Can QAOA provide useful warm-start candidates? | A simulated QAOA-to-classical warm-start pipeline worked end-to-end; this is **not** a claim of quantum advantage. |

Detailed curated values are in [`results/`](results/). Method boundaries and limitations are documented in [`docs/`](docs/).

## Repository layout

```text
shadow-q-benchmark-evidence/
├── README.md
├── NOTICE.md
├── CITATION.cff
├── MANIFEST_SHA256.txt
├── results/                 # curated public numerical evidence
├── figures/                 # public figure previews
├── scripts/                 # utilities that operate only on public result files
└── docs/
    ├── BENCHMARK_CATALOGUE.md
    ├── ASSUMPTIONS_AND_LIMITATIONS.md
    └── PUBLIC_SCOPE.md
```

## Inspecting the results

The repository intentionally does not reproduce proprietary optimisation implementations. You can still validate the public evidence package structurally:

```bash
python scripts/verify_public_results.py
```

To generate simple summary plots from the public JSON files:

```bash
python scripts/make_summary_plots.py
```

The generated plots use only the public numerical summaries contained in this repository.

## Benchmark identifiers

The public benchmark IDs B1-B8 are stable references used in Nexorion technical material. The public summaries are intentionally narrower than the internal development datasets and source code.

## Authors

- **Utsav Jayant Talekar** — Co-Founder & CTO, Nexorion Spacetech Ltd; technical lead for SHADOW-Q and author of the benchmark suite (B1–B8)
- **Thien Nguyen Quang Bui** — Co-Founder & CEO, Nexorion Spacetech Ltd; research direction for resource optimisation and solver development

## Citation

If referring to this evidence package, please cite:

> Talekar, U. J. and Bui, T. N. Q. (Nexorion Spacetech Ltd), *SHADOW-Q Benchmark Evidence*, public research evidence package, v0.1.0, 2026. https://github.com/nexorionspacetech/shadow-q-benchmark-evidence

## Copyright and use

Copyright © 2026 Nexorion Spacetech Ltd. All rights reserved.

No open-source licence is granted by publication of this repository. See [`NOTICE.md`](NOTICE.md).

## Contact

Nexorion Spacetech Ltd  
`info@nexorionspacetech.com`

Technical lead: Utsav Jayant Talekar — `utsav.talekar@nexorionspacetech.com`