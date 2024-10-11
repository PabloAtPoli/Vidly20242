from django.utils import timezone
from django.db import models

class Genre(models.Model):
    list_display = ('ID', 'name')
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)
    
    
class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
# genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title + " " + str(self.release_year) + " " + str(self.number_in_stock) + " " + str(self.daily_rate) + " " + str(self.genre) + " " + str(self.date_created)

