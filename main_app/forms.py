from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main_app.models import *



class Cs_UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class SearchForm(forms.Form):
    name = forms.CharField(max_length=100,required=True)
    