---
name: fix-js-syntax-with-line-artifacts
description: Repair JavaScript files corrupted with line-number prefixes or similar artifacts that cause syntax errors
version: 1.0.0
author: community
license: MIT
metadata:
  hermes:
    tags: [javascript, debugging, syntax-repair, file-repair]
---

# Fix JavaScript Syntax with Line Artifacts

Repairs JavaScript files that have been corrupted with line-number prefixes, timestamp markers, or similar artifacts that break syntax and cause runtime failures.

## When to Use

- JavaScript files show unexpected line-number prefixes like `   42|   42|actual code`
- Syntax errors occur despite visually correct code
- File was processed by tools that added metadata prefixes
- Specific patterns like empty lines in conditionals or misplaced operators
- After automated edits that inadvertently insert line markers

## Step-by-Step Process

### 1. Examine File Structure
```bash
# Look for prefix patterns
head -20 corrupted.js
# Look for lines like: "   42|   42|    const x = 5;"
```

### 2. Extract Clean Content
Remove everything before and including the last `|` character on each line:
```javascript
// Pseudocode for cleaning
cleaned_lines = []
for line in file_lines:
    if '|' in line:
        # Take everything after the last '|'
        clean_line = line.split('|').pop()
    else:
        clean_line = line
    cleaned_lines.append(clean_line)
```

### 3. Locate Problematic Region
Search for distinctive markers near the suspected error:
- Comments like `// Simple AABB collision`
- Function names or variable declarations
- Error stack traces indicating approximate location

### 4. Identify and Fix Syntax Issues
Common artifacts to fix:
- **Empty lines breaking statements**: Remove empty lines inside multi-line conditions
- **Leading operators**: Remove `&&` or `||` at start of continuation lines
- **Trailing operators**: Ensure operators are at end of lines, not beginning

Example fix:
```javascript
// BEFORE (broken)
if (condition1 &&
    [EMPTY LINE]
    && condition2) { ... }

// AFTER (fixed)
if (condition1 &&
    condition2) { ... }
```

### 5. Validate and Write Back
- Check that indentation remains consistent
- Verify all braces, parentheses, and semicolons are balanced
- Write cleaned content to file (overwriting original or creating backup)

## Example Repair Session

**Original corrupted file:**
```
    1|    1|<!DOCTYPE html>
    2|    2|<html>
    3|    3|<head>
   324|   324|                if (game.player.x < enemy.x + 30 &&
   325|   325|                    [EMPTY LINE]
   326|   326|                    && game.player.x + 30 > enemy.x 
   327|   327|                    && game.player.y < enemy.y + 30 
   328|   328|                    && game.player.y + 40 > enemy.y) {
```

**After cleaning:**
```javascript
<!DOCTYPE html>
<html>
<head>
// ... other lines ...
                if (game.player.x < enemy.x + 30 &&
                    game.player.x + 30 > enemy.x &&
                    game.player.y < enemy.y + 30 &&
                    game.player.y + 40 > enemy.y) {
// ... rest of code ...
```

## Verification

1. **Syntax check**: 
   ```bash
   node -c repaired.js  # Should return no errors
   ```

2. **Functional test**: 
   - Load in browser and verify the specific feature works
   - Check console for runtime errors

3. **Regression check**:
   - Ensure other functionality remains intact
   - Compare behavior against known good version

## Pitfalls to Avoid

- **Over-aggressive cleaning**: Don't remove pipes that are part of actual code (e.g., bitwise OR `|=`)
- **Incorrect line splitting**: Only split on `|` when it's part of the artifact pattern
- **Whitespace destruction**: Preserve indentation needed for readability (though JS doesn't require it)
- **Missing context**: Fixing one issue might reveal others; check entire function/block
- **Assuming single pattern**: Some files might have mixed artifacts; verify consistency

## Prevention Tips

- Use editors that don't automatically insert line numbers on copy/paste
- When using automation tools, verify output doesn't add unexpected metadata
- Implement pre-commit hooks to catch syntax errors early
- Consider using linters (ESLint) to automatically detect and fix many issues

## Related Skills

- `debugging-failed-technical-attempts`: General debugging methodology
- `systematic-debugging`: Root cause analysis for technical issues
- `js-linting-and-formatting`: Preventive code quality measures