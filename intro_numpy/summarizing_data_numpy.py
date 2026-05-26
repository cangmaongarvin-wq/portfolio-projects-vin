
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

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

if __name__ == "__main__":
    
    
    avg_monthly_sales = monthly_sales.mean(axis=1)
    plt.plot(np.arange(1, 13), avg_monthly_sales,label="Average sales across industries")
    plt.plot(np.arange(1, 13), monthly_sales[:, 2], label="Department store sales")


    cumulative_monthly_industry_sales = monthly_sales.cumsum(axis=0)
    plt.plot(np.arange(1, 13), cumulative_monthly_industry_sales[:, 0], label="Liquor Stores")
    plt.plot(np.arange(1, 13), cumulative_monthly_industry_sales[:, 1], label="Restaurants")
    plt.plot(np.arange(1, 13), cumulative_monthly_industry_sales[:, 2], label="Department stores")
    plt.legend()
    plt.show(block=True)