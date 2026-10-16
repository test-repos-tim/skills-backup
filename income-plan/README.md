# income-plan — Security Audit Service

A zero-investment plan to generate $59+/month by offering automated website security scans to small businesses. Built for Kali Linux environments with Hermes Agent.

## What You Get

- **`SKILL.md`** — Project orchestration skill with phased roadmap
- **`scripts/security_scan.py`** — Automated scan script (nmap + whatweb + httpx + nuclei)
- **`templates/service-page.html`** — Ready-to-use service page
- **`planning/income_plan.md`** — Detailed 4-week plan

## Quick Start

```bash
# 1. Test the scan script on a safe domain
python3 ~/.hermes/skills/income-plan/scripts/security_scan.py example.com

# 2. View the generated report
cat ~/income-plan/reports/*/report.md

# 3. Customize the service page
# Edit templates/service-page.html — replace contact placeholders
```

## How to Make Money

1. **Offer free 5-minute scans** to local businesses (build trust + testimonials)
2. **Charge $50** for the full automated report
3. **Upsell $59/month** for ongoing monitoring (recurring revenue)
4. **One client** = AIProfitBoardroom membership paid

## Service Tiers

| Tier | Price | What's Included |
|------|-------|----------------|
| Basic Scan | $50 | One-time scan + summary report |
| Full Audit | $100 | Full scan + detailed remediation guide + 30-day follow-up |
| Monthly Monitoring | $59/mo | Automated monthly scan + trend tracking |

## Requirements

- Kali Linux (or any Linux with security tools)
- Tools: nmap, nuclei, httpx, whatweb (all pre-installed on Kali)
- Python 3 with `requests` (for nuclei)
- **Written authorization** from target owner before scanning

## Important Legal Notes

- **Only scan sites you own or have written authorization to test**
- This is a non-destructive, read-only scan
- Frame as "security check" not "pentest" for liability purposes
- Get paid via PayPal invoicing (50% upfront, 50% after delivery)

## Files

```
income-plan/
├── SKILL.md                          # Project orchestration skill
├── README.md                         # This file
├── scripts/
│   └── security_scan.py              # Automated scan + report generator
├── templates/
│   ├── service-page.html             # Service landing page
│   └── report-template.md            # (Embedded in security_scan.py)
└── planning/
    └── income_plan.md                # Detailed 4-week plan
```
