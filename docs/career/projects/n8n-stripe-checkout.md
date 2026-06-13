---
repo: n8n-stripe-checkout
github_url:
mirror_url:
visibility: private
status: active
period: 2025 - ongoing
period_note: "TK Technologies contract/checkout automation work; implementation and docs tracked as part of Stok IA lifecycle systems."
employer: TK Technologies
role: Automation engineer - Stripe webhook fulfillment, n8n workflow design, transactional email templates
domains: [saas, e-commerce, automation, private-client-automation]
stack:
  - n8n
  - Stripe API
  - Gmail API
  - n8n Data Tables
  - HTML email templates
  - Node.js
  - Webhooks
portfolio_worthy: true
cv_worthy: true
verified_outcomes:
  - Paid checkout webhook fulfillment with template selection and branded email delivery
  - Idempotent event logging and retry-aware audit trail in n8n-managed tables
  - Git-tracked workflow export plus SPEC/WORKFLOW docs for AI-assisted maintenance
links:
  demo:
  docs:
last_synced: 2026-06-12
source_readme: readmes/n8n-stripe-checkout.md
related_projects: [n8n-clerk-followup]
product: Stok IA / TK Technologies
repo_access: "Private/sanitized; no public repository link."
---

# n8n Stripe Checkout Fulfillment

> Private checkout automation - paid Stripe checkout events, product context enrichment, template selection, branded Gmail delivery, and audited outcomes.

## One-liner

Production n8n workflow that turns paid Stripe checkouts into branded transactional emails for Stok IA/TK products, with template-driven content and idempotent event logging.

## Problem

After checkout, customers need immediate on-brand confirmation emails with correct product and line-item context, while operations need reliable auditability and duplicate-send protection.

## What I built

- Stripe checkout webhook fulfillment flow for paid sessions
- Stripe line-item enrichment before message rendering
- Template lookup and rendering from n8n-managed content tables
- Gmail API delivery for branded HTML transactional emails
- Event audit log, validation docs, and release checklist for maintainable ops

## Architecture

```text
Paid Stripe checkout event
  -> n8n validation
  -> Stripe line-item enrichment
  -> template selection
  -> Gmail HTML delivery
  -> event audit log
```

## Stack (verified)

n8n - Stripe API - Gmail API - n8n Data Tables - HTML templates - Node.js validation scripts - Webhooks

## Outcomes

- Automated post-checkout email fulfillment for TK/Stok IA products
- Maintainable automation package with workflow exports, specs, checkpoints, and changelog
- Strong CV proof point for n8n integration engineering and SaaS lifecycle automation

## Evidence

- Repository: private client/internal repo and sanitized mirror, not linked in public portfolio
- Sanitized README snapshot: `readmes/n8n-stripe-checkout.md`

## Notes for AI / alignment

- CV-worthy as a concise private-client automation project
- Pair with the Clerk trial follow-up automation for a full acquisition/activation lifecycle story
- Public copy must not expose webhook URLs, table IDs/names, env-var names, git remotes, or private repo links
