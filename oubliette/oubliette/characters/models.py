from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Character(models.Model):
    player_name = models.ForeignKey(User, on_delete=models.CASCADE)
    character_name = models.CharField(max_length=50)
    charclass = models.CharField(max_length=50)
    diety = models.CharField(max_length=50)
    race = models.CharField(max_length=50)
    homeland = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    height = models.CharField(max_length=50)
    hair_color = models.CharField(max_length=50)
    eye_color = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.player_name} {self.character_name}'