# Flask Backend from HTML — Directory Structure

Standard project layout for a Flask app migrated from a standalone HTML file.

```
project/
├── app.py              # Flask application with routes and API
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (SECRET_KEY, etc.)
├── database.db         # SQLite database (auto-created on first run)
├── start.sh            # Launcher script (creates venv, installs deps, runs app)
├── README.md           # Project documentation
├── templates/
│   └── index.html      # Jinja2 template (was index.html, now with template vars + API calls)
├── static/
│   └── style.css       # All CSS extracted from inline <style> tags
└── venv/               # Python virtual environment (gitignored)