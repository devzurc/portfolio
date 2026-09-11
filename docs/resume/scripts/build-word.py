#!/usr/bin/env python3
"""Build compact A4 Word CVs from markdown, matching the original Google Docs geometry."""

from __future__ import annotations

import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING, WD_TAB_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt


ROOT = Path(__file__).resolve().parents[1]
MD_DIR = ROOT / "markdown"
WORD_DIR = ROOT / "word"

MONTH_RE = (
    r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|"
    r"Fev|Abr|Mai|Ago|Set|Out|Dez)"
)
JOB_DATE_RE = re.compile(rf"^(.*?)\s+·\s+({MONTH_RE}\b.*)$")
SKILL_HEADERS = {"category", "categoria", "skills", "competências", "competencias"}


def strip_md(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    return text.strip()


def parse_frontmatter(content: str) -> tuple[dict[str, str], str]:
    if not content.startswith("---"):
        return {}, content
    end = content.find("\n---", 3)
    if end == -1:
        return {}, content
    block = content[3:end].strip().splitlines()
    meta: dict[str, str] = {}
    for line in block:
        if ":" in line:
            key, value = line.split(":", 1)
            meta[key.strip()] = value.strip()
    body = content[end + 4 :].lstrip("\n")
    return meta, body


def set_run_font(run, *, name: str = "Calibri", size: Pt | None = None, bold: bool | None = None, italic: bool | None = None) -> None:
    run.font.name = name
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(attr), name)
    if size is not None:
        run.font.size = size
    if bold is not None:
        run.bold = bold
    if italic is not None:
        run.italic = italic


def set_compact_paragraph(paragraph, *, before: float = 0, after: float = 0, line: float = 12, keep_with_next: bool = False) -> None:
    fmt = paragraph.paragraph_format
    fmt.space_before = Pt(before)
    fmt.space_after = Pt(after)
    fmt.line_spacing_rule = WD_LINE_SPACING.EXACTLY
    fmt.line_spacing = Pt(line)
    fmt.widow_control = True
    fmt.keep_together = True
    fmt.keep_with_next = keep_with_next


def disable_cell_margins(table) -> None:
    tbl = table._tbl
    tbl_pr = tbl.tblPr
    if tbl_pr is None:
        tbl_pr = OxmlElement("w:tblPr")
        tbl.insert(0, tbl_pr)
    existing = tbl_pr.find(qn("w:tblCellMar"))
    if existing is not None:
        tbl_pr.remove(existing)
    margins = OxmlElement("w:tblCellMar")
    for edge, value in (("top", "20"), ("left", "40"), ("bottom", "20"), ("right", "60")):
        node = OxmlElement(f"w:{edge}")
        node.set(qn("w:w"), value)
        node.set(qn("w:type"), "dxa")
        margins.append(node)
    tbl_pr.append(margins)


def set_table_width(table, width_twips: int) -> None:
    tbl = table._tbl
    tbl_pr = tbl.tblPr
    tbl_w = tbl_pr.find(qn("w:tblW"))
    if tbl_w is None:
        tbl_w = OxmlElement("w:tblW")
        tbl_pr.append(tbl_w)
    tbl_w.set(qn("w:w"), str(width_twips))
    tbl_w.set(qn("w:type"), "dxa")
    layout = tbl_pr.find(qn("w:tblLayout"))
    if layout is None:
        layout = OxmlElement("w:tblLayout")
        tbl_pr.append(layout)
    layout.set(qn("w:type"), "fixed")


def clear_table_borders(table) -> None:
    tbl = table._tbl
    tbl_pr = tbl.tblPr
    existing = tbl_pr.find(qn("w:tblBorders"))
    if existing is not None:
        tbl_pr.remove(existing)
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        node = OxmlElement(f"w:{edge}")
        node.set(qn("w:val"), "nil")
        node.set(qn("w:sz"), "0")
        node.set(qn("w:space"), "0")
        node.set(qn("w:color"), "auto")
        borders.append(node)
    tbl_pr.append(borders)


def set_cell_width(cell, width_twips: int) -> None:
    tc = cell._tc
    tc_pr = tc.get_or_add_tcPr()
    tc_w = tc_pr.find(qn("w:tcW"))
    if tc_w is None:
        tc_w = OxmlElement("w:tcW")
        tc_pr.append(tc_w)
    tc_w.set(qn("w:w"), str(width_twips))
    tc_w.set(qn("w:type"), "dxa")


