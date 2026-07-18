import os
import json

from rich.console import Console
from rich.table import Table

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

console = Console()

with open("portfolio/04_daily_ip_alert_comparator/logs.json", "r") as file:
    log_data = json.load(file)

yesterday_set = set(log_data["yesterday"])
today_set = set(log_data["today"])
thresholds = (5, 10, 20)

while True:
    clear_screen()

    console.print("=========================================", style="bold magenta")
    console.print("       DAILY IP ALERT COMPARATOR         ", style="bold white on black")
    console.print("=========================================\n", style="bold magenta")
    
    option = console.input("[bold cyan]Press Enter to continue (or enter 'q' to quit):[/bold cyan] \n").strip().lower()

    clear_screen()
    
    if option == 'q':
        console.print("[bold red]Closing application...[/bold red]")
        break
        
    elif not option:
        new_alerts = today_set - yesterday_set
        persistent_threats = today_set & yesterday_set
        resolved_alerts = yesterday_set - today_set
        combined_logs = yesterday_set | today_set

        table = Table(title="IP Traffic Delta Analysis", title_style="bold cyan", show_lines=True) 
        table.add_column("Incident Status", justify="left")
        table.add_column("Target IP Address", justify="center")
        
        for ip in sorted(new_alerts):
            table.add_row("[bold red]NEW ALERT[/bold red]", ip)
            
        for ip in sorted(persistent_threats):
            table.add_row("[bold yellow]PERSISTENT THREATS[/bold yellow]", ip)
            
        for ip in sorted(resolved_alerts):
            table.add_row("[bold green]RESOLVED THREATS[/bold green]", ip)

        console.print(table)
        console.print()
        
        console.print(f"[bold dim white]Total Unique IPs Tracked Across Both Days:[/bold dim white] {len(combined_logs)}\n")
        
        ip_hit_count = len(new_alerts)
        low_limit, med_limit, high_limit = thresholds
        
        if ip_hit_count >= high_limit:
            console.print(f"[bold white on red][CRITICAL!][/bold white on red] [red] {ip_hit_count} new threats detected! Immediate action required.[/red]")
        elif ip_hit_count >= med_limit:
            console.print(f"[bold white on yellow][WARNING!][/bold white on yellow] [yellow]{ip_hit_count} new threats detected! Monitor closely.[/yellow]")
        else:
            console.print(f"[bold white on green][LOW][/bold white on green] {ip_hit_count} new threats detected. Traffic within baseline.")

        console.input("\n[dim white]Press Enter to return to main menu...[/dim white]")

    else:
        console.input("[bold red]Invalid input.[/bold red] Press Enter to try again. ")