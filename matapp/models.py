from random import choice
from django.db import models
from django.forms import CharField

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=8, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    User = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    ingredients = models.CharField(max_length=400, null=True)

    def __str__(self):
        return self.title
