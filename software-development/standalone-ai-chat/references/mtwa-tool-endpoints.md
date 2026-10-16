# MTWA Tool Endpoints Specification

## Overview
MTWA (Model Testing Web Application) extends the standalone AI chat interface with server-side tool endpoints. All tools execute server-side; the browser only calls them via `fetch()`.

## Endpoint Table

| Endpoint | Method | Query/Body | Description |
|----------|--------|-----------|-------------|
| `/api/web-search` | GET | `?q=search+term` | Fetch current info via OpenRouter model |
| `/api/web-extract` | GET | `?url=https://...` | Extract text content from URL |
| `/api/file-read` | GET | `?path=/path/to/file` | Read local file as text |
| `/api/file-write` | POST | `{"path":"...","content":"..."}` | Write content to file |
| `/api/terminal` | POST | `{"command":"ls -la"}` | Execute shell command (30s timeout) |
| `/api/memory` | POST | `{"action":"get","key":"..."}` or `{"action":"set","key":"...","value":"..."}` | Persistent key-value store |

## Implementation Pattern

### Web Search
```javascript
if (pathname === '/api/web-search') {
  const q = url.searchParams.get('q');
  const result = await makeWebSearch(q);
  res.writeHead(200, {'Content-Type': 'application/json'});
  res.end(JSON.stringify(result));
}

async function makeWebSearch(query) {
  // Use OpenRouter model to search web
  const options = {
    hostname: 'openrouter.ai',
    path: '/api/v1/chat/completions',
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${appState.apiKey}`,
      'Content-Type': 'application/json'
    }
  };
  const payload = JSON.stringify({
    model: 'anthropic/claude-opus-4.8',
    messages: [{role: 'user', content: `Search the web for: ${query}. Return only the key findings.`}],
    max_tokens: 500
  });
  const result = await makeHttpsRequest(options, payload);
  return JSON.parse(result.body);
}
```

### File Read/Write
```javascript
// Read
if (pathname === '/api/file-read') {
  const p = url.searchParams.get('path');
  const content = fs.readFileSync(p, 'utf8');
  res.writeHead(200, {'Content-Type': 'application/json'});
  res.end(JSON.stringify({content}));
}

// Write
if (pathname === '/api/file-write') {
  let body = '';
  req.on('data', chunk => body += chunk);
  req.on('end', () => {
    const {path, content} = JSON.parse(body);
    fs.writeFileSync(path, content);
    res.writeHead(200, {'Content-Type': 'application/json'});
    res.end(JSON.stringify({success: true}));
  });
}
```

### Terminal
```javascript
if (pathname === '/api/terminal') {
  let body = '';
  req.on('data', chunk => body += chunk);
  req.on('end', async () => {
    const {command} = JSON.parse(body);
    const {exec} = require('child_process');
    const result = await new Promise((resolve, reject) => {
      exec(command, {timeout: 30000}, (err, stdout, stderr) => {
        if (err) reject(err); else resolve({stdout, stderr});
      });
    });
    res.writeHead(200, {'Content-Type': 'application/json'});
    res.end(JSON.stringify(result));
  });
}
```

### Memory
```javascript
if (pathname === '/api/memory') {
  let body = '';
  req.on('data', chunk => body += chunk);
  req.on('end', () => {
    const {action, key, value} = JSON.parse(body);
    const memFile = path.join(__dirname, '.mtwa-memory.json');
    let memory = {};
    try { memory = JSON.parse(fs.readFileSync(memFile, 'utf8')); } catch(e) { memory = {}; }
    if (action === 'get') {
      res.writeHead(200, {'Content-Type': 'application/json'});
      res.end(JSON.stringify({value: memory[key] || null}));
    } else if (action === 'set') {
      memory[key] = value;
      fs.writeFileSync(memFile, JSON.stringify(memory, null, 2));
      res.writeHead(200, {'Content-Type': 'application/json'});
      res.end(JSON.stringify({success: true}));
    }
  });
}
```

## Browser-Side Usage
```javascript
// Call any endpoint from browser
async function callMTWA(tool, params) {
  const url = tool === 'web-search' ? `/api/web-search?q=${encodeURIComponent(params)}`
            : tool === 'web-extract' ? `/api/web-extract?url=${encodeURIComponent(params)}`
            : tool === 'file-read' ? `/api/file-read?path=${encodeURIComponent(params)}`
            : `/api/${tool}`; // POST endpoints
  
  const response = await fetch(url, {
    method: tool === 'file-write' || tool === 'terminal' || tool === 'memory' ? 'POST' : 'GET',
    headers: {'Content-Type': 'application/json'},
    body: tool !== 'web-search' && tool !== 'web-extract' && tool !== 'file-read' ? JSON.stringify(params) : undefined
  });
  
  return await response.json();
}
```

## Security Notes
- Terminal and file write endpoints are powerful; restrict in production
- File paths should be validated to prevent path traversal
- Terminal commands should be sandboxed or restricted
- Memory store is file-based; consider encryption for sensitive data
