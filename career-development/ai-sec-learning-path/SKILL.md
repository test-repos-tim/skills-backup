---
name: ai-sec-learning-path
description: "Structured AI Security curriculum with milestones."
version: 1.0.0
author: Hermes Agent
tags: [career, ai-security, learning-path, curriculum, milestones]
---

# AI Security Learning Path Skill

## Purpose
Generate structured, phase-based learning curricula with milestones, prerequisites, resource links, and time estimates. Takes certification recommendations from `ai-sec-cert-research` and breaks them into weekly actionable steps.

## Phase Structure (12-Month Roadmap)

### PHASE 1: Foundations (Months 1-2) - "AI Literacy & Security Bridge"
**Goal**: Establish AI/ML fundamentals + connect to your security background

#### Week 1-2: AI/ML Foundations
- [ ] CompTIA AI Fundamentals exam prep (official study guide)
- [ ] Coursera "AI For Everyone" (Andrew Ng) - audit free
- [ ] Key concepts: Supervised/Unsupervised/RL, Neural Networks, Transformers
- **Deliverable**: Pass AI Fundamentals practice exam >85%

#### Week 3-4: AI Security Landscape
- [ ] Coursera AI Security (Infosec) - 6 modules, 8 hrs
- [ ] OWASP AI Exchange - read entire guide
- [ ] MITRE ATLAS - browse top 10 techniques
- **Deliverable**: Write 1-page summary: "How my forensics background applies to AI threats"

#### Week 5-6: Risk & Governance Frameworks
- [ ] NIST AI RMF 1.0 - complete read + workbook
- [ ] ISO/IEC 42001 (AI Management Systems) - executive summary
- [ ] EU AI Act - key provisions for high-risk AI
- **Deliverable**: Map NIST AI RMF functions to your forensics methodology

#### Week 7-8: Hands-On AI Security Lab
- [ ] Set up local LLM (Ollama + Llama3) - test prompt injection
- [ ] Google's "SAIF" (Secure AI Framework) self-assessment
- [ ] Build: Simple prompt injection detector (Python)
- **Deliverable**: GitHub repo with documented findings

**Phase 1 Exit Criteria**: 
- [ ] AI Fundamentals cert passed
- [ ] 3 GitHub repos with AI security experiments
- [ ] Can explain AI threat landscape to non-technical stakeholder

---

### PHASE 2: Core Technical Certs (Months 3-5) - "Certification Sprint"
**Goal**: Earn SecAI+ and Azure AI Engineer (AI-102)

#### Month 3: SecAI+ Deep Dive
**Week 1-2**: AI/ML Security Fundamentals (SecAI+ Domain 1)
- [ ] CompTIA SecAI+ official study guide Ch 1-3
- [ ] Labs: Model inversion, membership inference, data poisoning demos
- [ ] Resource: "Practical ML Security" (Nicolas Papernot)

**Week 3-4**: AI Threat Landscape (SecAI+ Domain 2)
- [ ] Study: Adversarial attacks, backdoors, supply chain
- [ ] Lab: Adversarial Robustness Toolbox (ART) - generate adversarial examples
- [ ] Resource: MITRE ATLAS deep-dive on 5 techniques

**Week 5-6**: Securing AI Systems (SecAI+ Domain 3)
- [ ] Model deployment security, monitoring, access control
- [ ] Lab: MLflow model signing, watermarking
- [ ] Resource: Google SAIF implementation guide

**Week 7-8**: AI Governance & Exam Prep (SecAI+ Domain 4)
- [ ] Policy frameworks, compliance, ethics
- [ ] Practice exams (official + Dion Training)
- **Deliverable**: Pass SecAI+ exam

#### Month 4: Azure AI Engineer (AI-102)
**Week 1-2**: Azure AI Services Overview
- [ ] Azure AI Foundry, Cognitive Services, OpenAI Service
- [ ] Lab: Deploy GPT-4o, Whisper, Vision APIs
- [ ] MS Learn path: "Create AI solutions with Azure AI Services"

**Week 3-4**: Computer Vision & NLP Implementation
- [ ] Custom Vision, Face API, Document Intelligence
- [ ] Lab: Build document classification pipeline
- [ ] MS Learn: "Develop computer vision solutions"

**Week 5-6**: Knowledge Mining & Responsible AI
- [ ] Azure AI Search, Content Safety, Prompt Shields
- [ ] Lab: RAG with Content Safety filters
- [ ] MS Learn: "Implement responsible AI practices"

**Week 7-8**: Exam Prep & Certification
- [ ] Official practice assessment
- [ ] Review weak areas
- **Deliverable**: Pass AI-102 exam

#### Month 5: Portfolio Project Sprint
- [ ] Project 1: AI Red Teaming Toolkit (prompt injection, jailbreak automation)
- [ ] Project 2: Secure RAG Pipeline (with Content Safety, PII detection)
- [ ] Project 3: Model Monitoring Dashboard (drift, adversarial detection)
- **Deliverable**: 3 polished GitHub repos with READMEs, demos, architecture diagrams

**Phase 2 Exit Criteria**:
- [ ] SecAI+ certified
- [ ] Azure AI Engineer certified
- [ ] 3 portfolio projects live on GitHub

