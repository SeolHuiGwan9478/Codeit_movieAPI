from rest_framework import serializers
from django.core.validators import MaxLengthValidator, MinLengthValidator

from .models import Movie, Actor

class MovieSerializer(serializers.ModelSerializer):
    overview = serializers.CharField(validators=[MaxLengthValidator(limit_value=300), MinLengthValidator(limit_value=10)])
    class Meta:
        model = Movie
        fields = ['id', 'name', 'opening_date', 'running_time', 'overview']

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name', 'gender', 'birth_date']