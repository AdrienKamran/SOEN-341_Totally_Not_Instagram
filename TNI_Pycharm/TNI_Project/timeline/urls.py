from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='timeline-home'),
    path('about/', views.about, name='timeline-about'),
]