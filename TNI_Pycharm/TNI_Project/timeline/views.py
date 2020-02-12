from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from django.contrib.auth.models import User
from timeline.forms import userProfileForm,userForm, ImageForm
from timeline.models import Image
from django.views.generic import ListView

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

def oldhome(request):
    context = {
       'posts': posts
    }
    return render(request, "timeline/home_test.html",context)

def register(request):
        form = forms.userForm()
        return render(request, 'timeline/user_registration.html', {'form':form})

def about(request):
    return HttpResponse("<h1>This is the About page.<h1>")

def registerUser(request):
    print("Register User Called")
    registered = False

    if request.method == "POST":

       user_registration = userForm(data=request.POST)

       if user_registration.is_valid():

           user = user_registration.save()
           user.set_password(user.password)
           user.save()
           registered = True
       else:
          print(user_registration.errors)
    else:
         user_registration = userForm()
    return render(request, 'timeline/base.html',
                           {'user_registration':user_registration,
                            'registered':registered})

# For Images Model
def image_view(request):
    if request.method == 'POST' and request.FILES['Img']:
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            print("SUCCESS IS COMING")
            form.save()
            return HttpResponse('successfully uploaded')
        else:
            print("FAILURE IS COMING")
    else:
        form = ImageForm()
        print("Even the post and files failed")
    return render(request, 'home_test.html', {'form' : form})

def home(request):
    model = Image
    context = {
       'posts': model.objects.all()
    }
    return render(request, "timeline/home_test.html",context)
