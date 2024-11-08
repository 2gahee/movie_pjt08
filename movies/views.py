from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe
from .models import Movie, Genre
from .serializers import MovieSerializer, GenreSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@require_safe
# @api_view
def index(request):
    movies = Movie.objects.all()
    # serializer = MovieSerializer(movies)
    context = {
        'moviesdata' : movies
    }
    return render(request, 'movies/index.html', context)

@api_view(['GET'])
def filter_genre(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        genres = Genre.objects.all()
        movies_serializer = MovieSerializer(movies, many=True)
        genres_serializer = GenreSerializer(genres, many=True)
        context = {
            'moviesdata' : movies_serializer.data,
            'genresdata' : genres_serializer.data
        }
        return Response(context)


@require_safe
def recommended(request):
    pass
