#!/usr/bin/env python3
"""Sync GitHub repo metadata and READMEs into docs/career/."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / ".sync-config.json"
READMES_DIR = ROOT / "readmes"
PROJECTS_DIR = ROOT / "projects"
INDEX_PATH = ROOT / "INDEX.md"
STACK_PATH = ROOT / "tech-stack-rollup.md"


def load_config() -> dict:
    defaults = {
        "github_user": "devzurc",
        "exclude_repos": ["My-Profile"],
        "include_private": False,
        "include_forks": False,
        "readme_max_chars": 12000,
    }
    if CONFIG_PATH.exists():
        defaults.update(json.loads(CONFIG_PATH.read_text(encoding="utf-8")))
    return defaults


def gh_json(args: list[str]):
    cmd = ["gh"] + args
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return json.loads(result.stdout)


def fetch_readme(full_name: str) -> str | None:
    try:
        data = gh_json(["api", f"repos/{full_name}/readme"])
        import base64

        raw = base64.b64decode(data["content"]).decode("utf-8", errors="replace")
        return raw.strip()
    except (subprocess.CalledProcessError, KeyError, json.JSONDecodeError):
        return None


def slugify(name: str) -> str:
    return re.sub(r"[^a-zA-Z0-9._-]+", "-", name).strip("-").lower()


def infer_stack(text: str, language: str | None) -> list[str]:
    hay = (text or "").lower()
    keywords = [
        "python", "sql", "airflow", "dbt", "snowflake", "docker", "aws", "azure", "gcp",
        "pandas", "pyspark", "spark", "delta lake", "trino", "postgresql", "n8n", "llm",
        "rag", "fastapi", "kubernetes", "power bi", "qlik", "superset", "parquet",
        "boto3", "terraform", "kafka", "redis", "mongodb", "flask", "django",
    ]
    found = [k for k in keywords if k in hay]
    if language and language.lower() not in found:
        found.insert(0, language.lower())
    # dedupe preserve order
    seen = set()
    out = []
    for item in found:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out


def ensure_project_stub(repo: dict, readme: str | None, today: str) -> None:
    name = repo["name"]
    path = PROJECTS_DIR / f"{name}.md"
    if path.exists():
        return

    language = (repo.get("primaryLanguage") or {}).get("name")
    stack = infer_stack(readme or repo.get("description") or "", language)
    visibility = "private" if repo.get("isPrivate") else "public"
    description = (repo.get("description") or "").replace('"', "'")

    content = f"""---
repo: {name}
github_url: {repo['url']}
visibility: {visibility}
status: needs-review
period: unknown
employer: unknown
role: unknown
domains: []
stack: {json.dumps(stack)}
portfolio_worthy: false
cv_worthy: false
verified_outcomes: []
links:
  demo:
  docs:
last_synced: {today}
source_readme: readmes/{name}.md
---

# {name}

> Auto-generated stub — **curate this file**. Raw README: `readmes/{name}.md`

## One-liner

{description or "_Add one sentence describing the business/technical problem solved._"}

## Problem

_TODO: owner input_

## What I built

_TODO: owner input_

## Architecture

_TODO: owner input_

## Stack (verified)

{', '.join(stack) if stack else '_TODO_'}

## Outcomes

_TODO: verified only_

## Evidence

- GitHub: {repo['url']}
- README: `readmes/{name}.md`

## Notes for AI / alignment

