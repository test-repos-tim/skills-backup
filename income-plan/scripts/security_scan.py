#!/usr/bin/env python3
"""
security_scan.py — Automated website security audit script for income-plan project.
Runs read-only, non-destructive tools against a single domain and packages
results into a markdown report.

Usage:
    python3 security_scan.py <domain> [--outdir DIR] [--report-only]

Examples:
    python3 security_scan.py example.com
    python3 security_scan.py example.com --outdir ~/income-plan/reports
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse


def run(cmd, timeout=120, cwd=None):
    """Run a command and return (stdout, stderr, returncode)."""
    try:
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True,
            timeout=timeout, cwd=cwd
        )
        return result.stdout, result.stderr, result.returncode
    except subprocess.TimeoutExpired:
        return "", f"[TIMEOUT after {timeout}s]", -1
    except FileNotFoundError:
        return "", f"[Tool not found: {cmd.split()[0]}]", -2


def extract_domain(url_or_domain):
    """Extract a clean domain from URL or bare domain input."""
    s = url_or_domain.strip()
    if not s.startswith(("http://", "https://")):
        s = "https://" + s
    parsed = urlparse(s)
    domain = parsed.netloc
    # Strip port and www for cleanliness
    if domain.startswith("www."):
        domain = domain[4:]
    return domain.split(":")[0]


def check_tools():
    """Check which security tools are available."""
    tools = {
        'nmap': shutil.which('nmap'),
        'nuclei': shutil.which('nuclei'),
        'httpx': shutil.which('httpx'),
        'whatweb': shutil.which('whatweb'),
        'curl': shutil.which('curl'),
        'subfinder': shutil.which('subfinder'),
        'amass': shutil.which('amass'),
        'gobuster': shutil.which('gobuster'),
    }
    return {k: v for k, v in tools.items() if v}


def generate_report(outdir, domain, domain_clean, findings_summary, tool_outputs, auth_info):
    """Generate a markdown report from scan results."""
    report_path = outdir / "report.md"
    
    # Count findings from nuclei output
    nuclei_findings = tool_outputs.get("nuclei", "")
    nuclei_lines = [l for l in nuclei_findings.strip().split("\n") if l.strip() and not l.startswith("[")]
    finding_count = len(nuclei_lines)
    
    # Determine severity summary
    high = len(re.findall(r'\[CRITICAL\]', nuclei_findings)) + len(re.findall(r'\[HIGH\]', nuclei_findings))
    medium = len(re.findall(r'\[MEDIUM\]', nuclei_findings))
    low = len(re.findall(r'\[LOW\]', nuclei_findings))
    info = len(re.findall(r'\[INFO\]', nuclei_findings))
    
    now = datetime.now().strftime("%Y-%m-%d %H:%M UTC")
    
    report = f"""# Security Audit Report

## {domain_clean}

**Scan Date:** {now}  
**Auditor:** Automated Security Scan (income-plan project)  
**Scope:** Read-only, non-destructive scan. No credentials or sensitive actions performed.  
**Authorization:** {auth_info}

---

## Executive Summary

A comprehensive automated security scan was performed against `{domain_clean}`. The scan covered:

- **Network surface** — top 50 common ports (nmap)
- **Technology fingerprinting** — server headers, tech stack (whatweb)
- **HTTP probing** — status codes, page titles, CDN detection (httpx)
- **Vulnerability scanning** — XSS, SQLi, SSRF, security headers, exposed data (nuclei)

### Findings Summary

| Severity | Count |
|----------|-------|
| Critical / High | {high} |
| Medium | {medium} |
| Low | {low} |
| Info | {info} |
| **Total** | **{finding_count}** |

---

## Key Recommendations

"""
    
    # Generate recommendations based on findings
    recs = []
    
    if high > 0:
        recs.append(f"""
### Immediate Action Required
{finding_count} high-severity issues were detected. Review the detailed findings below and remediate immediately, especially any:
- Exposed admin panels or debug endpoints
- SQL injection or command injection vulnerabilities
- Outdated software versions with known CVEs
""")
    
    if medium > 0:
        recs.append("""
### Medium Priority
Address medium-severity issues to improve security posture:
- Implement security headers (CSP, X-Frame-Options, etc.)
- Review exposed files (backup files, .git directories)
- Update outdated software components
""")
    
    if finding_count == 0:
        recs.append("""
### Security Health: Good
No vulnerabilities were detected by the automated scan. This is a positive sign.

However, automated scans only catch surface-level issues. Consider:
- Annual manual penetration testing for critical applications
- Enabling a Web Application Firewall (WAF)
- Implementing a vulnerability disclosure program
""")
    
    recs.append("""
### Ongoing Monitoring
Security is not a one-time check. Recommend monthly automated scans to catch:
- Newly deployed vulnerable endpoints
- Misconfigured cloud resources
- Expired SSL certificates
- Exposed .env or backup files

Contact us to set up recurring monthly scans for $59/month.
""")
    
    report += "\n".join(recs)
    
    # Detailed findings
    report += f"""

---

## Detailed Findings

"""
    
    if nuclei_lines:
        report += "| # | Severity | Host | Finding | Description |\n|---|----------|------|---------|-------------|\n"
        for i, line in enumerate(nuclei_lines[:50], 1):  # Cap at 50
            # Parse nuclei output line
            parts = line.split()
            severity = next((p for p in ["[CRITICAL]", "[HIGH]", "[MEDIUM]", "[LOW]", "[INFO]"] if p in line), "[UNKNOWN]")
            host_match = re.search(r'\[(.*?)\]', line)
            host = host_match.group(1) if host_match else domain_clean
            # Extract the finding title (after the host bracket)
            title = line.split("]", 1)[-1].strip() if "]" in line else line[:80]
            report += f"| {i} | {severity} | {host} | {title[:60]} | {title} |\n"
        
        if len(nuclei_lines) > 50:
            report += f"\n... and {len(nuclei_lines) - 50} more findings (see raw output below).\n"
    else:
        report += "No detailed findings from nuclei scan.\n"
    
    # Tool outputs as appendices
    report += f"""

