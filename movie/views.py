from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

class MoviePageNumberPagination(PageNumberPagination):
	page_size = 2

from .serializers import MovieSerializer, ActorSerializer, ReviewSerializer
from .models import Movie, Actor, Review
# Create your views here.

class MoviePageNumberPagination(PageNumberPagination):
    page_size = 2

class MovieList(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = MoviePageNumberPagination
        
class MovieDetail(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
class ActorList(ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class ActorDetail(RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    
class ReviewList(ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        movie = get_object_or_404(Review, pk=self.kwargs.get('pk'))
        return Review.objects.filter(movie=movie)
    
    def perform_create(self, serializer):
        movie = get_object_or_404(Movie, pk=self.kwargs.get('pk'))
        serializer.save(movie=movie)
