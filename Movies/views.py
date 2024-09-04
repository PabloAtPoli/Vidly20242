
# Create your views here.
from django.http import HttpResponse
def index(request):
    """The home page for Movies"""
    return HttpResponse("Hello, world. You're at the Movies index.")

