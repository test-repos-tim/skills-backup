---
name: flask-micro-learning-app
description: "Use when building Flask wisdom apps for Android APK."
version: 1.0.0
tags: [flask, web-app, modular, openrouter, scraping]
---

# Flask Micro-Learning App (DeepLearn Pattern)

Procedure (modular Flask app for wisdom/feed delivery):

1. Create `deeplearn/test1/`. Files: `app.py` (routes + openrouter/summarize + embedded scraper), `config.py` (env loader), `templates/`, `static/`, `README.md`, `.env`, `log/`.
2. `.env` holds `OPENROUTER_API_KEY` (secret; never expose) and `PORT=9899`. Log file at `logs/app.log`.
3. `/` landing page has header "Deep Learn Daily Wisdom" + login button. `/interface` loads UI with 4 clickable book links (Bhagavad Gita, Tao Te Ching, Book of Proverbs, Art of War). `/log` shows actions. `/api/scrape` returns JSON with book examples. `/api/summarize` POST takes `{book, author}` and uses `.env` model config with real OpenRouter API calls.
4. Start: `source venv/bin/activate && python app.py`. Stop: `pkill -f app.py`. Port configurable via `PORT=` in `.env` or command line.

Always-on rules:
- Every separate file gets top-level comments; `README.md` explains inputs/outputs per module.
- Scraping logic is embedded in `app.py` for independence and simplicity (no separate `scraper.py` needed).
- Keep APK architecture notes in README (Android Studio HTML5 wrapper).
- `config.py` loads .env via `load_dotenv()` but `app.py` must also call `load_dotenv()` explicitly before `app.config.from_object(Config)` to ensure Flask picks up runtime env values.

Pitfalls:
- Python 3.14 removes `pkgutil.get_loader`; Flask <3 fails at import — upgrade to Flask 3.1.3+ in venv.
- Never read `.env` with file-read tools; treat as secret-bearing (access denied by design).
- Log directory `logs/` must exist before `FileHandler` starts.
- Must call `load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))` in `app.py` *before* `app.config.from_object(Config)` so Flask sees the runtime env values; `config.py`'s class attributes are evaluated at import time and won't pick up `.env` changes after restart.
- `requests` must be installed for OpenRouter API calls (`pip install requests python-dotenv`).
- `app.run()` must use `port=app.config.get('PORT', 9876)` not hardcoded port to respect `.env` changes.
- Changing `.env` `PORT` requires server restart (`pkill -f app.py && python app.py`).
- Port already in use errors require killing existing processes (`fuser -k <port>/tcp` or `pkill -f "python app.py"`).
