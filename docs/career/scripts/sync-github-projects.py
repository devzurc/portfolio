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
MANIFEST_PATH = ROOT / ".repo-manifest.json"
READMES_DIR = ROOT / "readmes"
PROJECTS_DIR = ROOT / "projects"
INDEX_PATH = ROOT / "INDEX.md"
STACK_PATH = ROOT / "tech-stack-rollup.md"
REPORT_PATH = ROOT / "github-sync-report.md"


def load_config() -> dict:
    defaults = {
        "github_user": "devzurc",
        "github_orgs": [],
        "exclude_repos": ["My-Profile"],
        "exclude_private_repos": [],
        "include_private": False,
        "include_forks": False,
        "private_sync_mode": "sanitized",
        "readme_max_chars": 12000,
    }
    if CONFIG_PATH.exists():
        defaults.update(json.loads(CONFIG_PATH.read_text(encoding="utf-8")))
    return defaults


def load_manifest() -> dict:
    if MANIFEST_PATH.exists():
        return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    return {}


def build_alias_map(manifest: dict) -> dict[str, str]:
    """Map owner/repo or bare repo name to knowledge_slug.

    Monorepo subpaths (entries with `subpath`) do not claim the parent repo name
    during GitHub list sync — only the primary slug maps the repo.
    """
    mapping: dict[str, str] = {}
    for slug, info in manifest.get("aliases", {}).items():
        if info.get("subpath"):
            continue
        knowledge_slug = info.get("knowledge_slug", slug)
        for ref in (info.get("canonical"), info.get("mirror"), slug):
            if not ref:
                continue
            mapping[ref.lower()] = knowledge_slug
            if "/" in ref:
                mapping[ref.split("/")[-1].lower()] = knowledge_slug
    return mapping


def resolve_slug(repo: dict, alias_map: dict[str, str]) -> str:
    owner = repo.get("owner") or ""
    name = repo["name"]
    for key in (f"{owner}/{name}".lower(), name.lower()):
        if key in alias_map:
            return alias_map[key]
    return name


def viewer_login() -> str | None:
    try:
        payload = gh_json(["api", "graphql", "-f", "query={viewer{login}}"])
        return payload["data"]["viewer"]["login"]
    except (subprocess.CalledProcessError, KeyError, TypeError):
        return None


def fetch_all_repos(cfg: dict, manifest: dict) -> list[dict]:
    target = cfg["github_user"]
    viewer = viewer_login()
    json_fields = "name,description,isPrivate,isFork,primaryLanguage,updatedAt,pushedAt,url"
    repos: list[dict] = []

    if viewer and viewer.lower() == target.lower():
        batch = gh_json([
            "repo", "list",
            "--limit", "200",
            "--json", json_fields,
        ])
        for repo in batch:
            repo = dict(repo)
            repo["owner"] = target
            repos.append(repo)
    else:
        batch = gh_json([
            "repo", "list", target,
            "--limit", "200",
            "--json", json_fields,
        ])
        for repo in batch:
            repo = dict(repo)
            repo["owner"] = target
            repos.append(repo)

    return repos


