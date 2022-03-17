from django.test import TestCase

from matapp.views import deleteRecipe
from .models import Recipe
from django.utils import timezone
from django.test.utils import setup_test_environment
import datetime


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
        
        
class DatabaseTesting(TestCase):
    def create_recipe(self):
        """
        Lagrer et objekt i databasen.
        """
        recipe = Recipe('pizza',CONST_PIZZA_TODO,CONST_PIZZA_ITEM,TIME,PICTURE)
        recipe.save()
        self.assertEqual(recipe.objects.title,'pizza')
        self.assertEqual(recipe.objects.description,CONST_PIZZA_TODO)
        self.assertEqual(recipe.objects.ingredients,CONST_PIZZA_ITEM)
        self.assertEqual(recipe.objects.date_created,TIME)
        
        
    def edit_recipe(self):
        recipe = Recipe('pizza',CONST_PIZZA_TODO,CONST_PIZZA_ITEM,TIME,)
        recipe.save()
        recipe.objects.title = 'Mafiapannekake'
        recipe.save()
        self.assertNotEqual(recipe.objects.title,'pizza')
        self.assertEqual(recipe.objects.title,'Mafiapannekake')
        recipe.objects.ingredients = 'hvetemel,ost,tomat'
        recipe.save()
        self.assertEqual(recipe.objects.ingredients, 'hvetemel,ost,tomat')
        
    def delete_recipe(self):
        recipe = Recipe('pizza',CONST_PIZZA_TODO,CONST_PIZZA_ITEM,TIME,None)
        recipe.save()
        recipe2 = Recipe('pizza2',CONST_PIZZA_TODO,CONST_PIZZA_ITEM,TIME,None)
        recipe2.save()
        recipe.delete()
        self.assertIsNone(recipe.objects.title)
        self.assertIsNotNone(recipe2.objects.title)