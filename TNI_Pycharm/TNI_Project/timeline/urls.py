from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='timeline-base'),
    path('about/', views.about, name='timeline-about'),
    path('registration/', views.register, name='user-registration'),
    path('registration/registeruser/', views.registerUser, name='user-registration'),
    path('home/', views.home, name='timeline-home'),
    path('home/imageupload/', views.image_view, name='image_view'),

]
