 # Psilocybin Design Theory
+
+<p align="left">
+  <a href="#technical-report-metadata"><img alt="Version" src="https://img.shields.io/badge/version-1.0.1-111111?style=flat-square"></a>
+  <a href="#technical-report-metadata"><img alt="Technical Report" src="https://img.shields.io/badge/technical%20report-MD--TR--2026--001-111111?style=flat-square"></a>
+  <a href="#rights-and-license"><img alt="Rights" src="https://img.shields.io/badge/rights-all%20rights%20reserved-7a1f1f?style=flat-square"></a>
+  <a href="#citation-and-indexing"><img alt="Citation Metadata" src="https://img.shields.io/badge/citation-metadata%20included-2f4f4f?style=flat-square"></a>
+</p>
+
+<p align="left">
+  <a href="#install-the-cli"><img alt="CLI" src="https://img.shields.io/badge/CLI-psilocybin-1f2937?style=flat-square&logo=python&logoColor=white"></a>
+  <a href="packages/psilocybin-design-cli/"><img alt="Python Package" src="https://img.shields.io/badge/package-Python%20CLI-2563eb?style=flat-square&logo=python&logoColor=white"></a>
+  <a href="#configure-an-optional-local-llm"><img alt="Local LLM Ready" src="https://img.shields.io/badge/local%20LLM-optional-4b5563?style=flat-square"></a>
+  <a href="#coding-agent-handoff"><img alt="Agent Handoff" src="https://img.shields.io/badge/agent%20handoff-Codex%20%7C%20Claude%20Code%20%7C%20Copilot-374151?style=flat-square"></a>
+</p>
+
+<p align="left">
+  <a href="https://khalid-saqr.github.io/psilocybin-design-theory/"><img alt="GitHub Pages" src="https://img.shields.io/badge/docs-GitHub%20Pages-111827?style=flat-square&logo=githubpages&logoColor=white"></a>
+  <a href="https://khalid-saqr.github.io/psilocybin-design-theory/psilocybin-design-theory.pdf"><img alt="PDF Paper" src="https://img.shields.io/badge/paper-PDF-b91c1c?style=flat-square&logo=adobeacrobatreader&logoColor=white"></a>
+  <a href="https://colab.research.google.com/github/khalid-saqr/psilocybin-design-theory/blob/main/notebooks/Psilocybin_Genesis_CLI_v1_Colab_Tutorial.ipynb"><img alt="Open CLI Tutorial in Colab" src="https://img.shields.io/badge/Colab-CLI%20tutorial-f9ab00?style=flat-square&logo=googlecolab&logoColor=black"></a>
+  <a href="https://colab.research.google.com/github/khalid-saqr/psilocybin-design-theory/blob/main/notebooks/Psilocybin_Genesis_CLI_DeepSeek_Interview_Tutorial.ipynb"><img alt="Open DeepSeek Tutorial in Colab" src="https://img.shields.io/badge/Colab-DeepSeek%20interview-f9ab00?style=flat-square&logo=googlecolab&logoColor=black"></a>
+</p>
+
+<p align="left">
+  <a href="https://orcid.org/0000-0002-3058-2705"><img alt="ORCID" src="https://img.shields.io/badge/ORCID-0000--0002--3058--2705-a6ce39?style=flat-square&logo=orcid&logoColor=white"></a>
+  <a href="mailto:ipcontrol@knowdyn.co.uk"><img alt="Rights Contact" src="https://img.shields.io/badge/rights%20contact-ipcontrol%40knowdyn.co.uk-334155?style=flat-square"></a>
+</p>
+
+<p align="left">
+  <strong>🧬 Genome-first software design</strong> ·
+  <strong>🧠 language-game analysis</strong> ·
+  <strong>🧾 traceable genesis repositories</strong> ·
+  <strong>🤖 coding-agent handoff</strong>
+</p>
 
 ## Design a computer software as a digital organism. Build the genome, ontology, and survival conditions of your new software before asking an agent to code it.

**Psilocybin Design Theory** is a theory-method and practical CLI workflow for turning an concept-level software intention into an agent-readable **genesis repository**.

A genesis repository is not the final application. It is a design-constrained seed repository that tells coding agents what to build, why it exists, how its parts trace to the design identity, and what conditions define success or failure.

```text
Gap → Language-game → Hidden Verbs → Relations → Invariants
→ Genome → Organism → Ontology → Survival/Death Conditions
→ Stack → Genesis Repository
```

---

## Try it in 3 minutes

```bash
git clone https://github.com/khalid-saqr/psilocybin-design-theory.git
cd psilocybin-design-theory/packages/psilocybin-design-cli
python -m pip install -e .

psilocybin --help
```

Create a design workspace:

```bash
psilocybin init demo
cd demo.design
psilocybin interview
```

