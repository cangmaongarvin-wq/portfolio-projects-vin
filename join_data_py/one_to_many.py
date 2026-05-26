
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)

licenses = pd.read_csv('join_data_py/licenses.csv', index_col= 0)
biz_owners = pd.read_csv('join_data_py/business_owners.csv', index_col=0)

licenses_owners = licenses.merge(biz_owners, on='account', suffixes=('_cen', '_own'))

# You can groupby without the other argument with squarebrackets??!!
counted_df = licenses_owners.groupby('title').agg({'account':'count'})

# because I want it sorted
sorted_df = counted_df.sort_values(by='account', ascending=False)