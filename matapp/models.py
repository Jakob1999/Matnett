from msilib.schema import CheckBox
from random import choice
from tkinter import Widget
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
    #User = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    ingredients = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    avatar = models.ImageField(null=True, default="defaultRecipe.jpg")

    def __str__(self):
        return self.title
    
    def ingredientsFormat(self):
        return self.ingredients.split('\n')