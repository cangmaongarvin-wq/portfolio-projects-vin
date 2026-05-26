
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

netflix_df = pd.read_csv("intermediate_python/netflix_data.csv")

years = netflix_df[(netflix_df["release_year"].between(1990, 1999)) & (netflix_df["type"] == "Movie")][["release_year", "duration", "type", "genre"]]

max_duration = years["duration"].mode()[0]

short_movie_count = ((years["duration"] < 90) & (years["genre"] == "Action")).sum()
print(short_movie_count)
