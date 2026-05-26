# Arvin's Python Projects Workspace

Welcome to my repository showcasing Python tools built for data processing and log analytics.

## 📁 Projects Index
1. **[Network Traffic Analytics](#1-network-traffic-analytics)** - An automated data-enrichment and risk-profiling pipeline for network security logs.

---

## 1. Network Traffic Analytics
* **File:** `sec_projects/net_analysis.py`
* **Description:** A pandas-driven security analytics engine designed to ingest raw transactional network logs, isolate anomalous indicators, and prioritize high-risk connections using multi-tiered logical conditions.

### 🚀 Key Technical Features:
* **Log Enrichment:** Dynamically calculates localized tracking arrays, separating internal assets from external infrastructure vectors and automatically mapping throughput volumes into comparative classifications (`large` vs. `small`).
* **Compound Threat Risk Profiling:** Pairs security exceptions with structural country codes to instantly triage alerts, filtering high-threat anomalies by data-exfiltration weights.
* **Asset Behavioral Aggregation:** Leverages deep group-by matrices to cross-examine individual source IPs, creating operational baselines for internal assets based on asymmetric traffic sizes and historic alert volumes.

### How to Run:
```bash
python3 sec_projects/net_analysis.py