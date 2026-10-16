---
name: Audio Processing – Audacity Pipe vs CLI Tools
description: Guide for audio manipulation when Audacity is installed on a Linux system. Covers using Audacity's pipe interface on a normal desktop, fallback to command‑line tools (ffmpeg, sox) for headless environments, and optional VNC setup for remote GUI.
---

## Steps

1. **Check Audacity installation**
   ```bash
   which audacity
   audacity --version
   ```

2. **If you have a real X display (desktop Linux)**
   - Start Audacity with pipe support:
     ```bash
     audacity --pipe &
     ```
   - Locate the pipe (usually `~/.audacity_pipe`).
   - Send commands via the pipe, e.g.:
     ```bash
     echo "Import2:/path/file.wav" > ~/.audacity_pipe
     echo "Command=SelectAll" > ~/.audacity_pipe
     echo "Command=Normalize:Level=-1.0" > ~/.audacity_pipe
     echo "Command=SaveProject2:/path/project.aup" > ~/.audacity_pipe
     ```
   - See Audacity’s *Scripting with the Pipe* documentation for the full command set.

3. **If you are in a headless VM (no X server)**
   - Audacity’s pipe requires a functional X environment; it will exit immediately under plain Xvfb.
   - Use pure CLI audio tools instead. Ensure `ffmpeg` and `sox` are installed (e.g., `apt install ffmpeg sox`).
   - Common tasks (replace `<input>`/`<output>` as needed):
     - Convert WAV → MP3
       ```bash
       ffmpeg -i <input>.wav -codec:a libmp3lame -qscale:a 2 <output>.mp3
       ```
     - Trim first 30 s
       ```bash
       ffmpeg -ss 00:00:30 -i <input>.wav -c copy trimmed.wav
       ```
     - Normalize to –1 dB
       ```bash
       ffmpeg -i <input>.wav -filter:a "volume=-1dB" normalized.wav
       ```
     - Export spectrogram image
       ```bash
       ffmpeg -i <input>.wav -lavfi showspectrumpic=s=800x600:saturation=2 spectrogram.png
       ```
     - *SoX equivalents* (useful if ffmpeg is unavailable):
       ```bash
       sox <input>.wav <output>.mp3
       sox <input>.wav trimmed.wav trim 30
       sox <input>.wav normalized.wav gain -1
       sox <input>.wav -n spectrogram -o spectrogram.png
       ```
   - These tools work entirely in the terminal and are ideal for automated scripts.

4. **Optional remote GUI via VNC (if you really need Audacity UI)**
   - Install a lightweight window manager and VNC server (e.g., `apt install fluxbox x11vnc xvfb`).
   - Start a virtual X server with a WM and launch VNC:
     ```bash
     xvfb-run -s "-screen 0 1024x768x24" fluxbox &
     x11vnc -display :99 -nopw -forever &
     ```
   - Connect with a VNC client to `localhost:5900` and run Audacity normally.
   - Note: This adds overhead and is only needed for visual editing.

## Pitfalls
- Audacity’s pipe will not work under pure Xvfb without a window manager or DBus; the process exits immediately.
- Escape special characters in pipe commands (e.g., spaces in file paths).
- CLI tools may produce slightly different audio quality; verify if the result is critical.

## Verification
- Run a simple ffmpeg conversion and inspect the output file size/format.
- On a desktop, send a basic `Import2:` command and verify the track appears in Audacity.
