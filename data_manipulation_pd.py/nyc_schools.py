
import numpy as np
import pandas as pd

pd.set_option('display.max_column', None)

schools = pd.read_csv('data_manipulation_pd.py/schools.csv')

best_math_schools = schools[schools["average_math"] >= 640][
    ["school_name", "average_math"]
].sort_values("average_math", ascending=False)

schools['total_SAT'] = schools['average_math'] + schools['average_reading'] + schools['average_writing']

top_10_schools = schools[['school_name', 'total_SAT']].sort_values('total_SAT', ascending = False)

# We group the schools by borough before getting the largest std
borough_df = schools.groupby('borough').agg(
    num_schools=('school_name', 'count'),
    average_SAT=('total_SAT', 'mean'),
    std_SAT=('total_SAT', 'std')
)

# We round values to 2 decimal places
borough_df = borough_df.round(2)

# FInd the borough with largest std_SAT
largest_std_dev = borough_df.sort_values('std_SAT', ascending=False).head(1)

print(largest_std_dev)