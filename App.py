import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['original_title'] == movie].index[0]
    # distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:8]

    recommended_movie_names = []
    for i in movie_list:
        recommended_movie_names.append(movies.iloc[i[0]].original_title)

    return recommended_movie_names

movies_dict = pickle.load(open('movie_list.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies['original_title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)

