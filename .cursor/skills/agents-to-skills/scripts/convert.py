#!/usr/bin/env python3
"""Convert .agents/ skills and prompts to .cursor/skills/ SKILL.md files."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
AGENTS = ROOT / ".agents"
DEST = ROOT / ".cursor" / "skills"

DESCRIPTIONS: dict[str, str] = {
    "career-knowledge": (
        "Curates GitHub projects and syncs career data for portfolio and CV alignment. "
        "Use when curating GitHub projects, syncing career data, or preparing portfolio/CV alignment from work evidence."
    ),
    "continuous-career-sync": (
        "Watches GitHub signals and keeps career knowledge, CV drafts, cover letter, and portfolio aligned. "
        "Use when running continuous career sync, GitHub-to-career propagation, or proactive career workspace updates."
    ),
    "portfolio-review": (
        "Runs holistic hiring-manager and recruiter review of the portfolio site. "
        "Use for /review-portfolio, full-site hiring impact review, or recruiter lens assessment."
    ),
    "frontend-maintenance": (
        "Fixes layout, styles, navigation, and structural HTML in the static portfolio. "
        "Use when fixing layout bugs, responsive issues, animations, or making small structural HTML changes."
    ),
    "seo-accessibility": (
        "Audits and improves SEO metadata and web accessibility. "
        "Use for /seo-check, /a11y-pass, or when editing metadata, headings, links, and semantic structure."
    ),
    "copywriting-linkedin": (
        "Improves portfolio copy and LinkedIn-aligned messaging. "
        "Use when improving hero copy, experience bullets, project descriptions, or syncing tone with LinkedIn."
    ),
    "cv-management": (
        "Manages CV content, exports, and portfolio sync for Lucas Cruz's CV. "
        "Use when adding, editing, or removing CV content, exporting PDFs, or syncing CV facts to the portfolio."
    ),
    "prompt-start-audit-sync": (
        "Starts a full portfolio, CV, career, and job-fit alignment audit session. "
        "Use for /start-audit-sync or when beginning a comprehensive repo and career audit."
    ),
    "prompt-continuous-career-sync": (
        "Invokes a continuous career sync pass across GitHub, CV, cover letter, and portfolio. "
        "Use for /continuous-career-sync or when the user wants a GitHub-to-career sync run."
    ),
    "prompt-improve-section": (
        "Improves copy and structure for one portfolio section with EN/PT parity. "
        "Use for /improve-section or targeted section copy improvements."
    ),
    "prompt-review-before-commit": (
        "Reviews git diff before commit for factual integrity, bilingual parity, and regressions. "
        "Use for /pre-commit-review or before committing portfolio changes."
    ),
    "prompt-update-cv": (
        "Handles CV add, edit, or remove operations with Google Docs workflow. "
        "Use for CV update requests, new roles, bullets, skills, or CV-portfolio sync audits."
    ),
    "prompt-add-project": (
        "Adds a new project card to the portfolio #projects section. "
        "Use when adding a new portfolio project with EN/PT copy and stack tags."
    ),
}


def infer_description(name: str, body: str) -> str:
    if name in DESCRIPTIONS:
        return DESCRIPTIONS[name]
    for line in body.splitlines():
        line = line.strip()
        if line.lower().startswith("use when") or line.lower().startswith("use this skill"):
            text = re.sub(r"^use (when|this skill (for|when))\s*", "", line, flags=re.I)
            return f"Handles agent workflow tasks. Use when {text.rstrip('.')}."
    return f"Agent workflow from .agents/. Use when working on {name.replace('-', ' ')} tasks."


def write_skill(name: str, body: str, *, disable_invocation: bool = False) -> Path:
    desc = infer_description(name, body)
    lines = [
        "---",
        f"name: {name}",
        f"description: {desc}",
    ]
    if disable_invocation:
        lines.append("disable-model-invocation: true")
    lines.extend(["---", "", body.rstrip(), ""])
    out = DEST / name / "SKILL.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


def main() -> None:
    created: list[str] = []
    for path in sorted((AGENTS / "skills").glob("*.md")):
        name = path.stem
        out = write_skill(name, path.read_text(encoding="utf-8"))
        created.append(f"{path.relative_to(ROOT)} → {out.relative_to(ROOT)}")

    for path in sorted((AGENTS / "prompts").glob("*.md")):
        name = f"prompt-{path.stem}"
        out = write_skill(
            name,
            path.read_text(encoding="utf-8"),
            disable_invocation=True,
        )
        created.append(f"{path.relative_to(ROOT)} → {out.relative_to(ROOT)}")

    print(f"Converted {len(created)} files:\n")
    for line in created:
        print(f"  {line}")


if __name__ == "__main__":
    main()
