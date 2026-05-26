
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
pd.set_option('display.max_columns', None)

data = [
    {'region': 'East South Central', 'state': 'Alabama', 'individuals': 2570.0, 'family_members': 864.0, 'state_pop': 4887681},
    {'region': 'Pacific', 'state': 'Alaska', 'individuals': 1434.0, 'family_members': 582.0, 'state_pop': 735139},
    {'region': 'Mountain', 'state': 'Arizona', 'individuals': 7259.0, 'family_members': 2606.0, 'state_pop': 7158024},
    {'region': 'West South Central', 'state': 'Arkansas', 'individuals': 2280.0, 'family_members': 432.0, 'state_pop': 3009733},
    {'region': 'Pacific', 'state': 'California', 'individuals': 109008.0, 'family_members': 20964.0, 'state_pop': 39461588},
    {'region': 'Mountain', 'state': 'Colorado', 'individuals': 7607.0, 'family_members': 3250.0, 'state_pop': 5691287},
    {'region': 'New England', 'state': 'Connecticut', 'individuals': 2280.0, 'family_members': 1696.0, 'state_pop': 3571520},
    {'region': 'South Atlantic', 'state': 'Delaware', 'individuals': 708.0, 'family_members': 374.0, 'state_pop': 965479},
    {'region': 'South Atlantic', 'state': 'District of Columbia', 'individuals': 3770.0, 'family_members': 3134.0, 'state_pop': 701547},
    {'region': 'South Atlantic', 'state': 'Florida', 'individuals': 21443.0, 'family_members': 9587.0, 'state_pop': 21244317},
    {'region': 'South Atlantic', 'state': 'Georgia', 'individuals': 6943.0, 'family_members': 2556.0, 'state_pop': 10511131},
    {'region': 'Pacific', 'state': 'Hawaii', 'individuals': 4131.0, 'family_members': 2399.0, 'state_pop': 1420593},
    {'region': 'Mountain', 'state': 'Idaho', 'individuals': 1297.0, 'family_members': 715.0, 'state_pop': 1750536},
    {'region': 'East North Central', 'state': 'Illinois', 'individuals': 6752.0, 'family_members': 3891.0, 'state_pop': 12723071},
    {'region': 'East North Central', 'state': 'Indiana', 'individuals': 3776.0, 'family_members': 1482.0, 'state_pop': 6695497},
    {'region': 'West North Central', 'state': 'Iowa', 'individuals': 1711.0, 'family_members': 1038.0, 'state_pop': 3148618},
    {'region': 'West North Central', 'state': 'Kansas', 'individuals': 1443.0, 'family_members': 773.0, 'state_pop': 2911359},
    {'region': 'East South Central', 'state': 'Kentucky', 'individuals': 2735.0, 'family_members': 953.0, 'state_pop': 4461153},
    {'region': 'West South Central', 'state': 'Louisiana', 'individuals': 2540.0, 'family_members': 519.0, 'state_pop': 4659690},
    {'region': 'New England', 'state': 'Maine', 'individuals': 1450.0, 'family_members': 1066.0, 'state_pop': 1339057},
    {'region': 'South Atlantic', 'state': 'Maryland', 'individuals': 4914.0, 'family_members': 2230.0, 'state_pop': 6035802},
    {'region': 'New England', 'state': 'Massachusetts', 'individuals': 6811.0, 'family_members': 13257.0, 'state_pop': 6882635},
    {'region': 'East North Central', 'state': 'Michigan', 'individuals': 5209.0, 'family_members': 3142.0, 'state_pop': 9984072},
    {'region': 'West North Central', 'state': 'Minnesota', 'individuals': 3993.0, 'family_members': 3250.0, 'state_pop': 5606249},
    {'region': 'East South Central', 'state': 'Mississippi', 'individuals': 1024.0, 'family_members': 328.0, 'state_pop': 2981020},
    {'region': 'West North Central', 'state': 'Missouri', 'individuals': 3776.0, 'family_members': 2107.0, 'state_pop': 6121623},
    {'region': 'Mountain', 'state': 'Montana', 'individuals': 983.0, 'family_members': 422.0, 'state_pop': 1060665},
    {'region': 'West North Central', 'state': 'Nebraska', 'individuals': 1745.0, 'family_members': 676.0, 'state_pop': 1925614},
    {'region': 'Mountain', 'state': 'Nevada', 'individuals': 7058.0, 'family_members': 486.0, 'state_pop': 3027341},
    {'region': 'New England', 'state': 'New Hampshire', 'individuals': 835.0, 'family_members': 615.0, 'state_pop': 1353465},
    {'region': 'Mid-Atlantic', 'state': 'New Jersey', 'individuals': 6048.0, 'family_members': 3350.0, 'state_pop': 8886025},
    {'region': 'Mountain', 'state': 'New Mexico', 'individuals': 1949.0, 'family_members': 602.0, 'state_pop': 2092741},
    {'region': 'Mid-Atlantic', 'state': 'New York', 'individuals': 39827.0, 'family_members': 52070.0, 'state_pop': 19530351},
    {'region': 'South Atlantic', 'state': 'North Carolina', 'individuals': 6451.0, 'family_members': 2817.0, 'state_pop': 10381615},
    {'region': 'West North Central', 'state': 'North Dakota', 'individuals': 467.0, 'family_members': 75.0, 'state_pop': 758080},
    {'region': 'East North Central', 'state': 'Ohio', 'individuals': 6929.0, 'family_members': 3320.0, 'state_pop': 11676341},
    {'region': 'West South Central', 'state': 'Oklahoma', 'individuals': 2823.0, 'family_members': 1048.0, 'state_pop': 3940235},
    {'region': 'Pacific', 'state': 'Oregon', 'individuals': 11139.0, 'family_members': 3337.0, 'state_pop': 4181886},
    {'region': 'Mid-Atlantic', 'state': 'Pennsylvania', 'individuals': 8163.0, 'family_members': 5349.0, 'state_pop': 12800922},
    {'region': 'New England', 'state': 'Rhode Island', 'individuals': 747.0, 'family_members': 354.0, 'state_pop': 1058287},
    {'region': 'South Atlantic', 'state': 'South Carolina', 'individuals': 3082.0, 'family_members': 851.0, 'state_pop': 5084156},
    {'region': 'West North Central', 'state': 'South Dakota', 'individuals': 836.0, 'family_members': 323.0, 'state_pop': 878698},
    {'region': 'East South Central', 'state': 'Tennessee', 'individuals': 6139.0, 'family_members': 1744.0, 'state_pop': 6771631},
    {'region': 'West South Central', 'state': 'Texas', 'individuals': 19199.0, 'family_members': 6111.0, 'state_pop': 28628666},
    {'region': 'Mountain', 'state': 'Utah', 'individuals': 1904.0, 'family_members': 972.0, 'state_pop': 3153550},
    {'region': 'New England', 'state': 'Vermont', 'individuals': 780.0, 'family_members': 511.0, 'state_pop': 624358},
    {'region': 'South Atlantic', 'state': 'Virginia', 'individuals': 3928.0, 'family_members': 2047.0, 'state_pop': 8501286},
    {'region': 'Pacific', 'state': 'Washington', 'individuals': 16424.0, 'family_members': 5880.0, 'state_pop': 7523869},
    {'region': 'South Atlantic', 'state': 'West Virginia', 'individuals': 1021.0, 'family_members': 222.0, 'state_pop': 1804291},
    {'region': 'East North Central', 'state': 'Wisconsin', 'individuals': 2740.0, 'family_members': 2167.0, 'state_pop': 5807406},
    {'region': 'Mountain', 'state': 'Wyoming', 'individuals': 434.0, 'family_members': None, 'state_pop': None},
]

homelessness_pd = pd.DataFrame(data)
homelessness_pd.loc[homelessness_pd['state'] == 'Wyoming', ['family_members', 'state_pop']] = [205.0, 577601]

# In this dataframe, individual column is the number of homeless that's not part of a family with children.
# The family_members column is the number of homeless that's part of a family
# The state_pop column is the states' total population

homelessness_pd['total'] = homelessness_pd['individuals'] + homelessness_pd['family_members']

homelessness_pd['p_homeless'] = homelessness_pd['total'] / homelessness_pd['state_pop']

homelessness_pd['indiv_per_10k'] = 10000 * homelessness_pd['individuals'] / homelessness_pd['state_pop']

high_homelessness_pd = homelessness_pd[homelessness_pd['indiv_per_10k'] > 20]

high_homelessness_pd_srt = high_homelessness_pd.sort_values('indiv_per_10k', ascending = False)

result_pd = high_homelessness_pd_srt[['state', 'indiv_per_10k']]

print(result_pd)