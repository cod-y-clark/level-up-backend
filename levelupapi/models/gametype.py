from django.db import models

class GameType(models.Model):
    gametype = models.CharField(max_length=50)