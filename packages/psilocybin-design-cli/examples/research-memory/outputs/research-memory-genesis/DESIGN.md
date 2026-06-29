# Psilocybin Design Memory

## Gap

- Failed relation: Research outputs are detached from the reasoning that produced them.
- Present arrangement: Slack, notebooks, paper drafts, and commit history are searched manually.
- Missing possibility: The team cannot reliably recover why a decision was made.

## Language-game

- Why did we do it this way?
- Was this result superseded?
- Who approved this?
- What evidence supported that change?

## Hidden verbs

- `verb-remember`: remember — evidence: Why did we do it this way?
- `verb-verify`: verify — evidence: What evidence supported that change?
- `verb-decay`: decay — evidence: Was this result superseded?

## Relations

- `relation-decision-evidence`: decision_to_evidence (Decision → Evidence) — Every major decision must cite supporting evidence.
- `relation-result-status`: result_to_status (Result → Status) — Every result must show whether it is current, superseded, disputed, or obsolete.

## Invariants

- `invariant-decision-evidence`: A major decision without evidence is incomplete.
- `invariant-superseded-visible`: A superseded result remains findable but must not appear current.

## Genome

The system preserves research decision memory by connecting decisions, evidence, actors, status changes, and supersession events so the team can recover why something happened and whether it still holds.

## Organism

- Model: research-memory organism
- Boundary inside: Decision, Evidence, Actor, Result, StatusTransition, Supersession
- Boundary outside: generic task management, full paper search, laboratory notebook replacement
- Reason: The organism must preserve decision identity under changing research context.

## Ontology

- Entities: Decision, Evidence, Actor, Result, Claim, StatusTransition, Supersession
- Relations: Decision supported_by Evidence, Decision made_by Actor, Result has_status StatusTransition, Claim supersedes Claim
- States: current, superseded, disputed, obsolete
- Boundaries: inside decision provenance, outside raw document storage

## Survival conditions

- `survival-decision-trace`: Every major decision can be traced to supporting evidence. — test: Create a major decision without evidence; system must reject it or mark it incomplete.
- `survival-supersession`: Superseded results remain visible but cannot appear current. — test: Mark a result superseded; current-result views must exclude it unless explicitly requested.

## Death conditions

- `death-document-dump`: The system stores documents but cannot reconstruct decisions. — why dead even if running: It no longer preserves the design genome of research decision memory.
- `death-obsolete-current`: Obsolete results appear current. — why dead even if running: The system destroys the distinction required for knowledge decay.

## Stack rationale

Selected stack: FastAPI + PostgreSQL + React

Relational traceability, provenance, statuses, and multi-actor audit are central to the genome.
