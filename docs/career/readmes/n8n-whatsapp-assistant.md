# n8n WhatsApp Assistant

<!-- sanitized private project snapshot, created 2026-06-13 -->

Private TK Technologies WhatsApp intake automation using n8n and Evolution API.

## Summary

The workflow receives WhatsApp message events, normalizes inbound customer messages, records customer/request state, sends first-contact welcome replies when appropriate, and routes actionable needs to staff notification handling.

## Public-safe capabilities

- WhatsApp event intake through Evolution API webhooks
- Message normalization for channel, sender, thread, text, timestamp, and message type
- Customer need classification for sales, support, scheduling, billing, and general requests
- Database-backed interaction recording and request handoff state
- First-contact welcome replies with human-friendly message variation
- Staff notification path with fallback behavior
- Webhook acknowledgement for provider reliability

## Public-safe stack

n8n, Evolution API, WhatsApp automation, Webhooks, PostgreSQL, Slack notification path, JavaScript code nodes.

## Privacy note

The original workflow and execution data are private. Do not publish workflow IDs, webhook paths, endpoint URLs, phone numbers, instance names, tokens, database function names, environment variables, customer identifiers, or private repository links.
