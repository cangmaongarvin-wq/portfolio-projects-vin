import pandas as pd
pd.set_option('display.max_columns', None)
import matplotlib.pyplot as plt

df = pd.read_csv("portfolio/Phase_2/endpoint_health_raw.csv")

# memory_gb has invalid negative readings, treat them as missing
df.loc[df['memory_gb'] < 0, 'memory_gb'] = pd.NA

missing_before = df.isnull().sum()
missing_pct_before = (df.isnull().mean() * 100).round(2)

print("\nMissing before:")
print(missing_before)
print("\nMissing % before:")
print(missing_pct_before)

df.ffill(inplace=True)

missing_after = df.isnull().sum()
print("\nMissing after:")
print(f"{missing_after}\n")

# PART 5 - Anomaly detection on srv-web-02
df['timestamp'] = pd.to_datetime(df['timestamp'])
web_server_df = df[df['server'] == 'srv-web-02'].copy()

cpu_mean = web_server_df['cpu_percent'].mean()
cpu_std = web_server_df['cpu_percent'].std()
threshold = cpu_mean + 2 * cpu_std

web_server_df['cpu_zscore'] = (web_server_df['cpu_percent'] - cpu_mean) / cpu_std

anomalies = web_server_df[web_server_df['cpu_percent'] > threshold].copy()
anomalies['severity'] = anomalies['cpu_zscore'].apply(
    lambda z: 'severe' if z >= 3 else 'borderline'
)

print(f"srv-web-02 CPU baseline: mean={cpu_mean:.1f}%, std={cpu_std:.1f}%")
print(f"Anomaly threshold (mean + 2 std): {threshold:.1f}%\n")
print(anomalies[['timestamp', 'cpu_percent', 'cpu_zscore', 'severity', 'memory_gb', 'network_mbps']])

plt.figure(figsize=(12, 5))
plt.plot(web_server_df['timestamp'], web_server_df['cpu_percent'], color='red', label='CPU %')
plt.axhline(threshold, color='gray', linestyle='--', label=f'Threshold ({threshold:.1f}%)')
plt.scatter(anomalies['timestamp'], anomalies['cpu_percent'], color='black', zorder=5, label='Flagged')
plt.title('CPU Usage Over Time: srv-web-02')
plt.xlabel('Time')
plt.ylabel('CPU Percent')
plt.legend()
plt.grid(True)
plt.show()

df['cpu_zscore'] = df.groupby('server')['cpu_percent'].transform(
    lambda x: (x - x.mean()) / x.std()
)

df['cpu_threshold'] = df.groupby('server')['cpu_percent'].transform(
    lambda x: x.mean() + 2 * x.std()
)

fleet_anomalies = df[df['cpu_percent'] > df['cpu_threshold']].copy()
fleet_anomalies['severity'] = fleet_anomalies['cpu_zscore'].apply(
    lambda z: 'severe' if z >= 3 else 'borderline'
)

print()
print(
    fleet_anomalies[['timestamp', 'server', 'cpu_percent', 'cpu_zscore', 'severity', 'memory_gb', 'network_mbps']]
    .sort_values(['server', 'timestamp'])
)

app02_df = df[df['server'] == 'srv-app-02'].copy()

cpu_mean = app02_df['cpu_percent'].mean()
cpu_std = app02_df['cpu_percent'].std()
threshold = cpu_mean + 2 * cpu_std

app02_df['cpu_zscore'] = (app02_df['cpu_percent'] - cpu_mean) / cpu_std
app02_anomalies = app02_df[app02_df['cpu_percent'] > threshold].copy()
app02_anomalies['severity'] = app02_anomalies['cpu_zscore'].apply(
    lambda z: 'severe' if z >= 3 else 'borderline'
)

print(f"\nsrv-app-02 CPU baseline: mean={cpu_mean:.1f}%, std={cpu_std:.1f}%")
print(f"Anomaly threshold (mean + 2 std): {threshold:.1f}%\n")
print(app02_anomalies[['timestamp', 'cpu_percent', 'cpu_zscore', 'severity', 'memory_gb', 'network_mbps']])

plt.figure(figsize=(12, 5))
plt.plot(app02_df['timestamp'], app02_df['cpu_percent'], color='red', label='CPU %')
plt.axhline(threshold, color='gray', linestyle='--', label=f'Threshold ({threshold:.1f}%)')
plt.scatter(app02_anomalies['timestamp'], app02_anomalies['cpu_percent'], color='black', zorder=5, label='Flagged')
plt.title('CPU Usage Over Time: srv-app-02')
plt.xlabel('Time')
plt.ylabel('CPU Percent')
plt.legend()
plt.grid(True)
plt.show()

print()

spike_time = fleet_anomalies[fleet_anomalies['server'] == 'srv-app-01']['timestamp'].iloc[0]
print(f"srv-app-01 spike timestamp: {spike_time}\n")
print(fleet_anomalies[fleet_anomalies['timestamp'] == spike_time])
