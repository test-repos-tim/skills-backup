---
name: infomaniak_recon_workflow
description: Low‑traffic reconnaissance for Infomaniak bug‑bounty scope (sub‑domain enumeration, HTTP probing, URL collection, limited directory fuzzing, Nuclei scan).
---
# Prerequisites
- Kali/Ubuntu with: sublist3r, assetfinder, findomain, amass, httpx, gau, katana, ffuf, nuclei (plus optional masscan).
- Set User‑Agent: "Infomaniak-YWH-Bugbounty".

# Steps
1. Work dir:
   ```sh
   mkdir -p ~/infomaniak-bounty && cd ~/infomaniak-bounty
   ```
2. Passive sub‑domain enumeration:
   ```sh
   sublist3r -d infomaniak.com -o sublist3r.txt -t 30
   assetfinder --subs infomaniak.com > assetfinder.txt
   findomain -t infomaniak.com -u findomain.txt
   amass enum -d infomaniak.com -passive -config /dev/null -o amass.txt
   cat sublist3r.txt assetfinder.txt findomain.txt amass.txt | sort -u > all_subdomains.txt
   ```
3. HTTP/HTTPS probing (rate‑limited):
   ```sh
   cat all_subdomains.txt | httpx -silent -title -tech-detect -status-code \
       -rate-limit 150 -timeout 10s -user-agent "Infomaniak-YWH-Bugbounty" \
       -json -output httpx_results.json
   ```
4. Historic URL collection & spidering:
   ```sh
   cat all_subdomains.txt | gau --providers wayback,commoncrawl,otx,urlscan \
       --include-subdomains \
       --blacklist "png,jpg,gif,svg,css,ico,woff,woff2,ttf,mp4,flv,webm" -o gau.txt
   cat all_subdomains.txt | katana -silent -rate-limit 30 -depth 3 -output katana.txt
   cat gau.txt katana.txt | sort -u > urls.txt
   ```
5. Low‑rate directory brute‑force (example target from `targets.txt`):
   ```sh
   TARGET=$(head -n1 targets.txt)
   ffuf -w /usr/share/wordlists/dirb/common.txt -u https://$TARGET/FUZZ \
        -mc 200,204,301,302,307,401,403 -rate 50 -t 20 \
        -recursion -e .php,.html,.js,.json,.txt -o ffuf_results.json
   ```
6. Targeted Nuclei scan (focus tags, rate‑limited):
   ```sh
   cat urls.txt | grep "^https" > nuclei_targets.txt
   nuclei -l nuclei_targets.txt -rate-limit 150 \
          -tags xss,sqli,ssrf,auth-bypass,bizlogic,rce,lfi,csrf \
          -user-agent "Infomaniak-YWH-Bugbounty" -timeout 10s \
          -output nuclei_results.txt
   ```
7. (Optional) Light port sweep on discovered IPs using masscan, respecting low rate.
8. For any positive finding, capture PoC with `curl` (same User‑Agent) and optionally screenshot via `wkhtmltoimage`.

# Post‑processing
- Review `httpx_results.json` for interesting tech stacks.
- Analyse `ffuf_results.json` and `nuclei_results.txt` for XSS, SSRF, IDOR, auth‑bypass, etc.
- Store PoCs under `pocs/` and draft a report per Infomaniak guidelines.
