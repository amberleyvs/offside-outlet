from django import forms
from .models import Product
from .models import Car

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'thumbnail', 'category', 'is_featured', 'discount', 'is_limited']
    
class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'brand', 'stock']