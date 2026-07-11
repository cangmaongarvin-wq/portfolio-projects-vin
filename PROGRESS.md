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
| Milestone Project | ✅ Complete |

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
| 06 | Milestone Project (messy CSV cleanup) | File I/O, data cleaning, validation, normalization | ✅ Complete |

**Milestone Project key decisions:**
- Duplicate detection: same `user_id` + `ip_address` within a 1-minute window, via a `(user, ip, rounded_timestamp)` key stored in a `seen` set
- Custom `is_valid_ip()` (4 parts, 0-255 each) and `is_valid_status()` (against a `VALID_STATUSES` set)
- Accepts 3 real-world timestamp formats (`%Y-%m-%d %H:%M:%S`, `%d/%m/%Y %H:%M:%S`, `%Y-%m-%dT%H:%M:%SZ`)
- Flagged rows excluded entirely from `clean_logins.csv`; a row is counted once in the total even if it trips multiple issue types, though each issue type's own count can still include that row
- Normalize-and-write-back pattern: `user_id`, `status`, `ip_address`, and `timestamp` are all normalized for validation *and* written back into the row before saving, so the clean CSV doesn't just pass validation but is also formatted consistently (fixed inconsistent casing, whitespace, and 3 different timestamp formats coexisting in the same column)

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
- Documents bug evolution in companion notebooks using a unified format (see below)
- Tests edge cases deliberately (invalid input, empty input, duplicate entries)
- Asks "why" not just "what" — wants to understand root cause, not just apply the fix

---

## 📓 Notebook Documentation Standard

Applies to every project notebook going forward; all five existing notebooks (01, 03, 04, 05, and the Milestone Project) were retrofitted to this format:

- **Intro cell:** title (no emoji), one-line description, "What this does" bullet list, "Built with" tech stack line
- **Iteration cells:** unified heading, either "Revision N: Bug Check - <label>" for actual bugs or "Revision N: Enhancement - <label>" for feature additions that weren't bugs, followed by what was found/why, then the fix, then the updated code cell
- **Closing section:** every notebook ends with a findings/takeaways section in analyst-facing prose, grounded in the tool's actual output, not just a bullet dump of implementation details
- No trailing empty cells; no emojis or em-dashes anywhere in notebook markdown

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

1. Introduce Regex naturally through the next SOC simulation (log parsing)
2. Move into Phase 2 — NumPy deep dive, missing value handling, visualization
3. Consider adding password-protected access (`getpass` module) to a 
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
