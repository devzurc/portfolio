# Alignment note — 2026-09-11

Working audit of public facts vs live GitHub Pages vs Google Docs. Older `docs/portfolio-audit-*.md` files still describe Europe/Curitiba positioning; treat those as historical, not current.

**Locked facts:** Florianópolis header · visa sponsorship, no relocation line · TK Feb 2026 – Present · OrbitAI and Car Parts Price Searcher on public surfaces.

## Fact matrix

| Claim | Markdown / local site | Live GitHub Pages (origin) | Google Docs (2026-09-11 export) | Action |
|-------|----------------------|----------------------------|----------------------------------|--------|
| Home city | Florianópolis | Curitiba + Europe | EN: Curitiba + Europe; PT: Curitiba availability | Deploy local site; owner paste Docs |
| Visa | Required; no relocation | Europe relocation | Europe (EN) | Same |
| TK dates | Feb 2026 – Present | Present, expected Aug 2026 | Feb–May 2026 | Same |
| Flagship names | OrbitAI, Car Parts Price Searcher | Automotive CDP, unnamed CRM | Old automotive + dbt lab | Same |
| Cover letters | Florianópolis, current TK, OrbitAI named | N/A | N/A | Local drafts only |
| Certs | On 2-page markdown + site | On site + old live PDF | Absent on current Docs | Keep on site; include when pasting Docs |
| AI platform capstones | Direction in summary only | Live PDF listed in-progress project | Absent | Do not claim shipped repos |
| `franq-data-lakehouse-challenge` | Learning profile, public GitHub | Not on site | Not on CV | Keep off CV until owner promotes |

## Local CV exports (2026-09-11)

Google Docs still fail the reject checks (Curitiba header, Europe copy, May 2026 TK end). `sync-from-google-docs.py` was **not** run.

Local Word/PDF/source were rebuilt from markdown. Site PDFs now contain Florianópolis, OrbitAI, TK Present, and no Europe line. The basic PDF renderer is 3 pages; the compact 2-page ATS layout returns when Google Docs are pasted and re-exported.

## LinkedIn (manual — page fetch failed)

Check [linkedin.com/in/lucas-cruz](https://www.linkedin.com/in/lucas-cruz) against the same facts:

- [ ] Headline: Senior Data Engineer / Gen. AI Automation Engineer (not Europe-only)
- [ ] Location: Florianópolis, Santa Catarina, Brazil
- [ ] About: no “open to relocation across Europe”
- [ ] TK Technologies: Feb 2026 – Present
- [ ] Featured/projects: OrbitAI and car-parts searcher wording matches CV, no StokIA or private URLs