---

### PHASE 3: Advanced Specialization (Months 6-9) - "Expert Credibility"
**Goal**: Pursue ISACA AAISM/AAIA or SANS SEC595 based on budget/goals

#### Path A: ISACA AAISM/AAIA (If you have CISM/CISSP/CISA)
**Month 6-7**: AAISM Domains
- [ ] Domain 1: AI Governance (25%) - frameworks, policies, org structure
- [ ] Domain 2: AI Risk Management (30%) - assessment, treatment, monitoring
- [ ] Domain 3: AI Security Operations (25%) - secure dev, deployment, monitoring
- [ ] Domain 4: AI Compliance (20%) - regulations, audit, reporting

**Month 8-9**: AAIA Domains (if pursuing both)
- [ ] Domain 1: AI Audit Planning (20%)
- [ ] Domain 2: AI Risk Assessment (30%)
- [ ] Domain 3: AI Control Testing (30%)
- [ ] Domain 4: AI Governance Audit (20%)

**Deliverable**: Pass AAISM exam (+ AAIA if dual track)

#### Path B: SANS SEC595 / GIAC GCDA (Technical Depth)
**Month 6**: Pre-study (Python, stats, ML fundamentals refresh)
- [ ] Python for Data Science refresher
- [ ] Statistics for ML (hypothesis testing, distributions)
- [ ] ML fundamentals: regression, classification, clustering, NLP

**Month 7**: SEC595 Course (6-day intensive)
- [ ] Attend live or OnDemand
- [ ] Complete all 30 labs
- [ ] Build course index/cheat sheet

**Month 8-9**: GIAC GCDA Cert Attempt
- [ ] Practice exams, review labs
- [ ] Schedule and pass cert attempt

**Deliverable**: GIAC GCDA certified

#### Path C: Self-Directed Advanced (Budget-Conscious)
- [ ] Advanced Adversarial ML (Clevert et al., Carlini & Wagner papers)
- [ ] LLM Security: Prompt injection taxonomy, defenses (Microsoft, NVIDIA papers)
- [ ] AI Supply Chain Security: SLSA, Sigstore, model signing
- [ ] Contribute to OWASP AI Exchange / open-source AI security tools
- **Deliverable**: 2-3 technical blog posts + conference talk proposal

**Phase 3 Exit Criteria**:
- [ ] At least ONE advanced cert (AAISM, AAIA, or GCDA) OR equivalent portfolio
- [ ] Technical blog/portfolio demonstrating expert-level knowledge
- [ ] Speaking engagement or published article

---

### PHASE 4: Portfolio & Job Hunt (Months 9-12) - "Market Ready"
**Goal**: Polish portfolio, build presence, land interviews

#### Month 9: Portfolio Polish & Website
- [ ] Curate 5 best projects with case studies
- [ ] Build portfolio site (Next.js + Tailwind, deploy to Vercel)
- [ ] Each project: Problem, Approach, Tools, Results, Lessons Learned
- [ ] Technical writing: 3 deep-dive blog posts

#### Month 10: LinkedIn & Network Presence
- [ ] Optimize LinkedIn: Headline, About, Featured, Skills
- [ ] Content calendar: 2 posts/week (technical insights, project demos)
- [ ] Engage: Comment on 5 AI security posts/day
- [ ] Network: Connect with 50 AI security professionals

#### Month 11: Targeted Applications
- [ ] Target list: 50 companies (AI labs, security firms, enterprise)
- [ ] Tailor resume per role (consultant vs engineer)
- [ ] Track applications in job tracker
- [ ] Interview prep: System design, AI threat modeling, behavioral

#### Month 12: Interview Sprint & Offers
- [ ] Technical interview practice (LeetCode, system design, AI security scenarios)
- [ ] Negotiation prep: Market data, equity, benefits
- [ ] Decision framework for offers
- **Deliverable**: Signed offer letter

## Usage Commands

```bash
# Generate full 12-month plan
hermes skill run ai-sec-learning-path --action=create --profile="level7-cyber-forensics"

# Generate specific phase
hermes skill run ai-sec-learning-path --action=phase --phase=1

# Get weekly breakdown
hermes skill run ai-sec-learning-path --action=week --phase=2 --week=3

# Check prerequisites for phase
hermes skill run ai-sec-learning-path --action=prereqs --phase=2

# Update progress
hermes skill run ai-sec-learning-path --action=complete --phase=1 --week=4

# Export to calendar (ICS)
hermes skill run ai-sec-learning-path --action=export --format=ics
```

## Data Files
- `~/.hermes/ai-sec-career/learning-path.yaml` - Full curriculum with progress
- `~/.hermes/ai-sec-career/phase-1.yaml` through `phase-4.yaml` - Phase details
- `~/.hermes/ai-sec-career/weekly-checklist.yaml` - Current week tasks

## Integration
- Reads recommendations from `ai-sec-cert-research`
- Feeds projects to `ai-sec-project-builder`
- Tracks in `ai-sec-progress-dashboard`
- Cronjob: Weekly progress review (Sunday 7pm)