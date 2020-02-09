from django.shortcuts import render
from django.http import HttpResponse

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
    },

    {
        'author': 'Qandeel Arshad',
        'caption': 'This is the third test post!',
        'timestamp': '3/2/2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, "timeline/home_test.html", context)
def about(request):
    return HttpResponse("<h1>This is the About page.<h1>")