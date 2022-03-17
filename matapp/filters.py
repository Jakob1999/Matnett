import django_filters
from .models import *

class RecipeFilter(django_filters.FilterSet):
    class Meta:
        model = Recipe
        fields = ['kategorier']