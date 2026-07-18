# Arvin's Cybersecurity Data Science Portfolio

A growing collection of data analysis and cybersecurity projects built using Python.
This repository documents my journey toward becoming a Cybersecurity Data Scientist,
with projects developed alongside my Data Analytics training on DataCamp.

---

## 📁 Repository Structure

```
portfolio-projects-vin/
│
├── portfolio/
|   ├── Phase_1/
|   |   ├── 01_network_log_analysis/
|   |   |   ├── network_log_analysis.ipynb
|   |   |   └── data/
|   |   |        └── network_logs.csv
|   |   |
|   |   ├── 02_ip_watchlist_manager/
|   |   |   └── ip_watchlist_manager.py
|   |   |
|   |   ├── 03_threat_record_manager/
|   |   |    ├── threat_record_manager.ipynb
|   |   |    └── threat_record_manager.py
|   |   |
|   |   ├── 04_daily_ip_alert_comparator/
|   |   |   ├── daily_ip_alert_comparator.py
|   |   |   ├── daily_ip_alert_comparator.ipynb
|   |   |   └── logs.json
|   |   |
|   |   ├── 05_meridian_login_analysis/
|   |   |   ├── meridian_login_analysis.py
|   |   |   ├── meridian_login_analysis.ipynb
|   |   |   ├── meridian_logs.csv
|   |   |   ├── soc_triage_report.html
|   |   |   ├── soc_triage_report.txt
|   |   |   └── suspicious_findings.csv
|   |   |
|   |   ├── milestone_project/
|   |   |   ├── milestone_project.py
|   |   |   ├── milestone_project.ipynb
|   |   |   ├── messy_logins.csv
|   |   |   ├── clean_logins.csv
|   |   |   └── data_quality_report.txt
|   |   |
|   |   └── 07_firewall_log_triage/
|   |       └── firewall_logs_raw.txt
|   |
|   └── Phase_2/
|       └── 08_endpoint_health_monitoring/
|           └── endpoint_health_raw.csv
| 
├── README.md
└── requirements.txt
```

---

## 📊 Projects

### 1. Network Intrusion Log Analysis
> Exploratory data analysis of synthetic network logs using pandas — built to practice security-focused data analysis.

| | |
|---|---|
| **Notebook** | `portfolio/Phase_1/01_network_log_analysis/network_log_analysis.ipynb` |
| **Dataset** | Synthetic network log (20 events, 8 features) |
| **Tools** | Python, pandas, numpy, Jupyter |

**What this project covers:**
- Inspecting and summarizing a network log dataset
- Flagging suspicious traffic using new computed columns
- Classifying events by traffic size and risk level using `np.where()`
- Filtering and sorting high-risk connections
- Aggregating traffic patterns by source IP, protocol, and country
- Targeted row and column selection using `.loc` and `.iloc`

**Key Findings:**
- 7 out of 20 events triggered security alerts, all involving external destinations
- `10.0.0.5` and `10.0.0.99` were the highest-alert source IPs
- All high-risk events involved traffic routed to Russia (`RU`) with large payloads
- TCP traffic consistently produced the largest data transfers
- DNS was the most frequent protocol but carried significantly smaller payloads

---

### 2. IP Watchlist Manager
> A command-line IP watchlist manager built using Python lists and control flow — simulating a basic SOC analyst tool.

| | |
|---|---|
| **File** | `portfolio/Phase_1/02_ip_watchlist_manager/ip_watchlist_manager.py` |
| **Tools** | Python, lists, loops, conditionals, error handling |

**What this project covers:**
- Interactive CLI menu using `while True` loop
- Smart add/remove logic based on IP presence
- Replace existing IPs using `.index()`
- Input validation and error handling throughout

**What I learned:**
- If your script has options that were coded with `if-elif-else` conditions, always `if` on the first option and `elif` on subsequents.

**What I could've added:**
- I know there's a function to make the screen change for every option and not print them out everytime the loop resets but, I don't know how to do it and won't be adding it for the sake of a progress-driven portfolio.
- I also noticed options 2 and 3 don't have a block for incorrect input value. For example, option 2 would ask you to enter an IP and would still continue even if you entered a text or other value than an IP. I'll consider this on future projects.

---

### 3. Threat Record Manager
> A CLI threat intelligence record manager simulating SOC analyst workflows — built using Python dictionaries and control flow.

