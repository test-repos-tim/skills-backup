---
name: personal-goals-agent
description: A skill for creating and managing a personal goals tracking system that helps users set, track, and achieve their personal objectives
version: 1.0.0
author: Hermes Agent
category: productivity
---

# Personal Goals Agent for Shiva

## Description
A specialized skill for creating and managing a personal goals tracking system tailored to Shiva's specific goals: portfolio website creation, passive income through AI website services, personal psychology/mental health/habit tracking, and bug bounty hunting. Integrates with Hermes tools, Obsidian, and includes backup system setup for /home/shiva/Documents/.

## When to Use
- When you want to establish a structured approach to achieve specific goals: portfolio website, passive income AI services, mental health/habit tracking, and bug bounty hunting
- When you need help breaking down these specific goals into actionable steps
- When you want to track progress across these goal areas using Obsidian and other tools
- When you need motivation and accountability systems for long-term projects
- When you want to set up backup systems for your important documents in /home/shiva/Documents/
- When you want to integrate your goal tracking with your existing Obsidian workflow

## Setup Instructions
1. Set up your workspace at /home/shiva/Documents/hermes-goal-app (already created)
2. Configure backup system for /home/shiva/Documents/ to protect your work
3. Integrate goal tracking with your existing Obsidian vault
4. Define SMART goals for each of your four main areas:
   - Portfolio website creation (matching damian-moore.medium.com)
   - Passive income via AI website services (hosting-based)
   - Personal psychology, mental health, habit tracking, journalling
   - Bug bounty hunting skill development
5. Set up tracking system using Notion, Airtable, or Google Workspace (linked to Obsidian)
6. Create action plans and milestones for each goal area
7. Schedule regular review sessions

## Core Components

### 1. Goal Categories Framework
Focus on these four core areas based on your stated goals:

- **Portfolio Website**: Create professional portfolio website matching your Medium blog (damian-moore.medium.com), update LinkedIn profile and posts, expand to other social media platforms later
- **Passive Income AI Services**: Develop and host AI-powered websites that customers pay for, create sustainable revenue streams through hosting/services
- **Personal Psychology & Mental Health**: Mental health tracking, habit formation, journaling practice, self-improvement and emotional well-being
- **Bug Bounty Hunting**: Develop cybersecurity skills for vulnerability assessment, penetration testing, and participation in bug bounty programs

Each area should use the SMART criteria for goal setting:
- **S**pecific: Clear and well-defined objectives
- **M**easurable: Quantifiable progress indicators
- **A**chievable: Realistic given your resources and constraints
- **R**elevant: Aligned with your values and long-term vision
- **T**ime-bound: Clear deadlines and target dates

### 2. Tracking System Setup
Choose one of these integration options, all designed to work with your Obsidian setup:

#### Option A: Notion Database with Obsidian Integration (Recommended)
- Create a database in Notion with properties: Goal, Category, Status, Priority, Due Date, Progress %, Notes, Related Obsidian Notes
- Use different views: Table, Calendar, Board (Kanban), Gallery
- Link to relevant Obsidian notes using the Notion-Obsidian integration or manual linking
- Add formulas for automatic progress calculation
- Include motivation elements: quotes, images, reward systems
- Store in your workspace: /home/shiva/Documents/hermes-goal-app/notion/

#### Option B: Airtable Base with Obsidian Sync
- Similar structure to Notion with different field types
- Use calendar view for deadline tracking
- Use kanban view for status tracking
- Add attachment fields for vision boards/documents
- Sync with Obsidian using available plugins or manual linking
- Store in your workspace: /home/shiva/Documents/hermes-goal-app/airtable/

#### Option C: Google Workspace Suite with Obsidian Linking
- Google Sheets for goal tracking and metrics (link to Obsidian)
- Google Calendar for deadline reminders and time blocking (link events to Obsidian)
- Google Docs for detailed action plans and journals (link from Obsidian)
- Google Drive for resource storage (link to Obsidian)
- Store in your workspace: /home/shiva/Documents/hermes-goal-app/google-workspace/

