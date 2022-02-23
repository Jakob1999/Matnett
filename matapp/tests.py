from django.test import TestCase
from .models import Recipe
from django.utils import timezone

# Create your tests here.


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
        recipe = create_recipe('pizza','Sett på ovn\nRull ut deig\nTa på fyll\nStrø over ost\nStek'
                               ,'Pizzadeig, tomatsaus, skinke, ost',timezone.now())
        self.assertEqual(recipe.title,'pizza')