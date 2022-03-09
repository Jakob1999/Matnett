
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
    return render(request, 'matapp/browse.html', context)

@login_required(login_url='login')
def myrecipes(request):
    return render(request, 'matapp/myrecipes.html')

@login_required(login_url='login')
def profile(request):
    return render(request, 'matapp/profile.html')


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
