import csv
import os

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.terminal_theme import MONOKAI

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

console = Console(record=True)

total_logins = 0
success_logins = 0
failed_logins = 0

failed_counts = {}
failed_ips = {}
failed_systems = {}
user_ips = {}

suspicious_rows_buffer = []

with open("portfolio/05_meridian_login_analysis/meridian_logs.csv", "r", newline="") as infile: 
    logins = csv.DictReader(infile)
    csv_headers = logins.fieldnames

    clear_screen()

    console.print(Panel.fit(
        "        MERIDIAN LOGIN ANALYSIS — SOC TRIAGE        ",
        style="bold white on magenta",
        border_style="magenta"
    ))
    console.print()

    for row in logins:
        total_logins += 1
        
        if row["status"] == "FAILED":
               failed_logins += 1
               user = row["user"]
               ip = row["ip"]
               system = row["system"]
               
               failed_counts[user] = failed_counts.get(user, 0) + 1
               failed_ips[ip] = failed_ips.get(ip, 0) + 1
               failed_systems[system] = failed_systems.get(system, 0) + 1
               
               if user not in user_ips:
                   user_ips[user] = set()
               user_ips[user].add(ip)
                    
               suspicious_rows_buffer.append(row)

        elif row["status"] == "SUCCESS":
               success_logins += 1
        else:
            console.print("[yellow]WARNING: Unknown Values Detected[/yellow]")
    
    console.print(f"[bold]TOTAL LOGINS:[/bold] {total_logins}")
    console.print(f"[green] {success_logins} Successful[/green] vs [red] {failed_logins} Failed[/red] logins.\n")

with open("portfolio/05_meridian_login_analysis/suspicious_findings.csv", "w", newline="") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=csv_headers)
    writer.writeheader()
    
    for row in suspicious_rows_buffer:
        writer.writerow(row)

console.print("[bold cyan]SOC TRIAGE REPORT: TOP OFFENDERS & TARGETS[/bold cyan]")
console.print("-" * 50)

top_users = sorted(failed_counts, key=failed_counts.get, reverse=True)[:3]
top_ips = sorted(failed_ips, key=failed_ips.get, reverse=True)[:3]
top_systems = sorted(failed_systems, key=failed_systems.get, reverse=True)[:3]

user_table = Table(title="Top Targeted Accounts", title_style="bold yellow", box=None)
user_table.add_column("Rank", justify="center", style="dim")
user_table.add_column("Username", style="bold gold1")
user_table.add_column("Total Failures", justify="right", style="bold red")

for rank, user in enumerate(top_users, 1):
    user_table.add_row(str(rank), f"'{user}'", str(failed_counts[user]))
    
ip_table = Table(title="Top Attacking IP Addresses", title_style="bold red", box=None)
ip_table.add_column("Rank", justify="center", style="dim")
ip_table.add_column("IP Address", style="bold bright_red")
ip_table.add_column("Total Failures", justify="right", style="bold red")

for rank, ip in enumerate(top_ips, 1):
    ip_table.add_row(str(rank), f"'{ip}'", str(failed_ips[ip]))
    
sys_table = Table(title="Top Targeted Systems / Assets", title_style="bold cyan", box=None)
sys_table.add_column("Rank", justify="center", style="dim")
sys_table.add_column("Host", style="bold cyan")
sys_table.add_column("Total Failures", justify="right", style="bold red")

for rank, sys in enumerate(top_systems, 1):
    sys_table.add_row(str(rank), f"'{sys}'", str(failed_systems[sys]))

console.print(user_table)
console.print()
console.print(ip_table)
console.print()
console.print(sys_table)
console.print("="*50)

target_account = "admin"
ALERT_THRESHOLD = 5

if target_account in user_ips:
    total_admin_failures = failed_counts[target_account]
    unique_ip_count = len(user_ips[target_account])
    formatted_ips = ", ".join([f"[bold white]{ip}[/bold white]" for ip in user_ips[target_account]])

    if total_admin_failures >= ALERT_THRESHOLD:
        
        if unique_ip_count >= 3:
            attack_profile = "[bold bright_red]CRITICAL DISTRIBUTED ATTACK[/bold bright_red]"
            border_color = "bright_red"
        else:
            attack_profile = "[bold orange3]CRITICAL ISOLATED ATTACK[/bold orange3]"
            border_color = "orange3"

        console.print(Panel(
                f"Threat Profile: {attack_profile}\n\n"
                f"Account [yellow]'{target_account}'[/yellow] was hammered [bold red]{total_admin_failures}[/bold red] times!\n"
                f"Source Vector: Originated from [bold white]{unique_ip_count}[/bold white] unique IP address(es).\n"
                f"Rogue IP List: {formatted_ips}",
                title="Forensic Audit Alert",
                border_style=border_color
            ))
    else:
        console.print(f"[green]Audit: Low-volume threat detected on '{target_account}' ({total_admin_failures} failure). No action needed at this time.[/green]")
else:
    console.print(f"[green]Forensic Audit: No malicious footprint detected on target account '{target_account}'.[/green]")

console.save_text("portfolio/05_meridian_login_analysis/soc_triage_report.txt")
console.save_html("portfolio/05_meridian_login_analysis/soc_triage_report.html", theme=MONOKAI)