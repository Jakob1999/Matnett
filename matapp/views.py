from django.shortcuts import render
from django.http import HttpResponse

from matapp.models import *
# Create your views here.


def browse(request):
    recipe = Recipe.objects.all()
    return render(request, 'matapp/browse.html', {'recipe': recipe})


def myrecipes(request):
    return render(request, 'matapp/myrecipes.html')


def profile(request):
    return render(request, 'matapp/profile.html')


def alert(request):
    return render(request, 'matapp/alert.html')


def recipe(request, PK):
    return render(request, 'matapp/recipe.html')


def addRecipe(request):
    return render(request, 'matapp/addRecipe.html')
