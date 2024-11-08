from .models import Movie, Genre
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    class MovieGenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = '__all__'
    genre = MovieGenreSerializer(read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'