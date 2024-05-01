from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    release_date = models.DateField()
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Actor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    films = models.ManyToManyField(Film)

    def __str__(self):
        return self.name
