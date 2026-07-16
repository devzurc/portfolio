# Weekly progress log

> One entry per week. Format: **build, measure, explain, harden**.

---

## Week of 2026-06-24

**Monday — measurable improvement chosen:**  
Stand up `docs/career/goals/` roadmap system and wire it into career knowledge, job strategy, and agent skills.

**Tuesday–Wednesday — implemented:**  
- Created goals folder: roadmap, skill matrix, projects pipeline, job applications tracker  
- Integrated AI Platform Specialist positioning into job strategy and portfolio hooks  
- Fixed audit issues: CDP URL, CV source-of-truth, agent rules migration, SEO/a11y polish  

**Thursday — evaluate/observe:**  
- N/A (infrastructure week)

**Friday — technical note:**  
Senior AI hiring signal in 2026 is production systems over enterprise data — RAG with eval gates, agent orchestration with human approval, MCP with threat models — not framework breadth. The goals system exists to make that proof trackable and CV/portfolio-synced.

**Weekend — polish:**  
- Begin `raw-llm-systems` repo (July milestone)

---

## Week of 2026-07-01

**Monday — measurable improvement chosen:**  
Upskill in AI fundamentals and application patterns (Writing/Communicating, Research/Insights, Brainstorming/Planning) using Google's official curriculum.

**Tuesday–Wednesday — implemented:**  
- Completed 4 Google AI certifications (AI Fundamentals, AI for Writing, AI for Research, AI for Brainstorming) on Coursera / CIEE.

**Thursday — evaluate/observe:**  
- Verified all credentials and earned official Credly badges, mapping them to the profile `credly.com/users/devzurc`.

**Friday — technical note:**  
Structuring prompts and using models for business operations requires understanding specific cognitive tasks (like synthesis vs ideation). Google's framework on constraints and evaluation helps build better prompt libraries.

**Weekend — polish:**  
- Mapped out credential verification metadata (IDs and URLs) for the portfolio and CV additions.

---

## Week of 2026-07-08

**Monday — measurable improvement chosen:**  
Architect a production-ready, multi-channel messaging API replacing disjointed runtimes with a NestJS/Next.js/PostgreSQL system.

**Tuesday–Wednesday — implemented:**  
- Built the NestJS webhook API for Meta Cloud (WhatsApp, Instagram, Messenger).
- Created PostgreSQL schemas and functions for customer interaction & cooldowns.
- Deployed containerized services on Azure Container Apps using Bicep.

**Thursday — evaluate/observe:**  
- Ran concurrency tests on PostgreSQL webhook logging; confirmed signature validation blocks replay attacks; verified n8n rollback integration works.

**Friday — technical note:**  
Meta Cloud webhooks require immediate 200 OK responses to avoid webhook disabling. Moving state logic to DB triggers and background worker loops in PostgreSQL ensures the API remains highly responsive and avoids message loss under peak traffic.

**Weekend — polish:**  
- Built the Next.js marketing CRM agent inbox dashboard, filtering leads, managing tickets, and enabling agent outbound messaging via Graph API.

---

## Week of 2026-07-15

**Monday — measurable improvement chosen:**  
Perform a mega-update session to sync the new CRM platform, 4 Google AI badges, and Credly profile across all career documentation, CVs (EN/PT), and the portfolio site.

**Tuesday–Wednesday — implemented:**  
- Paired EN/PT CV markdown updates, cover letters, and job strategy docs.
- Integrated new project card and responsive glassmorphic AI badge cards in `index.html` / `sections.css`.
- Added Credly contact CTA and synced agent docs/roadmap files.

**Thursday — evaluate/observe:**  
- Validated bilingual block counts (exact parity), tested external cert links, verified mobile responsive layout grid collapse, and ran local CV compilation scripts (PDF + Word).

**Friday — technical note:**  
Keeping a dual-language static site in sync with resumes and project metadata requires a structured evidence pipeline. When canonical markdown files update, automated python compilers ensure local site assets stay aligned instantly, preventing manual layout regressions.

**Weekend — polish:**  
- Push changes to staging, perform visual inspection, prepare CV paste changes for Google Docs, and execute final git commit.

---

## Template (copy for future weeks)

```markdown
## Week of YYYY-MM-DD

**Monday — measurable improvement chosen:**  
<one specific system improvement>

**Tuesday–Wednesday — implemented:**  
- <what shipped>

**Thursday — evaluate/observe:**  
- <metrics, traces, eval scores, cost>

**Friday — technical note:**  
<one paragraph — what you learned and why it matters>

**Weekend — polish:**  
- <portfolio, docs, or light tool comparison>
```
