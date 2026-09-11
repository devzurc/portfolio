# Google Docs CV update — 2026-09-10

> **Checked 2026-09-11:** Canonical Google Docs still serve Curitiba / Europe / Feb–May 2026 copy. Do **not** run `sync-from-google-docs.py` until this pack is pasted in place. Local Word/PDF/source files were rebuilt from markdown so site downloads match Florianópolis, TK Present, and OrbitAI. Google Docs remain the ATS original once this paste is done.

Restore the **original compact 2-page Google Docs layout**, then replace text in place. Canonical draft copy lives in `docs/resume/markdown/LucasCruz_CV_EN.md` and `docs/resume/markdown/LucasCruz_CV_PT.md`.

**Do not** paste Markdown (`#`, `|`, `---`, `###`) into Google Docs. **Do not** delete the skills table. **Do not** run `python3 docs/resume/scripts/sync-from-google-docs.py` until both Docs look aligned on 2 pages.

| Language | Google Doc |
|----------|------------|
| EN | https://docs.google.com/document/d/1O4YsNWyfANs_332ecNZ8fgf-wclyuJCjZpO0LBqX2S8/edit |
| PT-BR | https://docs.google.com/document/d/1oi8mzTJNNTu3CdSuqEgiWCPmiyvGWxrsstU93K0QV0Q/edit |

## Layout rules (keep these)

- A4, narrow margins, **2 pages**
- Centered name, role, contact, and location
- Skills stay a **2-column table** (category | skills), 7 rows, no extra rows
- Job title and dates stay **on the same line**
- Hairline or no table borders — do not convert the table into a heavy grid
- Do not add StokIA, internal URLs, workflow IDs, or unverified metrics

If a paste breaks spacing: Undo, select only the old sentence, and type/replace the new sentence inside the existing style.

---

## 1. English CV

### Header

Role line:

```text
Senior Data Engineer | Gen. AI Automation Engineer
```

Keep the existing contact line. Location line:

```text
Florianópolis, Santa Catarina, Brazil  •  Requires visa sponsorship
```

### Professional Summary (replace the whole paragraph)

```text
Senior Data Engineer and Gen. AI Automation Engineer with 5+ years of experience building production data pipelines, cloud lakehouses, AI agents, and LLM/n8n automation across IoT, fintech, agribusiness, and automotive intelligence. Proven track record delivering end-to-end data platforms, governed analytics, conversational AI workflows, and customer-facing product development. Currently extending this work toward production AI platforms (RAG, agents, evaluation, MCP, observability) over enterprise data. Fluent in English (C1).
```

### Technical Skills (edit cells only — keep 7 rows)

| Category | Skills |
|----------|--------|
| Gen. AI & LLMs | LLM Integration, AI Agents (OpenAI, Claude, Gemini…), RAG, Prompt Engineering, Chatbot Development |
| Data Engineering & Orchestration | Python, SQL, Apache Spark (PySpark), Pandas, FastAPI, NestJS, Next.js, dbt, Trino, REST APIs, Web Scraping, Playwright, Parquet, Apache Airflow, n8n, Celery, Redis, Meta Cloud API |
| Cloud & Lakehouses | Amazon Web Service (AWS), Microsoft Azure, Google Cloud (GCP), Oracle Cloud (OCI), Snowflake, Databricks, Amazon Redshift, Delta Lake, Oracle Autonomous Database |
| Relational Databases & BI | PostgreSQL, SQL Server, MySQL, Redis, Power BI, Qlik Sense, Apache Superset, Looker |
| Security & Data Governance | LGPD/GDPR Compliance, Data Privacy, IAM, RBAC, Data Masking, Encryption (Rest/Transit), Audit Logging, RFID/NFC Tagging, Firewall |
| DevOps & Infrastructure | Docker, Kubernetes, Azure Bicep, Azure Container Apps, Git, CI/CD Pipelines, Linux, Bash Scripting |
| Languages | Portuguese (Native)  •  English (C1 – Advanced)  •  Spanish (B1 – Intermediate) |

If `WORK EXPERIENCE` is sitting inside the last skills row, cut it out of the table and put it back as the next section heading.

### Work Experience — TK Technologies

Replace the job header (keep one line):

```text
Gen. AI Engineer  –  TK Technologies  |  Curitiba, PR – Brazil (Hybrid)     Feb 2026 – Present · Contract
```

Replace the TK bullets with these five (remove the old Azure ~25% deployment bullet):

