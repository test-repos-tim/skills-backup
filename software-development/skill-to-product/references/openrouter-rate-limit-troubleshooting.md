# OpenRouter Rate Limit Troubleshooting

## Symptom

When calling OpenRouter API, you get:

```json
{"error": {"message": "Rate limit reached for requests", "type": "requests", "param": null, "code": "429"}}
```

or

```json
{"error": {"message": "Rate limit reached for tokens", "type": "tokens", "param": null, "code": "429"}}
```

## Root Cause

OpenRouter free-tier models have per-API-key rate limits that are shared across all users. These limits are typically:

- Requests per minute: ~20 requests/min for most free models
- Tokens per minute: varies by model (typically 20K-200K tokens/min)
- Some models have daily caps

The limits are shared across the entire API key. Multiple rapid requests during testing or from multiple users can hit the ceiling quickly.

## Why It Happened in This Session

The model `poolside/laguna-s-2.1:free` was called multiple times in rapid succession during testing. The free tier has tight rate limits and shared capacity. When the rate limit is hit, it returns HTTP 429.

## Solutions

### 1. Use a Better Free Model (Recommended)

Switch to `nvidia/nemotron-3-ultra-550b-a55b:free`:
- 1M token context (vs 262K for Laguna)
- Designed for research/analysis tasks
- More generous rate limits
- Produces better research summaries

### 2. Handle 429 Gracefully

```python
if resp.status_code == 429:
    retry_after = resp.headers.get('Retry-After', '60')
    return f"ERROR: Rate limit reached. Please try again in {retry_after} seconds."
```

### 3. Implement Key Rotation (For Multiple Users)

```python
API_KEYS = os.environ.get('OPENROUTER_API_KEYS', '').split(',')
key_pool = itertools.cycle(API_KEYS)
```

### 4. Upgrade to Paid Tier

OpenRouter paid tier ($10-50/month) removes free-tier limits entirely.

## Model Comparison for Research Tasks

| Model | Context | Rate Limit | Quality | Best For |
|---|---|---|---|---|
| nvidia/nemotron-3-ultra-550b-a55b | 1M tokens | Generous | Excellent | Research, long docs |
| nvidia/nemotron-3-super-120b-a12b | 262K | Good | Excellent | Research, coding |
| openai/gpt-oss-20b | 131K | Moderate | Good | General purpose |
| poolside/laguna-s-2.1 | 262K | Tight | Good | General purpose |
