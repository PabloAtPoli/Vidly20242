from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Movie

# Create your views here.
from django.http import HttpResponse

def index(request):
    """The home page for Movies"""

    movies = Movie.objects.all()
    # output = ', '.join([m.title for m in movies])
    return render(request, 'movies/index.html', {'movies': movies})
    # return render(request, 'index.html', {'movies': movies})
def detail(request, movie_id):
    """Show a single movie and its details"""

    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})


