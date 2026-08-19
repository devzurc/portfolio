#!/usr/bin/env python3
"""Generate Cursor and Codex specialist adapters from .agents/specialists/."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE_DIR = ROOT / ".agents" / "specialists"
CURSOR_DIR = ROOT / ".cursor" / "agents"
CODEX_DIR = ROOT / ".codex" / "agents"
REQUIRED = ("name", "description", "reasoning_effort", "readonly")


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str]:
    content = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n?(.*)\Z", content, re.DOTALL)
    if not match:
        raise ValueError(f"{path}: missing YAML frontmatter")
    metadata: dict[str, str] = {}
    for line in match.group(1).splitlines():
        key, separator, value = line.partition(":")
        if not separator:
            raise ValueError(f"{path}: invalid frontmatter line: {line}")
        metadata[key.strip()] = value.strip()
    missing = [key for key in REQUIRED if key not in metadata]
    if missing:
        raise ValueError(f"{path}: missing {', '.join(missing)}")
    if metadata["name"] != path.stem:
        raise ValueError(f"{path}: name must match filename")
    if metadata["readonly"] not in {"true", "false"}:
        raise ValueError(f"{path}: readonly must be true or false")
    return metadata, match.group(2).strip()


def toml_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def cursor_adapter(source: str) -> str:
    return source.rstrip() + "\n\n<!-- Generated from .agents/specialists; do not edit. Run .agents/scripts/sync-specialist-adapters.py. -->\n"


def codex_adapter(metadata: dict[str, str], body: str) -> str:
    sandbox = "read-only" if metadata["readonly"] == "true" else "workspace-write"
    instructions = (
        "This adapter is generated from .agents/specialists/; do not edit it directly. "
        "Run .agents/scripts/sync-specialist-adapters.py after changing the canonical definition.\n\n"
        + body
    ).replace('"""', '\\\"\\\"\\\"')
    return (
        f"name = {toml_quote(metadata['name'])}\n"
        f"description = {toml_quote(metadata['description'])}\n"
        f"model_reasoning_effort = {toml_quote(metadata['reasoning_effort'])}\n"
        f"sandbox_mode = {toml_quote(sandbox)}\n\n"
        f"developer_instructions = \"\"\"\n{instructions}\n\"\"\"\n"
    )


def expected() -> dict[Path, str]:
    results: dict[Path, str] = {}
    for source in sorted(SOURCE_DIR.glob("*.md")):
        metadata, body = parse_frontmatter(source)
        raw = source.read_text(encoding="utf-8")
        results[CURSOR_DIR / source.name] = cursor_adapter(raw)
        results[CODEX_DIR / f"{metadata['name']}.toml"] = codex_adapter(metadata, body)
    if not results:
        raise ValueError(f"No canonical specialists found in {SOURCE_DIR}")
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if adapters differ from canonical output")
    args = parser.parse_args()
    try:
        adapters = expected()
    except ValueError as error:
        print(error, file=sys.stderr)
        return 2
    drift = []
    for path, content in adapters.items():
        if not path.is_file() or path.read_text(encoding="utf-8") != content:
            drift.append(path.relative_to(ROOT))
            if not args.check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")
    if args.check:
        if drift:
            print("Specialist adapter drift:\n" + "\n".join(f"- {path}" for path in drift), file=sys.stderr)
            return 1
        print(f"Specialist adapters are current ({len(adapters) // 2} specialists).")
        return 0
    print(f"Wrote {len(drift)} adapter file(s) for {len(adapters) // 2} specialists.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
