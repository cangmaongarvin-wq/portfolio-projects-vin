
import numpy as np

multiplier_1 = [
    [0.98, 1.02, 1.0],
    [1.00, 1.01, 0.97],
    [1.06, 1.03, 0.98],
    [1.08, 1.01, 0.98],
    [1.08, 0.98, 0.98],
    [1.1, 0.99, 0.99],
    [1.12, 1.01, 1.0],
    [1.1, 1.02, 1.0],
    [1.11, 1.01, 1.01],
    [1.08, 0.99, 0.97],
    [1.09, 1.0, 1.02],
    [1.13, 1.03, 1.02]
]

multiplier_2 = [
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

monthly_industry_multipliers = np.array(multiplier_1)
monthly_sales = np.array(multiplier_2)
projected_monthly_sales = monthly_sales * monthly_industry_multipliers

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

if __name__ == "__main__":
    
    plt.plot(np.arange(1, 13), monthly_sales[:, 0], label = "Current liquor store sales")
    plt.plot(np.arange(1, 13), projected_monthly_sales[:, 0], label="Projected liquor store sales")
    plt.legend()
    plt.show(block=True)

    #Using np.vectorize() instead of "for" looping function in Python
    names = np.array([["Izzy", "Monica", "Marvin"],
                    ["Weber", "Patel", "Hernandez"]])

    vectorized_upper = np.vectorize(str.upper)
    uppercase_names = vectorized_upper(names)
    print(uppercase_names)