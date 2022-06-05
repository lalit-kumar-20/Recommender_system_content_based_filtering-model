from cProfile import run
from unicodedata import name
import streamlit as st
import pickle
import pandas  as pd
import requests
from PIL import Image
def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=2c42ca7a70792a5b94f0de18fc3640a2&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path'] 
def fetch_overview(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=2c42ca7a70792a5b94f0de18fc3640a2&language=en-US'.format(movie_id))
    data=response.json()
    return data['overview']
def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_listt=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:11]
    recommended_movies=[]
    recommended_movies_poster=[]
    overvieww=[]
    for i in movies_listt:
         movie_id=movies.iloc[i[0]].movie_id
         
         recommended_movies.append(movies.iloc[i[0]].title)
         #fetching poster from API
         recommended_movies_poster.append(fetch_poster(movie_id))
         overvieww.append(fetch_overview(movie_id))
    return recommended_movies,recommended_movies_poster ,overvieww  
     

movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
 'How would you like to be contacted?',
movies['title'].values)

if st.button('Recommend'):
    
    names,posters,overv = recommend(selected_movie_name)
    
    col1, col2, col3,col4,col5= st.columns(5)
    with col1:
         st.image(posters[0])
         st.subheader(names[0])
         with st.expander("See explanation"):
              st.write('Overview: ')
              st.write(overv[0])
    with col2:
         st.image(posters[1])
         st.subheader(names[1])
         with st.expander("See explanation"):
              st.write(overv[1])

    with col3:
         st.image(posters[2])
         st.subheader(names[2])
         with st.expander("See explanation"):
              st.write(overv[2])
    
    with col4:
         st.image(posters[3])
         st.subheader(names[3])
         with st.expander("See explanation"):
              st.write(overv[3])
    
    with col5:
         st.image(posters[4])
         st.subheader(names[4])
         with st.expander("See explanation"):
              st.write(overv[4])
  
    