from django.test import TestCase

from matapp.views import deleteRecipe
from .models import Recipe
from django.utils import timezone
import datetime

# Create your tests here.

CONST_PIZZA_TODO = 'Sett på ovn\nRull ut deig\nTa på fyll\nStrø over ost\nStek'
CONST_PIZZA_ITEM = 'Pizzadeig, tomatsaus, skinke, ost'

def create_recipe(title, description, ingredients, date_created):
    """Lager en oppskrift som brukes i testingen

    Args:
        title (Charfield): Tittel/navn på retten
        description (Textfield): fremgangsmåte
        ingredients (Textfield): ingredienser
        date_created (DateTimeField):
    """
    return Recipe.objects.create(title = title, ingredients = ingredients,
                                 date_created=date_created, description = description)

class CreateRecipe(TestCase):
    def test_add_recipe(self):
        """
        Sjekker at tittel og andre deler i modellen oppfører seg som forventet.
        TODO
        Burde lage test som baserer seg på PK?
        """
        time = timezone.localdate()
        recipe = create_recipe('pizza', CONST_PIZZA_TODO, CONST_PIZZA_ITEM,time)
        recipe_two = create_recipe('taco','Stek kjøttdeig og krydder\nKutt opp grønnsaker\nS',
                                   'Kjøttdeig, salat, ost, tortilla',time)
        self.assertEqual(recipe.title,'pizza')
        self.assertEqual(recipe_two.title,'taco')
        self.assertEqual(recipe.description, CONST_PIZZA_TODO)
        self.assertEqual(recipe.ingredients, CONST_PIZZA_ITEM) 
        self.assertEqual(recipe.date_created, time)
        self.assertNotEqual(recipe.title,'taco')
        
    def test_edit_recipe(self):
        """
        Endring av en recipe. Endrer variabler hver for seg. 
        """
        time = timezone.localdate()
        recipe = create_recipe('pizza', CONST_PIZZA_TODO ,CONST_PIZZA_ITEM,time)
        recipe_two = create_recipe('taco','Stek kjøttdeig og krydder\nKutt opp grønnsaker\nS',
                                   'Kjøttdeig, salat, ost, tortilla',time)
        self.assertEqual(recipe.title,'pizza')
        recipe.title = 'Mafiapannekake'
        recipe_two.desciption = 'Alle kan lage taco'
        self.assertNotEqual(recipe.title,'pizza')
        self.assertEqual(recipe.title,'Mafiapannekake')
        self.assertEqual(recipe_two.desciption, 'Alle kan lage taco')
        
"""     def test_delete_recipe(self):
        time = timezone.localdate()
        recipe = create_recipe('pizza', CONST_PIZZA_TODO ,CONST_PIZZA_ITEM,time)
        self.assertIsNotNone(recipe)
        Recipe.objects.all().delete()
        self.assertIsNone(recipe)
        self.assertIsNone(recipe.title) """