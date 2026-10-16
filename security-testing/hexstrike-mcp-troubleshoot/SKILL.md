---
name: hexstrike-mcp-troubleshoot
description: Troubleshoot a non‑responsive HexStrike AI MCP server for mcporter usage.
summary: Steps to recover when mcporter reports connection refused or 404 errors.
---

## Procedure
1. **Check running processes**
   ```bash
   process action=list
   ```
   Look for a background process running `hexstrike_server.py` (or `hexstrike_mcp.py`). Note its `session_id`.
2. **Inspect recent output (optional)**
   ```bash
   process action=log session_id=<session_id> limit=200
   ```
   Look for errors about the wrong script or port binding.
3. **If the wrong script is running** (e.g., `hexstrike_mcp.py` which serves STDIO instead of HTTP):
   - Terminate it:
     ```bash
     process action=kill session_id=<session_id>
     ```
   - Start the correct server in background:
     ```bash
     python3 /usr/share/hexstrike-ai/hexstrike_server.py --port 8888 &
     ```
   - Capture the new `session_id` from the start message.
4. **Verify the server is reachable via mcporter**
   ```bash
   mcporter call hexstrike-ai.server_health
   ```
   A successful JSON response with `"status":"ready"` indicates the server is operational.
5. **Run the intended tool** (example bug‑bounty workflow):
   ```bash
   mcporter call hexstrike-ai.bugbounty_reconnaissance_workflow domain:example.com scope:example.com,sub.example.com program_type:web
   ```
   The call should now succeed.

## Tips & Gotchas
- **Wrong entry point**: `hexstrike_mcp.py` launches a STDIO‑only bridge; mcporter expects an HTTP‑based server, so use `hexstrike_server.py`.
- **Port already in use**: If 8888 is occupied, choose another free port and update both the launch command (`--port <new>` ) and the MCP config (`~/.cursor/mcp.json`).
- **Background tracking**: Hermes’ `process` tool is the reliable way to manage the server PID; avoid using raw `ps`/`ss` to keep the workflow portable.
- **Health check**: Prefer the built‑in `hexstrike-ai.server_health` tool over raw `curl` to stay within the MCP ecosystem.

## Validation
After these steps, `mcporter list hexstrike-ai --schema` should work and any subsequent tool calls will return proper JSON output.
