# Nox TKTech Telegram Assistant (sanitized README snapshot)

Private TK Technologies conversational AI automation. This career copy intentionally omits workflow IDs/names, version IDs, table IDs/names, env-var names, API endpoints, sample commands, personal email addresses, operator git commands, and private repository links.

## Scope

- Receive Telegram messages in n8n and normalize text, caption, and metadata.
- Detect language and local time period for Portuguese-first responses.
- Debounce rapid message bursts with Redis before sending a combined request to the agent.
- Log users, conversations, inbound/outbound messages, knowledge lookups, handoff states, and workflow errors in n8n-managed tables.
- Retrieve answers from curated internal knowledge only, with no internet search.
- Use a Grok-backed n8n LangChain agent and a controlled fallback/handoff path.
- Trigger private CDP demo jobs for automotive workflows through secured internal APIs.

## Verified Work

- Production Telegram workflow was active and had successful webhook executions when checked in May 2026.
- Pinned workflow tests covered known-answer and fallback paths without requiring live model calls or live Telegram sends.
- The local workflow export remained the canonical review artifact for production changes.

## Public-Safe Maintenance Notes

- Keep workflow identifiers, table names/IDs, environment variable names, API endpoints, sample command strings, and test execution numbers out of public portfolio content.
- Present this as a private Gen. AI chatbot and automation integration project.
- CV-worthy as conversational AI work for business users querying product/pricing knowledge, especially when paired with the CDP platform.
