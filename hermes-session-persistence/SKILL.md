---
name: hermes-session-persistence
description: Session persistence and resume guide for Hermes Agent.
category: software-development
author: Hermes Agent
version: 1.0.0
---

# Session Persistence in Hermes Agent

## Core Principle

**Skills and config persist immediately** when created via `skill_manage()` or `config set`. They are written to `~/.hermes/skills/` and `~/.hermes/config.yaml` respectively and survive power loss and session restarts.

**Conversational context does NOT persist automatically.** Session history, in-progress tool results, and transient state live in the session store (`~/.hermes/state.db` and `~/.hermes/sessions/`) and must be explicitly resumed or saved.

## When Power Loss Happens

- **Skills you created**: Survive — they're on disk at `~/.hermes/skills/<name>/SKILL.md`.
- **Config changes**: Survive — written to `~/.hermes/config.yaml`.
- **Current conversation**: Lost unless you resume via `hermes --continue` or `hermes --resume <session-id>`.
- **In-progress tool work**: Lost — transcript saved to `sessions/` only if session ended cleanly.

## Commands to Secure Work Before Closing

| Goal | Command | What it does |
|------|---------|-------------|
| Shrink context before exit | `/compress` | Compresses conversation to stay within limits; does NOT save to disk but reduces state on next load. |
| Create restore point | `/snapshot [sub]` | Snapshots `config.yaml`, `state.db`, and skill references to `~/.hermes/snapshots/`. Resume with `hermes --resume <snapshot-name>`. |
| Graceful exit | `/quit` | Cleanly terminates running processes and persists whatever is savable. |
| Resume last session | `hermes --continue` | Reloads most recent session from `sessions/`. |
| Resume specific snapshot | `hermes --resume <id>` | Loads a named snapshot. |

## Resuming After Power Loss

1. Skills and config are already on disk — no action needed.
2. Run `hermes --continue` to restore the most recent session, or `hermes --resume <id>` for a specific prior session.
3. If you need the exact conversation state, check `~/.hermes/sessions/*.jsonl` for saved transcripts.

## What Always Persists (Immediate, No Special Action)

- Skills created via `skill_manage()` → `~/.hermes/skills/<name>/SKILL.md`
- Config changes via `hermes config set` → `~/.hermes/config.yaml`
- Memory entries via `memory()` tool → `~/.hermes/memories/`

## What Requires Explicit Save

- `/snapshot` for full session state restore
- Manual export of `~/.hermes/sessions/*.jsonl` for conversation transcripts
- `/compress` to manage context size (not a persistence save, just a runtime limit)

## Pitfalls & Lessons Learned

**Pitfall**: Assuming conversation history survives power loss.
**Why**: Session context lives in `state.db`/`sessions/`, not in skills or config. Power loss can flush in-memory session data.
**Fix**: Before closing, run `/snapshot` if you want a restorable state, or manually save important transcripts.

**Pitfall**: Thinking skill-creation commands aren't saved if session crashes.
**Why**: `skill_manage()` writes to disk immediately — the skill file exists on disk after the call returns, regardless of later session state.
**Fix**: Verify with `find ~/.hermes/skills -name '*.md' -mtime -1` after a crash to confirm persistence.

## Verification Commands

```bash
# Check all skills on disk
find ~/.hermes/skills -name '*.md'

# Verify a specific skill persists
cat ~/.hermes/skills/quick-money-passive-income/SKILL.md | head -3

# List recent snapshots
ls ~/.hermes/snapshots/

# Check session store
ls ~/.hermes/sessions/*.jsonl | tail -5
```

---

*This skill is class-level: any Hermes session can reference it for session‑durability guidance. It is NOT tied to a specific incident, PR, or error string.*