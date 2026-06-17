# Google Docs CV update - 2026-06-17

Use this to update the canonical Google Docs CVs before running `docs/resume/scripts/sync-from-google-docs.py`.

## EN summary replacement

Senior Data Engineer and Gen. AI Automation Engineer with 5+ years of experience building production data pipelines, cloud lakehouses, and LLM/n8n automation across IoT, fintech, agribusiness, and automotive intelligence. Proven track record delivering end-to-end data platforms, governed analytics datasets, conversational AI workflows, automated reporting systems, and customer-facing product implementation. Fluent in English (C1); open to relocation across Europe.

## EN TK Technologies bullet to add

- Coordinated Notion-based delivery sprints, customer-facing demos, product training, sales support, and post-launch support while preparing Play Store/EAS/DUNS mobile launch readiness.

## PT-BR summary replacement

Engenheiro de Dados Sênior e Engenheiro de Automação com IA Generativa com mais de 5 anos de experiência construindo pipelines de dados em produção, lakehouses em nuvem e automações com LLMs/n8n. Atuação comprovada em IoT, fintechs, agronegócio e inteligência automotiva utilizando AWS, Azure e GCP, com implementação de produto voltada a clientes. Inglês fluente (C1); disponível para realocação na Europa.

## PT-BR TK Technologies bullet to add

- Coordenou sprints de entrega no Notion, demos para clientes, treinamento de produto, apoio comercial e suporte pós-lançamento enquanto preparava o lançamento mobile com Play Store/EAS/DUNS.

## After updating Google Docs

Run:

```bash
python3 docs/resume/scripts/sync-from-google-docs.py
```

Then verify the synced `docs/resume/source/*.txt`, `docs/resume/pdf/*.pdf`, `docs/resume/word/*.docx`, and `assets/files/cv/*.pdf` still match the approved local wording.

**Status 2026-06-17:** Google Docs PT export is still stale (3-month contract, missing Europe relocation). Local markdown remains canonical until Google Docs are updated; use `build-word.py` and `build-basic-pdf.py` to regenerate exports.
