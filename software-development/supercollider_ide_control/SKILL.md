---
name: supercollider_ide_control
description: Guide to start, control, and script SuperCollider IDE and REPL using only user‑level commands.
version: "1.0"
maintainer: user
---

# SuperCollider IDE Control Skill (user‑level only)

This skill explains how to launch the SuperCollider IDE (`scide`) or the command‑line interpreter (`sclang`), evaluate code, manage synth definitions, and run scripts without requiring elevated privileges.

## Prerequisites
- SuperCollider IDE installed (`scide` and `sclang` available in `$PATH`).
- Audio subsystem active (PulseAudio, CoreAudio, or WASAPI).
- Optional: `xdg-open` (Linux) or `open` (macOS) for launching GUI apps from the terminal.

## Quick Commands
| Goal | Command | Notes |
|------|---------|-------|
| Launch IDE (background) | `scide &` | Keeps terminal free.
| Launch IDE (macOS) | `open -a SuperCollider` |
| Open REPL only | `sclang` |
| Run a .scd script and exit | `sclang /path/to/file.scd` |
| Evaluate a one‑liner from terminal | `sclang -e "{ SinOsc.ar(440,0,0.2) }.play;"` |
| Restart audio server | `s.quit; s.boot;` (type in REPL) |
| Open built‑in help browser | `HelpBrowser.help;` |
| Stop the IDE process | `pkill -f scide` |
| Reload current file in IDE | `File.reload;` |

## Typical Workflow
### 1. Start the IDE
```bash
scide &            # background launch, terminal remains usable
# macOS alternative
open -a SuperCollider
# Linux desktop shortcut (if .desktop file exists)
xdg-open /usr/share/supercollider/scide.desktop
```

### 2. Open a project or file
```bash
scide ~/myproject/demo.scd &
```
Or use **File → Open…** inside the IDE (`Ctrl‑O`).

### 3. Evaluate code
- Highlight a block → **Ctrl‑Enter** (Linux/Windows) or **Cmd‑Enter** (macOS).
- Whole buffer → **Ctrl‑Shift‑Enter**.
- Quick one‑liner without the IDE:
```bash
sclang -e "{ Saw.ar(440,0.1) }.play;"
```

### 4. Define and use a `SynthDef`
```supercollider
(
SynthDef(\buzz, { |freq=220, amp=0.1|
    var sig = Pulse.ar(freq, 0.3, amp);
    sig = LPF.ar(sig, freq*2);
    Out.ar(0, sig!2);
}).add;
)

x = Synth(\buzz, [\freq, 440, \amp, 0.15]);   // start synth
x.set(\freq, 660);                               // live tweak
x.free;                                           // stop synth
```
Paste the block into the IDE and evaluate with **Ctrl‑Enter**.

### 5. Manage the audio server (`scsynth`)
```supercollider
Server.default.boot;    // start if not running
Server.default.quit;    // stop
Server.default.restart; // restart (useful after driver changes)
# Quick reset from REPL
s.quit; s.boot;
```

### 6. Run a script non‑interactively (automation / CI)
```bash
sclang /path/to/automation.scd   # runs script and exits
```
Include `s.boot;` / `s.quit;` inside the script if explicit control is needed.

## Tips & Gotchas
- **Audio latency** – ensure PulseAudio or JACK is running before `s.boot;` on Linux.
- **Port conflicts** – `scsynth` uses UDP 57110; if you see "already in use", stop stray instances with `pkill -f scsynth`.
- **Version consistency** – keep the IDE and `scsynth` at the same major version.
- **Remote server** – connect to a remote audio server with `s = Server.remote("host", 57110); s.boot;`.

---
**Example Session**
```bash
# start IDE in background
scide &
# open a demo file
scide ~/demo.scd &
# fire a quick tone from terminal
sclang -e "{ SinOsc.ar(440,0,0.2) }.play;"
```

Retrieve this guide anytime with `skill_view(name="supercollider_ide_control")`.
