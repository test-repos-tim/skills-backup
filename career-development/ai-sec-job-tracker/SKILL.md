---
name: ai-sec-job-tracker
description: "Job search, application tracking, interview prep."
version: 1.0.0
author: Hermes Agent
tags: [career, ai-security, job-search, applications, interview-prep]
---

# AI Security Job Tracker Skill

## Purpose
Comprehensive job search management: company targeting, application tracking, interview preparation, offer comparison, and negotiation support for AI Security Consultant/Engineer roles.

## Target Role Definitions

### AI Security Engineer
- **Focus**: Building secure AI/ML systems, implementing guardrails, MLOps security
- **Keywords**: "AI Security Engineer", "ML Security Engineer", "LLM Security Engineer", "AI Safety Engineer"
- **Skills**: Python, PyTorch/TensorFlow, LLM APIs, Security frameworks, Cloud (AWS/Azure/GCP)
- **Typical Employers**: AI labs (OpenAI, Anthropic, Google DeepMind), Big Tech, Fintech, Defense

### AI Security Consultant
- **Focus**: Risk assessment, compliance, governance, client-facing advisory
- **Keywords**: "AI Security Consultant", "AI Risk Consultant", "AI Governance Consultant", "Responsible AI Consultant"
- **Skills**: Risk frameworks (NIST AI RMF, ISO 42001), Regulatory (EU AI Act), Audit, Communication
- **Typical Employers**: Big 4, Specialized consultancies (NCC Group, Trail of Bits), Boutique firms

### AI Red Teamer / Offensive AI Security
- **Focus**: Adversarial testing, jailbreaking, vulnerability research
- **Keywords**: "AI Red Teamer", "Offensive AI Security", "LLM Red Teamer", "Adversarial ML Researcher"
- **Skills**: Adversarial ML, Prompt injection, Jailbreak automation, Research publication
- **Typical Employers**: AI labs, Security firms, Bug bounty platforms, Research orgs

## Company Targeting Strategy

### Tier 1: Dream Companies (Apply Regardless of Openings)
- OpenAI, Anthropic, Google DeepMind, Microsoft AI, Meta FAIR
- NVIDIA, Apple ML, Amazon AGI
- Approach: Network → Referral → Cold email hiring managers

### Tier 2: AI Security Specialists
- Trail of Bits, NCC Group, Bishop Fox, Cobalt, HackerOne
- Robust Intelligence, HiddenLayer, Protect AI, Lakera
- Approach: Direct application + recruiter outreach

### Tier 3: Enterprise AI Adopters
- JPMorgan, Goldman Sachs (AI risk), Palantir, Databricks, Snowflake
- Healthcare (Epic, Cerner), Defense (Lockheed, Northrop)
- Approach: LinkedIn recruiter + job boards

### Tier 4: Consulting & Professional Services
- Deloitte, PwC, EY, KPMG (AI Assurance practices)
- Accenture, IBM Consulting, Guidehouse
- Approach: Campus/experienced hire portals

## Application Tracking Schema

```yaml
# ~/.hermes/ai-sec-career/job-applications.yaml
applications:
  - id: "app-001"
    company: "Anthropic"
    role: "AI Security Engineer"
    type: "Engineer"
    source: "Referral"  # Referral, LinkedIn, Company Site, Recruiter, Cold
    url: "https://jobs.anthropic.com/..."
    status: "applied"  # researched, applied, screening, technical, onsite, offer, rejected, withdrawn
    applied_date: "2025-01-15"
    contact:
      name: "Jane Smith"
      role: "Engineering Manager"
      email: "jane@anthropic.com"
      linkedin: "linkedin.com/in/janesmith"
    notes: "Referred by John Doe. Mentioned SecAI+ and RAG project."
    interview_stages:
      - stage: "Recruiter Screen"
        date: "2025-01-20"
        outcome: "passed"
        notes: "Discussed prompt injection taxonomy"
      - stage: "Technical - System Design"
        date: "2025-01-27"
        outcome: "pending"
    follow_up_date: "2025-01-28"
    salary_range: "$180k-$250k + equity"
    priority: "high"
```

## Interview Preparation Framework

### Stage 1: Recruiter Screen (30 min)
- **Prepare**: 2-min elevator pitch, salary expectations, timeline, visa status
- **Questions for them**: Team structure, current AI security challenges, tech stack

