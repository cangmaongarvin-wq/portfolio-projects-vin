
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')


data_list = [
    [4134, 23925, 8657],
    [4116, 23875, 9142],
    [4673, 27197, 10645],
    [4580, 25637, 10456],
    [5109, 27995, 11299],
    [5011, 27419, 10625],
    [5245, 27305, 10630],
    [5270, 27760, 11550],
    [4680, 24988, 9762],
    [4913, 25802, 10456],
    [5312, 25405, 13401],
    [6630, 27797, 18403]
]
monthly_sales = np.array(data_list)
monthly_growth_rate_1D = np.array([1.01, 1.03, 1.03, 1.02, 
                                   1.05, 1.03, 1.06, 1.04, 
                                   1.03, 1.04, 1.02, 1.01])
monthly_growth_rate_2D = monthly_growth_rate_1D.reshape(12, 1)

from vectorized_operations import monthly_industry_multipliers

mean_multipliers = monthly_industry_multipliers.mean(axis=0)
print(mean_multipliers)