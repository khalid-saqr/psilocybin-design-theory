# Survival Tests

Survival tests protect the design genome. A system may still run while being dead
relative to its original Psilocybin Design identity; these tests prevent that.

## survival-decision-trace

- Condition: Every major decision can be traced to supporting evidence.
- Test: Create a major decision without evidence; system must reject it or mark it incomplete.
- Evidence: What evidence supported that change?
- Traces to invariants: invariant-decision-evidence
## survival-supersession

- Condition: Superseded results remain visible but cannot appear current.
- Test: Mark a result superseded; current-result views must exclude it unless explicitly requested.
- Evidence: Was this result superseded?
- Traces to invariants: invariant-superseded-visible

## Death conditions to preserve

- `death-document-dump`: The system stores documents but cannot reconstruct decisions. — It no longer preserves the design genome of research decision memory.
- `death-obsolete-current`: Obsolete results appear current. — The system destroys the distinction required for knowledge decay.
