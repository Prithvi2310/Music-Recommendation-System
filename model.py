import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Load the dataset
data = pd.read_csv("data/data_cleaned.csv")

# Preprocess the data
data['artists'] = data['artists'].apply(lambda x: x.replace("[", "").replace("]", "").replace("'", ""))
data['genre'] = data['genre'].apply(lambda x: x.lower())

# Create TF-IDF matrix
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['artists'] + ' ' + data['genre'])

# Compute the cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Function to get recommendations
def get_recommendations(title):
    if title not in data['name'].unique():
        data_new = data.sample(n=5)['name'].tolist()
        return("This song is either not so popular or you have entered a song out of our list.", data_new)
    else:
        idx = data[data['name'] == title].index[0]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:11]
        song_indices = [i[0] for i in sim_scores]
        return data.iloc[song_indices]['name']

# Example usage
fav_song = "Shape of You"
recommendations = get_recommendations(fav_song)
print("Recommended songs similar to", fav_song, ":")
print(recommendations)
