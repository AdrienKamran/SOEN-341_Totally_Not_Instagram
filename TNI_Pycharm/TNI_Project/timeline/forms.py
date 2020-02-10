from django import forms
from django.contrib.auth.models import User
from timeline.models import userProfile, Image

class userForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model = User
        fields = ('username','email','password')

class userProfileForm(forms.Form):

    class Meta():
        model = userProfile
        fields = ('portfolio','picture')

class ImageForm(forms.ModelForm):
    class Meta():
        model = Image
        fields = ('name', 'Img')
