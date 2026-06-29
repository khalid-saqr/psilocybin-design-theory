#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p paper/build
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=paper/build paper/Psilocybin_Design_Theory_Complete.tex
cp paper/build/Psilocybin_Design_Theory_Complete.pdf paper/Psilocybin_Design_Theory_Complete.pdf
cp paper/build/Psilocybin_Design_Theory_Complete.pdf docs/psilocybin-design-theory.pdf
pandoc paper/Psilocybin_Design_Theory_Complete.tex --from=latex --to=html5 --standalone --mathjax --metadata title="Psilocybin Design:  Bio-inspired theory and CLI package for designing computer software as digital organisms" -o docs/paper.html.tmp
python tools/patch_paper_html.py
rm docs/paper.html.tmp
