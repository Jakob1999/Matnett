from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def browse(req):
    return render(req, 'matapp/browse.html')


def myrecipes(request):
    return render(request, 'matapp/myrecipes.html')


def profile(request):
    return render(request, 'matapp/profile.html')


def alert(request):
    return render(request, 'matapp/alert.html')


def recipe(request):
    return render(request, 'matapp/recipe.html')


def addRecipe(request):
    return render(request, 'matapp/addRecipe.html')
