from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def browse(req):
    return render(req, 'matapp/browse.html')

