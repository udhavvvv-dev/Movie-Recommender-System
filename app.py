import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poste(movie_id):
    responce = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = responce.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

#making recommend function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0] #its function that find index value from table
    distances = similarity[movie_index] #measuring distance of array
    # For next step we sort the list with emurate function so it convert with tuple 
    # Then it will reverse the list and then its will give 5 simmilar cordinate suggestion using lambda function
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6] 
    
    recommended_movie = []
    recommended_movie_posters = []
    for i in movies_list:
    #now we are try to fetch the poster of movie with movie id
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movie.append(movies.iloc[i[0]].title)
        #fetch poster from API
        recommended_movie_posters.append(fetch_poste(movie_id))
    return recommended_movie,recommended_movie_posters

# assign .pkl file to the frontend to show the list of titles of movies
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
    
#import statemnt for similarity
similarity = pickle.load(open('similarity.pkl','rb'))

# main heading for project
st.title('Movie Recommender System')

#creataing a search and selectbox two in one
selected_movie_name = st.selectbox(
'How Would you like to be contacted?',
movies['title'].values) 

# adding button to the screen
if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])
        
    with col5:
        st.text(names[4])
        st.image(posters[4]) 