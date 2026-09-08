from pathlib import Path
root = Path(__file__).resolve().parents[1]
for name in ["README.md", "LICENSE", "AGENTS.md", "CONTRIBUTING.md", "SECURITY.md", "GOVERNANCE.md", "CODE_OF_CONDUCT.md", "docs/product-research.md"]:
    assert (root / name).is_file(), f"Missing {name}"
assert "Apache License" in (root / "LICENSE").read_text()
print("Planning artifacts validated; application functionality is not yet implemented.")
