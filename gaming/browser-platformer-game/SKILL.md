---
name: browser-platformer-game
description: "Create a simple 2D platformer game that runs in the browser using HTML/CSS/JavaScript, with optional sprite generation via Hermes Web UI."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows, termux]
metadata:
  hermes:
    tags: [game, browser, javascript, html, css]
prerequisites:
  description: |
    Node.js/npm, Python3, and Hermes CLI should be available in the environment.
    A valid Hermes Web UI token is optional for sprite generation.
---

# Browser Platformer Game Skill

## Overview
This skill guides you through creating a simple 2D platformer that runs in a browser. The game includes player movement, jumping, enemies, traps, collectibles, lives, and energy. Sprite assets can be generated via Hermes Web UI's `apikey-image-gen` skill, but the provided JavaScript uses coloured rectangles as placeholders if no images are supplied.

## File Structure
```
/your-game-folder/
    index.html
    style.css
    game.js
```

### index.html
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

### style.css
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

### game.js
*(Copy the full JavaScript implementation from the conversation – it contains the `init`, `createColoredImage`, `Player`, `Enemy`, `Platform`, `Trap`, `Collectible`, `loadLevel`, `updateHUD`, `gameLoop`, and `window.onload = init` sections.)*

## Steps to Run

1. **Prepare the folder**  
   Create a directory for the game and place the three files above inside it.

2. **(Optional) Generate sprite images**  
   If you wish to replace the coloured‑rectangle placeholders with actual sprites:
   - Start Hermes Web UI (e.g., `hermes-web-ui start 6060` in a background process).
   - Use the `apikey-image-gen` skill to create PNG files for player, enemy, platform, trap, and collectible, saving them into the game folder.
   - Update the `game.js` `init()` function to load these files instead of calling `createColoredImage`.
   - If you skip this step, the game will use the built‑in coloured rectangles.

3. **Start a local server**  
   From the game folder, run:
   ```bash
   python3 -m http.server <your-port>
   ```
   Choose a port between 1 and 65535 (e.g., 12345). Ensure the port is free.

4. **Play**  
   Open a browser to `http://localhost:<your-port>/`.  
   Controls:
   - ← / → or A / D – move left/right  
   - ↑ / W or Space – jump  
   - R – restart level (shown on game over/win screen)  
   - N – go to next level (shown on win screen)

5. **Stop the server**  
   Find the process ID and terminate it, e.g.:
   ```bash
   kill $(lsof -t -i:<your-port>)
   ```

## Customisation
- Adjust constants in `game.js` (e.g., `PLAYER_SPEED`, `GRAVITY`, `MAX_ENERGY`) to change difficulty.
- Edit `loadLevel` to add more levels, varied platform layouts, or different enemy/trap placements.
- Replace the coloured‑rectangle drawing in `createColoredImage` with actual image drawing once sprites are available.

## Troubleshooting
- **Hermes Web UI fails to start** – Verify the Hermes CLI is installed and accessible in your `$PATH`.  
- **Port already in use** – Choose a different port or stop the existing process.  
- **No keyboard response** – Click inside the game canvas to give it focus.  
- **Missing images** – If you attempted to use sprites but the files are not found, the canvas will draw nothing; ensure the paths in `game.js` match the file locations.

Enjoy your browser‑based platformer!