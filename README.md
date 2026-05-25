
# Automated Firewall Threat Hunting Pipeline

## Project Overview
An automated Python pipeline leveraging the **Pandas** library to ingest, parse, and analyze raw JSON network firewall telemetry. The tool bypasses basic threshold indicators to isolate high-risk security incidents from background network noise.

## Threats Detected
* **Reconnaissance Identification:** Effectively mapped inbound brute-force/port-scanning behavior by aggregating and counting firewall `DENY` actions mapped to unique source IPs.

* **Data Exfiltration Flags:** Isolated unauthorized data egress vectors by filtering connection payloads exceeding high-volume thresholds (5MB+ bytes transferred).

## Technical Environment
* **OS:** Linux Ubuntu/Debian environment
* **Dependency Management:** Isolated Python virtual environments (`venv`)
* **Core Libraries:** Pandas, NumPy