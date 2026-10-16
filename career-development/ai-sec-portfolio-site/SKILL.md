---
name: ai-sec-portfolio-site
description: "AI Security portfolio website generator with deployment."
version: 1.0.0
author: Hermes Agent
tags: [career, ai-security, portfolio, website, deployment]
---

# AI Security Portfolio Site Skill

## Purpose
Generate a professional, modern portfolio website showcasing AI Security projects, certifications, writing, and professional background. Optimized for recruiter/hiring manager review.

## Tech Stack
- **Framework**: Next.js 14 (App Router) + TypeScript
- **Styling**: Tailwind CSS + shadcn/ui components
- **Content**: MDX for project case studies, blog posts
- **Deployment**: Vercel (free tier) with custom domain support
- **Analytics**: Vercel Analytics + Plausible (privacy-friendly)
- **Performance**: Static generation (SSG) for speed, ISR for blog

## Site Architecture

```
portfolio/
├── app/
│   ├── layout.tsx           # Root layout, SEO, fonts
│   ├── page.tsx             # Home: Hero, featured projects, certs, testimonials
│   ├── projects/
│   │   ├── page.tsx         # Project grid with filters
│   │   └── [slug]/
│   │       └── page.tsx     # Project case study (MDX)
│   ├── blog/
│   │   ├── page.tsx         # Blog index
│   │   └── [slug]/
│   │       └── page.tsx     # Blog post (MDX)
│   ├── certifications/
│   │   └── page.tsx         # Cert showcase with verification links
│   ├── about/
│   │   └── page.tsx         # Bio, background, speaking, contact
│   └── api/
│       └── contact/
│           └── route.ts     # Contact form (Formspawn/EmailJS)
├── content/
│   ├── projects/            # MDX files per project
│   ├── blog/                # MDX files per post
│   └── certifications/      # YAML cert data
├── components/
│   ├── ui/                  # shadcn/ui components
│   ├── project-card.tsx
│   ├── cert-badge.tsx
│   ├── skill-tag.tsx
│   └── theme-toggle.tsx
├── lib/
│   ├── mdx.ts               # MDX compilation
│   ├── utils.ts             # Helpers
│   └── constants.ts         # Site config
├── public/
│   ├── images/              # Project screenshots, og:image
│   └── favicon.ico
├── tailwind.config.ts
├── next.config.mjs
├── package.json
└── vercel.json
```

## Content Schema

### Project MDX Frontmatter
```yaml
---
title: "Secure RAG Pipeline with Guardrails"
slug: "secure-rag-pipeline"
date: "2025-01-15"
type: "Engineering / Defensive"
tags: ["RAG", "Content Safety", "PII Detection", "LangChain", "Azure Content Safety"]
featured: true
github: "https://github.com/username/secure-rag-pipeline"
demo: "https://secure-rag-demo.vercel.app"
architecture: "/images/secure-rag-architecture.svg"
skills: ["Python", "TypeScript", "Vector DBs", "LLM Guardrails"]
certifications: ["SecAI+", "Azure AI Engineer"]
---
```

### Certification YAML
```yaml
- name: "CompTIA SecAI+"
  issuer: "CompTIA"
  date: "2025-03-15"
  expiry: "2028-03-15"
  verification_url: "https://www.credly.com/badges/xxx"
  badge_image: "/images/certs/secai-plus.png"
  tier: "Core Technical"
```

## Key Pages

### 1. Home Page (`/`)
- Hero: "AI Security Engineer | Digital Forensics Expert | Building Secure AI Systems"
- Value proposition: Bridge cybersecurity + AI/ML
- Featured: 3 best projects with metrics
- Certifications: Badge row with verification links
- Social proof: Speaking, writing, GitHub stats
- CTA: "View Projects" / "Download Resume" / "Contact"

### 2. Projects Index (`/projects`)
- Filterable grid: Type (Red Team/Blue Team/Engineering/GRC), Tags, Phase
- Each card: Thumbnail, title, type badges, tech stack, 1-line impact
- Click → Case study page

### 3. Project Case Study (`/projects/[slug]`)
- **Problem**: Business/technical context
- **Threat Model**: What attacks addressed (STRIDE/MITRE ATLAS)
- **Architecture**: Interactive diagram (Mermaid.js)
- **Implementation**: Key technical decisions, code snippets
- **Results**: Metrics (latency, detection rate, false positive reduction)
- **Lessons Learned**: What worked, what didn't, next steps
- **Links**: GitHub, Live Demo, Blog Post, Video Walkthrough

### 4. Blog (`/blog`)
- Technical deep-dives on AI security topics
- SEO-optimized for "AI security", "prompt injection", "LLM red teaming"
- Series: "AI Security Foundations", "Red Teaming LLMs", "Securing RAG"

### 5. Certifications (`/certifications`)
- Timeline view with verification badges
- Grouped by tier (Foundational, Core, Advanced)
- Each links to Credly/Badge verification

### 6. About (`/about`)
- Background: Level 7 Cybersecurity & Digital Forensics → AI Security
- Speaking: Conferences, webinars, podcasts
- Writing: Blog, external publications
- Contact: Form + LinkedIn + GitHub + Email

## Deployment Pipeline

```yaml
# .github/workflows/deploy.yml
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '20', cache: 'npm' }
      - run: npm ci
      - run: npm run lint
      - run: npm run type-check
      - run: npm run test
      - run: npm run build
      - uses: actions/upload-artifact@v4
        with: { name: nextjs-build, path: .next/ }

  deploy:
    needs: build
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v4
        with: { name: nextjs-build, path: .next/ }
      - uses: amondnet/vercel-action@v25
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
          vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}
          vercel-args: '--prod'
```

## Usage Commands

```bash
# Scaffold new portfolio site
hermes skill run ai-sec-portfolio-site --action=scaffold --output="./my-portfolio"

# Add new project case study
hermes skill run ai-sec-portfolio-site --action=add-project --slug="ai-red-teaming-framework" --title="AI Red Teaming Automation Framework"

# Add blog post
hermes skill run ai-sec-portfolio-site --action=add-post --slug="prompt-injection-taxonomy" --title="A Taxonomy of Prompt Injection Attacks"

# Build locally
hermes skill run ai-sec-portfolio-site --action=build --path="./my-portfolio"

# Deploy to Vercel
hermes skill run ai-sec-portfolio-site --action=deploy --path="./my-portfolio"

# Validate all content
hermes skill run ai-sec-portfolio-site --action=validate --path="./my-portfolio"

# Generate sitemap & SEO report
hermes skill run ai-sec-portfolio-site --action=seo-audit --path="./my-portfolio"
```

## Customization Points
- **Colors**: Tailwind config (primary: security blue, accent: alert red)
- **Fonts**: Inter (UI) + JetBrains Mono (code)
- **Icons**: Lucide React
- **Dark mode**: System preference + manual toggle
- **Resume PDF**: Auto-generated from JSON data (React-PDF)

## Integration
- Pulls project data from `ai-sec-project-builder` export
- Pulls cert data from `ai-sec-cert-research` tracker
- Feeds `ai-sec-progress-dashboard` with deployment status
- Cronjob: Weekly build health check, monthly content audit