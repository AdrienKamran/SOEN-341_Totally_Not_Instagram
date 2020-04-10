from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='timeline-base'),
    path('login/', views.signIn, name='user-login'),
    path('home/login/', views.signIn, name='user-login'),
    path('logout/', views.signOut, name='user-logout'),
    path('home/logout/', views.signOut, name='user-logout'),
    path('home/', views.home, name='timeline-home'),
    path('registration/', views.register, name='user-registration'),
    path('registration/registeruser/', views.registerUser, name='user-registration'),
    path('home/imageupload/', views.image_view, name='image_view'),
    path('home/like/', views.image_like, name='image_like'),
    path('home/comment/', views.image_comment, name='image_comment'),
    path('home/profile/', views.viewuserprofile, name='timeline-profile'),
    path('home/profile/follow/', views.viewuserfollow, name='timeline-follow'),
    path('home/profile/comment/', views.image_comment, name='profile_image_comment'),
    path('home/profile/like/', views.image_like, name='profile_image_like'),


    path('about/', views.about, name='timeline-about'),
    

]
