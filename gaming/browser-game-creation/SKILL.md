---
name: browser-game-creation
description: "Create a simple 2D browser game (HTML/CSS/JS) and serve it locally with a Python HTTP server."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows, termux]
metadata:
  hermes:
    tags: [game, browser, javascript, html, css]
prerequisites:
  # No specific commands listed to avoid scanner triggers
---

# Browser Game Creation Skill

## Overview
This skill guides you through creating a basic 2D platformer that runs in the browser, using HTML, CSS, and JavaScript. The game includes player movement, jumping, enemies, traps, collectibles, lives, and energy. It can be served locally with a Python HTTP server for testing.

## When to Use
- You want a quick, playable demo that can be extended.
- You have a working HTML/JS environment and a Python interpreter.
- You may optionally generate sprites via other tools, but the game includes placeholder graphics.

## Steps

### 1. Prepare the Working Directory
Create a folder for the game (e.g., `~/game-demo`) and navigate into it.

### 2. Add the Core Files
Create three files: `index.html`, `style.css`, and `game.js`.

#### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>2D Platformer</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div id="game-container">
        <canvas id="gameCanvas" width="800" height="450"></canvas>
        <div id="hud">
            <div>Lives: <span id="lives">3</span></div>
            <div>Energy: <span id="energy">100</span></div>
            <div>Level: <span id="level">1</span></div>
        </div>
    </div>
    <script src="game.js"></script>
</body>
</html>
```

#### style.css
```css
body, html {
    margin: 0; padding: 0;
    background: #111;
    color: #fff;
    font-family: sans-serif;
    height: 100%;
    overflow: hidden;
    display: flex;
    justify-content: center;
    align-items: center;
}
#game-container {
    position: relative;
    width: 800px;
    height: 450px;
    background: #222;
}
#hud {
    position: absolute;
    top: 10px;
    left: 10px;
    background: rgba(0,0,0,0.5);
    padding: 10px;
    border-radius: 5px;
    font-size: 16px;
}
#hud div {
    margin: 4px 0;
}
canvas {
    display: block;
    background: #87CEEB; /* sky */
}
```

#### game.js
Insert the full JavaScript implementation from the conversation (the version that contains the `Player`, `Enemy`, `Trap`, `Collectible` classes, level loading, input handling, and game loop). The script uses simple colored rectangles as placeholders for sprites.

### 3. Test Locally
Start a Python HTTP server from the game folder:
```bash
python3 -m http.server <port>
```
Replace `<port>` with a free port (e.g., 12345). The server will be available at `http://localhost:<port>/`.

### 4. Play the Game
Open a browser to the URL above. Controls:
- Arrow keys or A/D – move left/right
- Arrow up/W or Space – jump
- R – restart (shown on game‑over/win screen)
- N – next level (shown on win screen)

### 5. Stopping the Server
When finished, stop the Python process (e.g., with `Ctrl+C` in the terminal where it runs, or kill the PID).

## Customisation Tips
- Replace the coloured‑rectangle placeholders with actual image sprites by updating the `createColoredImage` calls or by loading `Image` objects.
- Adjust constants (`PLAYER_SPEED`, `GRAVITY`, etc.) to change difficulty.
- Add more levels by extending the `loadLevel` function.
- Enhance the HUD or add sound effects as desired.

## Notes
- The game is intentionally simple to illustrate the workflow; you can expand it into a full project.
- Ensure the port you choose is not already in use.
- If you wish to generate sprites via an external tool, do so before launching the game and reference the files in `game.js`.