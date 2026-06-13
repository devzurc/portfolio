#!/usr/bin/env python3
"""Build simple text-first PDF CV files from markdown sources.

This is a local fallback for environments without LibreOffice, Pandoc, or
Google Docs export access. The design is intentionally plain, but the content
comes from the canonical markdown files.
"""

from __future__ import annotations

import re
import shutil
import textwrap
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
MD_DIR = ROOT / "markdown"
PDF_DIR = ROOT / "pdf"
ASSETS_CV = REPO / "assets" / "files" / "cv"

PAGE_W = 595
PAGE_H = 842
MARGIN = 42


@dataclass
class DrawText:
    text: str
    x: float
    y: float
    size: float
    font: str = "F1"


def strip_frontmatter(content: str) -> str:
    if not content.startswith("---"):
        return content
    end = content.find("\n---", 3)
    if end == -1:
        return content
    return content[end + 4 :].lstrip("\n")


def strip_md(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    return text.strip()


def parse_markdown(md_path: Path) -> list[tuple[str, str]]:
    body = strip_frontmatter(md_path.read_text(encoding="utf-8"))
    blocks: list[tuple[str, str]] = []
    for raw in body.splitlines():
        line = raw.rstrip()
        if not line:
            blocks.append(("blank", ""))
        elif line.startswith("# "):
            blocks.append(("h1", strip_md(line[2:])))
        elif line.startswith("## "):
            blocks.append(("h2", strip_md(line[3:])))
        elif line.startswith("### "):
            blocks.append(("h3", strip_md(line[4:])))
        elif line.startswith("- "):
            blocks.append(("bullet", strip_md(line[2:])))
        elif line.startswith("|") and "---" not in line:
            parts = [strip_md(part) for part in line.strip("|").split("|")]
            if len(parts) == 2 and parts[0].lower() not in ("category", "categoria"):
                blocks.append(("skill", f"{parts[0]}: {parts[1]}"))
        else:
            blocks.append(("p", strip_md(line)))
    return blocks


def wrap_text(text: str, size: float, indent: int = 0) -> list[str]:
    usable = PAGE_W - (MARGIN * 2) - indent
    width = max(34, int(usable / (size * 0.52)))
    return textwrap.wrap(text, width=width, break_long_words=False) or [""]


def paginate(blocks: list[tuple[str, str]]) -> list[list[DrawText]]:
    pages: list[list[DrawText]] = []
    page: list[DrawText] = []
    y = PAGE_H - MARGIN

    def ensure_space(height: float) -> None:
        nonlocal page, y
        if y - height >= MARGIN:
            return
        pages.append(page)
        page = []
        y = PAGE_H - MARGIN

    def add_line(text: str, size: float, font: str = "F1", x: float = MARGIN, center: bool = False) -> None:
        nonlocal y
        ensure_space(size * 1.45)
        draw_x = x
        if center:
            draw_x = max(MARGIN, (PAGE_W - len(text) * size * 0.5) / 2)
        page.append(DrawText(text=text, x=draw_x, y=y, size=size, font=font))
        y -= size * 1.45

    for kind, text in blocks:
        if kind == "blank":
            y -= 4
            continue
        if kind == "h1":
            y -= 4
            add_line(text, 18, "F2", center=True)
            continue
        if kind == "h2":
            y -= 8
            add_line(text.upper(), 11, "F2")
            y -= 2
            continue
        if kind == "h3":
            y -= 4
            for line in wrap_text(text, 10.5):
                add_line(line, 10.5, "F2")
            continue
        if kind == "bullet":
            wrapped = wrap_text(text, 9.4, indent=16)
            for idx, line in enumerate(wrapped):
                prefix = "- " if idx == 0 else "  "
                add_line(prefix + line, 9.4, x=MARGIN + 10)
            continue
        if kind == "skill":
            for line in wrap_text(text, 8.8):
                add_line(line, 8.8)
            continue
        size = 9.6
        center = "@" in text or "linkedin" in text or "github" in text or "+55" in text
        font = "F2" if text.startswith("Senior ") or text.startswith("Engenheiro ") else "F1"
        for line in wrap_text(text, size):
            add_line(line, size, font, center=center)

    if page:
        pages.append(page)
    return pages


def pdf_string(text: str) -> bytes:
    raw = text.encode("cp1252", errors="replace")
    out = bytearray()
    for byte in raw:
        if byte in (0x28, 0x29, 0x5C):
            out.extend(b"\\" + bytes([byte]))
        elif byte < 32 or byte > 126:
            out.extend(f"\\{byte:03o}".encode("ascii"))
        else:
            out.append(byte)
    return b"(" + bytes(out) + b")"


def build_pdf(pages: list[list[DrawText]], out_path: Path) -> None:
    objects: list[bytes] = []

    def add_obj(data: bytes) -> int:
        objects.append(data)
        return len(objects)

    catalog_id = add_obj(b"<< /Type /Catalog /Pages 2 0 R >>")
    pages_id = add_obj(b"")
    font_regular_id = add_obj(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>")
    font_bold_id = add_obj(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>")

    page_ids: list[int] = []
    for page in pages:
        commands: list[bytes] = []
        for item in page:
            commands.append(
                b"BT /%s %.1f Tf %.1f %.1f Td %s Tj ET"
                % (item.font.encode("ascii"), item.size, item.x, item.y, pdf_string(item.text))
            )
        stream = b"\n".join(commands)
        content_id = add_obj(b"<< /Length %d >>\nstream\n%s\nendstream" % (len(stream), stream))
        page_id = add_obj(
            b"<< /Type /Page /Parent %d 0 R /MediaBox [0 0 %d %d] "
            b"/Resources << /Font << /F1 %d 0 R /F2 %d 0 R >> >> /Contents %d 0 R >>"
            % (pages_id, PAGE_W, PAGE_H, font_regular_id, font_bold_id, content_id)
        )
        page_ids.append(page_id)

    kids = b" ".join(f"{page_id} 0 R".encode("ascii") for page_id in page_ids)
    objects[pages_id - 1] = b"<< /Type /Pages /Kids [%s] /Count %d >>" % (kids, len(page_ids))
    objects[catalog_id - 1] = b"<< /Type /Catalog /Pages %d 0 R >>" % pages_id

    out = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = [0]
    for idx, obj in enumerate(objects, start=1):
        offsets.append(len(out))
        out.extend(f"{idx} 0 obj\n".encode("ascii"))
        out.extend(obj)
        out.extend(b"\nendobj\n")
    xref = len(out)
    out.extend(f"xref\n0 {len(objects) + 1}\n".encode("ascii"))
    out.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        out.extend(f"{offset:010d} 00000 n \n".encode("ascii"))
    out.extend(
        b"trailer\n"
        + b"<< /Size %d /Root %d 0 R >>\n" % (len(objects) + 1, catalog_id)
        + b"startxref\n"
        + str(xref).encode("ascii")
        + b"\n%%EOF\n"
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(bytes(out))


def main() -> int:
    targets = [
        (MD_DIR / "LucasCruz_CV_EN.md", PDF_DIR / "LucasCruz_CV_EN.pdf"),
        (MD_DIR / "LucasCruz_CV_PT.md", PDF_DIR / "LucasCruz_CV_PT.pdf"),
    ]
    for md_path, pdf_path in targets:
        pages = paginate(parse_markdown(md_path))
        build_pdf(pages, pdf_path)
        ASSETS_CV.mkdir(parents=True, exist_ok=True)
        shutil.copy2(pdf_path, ASSETS_CV / pdf_path.name)
        print(f"Wrote {pdf_path} ({len(pages)} page(s))")
        print(f"Copied {ASSETS_CV / pdf_path.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
