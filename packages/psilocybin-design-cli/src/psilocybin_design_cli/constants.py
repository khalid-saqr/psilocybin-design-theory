from __future__ import annotations

APP_NAME = "psilocybin"
PACKAGE_NAME = "psilocybin-design-cli"
VERSION = "1.0.0"
DESIGN_FILENAME = "psilocybin.design.yaml"
SCHEMA_VERSION = "1.0"

STAGES = [
    "project",
    "gap",
    "language",
    "verbs",
    "relations",
    "invariants",
    "genome",
    "organism",
    "ontology",
    "survival",
    "death",
    "stack",
    "sequence",
    "agents",
]

LLM_STAGES = [
    "verbs",
    "relations",
    "invariants",
    "genome",
    "organism",
    "ontology",
    "survival",
    "death",
    "stack",
    "sequence",
    "agents",
]

ALLOWED_TARGET_PATHS = {
    "hidden_verbs",
    "relations",
    "invariants",
    "genome",
    "organism",
    "ontology",
    "survival_conditions",
    "death_conditions",
    "stack",
    "implementation_sequence",
    "agent_contract",
}

CONTROLLED_VERBS = [
    "sense",
    "remember",
    "verify",
    "route",
    "reconcile",
    "connect",
    "transform",
    "authorize",
    "preserve",
    "repair",
    "protect",
    "expose",
    "forget",
    "decay",
    "recover",
    "classify",
    "compare",
    "explain",
    "audit",
]

REQUIRED_GENESIS_FILES = [
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    ".github/copilot-instructions.md",
    "DESIGN.md",
    "IMPLEMENTATION_SEQUENCE.md",
    "SURVIVAL_TESTS.md",
    "psilocybin.design.yaml",
    "docs/genome.md",
    "docs/organism.md",
    "docs/ontology.md",
    "docs/stack-rationale.md",
    "docs/decision-memory.md",
    "tests/survival/README.md",
]
