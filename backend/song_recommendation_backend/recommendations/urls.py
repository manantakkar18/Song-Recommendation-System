from django.urls import path
from .views import *

urlpatterns = [
    path('recommend_artist/', recommend_artist, name='recommend_artist'),
    path('recommend_playlist/', recommend_playlist, name='recommend_playlist'),
    path('recommend_song/', recommend_song, name='recommend_song'),
    path('search/', search_from_dataset, name='search_from_dataset'),
    path('', trending_songs, name='trending_songs'),
    
]
