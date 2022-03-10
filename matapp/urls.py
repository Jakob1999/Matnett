from . import views
from django.urls import URLPattern, path

urlpatterns = [
    path('', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('browse/', views.browse, name="home"),
    path('myRecipes/<str:pk>', views.myRecipes, name='myRecipes'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('profile/favorites/<str:pk>', views.favorites, name='favorites'),
    path('alert/', views.alert),
    path('recipe/', views.recipe),
    path('addRecipe/', views.addRecipe, name="addRecipe"),
    path('editRecipe/<str:pk>/', views.editRecipe, name="editRecipe"),
    path('recipe/<str:pk>/', views.recipe, name="recipe"),
    path('deleteRecipe/<str:pk>/', views.deleteRecipe, name="deleteRecipe"),
    path('addFavorite/<int:pk>/', views.addFavorite, name="addFavorite"),

    
]
