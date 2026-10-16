---
name: mcp-discovery
description: Checklist for discovering and verifying MCP servers in a Linux environment.
title: MCP Discovery Procedure
category: tools
---

# MCP Discovery Procedure

Use this reusable checklist when you need to determine whether any Model Context Protocol (MCP) servers are configured or discoverable in your environment.

## Step‑by‑Step Overview

1. **Attempt to invoke the official MCP client**  
   ```bash
   mcporter list
   ```  
   - If the command succeeds, it will output any configured MCP endpoints.  
   - If the command is unavailable, continue to the next step.

2. **Confirm that the client binary is present**  
   ```bash
   which mcporter
   ```  
   - A non‑empty result indicates the binary exists but may not be on your `$PATH`.  

3. **Search the file system for MCP references**  
   - Use the built‑in `search_files` tool (or equivalent) to locate any files or directories that contain the term “mcp”.  
   - Example: `search_files pattern="mcp" target="files" path="."`

4. **Inspect common configuration locations**  
   - Check environment variables for MCP‑related settings.  
   - Look in typical config directories such as `~/.config/mcp*` or `~/.mcp*`.

5. **Validate network connectivity (if an endpoint is expected)**  
   - Perform a simple HTTP HEAD request to the reported URL or IP address to confirm accessibility.

## Common Issues & Fixes

| Symptom | Likely Cause | Remedy |
|---------|--------------|--------|
| `mcporter: command not found` | Client not installed or not in `$PATH`. | Install the client (e.g., via package manager or `pip`) and ensure the install directory is included in `$PATH`. |
| Binary found but `list` returns nothing | No servers configured, or the client is pointing at a different config location. | Verify the configuration files in the default and custom directories. |
| Excessive search results | Overly broad query. | Refine the pattern (e.g., `*mcp*.json`) or limit the search to known config paths. |
| Unable to reach endpoint | Network block, firewall, service down, or MCP server not started. | Test connectivity with `curl` or `ping`. If the server is not running, start the MCP server using the appropriate HexStrike script (e.g., `hexstrike_mcp.py` with `--server` argument). The client will attempt to connect, fail, and then launch the server automatically. Re‑run the connectivity check after start. |

## When to Stop

If after completing the above steps you have confirmed that no MCP client binary is installed, no relevant configuration files exist, and no network endpoints are reachable, you can conclude that **no MCP servers are currently available** in this environment. At that point you may choose to configure a new server, consult additional resources, or seek assistance from the system administrator. For detailed steps on launching offline MCP servers, see the `mcp-server-launch` skill.

## Reusability

Because this procedure is generic, it can be applied to any project or platform that uses MCP. Store it as a reusable skill (e.g., `mcp-discovery`) and invoke it whenever you need to perform a quick audit of MCP connectivity.