---
name: debug-missing-javascript-function
description: A systematic approach to identifying and fixing missing JavaScript function calls that cause scripts to fail, including iterative testing and parameter tweaking.
---

# Debug Missing JavaScript Function

## Description
When a JavaScript game or application fails to run and shows a blank screen or stops responding, a common cause is a missing function that is called but never defined. This skill outlines steps to identify and fix such missing function errors, and then iteratively test and tweak gameplay parameters to achieve the desired experience.

## Steps
1. **Check the browser console** (if running in a browser) for error messages like "`ReferenceError: <function_name> is not defined`".
2. If you cannot access a console, run a syntax check with Node.js:
   ```bash
   node -c /path/to/your/script.js
   ```
   This will report any undefined references if the code does not rely on DOM/BOM.
3. Search the source code for the missing function name (e.g., `rectRectCollision`).
4. If the function is called but not defined, implement it based on its usage context.
   - For an axis-aligned bounding box (AABB) collision function named `rectRectCollision`, the typical implementation is:
     ```javascript
     function rectRectCollision(x1, y1, w1, h1, x2, y2, w2, h2) {
         return !(x1 > x2 + w2 ||
                  x1 + w1 < x2 ||
                  y1 > y2 + h2 ||
                  y1 + h1 < y2);
     }
     ```
5. Insert the function definition before the first place it is used (usually before the main update or game loop function).
6. Re-run the syntax check or reload the page to verify the error is gone.
7. Test the application to ensure the missing functionality now works (e.g., collisions, rendering, etc.).
8. **Iterative testing and tweaking**: After fixing the missing function, you may need to adjust game parameters (jump strength, platform spacing, enemy speed, etc.) to achieve the desired difficulty and playability.
   - Playtest the game from start to finish.
   - Identify sections that feel too easy or too hard.
   - Adjust one variable at a time (e.g., increase jump height, move a platform closer/farther, adjust enemy speed).
   - Reload and test again.
   - Repeat until the gameplay feels balanced.
   - Use browser developer tools to tweak values in real-time if possible.

## Example
In a 2D platformer game, the enemy collision check used:
```javascript
if (rectRectCollision(game.player.x, game.player.y, 30, 40, enemy.x, enemy.y, 30, 30)) {
```
but `rectRectCollision` was missing, causing the game loop to halt. Adding the function above fixed the issue. After fixing, playtesting revealed the initial jump was too low to reach the first platform; increasing the jump power from 13 to 16 and adding a stepping stone platform made the level beatable while retaining challenge.

## Verification
- After adding the function, run `node -c` on the script file (if applicable) to ensure no syntax errors.
- Open the HTML file in a browser and confirm the game runs as expected.
- Playtest to verify that the gameplay feels appropriate and adjust parameters as needed using the iterative process.

## Note
If the missing function is a method on an object (e.g., `someObject.method()`), ensure the object is properly initialized and the method is attached to its prototype or instance.