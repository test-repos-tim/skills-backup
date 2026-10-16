---
name: nuclei_scan_ctf
title: Nuclei Scan Methodology for CTF
category: security-testing
description: |
  Workflow to run Nuclei scans with specific tags (csrf, xss, sqli) on a target, handle timeouts, interpret results, and decide next steps.
---

# Steps
1. **Update Nuclei templates** – `nuclei -update-templates` (ensures latest signatures).  
2. **Run scan** – `nuclei -u <target> -t "csrf,xss,sqli" -timeout 30s -silent`.  
3. **If timeout** – reduce `-rate`, increase `-timeout`, or split into multiple calls.  
4. **Review output** – zero matches may indicate no issues, outdated templates, or need for additional tags.  
5. **Follow-up** – run targeted fuzzers (Dalfox, SQLMap) or expand the tag set.  

# Troubleshooting
- **TimeoutError** – lower request volume (`-rate`) or timeout (`-timeout`).  
- **No matches** – run `nuclei -update-templates` and retry; consider custom templates.  
- **Custom parameters** – verify syntax in custom templates; keep them under `~/.local/nuclei-templates`.  

# Example Command
```bash
nuclei -u https://pentest-ground.com:4280 -t "csrf,xss,sqli" -timeout 30s -silent
```

This constitutes a reusable approach for CTF recon and vulnerability testing.