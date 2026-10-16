# OpenRouter API Key Handling

## Pattern
- API key stored only in `orapi.key` file (`OPENROUTER_API_KEY=sk-or-v1-***`)
- Browser cannot read this file; server proxies all auth
- Client calls `/api/status` to confirm server loaded key
- Authentication: `Authorization: Bearer ${apiKey}` header to `openrouter.ai/api/v1/chat/completions`

## Free Model Pattern
- OpenRouter free models have `:free` suffix in ID (e.g., `nvidia/nemotron-3-ultra-550b-a55b:free`)
- Always fetch from `/api/v1/models` and filter; never hardcode
- User's web-login account (`timv80408@gmail.com`) is separate from API auth

## Response Extraction
- Server returns `{statusCode, headers, body}` where `body` is OpenRouter's full response
- Client must access `response.body.choices[0].message.content`
- Chain of thought: `message.thought` / `message.reasoning_details`