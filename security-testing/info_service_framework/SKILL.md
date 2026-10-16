---
name: info_service_framework
title: Info‑Service Framework (Reusable)
description: Reusable workflow to build low‑cost automated data‑gathering newsletters, alerts and monetisable info services.
summary: A step‑by‑step reusable workflow to build low‑cost, automated data‑gathering newsletters / alerts that can be monetised.
---

## Goal
Create a single‑repo, single‑server pipeline that:
1. **Ingests** public data (Shodan, Gau, Katana, RSS feeds, GitHub releases, exchange APIs, regulator feeds).
2. **Enriches** each record with smart‑scan, technology detection, Nuclei vulnerability checks, price conversion, etc.
3. **Deduplicates & scores** records (sqlite + pandas), assigning a novelty/urgency score.
4. **Renders** a concise markdown / HTML digest via Jinja2 templates.
5. **Distributes** the digest through email (Mailgun/SendGrid), Telegram bot, and Discord webhook.
6. **Monetises** via a static GitHub‑Pages site with Stripe checkout, affiliate links, premium Discord alerts, PDF bundles, or B2B watch services.

## Reusable Components
- **skill: ingest_shodan** – Calls `mcp_hexstrike_ai_shodan_integration` with a query, outputs JSON.
- **skill: ingest_rss** – Uses `curl` to fetch an RSS feed, parses with `feedparser` in Python.
- **skill: enrich_nuclei** – Wraps `mcp_hexstrike_ai_nuclei_scan` (tags optional) to add vulnerability info.
- **skill: enrich_tech** – Calls `mcp_hexstrike_ai_detect_technologies_ai`.
- **skill: dedup_score** – Python script that loads the sqlite DB, drops duplicates, computes a score based on `age`, `severity`, `presence_of_nuclei_match`.
- **skill: render_template** – Jinja2 template renderer; templates live in `templates/` (e.g., `iot.md`, `crypto_fee.md`).
- **skill: send_email** – Wrapper that pipes the rendered markdown to Mailgun/SendGrid via curl.
- **skill: discord_alert** – Posts a short line to a Discord webhook (`curl -X POST -H "Content-Type: application/json" -d '{"content":"…"}' $WEBHOOK`).
- **skill: schedule_job** – Uses `cronjob` tool to run the whole pipeline on a chosen interval.

## High‑Level Procedure (one niche)
1. **Create a skill directory** – `skill_manage action=create name=my_niche_pipeline category=security-testing`.
2. **Populate the skill** with the above component calls, adjusting only:
   - The Shodan query (or other source URLs).
   - The Jinja2 template name.
   - The recipient list / webhook URL.
3. **Test manually** – Run each component step with `execute_code` or direct CLI to verify output.
4. **Commit the skill** – `skill_manage action=edit name=my_niche_pipeline content="<full SKILL.md>"`.
5. **Schedule** – `cronjob action=create name=my_niche schedule="0 9 * * MON" prompt="Run my_niche_pipeline" skill=my_niche_pipeline`.
6. **Launch** – Publish a landing page (GitHub Pages) with a Stripe checkout button; collect emails in a CSV that the `send_email` step reads.
7. **Iterate** – Add a **watchdog** cron (hourly) that calls `mcp_hexstrike_ai_shodan_integration` with `--history` to detect newly indexed assets, compute novelty score, and push high‑score items to a premium Discord channel.

## Optional Enhancements
- **Affiliate integration** – Append affiliate URLs inside the Jinja2 template based on product detection.
- **B2B watch** – Add a webhook to a Slack channel for enterprises.
- **Ad revenue** – Enable Google AdSense on the static site after traffic grows.
- **Community** – Deploy a free Flarum forum (Docker) for paid members; link from Discord.
- **AI‑generated summaries** – Replace the simple Jinja2 rendering with `mcp_hexstrike_ai_intelligent_smart_scan` to produce AI‑written prose.

## Checklist before publishing
- [ ] Verify all external API keys are stored securely (environment variables, GPG‑encrypted files).
- [ ] Rate‑limit every public source (use `-rate` flags, `time.sleep` in scripts).
- [ ] Test the unsubscribe flow for the email list.
- [ ] Add a `feedback.db` table to capture subscriber reactions and auto‑adjust the novelty‑score algorithm.
- [ ] Run a final dry‑run with a test subscriber list.

---
**Usage Example**
```bash
# 1. Create the skill (once)
skill_manage action=create name=iot_risk_pipeline category=security content="$(cat <<'EOF'
# (copy only the needed steps from this skill for IoT)\n...\nEOF
)"

# 2. Schedule it
cronjob action=create name=iot_weekly schedule="0 9 * * MON" prompt="Run iot_risk_pipeline" skill=iot_risk_pipeline
```
Now the pipeline runs automatically each Monday, sends the digest, and you can start charging for the premium Discord alerts.

---
**Why this skill is valuable**
- Encapsulates the entire end‑to‑end workflow in a single reusable definition.
- Allows you to spin up new niches (crypto‑fees, library‑pulse, compliance brief) by copying the skill and changing only the source/query/template.
- Provides a clear monetisation path without additional custom code for each niche.

---
**Next steps**
1. Pick the first niche you want to launch.
2. Create the skill using the template above.
3. Run a manual test run and verify the email arrives.
4. Publish the landing page and start collecting subscribers.
5. Iterate based on feedback and add premium alerts.
