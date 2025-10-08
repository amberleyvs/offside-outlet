from django import forms
from .models import Product, Car
from django.utils.html import strip_tags

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 
                  'price', 
                  'description', 
                  'thumbnail', 
                  'category', 
                  'is_featured', 
                  'discount', 
                  'is_limited',
                  'stock']

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price is not None and price < 0:
            raise forms.ValidationError("Price cannot be negative.")
        return price
    
    def clean_stock(self):
        stock = self.cleaned_data.get("stock", 0)
        if stock is None or stock < 0:
            raise forms.ValidationError("Stock cannot be negative.")
        return stock
    
    def clean_discount(self):
        d = self.cleaned_data.get("discount") or 0
        if not (0 <= d <= 100):
            raise forms.ValidationError("Discount must be between 0 and 100.")
        return d
    
class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'brand', 'stock']