#### Option D: Obsidian-Centric Approach (Leveraging Your Existing Setup)
- Use your existing Obsidian vault for goal tracking
- Create folders for each goal area: Portfolio Website, AI Services, Mental Health, Bug Bounty
- Use Dataview plugin for queries and dashboards
- Use Templater for automated note creation
- Use Calendar plugin for scheduling reviews
- Store everything in: /home/shiva/Documents/Obsidian-Vault/Goals/ (or similar)
- Backup your Obsidian vault regularly

### 3. Weekly Review Process
Schedule a recurring weekly review (Sunday evenings work well):
1. **Review Progress**: Update completion percentages for each goal area
2. **Review Metrics**: Check website traffic, income metrics, mood/habit tracking data, bug bounty findings
3. **Analyze Blockers**: Identify what's hindering progress in each area (technical challenges, motivation issues, time constraints)
4. **Adjust Plans**: Modify action steps, timelines, or resources as needed
5. **Celebrate Wins**: Acknowledge completed milestones (website features deployed, first client acquired, streak milestones, bugs found)
6. **Plan Next Week**: Set 3-5 priority actions for each category based on review insights
7. **Backup Check**: Verify backups of /home/shiva/Documents/ and Obsidian vault are current
8. **Obsidian Sync**: Ensure all notes and reflections are properly linked in your Obsidian vault

### 4. Available Tools Integration
Leverage these Hermes skills and MCP servers for your specific goals:

#### For Portfolio Website Goals:
- **Software Development Skills**: 
  - `software-development-plan`: Create detailed website development plans
  - `software-development-test-driven-development`: Apply TDD principles to web development
  - `software-development-systematic-debugging`: Troubleshoot website issues
  - `creative-architecture-diagram`: Plan site architecture and user flows
  - `creative-ascii-art`: Generate decorative elements for your site
  - `productivity-notion`: Document design decisions and component libraries
  - `productivity-airtable`: Track component inventory and development progress
- **MCP Servers**: Use hexstrike-ai for security testing of your website once deployed

#### For Passive Income AI Website Services:
- **MLOps Skills**:
  - `mlops-huggingface-hub`: Deploy and manage AI models for your services
  - `mlops-serving-llms-vllm`: Serve LLMs efficiently for customer websites
  - `mlops-unsloth`: Fine-tune models faster for custom AI services
  - `mlops-weights-and-biases`: Track experiments and model performance
  - `mlops-comet`: Experiment tracking for AI service development
- **Productivity Skills**:
  - `productivity-notion`: Business planning, pricing strategies, customer tracking
  - `productivity-airtable`: CRM, invoicing, subscription management
  - `productivity-google-workspace`: Financial tracking, proposals, contracts
  - `software-development-write-file`: Create service templates and documentation
- **MCP Servers**: Explore hexstrike-ai for security assessment of the AI services you'll offer

#### For Personal Psychology, Mental Health, Habit Tracking, Journalling:
- **Note-Taking Skills**:
  - `note-taking-obsidian`: Advanced Obsidian techniques for mental health tracking
- **Productivity Skills**:
  - `productivity-nano-pdf`: Create habit tracking templates and worksheets
  - `productivity-teams-meeting-pipeline`: Schedule regular self-check-ins
  - `leisure-find-nearby`: Find therapeutic activities and locations
- **Creative Skills**:
  - `creative-humanizer`: Make journal prompts and affirmations more personal
  - `creative-songwriting-and-ai-music`: Create personalized affirmation audio
  - `creative-ascii-video`: Create motivational visualizations for goals
- **MLOps Skills** (for mood/behavior prediction):
  - `mlops-huggingface-tokenizers`: Analyze journal entries for sentiment trends
  - `mlops-sentence-transformers`: Generate embeddings for similarity search in journals

