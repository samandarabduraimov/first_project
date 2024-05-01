from django.db import models

class Tree(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    age = models.IntegerField()
    height = models.FloatField()

    def __str__(self):
        return self.name
class Forest(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    trees = models.ManyToManyField(Tree)

    def __str__(self):
        return self.name