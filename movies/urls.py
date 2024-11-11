from django.urls import path
from . import views

app_name = "movies"
urlpatterns = [
    path("", views.index, name="index"),
    path("filter-genre/", views.filter_genre, name="filter_genre"),
    path("recommend/", views.recommend, name="recommend"),
    path('recommend/<str:city>/', views.recommend_movie_by_weather, name='recommend_movie'),
]
