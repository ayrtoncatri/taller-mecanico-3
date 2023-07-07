from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Producto

class CustomUserCreationForm(UserCreationForm):
    definicion = forms.CharField(label='Explique brevemente su problema', widget=forms.Textarea(attrs={'rows': 4}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2','definicion']



class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'