# Psilocybin Design Theory

Publication repository for **Psilocybin Design: A Theory-Method for Deriving Software Organisms from Gaps**.

Author: **Khalid Saqr**  
ORCID: <https://orcid.org/0000-0002-3058-2705>  
Version: **1.0.0**  
Date: **29 June 2026**  
Technical report: **MD-TR-2026-001**  
Rights manager: **KNOWDYN LTD**  
Rights contact: <ipcontrol@knowdyn.co.uk>

## Public site

Expected GitHub Pages URL after deployment:

<https://khalid-saqr.github.io/psilocybin-design-theory/>

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
│   ├── index.html
│   ├── paper.html
│   ├── publications.html
│   ├── psilocybin-design-theory.pdf
│   ├── robots.txt
│   ├── sitemap.xml
│   ├── style.css
│   └── metadata/
│       ├── citation.bib
│       ├── citation.enw
│       ├── citation.ris
│       └── metadata.json
├── paper/
│   ├── Psilocybin_Design_Theory_Complete.tex
│   ├── Psilocybin_Design_Theory_Complete.original.tex
│   ├── Psilocybin_Design_Theory_Complete.pdf
│   └── references.bib
└── .github/workflows/pages.yml
```

## Rights

All rights are reserved. No open-source license, Creative Commons license, public-domain dedication, or reuse permission is granted by this repository. See [LICENSE](LICENSE), [RIGHTS.md](RIGHTS.md), and [NOTICE.md](NOTICE.md).

## Scholarly indexing preparation

The GitHub Pages site includes:

- Google Scholar / Highwire citation metadata.
- Dublin Core fallback metadata.
- PRISM fallback metadata.
- Schema.org JSON-LD metadata.
- A crawlable publication page.
- A searchable PDF linked by `citation_pdf_url`.
- `robots.txt` and `sitemap.xml`.
- BibTeX, RIS, EndNote, CITATION.cff, and CodeMeta files.

Indexing by Google Scholar or any external aggregator cannot be guaranteed; this repository is structured to make discovery and parsing as straightforward as possible.

## Deploy with GitHub Pages

1. Create a public GitHub repository named `psilocybin-design-theory` under the account `khalid-saqr`.
2. Upload or push these files to the default branch.
3. In GitHub: **Settings → Pages → Build and deployment → Source: GitHub Actions**.
4. The included workflow `.github/workflows/pages.yml` deploys the `docs/` directory.
5. After deployment, confirm that these URLs resolve:
   - `https://khalid-saqr.github.io/psilocybin-design-theory/`
   - `https://khalid-saqr.github.io/psilocybin-design-theory/psilocybin-design-theory.pdf`
   - `https://khalid-saqr.github.io/psilocybin-design-theory/paper.html`
   - `https://khalid-saqr.github.io/psilocybin-design-theory/publications.html`
   - `https://khalid-saqr.github.io/psilocybin-design-theory/sitemap.xml`

## Build locally

```bash
cd paper
latexmk -pdf -interaction=nonstopmode Psilocybin_Design_Theory_Complete.tex
```

Then copy the generated PDF to:

```bash
cp paper/Psilocybin_Design_Theory_Complete.pdf docs/psilocybin-design-theory.pdf
```

## Product thesis

Psilocybin Design is being developed from a theory-method into a software design web environment that converts project ideas into operational design objects: gap, language of the gap, genome, organism, ontology, survival conditions, stack rationale, and decision memory.
