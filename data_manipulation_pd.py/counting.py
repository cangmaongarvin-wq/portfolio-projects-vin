import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)


sales = pd.read_csv("data_manipulation_pd.py/sales_subset.csv")

store_types = sales.drop_duplicates(subset=["store", "type"])
store_depts = sales.drop_duplicates(subset=["store", "department"])
holiday_dates = sales[sales["is_holiday"]].drop_duplicates(subset = "date")
holiday_dates_nodup = holiday_dates.duplicated().sum()

store_counts = store_types['type'].value_counts()
store_props = store_types['type'].value_counts(normalize=True)

dept_counts_sorted = store_depts['department'].value_counts(sort=True)
dept_props_sorted = store_depts['department'].value_counts(normalize=True, sort=True)

print(dept_counts_sorted, dept_props_sorted)