### Stage 2: Technical Phone Screen (60 min)
- **Coding**: LeetCode Medium (arrays, strings, graphs) - Python
- **AI Security Concepts**: 
  - Explain prompt injection types + mitigations
  - RAG security architecture
  - Adversarial attack/defense (FGSM, PGD, adversarial training)
  - Model deployment threats (model extraction, inversion)
- **Your Projects**: Deep-dive on 1 portfolio project

### Stage 3: System Design (60 min)
- **Scenario**: "Design a secure LLM gateway for enterprise"
- **Requirements**: Auth, rate limiting, prompt injection detection, PII redaction, audit logging, multi-model routing
- **Your Edge**: Connect to your forensics background (audit trails, chain of custody)

### Stage 4: Domain Deep-Dive (60 min)
- **AI Security Engineer**: Adversarial robustness, secure training, supply chain
- **AI Security Consultant**: Risk assessment methodology, EU AI Act mapping, client communication
- **Red Teamer**: Novel attack demonstration, responsible disclosure process

### Stage 5: Behavioral/Values (45 min)
- **STAR Stories**: 
  - "Time you found a critical security issue"
  - "Disagreement with stakeholder on risk"
  - "Learning a new technology under deadline"
  - "Ethical dilemma in security research"

### Stage 6: Hiring Manager/Values (30 min)
- **Focus**: Long-term vision, team fit, growth trajectory
- **Your Questions**: 
  - "What's the biggest AI security challenge your team faces?"
  - "How does security influence model release decisions?"
  - "What does success look like in 6 months?"

## Offer Evaluation Matrix

| Factor | Weight | Company A | Company B | Company C |
|--------|--------|-----------|-----------|-----------|
| Base Salary | 25% | | | |
| Equity/RSU | 20% | | | |
| Bonus | 10% | | | |
| Role Alignment | 15% | | | |
| Learning/Growth | 10% | | | |
| Team/Culture | 10% | | | |
| Location/Remote | 5% | | | |
| Mission Impact | 5% | | | |

## Negotiation Preparation

### Data Sources
- Levels.fyi (AI Security specific)
- Glassdoor, Blind, Wellfound
- H1B Data (h1bdata.info)
- Recruiter intel (ask: "What's the band for this level?")

### Scripts
- **Counter**: "Based on my SecAI+, Azure AI Engineer, and 3 production AI security projects, plus market data showing $X-$Y for this level, I'd like to discuss $Z."
- **Equity**: "Can you walk me through the equity valuation methodology and refresh policy?"
- **Signing Bonus**: "Given I'm leaving $X in unvested equity, a signing bonus of $Y would bridge the gap."

## Usage Commands

```bash
# Add new application
hermes skill run ai-sec-job-tracker --action=add --company="Anthropic" --role="AI Security Engineer" --type="Engineer" --source="Referral"

# Update status
hermes skill run ai-sec-job-tracker --action=update --id="app-001" --status="technical" --stage="System Design" --date="2025-01-27"

# List applications
hermes skill run ai-sec-job-tracker --action=list --status="active" --type="Engineer"

# Generate interview prep pack
hermes skill run ai-sec-job-tracker --action=prep-pack --id="app-001"

# Company research dossier
hermes skill run ai-sec-job-tracker --action=research --company="Anthropic"

# Salary benchmark
hermes skill run ai-sec-job-tracker --action=salary --role="AI Security Engineer" --location="Remote" --level="Senior"

# Offer comparison
hermes skill run ai-sec-job-tracker --action=compare --offers="app-001,app-005,app-012"

# Weekly pipeline review
hermes skill run ai-sec-job-tracker --action=pipeline-review

# Export to CSV/Notion
hermes skill run ai-sec-job-tracker --action=export --format=csv
```

## Data Files
- `~/.hermes/ai-sec-career/job-applications.yaml` - All applications
- `~/.hermes/ai-sec-career/target-companies.yaml` - Tiered company list with contacts
- `~/.hermes/ai-sec-career/interview-prep/` - Per-company prep docs
- `~/.hermes/ai-sec-career/offers.yaml` - Offer details for comparison

## Integration
- Pulls project talking points from `ai-sec-project-builder`
- Pulls certifications from `ai-sec-cert-research`
- Feeds `ai-sec-progress-dashboard` with pipeline metrics
- Cronjob: Daily 9am - follow-up reminders; Weekly Monday - pipeline review