#### For Bug Bounty Hunting:
- **Security Testing Skills** (MCP Server Based):
  - `mcp-hexstrike-ai-nmap_scan`: Network discovery and port scanning
  - `mcp-hexstrike-ai_nikto_scan`: Web server vulnerability scanning
  - `mcp-hexstrike-ai_dirsearch_scan`: Directory and file discovery
  - `mcp-hexstrike-ai_xsser_scan`: XSS vulnerability testing
  - `mcp-hexstrike-ai_sqlmap_scan`: SQL injection testing
  - `mcp-hexstrike-ai_wafw00f_scan`: WAF detection
  - `mcp-hexstrike-ai_whatweb`: Technology fingerprinting
  - `mcp-hexstrike-ai_subfinder_scan`: Subdomain discovery
  - `mcp-hexstrike-ai_amass_scan`: Advanced subdomain enumeration
  - `mcp-hexstrike-ai_dnsenum_scan`: DNS enumeration
  - `mcp-hexstrike-ai_fierce_scan`: DNS reconnaissance
  - `mcp-hexstrike-ai_hakrawler_crawl`: Web endpoint discovery
- **Productivity Skills**:
  - `productivity-notion`: Track vulnerabilities found, bounties earned, learning progress
  - `productivity-airtable`: Manage bug bounty programs, payouts, reporting
  - `software-development-systematic-debugging`: Methodical approach to vulnerability validation
  - `writing-plans`: Create structured bug bounty hunting methodologies
- **Research Skills**:
  - `research-duckduckgo-search`: Stay updated on latest vulnerabilities and techniques
  - `research-arxiv`: Read latest security research papers

#### Backup and System Tools:
- **Productivity Skills**:
  - `productivity-maps`: Plan physical backup storage locations (if using external drives)
- **Software Development Skills**:
  - `software-development-write-file`: Create backup scripts and documentation
  - `software-development-systematic-debugging`: Troubleshoot backup issues

### 5. Motivation and Accountability Features
- **Visual Progress Tracking**: 
  - Portfolio: Live website preview links in your tracking system
  - AI Services: Demo videos or screenshots of working prototypes
  - Mental Health: Mood charts and habit streaks in Obsidian
  - Bug Bounty: Bounty earned over time graph, vulnerabilities fixed timeline
- **Reward System**: 
  - Define meaningful rewards for milestones (e.g., "After launching portfolio site, buy that tech book")
  - Tie rewards to meaningful progress, not just completion
  - Use your Obsidian vault to store reward ideas and motivations
- **Accountability Partners**: 
  - Share goals with trusted friends using communication tools (consider Signal for privacy)
  - Use `social-media-xitter` or `social-media-xurl` for public accountability if desired
  - Join relevant communities: web dev forums, AI entrepreneur groups, mental health support groups, bug bounty platforms
- **Regular Reflection**: 
  - Daily journaling in Obsidian using templates
  - Weekly reflection prompts: "What did I learn this week?", "What challenged me?", "What am I grateful for?"
  - Monthly reviews: Deeper analysis of progress and direction adjustments
- **Inspiration Collection**: 
  - Use Obsidian to create a swipe file of website designs you admire
  - Save AI service business models that inspire you
  - Keep a mental health resources notebook in Obsidian
  - Maintain a bug bounty techniques and writeups collection

### 6. Example Goal Templates

#### Portfolio Website Goal Example:
```
Goal: Launch portfolio website showcing 5 projects matching Medium blog style
Category: Portfolio Website
Specific: Build responsive website with blog integration, project showcase, and contact form
Measurable: Live website at custom domain, 5+ projects displayed, mobile-responsive
Achievable: 10 hours/week available for development over 8 weeks
Relevant: Professional branding and client acquisition for AI services
Time-bound: Launch in 8 weeks (by September 3, 2026)
Milestones: 
- Week 1: Design wireframes and choose tech stack (HTML/CSS/JS or React)
- Week 2: Implement core layout and navigation
- Week 3: Build project showcase component
- Week 4: Integrate blog section matching Medium aesthetic
- Week 5: Add contact form and SEO optimization
- Week 6: Test responsiveness and fix bugs
- Week 7: Content population and final review
- Week 8: Launch to custom domain and announce on LinkedIn
```

