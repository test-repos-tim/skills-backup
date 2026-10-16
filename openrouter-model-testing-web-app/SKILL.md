---
name: openrouter-model-testing-web-app
description: "Build MTWA interfaces with model dropdowns and CoT tracking."
version: 1.1
---
# MTWA Rules
- Load FREE models from `/api/models`; filter `:free`.
- Key file: `orapi.key`; status via `/api/status`; never expose full bearer.
- Chain-of-thought: extract `reasoning` + `reasoning_details`.
- Headers: mask `Authorization`; show `date`, `cf-ray`, `server-timing`.
- Multi-provider endpoints: OpenRouter/Anthropic/OpenAI/Gemini/Custom.

## Feature Overview

The **MTWA (Model Testing Web App)** provides a standalone, self-contained interface for querying OpenRouter models with full chain-of-thought visibility and responsive feedback.

### Architecture
- **Frontend**: Single-page app served at `http://localhost:7777/mtwa.html`
- **Backend**: Node.js server at `http://localhost:7777` (`openrouter-server.cjs`)
- **Data Sources**: Free models from OpenRouter (`/api/models` via DDG search for `:free` suffix), user-specified API keys
- **Key file**: `orapi.key` (OpenRouter key format: `sk-or-v1-...`)

### Components

#### 1. Top Bar (always visible)
- **Model Dropdown** (`#model-select`): Lists all 17 free OpenRouter models
- **API Key Selector** (`#api-key-select`): Switch between providers (OpenRouter, Anthropic, OpenAI, Gemini, Custom)
- **Save Key Button** (`Save Key`): Persists the API key to the server
- **Send Button** (`🚀 SEND QUERY`): Disabled until a model is selected

#### 2. Query Area
- **Query Input** (`#query_input`): Multiline textarea for the user query
- **Query Output** (`#query_output`): Displays the model response
- **Chain of Thought** (`#chain_of_thought`): Extracted reasoning from the model response
- **Headers Box** (`#headers`): Full response headers in a styled box

#### 3. Action Flow
1. User selects a model from the dropdown
2. User enters a query in the text area
3. Click **Send** → request POST to `/api/chat`
4. Server responds with `body.choices[0].message` (response) and `reasoning`/`reasoning_details` (chain of thought)
5. Results are displayed in the respective sections

### Implementation Details

#### Model Selection
- Models are fetched from `GET /api/models`
- Only models with `free` flag are shown
- Selected model is highlighted in the dropdown
- If no model is selected, the Send button is disabled

#### API Key Management
- API keys are stored in `appState.apiKey`
- Saved keys are shown in the status bar
- Invalid keys are rejected with an error message

#### Response Handling
- The server returns a JSON with `body` (message + choices) and `headers`
- **Reasoning** is taken from `message.reasoning`
- **Reasoning details** are concatenated from `message.reasoning_details` (fallback to `message.thought`)
- **Headers** are rendered in a styled box with color-coding

#### Error Handling
- Network errors → "❌ Failed: <error_message>"
- Empty query → "Enter a query"
- No model selected → "Select a model first"
- Server errors → "❌ Error: <error_message>"

### Usage Steps
1. Navigate to `http://localhost:3000/mtwa.html`
2. Choose a model from the top dropdown (e.g., `cohere/north-mini-code:free`)
3. Type a query in the text area
4. Click **🚀 SEND QUERY**
5. Wait for the response to appear in the output sections
6. View the **Chain of Thought** for reasoning transparency
7. Inspect the **Headers** box for full response metadata

### Configuration
- **API Key**: Place your OpenRouter API key in `orapi.key` (starts with `sk-or-`)
- **Server URL**: `http://localhost:3000` (hardcoded in the app)
- **Status Endpoint**: `GET /api/status` returns `apiKeyLoaded`, `selectedModel`, `modelCount`, etc.

### Pitfalls
- **Empty query**: The app waits for input before sending
- **No model selected**: The Send button stays disabled until a model is picked
- **Invalid API key**: The status bar shows "Failed" and the key is cleared
- **Rate limiting**: OpenRouter may throttle; consider adding delays between queries
- **Provider switching**: Changing the API key provider updates the dropdown and clears the selected model

### Quick Test
```bash
# Start the server (already running on localhost:3000)
# Open http://localhost:3000/mtwa.html
# Select a model (e.g., cohere/north-mini-code:free)
# Type a query and click SEND
```

## File Structure
- **Main UI**: `mtwa.html` (standalone, no build step required)
- **Server**: `openrouter-server.cjs` (Node.js, runs on port 3000)
- **Configuration**: `orapi.key` (API key file)
- **Status**: `appState` object tracks selected model, API key, request count

## Troubleshooting
- **Page not loading**: Ensure `orapi.key` exists and has a valid OpenRouter key
- **Send button not responding**: Check that a model is selected and the query is not empty
- **Headers box empty**: The server responded successfully; headers are included in the JSON response
- **Chain of thought missing**: The model may not have provided reasoning; check the `reasoning` field in the response

---
*Last updated: 2026-09-26*
*Source: openrouter API / MTWA implementation*
