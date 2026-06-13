# n8n Clerk Trial Follow-up (sanitized README snapshot)

Private TK Technologies/Stok IA automation. This career copy intentionally omits live webhook URLs, workflow IDs, table IDs/names, env-var names, email addresses, operational commands, and private repository links.

## Scope

- Receive Clerk/Svix trial lifecycle events in n8n.
- Maintain idempotent lifecycle state and audit logs in n8n-managed tables.
- Render branded welcome, nurture, upgrade, expiration, and fallback email templates.
- Send branded transactional email through Gmail API raw MIME.
- Run scheduled follow-up checks for trial users that need lifecycle communication.

## Verified Work

- Workflow and table resources were created and validated through n8n maintenance tooling.
- Email template snapshots were synced between local source files and n8n-managed content storage.
- Proof batches covered welcome, duplicate welcome, upgrade, missing email, update, follow-up, expiration, invalid trial start, and renderer paths.
- Production readiness notes tracked Gmail credential binding, Clerk/Svix production configuration, cutover verification, and approval gates.

## Public-Safe Maintenance Notes

- Keep exact webhook paths, live hostnames, workflow IDs, table names/IDs, sender addresses, and personal test inboxes out of public career materials.
- Describe this as private SaaS lifecycle automation unless a sanitized demo is created.
- Reference it as supporting evidence for n8n + SaaS lifecycle work, not as a public repository.
