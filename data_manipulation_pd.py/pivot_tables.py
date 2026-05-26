
import pandas as pd
pd.set_option('display.max_columns', None)

sales = pd.read_csv("data_manipulation_pd.py/sales_subset.csv")

# weekly sales mean by store type
mean_sales_by_type = sales.pivot_table(values = "weekly_sales", index = "type")

# weekly sales mean and median by store type
mean_med_sales_by_type = sales.pivot_table(values = "weekly_sales", index = "type", aggfunc = ["mean", "median"])

# weekly sales mean by store type and holiday
mean_sales_by_type_holiday = sales.pivot_table(values = "weekly_sales", index = "type", columns = "is_holiday")

# weekly sales mean by department and store type, NaN values filled with 0
#print(sales.pivot_table(values = "weekly_sales", index = "type", columns = "department", fill_value = 0))

# weekly sales mean by department and store type, NaN values filled with 0, and rows and columns summed
#print(sales.pivot_table(values = "weekly_sales", index = "type", columns = "department", fill_value = 0, margins = True))

# key observation:
    # since we have more data for store A (about 90%), /
    # the grand total is much closer to its value

temperatures = pd.read_csv('data_manipulation_pd.py/temperatures.csv')

temperatures["date"] = pd.to_datetime(temperatures["date"])

temperatures["year"] = temperatures["date"].dt.year

temp_by_country_city_vs_year = temperatures.pivot_table(values = "avg_temp_c", 
                                                        index = ['country', 'city'], 
                                                        columns = "year")

mean_temp_by_year = temp_by_country_city_vs_year.mean()

print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])

mean_temp_by_city = temp_by_country_city_vs_year.mean(axis = 'columns')

print(mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()])