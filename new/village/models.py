from django.db import models

# Create your models here
class village(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    population = models.IntegerField()

    def __str__(self):
        return self.name
    
class People(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    village = models.ForeignKey('village', on_delete=models.CASCADE)

    def __str__(self):
        return self.name