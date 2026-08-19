#!/usr/bin/env python3
"""Validate portable skills, canonical specialist definitions, and instruction size."""

from __future__ import annotations

import re
import subprocess
import sys
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SKILLS = ROOT / ".agents" / "skills"
SPECIALISTS = ROOT / ".agents" / "specialists"
NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def frontmatter(path: Path) -> dict[str, str]:
    raw = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", raw, re.DOTALL)
    if not match:
        raise ValueError("missing YAML frontmatter")
    result = {}
    for line in match.group(1).splitlines():
        key, separator, value = line.partition(":")
        if separator:
            result[key.strip()] = value.strip()
    return result


def main() -> int:
    errors: list[str] = []
    for directory in sorted(path for path in SKILLS.iterdir() if path.is_dir()):
        skill = directory / "SKILL.md"
        if not skill.is_file():
            errors.append(f"{directory.relative_to(ROOT)}: missing SKILL.md")
            continue
        try:
            metadata = frontmatter(skill)
        except ValueError as error:
            errors.append(f"{skill.relative_to(ROOT)}: {error}")
            continue
        if metadata.get("name") != directory.name or not NAME.fullmatch(directory.name):
            errors.append(f"{skill.relative_to(ROOT)}: name must match a kebab-case folder name")
        if not metadata.get("description"):
            errors.append(f"{skill.relative_to(ROOT)}: missing description")
    for path in sorted(SPECIALISTS.glob("*.md")):
        try:
            metadata = frontmatter(path)
        except ValueError as error:
            errors.append(f"{path.relative_to(ROOT)}: {error}")
            continue
        for key in ("name", "description", "reasoning_effort", "readonly"):
            if not metadata.get(key):
                errors.append(f"{path.relative_to(ROOT)}: missing {key}")
        if metadata.get("name") != path.stem:
            errors.append(f"{path.relative_to(ROOT)}: name must match filename")
    for path in sorted((ROOT / ".codex" / "agents").glob("*.toml")):
        try:
            tomllib.loads(path.read_text(encoding="utf-8"))
        except tomllib.TOMLDecodeError as error:
            errors.append(f"{path.relative_to(ROOT)}: invalid TOML ({error})")
    agents = ROOT / "AGENTS.md"
    if agents.stat().st_size >= 32768:
        errors.append("AGENTS.md exceeds Codex's default 32 KiB instruction limit")
    stale = re.compile(r"\.cursor/skills/|\.agents/skills/[\w-]+\.md|\.agents/prompts/")
    for path in [ROOT / "AGENTS.md", ROOT / ".agents" / "commands.md", ROOT / ".agents" / "project-context.md"]:
        if path.is_file() and stale.search(path.read_text(encoding="utf-8")):
            errors.append(f"{path.relative_to(ROOT)}: stale skill or prompt path")
    check = subprocess.run([sys.executable, str(ROOT / ".agents/scripts/sync-specialist-adapters.py"), "--check"], cwd=ROOT)
    if check.returncode:
        errors.append("generated specialist adapters are stale or invalid")
    if errors:
        print("Agent-system validation failed:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    print("Agent-system validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
