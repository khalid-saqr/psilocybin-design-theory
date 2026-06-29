# Psilocybin Genesis CLI

Version: **1.0.1 Stable MVP**

Psilocybin Genesis CLI is a local-first, LLM-assisted design compiler. It guides
a user through Psilocybin Design Theory and emits an agent-readable
**genesis-repo** for Codex, GitHub Copilot, Claude Code, or another coding agent.

The CLI does **not** implement the user's final software. It produces a structured
seed repository containing the design genome, ontology, survival tests, stack
rationale, implementation sequence, and agent instructions required for a coding
agent to implement the software organism described by the design genome.

## What it does

- Creates a local design workspace.
- Maintains `psilocybin.design.yaml` as canonical design memory.
- Guides the user through gap, language-game, hidden verbs, relations,
  invariants, genome, organism, ontology, survival/death conditions, stack, and
  implementation sequence.
- Optionally asks a local LLM for structured suggestions.
- Requires user acceptance before LLM suggestions enter the design memory.
- Validates schema and traceability deterministically.
- Renders a genesis-repo directory and `.zip` pack.
- Generates `AGENTS.md`, `CLAUDE.md`, and `.github/copilot-instructions.md`.

## What it does not do

- It does not build the final application.
- It does not require a cloud LLM.
- It does not include model weights.
- It does not create GitHub repositories.
- It does not claim that software is biologically alive.
- It does not silently let an LLM overwrite the design.

## Installation

From the package directory:

```bash
cd packages/psilocybin-design-cli
python -m pip install -e .
```

Then verify:

```bash
psilocybin --help
psilocybin doctor
```

## Deterministic quickstart

```bash
psilocybin init research-memory
cd research-memory.design
psilocybin interview
psilocybin validate
psilocybin render --allow-warnings
psilocybin pack --allow-warnings
```

The generated pack appears under:

```text
outputs/research-memory-genesis.zip
```

## Example workflow from fixture

```bash
psilocybin validate --file examples/research-memory/psilocybin.design.yaml
psilocybin render --file examples/research-memory/psilocybin.design.yaml --output /tmp/research-memory-genesis
psilocybin pack --file examples/research-memory/psilocybin.design.yaml --output /tmp/research-memory-genesis.zip
```

## Optional local LLM setup

The default runtime is Ollama. The default configured model tag is `qwen3:4b`, but
model availability is not assumed. Use `doctor` to verify what is actually
available locally.

```bash
ollama pull qwen3:4b
psilocybin config set llm.enabled true
psilocybin config set llm.provider ollama
psilocybin config set llm.model qwen3:4b
psilocybin config set llm.base_url http://localhost:11434
psilocybin doctor
psilocybin suggest verbs
psilocybin accept verbs
```

Any OpenAI-compatible local endpoint can also be configured:

```bash
psilocybin config set llm.provider openai-compatible
psilocybin config set llm.base_url http://localhost:8000/v1
psilocybin config set llm.model Qwen/Qwen3-4B-Instruct-2507
```

## LLM authority model

The LLM is not the design authority.

```text
LLM suggests.
User accepts or edits.
Schema stores.
Validator checks.
Renderer writes files.
Packager emits genesis-repo.
Coding agent implements from the genesis-repo.
```

LLM outputs are written to `suggestions/<stage>.suggestion.json`. They never
modify `psilocybin.design.yaml` until accepted by the user.

## Generated genesis-repo structure

```text
<project>-genesis/
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── .github/
│   └── copilot-instructions.md
├── DESIGN.md
├── IMPLEMENTATION_SEQUENCE.md
├── SURVIVAL_TESTS.md
├── psilocybin.design.yaml
├── docs/
│   ├── genome.md
│   ├── organism.md
│   ├── ontology.md
│   ├── stack-rationale.md
│   └── decision-memory.md
└── tests/
    └── survival/
        └── README.md
```

## Validation gates

The validator checks schema shape and semantic traceability:

- hidden verbs must trace to language evidence;
- relations must trace to verbs;
- invariants must trace to relations;
- genome must trace to invariants when present;
- survival conditions must be testable;
- death conditions must be explicit;
- stack rationale must trace to genome and survival;
- implementation phases must trace to design objects.

Warnings can be bypassed during render/pack with `--allow-warnings`; hard
failures cannot be bypassed.

## Rights notice

All Rights Reserved. No reuse, copying, modification, distribution,
sublicensing, or derivative rights are granted except where separately
authorized by Khalid Saqr / KNOWDYN LTD or independently permitted by applicable
law.
