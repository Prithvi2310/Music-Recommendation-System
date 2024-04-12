import pandas as pd

tracks = pd.read_csv('data/data.csv')

def data_cleaning(tracks):

    tracks.dropna(inplace = True)

    tracks = tracks.drop(['id', 'id_artists'], axis = 1)

    tracks = tracks.sort_values(by=['popularity'], ascending=False)
    tracks.drop_duplicates(subset=['name'], keep='first', inplace=True)

    floats = []

    for col in tracks.columns:
        if tracks[col].dtype == 'float':
            floats.append(col)
        
    tracks = tracks.sort_values(by=['popularity'], ascending=False)

    tracks.to_csv('data/data_cleaned.csv')

data_cleaning(tracks)