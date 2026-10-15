# Assumptions and Limitations

The SHADOW-Q benchmarks are engineering simulations intended to test architecture assumptions and derive measurable requirements. They are not flight demonstrations.

## General

- Scenarios use fixed random seeds and synthetic or physically motivated inputs.
- Reported comparisons are benchmark-specific and should not be extrapolated to all lunar missions.
- Exact optima are used only where computationally practical.
- Timing measurements depend on the development environment. Any onboard timing projection is an assumption until processor-in-the-loop measurement is completed.

## B1 — Value-of-Drill site selection

- Synthetic resource fields and sensor models are used.
- The public evidence shows the performance trade-off between site regret and map error; it does not disclose the internal decision-score implementation.

## B2 — Fleet assignment / accelerator specification

- The reported study uses a small fleet-assignment family and synthetic target values.
- Quantisation and analog noise are emulated.
- Public data show benchmark outcomes and acceptance thresholds, not the internal QUBO construction or penalty design.

## B3 — Coordination

- Radio loss is represented statistically rather than by a terrain-resolved RF model.
- Agreement-time values in the public results describe the election/agreement stage after failure detection; total recovery also includes the configured detection timeout.

## B4 — Shadow Clock

- Terrain and illumination are simulated in the benchmark evidence.
- Battery and thermal behaviour are simplified.
- The public package reports route outcomes but does not publish the production planner implementation.

## B5 — Cooperative localisation

- The model is two-dimensional.
- Anchor locations are assumed known and UWB non-line-of-sight effects are statistical.
- Results are simulation evidence, not hardware localisation certification.

## B6 — Drill operations

- Drill, power, volatile-loss, and thermal models are simplified.
- The public package reports policy outcomes but does not disclose the internal adaptive drill-decision implementation.

## B7 — Scaling

- Flight-processor slowdown is an explicit projection rather than a measurement.
- Only the reported optimisation family is examined.
- The benchmark intentionally includes negative results from a naive penalty-QUBO approach.

## B8 — QAOA warm starts

- QAOA results are from exact classical statevector simulation in the reported benchmark.
- They do not demonstrate quantum advantage or operational quantum readiness.
- The public package reports outcome statistics but not the internal QAOA/QUBO implementation.
