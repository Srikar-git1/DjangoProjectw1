from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    release = models.IntegerField()
    overview = models.TextField()
    genre = models.CharField(max_length=150)
    link = models.URLField()
