
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)

wards = pd.read_csv('join_data_py/Chicago_wards.csv', index_col=0)
census = pd.read_csv('join_data_py/Chicago_census.csv', index_col=0)
taxi_owners = pd.read_csv('join_data_py/taxi_owners.csv', index_col=0)
taxi_veh = pd.read_csv('join_data_py/taxi_vehicles.csv', index_col=0)

wards_census = wards.merge(census, on='ward', suffixes=('_ward', '_cen'))

taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes=('_own', '_veh'))

print(taxi_own_veh['fuel_type'].value_counts())