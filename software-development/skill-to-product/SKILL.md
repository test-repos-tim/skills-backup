---
name: skill-to-product
description: Package Hermes skills as standalone web products for users.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [productization, deployment, flask, railway, web-app, standalone, packaging]
    related_skills: [flask-backend-from-html, hermes-agent-skill-authoring]
---

# Skill-to-Product: Packaging Hermes Skills as Standalone Web Apps

## Overview

Take any Hermes skill and turn it into a standalone web product that non-technical end users can access from a browser URL, with no Hermes installation, no terminal, and no Linux required on their end.

## When to Use

- User has a Hermes skill that solves a problem and wants to productize it as a service
- End users are non-technical and should not need to install Hermes or understand skills
- Solution needs a browser-based UI with user accounts and session isolation
- The skill can be reduced to API calls + LLM logic (research, analysis, content generation)
- Multi-tenant isolation is required (users should not see each other's data)

## When NOT to Use

- The skill depends on filesystem access or local tools that can't be remote
- The skill requires GPU/local model inference (use Modal/GPU cloud instead)
- The skill is purely interactive (requires terminal input) — package as a CLI instead
- The skill already has a web API or is already a web service

## Architecture Pattern

End users (browser) <-> Flask app (Railway) <-> LLM/Web APIs (OpenRouter, ArXiv). SQLite handles user isolation. Everything is self-contained on Railway.

## Deployment Files

**requirements.txt:**
```
Flask==3.1.2
requests>=2.31.0
bcrypt==4.1.2
flask-cors==5.0.1
flask-login==0.6.3
gunicorn==23.0.0
ddgs==9.1.2
```

**Dockerfile:**
```dockerfile
FROM python:3.11-slim
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
EXPOSE $PORT
CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "--workers", 2, "wsgi:app"]
```

**Procfile:**
```
web: gunicorn --bind 0.0.0.0:$PORT --workers 2 --timeout 300 wsgi:app
```

**wsgi.py:**
```python
from app import app, init_db
init_db()
```

## Environment Variables (Railway)

- `OPENROUTER_API_KEY` — required, from https://openrouter.ai/
- `SECRET_KEY` — `python3 -c "import secrets; print(secrets.token_hex(32))"`
- `OPENROUTER_MODEL` — default: `nvidia/nemotron-3-ultra-550b-a55b:free` (1M context)

## Deploy

```bash
railway login
railway init product-name
railway variables set OPENROUTER_API_KEY="sk-or-..."
railway variables set SECRET_KEY="..."
railway up
```

## Multi-User Isolation

- Flask-Login + bcrypt for auth
- Every DB query includes `WHERE user_id = ?` 
- Each user sees only their own sessions

## Model Selection (Research Tasks)

| Model | Context | Free |
|---|---|---|
| nvidia/nemotron-3-ultra-550b-a55b | 1M tokens | Yes |
| nvidia/nemotron-3-super-120b-a12b | 262K tokens | Yes |
| openai/gpt-oss-20b | 131K tokens | Yes |

## Common Pitfalls

1. **Not isolating user data** — every query MUST include `WHERE user_id = ?`
2. **Exposing API keys in frontend** — only use in backend Python
3. **Tool-call format from LLMs** — use `tool_choice: "none"` and `tools: []` to force text output
4. **Rate limit errors** — use Nemotron Ultra (1M context), handle 429 gracefully with retry-after header
5. **Railway free tier sleeping** — upgrade to Hobby ($5/mo) for persistence
6. **Render free tier misconception** — Render no longer offers a perpetual free tier (Aug 2026). Their "free" option is a $5 trial credit (30-day expiry) plus $5/month Hobby plan. Check actual pricing before assuming any platform has a perpetual free tier.

## Hosting Options (Free Tier Comparison)

| Platform | Free Tier | Notes |
|---|---|---|
| **Railway** | $5 trial credit, 30 days. $5/mo Hobby plan for persistent hosting | No perpetual free tier as of Aug 2026. CLI login via `railway login --browserless` works in headless environments. |
| **Render** | ~~Perpetual free tier~~ (Aug 2026: $5 trial credit, 30-day expiry, $5/month Hobby plan) | **No longer truly free** as of Aug 2026. Their marketing/schema.org claims `isAccessibleForFree: true` are misleading. Verify current pricing before deploying.
| **Fly.io** | 3GB RAM, 160GB disk, 3M CPU-seconds/month free | `flyctl install` via curl script. Requires interactive `flyctl auth login` (no headless mode in 2026). |
| **PythonAnywhere** | Free tier with limitations (no background workers, sleeps after 5min idle) | Simple but limited for research apps with API calls. |

**Recommendation:** For non-technical clients that need always-available access, use **Fly.io's free tier** (true free, 3GB RAM, requires $5 payment method for account verification) or **Railway's $5/month Hobby plan** (reliable, always-on, simple CLI). Render no longer offers a perpetual free tier as of Aug 2026 - their "free tier" is now a $5 trial credit (30-day expiry) + $5/month Hobby plan.

## Verification Checklist

- All files present: app.py, requirements.txt, Dockerfile, Procfile, wsgi.py
- flask-cors, flask-login, bcrypt in requirements
- Dockerfile uses python:3.11-slim + gunicorn
- Every DB query includes user_id filtering
- Login/Register UI works
- Sessions isolated per user

## One-Shot Recipe: Package a Skill

```bash
mkdir -p ~/my-product/prompts
cp /path/to/skill/SKILL.md ~/my-product/prompts/system_prompt.txt
cd ~/my-product
railway login && railway init my-product
railway variables set OPENROUTER_API_KEY="***"
railway variables set SECRET_KEY="$(python3 -c 'import secrets; print(secrets.token_hex(32))')"
railway up
```

## Reference Implementation

A complete implementation exists at `/home/shiva/tools/therapist-project/` with:
- `app.py` — Full Flask backend with auth, sessions, research API
- `prompts/research_system_prompt.txt` — System prompt for research LLM
- `wsgi.py`, `Dockerfile`, `Procfile` — Production deployment files