def set_narrow_margins(doc: Document) -> None:
    for section in doc.sections:
        section.page_width = Cm(21.0)
        section.page_height = Cm(29.7)
        section.top_margin = Cm(1.15)
        section.bottom_margin = Cm(1.15)
        section.left_margin = Cm(1.4)
        section.right_margin = Cm(1.4)


def content_width_emu(doc: Document) -> int:
    section = doc.sections[0]
    return int(section.page_width) - int(section.left_margin) - int(section.right_margin)


def content_width_twips(doc: Document) -> int:
    return int(round(content_width_emu(doc) / 635))


def add_horizontal_rule(doc: Document) -> None:
    p = doc.add_paragraph()
    set_compact_paragraph(p, before=4, after=2, line=4)
    p_pr = p._p.get_or_add_pPr()
    p_bdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "6")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), "B0B0B0")
    p_bdr.append(bottom)
    p_pr.append(p_bdr)


def add_bullet(doc: Document, text: str) -> None:
    p = doc.add_paragraph(style="List Bullet")
    set_compact_paragraph(p, before=0, after=1, line=12)
    p.paragraph_format.left_indent = Cm(0.45)
    p.paragraph_format.first_line_indent = Cm(-0.25)
    run = p.add_run(strip_md(text.lstrip("- ").strip()))
    set_run_font(run, size=Pt(9.5))


def add_skills_table(doc: Document, rows: list[tuple[str, str]]) -> None:
    table = doc.add_table(rows=0, cols=2)
    table.autofit = False
    clear_table_borders(table)
    disable_cell_margins(table)
    total = content_width_twips(doc)
    label_w = int(total * 0.31)
    skills_w = total - label_w
    set_table_width(table, total)
    for category, skills in rows:
        cells = table.add_row().cells
        set_cell_width(cells[0], label_w)
        set_cell_width(cells[1], skills_w)
        cells[0].text = ""
        cells[1].text = ""
        cat_p = cells[0].paragraphs[0]
        set_compact_paragraph(cat_p, before=1, after=1, line=12)
        cat_run = cat_p.add_run(category)
        set_run_font(cat_run, size=Pt(9), bold=True)
        skill_p = cells[1].paragraphs[0]
        set_compact_paragraph(skill_p, before=1, after=1, line=12)
        skill_run = skill_p.add_run(skills)
        set_run_font(skill_run, size=Pt(9))


def add_heading_block(doc: Document, text: str) -> None:
    add_horizontal_rule(doc)
    p = doc.add_paragraph()
    set_compact_paragraph(p, before=2, after=3, line=14, keep_with_next=True)
    run = p.add_run(text.upper())
    set_run_font(run, size=Pt(11), bold=True)


def add_job_header(doc: Document, text: str) -> None:
    p = doc.add_paragraph()
    set_compact_paragraph(p, before=5, after=1, line=13, keep_with_next=True)
    tab_stops = p.paragraph_format.tab_stops
    tab_stops.add_tab_stop(content_width_emu(doc), WD_TAB_ALIGNMENT.RIGHT)
    match = JOB_DATE_RE.match(text)
    if match:
        left, dates = match.group(1).strip(), match.group(2).strip()
        left_run = p.add_run(left)
        set_run_font(left_run, size=Pt(10.5), bold=True)
        p.add_run("\t")
        date_run = p.add_run(dates)
        set_run_font(date_run, size=Pt(9.5), italic=True)
        return
    run = p.add_run(text)
    set_run_font(run, size=Pt(10.5), bold=True)


def add_project_header(doc: Document, text: str) -> None:
    p = doc.add_paragraph()
    set_compact_paragraph(p, before=5, after=1, line=13, keep_with_next=True)
    parts = [part.strip() for part in text.split(" · ") if part.strip()]
    if len(parts) >= 2:
        title_run = p.add_run(parts[0])
        set_run_font(title_run, size=Pt(10.5), bold=True)
        rest_run = p.add_run("  ·  " + "  ·  ".join(parts[1:]))
        set_run_font(rest_run, size=Pt(9), italic=True)
        return
    run = p.add_run(text)
    set_run_font(run, size=Pt(10.5), bold=True)


