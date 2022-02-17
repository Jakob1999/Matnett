from . import views
from django.urls import URLPattern, path

urlpatterns = [
    path('', views.browse, name="home"),
    path('myrecipes/', views.myrecipes),
    path('profile/', views.profile),
    path('alert/', views.alert),
    path('recipe/', views.recipe),
    path('addRecipe/', views.addRecipe, name="addRecipe"),
    path('editRecipe/<str:pk>/', views.editRecipe, name="editRecipe"),
    path('recipe/<str:pk>/', views.recipe, name="recipe"),
    path('deleteRecipe/<str:pk>/', views.deleteRecipe, name="deleteRecipe"),
    
]
