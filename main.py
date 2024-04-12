import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
 
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.manifold import TSNE

tracks = pd.read_csv('data/data_cleaned.csv')

song_vectorizer = CountVectorizer()
song_vectorizer.fit(tracks['genre'])

def get_similarities(song_name, data):

    # Getting vector for the input song.
    text_array1 = song_vectorizer.transform(data[data['name']==song_name]['genres']).toarray()
    num_array1 = data[data['name']==song_name].select_dtypes(include=np.number).to_numpy()

    # We will store similarity for each row of the dataset.
    sim = []
    for idx, row in data.iterrows():
        name = row['name']
        
        # Getting vector for current song.
        text_array2 = song_vectorizer.transform(data[data['name']==name]['genres']).toarray()
        num_array2 = data[data['name']==name].select_dtypes(include=np.number).to_numpy()

        # Calculating similarities for text as well as numeric features
        text_sim = cosine_similarity(text_array1, text_array2)[0][0]
        num_sim = cosine_similarity(num_array1, num_array2)[0][0]
        sim.append(text_sim + num_sim)
        
    return sim

def recommend_songs(song_name, data=tracks):
    # Base case
    if tracks[tracks['name'] == song_name].shape[0] == 0:
        print('This song is either not so popular or you\
        have entered invalid_name.\n Some songs you may like:\n')
        
        for song in data.sample(n=5)['name'].values:
            print(song)
        return

    data['similarity_factor'] = get_similarities(song_name, data)

    data.sort_values(by=['similarity_factor', 'popularity'],
                    ascending = [False, False],
                    inplace=True)

    # First song will be the input song itself as the similarity will be highest.
    return data[['name', 'artists']][2:7]
