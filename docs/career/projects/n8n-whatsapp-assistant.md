---
repo: n8n-whatsapp-assistant
github_url:
mirror_url:
visibility: private
status: active
period: 2026
period_note: "TK Technologies WhatsApp intake automation; workflow and successful webhook executions verified from sanitized local evidence in June 2026. Engagement extended to 6 months, expected through Aug 2026."
employer: TK Technologies
role: Automation engineer - WhatsApp/Evolution API intake, message normalization, customer request logging, welcome replies, staff notifications
domains: [customer-support, sales-intake, whatsapp, private-client-automation]
stack:
  - n8n
  - Evolution API
  - WhatsApp automation
  - Webhooks
  - PostgreSQL
  - Slack
  - JavaScript
portfolio_worthy: true
cv_worthy: false
verified_outcomes:
  - Active n8n webhook workflow receiving WhatsApp message events through Evolution API
  - Message normalization for sender, thread, message type, text, timestamp, first-contact state, and customer need category
  - Audited customer interaction recording for users, contacts, messages, workflow runs, and request handoff state
  - First-contact welcome replies and staff notification path with fallback when staff messaging is unavailable
links:
  demo:
  docs:
last_synced: 2026-06-13
source_readme: readmes/n8n-whatsapp-assistant.md
related_projects: [n8n-telegram-assistant, n8n-instagram-assistant]
repo_access: "Private/sanitized; no public repository link."
---

# n8n WhatsApp Assistant

> Private WhatsApp intake automation for TK Technologies - Evolution API webhook intake, customer message normalization, audited request logging, first-contact welcome replies, and staff notification routing.

## One-liner

Production n8n workflow that receives WhatsApp messages through Evolution API, normalizes customer intent, records the interaction, sends a first-contact welcome when appropriate, and routes actionable requests to staff.

## Problem

Customer conversations arriving through WhatsApp need fast acknowledgement, structured intake, and an auditable handoff path so sales or support requests are not lost in manual chat handling.

## What I built

- WhatsApp webhook intake using Evolution API events
- Message normalization for sender identity, thread, message type, text, timestamp, and source channel
- Rule-based customer need classification for general, sales, support, scheduling, and billing intents
- Database-backed customer interaction recording and request state tracking
- First-contact welcome message generation with rotating human-friendly templates
- Staff notification routing with a safe fallback path when notification delivery is not configured
- Webhook acknowledgement path for reliable provider response handling

## Architecture

```text
WhatsApp message event
  -> Evolution API webhook
  -> n8n normalization and processing gate
  -> customer/contact/message/request audit record
  -> first-contact welcome or staff notification path
  -> webhook OK response
```

## Stack (verified)

n8n - Evolution API - WhatsApp automation - Webhooks - PostgreSQL - Slack notification path - JavaScript code nodes

## Outcomes

- Working WhatsApp intake workflow with successful webhook executions verified in June 2026
- Converts unstructured WhatsApp messages into auditable customer interaction records
- Supports both first-contact acknowledgement and staff handoff for messages with a clear customer need
- Strengthens the portfolio story around practical Gen. AI-adjacent automation, messaging channels, and customer operations

## Evidence

- Repository: private client/internal repo, not linked in public portfolio
- Sanitized README snapshot: `readmes/n8n-whatsapp-assistant.md`
- Local evidence: sanitized workflow metadata and execution snapshots reviewed on 2026-06-13

## Notes for AI / alignment

- Public copy must not expose workflow IDs, webhook paths, phone numbers, instance names, customer identifiers, endpoint URLs, database function names, environment variables, tokens, or private repo links.
- Present this as WhatsApp intake and operations automation rather than a fully autonomous AI agent unless a model-backed response path is later verified.
- Good portfolio support for recruiters and tech leads because it shows real-world messaging integration, event normalization, auditing, and operational handoff.
