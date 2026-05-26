
import pandas as pd
pd.set_option('display.max_columns', None)

import matplotlib.pyplot as plt

import pickle

with open('data_manipulation_pd.py/avoplotto.pkl', 'rb') as file:
    avocados = pickle.load(file)
    with open('data_manipulation_pd.py/avoplotto.pkl', 'wb') as f:
        pickle.dump(avocados, f)

#nb_sold_by_size = avocados.groupby("size")["nb_sold"].sum()
#nb_sold_by_size.plot(kind="bar")

#nb_sold_by_date = avocados.groupby('date')['nb_sold'].sum()
#nb_sold_by_date.plot(x='date',
#                     y='nb_sold',
#                     kind='line')

#avocados.plot(x='nb_sold',
#              y='avg_price',
#              kind='scatter',
#              title='Number of avocados sold vs average price')

#avocados[avocados['type'] == 'conventional']['avg_price'].hist(alpha=0.5)
#avocados[avocados['type'] == 'organic']['avg_price'].hist(alpha=0.5)

#plt.legend(['conventional', 'organic'])

avocados["date"] = pd.to_datetime(avocados["date"])

avocados_2016 = avocados[avocados['date'].dt.year == 2016]
print(avocados_2016.isna())

# to check for any column..
print(avocados_2016.isna().any())

# bar plot of missing values by variable..
avocados_2016.isna().sum().plot(kind='bar')
plt.show(block=True)