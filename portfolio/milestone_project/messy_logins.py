# MILESTONE PROJECT: MESSY LOGINS

# PART 1: IMPORT AND SETUP
import csv
import os
from datetime import datetime

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

INPUT_FILE = "portfolio/milestone_project/messy_logins.csv"
OUTPUT_FILE = "portfolio/milestone_project/clean_logins.csv"
REPORT_FILE = "portfolio/milestone_project/data_quality_report.txt"

REQUIRED_FIELDS = ["timestamp", "user_id", "ip_address", "status"]
TIMESTAMP_FORMATS = [
    "%Y-%m-%d %H:%M:%S",     # 2026-06-08 08:12:34
    "%d/%m/%Y %H:%M:%S",     # 08/06/2026 08:14:02
    "%Y-%m-%dT%H:%M:%SZ",    # 2026-06-08T08:18:00Z
]
VALID_STATUSES = {"SUCCESS", "FAILED"}

console = Console(record=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def is_valid_ip(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        if not 0 <= int(part) <= 255:
            return False
    return True

def parse_timestamp(ts_string):
    for fmt in TIMESTAMP_FORMATS:
        try:
            return datetime.strptime(ts_string, fmt)
        except ValueError:
            continue

    return None

def is_valid_status(status):
    return status.strip().upper() in VALID_STATUSES

# PART 2: READ AND CLEAN
clean_rows = []
seen = set()

total_rows = 0
flagged_rows = 0

issue_counts = {
    "missing_fields": 0,
    "invalid_ip": 0,
    "invalid_timestamp": 0,
    "invalid_status": 0,
    "duplicate": 0,
}

with open(INPUT_FILE, "r", newline="") as infile:
    reader = csv.DictReader(infile)
    csv_headers = reader.fieldnames

    clear_screen()
    console.print(Panel.fit(
        "        MILESTONE PROJECT — LOGIN DATA CLEANING        ",
        style="bold white on blue",
        border_style="blue"
    ))
    console.print()

    for row in reader:
        total_rows += 1
        issues = set()

        user_value = (row.get("user_id") or "").strip().lower()
        row["user_id"] = user_value
        ip_value = (row.get("ip_address") or "").strip().lower()
        row["ip_address"] = ip_value
        ts_value = (row.get("timestamp") or "").strip().lower()
        status_value = (row.get("status") or "").strip().lower()
        row["status"] = status_value 

        # MISSING FIELDS
        if not user_value or not ip_value or not ts_value or not status_value:
            issues.add("missing_fields")
        
        # INVALID IP
        if ip_value and not is_valid_ip(ip_value):
            issues.add("invalid_ip")
        
        # INVALID TIMESTAMP
        parsed_ts = None
        if ts_value:
            parsed_ts = parse_timestamp(ts_value)
            if parsed_ts is None:
                issues.add("invalid_timestamp")
            else:
                row["timestamp"] = parsed_ts.strftime("%Y-%m-%d %H:%M:%S")
        
        # INVALID STATUS
        if status_value and not is_valid_status(status_value):
            issues.add("invalid_status")
        
        # DUPLICATE: same normalized user_id + ip within the same minute
        if user_value and ip_value and parsed_ts:
            rounded_ts = parsed_ts.replace(second=0, microsecond=0)
            dup_key = (user_value, ip_value, rounded_ts)

            if dup_key in seen:
                issues.add("duplicate")
            else:
                seen.add(dup_key)
        
        if issues:
            flagged_rows += 1
            for issue in issues:
                issue_counts[issue] += 1
        
        else:
            clean_rows.append(row)

# PART 3: WRITING CLEAN LOGINS CSV FILE(clean_logins.csv)
console.print(f"[bold]TOTAL ROWS READ: [/bold] {total_rows}")
console.print(f"[green]{len(clean_rows)} clean[/green] vs [red]{flagged_rows} flagged[/red]\n")

with open(OUTPUT_FILE, "w", newline="") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=csv_headers)
    writer.writeheader()

    for row in clean_rows:
        writer.writerow(row)

console.print(f"[green]Clean data written to {OUTPUT_FILE}[/green]\n")

# PART 4: DATA QUALITY REPORT
console.print("[bold cyan]DATA QUALITY REPORT[/bold cyan]")
console.print("-"*50)

report_table = Table(box=None)
report_table.add_column("Issue Type", style="bold yellow")
report_table.add_column("Rows Affected", justify="right", style="bold red")

for issue_label, count in issue_counts.items():
    report_table.add_row(issue_label.replace("_", " ").title(), str(count))

console.print(report_table)
console.print("-" * 50)

flagged_pct = (flagged_rows / total_rows * 100) if total_rows else 0
clean_pct = (len(clean_rows) / total_rows * 100) if total_rows else 0

console.print(Panel(
    f"Total Rows Processed: [bold]{total_rows}[/bold]\n"
    f"Clean Rows Written:   [bold green]{len(clean_rows)}[/bold green] ({clean_pct:.1f}%)\n"
    f"Flagged Rows:         [bold red]{flagged_rows}[/bold red] ({flagged_pct:.1f}%)\n"
    f"(a flagged row is counted once here, even if it tripped multiple issue types above)",
    title="Summary",
    border_style="cyan"
))

console.save_text(REPORT_FILE)
console.print(f"\n[green]Report saved to {REPORT_FILE}[/green]")