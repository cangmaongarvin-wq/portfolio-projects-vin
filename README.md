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
|   ├── 01_network_log_analysis/
│   |   ├── network_log_analysis.ipynb
│   |   └── data/
│   |        └── network_logs.csv
|   |
|   ├── 02_ip_watchlist_manager/
|   |   └── ip_watchlist_manager.py
|   |
|   └── 03_threat_record_manager/
|       ├── threat_record_manager.ipynb
|       └── threat_record_manager.py
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
| **Notebook** | `portfolio/01_network_log_analysis/network_log_analysis.ipynb` |
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
| **File** | `portfolio/02_ip_watchlist_manager/ip_watchlist_manager.py` |
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
| **Script** | `portfolio/03_threat_record_manager/threat_record_manager.py` |
| **Notebook** | `portfolio/03_threat_record_manager/threat_record_manager.ipynb` |
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

## 🗺️ Roadmap

| # | Project | Status |
|---|---|---|
| 01 | Network Intrusion Log Analysis | ✅ Complete |
| 02 | IP Watchlist Manager | ✅ Complete |
| 03 | Threat Record Manager | ✅ Complete |
| 04 | Intrusion Detection EDA (NSL-KDD dataset) | 🔜 Upcoming |
| 05 | Malware Traffic Classification | 🔜 Upcoming |
| 06 | Threat Intelligence Analysis | 🔜 Upcoming |

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
   jupyter notebook portfolio/01_network_log_analysis/network_log_analysis.ipynb
```

4. Run the IP watchlist manager
```bash
   python3 portfolio/02_ip_watchlist_manager/ip_watchlist_manager.py
```

5. Launch the threat record manager notebook
```bash
   jupyter notebook portfolio/03_threat_record_manager/threat_record_manager.ipynb
```
   Once the notebook opens:
   1. Click the "Run" menu at the top
   2. Select "Render All Markdown Cells"
      
   > **Note:** This notebook contains interactive CLI code using `input()` which cannot run inside Jupyter. Rendering markdown cells only displays the documentation without executing the code.

6. Run the Threat Record Manager
```bash
   python3 portfolio/03_threat_record_manager/threat_record_manager.py
```

---

## 📦 Requirements

```
pandas
numpy
jupyter
```

---

## 👤 About

**Arvin**
Aspiring Cybersecurity Data Scientist | Currently training in Python Data Analytics via DataCamp

[GitHub](https://github.com/cangmaongarvin-wq) · [LinkedIn](https://www.linkedin.com/in/acangmaong/)