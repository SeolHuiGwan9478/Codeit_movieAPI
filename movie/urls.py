from django.urls import path
from .views import *

urlpatterns = [
    path('movies', movie_list),
]