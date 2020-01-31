#Update default models to interact with the costumized forms

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

#Overriding the defaults forms classes
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')
    
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model  = CustomUser
        fields = UserChangeForm.Meta.fields
        