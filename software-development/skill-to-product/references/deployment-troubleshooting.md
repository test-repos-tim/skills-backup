# Deployment Troubleshooting

## Railway CLI Headless Login

**Problem:** `railway login` tries to open a browser but fails in headless/SSH environments.

**Solution:**
```bash
railway login --browserless
```
This prints a sign-in URL + code you can use from any device:
```
→ Sign in with one click:
  https://railway.com/activate?user_code=FMWV-SSTR

→ Or go to https://railway.com/activate and enter this code:
  FMWV-SSTR
```

**After login:** The CLI automatically picks up the session token. You can then run `railway init` and `railway up`.

## Railway Free Tier Changes (August 2026)

Railway no longer has a perpetual free tier. Current pricing:
- **Free Trial:** $5 credit when you sign up, expires in 30 days
- **Hobby Plan:** $5/month (includes $5 of usage credits)
- **Pro Plan:** $20/month per seat

For a lightweight Flask app, the Hobby plan's $5 credit covers monthly costs. The app uses ~256MB RAM which is well within the free credits allocation.

## Alternative Free Hosting Platforms

### Render.com (Recommended for True Free Tier)
- **Free tier:** 256MB RAM web services, spins down when idle, wakes on request
- **Free tier covers:** Small Flask apps (usage-based credits ~$7/month)
- **Deploy:** Git push to Render's Git remote
- **Limitations:** 100GB bandwidth/month, 256MB RAM

### Fly.io
- **Free tier:** 3GB RAM, 160GB SSD, 3M CPU-seconds/month
- **Deploy:** `flyctl launch` via CLI
- **Caveat:** `flyctl auth login` requires interactive browser (no headless mode in v0.4.83)
- **Install:** `curl -L https://fly.io/install.sh | sh`

### PythonAnywhere
- **Free tier:** 512MB disk, 1 web worker, sleeps after 5min idle
- **Deploy:** Git push or manual upload
- **Caveat:** Free tier doesn't support background workers (Celery needed for async)

## Render Deployment

If Railway isn't suitable:

```bash
# 1. Create a free Render account at https://render.com
# 2. Create a Web Service from your Git repo
# 3. Set environment variables:
#    - OPENROUTER_API_KEY
#    - SECRET_KEY
# 4. Set build command:
#    pip install -r requirements.txt
# 5. Set start command:
#    gunicorn --bind 0.0.0.0:$PORT --workers 2 wsgi:app
# 6. Deploy - Render auto-deploys on Git push
```

## Environment Variables Checklist

Before deploying, ensure these are set:
- `OPENROUTER_API_KEY` - from https://openrouter.ai/ (required)
- `SECRET_KEY` - `python3 -c "import secrets; print(secrets.token_hex(32))"` (required)
- `OPENROUTER_MODEL` - defaults to `nvidia/nemotron-3-ultra-550b-a55b:free` (optional)
- `DB_PATH` - for production, use a persistent path (not /tmp unless using ephemeral deploy)

## Production vs Development

- **Development:** `python app.py` (Flask dev server, auto-reload)
- **Production:** `gunicorn wsgi:app` (multiple workers, no auto-reload)
- **Docker:** `FROM python:3.11-slim` + `CMD ["gunicorn", ...]`
- **Procfile:** For platforms that auto-detect (Render, Railway)
