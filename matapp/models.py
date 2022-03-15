from django.db import models
from django.forms import CharField
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Recipe(models.Model):

    Host = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    ingredients = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    avatar = models.ImageField(null=True, default="defaultRecipe.jpg")
    favorite = models.ManyToManyField(User, related_name="favorite", blank=True)
    handleliste = models.ManyToManyField(User, related_name="handleliste", blank=True)
    
    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title
    
    def ingredientsFormat(self):
        return self.ingredients.split('\n')

