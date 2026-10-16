---
name: ffufai-wrapper
description: "Use when running ffufai.py with OpenRouter/OpenAI/Anthropic for AI-chosen fuzzing extensions and wordlists."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [ffuf, fuzzing, web-security, ai-wrapper, openrouter]
    related_skills: [web-pentest, nuclei_scan_extended]
---

# ffufai Wrapper Skill

AI-powered wrapper for `ffuf` that auto-suggests file extensions and contextual wordlists using LLMs via OpenRouter, OpenAI, or Anthropic.

## Overview

`ffufai.py` wraps `ffuf` and calls an LLM to:
- Suggest relevant file extensions for the target (`-e` flag)
- Generate contextual wordlists based on URL, headers, tech stack (`-w` flag via temp file)

All ffuf parameters pass through unchanged.

## When to Use

- Directory/file fuzzing where you want AI-chosen extensions
- Content discovery with tech-stack-aware wordlists
- Any ffuf workflow where manual extension/wordlist crafting is slow

## Prerequisites

1. `ffuf` installed and in PATH (`go install github.com/ffuf/ffuf/v2@latest` or `brew install ffuf`)
2. Python 3.6+ with: `pip install requests openai anthropic beautifulsoup4`
3. One API key in env (priority order):
   - `OPENROUTER_API_KEY` (recommended — any model via OpenRouter)
   - `ANTHROPIC_API_KEY`
   - `OPENAI_API_KEY`
4. Optional: `OPENROUTER_MODEL` to override default (`openai/gpt-4o`)

## Installation

Clone at `/home/shiva/tools/ffufai` (assumed pre-cloned):

```bash
cd /home/shiva/tools/ffufai
pip install requests openai anthropic beautifulsoup4
chmod +x ffufai.py
# Optional symlink
sudo ln -s /home/shiva/tools/ffufai/ffufai.py /usr/local/bin/ffufai
```

## Environment Setup

```bash
# OpenRouter (recommended — access to all models)
export OPENROUTER_API_KEY='sk-or-v1-...'
export OPENROUTER_MODEL='openai/gpt-4o'  # or anthropic/claude-3.5-sonnet, etc.

# Or OpenAI directly
export OPENAI_API_KEY='sk-...'

# Or Anthropic directly
export ANTHROPIC_API_KEY='sk-ant-...'
```

**Key priority:** `OPENROUTER_API_KEY` > `ANTHROPIC_API_KEY` > `OPENAI_API_KEY`

## Usage Patterns

### 1. Extension Fuzzing (default mode)
```bash
python3 /home/shiva/tools/ffufai/ffufai.py -u https://target.com/FUZZ -w /path/to/wordlist.txt
```
AI picks extensions (default max 4) and runs `ffuf` with `-e .ext1,.ext2,...`

### 2. Contextual Wordlist Generation
```bash
python3 /home/shiva/tools/ffufai/ffufai.py --wordlists -u https://target.com/FUZZ
```
AI generates a wordlist (default 200 entries) from URL/headers, writes to temp file, runs `ffuf` with `-w`.

### 3. Wordlist with Response Context (better results)
```bash
python3 /home/shiva/tools/ffufai/ffufai.py --wordlists --include-response -u https://target.com/FUZZ
```
Fetches the base URL first, includes response body/headers/cookies in prompt.

### 4. Custom Wordlist Size
```bash
python3 /home/shiva/tools/ffufai/ffufai.py --wordlists --max-wordlist-size 500 -u https://target.com/FUZZ
```

### 5. Custom ffuf Path
```bash
python3 /home/shiva/tools/ffufai/ffufai.py --ffuf-path /usr/local/bin/ffuf -u https://target.com/FUZZ -w wordlist.txt
```

### 6. Pass-Through ffuf Flags
```bash
python3 /home/shiva/tools/ffufai/ffufai.py -u https://target.com/FUZZ -w wordlist.txt -mc 200 -fs 0 -t 50
```

## Model Selection via OpenRouter

Set `OPENROUTER_MODEL` to any OpenRouter model ID:

```bash
export OPENROUTER_MODEL='openai/gpt-4o'              # default
export OPENROUTER_MODEL='openai/gpt-4o-mini'        # cheaper
export OPENROUTER_MODEL='anthropic/claude-3.5-sonnet'
export OPENROUTER_MODEL='google/gemini-flash-1.5'   # cheapest/fastest
export OPENROUTER_MODEL='meta-llama/llama-3.1-8b-instruct'  # budget
```

## One-Shot Recipes

### Quick extension fuzz with cheap OpenRouter model
```bash
OPENROUTER_API_KEY=$KEY OPENROUTER_MODEL=openai/gpt-4o-mini \
  python3 /home/shiva/tools/ffufai/ffufai.py -u https://example.com/FUZZ -w wordlist.txt
```

### Deep content discovery with response context
```bash
OPENROUTER_API_KEY=$KEY \
  python3 /home/shiva/tools/ffufai/ffufai.py --wordlists --include-response \
  --max-wordlist-size 300 -u https://shop.example.com/checkout/FUZZ
```

### Bulk scan with budget model
```bash
OPENROUTER_API_KEY=$KEY OPENROUTER_MODEL=meta-llama/llama-3.1-8b-instruct \
  python3 /home/shiva/tools/ffufai/ffufai.py -u https://target.com/FUZZ -w wordlist.txt
```

## Common Pitfalls

1. **FUZZ not at end of path** — warns but still runs; extensions may be wrong
2. **Missing API key** — clear error; check which env var is set
3. **Model context limit** — large wordlists may exceed tokens; reduce `--max-wordlist-size`
4. **No ffuf in PATH** — install ffuf or use `--ffuf-path /path/to/ffuf`
5. **Python import errors** — always run with `python3 ffufai.py`, shebang may not be correct
6. **OpenRouter model typos** — model IDs must match exactly; check [openrouter.ai/models](https://openrouter.ai/models)

## Verification Checklist

- [ ] `ffuf --version` works
- [ ] `python3 -c "import openai, anthropic, requests, bs4"` succeeds
- [ ] At least one API key env var set (`OPENROUTER_API_KEY` recommended)
- [ ] Test run: `python3 /home/shiva/tools/ffufai/ffufai.py -u https://httpbin.org/FUZZ -w /usr/share/wordlists/dirb/common.txt --max-extensions 3`

## See Also

- `references/openrouter-models.md` for model recommendations and pricing
- ffuf documentation: https://github.com/ffuf/ffuf/wiki
