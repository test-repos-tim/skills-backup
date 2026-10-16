---
name: flask-backend-from-html
description: "Upgrade standalone HTML to a Flask backend app."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [flask, web-development, backend, full-stack, rest-api, authentication, python, migration]
    related_skills: [claude-design, sketch, subagent-driven-development]
---

# Flask Backend from Existing HTML

Use this skill when the user has a standalone HTML file with inline CSS and JavaScript (often using localStorage for state) and wants to upgrade it to a full-stack Flask application with:

- A proper backend serving the frontend via Jinja2 templates
- A REST API replacing localStorage/client-side state
- Secure credential storage (PBKDF2-HMAC-SHA256 with random salt)
- Session-based authentication with cookie handling
- A directory structure separating static assets, templates, and application logic

## When to Use This Skill

Load this skill when:
- User says "give this a proper backend" or "make this full-stack"
- User has a single HTML file that uses localStorage and wants a database
- User wants to add authentication to a static site
- User needs secure password storage but has credentials hardcoded in client-side JS
- User wants to migrate from inline CSS/JS to a proper Flask project structure

## When NOT to Use This Skill

- Building a brand-new Flask app from scratch (use standard Flask patterns directly)
- The user wants a single-file solution with no backend (keep it static)
- The project needs a frontend framework like React/Vue (this is for vanilla HTML/CSS/JS)
- The user only wants to fix a specific bug, not restructure

## Core Method

### 1. Analyze the Existing HTML

Before touching code, read the full HTML file to understand:
- What inline CSS exists (extract all of it to `static/style.css`)
- What JavaScript state management exists (localStorage, sessionStorage)
- What user interactions exist (forms, buttons, navigation)
- What data flow exists (how does data move between components?)
- What authentication exists (if any - often a hardcoded password check)

**Pitfall: Don't skip reading the full file.** Inline HTML files can be 2000+ lines. Read in chunks if needed.

### 2. Extract CSS to External File

```
templates/
  └── index.html       # Jinja2 template (was the original HTML)
static/
  └── style.css        # All CSS extracted from <style> tag
```

- Move all `<style>` content to `static/style.css`
- Replace `<style>...</style>` with `<link rel="stylesheet" href="/static/style.css">`
- Keep only the HTML structure and template variables in `index.html`

### 3. Create the Flask App Structure

Standard Flask project layout:

```
project/
├── app.py              # Flask app with routes
├── requirements.txt    # Dependencies (flask, bcrypt, python-dotenv)
├── .env                # Environment variables (SECRET_KEY, FLASK_ENV, etc.)
├── database.db         # SQLite database (auto-created)
├── templates/
│   └── index.html      # Jinja2 template
├── static/
│   └── style.css       # Extracted CSS
├── start.sh            # Launcher script
└── README.md           # Documentation
```

### 4. Implement Secure Authentication

**Never store passwords in client-side JavaScript.** Always hash them server-side.

```python
import hashlib
import secrets

def hash_password(password: str, salt: str = None) -> tuple:
    if salt is None:
        salt = secrets.token_hex(32)
    hashed = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000)
    return hashed.hex(), salt

def verify_password(password: str, stored_hash: str, salt: str) -> bool:
    computed_hash, _ = hash_password(password, salt)
    return secrets.compare_digest(computed_hash, stored_hash)
```

- Use PBKDF2-HMAC-SHA256 with 100,000+ iterations
- Generate a unique 64-character salt per password
- Store hash and salt separately in the database
- Use `secrets.compare_digest` to prevent timing attacks

### 5. Replace Client-Side State with REST API

Convert localStorage calls to API calls:

**Before (client-side):**
```javascript
localStorage.setItem('posts', JSON.stringify(posts));
const posts = JSON.parse(localStorage.getItem('posts'));
```

**After (REST API):**
```javascript
// Save
const response = await fetch('/api/posts', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    credentials: 'include',
    body: JSON.stringify(postData)
});

// Load
const response = await fetch('/api/posts');
const posts = await response.json();
```

### 6. Implement Standard REST Endpoints

For a blog/post content type:

| Method   | Endpoint            | Auth Required | Description        |
|----------|---------------------|---------------|--------------------|
| GET      | /api/posts          | No            | List all posts     |
| GET      | /api/posts/<id>     | No            | Get single post    |
| POST     | /api/posts          | Yes           | Create post        |
| PUT      | /api/posts/<id>     | Yes           | Update post        |
| DELETE   | /api/posts/<id>     | Yes           | Delete post        |
| GET      | /api/auth/status    | No            | Check auth status  |
| POST     | /api/auth/login     | No            | Login              |
| POST     | /api/auth/logout    | No            | Logout             |

### 7. Frontend JavaScript Migration

Key changes when migrating frontend JS to use API:

1. **Remove localStorage/sessionStorage** - replace with API calls
2. **Add credentials: 'include'** to all fetch requests for auth cookies
3. **Handle 401 responses** - redirect to login or show error
4. **Keep client-side rendering** - frontend still renders posts, but data comes from API instead of localStorage
5. **Preserve the markdown parser** - client-side rendering of markdown content stays intact
6. **Update auth flow** - login POSTs to API, checks response success, stores admin state in JS state object (not localStorage)

### 8. Verification Script

Always write and run a verification script that tests:

1. Homepage serves HTML with external CSS link
2. All public API endpoints return expected data
3. Authentication flow works (login, status, logout)
4. Protected endpoints reject unauthenticated requests (401)
5. CRUD operations work when authenticated
6. Password hash verifies correctly
7. Static files (CSS) are served correctly
8. 404 handler returns JSON for API paths

Use Python's urllib or requests library for testing. Run the Flask app in a subprocess and test against it.

## Pitfalls

- **Using Python 3.14 with Flask 2.3.2** — `pkgutil.get_loader` was removed in Python 3.14; use a Python 3.11–3.13 venv (`python -m venv venv`) instead.
- **Not setting `credentials: 'include'`** in fetch requests — sessions won't persist
- **Not initializing the database** - app will crash on first request
- **Hardcoding the demo password in frontend** - remove any `DEFAULT_PASSWORD` constants from client JS
- **Using weak hashing (SHA-256 without salt)** - always use PBKDF2 or bcrypt
- **Not setting a proper SECRET_KEY** - Flask will warn and sessions won't persist across restarts
- **Skipping the 404 handler** - Flask's default HTML 404 breaks API clients