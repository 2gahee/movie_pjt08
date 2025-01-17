from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe
from .models import Movie, Genre
import requests
from .config import weather_genre_map  # config.py에서 weather_genre_map 가져오기
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    genres = Genre.objects.all()
    context = {'movies': movies,
               'genres': genres}
    return render(request, 'movies/index.html', context)

@api_view(['GET'])
def filter_genre(request):
    genre_name = request.GET.get('genre')
    if genre_name:
        movies = Movie.objects.filter(genres__name=genre_name)
    else:
        movies = Movie.objects.all()
    
    movies_data = [{'title': movie.title} for movie in movies]
    return JsonResponse({'movies': movies_data})


@require_safe
def recommend(request):
    return render(request, 'movies/recommend.html')

def get_weather(city):
    # OpenWeatherMap API에서 날씨 정보를 가져오는 함수
    api_key = 'f8347bfb4ea81ec6f58c126428ff773c'  # 발급받은 API 키로 대체
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
   
    data = response.json()
    # print(data)
    return data

def recommend_movie_by_weather(request, city):
    # 1. 날씨 데이터 가져오기
    weather_data = get_weather(city)
    
    # 2. 날씨 상태 확인
    weather_condition = weather_data['weather'][0]['main']
    
    # 3. 날씨 상태에 맞는 장르 pk 찾기
    genre_pk = weather_genre_map.get(weather_condition, 12)  # 기본값으로 모험 (pk=12) 설정
    
    # 4. 해당 장르에 맞는 영화 필터링
    genre = Genre.objects.get(pk=genre_pk)
    recommended_movies = Movie.objects.filter(genres=genre)

    # 5. 영화 추천 결과를 템플릿으로 전달
    context = {
        'city': city,
        'weather_condition': weather_condition,
        'recommended_movies': recommended_movies,
    }
    return render(request, 'movies/recommendations.html', context)

