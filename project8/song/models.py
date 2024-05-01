from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    duration = models.DurationField()

    def __str__(self):
        return self.title
from django.db import models

class Playlist(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.name
