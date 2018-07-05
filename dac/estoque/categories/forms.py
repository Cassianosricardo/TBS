from django import forms
from .models import Categorie


class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['name']
