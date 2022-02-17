from django.shortcuts import render, redirect
from django.http import HttpResponse

from matapp.models import *
from .forms import RecipeForm
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


def recipe(request, pk):
    current = Recipe.objects.get(id=pk)
    return render(request, 'matapp/recipe.html', {'current': current})


def addRecipe(request):
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'matapp/addRecipe.html', context)

def editRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    form = RecipeForm(instance=recipe)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid:
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'matapp/addRecipe.html', context)