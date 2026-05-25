# Arvin's Security & Automation Workspace

Welcome to my repository showcasing Python tools built for security analytics, threat hunting, and log parsing.

## 📁 Projects Index
1. **[Threat Hunting Pipeline](#1-threat-hunting-pipeline)** - Parsers for network traffic logs to flag malicious indicators.

2. **[VESPA Mock Booking Tool]
(#2-vespa-mock-booking-tool)** - A stateful global distribution system (GDS) emulator designed for terminal workflow familiarization.

---

## 1. Threat Hunting Pipeline
* **File:** `sec_scripts/threat_hunt.py`
* **Description:** Automates the ingestion of `network_logs.json` to detect unauthorized connection attempts or data exfiltration markers.

### How to Run:
```bash
python3 sec_scripts/threat_hunt.py

## 2. Vespa Mock Booking Tool
* **File:** `projects_py/vespa.py`
* **Description:** An advanced terminal emulator mimicking corporate passenger reservation tools. It tracks changes in an isolated session memory buffer, enforces business logic checks (like blocking unpaid updates or limiting cash refunds), and processes transactional commits (.io)

### How to Run:
```bash
python3 projects_py/vespa.py