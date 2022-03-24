#from json import load
from turtle import title
from urllib import response
from django.test import RequestFactory, TestCase
from django.contrib.auth.models import AnonymousUser, User

from matapp.views import deleteRecipe
from .models import Recipe
from django.utils import timezone
from django.test.utils import setup_test_environment
import datetime
from .views import *


CONST_PIZZA_TODO = 'Sett på ovn\nRull ut deig\nTa på fyll\nStrø over ost\nStek'
CONST_PIZZA_ITEM = 'Pizzadeig, tomatsaus, skinke, ost'
TIME = datetime.datetime.now()
PICTURE = 'defaultRecipe.jpg'



def create_recipe(title, description, ingredients, date_created,bilde):
    """Lager en oppskrift som brukes i testingen

    Args:
        title (Charfield): Tittel/navn på retten
        description (Textfield): fremgangsmåte
        ingredients (Textfield): ingredienser
        date_created (DateTIMEField):
    """
    return Recipe.objects.create(title = title, ingredients = ingredients,
                                 date_created=date_created, description = description,bilde=bilde)

        
class CreateRecipeObject(TestCase):
    
    def test_add_recipe(self):
        """
        Sjekker at tittel og andre deler i modellen oppfører seg som forventet.
        TODO
        Burde lage test som baserer seg på PK?

        """
        recipe = create_recipe('pizza', CONST_PIZZA_TODO, CONST_PIZZA_ITEM,TIME,PICTURE)        
        self.assertEqual(recipe.title,'pizza')
        recipe_two = create_recipe('taco','Stek kjøttdeig og krydder\nKutt opp grønnsaker\nS',
                                   'Kjøttdeig, salat, ost, tortilla',TIME,None)
        self.assertEqual(recipe.title,'pizza')
        self.assertEqual(recipe_two.title,'taco')
        self.assertEqual(recipe.description, CONST_PIZZA_TODO)
        self.assertEqual(recipe.ingredients, CONST_PIZZA_ITEM) 
        self.assertNotEqual(recipe.title,'taco')
        
    def test_edit_recipe(self):
        """
        Endring av en recipe. Endrer variabler hver for seg. 
        """
        recipe = create_recipe('pizza', CONST_PIZZA_TODO ,CONST_PIZZA_ITEM,TIME,None)
        recipe_two = create_recipe('taco','Stek kjøttdeig og krydder\nKutt opp grønnsaker\nS',
                                   'Kjøttdeig, salat, ost, tortilla',TIME,None)
        self.assertEqual(recipe.title,'pizza')
        recipe.title = 'Mafiapannekake'
        recipe_two.desciption = 'Alle kan lage taco'
        self.assertNotEqual(recipe.title,'pizza')
        self.assertEqual(recipe.title,'Mafiapannekake')
        self.assertEqual(recipe_two.desciption, 'Alle kan lage taco')
        

    