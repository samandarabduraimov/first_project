from django.db import models

class Flower(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    blooming_season = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Garden(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    flowers = models.ManyToManyField(Flower)

    def __str__(self):
        return self.name