# OpenRouter Rate Limit & Tool-Call Handling

## Problem 1: Tool-Call JSON Instead of Text Response

**Symptom:** The LLM returns JSON like `{"tool": "search", "query": "..."}` instead of actual answer text.

**Root Cause:** Some free-tier models on OpenRouter have tool-calling enabled by default, even when no tools are defined. The model emits JSON in tool-call format instead of plain text.

**Fix:**
```python
payload = {
    "model": model,
    "messages": messages,
    "max_tokens": 3000,
    "temperature": 0.3,
    "tool_choice": "none",    # Force no tool usage
    "tools": []               # Empty tools list
}

# Post-process to catch any remaining JSON tool-call format:
try:
    parsed = json.loads(content)
    if isinstance(parsed, dict) and 'tool' in parsed and 'query' in parsed:
        content = f"Search was performed for: {parsed.get('query', '')}\n\nResults unavailable - please try again."
except (json.JSONDecodeError, TypeError):
    pass  # Normal text response, no action needed
```

## Problem 2: Rate Limit Errors (429)

**Symptom:** HTTP 429 from OpenRouter API.

**Root Cause:** Free-tier models have shared/per-API-key rate limits. Rapid successive requests can exhaust the quota.

**Models ranked by rate limit generosity (free tier):**
1. `nvidia/nemotron-3-ultra-550b-a55b:free` - Most generous, 1M context
2. `nvidia/nemotron-3-super-120b-a12b:free` - Good rate limits, 262K context
3. `openai/gpt-oss-20b:free` - Moderate, 131K context
4. `poolside/laguna-s-2.1:free` - Tightest rate limits, 262K context

**Fix:**
```python
if resp.status_code == 429:
    retry_after = resp.headers.get('Retry-After', '60')
    return f"Rate limit reached. Please try again in {retry_after} seconds."

# For multi-user apps, implement key rotation:
API_KEYS = os.environ.get('OPENROUTER_API_KEYS', '').split(',')
key_pool = itertools.cycle(API_KEYS)
```

## Model Comparison for Research Tasks

| Model | Context | Rate Limit | Quality | Best For |
|---|---|---|---|---|
| nvidia/nemotron-3-ultra-550b-a55b | 1M tokens | Generous | Excellent | Research, long docs |
| nvidia/nemotron-3-super-120b-a12b | 262K | Good | Excellent | Research, coding |
| openai/gpt-oss-20b | 131K | Moderate | Good | General purpose |
| poolside/laguna-s-2.1 | 262K | Tight | Good | General purpose |
