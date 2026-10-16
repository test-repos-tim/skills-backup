# Ad-Hoc Verification Script Template

Run this with your project's virtualenv before deploying:

```python
#!/usr/bin/env python3
"""Ad-hoc verification for Flask research apps."""
import sys, os, json, requests, time, subprocess

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJECT_DIR)

# Test 1: File structure
print("1. File structure...")
required_files = ["app.py", "requirements.txt", "Procfile", "runtime.txt", "wsgi.py"]
for f in required_files:
    assert os.path.exists(f"{PROJECT_DIR}/{f}"), f"Missing: {f}"
print("   PASS: All files present")

# Test 2: Dependencies
print("2. Dependencies...")
with open(f"{PROJECT_DIR}/requirements.txt") as f:
    reqs = f.read().lower()
for pkg in ["flask", "gunicorn", "flask-login", "bcrypt"]:
    assert pkg in reqs, f"Missing package: {pkg}"
print("   PASS: All dependencies present")

# Test 3: Config files
print("3. Config files...")
with open(f"{PROJECT_DIR}/Procfile") as f:
    procfile = f.read().strip()
assert "$PORT" in procfile, "Procfile must use $PORT"
assert "gunicorn" in procfile, "Procfile must use gunicorn"

with open(f"{PROJECT_DIR}/runtime.txt") as f:
    runtime = f.read().strip()
assert "python" in runtime.lower(), "runtime.txt must specify Python version"
print("   PASS: Config files correct")

# Test 4: App imports
print("4. App imports...")
import app as app_module
assert hasattr(app_module, "app"), "Missing Flask app instance"
assert hasattr(app_module, "init_db"), "Missing init_db function"
print("   PASS: App module imports correctly")

# Test 5: End-to-end
print("5. End-to-end (auth + research)...")
env = {**os.environ, "PORT": "5557", "SECRET_KEY": "verify-test-secret"}
proc = subprocess.Popen([sys.executable, "app.py"], env=env, cwd=PROJECT_DIR)
time.sleep(3)

try:
    # Register
    r = requests.post("http://localhost:5557/api/auth/register",
                      json={"email": "verify@test.com", "password": "testpass123"})
    assert r.json().get("success"), "Registration failed"

    # Login
    r = requests.post("http://localhost:5557/api/auth/login",
                      json={"email": "verify@test.com", "password": "testpass123"})
    assert r.json().get("success"), "Login failed"

    # Create session (need cookies)
    session = requests.Session()
    session.post("http://localhost:5557/api/auth/login",
                 json={"email": "verify@test.com", "password": "testpass123"})
    r = session.post("http://localhost:5557/api/sessions",
                     json={"title": "Test Session"})
    assert "session_id" in r.json(), "Session creation failed"

    print("   PASS: Auth and session flow works")
finally:
    proc.terminate()
    proc.wait()

# Test 6: Web UI
print("6. Web UI...")
# Start app again
proc = subprocess.Popen([sys.executable, "app.py"], env=env, cwd=PROJECT_DIR)
time.sleep(3)
try:
    r = requests.get("http://localhost:5557/login")
    assert "title" in r.text.lower(), "Login page failed to load"
    print("   PASS: Web UI renders")
finally:
    proc.terminate()
    proc.wait()

print("\n=== All verification tests passed! ===")
```

## What This Verifies

1. **File structure** - All deployment files present
2. **Dependencies** - Critical packages in requirements.txt
3. **Config files** - Procfile uses $PORT, runtime.txt has Python version
4. **Module imports** - app.py can be imported without errors
5. **Auth flow** - Register/login works, creates sessions
6. **Web UI** - Login page renders correctly

## Running

```bash
# Activate your virtualenv
source venv/bin/activate

# Run verification
python verify.py

# Or inline:
python -c "
import subprocess, sys, os
os.chdir('/path/to/your-project')
subprocess.check_call([sys.executable, '-m', 'pytest', 'verify.py'])
"
```

## Notes

- Tests run on port 5557 to avoid conflicts
- Temporary database is created in /tmp
- Processes are terminated cleanly after each test
- Cookie-based sessions are used for auth testing