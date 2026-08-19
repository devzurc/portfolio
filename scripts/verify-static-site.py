#!/usr/bin/env python3
"""Dependency-free regression checks for the static portfolio."""

from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PortfolioParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.headings: list[int] = []
        self.assets: list[str] = []
        self.inline_events: list[str] = []
        self.meta: dict[str, str] = {}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.headings.append(int(tag[1]))
        for name, value in attrs:
            if name.startswith("on"):
                self.inline_events.append(name)
            if tag in {"img", "script"} and name == "src" and value:
                self.assets.append(value)
            if tag == "link" and name == "href" and attributes.get("rel") == "stylesheet" and value:
                self.assets.append(value)
        if tag == "meta" and attributes.get("name") in {"description", "twitter:card"}:
            self.meta[attributes["name"]] = attributes.get("content", "")
        if tag == "meta" and attributes.get("property") == "og:image":
            self.meta["og:image"] = attributes.get("content", "")


def main() -> int:
    parser = PortfolioParser()
    parser.feed((ROOT / "index.html").read_text(encoding="utf-8"))
    errors: list[str] = []
    for previous, current in zip(parser.headings, parser.headings[1:]):
        if current > previous + 1:
            errors.append(f"heading level jumps from h{previous} to h{current}")
    if parser.inline_events:
        errors.append(f"inline event attributes found: {', '.join(sorted(set(parser.inline_events)))}")
    for asset in parser.assets:
        if asset.startswith(("http://", "https://", "//")):
            continue
        if not (ROOT / asset).is_file():
            errors.append(f"missing local asset: {asset}")
    for name in ("description", "twitter:card", "og:image"):
        if not parser.meta.get(name):
            errors.append(f"missing required metadata: {name}")
    sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    if "<lastmod>" not in sitemap:
        errors.append("sitemap has no lastmod")
    if errors:
        print("Static-site verification failed:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    print("Static-site verification passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
