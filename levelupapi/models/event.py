from django.db import models
from levelupapi.models.game import Game
from levelupapi.models.gamer import Gamer

class Event(models.Model):
    
    creator = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    date = models.DateField(default="2021-08-14")
    time = models.TimeField(default="19:30")