```text
• Architected OrbitAI, an omnichannel AI CRM platform (WhatsApp, Instagram, Facebook, Telegram, and Email) with role-based data governance, Meta/Google Ads tracking, and LLM-powered auto-replies, deploying to Azure Container Apps with Bicep IaC.
• Engineered a multi-source web scraping pipeline in Python targeting 10+ automotive parts websites, extracting pricing and product metadata at scale to deliver competitive market intelligence.
• Architected AI-powered n8n automation workflows (ETL, RPA, and chatbot agents) by integrating LLMs (Claude AI, Google AI Studio) and GCP APIs (Sheets, Drive) to enrich datasets and reduce manual analysis work.
• Developed a conversational AI chatbot that empowers business users to query and refine pricing datasets via natural language, reducing time-to-insight for non-technical stakeholders.
• Coordinated Notion-based delivery sprints, customer-facing demos, product training, sales support, and post-launch support; contribute to the TK web presence and ongoing CRM product development and maintenance.
```

### Work Experience — Spacecom / wDiscover / Itaete

Keep the existing roles, dates, and previously published metrics. Do not rewrite these blocks unless a heading lost its date alignment.

### Notable Projects

Keep three entries. Remove **Modern Cloud Data Pipeline** (Snowflake/dbt) and any standalone Telegram or in-progress AI-platform project block.

**1. Add at the top:**

```text
OrbitAI — Omnichannel AI CRM  ·  NestJS, Next.js, PostgreSQL, LLMs, Meta & Google Ads APIs, Azure Container Apps, Docker  ·  TK Technologies – Jun 2026 – Present
• Built OrbitAI, a secure omnichannel CRM integrating WhatsApp, Instagram, Facebook, Telegram, and Email into a unified inbox with role-based access control (RBAC).
• Layered Meta/Google Ads performance data and LLMs (Claude/Google AI Studio) for auto-replies, outbound messaging assistance, and automated campaign analysis.
```

**2. Replace the automotive project:**

```text
Car Parts Price Searcher  ·  Python, FastAPI, Celery, Playwright, Redis, PostgreSQL, n8n, Azure, Bicep  ·  TK Technologies – Feb 2026 – Present
• Built a car-parts price searcher across 10+ sites, with parallel public-price and internal-stock lookup, auditable reporting, and notifications from containerised Azure services.
```

**3. Keep the IoT lakehouse entry** (Feb 2024) as-is.

### Licenses & Certifications (add after Education if missing)

```text
• AI for Writing and Communicating — Google (Credential ID: HE8YE5IS7WVW) · Jul 2026
• AI for Research and Insights — Google (Credential ID: 4PZDF3XQOF55) · Jul 2026
• AI for Brainstorming and Planning — Google (Credential ID: 7SFW2HGOKIU5) · Jul 2026
• AI Fundamentals — Google (Credential ID: UKBGM0AZUIS2) · Jul 2026
```

Do not add Microsoft Applied Skills until a Credly or Microsoft Learn URL is confirmed.

---

## 2. Portuguese CV

The PT Doc is further behind (3-month on-site TK, extra skills rows). Restore the same 7-row table and compact headers as EN.

### Header

Role line:

```text
Engenheiro de Dados Sênior | Engenheiro de Automação com IA Generativa
```

Location line (replace the old presencial/híbrido/remoto sentence):

```text
Florianópolis, Santa Catarina  •  Necessita de patrocínio de visto
```

### Resumo Profissional

```text
Engenheiro de Dados Sênior e Engenheiro de Automação com IA Generativa com mais de 5 anos de experiência construindo pipelines de dados em produção, lakehouses em nuvem, agentes de IA e automações com LLMs/n8n. Atuação comprovada em IoT, fintechs, agronegócio e inteligência automotiva, com desenvolvimento e manutenção de produtos voltados a clientes. Atualmente estende esse trabalho para plataformas de IA em produção (RAG, agentes, avaliação, MCP, observabilidade) sobre dados empresariais. Inglês fluente (C1).
```

### Competências Técnicas (exactly 7 rows)

Merge “Plataformas de Nuvem” and “Plataformas de Dados” into **Cloud & Lakehouses**. Merge extra BI/database rows if present.

