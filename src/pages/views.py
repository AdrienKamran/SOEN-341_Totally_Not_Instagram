from django.shortcuts import render
#Make generic a render template
from django.views.generic import TemplateView



class HomePageView(TemplateView):
    #HTML web page
    template_name = 'index.html'
    title = 'HOME'