| | |
|---|---|
| **Script** | `portfolio/Phase_1/03_threat_record_manager/threat_record_manager.py` |
| **Notebook** | `portfolio/Phase_1/03_threat_record_manager/threat_record_manager.ipynb` |
| **Tools** | Python, dictionaries, os module, loops, error handling |

**What this project covers:**
- Full CRUD operations on a Python dictionary
- Smart update flow — change value, rename key, or both independently
- Input validation and cancel-at-any-step UX with 'q'
- Cross-platform terminal screen control using the os module
- Documented evolution from initial build to final version in the notebook

**What I added:**
- Implemented `clear_screen()` using the `os` module in Project 3 to solve this exact problem.
- Added blocks for incorrect input values on all options.

---

### 4. Daily IP Alert Comparator
> A CLI threat intelligence tool that compares network logs between two days to surface new, persistent, and resolved threats — built using Python sets, JSON, and the rich library for formatted output.

| | |
|---|---|
| **Script** | `portfolio/Phase_1/04_daily_ip_alert_comparator/daily_ip_alert_comparator.py` |
| **Notebook** | `portfolio/Phase_1/04_daily_ip_alert_comparator/daily_ip_alert_comparator.ipynb` |
| **Data** | `portfolio/Phase_1/04_daily_ip_alert_comparator/logs.json` |
| **Tools** | Python, sets, tuples, JSON, rich, os module |

**What this project covers:**
- Loading and parsing threat data from a JSON file
- Set operations to identify new, persistent, resolved, and combined threats
- Three-tier alert threshold system using tuple unpacking
- Color-coded terminal output using the `rich` library
- Cross-platform screen clearing using the `os` module

**Key Output:**
- 🔴 New Alerts — IPs seen today but not yesterday
- 🟡 Persistent Threats — IPs seen on both days
- 🟢 Resolved Threats — IPs seen yesterday but not today
- Total unique IPs tracked across both days

**What I could've added:**
- **Error Handling (`try/except`)** — catching missing or corrupted `logs.json` files so the script doesn't crash unexpectedly
- **Exporting Reports** — saving the rich table output to `.txt` or `.html` so analysts can share results via email
- **Historical Logging** — appending daily results to a master log file to track threat trends over a 30-day period instead of just 48 hours

---

### 5. Meridian Login Analysis — SOC Triage
> A Python-based threat intelligence tool that parses login events, filters out baseline security noise, and dynamically profiles brute-force attacks to generate dark-mode HTML triage dashboards.

| | |
|---|---|
| **Script** | `portfolio/Phase_1/05_meridian_login_analysis/soc_triage_report.py` |
| **Notebook** | `portfolio/Phase_1/05_meridian_login_analysis/meridian_login_analysis.ipynb` |
| **Tools** | Python, CSV module, Dictionaries, Sets, Rich library |

**What this project covers:**
- Safe file stream handling using Python context managers (`with open()`)
- In-memory data structures (Dictionaries and Unique Set sets) to aggregate threat metadata
- Conditional logic gates to establish attack volume thresholds (`ALERT_THRESHOLD = 5`)
- Dynamic threat profiling to classify attacks as either *Isolated* or *Distributed* based on unique IP footprints
- Building an automated UI reporting pipeline that outputs color-coded terminal tables, plain-text backups, and dark-mode dashboards simultaneously

**Key Analysis Output:**
- **Top Targeted Accounts Table:** Tracks and highlights the most heavily targeted usernames.
- **Top Attacking IP Addresses Table:** Maps malicious host origins based on failed login volumes.
- **Top Targeted Systems / Assets Table:** Visualizes corporate target vectors.
- **Dynamic Forensic Audit Alert:** Instantly surfaces malicious footprints targeting critical infrastructure accounts (e.g., `admin`).

---

### 6. Milestone Project: Login Data Quality Cleaner
> A batch Python script that reads a messy raw login export, flags rows with data quality problems, writes a clean CSV, and generates a data quality report for both terminal and file output.

| | |
|---|---|
| **Script** | `portfolio/Phase_1/milestone_project/milestone_project.py` |
| **Notebook** | `portfolio/Phase_1/milestone_project/milestone_project.ipynb` |
| **Data** | `portfolio/Phase_1/milestone_project/messy_logins.csv` |
| **Tools** | Python, csv module, datetime, rich |

