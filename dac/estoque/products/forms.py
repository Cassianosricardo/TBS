from django import forms
from django.forms import inlineformset_factory
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'quantity', 'categorie', 'price', 'vendable']     

    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     quantity = cleaned_data.get('quantity')
    #     if self.type in 'edit':
                    
    #             self.add_error('nome', 'Nome já existente.')
    #     elif (Agregacao.objects.get_by_nome_and_grupo(nome, self.grupo)): # Add
    #             self.add_error('nome', 'Nome já existente.')
    #     return cleaned_data


