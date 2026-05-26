
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)

sales = pd.read_csv("data_manipulation_pd.py/sales_subset.csv")

# total weekly_sales
sales_all = sales["weekly_sales"].sum()

# store A total weekly sales
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()

# store B total weekly sales
sales_B = sales[sales["type"] == "B"]["weekly_sales"].sum()

# store C total weekly sales
sales_C = sales[sales["type"] == "C"]["weekly_sales"].sum()

# prop sales of ABC
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all

# groupby: total weekly sales
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# prop sales of ABC
sales_propn_by_type2 = sales_by_type / sum(sales["weekly_sales"])

# sales during holidays
sales_by_type_is_holiday = sales.groupby(["type", "is_holiday"])["weekly_sales"].sum()

# weekly sales mean, max, mean and median for each store
# I used np.mean & np.median because mean & median aren't Python built-in functions 
sales_stats = sales.groupby("type")["weekly_sales"].agg(["min", "max", "mean", "median"])

# unemployment & fuel price in USD per liter min, max, mean, median for each store
unemp_fuel_stats = sales.groupby("type")[["unemployment", "fuel_price_usd_per_l"]].agg(["min", "max", "mean", "median"])

