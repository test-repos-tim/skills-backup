---
name: web-security-assessment
description: A reusable methodology for conducting comprehensive web application security assessments
category: security-testing
---

# Web Security Assessment Skill

## Description
A reusable methodology for conducting comprehensive web application security assessments. Includes reconnaissance, vulnerability testing, manual verification when tools fail, and documentation.

## When to Use
- Assessing web applications for vulnerabilities
- Performing penetration testing on web targets
- Needing a structured approach that adapts to tool availability/environment constraints
- When you need to document findings systematically

## Tools Required
- HTTP framework testing tools (spidering, manual request crafting)
- SQL injection testing tools (SQLMap preferred)
- XSS testing tools (dalfox, XSSer, or manual fallback)
- Basic curl/wget for verification
- File writing capability for documentation

## Procedure

### 1. Initial Reconnaissance
```bash
# Spider the target to discover attack surface
http_framework_test --url <TARGET> --action spider --max-depth 2 --max-pages 50

# Alternative if spidering fails:
# Use manual URL discovery with common paths and linked file analysis
```

### 2. Security Headers Testing
```bash
# Test for missing security headers on key endpoints
http_framework_test --url <TARGET_ENDPOINT> --action request
# Check response for:
#   - X-Frame-Options
#   - X-Content-Type-Options  
#   - X-XSS-Protection
#   - Strict-Transport-Security
#   - Content-Security-Policy
```

### 3. Input Vector Testing
#### XSS Testing (Prioritize automated tools, fallback to manual)
```bash
# Try automated XSS scanning first
dalfox_xss_scan --url <TARGET_URL_WITH_PARAMS>
# If dalfox fails/not available:
xsser_scan --url <TARGET_URL_WITH_PARAMS> 
# If both fail, use manual testing:
http_framework_test --url <TARGET> --action request --method GET --data '{"PARAM":"<script>alert(\"XSS\")</script>"}'
# Look for unfiltered reflection in response
```

#### SQL Injection Testing
```bash
sqlmap_scan --url <TARGET_URL> --data "<PARAM1>=<VALUE1>&<PARAM2>=<VALUE2>" 
# If standard tests fail/injectable not found:
# Try increasing --level/--risk or using tamper scripts
# Consider blind/manual techniques if automated fails completely
```

### 4. Authentication & Authorization Testing
```bash
# Test for weak/default credentials
http_framework_test --url <LOGIN_ENDPOINT> --action request --method POST \
  --data '{"uid":"admin","passw":"admin","btnSubmit":"Login"}'

# Test admin panel access without authentication
http_framework_test --url <ADMIN_ENDPOINT> --action request

# Test for CSRF protection
http_framework_test --url <TARGET_ENDPOINT> --action request \
  --headers '{"Referer":"https://evil.com"}'
# If request processes normally, CSRF protection likely missing
```

### 5. Information Gathering & Exposure Testing
```bash
# Check for sensitive file exposure
http_framework_test --url <TARGET>/sensitive_file.ext --action request

# Look for exposed documentation/interfaces
# Common paths: /swagger/, /api-docs/, /debug/, /status/, /admin/, /backup/

# Test directory traversal if file upload/functionality exists
```

### 6. Documentation
Throughout the assessment, continuously document:
- Discovered URLs and endpoints
- Tested parameters and payloads
- Tool outputs (both success and failure)
- Manual test results and evidence
- Vulnerability details (location, impact, proof-of-concept)
- Remediation recommendations

Save to assessment file with sections:
- Initial Reconnaissance
- Specific Vulnerability Testing (XSS, SQLi, etc.)
- Auth/Access Control Testing
- Information Gathering
- Vulnerability Summary
- Recommendations

## Pitfalls & Troubleshooting
- **Tool availability issues**: Always have manual fallback methods ready (as demonstrated with dalfox/xsser failures)
- **False negatives**: Just because SQLMap says "not injectable" doesn't mean no SQLi exists - consider blind techniques
- **Session handling**: Maintain cookies/session state between tests when testing authenticated paths
- **Rate limiting**: Be mindful of request frequency to avoid DoS or blocking
- **Legal boundaries**: Only test targets you have explicit permission to assess

## Verification Steps
1. Manually verify each finding with at least two different methods when possible
2. Test both authenticated and unauthenticated access paths where applicable
3. Confirm false positives by testing known-safe parameters
4. Document evidence clearly (request/response snippets, tool output)
5. Have another tester review findings if possible

## Example Workflow
1. Spider target → discover 81 URLs, multiple forms
2. Test security headers → find missing X-Frame-Options, CSP, etc.
3. Attempt automated XSS scan → tools fail, switch to manual → find reflected XSS in search parameter
4. Run SQLMap → parameters not injectable with standard tests → note for manual blind testing
5. Test admin access → discover weak credentials (admin/admin)
6. Test CSRF → find missing protection via Referer header manipulation
7. Discover sensitive file exposure (/admin/clients.xls) and API docs (/swagger/)
8. Document all findings with evidence and recommendations

## Output Format
Assessment findings should be saved in a structured text file with:
- Executive summary
- Detailed findings per vulnerability category
- Proof of concept for each finding
- Risk ratings (Critical/High/Medium/Low)
- Specific remediation steps
- Tools used and techniques attempted