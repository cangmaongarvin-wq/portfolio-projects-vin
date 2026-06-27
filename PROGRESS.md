# Progress Tracker

> A living snapshot of where this portfolio stands — written so any AI tool 
> (or human reviewer) can pick up context quickly without needing the full 
> conversation history.

Last updated: by Arvin, ongoing

---

## 🗺️ Roadmap Status — Cybersecurity Data Scientist Path

### Phase 1 — Python Essentials
| Topic | Status |
|---|---|
| Syntax & Logic (loops, conditionals, try/except) | ✅ Complete |
| Data Structures — Lists | ✅ Complete |
| Data Structures — Dictionaries | ✅ Complete |
| Data Structures — Tuples & Sets | ✅ Complete |
| File I/O (text, CSV, JSON) | ✅ Complete |
| Regex | ⬜ Not formally covered — being introduced naturally through SOC simulations |
| Milestone Project | 🔄 In progress |

### Phase 2 — Data Manipulation Libraries
| Topic | Status |
|---|---|
| NumPy | 🔄 Touched briefly in Project 1 |
| Pandas | ✅ Covered in Project 1 (filtering, sorting, groupby, agg, loc/iloc) |
| Missing Value Handling | ⬜ Not yet covered |
| Data Visualization (Matplotlib/Seaborn) | ⬜ Not yet covered |

### Phase 3 — SQL & Structured Data
⬜ Not started

### Phase 4 — Applied Mathematics & Statistics
⬜ Not started

### Phase 5 — Machine Learning for Security
⬜ Not started

### Phase 6 — Cybersecurity Domain Knowledge
🔄 Picked up informally through SOC analyst simulation exercises (see below)

---

## 📁 Portfolio Projects (GitHub: portfolio-projects-vin)

| # | Project | Skills | Status |
|---|---|---|---|
| 01 | Network Log Analysis | pandas, numpy, EDA | ✅ Complete |
| 02 | IP Watchlist Manager | lists, CLI, control flow | ✅ Complete |
| 03 | Threat Record Manager | dictionaries, CRUD, os module | ✅ Complete |
| 04 | Daily IP Alert Comparator | sets, tuples, JSON, rich library | ✅ Complete |
| 05 | Meridian Login Analysis | File I/O, CSV, SOC simulation, rich | ✅ Complete |
| 06 | Milestone Project (messy CSV cleanup) | File I/O, data cleaning | 🔄 In progress |

---

## 🧠 Coding Patterns & Preferences

These are habits established across all projects — keep consistent:

- **File handling:** Always use `with open()`, never bare `open()`
- **Dictionary lookups:** Use `.get(key, default)` to avoid `KeyError`
- **Menus:** Use `if/elif/else` chains for mutually exclusive options — never separate `if` statements for menu choices
- **Screen clearing:** `clear_screen()` called at the **top** of `while True` loops, not scattered at the bottom of each block
- **Cancel pattern:** Every multi-step CLI flow allows typing `'q'` to cancel and `continue` back to the main menu
- **Input safety:** `.strip().lower()` on most text inputs to avoid whitespace/case bugs
- **List comprehensions:** Used for filtering when appropriate, but always double-check which list version (original vs modified copy) is being read from
- **Sets over lists:** Used when uniqueness matters (e.g., tracking unique attacking IPs)
- **Naming constants:** e.g. `ALERT_THRESHOLD = 5` instead of hardcoded magic numbers
- **rich library:** Used for CLI output formatting — Console, Table, Panel — across Projects 4 and 5

---

## 🐛 Debugging Habits Demonstrated

- Catches own bugs before being told (e.g. `count`/`i` not resetting between loop runs, `clear_screen()` placement issues, missing `elif` for "no" responses)
- Documents bug evolution in notebooks — Problem → Fix → Impact format
- Tests edge cases deliberately (invalid input, empty input, duplicate entries)
- Asks "why" not just "what" — wants to understand root cause, not just apply the fix

---

## 🎭 SOC Analyst Simulation — Running Storyline

A fictional employer ("CyberShield Analytics") and client ("Meridian Bank") 
were created to simulate real analyst workflows with deadlines and 
open-ended tasks (no step-by-step instructions given).

- **Simulation 1 — Meridian Bank Login Surge:** Investigated overnight 
  login failures, identified brute force pattern, exported findings, 
  wrote client-facing summary. Became Portfolio Project 05.

This format is meant to continue as new scenarios are introduced, 
escalating in complexity as more skills are learned.

---

## 🔜 Immediate Next Steps

1. Finish Phase 1 Milestone Project — clean a messy login CSV (filter 
   missing timestamps, export clean version)
2. Introduce Regex naturally through the next SOC simulation (log parsing)
3. Move into Phase 2 — NumPy deep dive, missing value handling, visualization
4. Consider adding password-protected access (`getpass` module) to a 
   future CLI tool — noted as a parked idea

---

## 💼 Career Context

- Background: Former QA Analyst in a BPO company
- Recently started a new job (details not specified in this doc)
- Working toward: Cybersecurity Data Scientist (long-term, 12-18 month goal)
- Realistic near-term target: Junior Data Analyst roles with strong portfolio
- Daily availability: ~4 days/week with flexible shifting schedule

---

## 📝 Notes for Any AI Reviewing This Repo

- All scripts are built incrementally with deliberate bug-introduction 
  and bug-fixing documented in companion Jupyter notebooks
- The person prefers understanding *why* a fix works over just being 
  given the fix
- Tone preference: direct, honest feedback — no excessive praise, 
  but acknowledge genuine wins
- This person consistently exceeds exercise requirements with their 
  own design choices — encourage and review those additions seriously, 
  don't just grade against the original ask
