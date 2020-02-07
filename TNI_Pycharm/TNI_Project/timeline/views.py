from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.

posts = [
    {
        'author': 'Adrien Kamran',
        'caption': 'This is a test post!',
        'timestamp': '2/2/2020'
    },
    {
        'author': 'Nicolas Kamran',
        'caption': 'This is the second test post!',
        'timestamp': '2/2/2020'
    }
]

def index(request):
    context = {
       'posts': posts
    }
    return render(request, "timeline/base.html",context)

def home(request):
    context = {
       'posts': posts
    }
    return render(request, "timeline/home_test.html",context)

def register(request):
        form = forms.registrationForm()
        return render(request, 'timeline/user_registration.html', {'form':form})

def about(request):
    return HttpResponse("<h1>This is the About page.<h1>")
