
import numpy as np
import pandas as pd

pd.set_option('display.max_columns', None)

orders = {
    "customer": [
        "Anna", "Brian", "Cathy", "Daniel",
        "Ella", "Frank", "Grace", "Henry"
    ],
    "restaurant": [
        "Burger Hub", "Pizza Spot", "Burger Hub", "Sushi Place",
        "Pizza Spot", "Burger Hub", "Sushi Place", "Pizza Spot"
    ],
    "food_category": [
        "Fast Food", "Italian", "Fast Food", "Japanese",
        "Italian", "Fast Food", "Japanese", "Italian"
    ],
    "order_amount": [350, 500, 200, 800, 650, 400, 900, 550],
    "delivery_time": [25, 40, 20, 50, 35, 30, 45, 38],
    "rating": [5, 4, 4, 5, 3, 4, 5, 4],
    "city": [
        "Manila", "Cebu", "Manila", "Davao",
        "Cebu", "Manila", "Davao", "Cebu"
    ]
}

orders_df = pd.DataFrame(orders)

# 1. Create a new column named tip_amount (10% of order_amount)
orders_df['tip_amount'] = orders_df['order_amount'] * 0.10

# 2. Create new col "total_bill"
orders_df['total_bill'] = orders_df['order_amount'] + orders_df['tip_amount']

# 3. Create fast_delivery col (deliveries equal or under 30 mins)
orders_df['fast_delivery'] = np.where(orders_df['delivery_time']<= 30, 'Yes', 'No')

# 4. Create rating_label (excellent if equal to 5, average if not)
orders_df['rating_label'] = np.where(orders_df['rating'] == 5, 'Excellent', 'Average')

# 5. Average order amount
avg_order_amt = orders_df['order_amount'].mean()

# 6. total sales per restaurant (groupby)
total_sales_per_restaurant = orders_df.groupby('restaurant')['order_amount'].sum()

# 7. average delivery_time per city
avg_del_time_per_city = orders_df.groupby('city')['delivery_time'].mean()

# 8. mean AND max order amount per food category
mean_max_food_category = orders_df.groupby('food_category')['order_amount'].agg(['mean', 'max'])

# 9. display rows 2 to 5
print(orders_df.iloc[2:5])
print("\n" + "="*80)

# 10. display customer, restaurant, total_bill cols only
orders_df_srt = orders_df.loc[:, # select all rows first by colon
                              ['customer', 
                               'restaurant', 
                               'total_bill']
                               ] # then select the columns you want to display
print(orders_df_srt)
print("\n" + "="*80)

# 11. show custs from Manila w/ rating 5
slicer = (
    # create a slicer first
    orders_df['city'] == 'Manila') & (
        orders_df['rating'] == 5)

manila_five_star = orders_df.loc[slicer, ['customer', 'restaurant']]

print(manila_five_star)
print("\n" + "="*80)

# 12. Find the top restaurant/s
top_restaurants = total_sales_per_restaurant[
    total_sales_per_restaurant == total_sales_per_restaurant.max()
]

print(top_restaurants)
print("\n" + "="*80)

# 13. fastest city in avg_del
fastest_avg_del_city = avg_del_time_per_city[avg_del_time_per_city == 
                                             avg_del_time_per_city.max()]

print(fastest_avg_del_city)
print()

# 14. total orders per restaurant
print(orders_df['restaurant'].value_counts())
print()
