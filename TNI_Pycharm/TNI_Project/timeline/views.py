from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from timeline.forms import userProfileForm,userForm, ImageForm, CommentForm
from timeline.models import Image, Comment
from django.views.generic import ListView

# Create your views here.

def index(request):
    return render(request, "timeline/base.html")

def signIn(request):
    if request.user.is_authenticated:
        return redirect(reverse('timeline-home'))

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('timeline-home'))
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'timeline/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'timeline/login.html', {'form': form})


def signOut(request):
    if request.user.is_authenticated == False:
        return redirect(reverse('timeline-base'))

    logout(request)
    return redirect(reverse('timeline-base'))

def home(request):
    if request.user.is_authenticated == False:
        return redirect(reverse('timeline-base'))
    
    model = Image
    modelComment = Comment
    context = {
       'posts': model.objects.all(),
       'comments': modelComment.objects.all(),
    }
    return render(request, 'timeline/home_test.html',context)

def register(request):
    form = forms.userForm()
    return render(request, 'timeline/user_registration.html', {'form':form})

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
            imgObj = form.save(commit=False)
            imgObj.user = request.user
            imgObj.save()
            print(request.user)
            
            return redirect(reverse('timeline-home'))

    #return render(request, 'home_test.html', {'form' : form})
    return redirect(reverse('timeline-home'))

def image_like(request):
    if request.method == 'POST' and request.user.is_authenticated == True:
        imgObj = Image.objects.get(name=request.POST['name'])
        imgObj.likes += 1
        imgObj.save()
    return redirect(reverse('timeline-home'))

def image_comment(request):
    if request.method == 'POST' and request.user.is_authenticated == True:
        print(request.POST)
        form = CommentForm(request.POST)

        if form.is_valid():
            comObj = form.save(commit=False)
            imgObj = Image.objects.get(name=request.POST['img'])
            comObj.user = request.user
            comObj.img = imgObj
            comObj.save()
            print("Comment Created: ", request.POST)
        else:
            print("Comment Failed")
    return redirect(reverse('timeline-home'))

def about(request):
    return HttpResponse("<h1>This is the About page.<h1>")