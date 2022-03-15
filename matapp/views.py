
from email.mime import image
from importlib.metadata import requires
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import admin
from matapp.models import *
from .forms import RecipeForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def loginPage(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        Username = request.POST.get('username')
        Password = request.POST.get('password')

        try:
            user = User.objects.get(username=Username)
        except:
            messages.error(request, 'Bruker finnes ikke')
        user = authenticate(request, username=Username, password=Password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
             messages.error(request, 'Brukernavn eller passord finnes ikke')

    context = {'page':page}
    return render(request, 'matapp/registration_login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerUser(request):
    page = 'register'
    RegForm = UserCreationForm()

    if request.method == 'POST':
        RegForm = UserCreationForm(request.POST)
        if RegForm.is_valid:
            user = RegForm.save(commit=False)
            RegForm.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Noe gikk galt under registrering :(')
    
    context = {'RegForm':RegForm}
    return render(request, 'matapp/registration_login.html', context)

@login_required(login_url='login')
def browse(request):
    recipe = Recipe.objects.all()
    context = {'recipe':recipe}
    return render(request, 'matapp/recipes.html', context)


@login_required
def addFavorite(request, pk):
    fav = get_object_or_404(Recipe, id=pk)
    if fav.favorite.filter(id=request.user.id).exists():
        fav.favorite.remove(request.user.id)
    else:
        fav.favorite.add(request.user.id)
    return redirect('home')

@login_required(login_url='login')
def favorites(request, pk):
    bruker = User.objects.get(id=pk)
    recipes = Recipe.objects.all()
    context = {'bruker':bruker, 'recipes':recipes}
    return render(request, 'matapp/favorites.html', context)


@login_required(login_url='login')
def profile(request, pk):
    bruker = User.objects.get(id=pk)
    recipes = Recipe.objects.all()
    context = {'bruker':bruker, 'recipes':recipes}
    return render(request, 'matapp/profile.html', context)


@login_required(login_url='login')
def myRecipes(request, pk):
    bruker = User.objects.get(id=pk)
    recipes = Recipe.objects.all()
    context = {'bruker':bruker, 'recipes':recipes}
    return render(request, 'matapp/myrecipes.html', context)





def alert(request):
    return render(request, 'matapp/alert.html')


@login_required(login_url='login')
def recipe(request, pk):
    current = Recipe.objects.get(id=pk)
    return render(request, 'matapp/recipe.html', {'current': current})


@login_required(login_url='login')
def addRecipe(request):
    form = RecipeForm()
    
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid:
            form.instance.Host = request.user
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'matapp/addRecipe.html', context)


@login_required(login_url='login')
def editRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    form = RecipeForm(instance=recipe)

    if request.user != recipe.Host:
        return HttpResponse('Du får ikke lov')

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid:
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'matapp/addRecipe.html', context)


@login_required(login_url='login')
def deleteRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)

    if request.user != recipe.Host:
        return HttpResponse('Du får ikke lov')

    if request.method == "POST":
        recipe.delete()
        return redirect('/')
    context = {'recipe':recipe}
    return render(request, 'matapp/delete.html', context)


@login_required
def addToHandleliste(request, pk):
    liste = get_object_or_404(Recipe, id=pk)
    if liste.handleliste.filter(id=request.user.id).exists():
        liste.handleliste.remove(request.user.id)
    else:
        liste.handleliste.add(request.user.id)
    return redirect('home')


@login_required(login_url='login')
def handleliste(request, pk):
    bruker = User.objects.get(id=pk)
    iListe = Recipe.objects.all()
    context = {'iListe':iListe, 'bruker':bruker}
    return render(request, 'matapp/handleliste.html', context)


##Det som mangler:
##  bytting mellom dark og light mode
##  kategorisering
##  favorisering uten at siden refreshes?
