from __future__ import annotations

import zipfile
from pathlib import Path

from psilocybin_design_cli.core.render import project_slug, render_genesis_repo, verify_required_files


def zip_dir(source_dir: Path, zip_path: Path) -> Path:
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(source_dir.rglob("*")):
            if path.is_file():
                zf.write(path, path.relative_to(source_dir.parent))
    return zip_path


def pack_genesis_repo(
    design: dict,
    outputs_dir: Path,
    *,
    output_zip: Path | None = None,
    allow_warnings: bool = False,
) -> tuple[Path, Path]:
    slug = project_slug(design)
    repo_dir = outputs_dir / f"{slug}-genesis"
    render_genesis_repo(design, repo_dir, allow_warnings=allow_warnings)
    verify_required_files(repo_dir)
    zip_path = output_zip or outputs_dir / f"{slug}-genesis.zip"
    zip_dir(repo_dir, zip_path)
    return repo_dir, zip_path
