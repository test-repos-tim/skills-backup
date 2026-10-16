---
name: nutcracker-control
title: Nutcracker Mobile Security Tool - Control Skill
description: Provides concise CLI wrappers and workflow guidance for the Nutcracker mobile security and offensive threat intelligence framework.
author: Hermes Agent
version: 0.1
---

# Overview

This skill assists you in operating the **Nutcracker** mobile security framework (https://github.com/drneox/nutcracker). It summarizes the most common commands, required prerequisites, and typical workflow steps.

# Prerequisites

- Python 3.10+ with a virtual environment activated (`source .venv/bin/activate`).
- System tools installed (as per Nutcracker README): `apkeep`, `jadx`, `apktool`, `adb`, `frida-server`, `semgrep`, `apkleaks` (optional).
- Android SDK / emulator reachable via `adb`.
- Optional API credentials in `config.yaml` (Google Play AAS token, OpenAI key for `ai-review`).

# Installation (once, assuming the repo is already present)

```bash
# Navigate to the existing checkout
cd nutcracker
# Create and activate a venv if not already done
python3 -m venv .venv
source .venv/bin/activate
# Install Python dependencies
pip install -r requirements.txt
```

# Core Commands

| Action | Command | Description |
|---|---|---|
| **Setup API tokens** | `python nutcracker.py setup-token [--serial <device>] [--method auto]` | Initialise Google Play AAS token, OpenAI key, etc. |
| **Analyze local APK** | `python nutcracker.py analyze <path/to/app.apk>` | Runs static & dynamic analysis; produces PDF/JSON reports. |
| **Scan Google Play URL / package** | `python nutcracker.py scan '<PLAY_URL>'`<br>`python nutcracker.py analyze <package_id>` | Downloads the APK (via apkeep) then performs a full scan. |
| **Batch scan** | `python nutcracker.py batch <list.txt>` | `list.txt` holds one package ID or URL per line. |
| **Launch with Frida bypass** | `python nutcracker.py launch <package> [--serial <device>] [--script <js>]` | Restarts `frida‑server`, applies the latest bypass script, and launches the app. |
| **AI Review** | `python nutcracker.py ai-review <package> [--dry-run]` | Sends findings to the configured LLM, tags false positives, and regenerates the PDF. |
| **Help** | `python nutcracker.py --help` | Shows all sub‑commands and options. |

# Quick‑Start Example

```bash
source .venv/bin/activate          # activate environment
python nutcracker.py setup-token   # configure API tokens once
python nutcracker.py scan 'https://play.google.com/store/apps/details?id=com.example.app'
python nutcracker.py ai-review com.example.app   # optional LLM filtering
xdg-open reports/com.example.app.pdf               # view PDF report
```

# Configuration (`config.yaml`)

- Copy `config.yaml.example` → `config.yaml`.
- Populate `google_play.email` / `google_play.aas_token`.
- Enable AI review: `features.ai_review: true` and set `openai.api_key` (or compatible provider).

# Tips & Pitfalls

- **Android 14 SELinux**: `launch` runs `adb root`; ensure the emulator/device permits it.
- **Frida server**: Verify it is running (`adb shell "ps | grep frida"`).
- **Batch size**: Very large `list.txt` files may hit memory limits; split if needed.
- **Report location**: Controlled by `reports.output_dir` (default `./reports`).

# Extending the Skill

If you add custom plugins or post‑hooks, update the command explanations accordingly. Use `skill_manage(action='patch')` to modify this skill later.

---

**In‑session usage**

```text
> nutcracker-control install   # runs the installation snippet above
> nutcracker-control scan com.example.app
> nutcracker-control launch com.example.app --serial emulator-5554
> nutcracker-control review com.example.app
```

The skill will invoke the underlying `python nutcracker.py …` commands, capture the output, and return a short summary (risk score, MASVS compliance, PDF path).