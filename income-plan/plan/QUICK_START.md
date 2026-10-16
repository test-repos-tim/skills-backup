# Income Plan Project — Complete Structure

## Files Created

### Core
- `SKILL.md` — Project orchestration skill with refined positioning
- `README.md` — Client-facing quick-start guide

### Plans
- `plan/income_plan.md` — Original 4-week plan ($50-59 tiers)
- `plan/income_plan_revised.md` — Refined plan ($197-497+ tiers, strategic advisory)

### Scripts
- `scripts/security_scan.py` — Automated scan engine (nmap + nuclei + httpx + whatweb)
- `scripts/threat_model.py` — Custom threat modeling engine with business-context analysis

### Templates
- `templates/service-page.html` — Service page for original $50-59 tier
- `templates/threat-model-report.md` — (Embedded in threat_model.py)

### Content
- `content/essays/threat-modeling-philosophy.md` — Positioning essay: "The Asymmetric Defender"

## Quick Commands

```bash
# Run threat model for a business
python3 ${HERMES_SKILL_DIR}/scripts/threat_model.py \
  --business "DESCRIPTION" \
  --tech "TECH STACK" \
  --report-path ./reports/

# Run security scan
python3 ${HERMES_SKILL_DIR}/scripts/security_scan.py example.com

# Schedule monthly client check-in
hermes cron create "0 9 1 * *" \
  "python3 ${HERMES_SKILL_DIR}/scripts/threat_model.py --business '...' --tech '...' --report-path ./reports/monthly-update.md"
```

## First Actions

1. Read `plan/income_plan_revised.md` for the full strategy
2. Read `content/essays/threat-modeling-philosophy.md` for your positioning angle
3. Test `scripts/threat_model.py` with a sample business
4. Publish the essay on LinkedIn/Twitter with: "Why most security work is commoditized — and how to escape the $50 race to the bottom"
5. Reach out to 5 SaaS founders you know (or on Twitter/Reddit) with: "Free 30-minute threat modeling session — I'll find one attack vector you haven't considered"
