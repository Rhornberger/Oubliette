from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Character(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    charclass = models.CharField(max_length=50)
    diety = models.CharField(max_length=50)