---
name: hermes-surfaces-and-state-sharing
description: CLI, dashboard, desktop surfaces share state.db sessions.
version: 1.0.0
author: Hermes Agent
tags: [hermes, cli, dashboard, desktop, tui, sessions, state-sharing, architecture]
---

# Hermes Agent Surfaces: Cross-Surface State Sharing

The CLI (`hermes`), the web dashboard (`hermes dashboard` on http://localhost:9119),
the Ink TUI (`hermes --tui`), and the Electron desktop app are different interfaces into
**one shared agent ecosystem**. Sessions, config, skills, MCP servers, cron jobs, and
memory are shared across all surfaces via `~/.hermes/state.db` and the profile directory.

## Shared Resources

| Resource | Path | Shared? |
|---|---|---|
| Session history (messages, metadata) | `~/.hermes/state.db` (SQLite + FTS5) | YES |
| Session transcripts (JSONL) | `~/.hermes/sessions/` | YES |
| Config | `~/.hermes/config.yaml` | YES |
| API keys/secrets | `~/.hermes/.env` | YES |
| Installed skills | `~/.hermes/skills/` | YES |
| MCP servers | `config.yaml` + `~/.cursor/mcp.json` | YES |
| Cron jobs | `~/.hermes/cron/` + `state.db` | YES |
| Memory (cross-session) | `~/.hermes/memories/` | YES |

Both the CLI process and the dashboard process open `state.db` as file descriptors — they
read and write the same SQLite database concurrently. Verified in-session: the dashboard
process (PID 7306, port 9119) and the active CLI process both have `state.db` open.

## Session Source Tags

Every session is stamped with a `source` field in `state.db` (column: `sessions.source`),
letting the dashboard and CLI filter sessions by origin.

| Source | Surface that creates it |
|---|---|
| `cli` | `hermes chat` (classic REPL), `hermes chat -q` |
| `tui` | `hermes --tui` standalone, OR the dashboard's embedded chat panel |
| `desktop` | Electron desktop app chat panel (`HERMES_DESKTOP=1` env set) |
| `telegram` / `discord` / `slack` / etc. | Messaging platform gateway |
| `cron` | Scheduled cron jobs |
| `tool` | Subagent delegations via `delegate_task` |

## How the Dashboard's Embedded Chat Creates Sessions

The dashboard (`hermes dashboard`) does NOT run the agent itself. When you type in the
dashboard's Chat tab:

1. The web server (`web_server.py`) spawns or attaches to a TUI gateway process via PTY.
   See `_resolve_chat_argv()` in `hermes_cli/web_server.py`.
2. The child env gets `HERMES_TUI_DASHBOARD=1` set (tells the TUI it's in a browser,
   disables mouse tracking for xterm.js — but does NOT change the session source tag).
3. The TUI gateway process calls `session.create` over JSON-RPC (via `tui_gateway/entry.py`
   connecting to `tui_gateway/server.py`).
4. The source is determined by `_resolve_session_platform()` in `tui_gateway/server.py`:

```python
def _resolve_session_platform() -> str:
    if is_truthy_value(os.environ.get("HERMES_DESKTOP")) and not is_truthy_value(
        os.environ.get("HERMES_DESKTOP_TERMINAL")
    ):
        return "desktop"
    return "tui"
```

So the dashboard's embedded chat creates sessions with `source="tui"` — same as standalone
`hermes --tui`. The `HERMES_TUI_DASHBOARD` env var only affects TUI behavior, not the
session source tag.

## How to Check Which Surfaces See Which Sessions

From the CLI:
```bash
hermes sessions list
hermes sessions list --source cli
hermes sessions list --source tui
hermes sessions list --exclude-sources cron,tool
```

From SQL:
```bash
sqlite3 ~/.hermes/state.db "SELECT source, COUNT(*) FROM sessions GROUP BY source;"
```

## Cross-Surface Capabilities

- Resume a CLI session from the dashboard (and vice versa) — same `state.db`.
- Files and working directory are shared — both surfaces use the same `~` home and `cwd`.
- MCP servers are shared — both load from the same `config.yaml` `[mcp_servers]` section.
- Cron jobs see both — a cron job can read sessions created by either surface.

## What Does NOT Cross Over

- **Live conversation state:** If a task is running in the CLI, the dashboard won't show
  live streaming. The session row exists in `state.db` but the message stream is
  process-local.
- **Prompt caching is per-process:** Each surface maintains its own Anthropic prompt cache.
  See AGENTS.md — prompt caching must never break.
- **Background processes are tracked separately:** `delegate_task` subagents are tied to
  their spawning process's lifecycle. Use `cronjob` for durable work.

## Verifying State Sharing

```bash
# Find the dashboard PID (listening on port 9119)
ss -tlnp | grep 9119

# Check its file descriptors for state.db
ls -la /proc/<dashboard-pid>/fd/ | grep state.db

# Check the CLI PID similarly (while a CLI session is active)
ls -la /proc/<cli-pid>/fd/ | grep state.db
```

## Pitfall: Dashboard --tui flag

Older versions of `hermes dashboard` accepted a `--tui` flag. It was removed (a backward-
compat shim silently ignores it now). The dashboard's embedded chat is always on. If the
Chat tab shows "connection failed," check: dashboard is running
(`hermes dashboard --status`), port 9119 is not blocked, and the TUI build exists
(`ls ~/.hermes/hermes-agent/ui-tui/dist/entry.js` or `HERMES_TUI_DIR` is set).

## References

- `tui_gateway/server.py` — `_resolve_session_platform()` (~line 3245)
- `hermes_cli/web_server.py` — `_resolve_chat_argv()` (~line 14504), `HERMES_TUI_DASHBOARD` (~line 14584)
- `hermes_cli/main.py` — `_resolve_last_session()` (~line 1540)
- `hermes_cli/web_routers/sessions.py` — `GET /api/sessions`
- `tui_gateway/entry.py` — TUI gateway entry point that calls `session.create`