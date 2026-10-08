from django.shortcuts import render
from django.http import HttpResponse
# all the logical part of this app is staying here
# Create your views here.


def home(request):
    return render(request, "home/index.html")

def contact(request):
    return render(request, "home/contact.html")

def about(request):
    return render(request, "home/about.html")
