import streamlit as st
import pandas as pd
import numpy as np
from surprise import Dataset, Reader, SVD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -----------------------------
# Load Data
# -----------------------------
ratings = pd.read_csv("ml-latest-small/ratings.csv")
movies = pd.read_csv("ml-latest-small/movies.csv")
tags = pd.read_csv("ml-latest-small/tags.csv")

# Collaborative Filtering
reader = Reader(rating_scale=(0.5, 5))
data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)
trainset = data.build_full_trainset()
cf_model = SVD()
cf_model.fit(trainset)

# Content-Based (genres + tags)
movies['tags'] = movies['movieId'].map(
    lambda mid: " ".join(tags[tags['movieId'] == mid]['tag'].astype(str))
)
movies['features'] = movies['genres'].fillna('') + " " + movies['tags'].fillna('')

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['features'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
movie_indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()

# -----------------------------
# Recommendation Functions
# -----------------------------
def recommend_by_genre(genre, top_n=5):
    genre_movies = movies[movies['genres'].str.contains(genre, case=False)]
    return genre_movies.sample(min(top_n, len(genre_movies)))

def recommend_by_movie(title, top_n=5):
    if title not in movie_indices:
        return []
    idx = movie_indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    movie_indices_list = [i[0] for i in sim_scores]
    return movies.iloc[movie_indices_list]

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🎬 Movie Recommender")

mode = st.radio("Choose Recommendation Mode:", ["By Genre", "By Movie Title"])
top_n = st.slider("Number of recommendations", 1, 10, 5)

if mode == "By Genre":
    genre = st.selectbox("Select Genre:", ["Drama", "Comedy", "Action", "Romance", "Thriller"])
    if st.button("Get Recommendations"):
        recs = recommend_by_genre(genre, top_n)
        st.write(recs[['title', 'genres']])

elif mode == "By Movie Title":
    title = st.text_input("Enter Movie Title:")
    if st.button("Get Recommendations"):
        recs = recommend_by_movie(title, top_n)
        if len(recs) > 0:
            st.write(recs[['title', 'genres']])
        else:
            st.warning("Movie not found in dataset.")
