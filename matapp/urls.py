from . import views
from django.urls import URLPattern, path

urlpatterns = [
    path('', views.browse),
    path('myrecipes/', views.myrecipes),
    path('profile/', views.profile),
    path('alert/', views.alert),
    path('recipe/', views.recipe)
]