# Arvin's Cybersecurity Data Science Portfolio

A growing collection of data analysis and cybersecurity projects built using Python.
This repository documents my journey toward becoming a Cybersecurity Data Scientist,
with projects developed alongside my Data Analytics training on DataCamp.

---

## 📁 Repository Structure

```
portfolio-projects-vin/
│
├── portfolio/                        # Polished project notebooks
│   ├── 01_network_log_analysis/
│   │   ├── network_log_analysis.ipynb
│   │   └── data/
│   │       └── network_logs.csv
│   └── ... (more projects coming)
│
├── README.md
└── requirements.txt
```

---

## 📊 Projects

### 1. Network Intrusion Log Analysis
> Exploratory data analysis of synthetic network logs using pandas — built to practice security-focused data analysis.

| | |
|---|---|
| **Notebook** | `portfolio/network_log_analysis.ipynb` |
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

## 🗺️ Roadmap

| # | Project | Status |
|---|---|---|
| 01 | Network Intrusion Log Analysis | ✅ Complete |
| 02 | Intrusion Detection EDA (NSL-KDD dataset) | 🔜 Upcoming |
| 03 | Malware Traffic Classification | 🔜 Upcoming |
| 04 | Threat Intelligence Analysis | 🔜 Upcoming |

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

3. Launch the notebook
   ```bash
   jupyter notebook portfolio/network_log_analysis.ipynb
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
```