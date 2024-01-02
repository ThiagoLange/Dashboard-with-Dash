# import packages
import pandas as pd

# load data
df = pd.read_csv('data/netflix_titles.csv')

# fill missing values
df['director'].fillna('No director', inplace= True)
df['cast'].fillna('No cast', inplace= True)
df['country'].fillna('No country', inplace= True)

# drop missing and duplicates values
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# strip whitespaces from the data
df['data_added'] = pd.to_datetime(df['date_added'].str.strip())

# Save tthe clean dataset
df.to_csv('data/clean-netflix_titles.csv', index=False)

