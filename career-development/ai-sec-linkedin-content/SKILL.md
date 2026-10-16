---
name: ai-sec-linkedin-content
description: "LinkedIn content calendar and post generator for AI Security"
version: 1.0.0
author: Hermes Agent
tags: [career, ai-security, linkedin, content, personal-brand]
---

# AI Security LinkedIn Content Skill

## Purpose
Generate a strategic LinkedIn content calendar and ready-to-post content for building authority in AI Security. Designed for 2 posts/week + daily engagement.

## Content Strategy

### Content Pillars (Rotate Weekly)
1. **Technical Deep-Dives** (30%) - How-to, code, architecture
2. **Threat Intelligence** (25%) - New attacks, vulnerabilities, MITRE ATLAS
3. **Career Journey** (20%) - Learning updates, cert progress, project demos
4. **Industry Commentary** (15%) - Regulation, ethics, market trends
5. **Community** (10%) - Shoutouts, event recaps, resource sharing

### Post Templates

#### Type A: Technical Deep-Dive (Carousel/Article)
```
Hook: "Most teams miss this when securing RAG pipelines..."
Body: 
- The vulnerability (with diagram)
- Why standard approaches fail
- My implementation (code snippet)
- Results/metrics
CTA: "Full code on GitHub → [link]"
Hashtags: #AISecurity #RAG #LLMSecurity #CyberSecurity
```

#### Type B: Threat Intelligence Alert
```
Hook: "New prompt injection variant targeting [specific system]..."
Body:
- Attack description + MITRE ATLAS mapping
- Proof of concept (safe/sanitized)
- Detection/mitigation strategies
- Affected systems
CTA: "How are you detecting this? Comment below"
Hashtags: #PromptInjection #AIRedTeaming #ThreatIntel
```

#### Type C: Learning/Cert Update
```
Hook: "Week 3 of SecAI+ prep: The domain that surprised me most..."
Body:
- What I studied this week
- Key insight connecting to my forensics background
- Practice question + explanation
- Resources that helped
CTA: "Also studying for SecAI+? Let's connect"
Hashtags: #SecAIPlus #CompTIA #AISecurity #LearningInPublic
```

#### Type D: Project Showcase
```
Hook: "Built an automated AI red teaming framework. Here's what it found..."
Body:
- Problem statement
- Architecture (1 diagram)
- Key findings (3 bullets)
- Link to repo + demo
CTA: "Star the repo if useful → [link]"
Hashtags: #AIRedTeaming #OpenSource #SecurityResearch
```

#### Type E: Industry Commentary
```
Hook: "The EU AI Act Article 55 on GPAI models changes how we..."
Body:
- Regulation summary (plain English)
- Implementation impact for practitioners
- My take: opportunity vs burden
- Resources for compliance
CTA: "How is your org preparing? #EUAIAct"
Hashtags: #AIRegulation #EUAIAct #AIGovernance
```

## Content Calendar (12-Week Rolling)

### Month 1: Foundations Visibility
| Week | Mon (Technical) | Thu (Journey) | Engagement Focus |
|------|-----------------|---------------|------------------|
| 1 | AI Fundamentals: Key concepts for sec pros | "Starting my AI Security journey..." | Comment on 5 AI sec posts/day |
| 2 | OWASP AI Exchange: Top 5 takeaways | Week 2 progress: Prompt injection lab | Connect with 10 practitioners |
| 3 | NIST AI RMF: Mapping to forensics | "How my forensics degree applies to AI risk" | Share OWASP guide |
| 4 | MITRE ATLAS: Top techniques explained | Phase 1 complete: 3 repos + cert | Tag mentors/peers |

### Month 2: Certification Sprint
| Week | Mon (Technical) | Thu (Journey) |
|------|-----------------|---------------|
| 5 | SecAI+ Domain 1: ML security fundamentals | "SecAI+ study plan: Week 1 done" |
| 6 | Adversarial examples with ART (code) | "The attack that broke my local model" |
| 7 | Securing model deployment (SAIF) | "Practice exam results: focusing on Domain 3" |
| 8 | **SEC AI+ PASSED** + Azure AI Engineer kickoff | **Certification announcement post** |

### Month 3: Project Showcase
| Week | Mon (Technical) | Thu (Project) |
|------|-----------------|---------------|
| 9 | Building secure RAG: Guardrails architecture | Project 1 launch: Secure RAG Pipeline |
| 10 | PII detection in LLM outputs | Project 2 launch: Model Monitoring |
| 11 | Drift detection: PSI vs KS-test | Project 3 launch: Red Team Toolkit |
| 12 | Phase 2 complete: 2 certs + 3 projects | Portfolio website v1 live |

## Growth Tactics

### Daily (15 min)
- [ ] Comment thoughtfully on 5 posts from: AI security researchers, hiring managers, target companies
- [ ] Share 1 relevant article with commentary
- [ ] Respond to all comments on your posts within 2 hrs

### Weekly (1 hr)
- [ ] Write 2 posts (schedule via Buffer/Hootsuite/Typefully)
- [ ] Send 5 connection requests with personalized notes
- [ ] Engage in 2 relevant LinkedIn groups/discussions
- [ ] Review analytics: impressions, engagement rate, profile views

### Monthly (2 hrs)
- [ ] Audit: Which post types perform best?
- [ ] Update featured section on profile
- [ ] Request 1 recommendation from peer/mentor
- [ ] Plan next month's content themes

## Profile Optimization

### Headline Formula
```
AI Security Engineer | Digital Forensics (Level 7) | SecAI+ | Azure AI Engineer | Building Secure AI Systems | Open to AI Security Roles
```

### About Section Structure
1. **Hook**: "I bridge cybersecurity and AI/ML to build systems that are both intelligent and secure."
2. **Background**: Level 7 Cybersecurity & Digital Forensics → AI Security transition
3. **Current Focus**: SecAI+, Azure AI Engineer, AI Red Teaming, Secure RAG
4. **Proof**: 3 projects, 2 certs, GitHub, Portfolio link
5. **CTA**: "Open to AI Security Engineer/Consultant roles. Let's connect →"

### Featured Section
1. Portfolio website
2. Top GitHub repo (Secure RAG)
3. Certification badges (Credly embeds)
4. Best blog post
5. Speaking engagement / podcast

## Usage Commands

```bash
# Generate this week's content
hermes skill run ai-sec-linkedin-content --action=generate --week=5

# Get post template
hermes skill run ai-sec-linkedin-content --action=template --type="technical-deep-dive"

# Full content calendar
hermes skill run ai-sec-linkedin-content --action=calendar --months=3

# Analyze post performance
hermes skill run ai-sec-linkedin-content --action=analytics --post-id="urn:li:ugcPost:..."

# Optimize profile
hermes skill run ai-sec-linkedin-content --action=profile-audit

# Export to scheduling tool (CSV)
hermes skill run ai-sec-linkedin-content --action=export --format=csv --weeks=4
```

## Data Files
- `~/.hermes/ai-sec-career/linkedin-calendar.yaml` - 12-week rolling calendar
- `~/.hermes/ai-sec-career/linkedin-posts.yaml` - Draft/published posts with metrics
- `~/.hermes/ai-sec-career/linkedin-templates/` - Markdown templates per type

## Integration
- Pulls project milestones from `ai-sec-project-builder`
- Pulls cert achievements from `ai-sec-cert-research`
- Feeds `ai-sec-progress-dashboard` with engagement metrics
- Cronjob: Sunday 7pm - generate next week's content; Daily 8am - engagement reminders