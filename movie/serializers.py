from rest_framework import serializers
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator
from django.core.validators import MaxLengthValidator, MinLengthValidator

from .models import Movie, Actor, Review

class MovieSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[UniqueValidator(
        queryset=Movie.objects.all(),
        message='이미 존재하는 영화 이름입니다.'
    )])
    overview = serializers.CharField(validators=[MaxLengthValidator(limit_value=300), MinLengthValidator(limit_value=10)])
    class Meta:
        model = Movie
        fields = ['id', 'name', 'opening_date', 'running_time', 'overview']

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name', 'gender', 'birth_date']
    
class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(many=True, read_only=True)
    class Meta:
        model = Review
        fields = ['id', 'movie', 'username', 'star', 'comment', 'created']