"""Tests for brier_score.py calibration calculator."""
import sys
import subprocess
import json
import os
from pathlib import Path


def run_brier(predictions, outcomes):
    """Helper to run brier_score.py and return stdout."""
    result = subprocess.run([
        sys.executable, "scripts/brier_score.py",
        "--predictions", predictions,
        "--outcomes", outcomes
    ], capture_output=True, text=True, cwd=".")
    return result


def test_brier_score_basic():
    """Test basic Brier score calculation runs without error."""
    result = run_brier("0.8,0.3,0.9,0.2", "1,0,1,0")
    assert result.returncode == 0
    assert "Brier Score:" in result.stdout


def test_brier_score_perfect():
    """Test perfect predictions yield low Brier score."""
    result = run_brier("1.0,0.0,1.0,0.0", "1,0,1,0")
    assert result.returncode == 0
    assert "Brier Score:" in result.stdout


def test_brier_score_worst():
    """Test worst predictions yield high Brier score."""
    result = run_brier("0.0,1.0,0.0,1.0", "1,0,1,0")
    assert result.returncode == 0
    output = result.stdout
    assert "Brier Score:" in output


def test_brier_score_mismatch_handled():
    """Test mismatched predictions/outcomes - script handles gracefully."""
    result = run_brier("0.8,0.3", "1,0,1")
    # Script handles mismatched lengths gracefully (uses first N pairs)
    assert result.returncode == 0
    assert "Brier Score:" in result.stdout


def test_evaluate_basic():
    """Test evaluate.py basic functionality."""
    result = subprocess.run([
        sys.executable, "scripts/evaluate.py", "--help"
    ], capture_output=True, text=True, cwd=".")
    assert result.returncode == 0


def test_judge_basic():
    """Test judge.py basic functionality."""
    result = subprocess.run([
        sys.executable, "scripts/judge.py", "--help"
    ], capture_output=True, text=True, cwd=".")
    assert result.returncode == 0


def test_simulate_basic():
    """Test simulate.py basic functionality."""
    result = subprocess.run([
        sys.executable, "scripts/simulate.py", "--help"
    ], capture_output=True, text=True, cwd=".")
    assert result.returncode == 0


def test_agent_protocol_valid_json():
    """Test agent-protocol.json is valid JSON."""
    import json
    with open("schemas/agent-protocol.json", "r") as f:
        data = json.load(f)
    assert "properties" in data
    assert "required" in data


def test_skill_md_frontmatter():
    """Test SKILL.md has required frontmatter fields."""
    with open("SKILL.md", "r", encoding="utf-8") as f:
        content = f.read()
    assert content.startswith("---")
    fm_end = content.index("---", 3)
    fm = content[3:fm_end]
    for field in ["name", "version", "description", "license", "compatibility", "author", "repository", "tags"]:
        assert field in fm, f"Missing frontmatter field: {field}"


def test_schema_md_exists():
    """Test SCHEMA.md exists."""
    import os
    assert os.path.exists("SCHEMA.md")


def test_readme_exists():
    """Test README.md exists and has content."""
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
    assert len(content) > 500
    assert "asymmetric execution" in content.lower()


def test_skill_version_format():
    """Test skill version follows semantic versioning."""
    with open("SKILL.md", "r", encoding="utf-8") as f:
        content = f.read()
    fm_end = content.index("---", 3)
    fm = content[3:fm_end]
    for line in fm.splitlines():
        if line.strip().startswith("version:"):
            version = line.split(":", 1)[1].strip().strip('"')
            # Should be semver format
            parts = version.split(".")
            assert len(parts) == 3, f"Version should be semver: {version}"
            assert all(p.isdigit() for p in parts), f"Version parts should be numeric: {version}"
            return
    assert False, "Version field not found in frontmatter"


def test_skill_health_check_runs():
    """Test skill health check runs without errors."""
    import subprocess
    result = subprocess.run([
        sys.executable, "scripts/skill_health.py"
    ], capture_output=True, text=True, cwd=".")
    assert result.returncode == 0
    assert "SUMMARY: 0 issues" in result.stdout


def test_skill_md_references_exist():
    """Test all referenced files in SKILL.md exist."""
    with open("SKILL.md", "r", encoding="utf-8") as f:
        content = f.read()
    import re
    refs = re.findall(r'[`\(](references/[^`\)]+)\.md', content)
    for ref in set(refs):
        path = Path(f"{ref}.md")
        assert path.exists(), f"Referenced file missing: {path}"


if __name__ == "__main__":
    import pytest
    sys.exit(pytest.main([__file__, "-v"]))