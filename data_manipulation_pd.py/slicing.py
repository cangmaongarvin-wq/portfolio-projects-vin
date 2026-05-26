
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)

temperatures = pd.read_csv('data_manipulation_pd.py/temperatures.csv')

temperatures_ind = temperatures.set_index(['country', 'city'])

temperatures_srt = temperatures_ind.sort_index()

print(temperatures_srt.loc[('India', 'Hyderabad'):('Iraq', 'Baghdad')])
print(temperatures_srt.loc[:, 'date':'avg_temp_c'])
print(temperatures_srt.loc[('India', 'Hyderabad'):('Iraq', 'Baghdad'), "date":"avg_temp_c"])

temperatures_bool = temperatures[(temperatures['date'] >= '2010-01-01') & 
                                 (temperatures['date'] <= '2011-12-31')]

temperatures_ind = temperatures.set_index('date').sort_index()

print(temperatures.iloc[22, 1])

print(temperatures.iloc[0:5])

print(temperatures.iloc[:, 2:4])

print(temperatures.iloc[0:10, 1])