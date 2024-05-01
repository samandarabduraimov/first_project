from django.db import models

class Singer(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    birth_date = models.DateField()
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title
