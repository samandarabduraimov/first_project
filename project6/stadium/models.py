from django.db import models

class Stadium(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    capacity = models.IntegerField()
    opened = models.DateField()

    def __str__(self):
        return self.name
class Match(models.Model):
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    date = models.DateField()
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    result = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} at {self.stadium.name}"