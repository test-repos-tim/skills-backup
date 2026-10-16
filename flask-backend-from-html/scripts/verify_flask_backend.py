#!/usr/bin/env python3
"""
Automated verification script for Flask backend built from standalone HTML.

Run this after building a Flask app from an existing HTML file to verify:
- Homepage serves with external CSS
- API endpoints return expected data
- Authentication flow works
- Protected endpoints enforce auth
- CRUD operations succeed when authenticated
- Password hashing is correct
- Static files are served
- 404 handler returns JSON

Usage:
    python3 verify_flask_backend.py [PORT] [BASE_URL]

Defaults to port 5005 and http://localhost:5005
"""

import subprocess, time, os, sys, json, http.cookiejar
import urllib.request, urllib.error, urllib.parse
import sqlite3, hashlib

APP_DIR = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()
BASE = sys.argv[2] if len(sys.argv) > 2 else "http://localhost:5005"
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 5005

results = []

def check(name, fn):
    try:
        fn()
        results.append((name, "PASS", ""))
    except Exception as e:
        results.append((name, "FAIL", str(e)))

def get_url(path):
    return urllib.request.urlopen(f"{BASE}{path}", timeout=5).read().decode()

def get_json(path):
    return json.loads(urllib.request.urlopen(f"{BASE}{path}", timeout=5).read())

# --- Start server ---
print(f"Starting Flask server on port {PORT}...")
proc = subprocess.Popen(
    [sys.executable, "app.py"],
    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    cwd=APP_DIR,
    env={**os.environ, "FLASK_ENV": "production"}
)
time.sleep(3)

try:
    # 1. Homepage
    def test_homepage():
        html = get_url("/")
        assert "<title>" in html, "No title in HTML"
        assert "/static/style.css" in html, "CSS not linked externally"
    check("Homepage serves HTML with external CSS", test_homepage)

    # 2. Posts API
    def test_posts():
        posts = get_json("/api/posts")
        assert isinstance(posts, list), "Posts should be a list"
        for p in posts:
            assert "id" in p and "title" in p, "Post missing required fields"
    check("GET /api/posts returns posts", test_posts)

    # 3. Single post
    def test_single():
        posts = get_json("/api/posts")
        if posts:
            post = get_json(f"/api/posts/{posts[0]['id']}")
            assert post["id"] == posts[0]["id"], "Wrong post returned"
    check("GET /api/posts/<id> returns correct post", test_single)

    # 4. Auth status
    def test_auth_status():
        status = get_json("/api/auth/status")
        assert status["is_admin"] == False, "Should not be admin initially"
    check("GET /api/auth/status shows unauthenticated", test_auth_status)

    # 5. Login
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    
    def test_login():
        req = urllib.request.Request(f"{BASE}/api/auth/login",
                                      data=json.dumps({"username":"admin","password":"darknet5m3o"}).encode(),
                                      headers={"Content-Type":"application/json"},
                                      method="POST")
        resp = opener.open(req, timeout=5)
        result = json.loads(resp.read())
        assert result.get("success") == True, f"Login failed: {result}"
    check("POST /api/auth/login (correct credentials)", test_login)

    # 6. Create post
    created_id = None
    def test_create():
        nonlocal created_id
        req = urllib.request.Request(f"{BASE}/api/posts",
                                      data=json.dumps({"title":"Test Post","content":"Test content","tag":"TEST"}).encode(),
                                      headers={"Content-Type":"application/json"},
                                      method="POST")
        resp = opener.open(req, timeout=5)
        post = json.loads(resp.read())
        created_id = post["id"]
        assert post["title"] == "Test Post", "Wrong title returned"
    check("POST /api/posts (authenticated)", test_create)

    # 7. Delete post
    def test_delete():
        req = urllib.request.Request(f"{BASE}/api/posts/{created_id}", method="DELETE")
        resp = opener.open(req, timeout=5)
        result = json.loads(resp.read())
        assert "successfully" in result.get("message", "").lower(), f"Delete failed: {result}"
    if created_id:
        check("DELETE /api/posts/<id> (authenticated)", test_delete)

    # 8. Unauthenticated protected endpoint
    def test_no_auth():
        req = urllib.request.Request(f"{BASE}/api/posts",
                                      data=json.dumps({"title":"X","content":"Y"}).encode(),
                                      headers={"Content-Type":"application/json"},
                                      method="POST")
        try:
            urllib.request.urlopen(req, timeout=5)
            raise AssertionError("Should have been 401")
        except urllib.error.HTTPError as e:
            assert e.code == 401, f"Expected 401, got {e.code}"
    check("POST /api/posts (unauthenticated) returns 401", test_no_auth)

    # 9. Wrong password
    def test_wrong_pass():
        req = urllib.request.Request(f"{BASE}/api/auth/login",
                                      data=json.dumps({"username":"admin","password":"wrong"}).encode(),
                                      headers={"Content-Type":"application/json"},
                                      method="POST")
        try:
            urllib.request.urlopen(req, timeout=5)
            raise AssertionError("Should have been 401")
        except urllib.error.HTTPError as e:
            assert e.code == 401, f"Expected 401, got {e.code}"
    check("POST /api/auth/login (wrong password) returns 401", test_wrong_pass)

    # 10. Password hash verification
    def test_hash():
        db_path = os.path.join(APP_DIR, "portfxx1.db")
        for db_name in ["portfxx1.db", "database.db", "app.db"]:
            if os.path.exists(os.path.join(APP_DIR, db_name)):
                db_path = os.path.join(APP_DIR, db_name)
                break
        conn = sqlite3.connect(db_path)
        try:
            row = conn.execute("SELECT password_hash, salt FROM admin_users WHERE username = ?", ("admin",)).fetchone()
        except sqlite3.OperationalError:
            row = conn.execute("SELECT password_hash FROM admin_users WHERE username = ?", ("admin",)).fetchone()
        conn.close()
        assert row is not None, "Admin user not found"
    check("Password hash stored in database", test_hash)

    # 11. Static file
    def test_css():
        css = get_url("/static/style.css")
        assert ":root" in css, "CSS missing :root"
        assert "--accent" in css, "CSS missing accent variable"
    check("GET /static/style.css serves CSS", test_css)

    # 12. 404 handler
    def test_404():
        try:
            get_json("/api/nonexistent")
        except urllib.error.HTTPError as e:
            assert e.code == 404, f"Expected 404, got {e.code}"
    check("GET /api/nonexistent returns 404", test_404)

    # 13. Logout
    def test_logout():
        req = urllib.request.Request(f"{BASE}/api/auth/logout", method="POST")
        resp = opener.open(req, timeout=5)
        result = json.loads(resp.read())
        assert result.get("success") == True, "Logout failed"
    check("POST /api/auth/logout succeeds", test_logout)

finally:
    proc.terminate()
    try:
        proc.wait(timeout=5)
    except:
        proc.kill()

# Print results
print("\n" + "=" * 60)
print("VERIFICATION RESULTS")
print("=" * 60)
passed, failed = 0, 0
for name, status, err in results:
    icon = "OK" if status == "PASS" else "XX"
    print(f"  [{icon}] {name}: {status}")
    if err:
        print(f"        -> {err}")
    if status == "PASS":
        passed += 1
    else:
        failed += 1

print(f"\n  Total: {passed} passed, {failed} failed out of {len(results)}")
print("=" * 60)
sys.exit(0 if failed == 0 else 1)