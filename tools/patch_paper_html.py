from pathlib import Path

head_inner = Path('docs/index.html').read_text(encoding='utf-8').split('<head>', 1)[1].split('</head>', 1)[0]
body = Path('docs/paper.html.tmp').read_text(encoding='utf-8')
body_content = body.split('<body>', 1)[1].split('</body>', 1)[0] if '<body>' in body else body
nav = '<nav><a href="./">Home</a> <a href="psilocybin-design-theory.pdf">PDF</a> <a href="metadata/citation.bib">BibTeX</a></nav>'
footer = '<footer><p class="small">Copyright © 2026 Khalid Saqr. All rights reserved. No license granted. Rights managed by KNOWDYN LTD, <a href="mailto:ipcontrol@knowdyn.co.uk">ipcontrol@knowdyn.co.uk</a>.</p></footer>'
html = f'''<!doctype html>
<html lang="en">
<head>
{head_inner}
</head>
<body>
{nav}
<main class="paper">
{body_content}
</main>
{footer}
</body>
</html>
'''
html = html.replace('rel="canonical" href="https://khalid-saqr.github.io/psilocybin-design-theory/"', 'rel="canonical" href="https://khalid-saqr.github.io/psilocybin-design-theory/paper.html"')
Path('docs/paper.html').write_text(html, encoding='utf-8')
