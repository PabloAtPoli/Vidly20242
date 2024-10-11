from django.contrib import admin
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html
from .models import Genre, Movie


class CountMoviesFilter(admin.SimpleListFilter):
    title = 'Count Movies'
    parameter_name = 'count_movies'

    def lookups(self, request, model_admin):
        return [
            ('0-1', '0 to 1'),
            ('1-5', '1 to 5'),
            ('5+', 'More than 5'),
        ]

    def queryset(self, request, queryset):
        if self.value() == '0-1':
            return queryset.annotate(_count_movies=Count("movie")).filter(_count_movies__lte=1)
        if self.value() == '1-5':
            return queryset.annotate(_count_movies=Count("movie")).filter(_count_movies__gt=1, _count_movies__lte=5)
        if self.value() == '5+':
            return queryset.annotate(_count_movies=Count("movie")).filter(_count_movies__gt=5)

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'count_movies')
    search_fields = ['name']
    list_filter = (CountMoviesFilter,)  # Added count_movies filter

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(_count_movies=Count("movie"))  # Annotate the count of movies
        return queryset

    def count_movies(self, obj):
        url = reverse('admin:Movies_movie_changelist')
        return format_html('<a href="{}?genre={}">{}</a>', url, obj.id, obj._count_movies)
    count_movies.short_description = 'Count Movies'
    count_movies.admin_order_field = '_count_movies'  # Make count_movies sortable

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'release_year', 'number_in_stock', 'daily_rate', 'genre', 'date_created')
    search_fields = ['title', 'release_year']
    list_filter = ('genre',)

# Register your models here.

admin.site.site_header = "Vidly Administration"
admin.site.site_title = "Vidly Administration"
admin.site.index_title = "Welcome to Vidly Administration"    

admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
