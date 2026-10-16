# OpenRouter Free Models (as of 2026-08-31)

Fetched via `curl https://openrouter.ai/api/v1/models` — 21 free models total.

## Current Free Models

| Model ID | Name | Context | Notes |
|----------|------|---------|-------|
| `openrouter/free` | **Free Models Router** | 200K | **Auto-selects best available free model per request** — avoids individual rate limits |
| `nvidia/nemotron-3-ultra-550b-a55b:free` | NVIDIA: Nemotron 3 Ultra | 1M | Current default before switch |
| `nvidia/nemotron-3.5-lightning:free` | NVIDIA: Nemotron 3.5 Lightning | 1M | Fast, long context |
| `thinkingmachines/inkling:free` | Thinking Machines: Inkling | 1M | Long context |
| `minimax/minimax-m3:free` | MiniMax: MiniMax M3 | 1M | Long context |
| `poolside/laguna-s-2.1:free` | Poolside: Laguna S 2.1 | 262K | Coding-oriented |
| `google/gemma-4-31b-it:free` | Google: Gemma 4 31B | 262K | Strong general purpose |
| `cohere/north-mini-code:free` | Cohere: North Mini Code | 256K | Coding-focused |
| `z-ai/glm-5.2:free` | Z.ai: GLM 5.2 | 256K | Rate-limited (429 observed) |
| `dots-studio/dots-3-note-preview:free` | Dots Studio: Dots3-Note Preview | 512K | |
| `inclusionai/ling-3.0-flash-fin:free` | Ling 3.0 Flash Fin | 262K | Finance-tuned |
| `thinkingmachines/inkling-small:free` | Thinking Machines: Inkling Small | 1M | Smaller variant |
| `poolside/laguna-xs-2.1:free` | Poolside: Laguna XS 2.1 | 262K | Tiny variant |
| `nvidia/nemotron-3.5-content-safety:free` | NVIDIA: Nemotron 3.5 Content Safety | 128K | Safety-focused |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | NVIDIA: Nemotron 3 Nano Omni | 256K | Reasoning |
| `google/gemma-4-26b-a4b-it:free` | Google: Gemma 4 26B A4B | 262K | MoE variant |
| `minimax/minimax-m2.7:free` | MiniMax: MiniMax M2.7 | 196K | |
| `nvidia/nemotron-3-super-120b-a12b:free` | NVIDIA: Nemotron 3 Super | 262K | |
| `liquid/lfm-2.5-2.6b:free` | LiquidAI: LFM2.5-2.6B | 65K | Small, fast |
| `google/lyria-3-pro-preview` | Google: Lyria 3 Pro Preview | 1M | Audio generation |
| `google/lyria-3-clip-preview` | Google: Lyria 3 Clip Preview | 1M | Audio generation |

## Key Finding: Use the Auto-Router

`openrouter/free` automatically routes to whatever free model has capacity. This avoids the 429 rate limits seen on individual models (e.g., `z-ai/glm-5.2:free` returned 429).

**Recommended default**: `openrouter/free`

## Hermes Config Commands

```bash
# Use the Hermes agent's own CLI (not global `hermes` which is a different package)
/root/.hermes/hermes-agent/hermes config set model.aliases.default "openrouter/free"
/root/.hermes/hermes-agent/hermes config set model.default "openrouter/free"
```

The global `hermes` command (`/usr/local/bin/hermes`) is an unrelated npm package (v0.4.4, a chat bot). The actual Hermes Agent runs from `/root/.hermes/hermes-agent/hermes` (Python-based).