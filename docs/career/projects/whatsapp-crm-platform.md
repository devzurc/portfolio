---
repo: whatsapp-crm-platform
github_url:
github_ref: devzurc/ORBITAI-CRM
visibility: private
status: active
period: 2026-06 - ongoing
employer: TK Technologies
role: Full-stack Engineer / Architect
domains: [saas, crm, messaging, automation, ai]
stack: [TypeScript, NestJS, Next.js, PostgreSQL, LLMs, Meta Ads API, Google Ads API, Meta Cloud API, Telegram API, Docker, Azure Container Apps, Azure Bicep, GitHub Actions CI/CD, pnpm, RBAC]
portfolio_worthy: true
cv_worthy: true
verified_outcomes: []
links:
  demo:
  docs:
last_synced: 2026-08-19
cv_alignment: Omnichannel AI CRM
---

## One-liner

An all-in-one Omnichannel AI CRM that centralizes messaging (WhatsApp, Instagram, Telegram, Facebook, Email), integrates Google/Meta Ads data, manages user roles, and uses LLMs for automated replies and marketing insights.

## Problem

Fragmented customer communications across multiple messaging apps and separate ad platform dashboards made it difficult to maintain a unified customer view, role-aware access, and shared campaign context.

## What I built

- **Omnichannel Inbox Hub:** Developed NestJS endpoint infrastructure to ingest webhooks and APIs from WhatsApp, Instagram, Messenger, Telegram, and Email into a single Next.js dashboard.
- **Ads Data Integration:** Connected Meta Ads and Google Ads APIs to pull live campaign metrics directly into the platform, allowing the marketing team to track lead acquisition.
- **Governance & Role-Based Access (RBAC):** Built strict access management controls so agents and managers only access chats, customer profiles, and ad data corresponding to their authorized roles.
- **LLM Automation Layer:** Implemented LLM orchestration (Claude / Google AI Studio) for initial customer auto-replies, outbound agent-message drafting, and campaign analysis support.
- **Azure IaC Deployment:** Containerized the services (Docker) and deployed via Azure Container Apps (ACA) using modular Bicep templates.
- **Current product contribution:** Building the new TK web presence and contributing to ongoing product development and maintenance across the CRM product ecosystem. The separate frontend product is curated in `projects/tk-ai-workspace-frontend.md`. Public copy uses that profile's sanitized TK bullet only.

## Architecture

```text
Customer Channels (WhatsApp/IG/FB/Telegram/Email)
  --> API Webhooks
  --> NestJS CRM Core API
  --> PostgreSQL DB (Access Control & Auditing)
  --> LLM Core (Auto-Reply & Ad Analysis)
  --> Next.js Unified Agent Dashboard (RBAC)
  --> Meta / Google Ads API (Marketing Insights)
```

## Stack (verified)

- NestJS, Next.js, Node.js, pnpm, PostgreSQL, Prisma
- Large Language Models (Claude AI, Google AI Studio)
- Meta Graph API (WhatsApp Cloud, Instagram Graph), Telegram Bot API, IMAP/SMTP
- Meta Ads API, Google Ads API
- Azure Container Apps, Azure Bicep, Docker

## Outcomes

<!-- TODO: confirm public-safe, measurable outcomes with owner. -->

## CI/CD (verified 2026-09-22, sanitized)

Checked on the private CRM hub. The workflow is a quality and security gate, not an automated production deploy.

- Runs on pull requests, pushes to `main`, and a weekly schedule.
- Gates include secret scanning, CodeQL, Semgrep, a high-level dependency audit, lint, API and web unit tests, a production build, shellcheck, and a Bicep compile of the CRM infrastructure template.
- A filesystem and IaC scanner fails the job on high and critical findings.
- Deployment evidence for CRM remains Docker images plus Azure Container Apps defined in Bicep. Do not describe this repo as having the same push-to-dev CD pipeline as CDP.

## Public-safe scope note

The owner confirmed current contributions to the new TK website, CRM work, and StokIA development and maintenance on 2026-08-19. The CRM product name is approved for public CV notable projects and the matching portfolio card. Do not expose StokIA, product internals, customer data, deployment identifiers, or private URLs.
