
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)

data = {
    'timestamp': ['2024-01-01 08:00','2024-01-01 08:05','2024-01-01 08:10',
                  '2024-01-01 08:15','2024-01-01 08:20'],
    'src_ip':    ['192.168.1.10','10.0.0.5','192.168.1.10','172.16.0.3','10.0.0.5'],
    'dst_ip':    ['8.8.8.8','185.220.101.1','8.8.4.4','192.168.1.1','8.8.8.8'],
    'protocol':  ['DNS','TCP','DNS','HTTP','DNS'],
    'bytes_sent':[512, 15400, 480, 3200, 510],
    'alert':     [False, True, False, False, True]
}

df = pd.DataFrame(data)

# 2a.
true_alerts = df[df['alert'] == True]
# watch for columns with boolean values when setting your condition. "True" is different from True.
print(true_alerts)
print()
# 2b.
dns_and_bytes = df[np.logical_and(
    df['protocol']=="DNS", 
    df['bytes_sent'] > 500)]
print(dns_and_bytes)
print()
# 2c.
detect = ['10.0.0.5', '172.16.0.3']
print(df[df['src_ip'].isin(detect)])
print()

# 3. Sorting Data
# 3a.
print(df.sort_values(by='bytes_sent', 
                     ascending = False))
print()
# 3b.
df_sorted = df.sort_values(by=['protocol', 'bytes_sent'], 
                           ascending=[True, False])
print()

# 4. Creating new columns
# 4a.
df['bytes_kb'] = (df['bytes_sent'] / 1024).round(2)
# 4b.
df['is_external'] = ~df['dst_ip'].str.startswith(
    ('192.168', '10.', '172.16'))
print()

# 5. Conditional columns with np.where()
df_c = df.copy()
# 5.a
df_c['traffic_size'] = np.where(df['bytes_sent'] > 5000, 'large', 'small')
# 5.b
df_c['risk_label'] = np.where((df['alert'] == True) & 
                            (df['bytes_sent'] > 5000), 'high', 'low')

# 6. Aggregations
# 6a. To find mean, max, min
print(df_c['bytes_sent'].agg(['mean', 'max', 'min']))
# 6b.
print(df_c['protocol'].value_counts())
# 6c.
print(df_c)
print(df_c['bytes_sent'].agg(
    average='mean', 
    highest='max', 
    lowest='min', 
    total='count'))
print()

# 7. GroupBy analysis
# 7a.
print(df_c.groupby('protocol')['bytes_sent'].sum())
print()
# 7b. calculate mean bytes sent and total alert per source IP
print(df_c.groupby('src_ip').agg(
    mean_bytes=('bytes_sent', 'mean'),
    total_alerts=('alert', 'sum')
))
print()
# 7c. Group by both protocol and alert, 
# then count the number of events in each group.
print(df_c.groupby(['protocol', 'alert']).size().reset_index(name='count'))
print()

# 8. Row / Column selection (loc/iloc)
# 8a.
print(df_c.iloc[0:3, 0:3])
print()
# 8b.
print(df_c.loc[df_c['alert'] == True, 
      ['src_ip', 'bytes_sent', 'protocol']])
# 8c.
print()
print(df_c.iloc[-1, :])
print(df_c.iloc[2, 4])