**What this project covers:**
- Custom validation for IP addresses, timestamps, and status values, with no external regex or validation libraries
- Duplicate detection using a rounded-timestamp key stored in a set, matching the same user and IP within a 1-minute window
- Accepts multiple real-world timestamp formats in the same input file (standard, slash-date, and ISO with a Z suffix)
- A normalize-and-write-back pattern: fields are cleaned for validation and the cleaned form is written back into the row before saving, so the output CSV is consistently formatted rather than just individually valid
- A data quality report that counts each flagged row once overall, while still tracking how many rows fall into each issue type
- Documented bug evolution in the notebook: a misspelled keyword argument, then three separate normalization gaps found by inspecting the actual output file rather than the code

**Key Findings:**
- 5 clean rows and 3 flagged rows out of 8 total, from a real messy login export
- Flags broke down as 2 rows for missing fields (one blank IP, one blank timestamp) and 1 row for an unrecognized status value
- No rows flagged for invalid IP, invalid timestamp, or duplicate login in this run, all three accepted timestamp formats parsed successfully, and the one repeated user and IP pair in the file fell outside the 1-minute duplicate window

---

## 🗺️ Roadmap

| # | Project | Status |
|---|---|---|
| 01 | Network Intrusion Log Analysis | ✅ Complete |
| 02 | IP Watchlist Manager | ✅ Complete |
| 03 | Threat Record Manager | ✅ Complete |
| 04 | Daily IP Alert Comparator | ✅ Complete |
| 05 | Meridian Login Analysis — SOC Triage | ✅ Complete |
| 06 | Milestone Project | ✅ Complete |
| 07 | Firewall Log Triage (Regex) | ✅ Complete |
| 08 | Endpoint Health Monitoring (NumPy/pandas, missing values, visualization) | 🔄 In progress |
| 09 | Intrusion Detection EDA (NSL-KDD dataset) | 🔜 Upcoming |

---

## ⚙️ How to Run

1. Clone the repository
```bash
   git clone https://github.com/cangmaongarvin-wq/portfolio-projects-vin.git
   cd portfolio-projects-vin
```

2. Install dependencies
```bash
   pip install -r requirements.txt
```

3. Launch the network log analysis notebook
```bash
   jupyter notebook portfolio/Phase_1/01_network_log_analysis/network_log_analysis.ipynb
```

4. Run the IP watchlist manager
```bash
   python3 portfolio/Phase_1/02_ip_watchlist_manager/ip_watchlist_manager.py
```

5. Launch the threat record manager notebook
```bash
   jupyter notebook portfolio/Phase_1/03_threat_record_manager/threat_record_manager.ipynb
```
   Once the notebook opens:
   1. Click the "Run" menu at the top
   2. Select "Render All Markdown Cells"
      
   > **Note:** This notebook contains interactive CLI code using `input()` which cannot run inside Jupyter. Rendering markdown cells only displays the documentation without executing the code.

6. Run the Threat Record Manager
```bash
   python3 portfolio/Phase_1/03_threat_record_manager/threat_record_manager.py
```

7. Launch the Daily IP Alert Comparator notebook
```bash
   jupyter notebook portfolio/Phase_1/04_daily_IP_alert_comparator/daily_ip_alert_comparator.ipynb
```

8. Run the Daily IP Alert Comparator
```bash
   python3 portfolio/Phase_1/04_daily_ip_alert_comparator/daily_ip_alert_comparator.py
```

9. Launch the Meridian Login Analysis notebook
```bash
   jupyter notebook portfolio/Phase_1/05_meridian_login_analysis/meridian_login_analysis.ipynb
```
10. Run the Meridian Login Analysis
```bash
   python3 portfolio/Phase_1/05_meridian_login_analysis/meridian_login_analysis.py
```

11. Launch the Milestone Project notebook
```bash
   jupyter notebook portfolio/Phase_1/milestone_project/milestone_project.ipynb
```

12. Run the Milestone Project
```bash
   python3 portfolio/Phase_1/milestone_project/milestone_project.py
```
   > **Note:** Run this one from the repository root so the relative file paths inside the script resolve correctly.
---

## 📦 Requirements

```
# Core dependencies
numpy==2.4.6
pandas==3.0.3
rich==15.0.0

# Jupyter
jupyter==1.1.1
jupyterlab==4.5.7
jupyter-console==6.6.3
jupyter_client==8.8.0
jupyter_core==5.9.1
jupyter_server==2.18.2

# Python version: 3.12.3
```
---

## 👤 About

**Arvin Cangmaong**
Aspiring Cybersecurity Data Scientist | Currently training in Python Data Analytics via DataCamp

[GitHub](https://github.com/cangmaongarvin-wq) · [LinkedIn](https://www.linkedin.com/in/acangmaong/)