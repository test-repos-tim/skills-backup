---
name: persistent-work-storage
description: Maintain code/work across Hermes sessions using fixed file location with verification to prevent context loss
version: 1.0.0
author: Hermes Agent
---

# Persistent Work Storage

## Purpose
Maintain code/work across Hermes sessions by using a fixed file location with verification steps to prevent context loss and ensure work continuity.

## When to Use
- Working on multi-session coding projects
- Need to preserve state between conversations
- Want to avoid repeatedly explaining context or redoing work
- Developing games, websites, or any code that benefits from persistence

## Key Benefits
- Prevents context loss between sessions
- Eliminates need to re-explain project details
- Provides verifiable work persistence
- Enables incremental development across sessions

## When NOT to Use
- Simple one-off tasks that don't need persistence
- Tasks requiring real-time collaboration (use delegate_task instead)
- When working with temporary/disposable code

## Step-by-Step Approach

### 1. Establish Fixed Storage Location
Choose a dedicated directory and file pattern for your work:
```bash
# Example structure
~/projects/[project-name]/[component].html
~/projects/[project-name]/[component].js
~/projects/[project-name]/README.md
```

### 2. Initial Setup
At the start of work:
```bash
# Create directory if needed
mkdir -p /path/to/your/project

# Create initial file if doesn't exist
touch /path/to/your/project/main.html
```

### 3. Save Work Regularly
When making changes:
1. Prepare your complete code/content
2. Write it to the fixed location
3. **VERIFY** the write was successful

### 4. Verification Steps (Critical!)
After writing, ALWAYS verify:
- ✅ File size matches expected (or is within reasonable range)
- ✅ Contains required opening tags (`<!DOCTYPE html>`, `<html>`, etc.)
- ✅ Contains required closing tags (`</html>`, `</body>`, `</script>`, etc.)
- ✅ Contains key functional components (event listeners, game loops, etc.)
- ✅ Can be read back correctly

### 5. Handling Write Failures
If verification fails:
1. Try writing again (sometimes transient issues occur)
2. Check available disk space/permissions
3. Try breaking write into smaller chunks
4. As fallback, use direct system commands:
   ```bash
   # Instead of relying solely on API tools
   echo "your content" > /path/to/file.html
   # OR
   cat > /path/to/file.html << 'EOF'
   your multi-line content
   EOF
   ```

### 6. Session Resumption
At start of each session:
1. Read from your fixed storage location
2. Verify file integrity
3. Continue from where you left off
4. If corrupted, restore from backup if available

## Verification Checklist for HTML/JS Games
When saving game code, verify:
- [ ] `<!DOCTYPE html>` present
- [ ] `<html>` tag with proper attributes
- [ ] `<head>` and `<body>` sections
- [ ] `<canvas id="gameCanvas">` (or your canvas ID)
- [ ] `<script>` tags wrapping JavaScript
- [ ] Proper closing tags: `</script>`, `</body>`, `</html>`
- [ ] Key functions: `init()`, `gameLoop()`, `update()`, `render()`
- [ ] Event listeners: `addEventListener('keydown'`, `addEventListener('keyup'`
- [ ] Animation loop: `requestAnimationFrame(gameLoop)`
- [ ] Game state object with lives/score/etc if applicable
- [ ] File ends cleanly (no truncation)

## Verification Checklist for General Code
- [ ] File opens with expected syntax (language-appropriate)
- [ ] All major functions/classes present
- [ ] No obvious syntax errors visible
- [ ] File closes properly
- [ ] Reasonable file size (not suspiciously small)

## Advanced: Backup Strategy
For critical work:
1. Save with timestamp: `project_v1.html`, `project_v2.html`
2. Or use simple rotation: `project.html.bak1`, `project.html.bak2`
3. Before major changes, copy current to backup

## Troubleshooting Common Issues

### "File appears truncated"
- Symptom: Missing closing tags, sudden end of content
- Cause: Write interruption, buffer issues
- Solution: 
  - Retry write
  - Check if using streaming write that needs flushing
  - Try writing smaller chunks
  - Verify available storage space

### "Content doesn't match what I wrote"
- Symptom: Read-back differs from source
- Cause: Encoding issues, accidental modification
- Solution:
  - Check encoding (UTF-8 standard)
  - Verify no intermediate processing altering content
  - Compare byte-for-byte if critical

### "Verification passes but code doesn't work"
- Symptom: File looks correct but fails at runtime
- Cause: Logic errors, missing dependencies
- Solution:
  - Verify in isolation (simple test case)
  - Check browser console for errors
  - Validate against known working examples

## Example Workflow for a Browser Game

### Session 1: Initial Creation
1. Create directory: `mkdir -p ~/hermes/games/myplatformer`
2. Create basic HTML structure with canvas
3. Write to: `~/hermes/games/myplatformer/index.html`
4. Verify: Check DOCTYPE, canvas, script tags, closing tags
5. Test locally: `python3 -m http.server 8000` → visit localhost:8000
6. Note any issues for next session

### Session 2: Resumption & Enhancement
1. Read: `cat ~/hermes/games/myplatformer/index.html`
2. Verify integrity
3. Add player movement logic
4. Write updated version to same location
5. Verify again (especially event listeners and game loop)
6. Test and note results

### Session 3: Feature Completion
1. Read existing code
2. Verify
3. Add enemies/collision detection
4. Write and verify
5. Test gameplay
6. Document any bugs for fixing

## Integration with Other Skills
- Use with `browser-game-creation` or `browser-platformer-game` for game-specific guidance
- Combine with `personal-goals-agent` to track development milestones
- Pair with `debugging-failed-technical-attempts` when issues arise
- Use `plan` skill to outline multi-session development strategy

## Safety Notes
- Never store sensitive information (passwords, keys) in plain text
- Consider encryption for highly sensitive work
- Regular backups prevent accidental loss
- Be mindful of file permissions in shared environments

## Why This Approach Works
By anchoring work to a fixed, verifiable location:
- Eliminates reliance on conversation history
- Provides tangible proof of progress
- Enables reliable session-to-session continuity
- Works regardless of Hermes context limits
- Creates a reusable artifact beyond the chat session