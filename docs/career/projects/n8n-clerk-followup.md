---
repo: n8n-clerk-followup
github_url:
mirror_url:
visibility: private
status: active
period: 2025 - ongoing
period_note: "TK Technologies contract/lifecycle work; automation milestones verified in May 2026. Engagement extended to 6 months, expected through Aug 2026."
employer: TK Technologies
role: Automation engineer - Clerk webhook lifecycle, trial email sequences, Gmail raw MIME, idempotency
domains: [saas, lifecycle-email, auth, private-client-automation]
stack:
  - n8n
  - Clerk
  - Svix webhooks
  - Gmail API
  - n8n Data Tables
  - Node.js
  - HTML email templates
portfolio_worthy: false
cv_worthy: false
verified_outcomes:
  - Clerk/Svix trial-event intake with idempotent lifecycle tracking
  - Scheduled follow-up workflow with template-driven delivery and audit logs
  - Branded transactional email delivery via Gmail API raw MIME
  - Proof batches validated across welcome, duplicate, upgrade, follow-up, expiration, and invalid-trial paths
links:
  demo:
  docs:
last_synced: 2026-06-12
source_readme: readmes/n8n-clerk-followup.md
related_projects: [n8n-stripe-checkout]
product: Stok IA
repo_access: "Private/sanitized; no public repository link."
---

# n8n Clerk Trial Follow-up

> Private Stok IA lifecycle automation - Clerk event intake, templated follow-up sequences, idempotent logging, and branded email delivery.

## One-liner

Production n8n automation that turns Clerk trial lifecycle events into audited welcome, nurture, and expiration email sequences without duplicate sends.

## Problem

Stok IA free trials need timely lifecycle communication after signup and trial-state changes, with branded sender identity and guardrails against duplicate or out-of-order emails.

## What I built

- Clerk/Svix event receiver for trial lifecycle events
- Idempotent user lifecycle tracking and audit logging in n8n-managed tables
- Scheduled follow-up workflow for welcome, nurture, expiration, and upgrade paths
- Template sync and rendering pipeline for branded HTML email content
- Operational docs for architecture, workflow changes, checkpoints, and release readiness

## Architecture

```text
Clerk/Svix lifecycle event
  -> n8n receiver
  -> lifecycle state + template lookup + audit log
  -> Gmail API raw MIME delivery

Scheduled follow-up
  -> due-trial selection
  -> template render
  -> send + audit result
```

## Stack (verified)

n8n - Clerk - Svix - Gmail API raw MIME - n8n Data Tables - Node.js - HTML email templates

## Outcomes

- Automated trial email lifecycle for Stok IA
- Validated idempotency and renderer paths through pinned workflow tests
- Complements the Stripe checkout fulfillment project as part of the acquisition lifecycle

## Evidence

- Repository: private client/internal repo, not linked in public portfolio
- Sanitized README snapshot: `readmes/n8n-clerk-followup.md`

## Notes for AI / alignment

- Good portfolio support for n8n + SaaS lifecycle automation
- Not a standalone CV line by default; fold into Stok IA automation work if space is tight
- Public copy must not expose webhook URLs, workflow IDs, table IDs/names, email addresses, env vars, or private repo links
