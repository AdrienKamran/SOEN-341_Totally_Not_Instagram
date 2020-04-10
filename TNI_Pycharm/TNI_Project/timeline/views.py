from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from timeline.forms import userProfileForm,userForm, ImageForm, CommentForm
from timeline.models import Image, Comment, userProfile, userFollowers
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

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


def viewuserprofile(request):
    if request.method == 'POST' and request.user.is_authenticated == True:
        userObj = User.objects.get(username=request.POST['targetUser'])
        profile = userProfile.objects.get(user=userObj)

        followingObj = list(userFollowers.objects.filter(followedUser=userObj, followerUser=request.user))
        userPosts = []
        if(len(followingObj) != 0):
            userPosts = list(Image.objects.filter(user=userObj))

        numFollowers = len(list(userFollowers.objects.filter(followedUser=userObj)))
        numFollowed = len(list(userFollowers.objects.filter(followerUser=userObj)))
        numposts = len(list(Image.objects.filter(user=request.user)))

        context = {
            'profile': profile,
            'numFollowers': numFollowers,
            'numFollowed': numFollowed,
            'numposts': numposts,
            'posts': userPosts,
            'comments': Comment.objects.all(),
        }
        return render(request, "timeline/profile.html", context)
    return render(request, "timeline/profile.html")

def viewuserfollow(request):
    if request.method == 'POST' and request.user.is_authenticated == True:
        userObj = User.objects.get(username=request.POST['targetUser'])
        followingObj = list(userFollowers.objects.filter(followedUser=userObj, followerUser=request.user))
        if(len(followingObj) == 0):
            newFollow = userFollowers(followedUser=userObj, followerUser=request.user)
            newFollow.save()
        return viewuserprofile(request)

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
           userPro = userProfile(user=user)
           userPro.save()
           newFollow = userFollowers(followedUser=user, followerUser=user)
           newFollow.save()

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
            #imgObj = Image.objects.get(name=request.POST['img'])
            imgObj = get_object_or_404(Image, name=request.POST['img'])
            print(request.POST['img'])
            comObj.user = request.user
            comObj.img = imgObj
            comObj.save()
            print("Comment Created: ", request.POST)
        else:
            print("Comment Failed")
    return redirect(reverse('timeline-home'))

def about(request):
    return HttpResponse("<h1>This is the About page.<h1>")
    


