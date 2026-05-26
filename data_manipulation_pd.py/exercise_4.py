
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)

movies = {
    "title": [
        "Shadow Night", "Fast Track", "Ocean Deep", "Pixel Wars",
        "Dream City", "Code Zero", "Sky Hunter", "Last Signal"
    ],
    "genre": [
        "Action", "Action", "Drama", "Sci-Fi",
        "Drama", "Sci-Fi", "Action", "Drama"
    ],
    "rating": [8.5, 7.8, 9.1, 8.9, 7.5, 9.3, 8.0, 8.7],
    "views_millions": [120, 95, 140, 110, 80, 150, 100, 130],
    "subscription_type": [
        "Premium", "Basic", "Premium", "Premium",
        "Basic", "Premium", "Basic", "Premium"
    ]
}

movies_df = pd.DataFrame(movies)

#task 1
print(movies_df.head())
print()

#task 2
print(movies_df[['title', 'genre', 'rating']])
print()

#task 3
print(movies_df.columns)
print()

#task 4
print(movies_df[movies_df['rating'] > 8.5])
print()

#task 5
print(movies_df[(movies_df['genre'] == 'Drama') & 
                (movies_df['views_millions'] > 100)])
print()

#task 6
print(movies_df[movies_df['subscription_type'] == 'Premium'])
print()

#task 7
print(movies_df.sort_values(by='rating', ascending = False))
print()

#task 8
print(movies_df.sort_values(by=['genre', 'views_millions'], 
                            ascending = [True, False]))
print()

#task 9
movies_df['popularity_score'] = movies_df['rating'] * movies_df['views_millions']
print(movies_df.head())
print()

#task 10
movies_df['hit_movie'] = np.where(movies_df['views_millions'] >= 120, 'Yes', 'No')
print(movies_df.head())

#task 11
movies_df['rating_category'] = np.where(movies_df['rating'] >= 9, 'Top Rated', 'Regular')
print(movies_df.head())
print()

#task 12
print(movies_df['rating'].mean())
print()

#task 13
print(movies_df.groupby('genre')['views_millions'].sum())
print()

#task 14
print(movies_df.groupby('subscription_type')['rating'].mean())
print()

#task 15
print(movies_df['genre'].value_counts())
print()

#task 16
print(movies_df.loc['title', 'rating'])
print()