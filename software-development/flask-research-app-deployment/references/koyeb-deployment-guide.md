# Koyeb Free Tier Deployment Guide

## Why Koyeb for Flask Apps

- **Truly free tier**: 512MB RAM, 1 vCPU, 2GB SSD, no credit card required
- **GitHub integration**: Deploy directly from GitHub repo
- **Dockerfile support**: Full control over build process
- **Environment variables UI**: Proper UI for setting env vars (unlike PythonAnywhere free tier)
- **Auto HTTPS**: Automatic SSL certificates
- **Global regions**: Multiple deployment regions

## Deployment Steps

1. **Prepare Dockerfile** (required for Koyeb):
   ```dockerfile
   FROM python:3.11-slim
   WORKDIR /app
   RUN apt-get update && apt-get install -y --no-install-recommends gcc && rm -rf /var/lib/apt/lists/*
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt
   COPY app.py wsgi.py Procfile runtime.txt .gitignore ./
   COPY prompts/ ./prompts/
   RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
   USER appuser
   EXPOSE 8080
   CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "1", "--timeout", "300", "wsgi:app"]
   ```

2. **Deploy via Koyeb Dashboard**:
   - Go to https://app.koyeb.com/
   - Sign up with GitHub (no payment details)
   - Create App → GitHub → Select your repo
   - Builder: Dockerfile
   - Instance: Free (512MB RAM)
   - Environment Variables:
     - `SECRET_KEY` = [generated secret]
     - `OPENROUTER_API_KEY` = [your key]
     - `OPENROUTER_MODEL` = `nvidia/nemotron-3-ultra-550b-a55b:free`
     - `PORT` = `8080`
   - Deploy

3. **Your app URL**: `https://<app-name>-<random>.koyeb.app`

## Key Notes

- Koyeb uses port 8080 internally (not 5000 or $PORT)
- Dockerfile MUST be in repo root
- Build uses Dockerfile, not Procfile or render.yaml
- No `render.yaml` needed for Koyeb
- Procfile is optional but good to keep for other platforms

## Verification

Before deploying, verify Dockerfile locally:
```bash
# Build test
docker build -t test-app .
docker run -p 8080:8080 -e OPENROUTER_API_KEY=... test-app
```

## Comparison with Other Free Tiers

| Platform | Free RAM | Card Required | Env Vars UI | Dockerfile Support |
|---|---|---|---|---|
| Koyeb | 512MB | No | Yes | Yes |
| Fly.io | 3GB | Yes ($5 auth) | Yes | Yes |
| PythonAnywhere | 512MB | No | No (paid only) | No |
| Render | 512MB | No | Yes | Yes (but paid after trial) |
| Railway | 512MB | Yes ($5/mo) | Yes | Yes |