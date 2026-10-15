# Benchmark Catalogue

## B1 — Value-of-Drill site selection

**Question:** Can limited drill cycles improve both extraction-site choice and knowledge of the resource map?

**Public evidence:** 120 simulated campaigns. Reported site regret: random 0.44, fixed grid 0.46, greedy-mean 0.24, max-variance 0.45, Value-of-Drill 0.23. Reported map RMSE: 0.43, 0.43, 0.45, 0.39, and 0.43 respectively.

## B2 — Fleet task assignment and accelerator specification

**Question:** How much mission value is lost by a simple greedy assignment, and what effective coefficient quality would an Ising-type accelerator need?

**Public evidence:** 200 reported 44-variable instances. Greedy 79.7% of optimum; simulated annealing 93.0%; best-of portfolio 95.7%. At 10-bit coefficient precision, 0.25% full-scale analog noise retained 93.1% of optimum in the reported sweep, while 1% noise fell below the greedy reference.

## B3 — Failure detection and coordinator agreement

**Question:** How should timeout/relay behaviour be set under bursty communication loss, and can surviving assets agree on one coordinator?

**Public evidence:** With bursty loss plus relay, the reported 1 s timeout produced zero false failovers up to 10% mean loss, 0.25 per hour at 15%, and 1.5 per hour at 20%. The epoch-based election study reported 100% agreement, with 450 ms p99 agreement time after detection at the highest reported loss point.

## B4 — Shadow Clock

**Question:** Does planning over position and time avoid routes that become dark after departure?

**Public evidence:** 23 reported start-goal pairs. Snapshot planning found a route in 69.6% of cases and 31.25% of those routes entered darkness. Shadow Clock found a route in 95.7% of cases with zero planned dark exposure.

## B5 — Cooperative localisation

**Question:** Can visual odometry, IMU information and UWB ranging maintain useful localisation without GNSS?

**Public evidence:** 30 simulated two-hour traverses. Robust EKF: 0.228 m RMSE, 0.422 m p95 error, 0.298 m RMSE during the simulated lens-dust event, and error below 0.5 m for 97.1% of the reported time.

## B6 — Lander drill-operations planning

**Question:** When drill cycles are scarce, can adaptive depth/timing decisions improve the probability of correctly identifying the ice-table state?

**Public evidence:** In the 48-hour / approximately two-cycle case, reported success was 50.0% for the fixed timeline, 59.5% for bisection, and 68.5% for Value-of-Drill. Illumination forecasting removed simulated cycle aborts in the reported runs.

## B7 — Scaling

**Question:** Where do exact and heuristic approaches become unsuitable for rapid onboard replanning?

**Public evidence:** Reported exact workstation solve time grew from 0.013 s at 44 variables to 59.1 s at 2,184 variables. Greedy quality declined from 82.7% to 63.9% of optimum. Naive penalty-QUBO annealing degraded beyond the smallest reported size, illustrating that acceleration does not fix a weak formulation.

## B8 — QAOA warm-start evidence

**Question:** Can a simulated QAOA pipeline produce candidate states that are useful as starts for a classical optimiser?

**Public evidence:** At 10 qubits, the reported QAOA-started short classical search reached 97.5% of optimum versus 8.4% from a random start. At 15 qubits it reached 46.8% versus 14.9%. These are simulation results and do not constitute quantum-advantage evidence.
