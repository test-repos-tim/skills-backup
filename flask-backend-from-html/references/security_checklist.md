# Security Checklist — Flask Backend from HTML

## Password Storage
- [ ] Passwords hashed with PBKDF2-HMAC-SHA256 (100,000+ iterations)
- [ ] Each password has a unique 64-character random salt
- [ ] Hash and salt stored separately in database
- [ ] `secrets.compare_digest` used for timing-safe comparison
- [ ] No plaintext passwords in code or database
- [ ] No hardcoded passwords in frontend JavaScript

## Session Management
- [ ] SECRET_KEY loaded from environment variable (not hardcoded)
- [ ] Session cookies have HttpOnly, Secure, SameSite flags
- [ ] Sessions expire after timeout

## API Security
- [ ] All POST/PUT/DELETE endpoints require authentication
- [ ] 401 returned for unauthenticated requests
- [ ] Input validated and sanitized server-side
- [ ] HTML output escaped to prevent XSS
- [ ] Content-Type headers set correctly on all responses

## Database Security
- [ ] SQL queries use parameterized statements (no string interpolation)
- [ ] Database file not in public web directory
- [ ] Connection properly closed on app teardown

## General
- [ ] No sensitive data in error messages
- [ ] Debug mode off in production
- [ ] HTTPS enforced (reverse proxy config)