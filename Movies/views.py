from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

# Create your views here.
from django.http import HttpResponse
def index(request):
    """The home page for Movies"""

    movies = Movie.objects.all()
    # output = ', '.join([m.title for m in movies])
    return render(request, 'movies/index.html', {'movies': movies})

