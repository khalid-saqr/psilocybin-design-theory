from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass
class TraceIssue:
    severity: str
    name: str
    message: str


def ids(items: Iterable[dict]) -> set[str]:
    return {str(item.get("id", "")) for item in items if item.get("id")}


def check_unknown_refs(
    refs: Iterable[str], known: set[str], *, name: str, owner: str, severity: str = "error"
) -> list[TraceIssue]:
    issues: list[TraceIssue] = []
    for ref in refs:
        if ref not in known:
            issues.append(TraceIssue(severity, name, f"{owner} references unknown id: {ref}"))
    return issues


def traceability_issues(design: dict) -> list[TraceIssue]:
    issues: list[TraceIssue] = []
    verb_ids = ids(design.get("hidden_verbs", []))
    relation_ids = ids(design.get("relations", []))
    invariant_ids = ids(design.get("invariants", []))
    survival_ids = ids(design.get("survival_conditions", []))
    all_ids = verb_ids | relation_ids | invariant_ids | survival_ids | ids(design.get("death_conditions", []))

    for verb in design.get("hidden_verbs", []):
        if verb.get("verb") and not verb.get("evidence"):
            issues.append(TraceIssue("error", "hidden_verbs.trace_to_language", f"{verb.get('id')} has no evidence."))

    for relation in design.get("relations", []):
        if relation.get("name") and not relation.get("traces_to_verbs"):
            issues.append(TraceIssue("error", "relations.trace_to_verbs", f"{relation.get('id')} has no verb trace."))
        issues.extend(check_unknown_refs(relation.get("traces_to_verbs", []), verb_ids, name="relations.trace_to_verbs", owner=str(relation.get("id"))))

    for invariant in design.get("invariants", []):
        if invariant.get("statement") and not invariant.get("traces_to_relations"):
            issues.append(TraceIssue("error", "invariants.trace_to_relations", f"{invariant.get('id')} has no relation trace."))
        issues.extend(check_unknown_refs(invariant.get("traces_to_relations", []), relation_ids, name="invariants.trace_to_relations", owner=str(invariant.get("id"))))

    genome = design.get("genome", {}) or {}
    if genome.get("statement"):
        if not genome.get("traces_to_invariants"):
            issues.append(TraceIssue("error", "genome.trace_to_invariants", "Genome statement has no invariant trace."))
        issues.extend(check_unknown_refs(genome.get("traces_to_invariants", []), invariant_ids, name="genome.trace_to_invariants", owner="genome"))

    for condition in design.get("survival_conditions", []):
        if condition.get("condition") and not condition.get("test"):
            issues.append(TraceIssue("error", "survival_conditions.testable", f"{condition.get('id')} has no test."))
        issues.extend(check_unknown_refs(condition.get("traces_to_invariants", []), invariant_ids, name="survival_conditions.trace_to_invariants", owner=str(condition.get("id"))))

    for condition in design.get("death_conditions", []):
        if condition.get("condition") and not condition.get("why_dead_even_if_running"):
            issues.append(TraceIssue("error", "death_conditions.explicit", f"{condition.get('id')} has no reason."))
        issues.extend(check_unknown_refs(condition.get("traces_to_survival", []), survival_ids, name="death_conditions.trace_to_survival", owner=str(condition.get("id"))))

    stack = design.get("stack", {}) or {}
    selected = stack.get("selected", {}) or {}
    if selected.get("name") and not genome.get("statement"):
        issues.append(TraceIssue("error", "stack.trace_to_genome", "Stack is selected before genome exists."))
    if selected.get("name"):
        if not stack.get("traces_to_genome"):
            issues.append(TraceIssue("error", "stack.trace_to_genome", "Selected stack is not marked as tracing to genome."))
        if not stack.get("traces_to_survival"):
            issues.append(TraceIssue("error", "stack.trace_to_survival", "Selected stack has no survival traces."))
        issues.extend(check_unknown_refs(stack.get("traces_to_survival", []), survival_ids, name="stack.trace_to_survival", owner="stack"))

    for phase in design.get("implementation_sequence", []):
        if phase.get("phase") and not phase.get("traces_to"):
            issues.append(TraceIssue("error", "implementation_sequence.traceable", f"{phase.get('id')} has no trace."))
        issues.extend(check_unknown_refs(phase.get("traces_to", []), all_ids | {"genome", "ontology", "stack"}, name="implementation_sequence.traceable", owner=str(phase.get("id")), severity="warning"))

    return issues
