---
name: ai-sec-career-orchestrator
description: "Master controller for AI Security career: unified CLI."
version: 1.0.0
author: Hermes Agent
tags: [career, ai-security, orchestrator, cli, workflow]
---

# AI Security Career Orchestrator

## Purpose
Master control skill providing unified CLI, automated workflows, and cross-skill coordination for the entire AI Security career transition system.

## Sub-Skills Managed
1. `ai-sec-cert-research` - Certification research & recommendations
2. `ai-sec-learning-path` - Structured curriculum & milestones
3. `ai-sec-project-builder` - Portfolio project templates
4. `ai-sec-portfolio-site` - Portfolio website generator
5. `ai-sec-linkedin-content` - LinkedIn content calendar
6. `ai-sec-job-tracker` - Job search & application tracking
7. `ai-sec-progress-dashboard` - Unified progress dashboard

## Unified CLI Commands

### Daily Workflow (Run each morning)
```bash
# Complete daily briefing
hermes skill run ai-sec-career-orchestrator --action=daily-briefing

# Output includes:
# - Today's learning tasks (from learning-path)
# - Pipeline follow-ups due (from job-tracker)
# - LinkedIn engagement reminder
# - Project next steps
# - Dashboard readiness score
```

### Weekly Workflow (Run Sunday)
```bash
# Complete weekly review & planning
hermes skill run ai-sec-career-orchestrator --action=weekly-review

# Does:
# 1. Refresh dashboard data from all skills
# 2. Generate weekly progress report
# 3. Plan next week's learning tasks
# 4. Generate LinkedIn content for next week
# 5. Identify pipeline actions needed
# 6. Update readiness score & targets
```

### Monthly Workflow (Run 1st of month)
```bash
# Monthly strategic review
hermes skill run ai-sec-career-orchestrator --action=monthly-review

# Does:
# 1. Deep-dive on readiness trends
# 2. Certification market demand refresh
# 3. Skill self-assessment prompt
# 4. Target company list review
# 5. Budget review (cert costs, tools)
# 6. Strategy adjustment recommendations
```

## Phase Transition Automation

```bash
# Check if ready for next phase
hermes skill run ai-sec-career-orchestrator --action=phase-check

# Auto-transition when criteria met
hermes skill run ai-sec-career-orchestrator --action=phase-advance --to=3
```

## Quick Actions

```bash
# Start new project from template
hermes skill run ai-sec-career-orchestrator --action=start-project --template="secure-rag-pipeline"

# Log cert achievement (updates all skills)
hermes skill run ai-sec-career-orchestrator --action=log-cert --cert="SecAI+" --date="2025-03-15"

# Add job application (updates tracker + dashboard)
hermes skill run ai-sec-career-orchestrator --action=apply --company="Anthropic" --role="AI Security Engineer"

# Generate interview prep for application
hermes skill run ai-sec-career-orchestrator --action=prep-interview --app-id="app-001"

# Publish LinkedIn post (from calendar)
hermes skill run ai-sec-career-orchestrator --action=publish-linkedin --week=5 --day=mon

# Deploy portfolio updates
hermes skill run ai-sec-career-orchestrator --action=deploy-portfolio
```

## Status & Reporting

```bash
# Full system status
hermes skill run ai-sec-career-orchestrator --action=status

# Readiness score with breakdown
hermes skill run ai-sec-career-orchestrator --action=readiness

# Export all data for backup/migration
hermes skill run ai-sec-career-orchestrator --action=export-all --format=zip

# Import data (new machine/setup)
hermes skill run ai-sec-career-orchestrator --action=import-all --path="./backup.zip"
```

## Automated Cronjobs (Configure Once)

```bash
# Install all cronjobs
hermes skill run ai-sec-career-orchestrator --action=install-cronjobs

# Creates:
# - Daily 7:00  : daily-briefing (notify via Hermes)
# - Sunday 19:00: weekly-review (notify via Hermes)  
# - 1st 09:00   : monthly-review (notify via Hermes)
# - Daily 08:00 : pipeline follow-up check
# - Weekly Mon 09:00: LinkedIn content generation
```

## Configuration

```yaml
# ~/.hermes/ai-sec-career/config.yaml
profile:
  background: "level7-cyber-forensics"
  target_roles: ["AI Security Engineer", "AI Security Consultant"]
  target_companies_tier1: ["Anthropic", "OpenAI", "Google DeepMind", "Trail of Bits"]
  cert_budget: 5000  # USD
  timeline_months: 12
  hours_per_week: 15

preferences:
  notification_channel: "hermes"  # hermes, email, telegram
  linkedin_scheduling_tool: "typefully"  # typefully, buffer, hootsuite, manual
  portfolio_deploy: "vercel"
  dashboard_format: "terminal"  # terminal, web, json

phase_criteria:
  phase1_complete:
    - cert: "AI Fundamentals"
    - projects: 3
    - github_repos: 3
  phase2_complete:
    - certs: ["SecAI+", "Azure AI Engineer"]
    - projects: 3
  phase3_complete:
    - advanced_cert: true  # AAISM or AAIA or GCDA
    - blog_posts: 3
  phase4_complete:
    - portfolio_site: true
    - applications: 50
    - interviews: 10
    - offer: true
```

## Data Flow Architecture

```
┌─────────────────┐     ┌──────────────────┐     ┌────────────────────┐
│ cert-research   │────▶│ learning-path    │────▶│ project-builder    │
│ (recommendations)│     │ (curriculum)     │     │ (project specs)    │
└─────────────────┘     └──────────────────┘     └─────────┬──────────┘
                                                           │
                      ┌─────────────────┐                  │
                      │ portfolio-site  │◀─────────────────┘
                      │ (case studies)  │
                      └────────┬────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        ▼                      ▼                      ▼
┌───────────────┐     ┌─────────────────┐     ┌──────────────┐
│ linkedin-     │     │ job-tracker     │     │ progress-    │
│ content       │     │ (applications)  │     │ dashboard    │
│ (posts)       │     │                 │     │ (unified)    │
└───────────────┘     └─────────────────┘     └──────────────┘
        │                      │                      │
        └──────────────────────┼──────────────────────┘
                               ▼
                    ┌─────────────────────┐
                    │ ai-sec-career-      │
                    │ orchestrator        │
                    │ (master control)    │
                    └─────────────────────┘
```

## Emergency Commands

```bash
# Panic: "I have an interview tomorrow!"
hermes skill run ai-sec-career-orchestrator --action=interview-emergency --company="Anthropic" --role="AI Security Engineer"

# Panic: "I need to pivot strategy"
hermes skill run ai-sec-career-orchestrator --action=strategy-pivot --reason="budget_cut" --new-timeline=18

# Panic: "Data corruption"
hermes skill run ai-sec-career-orchestrator --action=repair-data --backup-last="2025-01-10"
```

## Integration Points
- **Hermes Cron**: All scheduled workflows
- **Hermes Memory**: User preferences, API keys, tokens
- **Hermes Session Search**: Historical decisions, research
- **External**: GitHub (projects), Vercel (portfolio), LinkedIn API (metrics), Job boards (via RSS/API)