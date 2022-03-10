from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):

    Host = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    ingredients = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    avatar = models.ImageField(null=True, default="defaultRecipe.jpg")
    created = models.DateTimeField(auto_now_add=True)
    favorite = models.ManyToManyField(User, related_name="favorite", blank=True)
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
    
    def ingredientsFormat(self):
        return self.ingredients.split('\n')