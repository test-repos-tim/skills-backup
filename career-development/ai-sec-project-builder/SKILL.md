---
name: ai-sec-project-builder
description: "AI Security portfolio project templates and guidance."
version: 1.0.0
author: Hermes Agent
tags: [career, ai-security, projects, portfolio, templates]
---

# AI Security Project Builder Skill

## Purpose
Provide project templates, starter code, architecture guidance, and evaluation criteria for building a compelling AI Security portfolio. Each project maps to specific skills employers seek.

## Project Catalog (Tiered by Difficulty & Impact)

### TIER 1: FOUNDATIONAL (Phase 1-2) - Quick Wins

#### P1: Prompt Injection Detection Lab
- **Type**: Red Team / Defensive
- **Skills**: Python, LLM APIs, Prompt Engineering, Security Testing
- **Description**: Build a tool that systematically tests LLM endpoints for prompt injection vulnerabilities using a taxonomy of attack patterns
- **Tech Stack**: Python, OpenAI/Anthropic APIs, Ollama (local), pytest
- **Deliverables**: 
  - CLI tool with 20+ attack patterns (ignore instructions, roleplay, encoding, etc.)
  - Automated report generator (JSON/HTML)
  - Docker container for easy deployment
- **Portfolio Value**: Demonstrates red teaming methodology, LLM security knowledge
- **Time**: 1-2 weeks
- **Difficulty**: ⭐⭐

#### P2: Secure RAG Pipeline with Guardrails
- **Type**: Engineering / Defensive
- **Skills**: RAG Architecture, Content Safety, PII Detection, Vector DBs
- **Description**: Production-ready RAG pipeline with input/output guardrails, PII redaction, and audit logging
- **Tech Stack**: LangChain/LlamaIndex, Chroma/Pinecone, Presidio/Spacy (PII), Azure Content Safety or Llama Guard
- **Deliverables**:
  - Modular pipeline: Ingestion → Chunking → Embedding → Retrieval → Generation → Guardrails
  - Configurable guardrails (prompt injection, PII, toxicity, hallucination detection)
  - Evaluation harness (RAGAS metrics + security test cases)
  - API + simple UI (Streamlit/Gradio)
- **Portfolio Value**: Shows production engineering, defense-in-depth, responsible AI
- **Time**: 2-3 weeks
- **Difficulty**: ⭐⭐⭐

#### P3: Model Monitoring & Drift Detection Dashboard
- **Type**: Engineering / Operations
- **Skills**: ML Observability, Statistical Drift, Adversarial Detection, Dashboards
- **Description**: Real-time monitoring for deployed ML models detecting data drift, concept drift, and adversarial inputs
- **Tech Stack**: Prometheus/Grafana or custom (Streamlit/Plotly), Evidently AI, scikit-learn, FastAPI
- **Deliverables**:
  - Feature drift detection (PSI, KS-test, Jensen-Shannon)
  - Prediction drift monitoring
  - Adversarial input detection (statistical + ML-based)
  - Alerting system (Slack/Email/PagerDuty)
  - Historical comparison reports
- **Portfolio Value**: MLOps maturity, operational security thinking
- **Time**: 2 weeks
- **Difficulty**: ⭐⭐

---

### TIER 2: INTERMEDIATE (Phase 2-3) - Technical Depth

#### P4: AI Red Teaming Automation Framework
- **Type**: Red Team / Research
- **Skills**: Adversarial ML, Jailbreak Automation, Multi-turn Attacks, Reporting
- **Description**: Automated framework for discovering novel jailbreaks and prompt injections across multiple models
- **Tech Stack**: Python, multiple LLM providers, evolutionary algorithms, prompt optimization
- **Deliverables**:
  - Attack generator: PAIR, GCG, AutoDAN implementations
  - Multi-turn conversation attack simulator
  - Success rate benchmarking across models (GPT-4, Claude, Llama, local)
  - Responsible disclosure template
  - Research blog post with findings
- **Portfolio Value**: Cutting-edge research capability, published findings
- **Time**: 3-4 weeks
- **Difficulty**: ⭐⭐⭐⭐

#### P5: AI Supply Chain Security Scanner
- **Type**: Engineering / Supply Chain
- **Skills**: SBOM, Model Signing, SLSA, Provenance, Vulnerability Scanning
- **Description**: Tool to scan ML model repositories for supply chain risks: unverified dependencies, unsigned models, malicious code in pickles
- **Tech Stack**: Python, Sigstore/Cosign, SBOM tools (Syft), pickle scanning, GitHub Actions
- **Deliverables**:
  - Scanner for Hugging Face repos, local model files, MLflow artifacts
  - Checks: Model signature verification, pickle safety, dependency vulnerabilities, license compliance
  - CI/CD integration (GitHub Action)
  - SARIF output for GitHub Security tab
- **Portfolio Value**: Emerging critical area, DevSecOps + AI intersection
- **Time**: 2-3 weeks
- **Difficulty**: ⭐⭐⭐

