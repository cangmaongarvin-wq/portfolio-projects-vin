
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)

avocados_list = [
    {"date":'2019-11-03',
     "small_sold":10376832, 
     "large_sold":7835071},
    {"date":'2019-11-10',
    "small_sold":10717154,
    "large_sold":8561348}
    ]

avocados_2019 = pd.DataFrame(avocados_list)
print(avocados_2019)

avocados_dict = {
    "date": ['2019-11-03', '2019-11-10'],
    "small_sold": [10376832, 10717154],
    "large_sold": [7835071, 8561348]
}

avocados_2019_dict = pd.DataFrame(avocados_dict)
print(avocados_2019_dict)
