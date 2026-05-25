# Arvin's Python Projects Workspace

Welcome to my repository showcasing Python tools built for data processing, log analytics, and systems emulation.

## 📁 Projects Index
1. **[Threat Hunting Pipeline](#1-threat-hunting-pipeline)** - Parsers for network traffic logs to flag malicious indicators.
2. **[VESPA Mock Booking Tool](#2-vespa-mock-booking-tool)** - A stateful global distribution system (GDS) emulator designed for terminal workflow familiarization.

---

## 1. Threat Hunting Pipeline
* **File:** `sec_scripts/threat_hunt.py`
* **Description:** Automates the ingestion of network traffic logs to detect unauthorized connection attempts or data exfiltration markers.

### How to Run:
```bash
python3 sec_scripts/threat_hunt.py

---

## 2. VESPA Mock Booking Tool
* **File:** `projects_py/vespa.py`
* **Description:** A stateful, terminal-based reservation emulator inspired by corporate Global Distribution Systems (GDS). It mirrors professional reservation environments by implementing transactional state management and realistic data flows.

### 🚀 Key Technical Features:
* **Stateful Session Buffering:** Implements a localized memory workspace utilizing deep-copy tracking (`copy.deepcopy`). Modifications are kept in an uncommitted staging buffer until explicitly committed using transactional logic (`.io`).
* **Robust Error & Flow Control:** Built-in safeguards preventing standard program crashes from unexpected terminal user breaks (`KeyboardInterrupt` intercepts). Features immediate data verification routines to reject invalid input IDs instantly.
* **Corporate Logic & Restrictive Workflows:** Enforces multi-tier constraint rules, such as structural control blocks that automatically freeze data updates on accounts with outstanding balances (`svc_indicator == "1"`).
* **Financial Ledger Computations:** Features real-time parameter checking for custom terminal scripts, including aggregate loop-checks that limit local refund allocations to dynamic ceilings (e.g., maximum GBP 50.00).

### How to Run:
```bash
python3 projects_py/vespa.py