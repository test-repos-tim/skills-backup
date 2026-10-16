---
name: debugging-failed-technical-attempts
description: A systematic approach to helping users who have attempted a technical task that didn't work as expected, especially when there might be misunderstandings about what was actually accomplished together.
---

# Debugging Failed Technical Attempts

## Overview
This skill provides a systematic approach to helping users who have attempted a technical task (like creating a game, building a website, etc.) that didn't work as expected, especially when there might be misunderstandings about what was actually accomplished together.

## When to Use
- User says "it didn't work" or "it went crazy" after attempting something technical
- User seems to believe we worked on something together that we actually didn't
- User is frustrated after a failed technical attempt
- Need to clarify what was actually done vs. what user remembers/expected

## Step-by-Step Approach

### 1. Clarify the Actual History
- **Listen carefully** to what the user says they tried
- **Review conversation history** to see what was actually discussed/worked on
- **Gently clarify discrepancies** without making user feel wrong
- **Example**: "I want to make sure I understand - are you referring to something we worked on together in this conversation, or something you tried elsewhere?"

### 2. Identify Common Failure Points
Once you understand what they attempted, identify typical issues:
- For JavaScript games: input handling, game loop issues, timing problems
- For websites: CSS/JS loading issues, DOM timing, browser compatibility
- For setup/config: missing dependencies, path issues, permission problems
- For logic errors: off-by-one errors, incorrect variable scope, race conditions

### 3. Provide Specific Debugging Guidance
Offer targeted advice based on the identified issue type:
- **JavaScript game input issues**:
  - Check if game loop is actually running (add console.log to loop)
  - Verify event listeners are attached after DOM is ready
  - Ensure element is focusable for keyboard events (add tabindex if needed)
  - Use window-level listeners instead of element-specific when appropriate
  - Check for JavaScript errors in console that might break event handling
  
- **General debugging approach**:
  - "What specific behavior did you expect vs. what happened?"
  - "Did you see any error messages in the browser console?"
  - "Can you share the exact code you were trying to run?"
  - "Let's try a minimal working example first..."

### 4. Provide Robust Starting Templates
When appropriate, offer a minimal, working example that addresses common pitfalls:
- Include proper initialization sequence
- Show correct event handling patterns
- Demonstrate basic game loop or update mechanism
- Include comments explaining why each part is necessary
- Make it easy to extend/customize

### 5. Verify Understanding
- Ask if the explanation makes sense
- Invite them to try the suggested approach
- Offer to help debug further if they share specific issues/code
- Keep tone supportive and collaborative

## Common JavaScript Game Pitfalls to Check

### Input Handling Issues
- Event listeners attached before DOMContentLoaded
- Using element-specific listeners instead of window/document
- Not preventing default behavior when needed
- Focus issues (element not focusable for keyboard events)
- Event bubbling/capturing confusion

### Game Loop Problems
- Missing requestAnimationFrame loop
- Incorrect timing/delta time calculations
- Blocking the main thread with heavy computations
- Not cleaning up animation frames when stopping

### State Management
- Variables not properly scoped
- State not updating as expected
- Race conditions between async operations
- Memory leaks from uncleared intervals/timeouts

## Example Response Template

When user says a technical attempt didn't work:

"I understand it's frustrating when something doesn't work as expected. Let me help clarify and troubleshoot.

First, to make sure we're on the same page: [clarify what was actually done vs. what they recall].

Common issues with [type of project] include:
- [Specific issue 1 with explanation]
- [Specific issue 2 with explanation]
- [Specific issue 3 with explanation]

Here's a minimal working example that avoids these common pitfalls:
[Provide clean, commented template]

Would you like to try this approach, or do you have specific error messages/code you'd like me to look at?"

## Pitfalls to Avoid
- Don't dismiss user's experience ("that's not what happened")
- Don't overwhelm with technical jargon
- Don't assume user knows basic debugging techniques
- Don't forget to validate their frustration before jumping to solutions
- Don't make assumptions without checking history/asking clarifying questions

## Verification
After providing guidance, ask:
- Does this match what you were experiencing?
- Does the suggested approach make sense to you?
- Would you like me to explain any part in more detail?
- Shall we try implementing this together step by step?

## Related Skills
- systematic-debugging: For more general debugging approaches
- spike: For throwaway experiments to validate ideas
- browser-game-creation: For specific game development guidance