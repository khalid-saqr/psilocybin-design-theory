from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

from psilocybin_design_cli.core.schema import validate_with_schema
from psilocybin_design_cli.core.traceability import traceability_issues

Severity = Literal["pass", "warning", "error"]


@dataclass
class ValidationMessage:
    severity: Severity
    name: str
    message: str


@dataclass
class ValidationReport:
    messages: list[ValidationMessage] = field(default_factory=list)

    @property
    def errors(self) -> list[ValidationMessage]:
        return [m for m in self.messages if m.severity == "error"]

    @property
    def warnings(self) -> list[ValidationMessage]:
        return [m for m in self.messages if m.severity == "warning"]

    @property
    def ok(self) -> bool:
        return not self.errors

    def add(self, severity: Severity, name: str, message: str) -> None:
        self.messages.append(ValidationMessage(severity, name, message))

    def to_dict(self) -> dict:
        return {"ok": self.ok, "messages": [m.__dict__ for m in self.messages]}


def has_text(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def has_list(value: object) -> bool:
    return isinstance(value, list) and len(value) > 0


def validate_design(design: dict, *, strict: bool = False) -> ValidationReport:
    report = ValidationReport()

    schema_errors = validate_with_schema(design, "psilocybin-design.schema.json")
    if schema_errors:
        for err in schema_errors:
            report.add("error", "schema.valid", err)
    else:
        report.add("pass", "schema.valid", "YAML matches the Psilocybin Design schema.")

    project = design.get("project", {}) or {}
    gap = design.get("gap", {}) or {}
    language = design.get("language_game", {}) or {}
    genome = design.get("genome", {}) or {}
    organism = design.get("organism", {}) or {}
    ontology = design.get("ontology", {}) or {}
    agent = design.get("agent_contract", {}) or {}

    if has_text(project.get("raw_intention")):
        report.add("pass", "project.raw_intention", "Raw intention is present.")
    else:
        report.add("warning", "project.raw_intention", "Raw intention is empty.")

    if has_text(gap.get("failed_relation")):
        report.add("pass", "gap.exists", "Gap failed relation is present.")
    else:
        report.add("warning", "gap.exists", "Gap failed relation is empty.")

    language_evidence = any(
        has_list(language.get(k)) for k in ["repeated_phrases", "workarounds", "tensions", "judgments"]
    )
    if language_evidence:
        report.add("pass", "language_game.has_evidence", "Language-game evidence is present.")
    else:
        report.add("warning", "language_game.has_evidence", "Language-game evidence is empty.")

    for issue in traceability_issues(design):
        report.add(issue.severity, issue.name, issue.message)

    if genome.get("statement"):
        report.add("pass", "genome.exists", "Genome statement is present.")
    else:
        report.add("warning", "genome.exists", "Genome statement is empty.")

    if organism.get("model") and organism.get("boundary_inside"):
        report.add("pass", "organism.has_boundary", "Organism model and boundary are present.")
    else:
        report.add("warning", "organism.has_boundary", "Organism model or boundary is incomplete.")

    if ontology.get("entities") and ontology.get("relations"):
        report.add("pass", "ontology.supports_genome", "Ontology entities and relations are present.")
    else:
        report.add("warning", "ontology.supports_genome", "Ontology is incomplete.")

    if design.get("survival_conditions"):
        report.add("pass", "survival_conditions.present", "Survival conditions are present.")
    else:
        report.add("warning", "survival_conditions.present", "No survival conditions are present.")

    if design.get("death_conditions"):
        report.add("pass", "death_conditions.present", "Death conditions are present.")
    else:
        report.add("warning", "death_conditions.present", "No death conditions are present.")

    stack = design.get("stack", {}) or {}
    if (stack.get("selected", {}) or {}).get("name"):
        report.add("pass", "stack.selected", "Stack selection is present.")
    else:
        report.add("warning", "stack.selected", "No stack is selected.")

    if stack.get("alternatives"):
        report.add("pass", "stack.alternatives", "Stack alternatives are present.")
    else:
        report.add("warning", "stack.alternatives", "No stack alternatives are present.")

    if genome.get("must_repair"):
        report.add("pass", "genome.repair", "Repair logic is present.")
    else:
        report.add("warning", "genome.repair", "No repair logic is recorded.")

    if genome.get("must_decay"):
        report.add("pass", "genome.decay", "Decay logic is present.")
    else:
        report.add("warning", "genome.decay", "No decay logic is recorded.")

    if agent.get("instructions"):
        report.add("pass", "agent_contract.present", "Agent contract instructions are present.")
    else:
        report.add("warning", "agent_contract.present", "Agent contract instructions are empty.")

    if strict:
        for msg in list(report.messages):
            if msg.severity == "warning":
                msg.severity = "error"  # type: ignore[assignment]
                msg.message = f"Strict mode: {msg.message}"

    return report


def assert_renderable(report: ValidationReport, *, allow_warnings: bool = False) -> None:
    if report.errors:
        details = "\n".join(f"ERROR {m.name}: {m.message}" for m in report.errors)
        raise ValueError(f"Validation has hard failures:\n{details}")
    if report.warnings and not allow_warnings:
        details = "\n".join(f"WARN {m.name}: {m.message}" for m in report.warnings)
        raise ValueError(f"Validation has warnings. Use --allow-warnings to continue.\n{details}")
