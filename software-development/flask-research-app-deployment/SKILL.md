---
name: flask-research-app-deployment
description: Deploy Flask research apps to free hosting tiers.
version: 1.1.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [flask, deployment, render, railway, free-tier, research-assistant]
---

# Flask Research App Deployment

## Overview

Package a Flask research assistant as a standalone web product on free hosting tiers. Provides browser-based access for non-technical users with no Hermes installation required.

## Project Structure

```
your-app/
├── app.py              # Flask backend
├── wsgi.py             # Production entry point
├── requirements.txt    # Dependencies
├── Procfile            # Process definition
├── runtime.txt         # Python version
├── render.yaml         # Render explicit config (use when Procfile not detected)
├── prompts/
│   └── research_system_prompt.txt
```

## Key Files

**requirements.txt:**
```txt
Flask==3.1.2
requests>=2.31.0
bcrypt==4.1.2
flask-cors==5.0.1
flask-login==0.6.3
gunicorn==23.0.0
ddgs==9.1.2
```

Note: Use `requests>=2.31.0` instead of pinned `==2.31.3` because Render uses Python 3.14, which breaks older pinned versions.

**Procfile:**
```
web: gunicorn --bind 0.0.0.0:$PORT --workers 2 --timeout 300 wsgi:app
```

**render.yaml (explicit Render config when Procfile not detected):**
```yaml
services:
  - type: web
    name: therapy-research-app
    build:
      buildCommand: pip install -r requirements.txt
    startCommand: gunicorn --bind 0.0.0.0:$PORT --workers 1 --timeout 300 wsgi:app
```

## Prevent Tool-Call JSON from LLM

On OpenRouter free tier, models may return JSON tool-call format instead of text. Fix with `tool_choice: "none"` and `tools: []`.

## User Isolation Pattern

Every database query MUST include user_id filtering.

## Verification Checklist

1. File structure - all required files present
2. Dependencies - gunicorn, flask, flask-login, bcrypt, flask-cors, requests, ddgs
3. Config - Procfile uses $PORT, runtime.txt has Python 3.11, wsgi.py calls init_db()
4. Module imports without errors
5. End-to-end: register, login, create session, ask research question

## Deployment

### Render.com (Free Tier)

1. Push to GitHub
2. render.com/dashboard -> New -> Web Service -> Connect GitHub
3. Start command: `gunicorn --bind 0.0.0.0:$PORT --workers 2 wsgi:app`
4. Add env vars: OPENROUTER_API_KEY, SECRET_KEY

### Railway (Hobby Plan, $5/month)

### Fly.io (Free Tier)

## Environment Variables

| Variable | Required | Description |
|---|---|---|
| OPENROUTER_API_KEY | Yes | From https://openrouter.ai/keys |
| SECRET_KEY | Yes | python3 -c "import secrets; print(secrets.token_hex(32))" |
| OPENROUTER_MODEL | No | Default: nvidia/nemotron-3-ultra-550b-a55b:free |

## Model Selection

| Model | Context | Free | Notes |
|---|---|---|---|
| nvidia/nemotron-3-ultra-550b-a55b:free | 1M tokens | Yes | Best for research |
| nvidia/nemotron-3-super-120b-a12b:free | 262K | Yes | Alternative |

## Common Pitfalls