#### AI Services Business Goal Example:
```
Goal: Launch first AI website service with 3 paying customers
Category: AI Services Business
Specific: Create and deploy AI-powered website optimization service
Measurable: Service deployed, 3 clients paying $50+/month each
Achievable: Leverage existing AI skills, start with simple automation
Relevant: First step toward passive income goal
Time-bound: First customer in 6 weeks, 3 customers in 12 weeks
Milestones: 
- Week 1-2: Define service scope and pricing model
- Week 3-4: Develop MVP using available AI tools/APIs
- Week 5: Create sales materials and outreach sequence
- Week 6: Launch landing page and begin outreach
- Week 7-8: Onboard first customer
- Week 9-10: Onboard second customer
- Week 11-12: Onboard third customer and request testimonials
```

#### Mental Health and Habit Tracking Goal Example:
```
Goal: Establish consistent mental health tracking and improvement system
Category: Mental Health & Habits
Specific: Daily mood tracking, weekly review, and three core habits (meditation, journaling, exercise)
Measurable: 80%+ completion rate on habit tracking, weekly insights generated
Achievable: Start with 5 minutes daily, build gradually
Relevant: Foundation for sustained productivity and creativity
Time-bound: System established in 4 weeks, optimized by 8 weeks
Milestones: 
- Week 1: Set up Obsidian dashboard with daily note template
- Week 2: Establish morning routine (5 min meditation + journaling)
- Week 3: Add evening reflection and habit tracking
- Week 4: Incorporate exercise tracking and weekly review
- Week 5-6: Refine system based on what works
- Week 7-8: Optimize for sustainability and add insights generation
```

#### Bug Bounty Skill Development Goal Example:
```
Goal: Develop proficiency in web application security testing and earn first bounty
Category: Bug Bounty Hunting
Specific: Learn and practice OWASP Top 10 vulnerabilities, submit first valid report
Measurable: Complete structured learning path, submit at least one valid bug report
Achievable: 5 hours/week study and practice time available
Relevant: Skill development for potential freelance/security career path
Time-bound: Complete learning in 10 weeks, submit first report in 12 weeks
Milestones: 
- Weeks 1-2: Learn HTTP basics, web technologies, and reconnaissance
- Weeks 3-4: Study and practice injection flaws (SQLi, XSS)
- Weeks 5-6: Study broken authentication and sensitive data exposure
- Weeks 7-8: Study XML external entities, broken access control
- Weeks 9-10: Study security misconfiguration, XSS, insecure deserialization
- Weeks 11-12: Practice on intentionally vulnerable sites (OWASP Juice Shop, etc.)
- Week 13: Submit first vulnerability report to a bug bounty platform
```

### 7. Backup System for /home/shiva/Documents/
Given your concern about computer reliability, implement a robust backup strategy:

#### Local Backup (Immediate Protection)
- **External Hard Drive**: Use rsync or Timeshift for daily backups
  ```
  rsync -av --delete /home/shiva/Documents/ /mnt/backup/drive/Documents/
  ```
- **Schedule**: Automate with cron job (daily at 2 AM)
- **Verification**: Monthly test restore of random files

#### Cloud Backup (Offsite Protection)
- **Options**: 
  - Backblaze B2 or Wasabi (cost-effective S3-compatible)
  - Google Drive/Dropbox (for smaller critical files)
  - Rclone for encryption and synchronization
- **Implementation**: 
  ```
  rclone sync /home/shiva/Documents/ remote:backup-shiva-docs --progress
  ```

#### Version Control for Critical Files
- **Git Repository**: For configuration files, code, and documents
  ```
  cd /home/shiva/Documents
  git init
  git add .
  git commit -m "Initial backup commit"
  ```
- **Private Remote**: GitHub private repository or GitLab for offsite versioning

#### Encryption for Sensitive Data
- **VeraCrypt Containers**: For particularly sensitive information
- **Age or GPG**: Encrypt specific files before backup
- **Encrypted Cloud**: Services like Tresorit or Sync.com

#### Backup Testing Schedule
- **Weekly**: Verify backup completed successfully
- **Monthly**: Restore random sample of files
- **Quarterly**: Full restore test to ensure recoverability

#### Integration with Your Workflow
- Store backup scripts in: `/home/shiva/Documents/hermes-goal-app/backup/`
- Document procedures in Obsidian: `Backup Procedures.md`
- Include backup status check in your weekly review
- Automate where possible to reduce cognitive load

