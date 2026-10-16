---
name: meta_income_skill
description: Manage money/income skills via skill_manage.
category: personal-finance
author: Hermes Agent
date: 2026-09-16
---

# Meta Income Skill

Metaskill that helps manage money‑income skills: create, list, patch, or delete skills such as `quick-money-passive-income`, `web_money`, `clipping-for-income`, and `income-plan`.

## Usage

Invoke through the `skill_manage` tool or `/skills` slash‑commands:

- List: `/skills list --category personal-finance`
- Create: `/learn <source>` or `skill_manage(action='create', ...)`
- Patch: `skill_manage(action='patch', ...)`
- Delete: `skill_manage(action='delete', ...)`

Always check `skills.write_approval` before creating skills.

## Subskills Under This Metaskill

- `biz_ideas` — business idea catalog (flipping, AI agents, white-label SaaS, passive income)
- `biz_tools` — open-source repo replacements for paid SaaS (PostHog, Chatwoot, Typebot, Voice Studio, Hindsight, NewsJack, Jev)
- `biz_service1` — step-by-step plan for AI Agent Service Business (#10 in `biz_ideas`), fully refactored with `biz_tools` costs, timelines, and cross-sell options. Includes POC development plan (local vet clinic demo) with milestone phases 0–5, progress tracker, and GitHub push procedure.

### POC / Demo Workflow (Added)

When building a local demo for a business offering (e.g., vet clinic agent), use the `biz_service1` POC structure: workspace at `/home/shiva/poc-vet-agent/`, `docs/poc_progress.md`, `README.md`, and commit milestones to a public repo (`poc-vet-agent`) using `gh` auth with `GH_TOKEN`. Never embed tokens in chat or files; pass via environment variable (`export GH_TOKEN=...`). If `gh auth login --with-token` hangs (common on headless Linux), fall back to writing `~/.config/gh/hosts.yml` directly and using `gh auth status` + `gh auth setup-git` before pushing.
- `quick-money-passive-income` — base passive-income guide
- `web_money` — fastest online income in Ireland
- `clipping-for-income` — zero-cost clipping hustle
- `income-plan` — premium security advisory services

## How to Drill Down

Use `/skills` or `skill_view(name='biz_service1')` to open any subskill. Within `biz_service1`, the 10 sections (Offer, Investment, Timeline, Tools, Skills, Customer Acquisition, Probability, Viability Exercise, Integration, Bottom Line) are structured for direct reference — ask specific questions (e.g., “what’s the 2-week exercise?” or “which tools reduce SaaS cost?”) and the content is already organized to answer them.

*Prepared by Hermes Agent – 2026-09-16*
