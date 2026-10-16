---
name: ai-sec-career-roadmap
description: "AI Security career roadmap: certs, projects, portfolio, job."
version: 1.0.0
author: Hermes Agent
tags: [career, ai-security, roadmap, certifications, portfolio, job-search]
---

# AI Security Career Roadmap - Master Skill

## Overview
This skill provides a complete structured system for transitioning into AI Security (AI Security Consultant / AI Security Engineer) leveraging your Level 7 Cybersecurity & Digital Forensics degree.

## Architecture: Multi-Skill System

### Core Skills (to be created)
1. **`ai-sec-cert-research`** - Certification landscape research & recommendation engine
2. **`ai-sec-learning-path`** - Structured curriculum with milestones & prerequisites
3. **`ai-sec-project-builder`** - Portfolio project templates & guidance
4. **`ai-sec-portfolio-site`** - Portfolio website generator & deployment
5. **`ai-sec-linkedin-content`** - LinkedIn content calendar & post generator
6. **`ai-sec-job-tracker`** - Job search, application tracking, interview prep
7. **`ai-sec-progress-dashboard`** - Master dashboard unifying all tracking

### Master Controller
- **`ai-sec-career-orchestrator`** - Coordinates all sub-skills, provides unified CLI

## Certification Research Findings (2024-2025)

### Tier 1: HIGH VALUE - Direct AI Security Focus
| Cert | Provider | Level | Cost | Time | Relevance to Your Background |
|------|----------|-------|------|------|------------------------------|
| **AAISM** (Advanced in AI Security Management) | ISACA | Advanced | ~$760 | 2-3 mo | **PERFECT** - Requires CISM/CISSP, builds on your sec mgmt knowledge |
| **AAIA** (Advanced in AI Audit) | ISACA | Advanced | ~$760 | 2-3 mo | **EXCELLENT** - Leverages your audit/forensics background |
| **SecAI+** | CompTIA | Intermediate | ~$400 | 1-2 mo | **GOOD** - New AI+csecurity hybrid, practical |
| **Azure AI Engineer Associate (AI-102)** | Microsoft | Intermediate | $165 | 1-2 mo | **GOOD** - Cloud AI implementation focus |
| **SEC595** (Applied Data Science & AI/ML for Cyber) | SANS/GIAC | Advanced | ~$8,500 | 6 days + study | **EXCELLENT** - Hands-on, technical depth, GIAC cert |

### Tier 2: FOUNDATIONAL - AI/ML Fundamentals
| Cert | Provider | Level | Cost | Time | Notes |
|------|----------|-------|------|------|-------|
| **AI Fundamentals** | CompTIA | Entry | ~$150 | 2-4 wks | Baseline AI literacy |
| **AI Security (Coursera/Infosec)** | Coursera | Entry | $49/mo | 8 hrs | Good intro, not a "cert" per se |
| **Google Cloud AI/ML Certs** | Google | Various | Various | Variable | Cloud-specific |

### Tier 3: SPECIALIZED/NICHE
- **OWASP AI Exchange** - Free, community-driven, excellent reference
- **NIST AI RMF Training** - Free, regulatory compliance focus
- **MITRE ATLAS** - Free, AI threat modeling framework

## Recommended Path for YOUR Profile

### Phase 1 (Months 1-2): Foundations & Quick Wins
- [ ] CompTIA AI Fundamentals (baseline)
- [ ] Coursera AI Security course (8 hrs)
- [ ] Complete OWASP AI Exchange guide
- [ ] Start NIST AI RMF self-study

### Phase 2 (Months 3-5): Core Technical Certifications
- [ ] **SecAI+** (CompTIA) - bridges your sec + AI gap
- [ ] **Azure AI Engineer (AI-102)** - cloud AI implementation
- [ ] Build 2-3 portfolio projects during this phase

### Phase 3 (Months 6-9): Advanced/Specialized
- [ ] **AAISM** (ISACA) - requires CISM/CISSP (do you have?)
- [ ] **AAIA** (ISACA) - leverages your forensics/audit degree
- [ ] **SEC595 / GIAC** - if budget allows, highest technical credibility

### Phase 4 (Months 9-12): Portfolio & Job Hunt
- [ ] 5+ polished portfolio projects
- [ ] Deployed portfolio website
- [ ] LinkedIn content strategy active
- [ ] Active applications + interview prep

## Skill Interface

### Commands (via ai-sec-career-orchestrator)
```bash
# Certification research
hermes skill run ai-sec-cert-research --action=recommend --profile="level7-cyber-forensics"

# Generate learning path
hermes skill run ai-sec-learning-path --action=create --phase=1

# Create portfolio project
hermes skill run ai-sec-project-builder --action=new --type="ai-red-teaming"

# Generate LinkedIn content
hermes skill run ai-sec-linkedin-content --action=generate --topic="ai-security-trends"

# Track job application
hermes skill run ai-sec-job-tracker --action=add --company="Anthropic" --role="AI Security Engineer"

# View unified dashboard
hermes skill run ai-sec-progress-dashboard --action=show
```

## Data Storage
All progress stored in `~/.hermes/ai-sec-career/`:
- `certifications.yaml` - Track cert progress
- `learning-path.yaml` - Milestones & completions
- `projects/` - Project metadata & artifacts
- `job-applications.yaml` - Application tracking
- `linkedin-posts.yaml` - Content calendar
- `dashboard.db` - SQLite for unified queries

## Integration Points
- **cronjob** - Weekly progress review, LinkedIn scheduling
- **skills_list** - Discover sub-skills
- **session_search** - Recall past research/decisions
- **memory** - Store preferences (target companies, salary, location)