#### P6: LLM-Based Security Log Analyzer
- **Type**: Engineering / Blue Team
- **Skills**: Log Analysis, Fine-tuning/RAG, Threat Detection, SOC Automation
- **Description**: Fine-tuned or RAG-enhanced LLM that parses security logs (SIEM, firewall, EDR) and identifies anomalies/attacks
- **Tech Stack**: Llama/Llama3 fine-tuning (Unsloth/LoRA) or RAG, Elasticsearch/Splunk API, MITRE ATT&CK mapping
- **Deliverables**:
  - Training data pipeline (public datasets + synthetic)
  - Fine-tuned model or RAG system with MITRE ATT&CK knowledge
  - API for real-time log analysis
  - False positive reduction metrics
  - Integration guide for Splunk/Elastic
- **Portfolio Value**: Bridges your forensics background + AI, practical SOC tool
- **Time**: 3-4 weeks
- **Difficulty**: ⭐⭐⭐⭐

---

### TIER 3: ADVANCED (Phase 3-4) - Expert Differentiators

#### P7: Adversarial Robustness Benchmark Suite
- **Type**: Research / Engineering
- **Skills**: Adversarial ML, Benchmarking, Paper Implementation, Open Source
- **Description**: Reproduction and extension of seminal adversarial robustness papers with unified benchmarking
- **Tech Stack**: PyTorch, Foolbox/ART/CleverHans, multiple architectures (ResNet, ViT, CLIP)
- **Deliverables**:
  - Clean implementations of 5+ key papers (PGD, AutoAttack, TRADES, etc.)
  - Unified benchmark runner with standardized metrics
  - Novel contribution: New defense or attack variant
  - Paper-style writeup + open source release
- **Portfolio Value**: Research credibility, open source leadership
- **Time**: 4-6 weeks
- **Difficulty**: ⭐⭐⭐⭐⭐

#### P8: AI Governance Automation Platform
- **Type**: Consulting / GRC
- **Skills**: Policy as Code, Compliance Automation, Risk Assessment, Reporting
- **Description**: Tool that maps organizational AI inventory to regulatory requirements (EU AI Act, NIST AI RMF, ISO 42001) and generates compliance artifacts
- **Tech Stack**: Python, Rego/OPA (policy as code), YAML/JSON schemas, report generation (PDF/HTML)
- **Deliverables**:
  - AI System Registry (CRUD + classification)
  - Risk assessment wizard (questionnaire → risk score → controls)
  - Control mapping matrix (NIST AI RMF ↔ EU AI Act ↔ ISO 42001)
  - Automated artifact generation (DPIA, Model Cards, Incident Response Plans)
  - Multi-tenant SaaS architecture design
- **Portfolio Value**: Consulting-ready, regulatory expertise, product thinking
- **Time**: 4-6 weeks
- **Difficulty**: ⭐⭐⭐⭐

---

## Project Template Structure

Each project follows this standardized structure:

```
project-name/
├── README.md              # Problem, Approach, Architecture, Results, Lessons
├── architecture.svg       # System diagram (draw.io/mermaid)
├── docs/
│   ├── design-decisions.md
│   ├── threat-model.md
│   └── future-work.md
├── src/                   # Source code
├── tests/                 # Unit + integration + security tests
├── scripts/               # Deployment, evaluation, demo scripts
├── .github/
│   └── workflows/         # CI/CD, security scanning
├── Dockerfile
├── docker-compose.yml
├── requirements.txt / pyproject.toml
├── Makefile               # Common commands
└── DEMO.md                # Screenshots, demo video link, live demo URL
```

## Usage Commands

```bash
# List all project templates
hermes skill run ai-sec-project-builder --action=list

# Get project details
hermes skill run ai-sec-project-builder --action=info --project="secure-rag-pipeline"

# Scaffold new project
hermes skill run ai-sec-project-builder --action=new --project="prompt-injection-lab" --output="./my-projects/p1"

# Get architecture review checklist
hermes skill run ai-sec-project-builder --action=checklist --project="ai-red-teaming-framework"

# Export project metadata for portfolio
hermes skill run ai-sec-project-builder --action=export --project="secure-rag-pipeline" --format=portfolio-json

# Validate project completeness
hermes skill run ai-sec-project-builder --action=validate --path="./my-projects/p1"
```

## Evaluation Criteria (What Employers Look For)

| Criterion | Weight | How to Demonstrate |
|-----------|--------|-------------------|
| **Technical Depth** | 30% | Novel implementation, not just tutorial copy |
| **Security Mindset** | 25% | Threat model, abuse cases, defense-in-depth |
| **Code Quality** | 20% | Tests, CI/CD, docs, type hints, linting |
| **Documentation** | 15% | Clear README, architecture diagram, decision log |
| **Presentation** | 10% | Live demo, video walkthrough, blog post |

## Integration
- Reads phase requirements from `ai-sec-learning-path`
- Feeds project metadata to `ai-sec-portfolio-site` and `ai-sec-progress-dashboard`
- Cronjob: Monthly project health check (dependencies, security scans)