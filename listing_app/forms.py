from django import forms
from django.forms import ModelForm
from .models  import Order
from django.contrib.auth.models import User

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ('customer', 'date_created')

# class OrderForm(forms.Form):
    
#     class Meta:
#         model = Order
#         exclude = ('customer',)

