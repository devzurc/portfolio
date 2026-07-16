---
repo: whatsapp-automation-platform
github_url: https://github.com/devzurc/whatsapp-automation-platform
visibility: private
status: active
period: 2026-06 - ongoing
employer: TK Technologies
role: Full-stack Engineer / Architect
domains: [saas, crm, messaging, automation]
stack: [NestJS, Next.js, PostgreSQL, n8n, Azure Container Apps, Meta Cloud API, WhatsApp, Instagram, Messenger, Docker, Bicep, pnpm]
portfolio_worthy: true
cv_worthy: true
verified_outcomes: []
links:
  demo:
  docs:
last_synced: 2026-07-16
---

## One-liner

Production-oriented platform for official Meta channels automation (NestJS API + CRM worker + PostgreSQL) and a marketing CRM dashboard (Next.js) for agent inbox management.

## Problem

Replacing legacy runtime and fragmented flows with a unified, high-reliability platform to manage official WhatsApp, Instagram, and Messenger messaging streams, coordinate agent handoff, and implement reliable customer auto-replies without message loss or race conditions.

## What I built

- **Meta Cloud API Webhook Handlers:** Developed NestJS endpoint infrastructure to securely ingest webhooks for WhatsApp, Instagram, and Messenger.
- **Durable Event Storage:** Integrated PostgreSQL to store raw webhook payloads, verifying signatures and ensuring idempotency.
- **Stateful Conversation Engine:** Authored DB functions (`record_customer_interaction`) to govern welcome message cooldowns (12h/24h) and trigger support routing.
- **CRM Agent Inbox:** Created a Next.js interface allowing multiple agents to view conversations, filter leads, and send outbound messages via Graph API.
- **Azure IaC Deployment:** Containerized the services (Docker) and deployed via Azure Container Apps using modular Bicep templates.

## Architecture

```text
Customer Messaging (WA/IG/FB) 
  --> Meta Webhook 
  --> NestJS API (CRM API) 
  --> PostgreSQL (durably ingest & decide action) 
  --> CRM Worker 
  --> Meta Graph API 
  --> Customer Response
```

## Stack (verified)

- NestJS, Next.js, Node.js, pnpm
- PostgreSQL, Prisma/SQL queries
- n8n (retained as inactive rollback path)
- Azure Container Apps, Azure Bicep, Docker
- Meta Graph APIs (WhatsApp Cloud API, Instagram Graph API)

## Outcomes

- Delivered a robust, containerized multi-tenant inbox dashboard eliminating reliance on multiple third-party integration runtimes.
- Built a secure webhook validation layer preventing replay attacks.
