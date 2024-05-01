from django.db import models

# Create your models here
class city(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    population = models.IntegerField()

    def __str__(self):
        return self.name
    
class People(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.ForeignKey('City', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
