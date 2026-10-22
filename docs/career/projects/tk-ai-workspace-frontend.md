---
repo: tk-ai-workspace-frontend
github_url:
visibility: private
status: private-evidence
period: 2026-08 – ongoing
employer: TK Technologies
role: Frontend engineer — Figma implementation and API integration on an existing Node.js product
domains: [gen-ai, saas, frontend]
stack:
  - React 18
  - TypeScript
  - Vite 5
  - Tailwind CSS
  - React Router 6
  - Zustand
  - Clerk
  - Vitest
  - ESLint
portfolio_worthy: false
cv_worthy: false
verified_outcomes: []
links:
  demo:
  docs:
last_synced: 2026-10-21
public_safety: Product name, hostnames, Figma file keys, customer identifiers, and internal routes stay out of CV, portfolio, and cover letters. Work-experience wording is the sanitized TK bullet approved 2026-10-21.
---

# TK AI workspace frontend

> Private evidence for the current TK product UI. Not a portfolio card and not a CV notable project.

## One-liner

Product frontend built from Figma and connected to an existing Node.js API for workspace-scoped AI features.

## Problem

The product needed a recruiter-invisible, in-house UI: screens implemented from design frames, then wired to a backend owned by another engineer, without hard-coding entitlements or content catalogs.

## What I built

Evidence is Lucas Cruz / lucas-devzurc commits from 2026-08-19 through 2026-10-21 (about 122 commits), concentrated in `Frontend/src`. Backend, release, and infrastructure ownership stays with the tech lead.

- **Home shell from Figma:** Sidebar, collapsed rail, composer, menus, notifications, and conversation move/delete, plus image mode, deep-research suggestions, and artifact mode. Frames are treated as implementation contracts, with a screen registry, source audits, and preview fixtures.
- **Learning hub and prompt-pack studio:** Hub and lesson page read the catalog from the API only. Pack and case screens load the workspace grant and can place a case into the conversation flow.
- **Feature-interest gate:** Shared “not active in this workspace yet” entry for the learning hub, the prompt-pack studio, and corporate memory. The client records view, click, and interest through the session and workspace header.
- **API facade:** Native `fetch` behind a domain-split client (chat stream, conversations, projects, workspaces, integrations, notifications, and the newer content and interest clients). Clerk session plus workspace scope. Pack and trail ids are not hard-coded.

Approved public bullets (product name omitted):

- Built the product frontend in React, TypeScript, Vite, and Tailwind from Figma, including the home shell, image and artifact modes, a learning hub, and a prompt-pack studio.
- Connected those screens to an existing Node.js API for workspace entitlements, content catalogs, and feature-interest tracking, using Clerk sessions and workspace-scoped requests.
- Kept delivery on short-lived Scrum branches with typecheck, production build, and visual source audits before review.

The CV and portfolio use one combined TK-role bullet so the role stays within five bullets. They do not add a notable project or a portfolio card.

## Architecture

```text
Figma frame contract
  --> React 18 + Vite + TypeScript feature modules
  --> apiService (fetch, Clerk session, workspace header)
  --> existing Node.js / Express API (tech lead)
  --> workspace-scoped content, entitlements, and interest events
```

The running product also serves the compiled frontend and API from one container, with document storage, realtime sockets, and several model providers. Those layers are surrounding platform context. They are not claimed as this frontend role.

## Stack (verified)

React 18 · TypeScript · Vite 5 · Tailwind CSS · React Router 6 · Zustand · Clerk · native fetch · Vitest · ESLint

Playwright is available for browser checks. Delivery uses one Scrum ticket, one short branch, and a pull request into the integration branch after CI (quality, build, secret scan, PR title, dependency audit) and tech-lead review.

## Outcomes

No public metric is verified. Do not invent screen counts, user counts, or latency numbers.

## Evidence

- Local private checkout reviewed 2026-10-21. This portfolio repo does not mirror the private README.
- Commit window: 2026-08-19 through 2026-10-21, authors Lucas Cruz and lucas-devzurc.
- Main paths: `Frontend/src/features/home`, `features/estudio`, `features/imersao`, `Frontend/src/lib/api`, plus a small set of backend files for plan access, pack loading, and the interest client.

## Notes for AI / alignment

- Internal product name stays off public copy, including CV markdown, `index.html`, cover letters, and structured data.
- `cv_worthy: false` means no Notable Project. The sanitized bullet belongs on the TK Technologies work-experience entry only.
- `portfolio_worthy: false`. Do not add a project card.
- Skills justified by this work: React, Vite, Tailwind CSS. Next.js and NestJS remain CRM evidence, not this product.
- Do not claim the multi-model orchestrator, agent loop, retrieval layer, database, or cloud deploy as this role.
- Radix / shadcn are named in internal conventions and are not frontend package dependencies. Leave them off the skills row.
