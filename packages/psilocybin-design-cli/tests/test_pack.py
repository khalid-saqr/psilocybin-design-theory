from pathlib import Path
import zipfile
from psilocybin_design_cli.io import read_yaml
from psilocybin_design_cli.core.pack import pack_genesis_repo

FIX = Path(__file__).parent / "fixtures"


def test_pack_valid_design(tmp_path):
    repo, zip_path = pack_genesis_repo(read_yaml(FIX / "valid_design.yaml"), tmp_path)
    assert repo.exists()
    assert zip_path.exists()
    with zipfile.ZipFile(zip_path) as zf:
        names = set(zf.namelist())
    assert any(name.endswith("AGENTS.md") for name in names)
    assert any(name.endswith("psilocybin.design.yaml") for name in names)
