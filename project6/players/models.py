from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    team = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class MatchResult(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    date = models.DateField()
    opponent = models.CharField(max_length=100)
    score = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.player.name} - {self.date}"