- [ ] Confirm employer/client context
- [ ] Mark portfolio_worthy / cv_worthy in frontmatter when ready
"""
    path.write_text(content, encoding="utf-8")


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    try:
        block = text.split("---", 2)[1]
    except IndexError:
        return {}

    data: dict[str, str] = {}
    for line in block.splitlines():
        if not line or line.startswith(" ") or line.startswith("-"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def is_true(value: str | None) -> bool:
    return (value or "").strip().lower() == "true"


def build_index(repos: list[dict], today: str) -> str:
    repo_urls = {repo["name"]: repo["url"] for repo in repos}
    profiles = []
    for path in sorted(PROJECTS_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        text = path.read_text(encoding="utf-8")
        meta = parse_frontmatter(text)
        slug = path.stem
        name = meta.get("repo") or slug
        visibility = meta.get("visibility") or "unknown"
        status = meta.get("status") or "unknown"
        employer = meta.get("employer") or "unknown"
        portfolio = is_true(meta.get("portfolio_worthy"))
        cv = is_true(meta.get("cv_worthy"))
        url = meta.get("github_url") or meta.get("mirror_url") or repo_urls.get(name) or ""
        source_readme = meta.get("source_readme") or f"readmes/{name}.md"
        readme_path = ROOT / source_readme
        readme = f"[readme]({source_readme})" if readme_path.exists() else "CV-backed"
        project = f"[{name}]({url})" if url and "private" not in visibility.lower() else name
        profile = f"[profile](projects/{path.name})"
        row = {
            "project": project,
            "visibility": visibility,
            "status": status,
            "employer": employer,
            "portfolio": str(portfolio).lower(),
            "cv": str(cv).lower(),
            "profile": profile,
            "readme": readme,
        }
        if cv:
            category = "flagship"
        elif portfolio and "private" in visibility.lower():
            category = "private"
        else:
            category = "supporting"
        profiles.append((category, name.lower(), row))

    lines = [
        "# Career project index",
        "",
        f"> Updated {today}. Public-safe portfolio/CV evidence layer.",
        "",
    ]

    def append_full_table(title: str, category: str) -> None:
        rows = [row for cat, _, row in sorted(profiles, key=lambda item: item[1]) if cat == category]
        if not rows:
            return
        lines.extend([
            f"## {title}",
            "",
            "| Project | Visibility | Status | Employer | Portfolio | CV | Profile | README |",
            "|---------|------------|--------|----------|-----------|-----|---------|--------|",
        ])
        for row in rows:
            lines.append(
                f"| {row['project']} | {row['visibility']} | {row['status']} | "
                f"{row['employer']} | {row['portfolio']} | {row['cv']} | "
                f"{row['profile']} | {row['readme']} |"
            )
        lines.append("")

    append_full_table("Flagship and CV-backed work", "flagship")
    append_full_table("Sanitized private automation", "private")
    append_full_table("Learning, archived, or supporting evidence", "supporting")
    lines.extend([
        "## Manifest and sync",
        "",
        "- GitHub sync: `python3 docs/career/scripts/sync-github-projects.py`",
        "- Public repo safety: `.sync-config.json` keeps `include_private: false` by default.",
        "- Private project details are represented only through sanitized summaries.",
        "",
    ])
    return "\n".join(lines)


def parse_frontmatter_stack(text: str) -> list[str]:
    inline = re.search(r"^stack:\s*(\[.*?\])\s*$", text, re.MULTILINE)
    if inline:
        try:
            parsed = json.loads(inline.group(1).replace("'", '"'))
            return [str(item) for item in parsed]
        except json.JSONDecodeError:
            return []

    lines = text.splitlines()
    stack: list[str] = []
    in_stack = False
    for line in lines:
        if line.strip() == "stack:":
            in_stack = True
            continue
        if not in_stack:
            continue
        if line.startswith("  - "):
            stack.append(line[4:].strip().strip('"').strip("'"))
            continue
        if line.strip() and not line.startswith(" "):
            break
    return stack


def build_stack_rollup() -> str:
    counts: dict[str, int] = {}
    labels: dict[str, str] = {}
    for path in sorted(PROJECTS_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        text = path.read_text(encoding="utf-8")
        stack = parse_frontmatter_stack(text)
        if not stack:
            continue
        for tech in stack:
            key = tech.strip().lower()
            labels.setdefault(key, tech.strip())
            counts[key] = counts.get(key, 0) + 1

    lines = [
        "# Tech stack rollup",
        "",
        f"> Updated {date.today().isoformat()}",
        "> Counts are generated from curated `docs/career/projects/*.md` frontmatter, including multiline YAML `stack:` lists. Public-safe service categories are used where exact internal names are not needed.",
        "",
        "| Technology | Projects |",
        "|------------|----------|",
    ]
    for tech, count in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
        lines.append(f"| {labels[tech]} | {count} |")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    cfg = load_config()
    user = cfg["github_user"]
    today = date.today().isoformat()

    READMES_DIR.mkdir(parents=True, exist_ok=True)
    PROJECTS_DIR.mkdir(parents=True, exist_ok=True)

    repos = gh_json([
        "repo", "list", user,
        "--limit", "200",
        "--json", "name,description,isPrivate,isFork,primaryLanguage,updatedAt,pushedAt,url",
    ])

    filtered = []
    for repo in repos:
        if repo["name"] in cfg.get("exclude_repos", []):
            continue
        if repo.get("isFork") and not cfg.get("include_forks"):
            continue
        if repo.get("isPrivate") and not cfg.get("include_private"):
            continue
        filtered.append(repo)

    print(f"Syncing {len(filtered)} repos for {user}…")

    for repo in filtered:
        name = repo["name"]
        full_name = f"{user}/{name}"
        readme = fetch_readme(full_name)
        readme_path = READMES_DIR / f"{name}.md"

        if readme:
            if len(readme) > cfg.get("readme_max_chars", 12000):
                readme = readme[: cfg["readme_max_chars"]] + "\n\n<!-- truncated by sync script -->\n"
            header = f"<!-- synced from {repo['url']} on {today} -->\n\n"
            readme_path.write_text(header + readme, encoding="utf-8")
            print(f"  readme: {name}")
        else:
            if readme_path.exists():
                print(f"  readme: {name} (kept existing, none on GitHub)")
            else:
                readme_path.write_text(
                    f"<!-- no README on GitHub as of {today} -->\n\n_No README found. Add notes in projects/{name}.md._\n",
                    encoding="utf-8",
                )
                print(f"  readme: {name} (placeholder)")

        ensure_project_stub(repo, readme, today)

    INDEX_PATH.write_text(build_index(filtered, today), encoding="utf-8")
    STACK_PATH.write_text(build_stack_rollup(), encoding="utf-8")
    print(f"Wrote {INDEX_PATH.relative_to(ROOT.parents[1])}")
    print(f"Wrote {STACK_PATH.relative_to(ROOT.parents[1])}")
    print("Next: curate docs/career/projects/*.md (employer, outcomes, portfolio_worthy).")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.CalledProcessError as exc:
        print(exc.stderr or exc.stdout or str(exc), file=sys.stderr)
        raise SystemExit(1)
