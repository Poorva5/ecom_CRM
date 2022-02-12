from django.forms import ModelForm
from .models import  Customer, Order
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'product', 'status']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']