#### Minimum Viable Backup Plan (Start Here)
1. Get an external USB drive
2. Set up weekly manual copy: `cp -r /home/shiva/Documents/* /path/to/backup/`
3. Gradually automate with cron scripts
4. Add cloud backup as secondary layer
5. Implement version control for active projects

### 8. Troubleshooting Common Issues
#### Lack of Motivation for Long-Term Projects:
- **Portfolio Website**: Break into smaller, showcaseable components (one project page at a time)
- **AI Services**: Start with one simple service you can build in a weekend
- **Mental Health**: Focus on one tiny habit (e.g., one minute of breathing) rather than overhaul
- **Bug Bounty**: Learn one new technique per week rather than trying to master everything
- Use the `creative-humanizer` skill to rewrite goal statements in motivating language
- Reconnect with your "why" - visualize the outcome clearly

#### Feeling Overwhelmed by Technical Complexity:
- Apply the `software-development-simplify-code` principle: start with the simplest version that works
- For website: Start with a single HTML page before adding frameworks
- For AI services: Use no-code/low-code tools first, then graduate to custom code
- For mental health: Start with paper journaling before building complex digital systems
- For bug bounty: Focus on OWASP Top 10 before exploring niche vulnerabilities
- Use the `productivity-plan` skill to create micro-action plans for each area

#### Not Seeing Progress or Results:
- **Portfolio**: Share early versions with friends for feedback and motivation
- **AI Services**: Talk to potential customers early to validate your service idea
- **Mental Health**: Track subjective well-being metrics, not just streaks
- **Bug Bounty**: Track skills learned and attempts made, not just bounties earned
- Review your metrics - are you measuring leading indicators or just lagging ones?
- Use the `software-development-systematic-debugging` approach: observe, hypothesize, experiment, conclude
- Consider if goals need adjustment based on learning and changing circumstances

#### Technical Issues and System Failures:
- **Backup First**: Always ensure your /home/shiva/Documents/ is backed up before major changes
- **Version Control**: Use Git for your website code and configuration files
- **Environment Backup**: Document your development environment setup
- **Test Restores**: Quarterly, practice restoring from backup to ensure it works
- Use version control for your Obsidian vault (consider git or Obsidian's version history)

### 9. Implementation Steps
1. **Workspace Setup**: Your workspace at `/home/shiva/Documents/hermes-goal-app` is already created with:
   - `personalgoals.txt`: Your master goals list
   - `backup_needs.txt`: Documentation of your backup requirements
2. **Backup System**: Implement the backup strategy outlined in Section 7
3. **Tool Selection**: Choose your primary tracking system (Notion/Airtable/Google/Obsidian)
4. **Goal Definition**: Write SMART goals for each of your four areas using the templates in Section 6 as inspiration
5. **Tracking Setup**: Create your tracking system in your chosen tool
6. **Obsidian Integration**: Link your tracking system to your Obsidian vault
7. **Schedule Reviews**: Set up recurring weekly and monthly review times in your calendar
8. **Begin Execution**: Start with your highest priority action from any goal area
9. **First Review**: Conduct your first weekly review after one week of effort
10. **Iterate**: Continuously improve your system based on what works and what doesn't

### 10. Maintenance
- Update your tracking system weekly
- Refresh goals quarterly based on progress and changing priorities
- Add new goal categories as needed (beyond the initial four framework)
- Share successes and learnings with accountability partners
- **Backup Verification**: Include backup status check in weekly and monthly reviews
- **System Maintenance**: Quarterly review of your tools and processes for efficiency

### 11. Related Skills to Explore
- `productivity-notion`: For advanced goal tracking databases
- `productivity-airtable`: For flexible goal management
- `productivity-google-workspace`: For integrated goal tracking suite
- `software-development-plan`: For detailed action planning
- `creative-architecture-diagram`: For visual goal mapping
- `creative-humanizer`: For refining goal language for motivation
- `software-development-systematic-debugging`: For overcoming obstacles
- `note-taking-obsidian`: For enhancing your existing Obsidian workflow
- `mcp-hexstrike-ai_*`: For security testing skills (when backend is available)
- `mlops-*`: For AI/ML deployment skills (for your passive income goal)