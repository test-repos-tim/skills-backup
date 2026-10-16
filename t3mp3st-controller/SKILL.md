---
name: t3mp3st-controller
description: >
  Use when the user wants to control or query a T3MP3ST security operation from Hermes.
  Also supports creating mission documentation files for different execution contexts.
---

# T3MP3ST Controller

Control and query the T3MP3ST tactical execution multi-agent platform from within Hermes.

## Capabilities

1. **Start new operations** — auto, stealth, aggressive, or test mode
2. **Check operation status** — operators, findings, OPSEC risk level
3. **Add targets** — web apps, APIs, networks, hosts, databases, cloud
4. **Create and start missions** — with named objectives
5. **Chat with AI** — get operational analysis and guidance
6. **Generate engagement reports** — findings summary and recommendations

## Numbered Steps

1. **Start new operation**:
   - Run `npx t3mp3st start` in terminal
   - Select operation type: Auto (configured defaults), Stealth (minimal detection), Aggressive (maximum speed), or Test (mock LLM)
   - Enter operation name (defaults to `Operation <timestamp>`)

2. **Check status**:
   - Run `npx t3mp3st status` in terminal
   - View operation state, operator counts (available/busy/cooldown/burned), findings by severity, and OPSEC risk

3. **Add target**:
   - Run `npx t3mp3st add-target`
   - Enter target address (URL or IP)
   - Select target type: web_application, api, network, host, database, cloud
   - Choose target zone: external, dmz, internal, restricted

4. **Create mission**:
   - Run `npx t3mp3st create-mission`
   - Enter mission name (default: Primary Mission)
   - Enter objectives (comma-separated: e.g., "Enumerate attack surface, Identify vulnerabilities, Document findings")

5. **Chat with AI**:
   - Run `npx t3mp3st chat`
   - Type messages for AI analysis of operation status
   - Type "exit" to return to main menu

6. **Generate report**:
   - Run `npx t3mp3st report`
   - View detailed engagement report with findings, severity breakdown, and recommendations

## Pitfalls

- Configure API keys first with `npx t3mp3st setup` if no providers are detected
- Target validation rejects anything outside `[A-Za-z0-9._:-]` — no shell metacharacters allowed
- OPSEC risk level "critical" or abort recommended means reconsider the operation approach
- Verify mission creation succeeded before attempting to generate a report

## Verification Steps

1. Confirm operation shows "RUNNING" status in the status output
2. Verify target appears with the correct address, type, and zone
3. Confirm mission status is "ACTIVE" before proceeding
4. Check report includes all specified objectives and findings
5. Ensure AI responses are coherent and relevant to current operation state

## Usage Example

```
$ npx t3mp3st start
Operation name: NightOwl
Operation type: stealth
✓ Operation "NightOwl" started!

$ npx t3mp3st status
═══ OPERATION STATUS ═══

Operation: NightOwl
Status: RUNNING
Tick Count: 42

Operators:
  Available 5 | Busy 2 | Cooldown 1 | Burned 0 | Total 8

Findings:
  Critical 0 | High 1 | Medium 3 | Low 2 | Info 4

OPSEC: HIGH
Detections: 1/5

⚠ ABORT RECOMMENDED
```

## Mission File Creation

When a mission is defined (e.g., `mtest1`), create three documentation files in `/home/shiva/tools/T3MP3ST/missions/`:
- `<mission>_withhermes.txt` — How to execute via the t3mp3st-controller skill in Hermes
- `<mission>_cli.txt` — How to execute using native Kali Linux CLI tools (dig, nmap, curl, gobuster, nikto, etc.)
- `<mission>_withtempest.txt` — How to execute via the T3MP3ST CLI (`npx t3mp3st`)

Example for mission `mtest1` targeting `pentest-ground.com:81` (external web app):
```bash
mkdir -p /home/shiva/tools/T3MP3ST/missions
# Creates:
#   missions/mtest1_withhermes.txt
#   missions/mtest1_cli.txt
#   missions/mtest1_withtempest.txt
```

## CLI Reference

| Command | Action |
|---|---|
| `npx t3mp3st start` | Start a new interactive operation |
| `npx t3mp3st status` | Display current operation status |
| `npx t3mp3st add-target` | Add a new target to the environment |
| `npx t3mp3st create-mission` | Create and start a new mission |
| `npx t3mp3st chat` | Chat with AI assistant |
| `npx t3mp3st report` | Generate engagement report |
| `npx t3mp3st setup` | Configure API keys and providers |
| `npx t3mp3st stop` | Stop the current operation |

## MCP Server

T3MP3ST also exposes an MCP server with the `security_recon` tool for nmap/DNS reconnaissance:
- `npx t3mp3st mcp` — start the MCP server (stdio transport)
- Tool: `security_recon` — run nmap/DNS scans against a target with configurable depth (quick/standard/full/stealth)