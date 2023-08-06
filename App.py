import streamlit as st
import pickle
import pandas as pd
import requests

intial_count = 6
def get_posters(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    res = requests.get(url)
    data = res.json()
    img_url = "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    return img_url

def recommend(movie):
    movie_index = movies[movies['original_title'] == movie].index[0]
    # distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:intial_count+1]
    recommended_movie_names = []
    movie_pics = []
    for i in movie_list:
        temp_list = []
        temp_list.append(movies.iloc[i[0]].original_title)
        temp_list.append(movies.iloc[i[0]].release_year)
        recommended_movie_names.append(temp_list)
        temp2_list  = []
        temp2_list.append(movies.iloc[i[0]].release_year)
        temp2_list.append(get_posters(movies.iloc[i[0]].id))
        movie_pics.append(temp2_list)
    recommended_movie_names =  sorted(recommended_movie_names,reverse=True,key=lambda x:x[1])
    movie_pics = sorted(movie_pics, reverse=True, key= lambda x:x[0])
    return recommended_movie_names, movie_pics
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
    'Select a Movie',
    movies['original_title'].values)

if st.button('Find Similar Movies'):
    recommendations,movie_pics = recommend(selected_movie_name)
    count=0
    for i in range(0,intial_count//3):
        col1,col2,col3 = st.columns(3)
        with col1:
            st.image(movie_pics[count][1])
            st.subheader(recommendations[count][0]+" ({})".format(recommendations[i+0][1]))
            count+=1
        with col2:
            st.image(movie_pics[count][1])
            st.subheader(recommendations[count][0]+" ({})".format(recommendations[i+0][1]))
            count+=1
        with col3:
            st.image(movie_pics[count][1])
            st.subheader(recommendations[count][0]+" ({})".format(recommendations[i+0][1]))
            count+=1




