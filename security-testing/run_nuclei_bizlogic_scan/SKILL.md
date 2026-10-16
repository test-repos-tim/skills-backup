---
name: run_nuclei_bizlogic_scan
title: Run a Nuclei business‑logic scan via mcporter
category: security-testing
description: |
  Step‑by‑step reusable guide for launching the interactive mcporter UI, selecting the Nuclei scanner, and executing a `bizlogic` tag scan against a target URL.
---

## Prerequisites
- HexStrike MCP server must be running and reachable.
- `mcporter` CLI installed.
- Nuclei templates up‑to‑date.

## Procedure
1. **Open the interactive tool list**
   ```bash
   npx mcporter list hexstrike-ai --schema
   ```
   Use arrow keys to locate the Nuclei entry, press **Space** to mark it, then **Enter**.
2. **Execute the scan** (replace `<target>` with your URL):
   ```bash
   npx mcporter call hexstrike-ai mcp_hexstrike_ai_nuclei_scan \
       --args '{"target":"<target>","tags":"bizlogic","additional_args":"-rate 150 -timeout 30s"}'
   ```
3. **Optional: store results**
   ```bash
   npx mcporter call hexstrike-ai mcp_hexstrike_ai_nuclei_scan \
       --args '{"target":"<target>","tags":"bizlogic","additional_args":"-rate 150 -timeout 30s"}' \
       > <target>_bizlogic.txt
   ```

## Tips & pitfalls
- If the MCP server is not reachable, start it before step 1.
- Adjust `-rate` if the target throttles requests.
- If no findings appear, refresh Nuclei templates or add more tags.
---