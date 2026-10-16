---
name: shodan-integration
description: Natural language interface for Shodan CLI OSINT tool
version: 1.0.0
author: Hermes Agent
---

# Shodan CLI Natural Language Interface

Provides mapping from natural language requests to Shodan CLI commands for OSINT gathering.

## Prerequisites
- Shodan CLI installed and configured with API key
- Run `shodan init YOUR_API_KEY` to configure if not already done

## Command Mappings

### Account Queries
- "Show my Shodan account info" → `shodan info`
- "Check my Shodan credits" → `shodan info`

### Host/IP Lookup
- "Get info on IP address [address]" → `shodan host [address]`
- "What does Shodan know about [IP]?" → `shodan host [IP]`
- "Look up host [address]" → `shodan host [address]`

### Search Operations
- "Search for [term]" → `shodan search [term]`
- "Find [product] on port [number]" → `shodan search port:[number] [product]`
- "Search for webcams in [location]" → `shodan search [term] --country [code] --city [name]`
- "Search with filter [filter]" → `shodan search [term] [filter]`

### Domain Queries
- "Get domain info for [domain]" → `shodan domain [domain]`
- "Show Shodan data for [domain]" → `shodan domain [domain]`

### Utility Commands
- "What is my external IP?" → `shodan myip`
- "Show Shodan version" → `shodan version`

### Bulk Operations
- "Download results for [query]" → `shodan download --limit [number] [query] [filename]`
- "Parse Shodan download file" → `shodan parse --fields [fields] [file]`

## Common Search Filters
- Country: `country:"US"`
- City: `city:"London"`
- Organization: `org:"Google"`
- Hostname: `hostname:"example.com"`
- Port: `port:80`
- OS: `os:"Windows"`
- Product: `product:"Apache"`

## Examples
- "Show my account info" → `shodan info`
- "Tell me about 8.8.8.8" → `shodan host 8.8.8.8`
- "Search for MongoDB on port 27017" → `shodan search port:27017 mongodb`
- "Find webcams in Germany" → `shodan search webcam --country DE`
- "Get info for example.com" → `shodan domain example.com`
- "What's my public IP?" → `shodan myip`

## Notes
- Free tier limits: 1 query/second, 50 results/search
- Use `--limit [num]` to increase results (up to 1000 for free tier)
- For more than 1000 results, use `shodan download` with pagination
- Only use on targets you have authorization to test

## Limited Tier Workarounds
When the `vuln:*` filter is unavailable (requires Academic/Small Business tier or higher), you can:
1. Search for specific smart-home/IoT products: `shodan search "product name"`
2. Extract IP addresses from results (e.g., `cut -f1`)
3. Check each host individually for vulnerability details: `shodan host <IP> | grep -i "Vulnerabilities:"`
4. Use external CVE databases (like NVD) to assess severity of reported CVEs.