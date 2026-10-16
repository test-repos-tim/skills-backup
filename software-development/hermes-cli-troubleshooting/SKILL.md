---
name: hermes-cli-troubleshooting
description: "Troubleshoot Hermes CLI: npm hermes vs Python agent CLI."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [hermes, cli, troubleshooting, config, openrouter]
    category: software-development
---

# Hermes CLI Troubleshooting

## The Critical Confusion

**Two different `hermes` commands exist on the system:**

| Command | Path | Type | Purpose |
|---------|------|------|---------|
| Global npm `hermes` | `/usr/local/bin/hermes` → `/usr/local/lib/node_modules/hermes/bin/hermes` | Node.js package v0.4.4 | Unrelated chat bot (segmentio/hermes) |
| Actual Hermes Agent | `/root/.hermes/hermes-agent/hermes` | Python CLI | The real Hermes Agent you're using |

**The global `hermes` command does NOT work for Hermes Agent config.** It tries to load a Node module and fails with `Error: Cannot find module '/tmp/config'`.

## Always Use the Agent's Own CLI

```bash
# CORRECT - Use the Hermes Agent's Python CLI
/root/.hermes/hermes-agent/hermes config set model.aliases.default "openrouter/free"
/root/.hermes/hermes-agent/hermes config get model.default
/root/.hermes/hermes-agent/hermes config --help

# WRONG - Global npm hermes (different package)
hermes config set ...  # Fails with module not found errors
```

## OpenRouter Free Model Selection

### Current Free Models (as of 2026-08-31)

21 free models available via `curl https://openrouter.ai/api/v1/models`:

**Recommended: `openrouter/free` (Auto-Router)**
- Automatically routes to best available free model per request
- Avoids individual model rate limits (429 errors)
- Context: 200K tokens

**Other notable free models:**
- `nvidia/nemotron-3-ultra-550b-a55b:free` — 1M context (was default)
- `nvidia/nemotron-3.5-lightning:free` — 1M context, fast
- `thinkingmachines/inkling:free` — 1M context
- `minimax/minimax-m3:free` — 1M context
- `poolside/laguna-s-2.1:free` — 262K, coding-oriented
- `google/gemma-4-31b-it:free` — 262K, strong general
- `cohere/north-mini-code:free` — 256K, coding-focused
- `z-ai/glm-5.2:free` — 256K, **rate-limited (429 observed)**

### Switching Models

```bash
# Use the Agent's CLI
/root/.hermes/hermes-agent/hermes config set model.aliases.default "openrouter/free"
/root/.hermes/hermes-agent/hermes config set model.default "openrouter/free"

# Verify
/root/.hermes/hermes-agent/hermes config get model.default
```

## Common Issues & Fixes

| Symptom | Cause | Fix |
|---------|-------|-----|
| `Error: Cannot find module '/tmp/config'` | Using global npm `hermes` | Use `/root/.hermes/hermes-agent/hermes` |
| `429 rate limited` on free model | Individual model capacity exhausted | Switch to `openrouter/free` auto-router |
| `User not found` (401) | API key invalid or not in credential store | Check `hermes config get providers.openrouter.api_key` |
| Config changes not persisting | Editing wrong file or wrong CLI | Use Agent CLI, edits go to `/root/.hermes/config.yaml` |

## Config File Location

Active config: `/root/.hermes/config.yaml`

The YAML shows redacted keys (`sk-or-...5591`) — actual keys stored in secure credential store, not in the file.

## Verification Commands

```bash
# Test API key works
curl -s -X POST https://openrouter.ai/api/v1/chat/completions \
  -H "Authorization: Bearer $(/root/.hermes/hermes-agent/hermes config get providers.openrouter.api_key)" \
  -H "Content-Type: application/json" \
  -d '{"model": "openrouter/free", "messages": [{"role": "user", "content": "test"}], "max_tokens": 10}'

# List all free models
curl -s https://openrouter.ai/api/v1/models | python3 -c "
import json, sys
data = json.load(sys.stdin)
free = [m for m in data.get('data', []) if m.get('pricing', {}).get('prompt') == '0']
for m in free: print(m['id'], '|', m.get('context_length', 0))
"
```