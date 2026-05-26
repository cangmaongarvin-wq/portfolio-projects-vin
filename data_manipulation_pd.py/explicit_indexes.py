
import pandas as pd
pd.set_option('display.max_columns', None)

temperatures = pd.read_csv('data_manipulation_pd.py/temperatures.csv', index_col = 0)

# setting the index to city
temperatures_ind = temperatures.set_index("city")

# resetting the index of temperatures_ind / you can add drop = True argument to remove the resulting index


# creating a list with London and Paris to subset on temperatures
cities = ["London", "Paris"]

# subsetting using the cities variable
#print(temperatures[temperatures["city"].isin(cities)].head())
#print(temperatures_ind.loc[cities])

# setting a different index to temperatures dateset
temperatures_ind = temperatures.set_index(["country", "city"])

# keeping some countries and their capital / assigning it to rows_to_keep
rows_to_keep = [("Brazil", "Rio De Janeiro"), ("Pakistan", "Lahore")]

# subsetting temperatures_ind using rows_to_keep
#print(temperatures_ind.loc[rows_to_keep])

# sorting temperatures_ind
print(temperatures_ind.sort_index(level = ["country", "city"], ascending = [True, False]))
