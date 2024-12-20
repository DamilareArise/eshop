from django import forms
from .models import Product

class CreateProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'image',
            'category'
        ]