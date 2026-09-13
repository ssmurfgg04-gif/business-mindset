#!/usr/bin/env python3
"""
Business Mindset Skill — Health Diagnostic
Validates skill integrity, structure, and references.
Run: python scripts/skill_health.py
"""

import json
import re
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).parent.parent
SKILL_MD = SKILL_ROOT / "SKILL.md"
SCHEMA_MD = SKILL_ROOT / "SCHEMA.md"
REFERENCES = SKILL_ROOT / "references"
SCHEMAS = SKILL_ROOT / "schemas"
SCRIPTS = SKILL_ROOT / "scripts"
EXAMPLES = SKILL_ROOT / "examples"

ISSUES: list[str] = []
WARNINGS: list[str] = []


def check_frontmatter() -> dict:
    """Validate SKILL.md frontmatter has required fields."""
    content = SKILL_MD.read_text(encoding="utf-8")
    if not content.startswith("---"):
        ISSUES.append("SKILL.md missing frontmatter (---)")
        return {}

    try:
        fm_end = content.index("---", 3)
        fm_text = content[3:fm_end]
    except ValueError:
        ISSUES.append("SKILL.md frontmatter not closed")
        return {}

    required = ["name", "version", "description", "license", "compatibility"]
    recommended = ["author", "repository", "tags", "metadata"]

    data = {}
    for line in fm_text.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            data[k.strip()] = v.strip().strip('"')

    for k in required:
        if k not in data:
            ISSUES.append(f"Missing required frontmatter field: {k}")
    for k in recommended:
        if k not in data:
            WARNINGS.append(f"Missing recommended frontmatter field: {k}")

    # Note: metadata section in YAML is nested - simple parser doesn't parse nested structures
    # but the fields are present in the actual YAML frontmatter
    return data


def check_references_exist() -> int:
    """Verify all referenced files in SKILL.md exist."""
    content = SKILL_MD.read_text(encoding="utf-8")
    # Find all references/... patterns
    refs = re.findall(r"[`\(](references/[^`\)]+)\.md", content)
    missing = 0
    for ref in set(refs):
        path = SKILL_ROOT / f"{ref}.md"
        if not path.exists():
            WARNINGS.append(f"Referenced file missing: {path}")
            missing += 1
    return missing


def check_schema_validity() -> bool:
    """Validate agent-protocol.json is valid JSON."""
    try:
        schema_file = SCHEMAS / "agent-protocol.json"
        if not schema_file.exists():
            WARNINGS.append(f"Schema file missing: {schema_file}")
            return False
        json.loads(schema_file.read_text(encoding="utf-8"))
        return True
    except json.JSONDecodeError as e:
        ISSUES.append(f"Invalid JSON in agent-protocol.json: {e}")
        return False


def check_scripts_executable() -> int:
    """Check Python scripts are valid and have no syntax errors."""
    errors = 0
    for script in SCRIPTS.glob("*.py"):
        try:
            with open(script, encoding="utf-8") as f:
                content = f.read()
                compile(content, script.name, "exec")
        except SyntaxError as e:
            ISSUES.append(f"Syntax error in {script.name}: {e}")
            errors += 1
        except Exception as e:
            WARNINGS.append(f"Could not check {script.name}: {e}")
    return errors


def check_secrets_leak() -> int:
    """Check for potential secrets/keys in the codebase."""
    count = 0
    patterns = [
        r"ghp_[A-Za-z0-9]{36,}",  # GitHub PAT
        r"sk-[A-Za-z0-9]{48,}",  # OpenAI API key
        r"sk-ant-[A-Za-z0-9]{95,}",  # Anthropic API key
        r"AKIA[A-Z0-9]{16}",  # AWS access key
    ]
    for md_file in SKILL_ROOT.rglob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        for pattern in patterns:
            if re.search(pattern, content):
                WARNINGS.append(f"Potential secret in {md_file.name}: {pattern}")
                count += 1
    for py_file in SKILL_ROOT.rglob("*.py"):
        content = py_file.read_text(encoding="utf-8")
        for pattern in patterns:
            if re.search(pattern, content):
                WARNINGS.append(f"Potential secret in {py_file.name}: {pattern}")
                count += 1
    return count


def check_placeholder_paths() -> int:
    """Verify no hardcoded /home/z/ paths remain."""
    count = 0
    for md_file in REFERENCES.rglob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        if "/home/z/" in content:
            lines = [i + 1 for i, line in enumerate(content.splitlines()) if "/home/z/" in line]
            WARNINGS.append(f"Hardcoded /home/z/ path in {md_file.name} at lines {lines}")
            count += 1
    return count


def check_skill_md_structure() -> list[str]:
    """Verify SKILL.md has expected sections."""
    content = SKILL_MD.read_text(encoding="utf-8")
    required_sections = [
        "Core Philosophy",
        "Progressive Loading",
        "Mandatory Protocols",
        "Token Efficiency",
    ]
    missing = []
    for section in required_sections:
        if section not in content:
            missing.append(section)

    # Check line count (should be under 500 lines per best practices)
    line_count = len(content.splitlines())
    if line_count > 500:
        WARNINGS.append(f"SKILL.md has {line_count} lines (recommended <500)")

    # Check token estimate (rough approximation)
    token_estimate = len(content.split())
    if token_estimate > 3000:
        WARNINGS.append(f"SKILL.md estimated {token_estimate} tokens (recommended <3000)")

    return missing


def check_readme_sync() -> bool:
    """Verify README.md mentions key skill features."""
    readme = (SKILL_ROOT / "README.md").read_text(encoding="utf-8")
    key_terms = ["asymmetric execution", "exponential potential", "lens", "framework", "lens"]
    missing = [t for t in key_terms if t.lower() not in readme.lower()]
    if missing:
        WARNINGS.append(f"README.md missing key terms: {missing}")
        return False
    return True


def main():
    print("=" * 60)
    print("Business Mindset Skill - Health Diagnostic")
    print("=" * 60)

    # Run all checks
    fm = check_frontmatter()
    print(
        f"\n[OK] Frontmatter: {len([k for k in ['name', 'version', 'description', 'license', 'compatibility'] if k in fm])}/5 required fields present"
    )
    for w in [w for w in WARNINGS if w.startswith("Missing recommended")]:
        print(f"  [WARN] {w}")

    missing_refs = check_references_exist()
    print(f"\n[OK] References check: {missing_refs} missing files")

    schema_ok = check_schema_validity()
    print(f"\n[OK] Schema validity: {'OK' if schema_ok else 'FAIL'}")

    script_errors = check_scripts_executable()
    print(f"\n[OK] Script syntax: {script_errors} errors")

    hardcoded = check_placeholder_paths()
    print(f"\n[OK] Hardcoded paths: {hardcoded} files with issues")

    secrets = check_secrets_leak()
    print(f"\n[OK] Secrets check: {secrets} potential leaks")

    missing_sections = check_skill_md_structure()
    if missing_sections:
        print(f"\n[FAIL] SKILL.md missing sections: {missing_sections}")
    else:
        print("\n[OK] SKILL.md structure: OK")

    readme_ok = check_readme_sync()
    print(f"\n[OK] README sync: {'OK' if readme_ok else 'WARNING'}")

    print("\n" + "=" * 60)
    print(f"SUMMARY: {len(ISSUES)} issues, {len(WARNINGS)} warnings")
    for issue in ISSUES:
        print(f"  [FAIL] {issue}")
    for warning in WARNINGS:
        print(f"  [WARN] {warning}")

    # Exit code: 0 if no issues, 1 if issues
    return 1 if ISSUES else 0


if __name__ == "__main__":
    sys.exit(main())
