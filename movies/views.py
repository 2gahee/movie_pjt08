from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe
from .models import Movie, Genre
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
def recommended(request):
    pass
