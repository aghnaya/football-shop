from django import forms
from .models import Product

class AddForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'category', 'thumbnail', 'is_featured']