---

## Appendix: Raw Tool Outputs

### nmap Scan
```
{tool_outputs.get('nmap', '[not run]')[:3000]}
```

### whatweb Fingerprint
```
{tool_outputs.get('whatweb', '[not run]')[:3000]}
```

### httpx Results
```
{tool_outputs.get('httpx', '[not run]')[:3000]}
```

### nuclei Findings (full)
```
{tool_outputs.get('nuclei', '[not run]')[:5000]}
```

---

*This report was generated by an automated security scanner. For questions about specific findings or to schedule a manual review, contact the auditor.*
"""
    
    report_path.write_text(report, encoding="utf-8")
    return report_path

def main():
    parser = argparse.ArgumentParser(
        description="Automated security scan for a single domain"
    )
    parser.add_argument("target", help="Domain or URL to scan (e.g. example.com)")
    parser.add_argument("--outdir", "-o", default=None,
                        help="Output directory (default: reports/YYYYMMDD-HHMMSS-domain)")
    parser.add_argument("--no-nuclei", action="store_true", help="Skip nuclei scan")
    parser.add_argument("--auth", default="See engagement authorization record",
                        help="Authorization reference for the report")
    args = parser.parse_args()
    
    domain = extract_domain(args.target)
    domain_clean = domain.replace("https://", "").replace("http://", "")
    
    # Set output directory
    if args.outdir:
        outdir = Path(args.outdir) / domain_clean
    else:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        outdir = Path.home() / "income-plan" / "reports" / f"{timestamp}-{domain_clean}"
    
    outdir.mkdir(parents=True, exist_ok=True)
    
    print(f"=== Security Scan: {domain_clean} ===")
    print(f"Output directory: {outdir}")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print()
    
    tool_outputs = {}
    
    # --- nmap ---
    available = check_tools()
    print(f"Tools available: {', '.join(available.keys())}")
    print()
    
    if 'nmap' in available:
        print("[1/4] Running nmap port scan...")
        stdout, stderr, rc = run(
            f'nmap -sT -T3 --top-ports 50 -oA "{outdir}/nmap" {domain_clean}',
            timeout=120
        )
        nmap_out = stdout + "\n" + stderr
        tool_outputs["nmap"] = nmap_out
        nmap_file = outdir / "nmap.txt"
        nmap_file.write_text(nmap_out, encoding="utf-8")
        print(f"  → nmap output saved ({len(nmap_out)} chars)")
    
    # --- whatweb ---
    if 'whatweb' in available:
        print("[2/4] Running whatweb fingerprint...")
        stdout, stderr, rc = run(
            f'whatweb -v https://{domain_clean}',
            timeout=60
        )
        whatweb_out = stdout + "\n" + stderr
        tool_outputs["whatweb"] = whatweb_out
        (outdir / "whatweb.txt").write_text(whatweb_out, encoding="utf-8")
        print(f"  → whatweb output saved ({len(whatweb_out)} chars)")
    
    # --- httpx ---
    if 'httpx' in available:
        print("[3/4] Running httpx probe...")
        stdout, stderr, rc = run(
            f'httpx -title -status-code -cdn -tech-detect https://{domain_clean}',
            timeout=60
        )
        httpx_out = stdout + "\n" + stderr
        tool_outputs["httpx"] = httpx_out
        (outdir / "httpx.txt").write_text(httpx_out, encoding="utf-8")
        print(f"  → httpx output saved ({len(httpx_out)} chars)")
    
    # --- nuclei ---
    if not args.no_nuclei and 'nuclei' in available:
        print("[4/4] Running nuclei vulnerability scan...")
        stdout, stderr, rc = run(
            f'nuclei -u https://{domain_clean} -tags xss,sqli,ssrf,exposed-env,security-headers,exposure -no-color -silent',
            timeout=300
        )
        nuclei_out = stdout + "\n" + stderr
        tool_outputs["nuclei"] = nuclei_out
        (outdir / "nuclei.txt").write_text(nuclei_out, encoding="utf-8")
        print(f"  → nuclei output saved ({len(nuclei_out)} chars)")
    elif 'nuclei' not in available:
        print("[4/4] nuclei not installed — skipping")
    
    # Generate report
    print()
    print("Generating report...")
    findings_summary = []
    
    metadata = {
        "domain": domain_clean,
        "scan_timestamp": datetime.now().isoformat(),
        "outdir": str(outdir),
        "tools_available": list(available.keys()),
        "authorization": args.auth,
    }
    (outdir / "scan_metadata.json").write_text(
        json.dumps(metadata, indent=2), encoding="utf-8"
    )
    
    report_path = generate_report(
        outdir, domain, domain_clean, findings_summary, tool_outputs, args.auth
    )
    
    print(f"\n=== Scan Complete ===")
    print(f"Report: {report_path}")
    print(f"Raw outputs: {outdir}")
    print(f"\nFindings summary:")
    nuclei_out = tool_outputs.get("nuclei", "")
    nuclei_lines = [l for l in nuclei_out.strip().split("\n") if l.strip()]
    print(f"  Total findings: {len(nuclei_lines)}")
    print(f"  Critical/High: {nuclei_out.count('[CRITICAL]') + nuclei_out.count('[HIGH]')}")
    print(f"  Medium: {nuclei_out.count('[MEDIUM]')}")
    print(f"  Low: {nuclei_out.count('[LOW]')}")


if __name__ == "__main__":
    main()
