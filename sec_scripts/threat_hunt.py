
import pandas as pd
pd.set_option('display.max_columns', None)

sec_logs = pd.read_json('network_logs.json')

print("--- RAW FIREWALL SEC LOGS ---")
print(sec_logs)
print("\n" + "="*50 + "\n")

# hunt for threat type A: Potential Data Exfil
# RULE: find any connection where bytes_sent exceeds 5(mb)
exfil_threshold = 5000000
huge_transfers = sec_logs[sec_logs['bytes_sent'] > exfil_threshold]

print("⚠️ ALERT: POTENTIAL DATA EXFILTRATION DETECTED ⚠️")
if not huge_transfers.empty:
    print(huge_transfers[[
        "timestamp", "source_ip", "dest_ip", "bytes_sent"
    ]])
else:
    print("No large data transfers detected.")

print("\n" + "="*50 + "\n")

# hunt for threat type B: Recon / Port Scanning
deny_logs = sec_logs[sec_logs['action'] == "DENY"]
scan_counts = deny_logs['source_ip'].value_counts()

print("🚨 ALERT: RECONNAISSANCE / BLOCKED SCANNER SUMMARY 🚨")
print(scan_counts)