# -*- coding: utf-8 *-*
from django.forms import ModelForm, TextInput, DateInput
from apps.stock.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        widgets = {
            'manufactured_date': DateInput(
                attrs={'placeholder': 'aaaa-mm-dd'}
            ),
            'expiracy_date': DateInput(
                attrs={'placeholder': 'aaaa-mm-dd'}
            ),
            'shipped_date': DateInput(
                attrs={'placeholder': 'aaaa-mm-dd'}
            ),
            'weight': TextInput(
                attrs={'placeholder': 'In grams'}
            ),
        }
