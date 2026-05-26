
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)

data = {
    'timestamp': [
        '2024-01-01 08:00', '2024-01-01 08:05', '2024-01-01 08:10',
        '2024-01-01 08:15', '2024-01-01 08:20', '2024-01-01 08:25',
        '2024-01-01 08:30', '2024-01-01 08:35', '2024-01-01 08:40',
        '2024-01-01 08:45', '2024-01-01 08:50', '2024-01-01 08:55',
        '2024-01-01 09:00', '2024-01-01 09:05', '2024-01-01 09:10',
        '2024-01-01 09:15', '2024-01-01 09:20', '2024-01-01 09:25',
        '2024-01-01 09:30', '2024-01-01 09:35'
    ],
    'src_ip': [
        '192.168.1.10', '10.0.0.5', '192.168.1.10', '172.16.0.3',
        '10.0.0.5', '192.168.1.10', '10.0.0.99', '172.16.0.3',
        '10.0.0.5', '192.168.1.10', '10.0.0.99', '172.16.0.3',
        '192.168.1.10', '10.0.0.5', '10.0.0.99', '172.16.0.3',
        '192.168.1.10', '10.0.0.5', '10.0.0.99', '172.16.0.3'
    ],
    'dst_ip': [
        '8.8.8.8', '185.220.101.1', '8.8.4.4', '192.168.1.1',
        '8.8.8.8', '185.220.101.1', '8.8.8.8', '192.168.1.1',
        '185.220.101.1', '8.8.4.4', '185.220.101.1', '192.168.1.1',
        '8.8.8.8', '185.220.101.1', '8.8.4.4', '10.0.0.1',
        '185.220.101.1', '8.8.8.8', '185.220.101.1', '192.168.1.1'
    ],
    'protocol': [
        'DNS', 'TCP', 'DNS', 'HTTP', 'DNS', 'TCP', 'DNS', 'HTTP',
        'TCP', 'DNS', 'TCP', 'HTTP', 'DNS', 'TCP', 'DNS', 'HTTP',
        'TCP', 'DNS', 'TCP', 'HTTP'
    ],
    'bytes_sent': [
        512, 15400, 480, 3200, 510, 18200, 490, 2900,
        16800, 520, 14900, 3100, 505, 17600, 475, 2800,
        19200, 495, 15600, 3300
    ],
    'bytes_received': [
        1024, 512, 980, 8400, 1100, 480, 990, 7800,
        600, 1050, 550, 8100, 1080, 520, 1010, 7600,
        490, 1090, 570, 8200
    ],
    'alert': [
        False, True, False, False, False, True, False, False,
        True, False, True, False, False, True, False, False,
        True, False, True, False
    ],
    'country': [
        'US', 'RU', 'US', 'US', 'US', 'RU', 'US', 'US',
        'RU', 'US', 'RU', 'US', 'US', 'RU', 'US', 'US',
        'RU', 'US', 'RU', 'US'
    ]
}

net_logs = pd.DataFrame(data)

print(net_logs.shape)
print(net_logs.isnull().sum())
print(net_logs.describe().round(2))

net_logs_copy = net_logs.copy()

net_logs_copy['total_bytes'] = net_logs_copy['bytes_sent'] + net_logs_copy['bytes_received']
net_logs_copy['is_external'] = ~net_logs_copy['dst_ip'].str.startswith(('192.168', '10.', '172.16'))
net_logs_copy["traffic_size"] = np.where(net_logs_copy['total_bytes'] > 10000, "large", "small")
net_logs_copy['risk_level'] = np.where((net_logs_copy['alert'] == True) & 
                                       (net_logs_copy['country'] == 'RU'), 
                                       'high', 'low')
print(net_logs_copy.head())

high_risk = net_logs_copy.loc[net_logs_copy['risk_level'] == 'high', 
                              ['timestamp', 'src_ip', 'dst_ip', 'total_bytes',]]

print(high_risk.sort_values(by='total_bytes', ascending = False))

print(net_logs_copy[np.logical_and(net_logs_copy['is_external'] == True,
                                   net_logs_copy['traffic_size'] == 'large')])

print(net_logs_copy['total_bytes'].agg(average='mean',
                                       lowest='min',
                                       highest='max'
                                       ))

print(net_logs_copy.groupby('src_ip').agg(total_sent=('bytes_sent', 'sum'),
                                          average_received=('bytes_received', 'mean'),
                                          total_alerts=('alert', 'sum')
                                          ))

print(net_logs_copy.groupby(['country', 'protocol']).size().reset_index(name='count'))

print(net_logs_copy.loc[net_logs_copy['src_ip'] == '10.0.0.99',
      ['timestamp', 'protocol', 'alert', 'risk_level']])

print(net_logs_copy.iloc[-5:, [4, 5, 8]])
