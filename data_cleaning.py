import pandas as pd

tracks = pd.read_csv('data/data.csv')

tracks = tracks.drop(['id', 'id_artists'], axis = 1)

tracks.to_csv('data/data_cleaned.csv')