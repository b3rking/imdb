from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Movie
# Create your views here.

def movie_list(request):

    movies = Movie.objects.all()
    data = {
        'movies': list(movies.values())
    }
    return JsonResponse(data, safe=False)

def movie_detail(request, pk):

    movie = Movie.objects.get(pk=pk)

    data = {
        'name': movie.name,
        'description': movie.description,
        'published': movie.active
    }

    return JsonResponse(data)