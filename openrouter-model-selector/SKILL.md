---
name: openrouter-model-selector
description: Enhanced OpenRouter model selector with detailed capability scores.
version: 2.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [openrouter, model, selection, configuration]
---

# OpenRouter Model Selector Skill

This skill guides Hermes to fetch the list of free models available on OpenRouter, present them to the user for selection with detailed capability scores, and set the chosen model as the default model in Hermes.

## When to Use

Use this skill when you want to quickly switch to a free LLM provider on OpenRouter without manually looking up model names and configuring Hermes, and when you want detailed capability scores to make an informed selection.

## Prerequisites

- An OpenRouter API key must be configured in Hermes (via `hermes auth add openrouter` or setting `OPENROUTER_API_KEY` in `.env`).
- The `hermes` CLI must be available in the current environment.

## Procedure

When the user invokes this skill, the agent should follow these steps:

### 1. Fetch Free Models

- Use the `terminal` tool to call the OpenRouter API: `curl -s https://openrouter.ai/api/v1/models`
- Capture the JSON response and save it to a temporary file for processing

### 2. Present Selection Menu with Enhanced Scoring

- Use `terminal` tool to create an interactive model selection script that:
  - Fetches models from OpenRouter API
  - Calculates and displays scores for novel writing (1-10), coding (1-10), and other capabilities
  - Shows guardrailed score (1-10, where 10 = most censored/guardrailed)
  - Presents models in a table with selection numbers (1, 2, 3...)
  - Displays current model being questioned
  - Allows user to type the number and enter to select
- The script should include:
  - Novel writing score (1-10): based on reasoning, agentic capabilities, creativity indicators, context length
  - Coding score (1-10): based on coding benchmarks, tool support, reasoning
  - Other capabilities as yes/no: multimodal, agentic, web search
  - Guardrailed score (1-10): based on moderation level
  - Context length (tokens)
  - Tools support (yes/no)
  - Reasoning enabled (yes/no)
- Display current model info at the top: "Currently set model: [model_name] (if any)"
- Prompt: "Select a free model from OpenRouter to set as the default in Hermes:"

### 3. Set the Selected Model in Hermes

- Let the selected model's `id` be `MODEL_ID`.
- Use the `terminal` tool to run: `hermes model set MODEL_ID`
  - This sets the model for the current Hermes session.
- To make it the default for future sessions, run: `hermes config set model.aliases.default MODEL_ID`
  - (Alternatively, check if `hermes model set --global MODEL_ID` is supported by running `hermes model --help` and adjust accordingly.)
- Verify the change by running `hermes model` and checking the current model.

### 4. Provide Feedback

- Inform the user that the model has been set successfully.
- Show the selected model's details (name, scores, context length, etc.).

## Notes

- The skill assumes the OpenRouter API returns data in the expected format. If the API changes, the parsing may need adjustment.
- The scoring for novel writing and coding is based on benchmark data and heuristics from model descriptions - it may not be perfect but provides a good starting point.
- The guardrailed score is based on moderation status and model characteristics - higher scores indicate more conservative/content-safe models.
- If the user wants to revert to a previous model, they can use `hermes model set <previous>` or adjust the config manually.

## Example Output

After invoking this skill, the user might see a prompt like:

"Currently set model: openai/gpt-4o-mini (free)"

"Select a free model from OpenRouter to set as the default in Hermes:"

```
#   Model Name                                    ID                                    Novel  Code  Guard  Context  Tools  Reasoning  Description
1   Claude Opus 5                                anthropic/claude-opus-5                     9/10    8/10   8/10    1M tokens   yes       yes     Flagship model for demanding reasoning...
2   Gemini 3.6 Flash                             google/gemini-3.6-flash                      7/10    8/10   5/10    1M tokens   yes       yes     High-efficiency model for coding and...
3   DeepSeek V4 Flash                            deepseek/deepseek-v4-flash-0731             8/10    9/10   3/10    1M tokens   yes       yes     Sparse MoE model with 13B active params...
```

Instructions:
Enter the number of the model you want to select (e.g., "1" for Claude Opus 5)

## Author Notes

This skill was created to streamline the process of experimenting with free LLMs on OpenRouter within Hermes. The enhanced scoring system helps users make informed decisions based on their specific needs (novel writing, coding, etc.).

---