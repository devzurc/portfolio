# Google Docs CV update — 2026-07-16

Use this to update the canonical Google Docs CVs before running `docs/resume/scripts/sync-from-google-docs.py`.

---

## 1. English CV Updates (EN)

**Document Link:** https://docs.google.com/document/d/1O4YsNWyfANs_332ecNZ8fgf-wclyuJCjZpO0LBqX2S8/edit

### Professional Summary (Replacement)

Replace the existing Professional Summary block with:

```text
Senior Data Engineer and Gen. AI Automation Engineer with 5+ years of experience building production data pipelines, cloud lakehouses, and LLM/n8n automation across IoT, fintech, agribusiness, and automotive intelligence. Proven track record delivering end-to-end data platforms, governed analytics datasets, conversational AI workflows, automated reporting systems, and customer-facing product implementation. Building a public portfolio of production AI platform systems (RAG, agents, evaluation, MCP, observability) over enterprise data through 2026. Fluent in English (C1); open to relocation across Europe.
```

### Technical Skills (Integrations)

- Add `NestJS` and `Next.js` to **Data Engineering, APIs & Orchestration**.
- Add `Meta Cloud API` to the end of the list in **Data Engineering, APIs & Orchestration**.

### Work Experience — TK Technologies Bullets (Add to top of list)

Insert this bullet at the top of the TK Technologies list:

```text
- Architected a multi-channel CRM platform (WhatsApp, Instagram, Messenger) using NestJS, Next.js, and PostgreSQL logic, deploying to Azure Container Apps with Bicep IaC.
```

### Notable Projects (Add new entry at top)

Add this entry at the top of the Notable Projects section:

```text
### WhatsApp CRM & Automation Platform

*NestJS, Next.js, PostgreSQL, n8n, Azure Container Apps, Meta Cloud API, Docker · TK Technologies – Jun 2026 – Present*

- Developed a production CRM receiving Meta Cloud API webhooks for WhatsApp, Instagram, and Messenger; integrated dynamic welcome/cooldown flows via PostgreSQL and Next.js agent inbox. Deployed on Azure ACA.
```

Also, add the **AI Platform Engineering Portfolio** entry at the bottom of Notable Projects:

```text
### AI Platform Engineering Portfolio (in progress — 2026)

*FastAPI · PostgreSQL/pgvector · LangGraph · MCP · RAGAS · Docker · OpenTelemetry*

- Building public, production-grade AI systems over enterprise data: RAG with hybrid retrieval and evaluation gates, LangGraph agent orchestration with human approval, MCP tool servers, and observability. Milestones shipping Jul–Dec 2026 on github.com/devzurc.
```

### Licenses & Certifications (Add to bottom)

Append the following Google/Coursera certifications to the bottom of the section:

```text
- AI for Writing and Communicating — Google (Credential ID: HE8YE5IS7WVW) · Jul 2026
- AI for Research and Insights — Google (Credential ID: 4PZDF3XQOF55) · Jul 2026
- AI for Brainstorming and Planning — Google (Credential ID: 7SFW2HGOKIU5) · Jul 2026
- AI Fundamentals — Google (Credential ID: UKBGM0AZUIS2) · Jul 2026
```

---

## 2. Portuguese CV Updates (PT)

**Document Link:** https://docs.google.com/document/d/1oi8mzTJNNTu3CdSuqEgiWCPmiyvGWxrsstU93K0QV0Q/edit

### Resumo Profissional (Replacement)

Replace the existing Resumo Profissional block with:

```text
Engenheiro de Dados Sênior e Engenheiro de Automação com IA Generativa com mais de 5 anos de experiência construindo pipelines de dados em produção, lakehouses em nuvem e automações com LLMs/n8n. Atuação comprovada em IoT, fintechs, agronegócio e inteligência automotiva utilizando AWS, Azure e GCP, com implementação de produto voltada a clientes. Construindo portfólio público de plataformas de IA em produção (RAG, agentes, avaliação, MCP, observabilidade) sobre dados empresariais ao longo de 2026. Inglês fluente (C1); disponível para realocação na Europa.
```

### Competências Técnicas (Integrations)

- Add `NestJS` and `Next.js` to **Engenharia de Dados, APIs & Orquestração**.
- Add `Meta Cloud API` to the end of the list in **Engenharia de Dados, APIs & Orquestração**.

### Experiência Profissional — TK Technologies Bullets (Add to top of list)

Insert this bullet at the top of the TK Technologies list:

```text
- Projetou uma plataforma de CRM multi-canal (WhatsApp, Instagram, Messenger) usando NestJS, Next.js e lógica de negócio em PostgreSQL, realizando deploy no Azure Container Apps com Bicep IaC.
```

### Projetos de Destaque (Add new entry at top)

Add this entry at the top of the Projetos de Destaque section:

```text
### Plataforma CRM & Automação WhatsApp

*NestJS, Next.js, PostgreSQL, n8n, Azure Container Apps, Meta Cloud API, Docker · TK Technologies – Jun 2026 – Atual*

- Desenvolveu um CRM em produção para processamento de webhooks oficiais da Meta Cloud API (WhatsApp, Instagram, Messenger) integrado a fluxos de auto-reply/cooldown em PostgreSQL e inbox de agentes em Next.js. Deploy via ACA.
```

Also, add the **Portfólio de Engenharia de Plataforma de IA** entry at the bottom of Projetos de Destaque:

```text
### Portfólio de Engenharia de Plataforma de IA (em andamento — 2026)

*FastAPI · PostgreSQL/pgvector · LangGraph · MCP · RAGAS · Docker · OpenTelemetry*

- Construindo sistemas públicos de IA em produção sobre dados empresariais: RAG com recuperação híbrida e gates de avaliação, orquestração de agentes com LangGraph e aprovação humana, servidores MCP e observabilidade. Marcos previstos Jul–Dez 2026 em github.com/devzurc.
```

### Licenças & Certificações (Add to bottom)

Append the following Google/Coursera certifications to the bottom of the section:

```text
- AI for Writing and Communicating — Google (ID da Credencial: HE8YE5IS7WVW) · Jul 2026
- AI for Research and Insights — Google (ID da Credencial: 4PZDF3XQOF55) · Jul 2026
- AI for Brainstorming and Planning — Google (ID da Credencial: 7SFW2HGOKIU5) · Jul 2026
- AI Fundamentals — Google (ID da Credencial: UKBGM0AZUIS2) · Jul 2026
```

---

## 3. After Updating Google Docs

Once you have manually pasted the above text blocks into both Google Docs, run:

```bash
python3 docs/resume/scripts/sync-from-google-docs.py
```

This will download the canonical outputs (.pdf, .docx, .txt) and copy the updated PDFs to `assets/files/cv/` for live site downloads.
