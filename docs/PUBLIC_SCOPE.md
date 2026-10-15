# Public Scope and IP Boundary

This public package is designed to support independent reading of SHADOW-Q benchmark evidence while keeping implementation-specific know-how outside the public repository.

## Included publicly

- benchmark purpose and scenario summaries;
- numerical headline results already intended for external technical review;
- public figures derived from those results;
- assumptions and limitations needed to interpret the evidence;
- utilities for validating and plotting the public result files.

## Deliberately not included

- production or internal benchmark source code for application-specific decision logic;
- Value-of-Drill scoring implementation and tuning;
- SHADOW-Q QUBO matrix construction, penalty design, structural pruning, and decomposition logic;
- solver-selection and tuning pipelines;
- Mission Assurance Boundary production rules and implementation;
- detailed drill scheduling and Bayesian decision implementation;
- full coordinator-election implementation and internal weighting logic;
- QAOA circuit-generation and warm-start implementation tied to internal SHADOW-Q QUBOs;
- proposal-generation source files, internal documents, or private interfaces.

The absence of those files is intentional. This repository is an evidence package, not the commercial SHADOW-Q codebase.