def is_centered_meta(line: str) -> bool:
    lowered = line.lower()
    return any(
        token in lowered
        for token in (
            "+55",
            "@",
            "linkedin",
            "github",
            "curitiba",
            "florianópolis",
            "florianopolis",
            "relocation",
            "realocação",
            "realocacao",
        )
    )


def configure_styles(doc: Document) -> None:
    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(10)
    style.paragraph_format.space_before = Pt(0)
    style.paragraph_format.space_after = Pt(0)
    style.paragraph_format.line_spacing = 1.0
    rpr = style.element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(attr), "Calibri")


def build_docx(md_path: Path, out_path: Path) -> None:
    content = md_path.read_text(encoding="utf-8")
    _, body = parse_frontmatter(content)
    lines = body.splitlines()

    doc = Document()
    set_narrow_margins(doc)
    configure_styles(doc)

    i = 0
    skill_rows: list[tuple[str, str]] = []
    in_projects = False

    while i < len(lines):
        line = lines[i].rstrip()

        if not line:
            i += 1
            continue

        if line.startswith("# "):
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            set_compact_paragraph(p, before=0, after=1, line=22)
            run = p.add_run(strip_md(line[2:]))
            set_run_font(run, size=Pt(18), bold=True)
            i += 1
            continue

        if line.startswith("**") and line.endswith("**"):
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            set_compact_paragraph(p, before=0, after=1, line=14)
            run = p.add_run(strip_md(line))
            set_run_font(run, size=Pt(11), bold=True)
            i += 1
            continue

        if line.startswith("## "):
            if skill_rows:
                add_skills_table(doc, skill_rows)
                skill_rows = []
            heading = strip_md(line[3:])
            in_projects = heading.lower() in {"notable projects", "projetos de destaque"}
            add_heading_block(doc, heading)
            i += 1
            continue

        if line.startswith("### "):
            heading = strip_md(line[4:])
            if in_projects:
                add_project_header(doc, heading)
            elif " | " in heading:
                add_job_header(doc, heading)
            elif " · " in heading:
                add_project_header(doc, heading)
            else:
                add_job_header(doc, heading)
            i += 1
            continue

        if line.startswith("|"):
            if "---" not in line:
                parts = [part.strip() for part in line.strip("|").split("|")]
                if len(parts) == 2 and parts[0].lower() not in SKILL_HEADERS:
                    skill_rows.append((strip_md(parts[0]), strip_md(parts[1])))
            i += 1
            continue

        if line.startswith("- "):
            add_bullet(doc, line)
            i += 1
            continue

        if line.startswith("*") and line.endswith("*"):
            p = doc.add_paragraph()
            set_compact_paragraph(p, before=0, after=1, line=12)
            run = p.add_run(strip_md(line))
            set_run_font(run, size=Pt(9), italic=True)
            i += 1
            continue

        if line.startswith("**") and "—" in line:
            p = doc.add_paragraph()
            set_compact_paragraph(p, before=4, after=1, line=13)
            run = p.add_run(strip_md(line))
            set_run_font(run, size=Pt(10), bold=True)
            i += 1
            continue

        p = doc.add_paragraph()
        set_compact_paragraph(p, before=0, after=1, line=12.5)
        run = p.add_run(strip_md(line))
        set_run_font(run, size=Pt(10))
        if is_centered_meta(line):
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            set_run_font(run, size=Pt(9.5))
        i += 1

    if skill_rows:
        add_skills_table(doc, skill_rows)

    WORD_DIR.mkdir(parents=True, exist_ok=True)
    doc.save(out_path)
    print(f"Wrote {out_path}")


def main() -> int:
    targets = [
        (MD_DIR / "LucasCruz_CV_EN.md", WORD_DIR / "LucasCruz_CV_EN.docx"),
        (MD_DIR / "LucasCruz_CV_PT.md", WORD_DIR / "LucasCruz_CV_PT.docx"),
    ]
    for md_path, out_path in targets:
        if not md_path.exists():
            print(f"Missing {md_path}", file=sys.stderr)
            return 1
        build_docx(md_path, out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
