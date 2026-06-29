# Implementation Sequence

Implement the software organism described by the design genome in the following order.

## 1. Genome-bearing data model

- ID: `phase-data-model`
- Purpose: Create entities that preserve decision memory and supersession.
- Files to create:
  - `backend/models.py`
  - `backend/migrations/0001_initial.sql`
- Validation:
  - Decision requires evidence before completion
  - Result has explicit status
- Traces to: invariant-decision-evidence, invariant-superseded-visible
## 2. Survival APIs

- ID: `phase-survival-api`
- Purpose: Implement APIs that enforce evidence trace and supersession logic.
- Files to create:
  - `backend/api/decisions.py`
  - `backend/api/results.py`
- Validation:
  - Survival tests pass
- Traces to: survival-decision-trace, survival-supersession