1. **Tool-call JSON from LLM** - Fix with tool_choice: "none" and tools: []
2. **Rate limits** - Handle 429, use Nemotron Ultra (1M context)
3. **User data leakage** - Every DB query MUST filter by user_id
4. **Headless deployment** - Use railway login --browserless
5. **Missing runtime.txt** - Causes build failures
| Render env var prompt | Add PORT=10000 manually to clear the warning |
7. **gunicorn not in venv** - Install in project venv for local testing
8. **Procfile line endings** - Must end with newline, no trailing spaces
9. **Python version pinning** - Use flexible specifiers (requests>=2.31.0) since Render uses Python 3.14
10. **Render ignoring Procfile** - Create render.yaml with explicit startCommand
11. **Python 3.14 breaks older Flask** - `pkgutil.get_loader` removed in Python 3.14; use Flask 3.1.3+ or `Flask(__name__, instance_relative_config=False)` workaround. For Python 3.14 specifically, always upgrade Flask to >=3.1.3 before testing.
12. **`.env` must specify correct `OPENROUTER_MODEL`** - A malformed line like `OPENROUTER_MODEL=-dots-studio/dots-3-note-preview:free` overrides the correct model and causes 400 errors from OpenRouter. Verify with `grep OPENROUTER_MODEL .env`; the active line must match a valid OpenRouter model ID (e.g., `nvidia/nemotron-3-ultra-550b-a55b:free`).
12. **GitHub repo doesn't exist on remote** - Render build will silently use cached/old build. Always verify repo exists BEFORE deploying: `curl -s https://raw.githubusercontent.com/USER/REPO/main/Procfile`. If this returns 404, the repo doesn't exist or files weren't pushed. Render will clone a non-existent repo but use a cached build from a previous successful (or attempted) deployment, giving misleading build logs that show "Building" and "Installing dependencies" but then fail with "ModuleNotFoundError: No module named 'your_application'" because it doesn't have your actual app files.
13. **therapist-project.zip in repo** - Never commit zip files. Render won't extract them. Must upload individual files or use git clone + cp approach.
14. **render.yaml env section creates REQUIRED env vars** - When render.yaml includes `env:` section, Render UI shows variables as REQUIRED. Remove the `env:` section entirely to avoid deployment blocking errors.
15. **GitHub repo name mismatch** - Repo created as `therapy-research-app-public` but deployed as `therapy-research-app`. Verify exact name via GitHub API before deploying.
16. **Fly.io requires credit card for verification** - Even for free tier (3GB RAM), Fly.io requires a credit card for signup verification ($5 auth, refunded). Not truly "no card" free.
17. **PythonAnywhere free tier lacks env vars UI** - Environment variables section in Web tab only available on paid plans. Workaround: set env vars directly in WSGI file with `os.environ['VAR'] = 'value'`.
18. **Koyeb free tier works without card** - 512MB RAM, 1 vCPU, 2GB SSD, no credit card required, has proper env vars UI, deploy from GitHub with Dockerfile.
19. **Render cached builds mislead** - Render can show "Building" and "Installing dependencies" from a cached build even when the repo doesn't exist or files weren't pushed. Verify the actual GitHub repo exists and has files before trusting Render's build logs.
20. **Flexible version specifiers mandatory** - Use `requests>=2.31.0` instead of pinned versions (e.g., `==2.31.3`) since Render uses Python 3.14 which breaks older pinned versions.
21. **Procfile/render.yaml must be in repo root** - Verify with `curl -sf https://raw.githubusercontent.com/USER/REPO/main/Procfile` before deploying. If 404, the file isn't in the repo root or repo doesn't exist.

## Deployment Debugging Workflow

When Render fails with "ModuleNotFoundError: No module named 'your_application'" or similar:

1. **Verify GitHub repo exists** BEFORE deploying:
   ```bash
   curl -s https://raw.githubusercontent.com/USER/REPO/main/Procfile
   ```
   If this returns 404, the repo doesn't exist or files weren't pushed.

3. **Check what Render actually sees** in the build logs:
   - Does it show "Cloning from https://github.com/..."? (if NOT, it's using cached build)
   - Does it show "Running build command 'pip install -r requirements.txt'"? (if yes, repo was found)
   - Does it show the correct start command (not `your_application.wsgi`)?
   - **If Render is NOT cloning from your GitHub**, verify the repo exists and the Render service is connected to the correct GitHub repo. A cached build can look like it's building but is actually stale.

- **Render ignoring Procfile** - Create render.yaml with explicit `startCommand`.
   Render sometimes uses a default `gunicorn your_application.wsgi` instead of reading the Procfile. This happens when:
   - Procfile is missing from the repo
   - Repo wasn't actually pushed (Render uses a cached build)
   - render.yaml override is needed
   - **Always verify GitHub repo has files before deploying** — use `curl -sf https://raw.githubusercontent.com/USER/REPO/main/Procfile` to confirm before trusting Render build logs (cached builds can show fake "Installing dependencies" without actually cloning your repo)

## Verified Reference

Working implementation at `/home/shiva/tools/therapist-project/` with 6/6 ad-hoc tests passing, research queries returning 6,700+ char answers with 11 citations.

### Linked References
- `references/openrouter-rate-limit-troubleshooting.md` - Rate limit handling and model comparison
- `references/research-system-prompt-template.md` - System prompt template for research assistants
- `references/render-procfile-not-detected-fix.md` - Debugging guide for Render Procfile detection issues
