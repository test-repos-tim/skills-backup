---
name: biz_service1
description: AI Agent Service Business — detailed step-by-step plan with investment, timeline, tools, skills, outreach, probability, viability exercise, and cross-sell integration
category: personal-finance
author: Hermes Agent
date: 2026-09-16
related_skills: [meta_income_skill, biz_ideas, biz_tools]
---

# Biz Service 1 — AI Agent Service Business

This skill contains the complete, refactored step-by-step plan for the AI Agent Service Business (originally #10 in `biz_ideas`), now enriched with tool-stack intelligence from `biz_tools` (open-source repo alternatives) and the latest video from `hlOk-EFUITQ` (NewsJack + Jev).

## 1. The Offer (What You Sell)

- **Core product:** Managed AI agent service sold to local businesses/niche professionals at **$3,000–$5,000/month per customer**.
- **Agent handles:** One repetitive workflow — lead qualification, appointment booking, customer support triage, or invoice chasing — via web chat, WhatsApp, SMS, or voice.
- **Refactored offer now includes tool-stack consulting add-ons:**
  - PostHog analytics setup ($500 one-time)
  - Chatwoot + AI reply bot ($800 one-time)
  - Cal.diy + Autumn billing ($600 one-time)
  - Typebot lead-funnel ($700 one-time)
  - Voice Studio TTS ($400 one-time)
  - Hindsight memory upgrade ($600 one-time)
  - NewsJack PR setup ($400 one-time)
  - Jev lead scoring ($300 one-time)
- **Effective revenue per customer:** $5K/month retainer + $3,700–$4,300 in one-time setup consulting on first engagement.

## 2. Investment Required

| Category | Upfront Cost | Ongoing Monthly Cost |
|----------|--------------|----------------------|
| Agent stack (Hermes + Claude Code) | $0 | $0 |
| LLM API + Jev decision calls | $0 | $50–$150 |
| Self-hosted tools stack (PostHog, Chatwoot, Typebot, Frappe CRM, Mautic, Invoice Ninja, Cal.diy, Autumn, Voice Studio, Hindsight) | $0 | ~$20 (VPS only) |
| Domain + website | $20–$50 | $15–$30 |
| VPS (Hostinger) | $0 | $3–$10 |
| Legal (LLC, contract template) | $0–$300 | $0 |
| **Total upfront** | **~$20–$370** | **~$85–$210** |

*Compared to original plan ($115–$530/mo SaaS fees), self-hosting drops recurring tooling cost to ~$85–$210/mo — roughly 70–80% lower.*

**Time investment:** 30–60 hours to build MVP + first customer (reduced from 40–80 because Docker-compose repos are deployed from `biz_tools` rather than built from scratch).

## 3. Timeline to Profitability

| Phase | Duration | Milestone |
|-------|----------|-----------|
| Build MVP agent + tool stack | 1–2 weeks | Working prototype on Hostinger VPS with Hindsight memory + Typebot qualification |
| Outreach & first customer | 3–6 weeks | Signed contract, first $3–$5K retainer + setup fee |
| Break-even | Month 2 | Revenue covers tooling + your time |
| Scale to 3–5 customers | Months 3–6 | $10K–$25K/month recurring + setup fees |
| Semi-passive | Months 6–12 | Agent runs with Hindsight memory + minimal oversight |

**Realistic first profit:** Month 2 (often Month 3 if sales cycle is slow).

## 4. Tools Needed

| Tool | Source | Role |
|------|--------|------|
| Hermes Agent | `hermes-agent` | Orchestration, memory, skill management |
| Claude Code | Local | Code generation, agent scaffolding |
| PostHog | GitHub (`PostHog/posthog`) | Analytics, session replays, A/B tests |
| Chatwoot | GitHub (`chatwoot/chatwoot`) | Support inbox, AI replies, no per-seat fees |
| Typebot | GitHub (`baptisteArno/typebot.io`) | Lead-qualification forms, WhatsApp flows |
| Frappe CRM | GitHub (`frappe/crm`) | Lead/deal pipeline |
| Invoice Ninja | GitHub (`invoiceninja/invoiceninja`) | Client invoicing & subscriptions |
| Cal.diy | GitHub (`calcom/cal.diy`) | Self-hosted booking |
| Autumn | GitHub (`useautumn/autumn`) | Usage-based / metered billing |
| Voice Studio | GitHub (from Video 2) | Open-source TTS (ElevenLabs alternative) |
| Hindsight | GitHub (from Video 2) | Persistent Hermes agent memory |
| NewsJack | GitHub (`hlOk-EFUITQ`) | LLM PR manager — find reporters, wedge into stories |
| Jev | GitHub (from Video 3) | Cheap decision model for lead scoring / routing |
| Hostinger VPS | Hostinger | $3–$10/mo self-hosting |
| Stripe | stripe.com | Payment processing |

## 5. Skills to Learn

| Skill | Priority | How to Learn |
|-------|----------|--------------|
| Prompt engineering & agent design | High | Build 3–5 agents in Hermes; use Hindsight memory |
| Docker / self-hosting | Medium | Deploy repos from `biz_tools` via Docker-compose |
| API integration | Medium | Connect LLM API, Jev, Voice Studio to agent |
| Sales / outreach | High | Cold email, LinkedIn DM, NewsJack for PR |
| Contract / SLA writing | Medium | Template: scope, uptime, data privacy, escalation |
| Light debugging / monitoring | Medium | PostHog session replays to find agent drop-offs |

Your **CS/cybersecurity background** means the build side is easy. The gap is *productizing* and *selling*.

## 6. How to Get Customers

**Step 1:** Pick one niche (e.g., dental offices in your city).

**Step 2:** Build a free demo — 2-minute video of your agent (with Hindsight memory + Typebot form) handling a realistic inquiry.

**Step 3:** Outreach (20–30 personalized emails/DMs per week):
- “I built an AI agent that [books leads / answers FAQs] for [niche] businesses. It runs 24/7 and costs less than one part-time receptionist. Free 14-day pilot.”

**Step 4:** PR via NewsJack — use it to find reporters covering AI automation or local business tech, wedge your story in, get press that drives inbound leads.

**Step 5:** Pilot → Paid — after pilot shows results (booked appointments, saved hours), convert to $3–$5K/month retainer + setup fee.

**Step 6:** Referrals — ask happy customers for introductions to peers.

**Step 7:** Upsell tool-stack consulting (PostHog, Chatwoot, Autumn, etc.) as add-on services.

## 7. Probability of Success

| Timeframe | Probability | Notes |
|-----------|-------------|-------|
| Short term (0–3 months) | 40–60% | Higher than before because tool stack is cheaper and faster to deploy; NewsJack + Jev give you PR and lead-scoring leverage. |
| Long term (6–18 months) | 70–85% *if* you reach 3+ paying customers | Recurring revenue compounds; self-hosted stack keeps margins high; niche dominance via referrals. |

**Key risks:** Client churn if agent hallucinates, LLM API cost creep, regulatory/data-privacy (HIPAA/GDPR) for medical/legal niches. Hindsight memory reduces hallucination risk over time.

## 8. Short-Term Viability Exercise (2 Weeks)

**Days 1–3:** Pick a niche. List 30 local businesses. Identify the one repetitive task they hate (e.g., “responding to new patient inquiries”).

**Days 4–7:** Build a *manual* version — you act as the agent using Hermes + templates. Track time saved and client reaction.

**Days 8–10:** Deploy the self-hosted stack on Hostinger VPS (PostHog + Chatwoot + Typebot + Hindsight) using Docker-compose from `biz_tools`. Offer a free 14-day pilot to 2–3 businesses.

**Days 11–14:** Review results. Use NewsJack to find one local business story to pitch to press. Use Jev to score inbound leads cheaply.

**Success metric:** At least one business verbally commits to pay ≥$2,000/month after the pilot.

## 9. How This Fits Your Overall Offerings

- **CS/cybersecurity angle:** Position the agent as “secure, auditable, private-by-design.” Self-hosted stack means client data stays on your VPS, not a black-box SaaS. Highlight HIPAA/GDPR compliance capability.
- **Combine with other ideas:** Use the agent to qualify leads for your white-label SaaS (ideas #5/#6 in `biz_ideas`) or to handle support for your done-for-you AI implementation service.
- **Cross-sell:** Once you have an agent customer, offer additional automations (invoice processing via Invoice Ninja, appointment reminders via Cal.diy, review generation via Mautic).

## 10. Bottom Line

Number 10 is now **stronger** with `biz_tools` and Video 3 integrated:

- **Cost:** ~70–80% lower monthly tooling spend (self-hosted vs. SaaS).
- **Speed:** MVP in 1–2 weeks instead of 2–4.
- **Revenue:** $5K/month retainer + $3.7K–$4.3K in one-time setup fees per customer.
- **Automation:** Typebot + Hindsight memory + Voice Studio + Jev = multi-channel agent with memory, voice, and cheap lead scoring.
- **Growth engine:** NewsJack gives you low-cost PR/traffic so you’re not 100% dependent on cold outreach.

**Run the 2-week pilot exercise.** If you get one verbal commitment to pay ≥$2,000/month, the AI Agent Service Business is viable as a semi-passive, high-margin addition to your overall business offerings.

## 11. Proof of Concept Development Plan (Local POC — Vet Clinic Demo)

> *Goal:* Build and test a local POC demonstrating an AI agent that answers vet clinic inquiries (appointments, emergencies, prescriptions) via a web chat widget. The agent runs in Hermes and communicates with a local website hosted on this laptop. No hosting or payment processing included in this phase — purely local testing.

### 11.1 Project Structure

```
/home/shiva/poc-vet-agent/
├── app/                      ← Static website (vet clinic frontend)
│   ├── index.html            ← Landing page with chat widget placeholder
│   ├── chat.css              ← Chat widget styling (uses :where() scoping, shared tokens)
│   ├── chat.js               ← Chat widget JS, polls Hermes agent via REST endpoint
│   └── assets/               ← Images, vet clinic mock data
├── config/                   ← POC configuration files
│   ├── vet_knowledge_base.json   ← FAQ + vet clinic service info for agent memory
│   └── agent_prompts.yaml    ← Prompt templates for different agent roles
├── docs/                     ← Development plan, progress logs, meeting notes
│   ├── development_plan.md   ← This doc (full dev plan with milestones)
│   ├── poc_progress.md       ← Incremental progress tracking
│   └── vet_faq.md            ← Curated vet clinic FAQ for testing
├── data/                     ← Local SQLite (real migrations, in-memory mode for tests)
│   └── vet_agent.db          ← Agent memory, conversation history, appointments table
├── logs/                    ← Local logs for debugging
└── README.md               ← Quick start instructions for the POC
```

### 11.2 Prerequisites (Already Available)

| Tool | Availability | Notes |
|------|-------------|-------|
| Hermes Agent | ✅ Available | Running on laptop; will host local agent |
| Claude Code | ✅ Available | Code generation for website and agent logic |
| Python 3.11 | ✅ Available | For running local Flask API bridge |
| pip / uv | ✅ Available | For dependency management |
| git | ✅ Available | For tracking POC changes |

### 11.3 Key GitHub Repos for POC (Local Only)

| Repo | Use Case | Status |
|------|----------|--------|
| `fastapi/fastapi` | REST API endpoint between website and Hermes agent (if needed) | Will clone if needed |
| `tiangolo/full-stack-fastapi-postgresql` | Reference architecture (website + API + DB) | Reference only |
| `baptisteArno/typebot.io` | (Future) Chat widget replacement — not needed for POC | Future use only |

> **Note:** For the POC, we are NOT deploying the full `biz_tools` stack (PostHog, Chatwoot, Voice Studio, etc.). We are only proving the core concept: local website → chat widget → Hermes agent → response. The full tool stack will be integrated later in production phase.

### 11.4 Milestone-Based Development Plan

#### Phase 0: Environment Setup & Workspace (Estimated: 1–2 hours)
- [x] Create POC workspace at `/home/shiva/poc-vet-agent/`
- [ ] Initialize git repo and README
- [ ] Verify Hermes Agent is running and accessible
- [ ] Verify Python 3.11 + pip available
- [ ] Create local SQLite database schema for vet clinic data

#### Phase 1: Vet Clinic Website Stub (Estimated: 3–4 hours)
- [ ] Create `index.html` — vet clinic landing page with hero, services, contact
- [ ] Create `chat.css` — floating chat widget styling (dark theme, kawaii accents optional)
- [ ] Create `chat.js` — widget that renders chat UI, sends user messages to Hermes agent endpoint
- [ ] Mock vet clinic data: clinic name "Paws & Claws Animal Hospital", phone, address

#### Phase 2: Hermes Agent Integration (Estimated: 4–6 hours)
- [ ] Create a Hermes skill called `vet_agent_poc` with vet-specific memory
- [ ] Load vet FAQ from `vet_knowledge_base.json` into agent memory
- [ ] Set up local API endpoint (Flask or FastAPI) to bridge HTTP requests from website to Hermes
- [ ] Configure agent to answer questions: appointments, emergencies, prescriptions, clinic hours
- [ ] Test basic round-trip: website → API → Hermes → response

#### Phase 3: Core Agent Features (Estimated: 6–8 hours)
- [ ] Appointment booking via agent (store in SQLite, show confirmation)
- [ ] Emergency triage logic (urgent/non-urgent classification)
- [ ] Prescription refill requests (store in SQLite, track status)
- [ ] FAQ lookup using agent memory (Hermes knowledge base)
- [ ] Error handling: agent fails gracefully when query is unclear

#### Phase 4: Demo Polish & Customer-Facing Features (Estimated: 3–4 hours)
- [ ] Chat history per browser session (localStorage)
- [ ] Typing indicators, message timestamps
- [ ] Demo mode toggle (shows fake "agent is typing" delays)
- [ ] README with one-click-start instructions
- [ ] Record a 30-second Loom-style demo video walkthrough (using ffmpeg or OBS if available)

#### Phase 5: Testing & Bug Fixing (Ongoing)
- [ ] Test all 4 core agent features with simulated customer queries
- [ ] Edge cases: empty messages, very long messages, off-topic queries
- [ ] Cross-browser test: Chrome + Firefox on laptop
- [ ] Log all bugs in `docs/poc_progress.md` with fixes

### 11.5 Current Progress Tracker

| Task | Status | Owner |
|------|--------|-------|
| Phase 0: Environment Setup | In progress | You (user) + Hermes |
| Phase 1: Vet Clinic Website Stub | Not started | Hermes (Claude Code) |
| Phase 2: Hermes Agent Integration | Not started | Hermes (Claude Code) |
| Phase 3: Core Agent Features | Not started | Hermes (Claude Code) |
| Phase 4: Demo Polish | Not started | Hermes (Claude Code) |
| Phase 5: Testing & Bug Fixing | Not started | You (user) |

*Progress will be updated in `docs/poc_progress.md` after each completed phase.*

---

*Prepared by Hermes Agent – 2026-09-16*