def sanitize_private_readme(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = "\n".join(line.rstrip() for line in text.split("\n"))
    text = re.sub(r"https?://[^\s<>\"'\])]+", "[REDACTED_URL]", text)
    text = re.sub(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", "[REDACTED_EMAIL]", text)
    text = re.sub(
        r"(?i)\b(?:api[_-]?key|secret|token|password|webhook|bearer)\s*[=:]\s*\S+",
        "[REDACTED_CREDENTIAL]",
        text,
    )
    text = re.sub(r"(?i)\b(?:sk|pk)_[A-Za-z0-9]{10,}", "[REDACTED_TOKEN]", text)
    text = re.sub(r"(?i)\bghp_[A-Za-z0-9]{20,}", "[REDACTED_TOKEN]", text)
    return text


def is_curated_readme(path: Path) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8").lower()
    markers = (
        "sanitized private",
        "public-safe excerpt",
        "local career note",
        "career curation note",
        "intentionally omits",
        "private tk technologies",
    )
    return any(marker in text for marker in markers)


def gh_json(args: list[str]):
    cmd = ["gh"] + args
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return json.loads(result.stdout)


def warn_if_wrong_gh_account(cfg: dict) -> None:
    expected = cfg.get("github_user", "")
    if not expected:
        return
    try:
        login = gh_json(["api", "user"]).get("login", "")
    except (subprocess.CalledProcessError, json.JSONDecodeError):
        return
    if login.lower() != expected.lower():
        print(
            f"WARNING: gh CLI is logged in as '{login}', but github_user is '{expected}'.",
            file=sys.stderr,
        )
        print(
            f"         Only public repos under {expected} will sync (~10). Private repos need:",
            file=sys.stderr,
        )
        print("         gh auth login -h github.com   # sign in as devzurc", file=sys.stderr)


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


def repo_language(repo: dict) -> str | None:
    language = repo.get("primaryLanguage") or repo.get("language")
    if isinstance(language, dict):
        return language.get("name")
    if isinstance(language, str):
        return language
    return None


def strip_sync_header(text: str) -> str:
    return re.sub(r"^<!-- synced from .*? on \d{4}-\d{2}-\d{2} -->\n\n", "", text, count=1)


def split_local_notes(text: str) -> tuple[list[str], str]:
    """Keep local career notes in README mirrors while comparing raw README bodies."""
    body = strip_sync_header(text)
    notes: list[str] = []
    pattern = re.compile(r"\A<!--\s*(?:career curation note|local career note):.*?-->\s*", re.DOTALL)
    while True:
        match = pattern.match(body)
        if not match:
            break
        notes.append(match.group(0).strip())
        body = body[match.end():]
    return notes, body


def build_readme_mirror(header: str, notes: list[str], readme: str) -> str:
    parts = [header.strip()]
    parts.extend(notes)
    parts.append(readme)
    return "\n\n".join(parts)


def normalize_readme_body(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    return "\n".join(line.rstrip() for line in text.split("\n"))


def normalize_generated_dates(text: str) -> str:
    return re.sub(r"Updated \d{4}-\d{2}-\d{2}", "Updated <date>", text)


def write_if_changed(path: Path, content: str, *, normalizer=None) -> bool:
    if path.exists():
        previous = path.read_text(encoding="utf-8")
        if normalizer:
            if normalizer(previous) == normalizer(content):
                return False
        elif previous == content:
            return False

    path.write_text(content, encoding="utf-8")
    return True


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


def ensure_project_stub(repo: dict, readme: str | None, today: str, slug: str) -> bool:
    name = repo["name"]
    path = PROJECTS_DIR / f"{slug}.md"
    if path.exists():
        return False

    language = repo_language(repo)
    stack = infer_stack(readme or repo.get("description") or "", language)
    visibility = "private" if repo.get("isPrivate") else "public"
    description = (repo.get("description") or "").replace('"', "'")
    owner = repo.get("owner") or ""
    github_ref = f"{owner}/{name}" if owner else name

    content = f"""---
repo: {slug}
github_url: {repo['url']}
github_ref: {github_ref}
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
source_readme: readmes/{slug}.md
---

# {slug}

> Auto-generated stub — **curate this file**. Raw README: `readmes/{slug}.md`

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
- README: `readmes/{slug}.md`

## Notes for AI / alignment

- [ ] Confirm employer/client context
- [ ] Mark portfolio_worthy / cv_worthy in frontmatter when ready
"""
    path.write_text(content, encoding="utf-8")
    return True


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
        "- Account: `devzurc` only — authenticate `gh` as **devzurc** (`gh auth login`) to include private repos.",
        "- Public repo safety: private README mirrors are sanitized; curated snapshots are never overwritten.",
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


def parse_stack_rollup_techs(text: str) -> set[str]:
    techs: set[str] = set()
    for line in text.splitlines():
        if not line.startswith("| ") or line.startswith("| Technology") or line.startswith("|---"):
            continue
        parts = [part.strip() for part in line.strip("|").split("|")]
        if len(parts) >= 2 and parts[0]:
            techs.add(parts[0])
    return techs


def tech_diff(current: set[str], previous: set[str]) -> tuple[list[str], list[str]]:
    """Case-insensitive stack diff to avoid false positives (e.g. Python vs python)."""
    current_by_key = {item.strip().lower(): item for item in current if item.strip()}
    previous_by_key = {item.strip().lower(): item for item in previous if item.strip()}
    new_keys = set(current_by_key) - set(previous_by_key)
    removed_keys = set(previous_by_key) - set(current_by_key)
    new_items = sorted((current_by_key[key] for key in new_keys), key=str.lower)
    removed_items = sorted((previous_by_key[key] for key in removed_keys), key=str.lower)
    return new_items, removed_items


def list_needs_review_projects() -> list[str]:
    projects = []
    for path in sorted(PROJECTS_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        meta = parse_frontmatter(path.read_text(encoding="utf-8"))
        if (meta.get("status") or "").strip() == "needs-review":
            projects.append(path.stem)
    return projects


def md_list(items: list[str], empty: str) -> list[str]:
    if not items:
        return [f"- {empty}"]
    return [f"- {item}" for item in items]


def format_recent_repo(repo: dict) -> str:
    language = repo_language(repo) or "unknown"
    visibility = "private" if repo.get("isPrivate") else "public"
    pushed = repo.get("pushedAt") or repo.get("updatedAt") or "unknown"
    return f"{repo['name']} - pushed {pushed} - {language} - {visibility}"


def build_sync_report(
    *,
    repos: list[dict],
    cfg: dict,
    today: str,
    readme_created: list[str],
    readme_updated: list[str],
    readme_missing: list[str],
    new_stubs: list[str],
    index_changed: bool,
    stack_changed: bool,
    new_techs: list[str],
    removed_techs: list[str],
    needs_review: list[str],
) -> str:
    recent = sorted(
        repos,
        key=lambda repo: repo.get("pushedAt") or repo.get("updatedAt") or "",
        reverse=True,
    )[:10]

    lines = [
        "# GitHub career sync report",
        "",
        f"> Last checked: {today}. Generated by `python3 docs/career/scripts/sync-github-projects.py`.",
        "",
        "## Scope",
        "",
        f"- GitHub user: `{cfg['github_user']}` (devzurc personal account only)",
        f"- gh CLI viewer: `{viewer_login() or 'unknown'}`",
        f"- Repos scanned after filters: {len(repos)}",
        f"- Include private repos: `{str(cfg.get('include_private', False)).lower()}`",
        f"- Private sync mode: `{cfg.get('private_sync_mode', 'sanitized')}`",
        f"- Include forks: `{str(cfg.get('include_forks', False)).lower()}`",
        "- Public safety: raw private repo details must stay out of this public portfolio workspace.",
        "",
        "## Change summary",
        "",
        f"- README mirrors created: {len(readme_created)}",
        f"- README mirrors updated: {len(readme_updated)}",
        f"- Repos without README: {len(readme_missing)}",
        f"- Project stubs created: {len(new_stubs)}",
        f"- `INDEX.md` changed: `{str(index_changed).lower()}`",
        f"- `tech-stack-rollup.md` changed: `{str(stack_changed).lower()}`",
        "",
        "## GitHub updates to review",
        "",
        "### New README mirrors",
        "",
        *md_list(readme_created, "None"),
        "",
        "### Updated README mirrors",
        "",
        *md_list(readme_updated, "None"),
        "",
        "### New project stubs",
        "",
        *md_list(new_stubs, "None"),
        "",
        "### Recently pushed repos",
        "",
        *md_list([format_recent_repo(repo) for repo in recent], "None"),
        "",
        "## Tech signal changes",
        "",
        "### Newly seen in curated project stack",
        "",
        *md_list(new_techs, "None"),
        "",
        "### No longer present in curated project stack",
        "",
        *md_list(removed_techs, "None"),
        "",
        "## Project profiles needing owner review",
        "",
        *md_list(needs_review, "None"),
        "",
        "## Agent propagation checklist",
        "",
        "- Curate each new or changed `docs/career/projects/*.md` profile before public use.",
        "- Treat GitHub README text as evidence, not final CV or portfolio copy.",
        "- Update `docs/career/JOB-SEARCH-STRATEGY.md` when a new project changes role-fit positioning.",
        "- Draft CV, cover letter, and `index.html` changes only from curated profiles or confirmed CV facts.",
        "- Ask Lucas before adding employers, dates, metrics, client names, private URLs, or outcome claims.",
        "",
        "## Safe automation boundary",
        "",
        "- Safe to auto-update: README mirrors, generated index, tech rollup, this report, and `status: needs-review` stubs.",
        "- Draft only: CV bullets, cover letter wording, project cards, hero stats, experience copy, and job-fit claims.",
        "- Never publish: workflow IDs, webhook URLs, secrets, internal URLs, raw Notion ticket names, phone numbers, or private client details.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    cfg = load_config()
    manifest = load_manifest()
    alias_map = build_alias_map(manifest)
    warn_if_wrong_gh_account(cfg)
    today = date.today().isoformat()

    READMES_DIR.mkdir(parents=True, exist_ok=True)
    PROJECTS_DIR.mkdir(parents=True, exist_ok=True)

    previous_stack = STACK_PATH.read_text(encoding="utf-8") if STACK_PATH.exists() else ""
    previous_techs = parse_stack_rollup_techs(previous_stack)

    repos = fetch_all_repos(cfg, manifest)

    filtered = []
    for repo in repos:
        if repo["name"] in cfg.get("exclude_repos", []):
            continue
        if repo.get("isFork") and not cfg.get("include_forks"):
            continue
        if repo.get("isPrivate") and not cfg.get("include_private"):
            continue
        if repo.get("isPrivate") and repo["name"] in cfg.get("exclude_private_repos", []):
            continue
        filtered.append(repo)

    owners = sorted({repo.get("owner", cfg["github_user"]) for repo in filtered})
    print(f"Syncing {len(filtered)} repos across {', '.join(owners)}…")
    readme_created: list[str] = []
    readme_updated: list[str] = []
    readme_missing: list[str] = []
    readme_curated: list[str] = []
    new_stubs: list[str] = []

    for repo in filtered:
        slug = resolve_slug(repo, alias_map)
        owner = repo.get("owner") or cfg["github_user"]
        full_name = f"{owner}/{repo['name']}"
        is_private = bool(repo.get("isPrivate"))
        readme_path = READMES_DIR / f"{slug}.md"

        readme = None
        if not (is_private and cfg.get("private_sync_mode") == "metadata-only"):
            readme = fetch_readme(full_name)

        if readme:
            readme = normalize_readme_body(readme)
            if is_private:
                readme = sanitize_private_readme(readme)
            if len(readme) > cfg.get("readme_max_chars", 12000):
                readme = readme[: cfg["readme_max_chars"]] + "\n\n<!-- truncated by sync script -->\n"
            header = (
                f"<!-- PRIVATE REPO: sanitized from {repo['url']} on {today} -->\n\n"
                if is_private
                else f"<!-- synced from {repo['url']} on {today} -->\n\n"
            )
            if is_curated_readme(readme_path):
                readme_curated.append(slug)
                print(f"  readme: {slug} (kept curated snapshot)")
            else:
                previous = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""
                local_notes, previous_readme = split_local_notes(previous)
                changed = previous_readme != readme
                if changed:
                    readme_path.write_text(build_readme_mirror(header, local_notes, readme), encoding="utf-8")
                    if previous:
                        readme_updated.append(slug)
                        print(f"  readme: {slug} (updated)")
                    else:
                        readme_created.append(slug)
                        print(f"  readme: {slug} (created)")
                else:
                    print(f"  readme: {slug} (unchanged)")
        else:
            readme_missing.append(slug)
            if is_curated_readme(readme_path):
                readme_curated.append(slug)
                print(f"  readme: {slug} (kept curated snapshot, none on GitHub)")
            elif readme_path.exists():
                print(f"  readme: {slug} (kept existing, none on GitHub)")
            else:
                placeholder = (
                    f"<!-- no README on GitHub as of {today} -->\n\n"
                    f"_No README found. Add notes in projects/{slug}.md._\n"
                )
                if is_private:
                    placeholder = (
                        f"<!-- PRIVATE REPO: no README on GitHub as of {today} -->\n\n"
                        f"_No README found. Curate sanitized notes in projects/{slug}.md._\n"
                    )
                readme_path.write_text(placeholder, encoding="utf-8")
                print(f"  readme: {slug} (placeholder)")

        if ensure_project_stub(repo, readme, today, slug):
            new_stubs.append(slug)

    index_content = build_index(filtered, today)
    stack_content = build_stack_rollup()
    index_changed = write_if_changed(INDEX_PATH, index_content, normalizer=normalize_generated_dates)
    stack_changed = write_if_changed(STACK_PATH, stack_content, normalizer=normalize_generated_dates)
    current_techs = parse_stack_rollup_techs(stack_content)
    new_techs, removed_techs = tech_diff(current_techs, previous_techs)
    needs_review = list_needs_review_projects()
    report = build_sync_report(
        repos=filtered,
        cfg=cfg,
        today=today,
        readme_created=readme_created,
        readme_updated=readme_updated,
        readme_missing=readme_missing,
        new_stubs=new_stubs,
        index_changed=index_changed,
        stack_changed=stack_changed,
        new_techs=new_techs,
        removed_techs=removed_techs,
        needs_review=needs_review,
    )
    REPORT_PATH.write_text(report, encoding="utf-8")
    print(f"{'Wrote' if index_changed else 'Checked'} {INDEX_PATH.relative_to(ROOT.parents[1])}")
    print(f"{'Wrote' if stack_changed else 'Checked'} {STACK_PATH.relative_to(ROOT.parents[1])}")
    print(f"Wrote {REPORT_PATH.relative_to(ROOT.parents[1])}")
    print("Next: curate docs/career/projects/*.md (employer, outcomes, portfolio_worthy).")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.CalledProcessError as exc:
        print(exc.stderr or exc.stdout or str(exc), file=sys.stderr)
        raise SystemExit(1)