Validate, render, and pack a genesis repository:

```bash
psilocybin validate
psilocybin render
psilocybin pack
```

The output is a generated repository seed for Codex, GitHub Copilot, Claude Code, or another coding agent.

---

## Open the tutorials

### DeepSeek-R1 Distilled Interview Tutorial

Runs the CLI from GitHub, installs Ollama, pulls a DeepSeek-R1 distilled model, runs interview mode, performs real LLM-assisted suggestions, validates, renders, packs, and downloads a genesis repository.

[Open in Colab](https://colab.research.google.com/github/khalid-saqr/psilocybin-design-theory/blob/main/notebooks/Psilocybin_Genesis_CLI_DeepSeek_Interview_Tutorial.ipynb)

### Psilocybin Genesis CLI Colab Tutorial

Runs the CLI in Google Colab, configures a local model runtime, performs real `suggest` / `accept` stages, validates the design memory, and generates a downloadable genesis repository.

[Open in Colab](https://colab.research.google.com/github/khalid-saqr/psilocybin-design-theory/blob/main/notebooks/Psilocybin_Genesis_CLI_v1_Colab_Tutorial.ipynb)

---

## What this project does

This repository contains:

- the formal Psilocybin Design Theory paper;
- citation and indexing metadata;
- a GitHub Pages documentation site;
- the **Psilocybin Genesis CLI** package;
- Google Colab tutorial notebooks;
- coding-agent handoff workflows;
- rights, citation, and publication files.

The practical purpose is to help a user move from:

```text
“I have an idea for software.”
```

to:

```text
“I have a design-constrained genesis repository that a coding agent can implement.”
```

---

## What this project does not do

This project is not:

- a claim that software is biologically alive;
- a generic prompt-to-app generator;
- a static boilerplate generator;
- a replacement for human design authority;
- an autonomous coding agent;
- an open-source repository unless licensing terms change explicitly;
- a public-domain or Creative Commons release.

The organismic language in Psilocybin Design is a disciplined design model. It is only useful when it constrains architecture, ontology, tests, survival conditions, implementation sequence, and agent instructions.

---

## Why this differs from ordinary AI coding workflows

| Approach                   | Starts from           | Produces                          | Main limitation                               |
| -------------------------- | --------------------- | --------------------------------- | --------------------------------------------- |
| Code autocomplete          | Current file context  | Suggestions                       | No full design traceability                   |
| Chat-based coding          | User prompt           | Code fragments or app drafts      | Design rationale remains implicit             |
| Scaffold generators        | Template choice       | Boilerplate                       | Stack is chosen before identity               |
| Prompt-to-app tools        | Product description   | Generated application             | Weak survival/death criteria                  |
| Architecture documents     | Human-written plans   | Documentation                     | Often disconnected from agent execution       |
| **Psilocybin Genesis CLI** | Gap and language-game | Agent-readable genesis repository | Requires structured design work before coding |

Psilocybin Design’s differentiator is **traceability from intention to implementation**.

Every major implementation decision should trace back to at least one of:

```text
gap
language-game
hidden verb
relation
invariant
genome
organism
ontology
survival condition
death condition
```

---

## Before and after

Input:

```text
A tool for research teams to remember why decisions were made across papers,
experiments, meetings, and code changes.
```

Output:

```text
research-memory-genesis/
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── DESIGN.md
├── IMPLEMENTATION_SEQUENCE.md
├── SURVIVAL_TESTS.md
├── psilocybin.design.yaml
├── .github/
│   └── copilot-instructions.md
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

---

## Install the CLI

From the repository root:

```bash
cd packages/psilocybin-design-cli
python -m pip install -e .
psilocybin --help
```

The CLI command is:

```bash
psilocybin
```

The package is local-first. It can run deterministic commands without an LLM, and it can use a configured local or OpenAI-compatible LLM provider for suggestion stages.

---

## Configure an optional local LLM

Example using Ollama:

```bash
ollama pull deepseek-r1:1.5b

psilocybin config set llm.enabled true
psilocybin config set llm.provider ollama
psilocybin config set llm.model deepseek-r1:1.5b
psilocybin config set llm.base_url http://127.0.0.1:11434

psilocybin doctor
```

The LLM is not the design authority.

The LLM may suggest hidden verbs, relations, invariants, genome wording, organism model, ontology, survival/death conditions, stack rationale, implementation sequence, and agent instructions.

The user accepts, edits, or rejects suggestions. The validator checks the design memory before rendering.

---

## Core workflow

```bash
psilocybin init my-project
cd my-project.design

psilocybin interview

psilocybin suggest verbs
psilocybin accept verbs --all

psilocybin suggest relations
psilocybin accept relations --all

psilocybin suggest invariants
psilocybin accept invariants --all

psilocybin suggest genome
psilocybin accept genome --all

psilocybin validate
psilocybin render
psilocybin pack
```

The generated `.zip` can be extracted into a new repository and given to a coding agent.

---

## Command reference

| Command                      | Purpose                                           |
| ---------------------------- | ------------------------------------------------- |
| `psilocybin init <name>`     | Create a design workspace                         |
| `psilocybin interview`       | Collect design inputs                             |
| `psilocybin suggest <stage>` | Ask the configured LLM for suggestions            |
| `psilocybin accept <stage>`  | Merge accepted suggestions into the design memory |
| `psilocybin validate`        | Check schema and traceability                     |
| `psilocybin render`          | Render the genesis repository files               |
| `psilocybin pack`            | Package the generated genesis repository as a zip |
| `psilocybin config`          | Read or update workspace configuration            |
| `psilocybin doctor`          | Check package, workspace, and LLM runtime status  |

Common stages include:

```text
verbs
relations
invariants
genome
organism
ontology
survival
death
stack
sequence
agents
```

---

## What the CLI generates

The most important generated file is:

```text
psilocybin.design.yaml
```

It is the design memory of the project.

It records:

```text
project
gap
language_game
hidden_verbs
relations
invariants
genome
organism
ontology
survival_conditions
death_conditions
stack
implementation_sequence
agent_contract
```

The rendered genesis repository contains human-readable and agent-readable files:

```text
README.md
AGENTS.md
CLAUDE.md
.github/copilot-instructions.md
DESIGN.md
IMPLEMENTATION_SEQUENCE.md
SURVIVAL_TESTS.md
docs/genome.md
docs/organism.md
docs/ontology.md
docs/stack-rationale.md
docs/decision-memory.md
```

---

## Coding-agent handoff

The generated repository is designed to guide coding agents.

Supported instruction targets include:

- Codex-style agents through `AGENTS.md`;
- Claude Code through `CLAUDE.md`;
- GitHub Copilot through `.github/copilot-instructions.md`.

The generated agent instructions tell agents to begin from:

```text
psilocybin.design.yaml
IMPLEMENTATION_SEQUENCE.md
SURVIVAL_TESTS.md
```

Expected implementation rule:

```text
No untraced component.
No untraced abstraction.
No stack decision without genome or survival-condition rationale.
```

---

## Theory in one paragraph

Psilocybin Design derives software from a gap rather than from a framework default. It moves through the language around the gap, the hidden verbs implied by that language, the relations required by those verbs, the invariants that must survive change, and the genome that compresses the system’s identity. From that genome it derives an organism model, ontology, survival/death conditions, stack rationale, and implementation sequence. The stack is the executable body of an identity already discovered.

---

## Theory vocabulary

| Term               | Meaning                                                                                           |
| ------------------ | ------------------------------------------------------------------------------------------------- |
| Gap                | A failed or insufficient relation between intention and possibility                               |
| Language-game      | The situated vocabulary, roles, workarounds, judgments, and tensions around the gap               |
| Hidden verb        | An implied action such as remember, verify, route, reconcile, protect, expose, repair, or decay   |
| Relation           | A dependency, authority, trace, transfer, memory, boundary, transformation, or constraint         |
| Invariant          | A condition that must remain true across changes                                                  |
| Genome             | The compressed identity of the software                                                           |
| Organism           | A disciplined model of boundary, function, repair, exposure, decay, and survival                  |
| Ontology           | Entities, states, relations, boundaries, and transformations recognized by the system             |
| Survival condition | A testable condition under which the software still bridges the original gap                      |
| Death condition    | A failure mode where the software may run but no longer preserves its design identity             |
| Stack              | The executable body: language, storage, services, interface, deployment, tests, and observability |

---

## Repository structure

```text
.
├── CITATION.cff
├── LICENSE
├── NOTICE.md
├── RIGHTS.md
├── README.md
├── codemeta.json
├── docs/
│   ├── cli.html
│   ├── index.html
│   ├── paper.html
│   ├── publications.html
│   ├── psilocybin-design-theory.pdf
│   ├── robots.txt
│   ├── sitemap.xml
│   ├── style.css
│   └── metadata/
├── notebooks/
│   ├── Psilocybin_Genesis_CLI_v1_Colab_Tutorial.ipynb
│   └── Psilocybin_Genesis_CLI_DeepSeek_Interview_Tutorial.ipynb
├── packages/
│   └── psilocybin-design-cli/
│       ├── pyproject.toml
│       ├── README.md
│       ├── src/
│       └── tests/
├── paper/
│   ├── Psilocybin_Design_Theory_Complete.tex
│   ├── Psilocybin_Design_Theory_Complete.original.tex
│   ├── Psilocybin_Design_Theory_Complete.pdf
│   └── references.bib
└── .github/
    └── workflows/
        └── pages.yml
```

---

## Public site

Expected GitHub Pages URL after deployment:

```text
https://khalid-saqr.github.io/psilocybin-design-theory/
```

Expected pages:

```text
https://khalid-saqr.github.io/psilocybin-design-theory/
https://khalid-saqr.github.io/psilocybin-design-theory/paper.html
https://khalid-saqr.github.io/psilocybin-design-theory/cli.html
https://khalid-saqr.github.io/psilocybin-design-theory/publications.html
https://khalid-saqr.github.io/psilocybin-design-theory/psilocybin-design-theory.pdf
https://khalid-saqr.github.io/psilocybin-design-theory/sitemap.xml
```

---

## Citation and indexing

This repository includes files and metadata intended to support scholarly discovery and citation indexing:

- `CITATION.cff`;
- CodeMeta JSON;
- BibTeX;
- RIS;
- EndNote;
- Schema.org JSON-LD;
- Google Scholar / Highwire-style citation metadata;
- Dublin Core fallback metadata;
- PRISM fallback metadata;
- crawlable GitHub Pages HTML;
- linked PDF;
- `robots.txt`;
- `sitemap.xml`.

Indexing by Google Scholar, Semantic Scholar, Crossref, OpenAlex, or any external aggregator cannot be guaranteed. The repository is structured to make discovery and parsing as straightforward as possible.

---

## Technical report metadata

```text
Title:             Psilocybin Design: Bio-inspired theory and CLI package for designing computer software as digital organisms
Author:            Khalid Saqr
ORCID:             https://orcid.org/0000-0002-3058-2705
Version:           1.0.1
Date:              29 June 2026
Technical report:  MD-TR-2026-001
Rights manager:    KNOWDYN LTD
Rights contact:    ipcontrol@knowdyn.co.uk
```

---

## Build the paper locally

```bash
cd paper
latexmk -pdf -interaction=nonstopmode Psilocybin_Design_Theory_Complete.tex
```

Copy the generated PDF to the documentation site:

```bash
cp paper/Psilocybin_Design_Theory_Complete.pdf docs/psilocybin-design-theory.pdf
```

---

## Deploy with GitHub Pages

1. Use the public GitHub repository:

   ```text
   khalid-saqr/psilocybin-design-theory
   ```

2. Push the repository contents to the default branch.

3. In GitHub, open:

   ```text
   Settings → Pages → Build and deployment
   ```

4. Set the source to:

   ```text
   GitHub Actions
   ```

5. The workflow at:

   ```text
   .github/workflows/pages.yml
   ```

   deploys the `docs/` directory.

6. Confirm that the public URLs resolve after deployment.

---

## Rights and license

All rights are reserved.

This repository is public for reading, citation, evaluation, and controlled demonstration. It is not currently licensed for reuse, redistribution, sublicensing, commercial use, public-domain use, or derivative works.

No open-source license, Creative Commons license, public-domain dedication, or reuse permission is granted by this repository unless explicitly stated in writing by the rights holder or rights manager.

The public visibility of this repository does not imply permission to copy, modify, redistribute, sublicense, train on, commercialize, or create derivative works from its contents.

See:

- LICENSE
- RIGHTS.md
- NOTICE.md

Rights manager:

```text
KNOWDYN LTD
ipcontrol@knowdyn.co.uk
```

---

## Roadmap

Planned development path:

```text
1. Formal theory publication repository
2. Psilocybin Genesis CLI package
3. Google Colab training notebooks
4. DeepSeek / local LLM tutorial workflow
5. Agent compatibility demonstrations
6. Case studies
7. Web-based Psilocybin Design environment
8. Community and industry validation
```

The roadmap is directional and may change as the theory, CLI, and user evidence develop.

---

## Author

**Khalid Saqr**\
ORCID: [https://orcid.org/0000-0002-3058-2705](https://orcid.org/0000-0002-3058-2705)

Rights managed by:

**KNOWDYN LTD**\
[ipcontrol@knowdyn.co.uk](mailto\:ipcontrol@knowdyn.co.uk)

---

## Citation

Use the repository citation metadata where possible:

```text
CITATION.cff
docs/metadata/citation.bib
docs/metadata/citation.ris
docs/metadata/citation.enw
codemeta.json
```

Suggested short citation:

```text
Saqr, K. Psilocybin Design Theory. Technical Report MD-TR-2026-001, version 1.0.1, 2026.
```

---

## Product thesis

Psilocybin Design is being developed from a theory-method into a practical software design environment.

Its purpose is to convert project ideas into operational design objects:

```text
gap
language of the gap
hidden verbs
relations
invariants
genome
organism
ontology
survival conditions
death conditions
stack rationale
decision memory
agent instructions
```

The practical output is a genesis repository that helps coding agents implement software from a traceable design identity rather than from unstructured prompting or generic scaffolding.
