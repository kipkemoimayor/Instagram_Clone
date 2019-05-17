from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    title='Home'
    return render(request,"index.html",{"title":title})


def stories(request):
    return render(request,'feeds.html')
