from django.shortcuts import render
from .models import Movie
import random


def home(request):
    movies = list(Movie.objects.all())
    rand = random.sample(movies,12)
    return render(request, 'movies/home.html', {'movies':rand})

def movie_details(request, id):
    movie = Movie.objects.get(id=id)
    return render(request,'movies/detail.html',{'movie':movie})