| Categoria | Competências |
|-----------|--------------|
| IA Generativa & LLMs | Integração com LLMs, Agentes de IA (OpenAI, Claude, Gemini…), RAG, Engenharia de Prompt, Chatbots |
| Dados & Orquestração | Python, SQL, Apache Spark (PySpark), Pandas, FastAPI, NestJS, Next.js, dbt, Trino, REST APIs, Web Scraping, Playwright, Parquet, Apache Airflow, n8n, Celery, Redis, Meta Cloud API |
| Cloud & Lakehouses | Amazon Web Service (AWS), Microsoft Azure, Google Cloud (GCP), Oracle Cloud (OCI), Snowflake, Databricks, Amazon Redshift, Delta Lake, Oracle Autonomous Database |
| Bancos de Dados & BI | PostgreSQL, SQL Server, MySQL, Redis, Power BI, Qlik Sense, Apache Superset, Looker |
| Segurança & Governança | Conformidade LGPD/GDPR, Privacidade de Dados, IAM, RBAC, Mascaramento de Dados, Criptografia em Repouso/Trânsito, Logs de Auditoria, RFID/NFC, Firewall |
| DevOps & Infraestrutura | Docker, Kubernetes, Azure Bicep, Azure Container Apps, Git, Pipelines CI/CD, Linux, Bash Scripting |
| Idiomas | Português (Nativo)  •  Inglês (C1 – Avançado)  •  Espanhol (B1 – Intermediário) |

### Experiência — TK Technologies

Header (one line):

```text
Engenheiro de IA Generativa  –  TK Technologies  |  Curitiba, PR (Híbrido)     Fev 2026 – Atual · Contrato
```

Bullets:

```text
• Projetou o OrbitAI, uma plataforma de CRM de IA omnichannel (WhatsApp, Instagram, Facebook, Telegram e e-mail) com governança de acesso (RBAC), rastreamento de Meta/Google Ads e auto-respostas por LLMs, realizando deploy no Azure Container Apps com Bicep IaC.
• Desenvolveu pipeline de web scraping em Python coletando dados de preço e metadados de mais de 10 sites de peças automotivas, gerando inteligência competitiva de mercado em escala.
• Projetou workflows de automação com IA no n8n (ETL, RPA e agentes chatbot) integrando LLMs (Claude AI, Google AI Studio) e APIs do GCP (Sheets, Drive) para enriquecer dados e reduzir trabalho manual de análise.
• Desenvolveu chatbot de IA conversacional permitindo que usuários de negócio consultassem e refinassem datasets de preço por linguagem natural, reduzindo o tempo de obtenção de insights.
• Coordenou sprints de entrega no Notion, demos para clientes, treinamento de produto, apoio comercial e suporte pós-lançamento; contribui para a presença web da TK e para o desenvolvimento e manutenção contínuos do produto CRM.
```

Keep Spacecom / wDiscover / Itaeté metrics as already published on the PT Doc.

### Projetos de Destaque

Remove the Snowflake/dbt personal project. Keep three entries:

```text
OrbitAI — CRM de IA Omnichannel  ·  NestJS, Next.js, PostgreSQL, LLMs, APIs de Meta/Google Ads, Azure Container Apps, Docker  ·  TK Technologies – Jun 2026 – Atual
• Desenvolveu o OrbitAI, um CRM omnichannel seguro que centraliza WhatsApp, Instagram, Facebook, Telegram e e-mails em uma caixa de entrada unificada com controle de acesso baseado em funções (RBAC).
• Conectou dados de desempenho de Meta e Google Ads e uma camada de LLMs (Claude/Google AI Studio) para auto-respostas, mensagens outbound e análise automatizada de campanhas.

Buscador de Preços de Peças  ·  Python, FastAPI, Celery, Playwright, Redis, PostgreSQL, n8n, Azure, Bicep  ·  TK Technologies – Fev 2026 – Atual
• Construiu um buscador de preços de peças em mais de 10 sites, com pesquisa paralela de preços públicos e estoque interno, relatórios auditáveis e notificações em serviços conteinerizados no Azure.
```

Keep the IoT lakehouse project.

### Licenças & Certificações

```text
• AI for Writing and Communicating — Google (ID da Credencial: HE8YE5IS7WVW) · Jul 2026
• AI for Research and Insights — Google (ID da Credencial: 4PZDF3XQOF55) · Jul 2026
• AI for Brainstorming and Planning — Google (ID da Credencial: 7SFW2HGOKIU5) · Jul 2026
• AI Fundamentals — Google (ID da Credencial: UKBGM0AZUIS2) · Jul 2026
```

---

## 3. After both Docs look aligned

1. Confirm EN and PT are 2 pages, skills table has 7 rows, and section headings are not inside the table.
2. Tell the agent to run:

```bash
python3 docs/resume/scripts/sync-from-google-docs.py
```

3. That command updates `docs/resume/word/`, `docs/resume/source/`, `docs/resume/pdf/`, and copies PDFs to `assets/files/cv/`.

Until then, local Word previews are generated from markdown with:

```bash
docs/resume/.venv/bin/python docs/resume/scripts/build-word.py
```

Public site PDFs must come from the Google Docs export, not from `build-basic-pdf.py`.
