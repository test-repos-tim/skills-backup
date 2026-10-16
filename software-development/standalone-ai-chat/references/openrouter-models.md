# OpenRouter Free Model Filtering

## Pattern
- Fetch from `https://openrouter.ai/api/v1/models`
- Filter: `model.id.includes(':free')`
- Never hardcode model names; always fetch live
- User's web-login (`timv80408@gmail.com`) is separate from API auth

## Chain of Thought Extraction
- Check `message.reasoning` (primary reasoning text)
- Check `message.reasoning_details` (array with `.text` fields for structured reasoning)
- Check `message.thought` (alternative field name)
- Combine all available fields; never assume one name