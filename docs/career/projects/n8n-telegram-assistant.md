---
repo: n8n-telegram-assistant
github_url:
mirror_url:
visibility: private
status: active
period: 2025 - ongoing
period_note: "TK Technologies contract/conversational AI work; production workflow verified in May 2026."
employer: TK Technologies
role: Gen. AI engineer - conversational Telegram bot with internal knowledge, LangChain agent, and CDP demo integration
domains: [gen-ai, chatbots, automotive-parts, customer-support, private-client-automation]
stack:
  - n8n
  - n8n LangChain Agent
  - xAI Grok
  - Telegram Bot API
  - Redis
  - n8n Data Tables
  - Python
  - FastAPI
portfolio_worthy: true
cv_worthy: true
verified_outcomes:
  - Production Telegram chatbot using curated internal knowledge only, with no web search
  - Redis message debounce/cache plus n8n-managed logs for users, conversations, messages, knowledge, and handoff states
  - Command-triggered automotive demo integrations with CDP scraper/demo APIs
  - MCP-validated workflow with pinned test coverage for known-answer and fallback paths
links:
  demo:
  docs:
last_synced: 2026-06-12
source_readme: readmes/n8n-telegram-assistant.md
related_projects: [cdp-hub]
cv_alignment: TK Technologies conversational AI chatbot bullet
repo_access: "Private/sanitized; no public repository link."
---

# Nox TKTech Telegram Assistant

> Private production Telegram chatbot for TK Technologies - internal knowledge answers, Grok-backed n8n agent, Redis debounce, and CDP demo triggers.

## One-liner

n8n-powered Telegram assistant that answers from curated internal knowledge, debounces multi-message input, logs conversations for audit, and can trigger automotive demo workflows through private CDP APIs.

## Problem

Prospects and users need quick, accurate Portuguese-first answers about TK/Stok products, with safe fallback to human handoff and optional live demo automation.

## What I built

- Telegram intake, message normalization, language/period detection, and Redis debounce
- n8n-managed logging for users, conversations, messages, knowledge, handoff, and errors
- Internal-knowledge retrieval with explicit no-web-search guardrails
- LangChain Agent node with Grok chat model and controlled fallback behavior
- Command-triggered integration with private CDP demo APIs for automotive workflows
- Spec-driven maintenance and MCP workflow validation before production changes

## Architecture

```text
Telegram message
  -> normalize + language/period detection
  -> Redis debounce/cache
  -> conversation + message audit logs
  -> optional private demo command route
  -> internal knowledge retrieval
  -> Grok-backed n8n agent
  -> fallback or Telegram reply
```

## Stack (verified)

n8n - LangChain Agent node - xAI Grok - Telegram Bot API - Redis - n8n Data Tables - Python validation - FastAPI CDP APIs

## Outcomes

- Active production workflow with successful webhook executions verified in May 2026
- Directly supports CV positioning around conversational AI for business users querying pricing/product knowledge
- Bridges Gen. AI chatbot work with data/automation engineering through CDP integrations

## Evidence

- Repository: private client/internal repo, not linked in public portfolio
- Sanitized README snapshot: `readmes/n8n-telegram-assistant.md`

## Notes for AI / alignment

- Top portfolio and CV asset for Gen. AI Engineer positioning
- Brazilian Portuguese is the primary user language; multilingual detection is included
- Public copy must not expose workflow IDs/names, table IDs/names, env-var names, API endpoints, sample commands, email addresses, or private repo links
