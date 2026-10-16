---
name: ai-sec-cert-research
description: "Research AI Security certs, match profile, recommend path."
version: 1.0.0
author: Hermes Agent
tags: [career, ai-security, certifications, research, recommendations]
---

# AI Security Certification Research Skill

## Purpose
Research, evaluate, and recommend AI Security certifications based on your Level 7 Cybersecurity & Digital Forensics background, career goals (AI Security Consultant/Engineer), and current market demands.

## Certification Database (2024-2025)

### TIER 1: HIGH PRIORITY - Direct AI Security Alignment

#### 1. ISACA AAISM (Advanced in AI Security Management)
- **Prerequisites**: CISM or CISSP (5+ years security management)
- **Cost**: ~$760 (member) / $950 (non-member)
- **Exam**: 150 questions, 4 hours
- **Domains**: AI Governance, AI Risk Management, AI Security Operations, AI Compliance
- **Your Fit**: **EXCELLENT** - Builds directly on security management experience
- **Timeline**: 2-3 months prep
- **ROI**: High - Recognized at enterprise level, leadership roles

#### 2. ISACA AAIA (Advanced in AI Audit)
- **Prerequisites**: CISA, CIA, or CPA (audit experience)
- **Cost**: ~$760 (member) / $950 (non-member)
- **Exam**: 150 questions, 4 hours
- **Domains**: AI Audit Planning, AI Risk Assessment, AI Control Testing, AI Governance Audit
- **Your Fit**: **EXCELLENT** - Directly leverages your digital forensics/audit degree
- **Timeline**: 2-3 months prep
- **ROI**: High - Niche expertise, consulting-friendly

#### 3. CompTIA SecAI+
- **Prerequisites**: Security+ recommended, 2+ years security experience
- **Cost**: ~$400
- **Exam**: 90 questions, 90 minutes
- **Domains**: AI/ML Fundamentals, AI Threat Landscape, Securing AI Systems, AI Governance
- **Your Fit**: **GOOD** - Bridges security + AI gap, practical focus
- **Timeline**: 1-2 months prep
- **ROI**: Good - Vendor-neutral, growing recognition

#### 4. Microsoft Azure AI Engineer Associate (AI-102)
- **Prerequisites**: Azure fundamentals, programming (Python/C#)
- **Cost**: $165
- **Exam**: 40-60 questions, 100 minutes
- **Domains**: Azure AI Services, Computer Vision, NLP, Knowledge Mining, Responsible AI
- **Your Fit**: **GOOD** - Cloud AI implementation, practical skills
- **Timeline**: 1-2 months prep
- **ROI**: Good - Cloud-specific, high demand in Azure shops

#### 5. SANS SEC595 / GIAC GCDA (Applied Data Science & AI/ML for Cybersecurity)
- **Prerequisites**: Strong Python, statistics, security background
- **Cost**: ~$8,500 (course + cert) / $949 (cert attempt only)
- **Format**: 6-day intensive + hands-on labs
- **Domains**: ML for threat detection, anomaly detection, AI/ML model security, adversarial ML
- **Your Fit**: **EXCELLENT** - Deepest technical credibility, hands-on
- **Timeline**: 6 days course + 2-3 months study
- **ROI**: Highest technical credibility - but expensive

### TIER 2: FOUNDATIONAL - AI Literacy Base

#### 6. CompTIA AI Fundamentals
- **Prerequisites**: None
- **Cost**: ~$150
- **Exam**: 75 questions, 60 minutes
- **Domains**: AI Concepts, ML Basics, AI Applications, Ethics/Governance
- **Your Fit**: **BASELINE** - Quick win, establishes AI literacy
- **Timeline**: 2-4 weeks
- **ROI**: Low standalone, good foundation

#### 7. Coursera AI Security (Infosec)
- **Prerequisites**: None
- **Cost**: $49/mo (Coursera Plus) or free audit
- **Format**: 6 modules, ~8 hours
- **Certificate**: Course completion (not industry cert)
- **Your Fit**: **GOOD STARTER** - Structured intro
- **Timeline**: 1-2 weeks

### TIER 3: FREE/COMMUNITY - Reference & Frameworks

#### 8. OWASP AI Exchange
- **Cost**: Free
- **Format**: Living document, community-driven
- **Topics**: AI threats, controls, testing, governance
- **Use Case**: Reference implementation, interview talking points

#### 9. NIST AI RMF (Risk Management Framework)
- **Cost**: Free
- **Format**: NIST publication + self-study
- **Topics**: Govern, Map, Measure, Manage AI risks
- **Use Case**: Regulatory compliance, government/defense roles

#### 10. MITRE ATLAS (Adversarial Threat Landscape for AI Systems)
- **Cost**: Free
- **Format**: Knowledge base of AI/ML tactics/techniques
- **Use Case**: Threat modeling, red teaming, interview depth

## Recommendation Engine Logic

### For YOUR Profile (Level 7 Cybersecurity & Digital Forensics):

```
IF has_CISM_or_CISSP:
    PRIMARY_PATH = [AAISM, AAIA]  # Leverage existing creds
ELIF has_CISA_or_audit_background:
    PRIMARY_PATH = [AAIA, SecAI+]  # Leverage forensics/audit degree
ELSE:
    PRIMARY_PATH = [SecAI+, AI-102, AI Fundamentals]  # Build from ground up

ALWAYS_INCLUDE = [OWASP AI Exchange, NIST AI RMF, MITRE ATLAS]  # Free knowledge base

PORTFOLIO_BOOSTERS = [SEC595/GIAC]  # If budget allows
```

## Usage Commands

```bash
# Get personalized recommendations
hermes skill run ai-sec-cert-research --action=recommend --profile="level7-cyber-forensics"

# Compare specific certs
hermes skill run ai-sec-cert-research --action=compare --certs="AAISM,SecAI+,AI-102"

# Get study plan for a cert
hermes skill run ai-sec-cert-research --action=study-plan --cert="AAISM"

# Check prerequisites
hermes skill run ai-sec-cert-research --action=prereqs --cert="AAISM"

# Market demand analysis
hermes skill run ai-sec-cert-research --action=market-demand --role="AI Security Engineer"

# Export certification tracker (YAML)
hermes skill run ai-sec-cert-research --action=export --format=yaml
```

## Data Files Created
- `~/.hermes/ai-sec-career/certifications.yaml` - Your certification tracker
- `~/.hermes/ai-sec-career/cert-database.json` - Full certification database
- `~/.hermes/ai-sec-career/recommendations.json` - Personalized recommendations

## Integration
- Feeds into `ai-sec-learning-path` for curriculum generation
- Tracks progress in `ai-sec-progress-dashboard`
- Cronjob: Monthly market demand refresh