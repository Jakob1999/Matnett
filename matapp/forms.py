from xml.etree.ElementInclude import include
from .models import Recipe
from django import forms

class RecipeForm(forms.ModelForm):
     ingredients = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={"placeholder": "Paprika 1 stk\nRis 2 dl\nKjøttdeig 1 pakke"}
        ))
     class Meta:
        model = Recipe
        fields = ['title','description', 'avatar', 'ingredients']