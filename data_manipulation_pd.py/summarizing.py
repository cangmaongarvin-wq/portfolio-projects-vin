
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)

sales = pd.read_csv("data_manipulation_pd.py/sales_subset.csv")

#print(sales.head())
#print(sales.info())
#print(sales["weekly_sales"].mean())
#print(sales["weekly_sales"].median())
#print(sales["date"].min())
#print(sales["date"].max())
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
    # iqr is short for interquantile range, which is the -
    # - 75th percentile minust 25th. This is helpful if -
    # - data contains outliers

#print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment",]].agg(iqr))
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment",]].agg([iqr, "median"]))

