from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts

# Create your views here.


def home(request):
    con = {
        "posts": Posts.objects.all(),
    }
    return render(request, "blogs/home.html", con)


def about(request):
    return render(request, "blogs/about.html")
