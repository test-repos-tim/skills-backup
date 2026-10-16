---
name: standalone-ai-chat
description: Create self-contained AI chat interfaces for browser use.
---

# Standalone AI Chat Interface

Build local AI chat interfaces using Node.js server + HTML frontend.

## Procedure
1. Create `openrouter-server.cjs` - proxy server that reads API key from `orapi.key` with port conflict handling
2. Create `mtwa.html` - MTWA interface with collapsible sections, API tool toggles, parameter controls, colored headers, top-panel send button
3. Create `orapi.key` with `OPENROUTER_API_KEY=sk-or-v1-***`
4. Run server with persistence: `fuser -k 7777/tcp && cd /home/shiva/tools/MTWAv1 && nohup node openrouter-server.cjs > mtwa.log 2>&1 &`
5. Access interface at `http://localhost:7777/mtwa.html`

## Key Rules
- **Browser cannot read local files**: Use server proxy for `orapi.key`
- **OpenRouter free models**: Filter by `:free` suffix in model IDs
- **ES module conflicts**: Use `.cjs` extension when `package.json` has `"type":"module"`
- **Auth**: `Authorization: Bearer *** header` required
- **Browser state sync**: Client JS must read server `/api/status` to know API key is loaded; don't rely on client-side `appState.apiKey`
- **MTWA tool endpoints**: Server exposes `/api/web-search` (DuckDuckGo), `/api/web-extract`, `/api/file-read`, `/api/file-write`, `/api/terminal`, `/api/memory` for tool-enabled testing
- **Collapsible sections**: Use arrow toggle controls for UI sections; collapsed state persists per section
- **Colored headers**: Cyan for keys, green for values, gold for content; use inline styles for consistent rendering
- **Parameter controls**: Temperature, max_tokens, top_p, stream, top_k, response_format, presence_penalty, frequency_penalty
- **Source tracking**: Explicitly state where each answer comes from (model knowledge, web search, tool result, mixed sources)
- **Port conflict handling**: Server implements EADDRINUSE retry logic (wait 5s, retry) instead of crashing
- **Top-panel controls**: SEND button and progress dial in top gold panel for immediate feedback
- **Model dropdown retry**: `fetchModels()` and `loadStatus()` implement retry logic (5 attempts) for server startup delays
- **Persistence for background processes**: Use `nohup`, `screen`, or `tmux` to keep server running after terminal closes

## Pitfalls
- **401 errors**: Check `orapi.key` format; must start with `sk-or-v1-`
- **Port conflicts**: Server now handles EADDRINUSE gracefully with retry logic; manually use `fuser -k 7777/tcp` to kill stale processes
- **Hardcoded keys**: Store only in `orapi.key`; never in source
- **Wrong model list**: Always fetch from OpenRouter API; don't hardcode
- **Send button disabled despite server having key**: Client doesn't know server has key until `/api/status` called (fixed with retry logic)
- **Response parsing fails**: Server wraps OpenRouter response in `{statusCode, headers, body}`; client must access `response.body.choices[0].message.content`
- **Chain of thought missing**: Check `reasoning`, `reasoning_details`, `thought` fields; OpenRouter returns structured reasoning not always in `thought`
- **Google login vs API key**: Web UI Google auth (`timv80408@gmail.com`) is separate from API auth; only `sk-or-v1-*` key needed
- **Server restart needed**: Configuration changes require server restart; old process must be killed first
- **EADDRINUSE**: Multiple server instances cause port conflict; server now waits and retries instead of crashing
- **File not found when starting standalone server**: Server route handler for root path `/` serves `mtwa.html`
- **Source attribution confusion**: Same model name can give different results via different interfaces; Hermes has its own knowledge/tools separate from OpenRouter models
- **Chain of thought field names vary**: Some models return `reasoning`, others `reasoning_details` array, others `thought`; always check all three
- **Browser cannot execute server tools**: All tool endpoints must be server-side; browser only calls them via fetch
- **UI appears unresponsive after query**: Server processes one query at a time; wait for completion before sending next
- **Background process termination**: Terminal session ending kills background processes; use persistence methods (nohup/screen/tmux)

## References
- `references/openrouter-api-auth.md`: API key handling, authentication patterns, and response parsing
- `references/openrouter-models.md`: OpenRouter free model endpoint patterns and filtering rules
- `references/mtwa-tool-endpoints.md`: MTWA tool endpoint specifications, request/response formats, and implementation details
- `references/model-testing-data.md`: Per-model tracking metrics, token economics, provider routing, and consistency patterns
- `references/server-persistence.md`: Methods for keeping Node.js servers running after terminal closure
- `references/port-conflict-handling.md`: Strategies for handling EADDRINUSE errors in Node.js servers

## References
- `references/openrouter-api-auth.md`: API key handling, authentication patterns, and response parsing
- `references/openrouter-models.md`: OpenRouter free model endpoint patterns and filtering rules
- `references/mtwa-tool-endpoints.md`: MTWA tool endpoint specifications, request/response formats, and implementation details
- `references/model-testing-data.md`: Per-model tracking metrics, token economics, provider routing, and consistency patterns
