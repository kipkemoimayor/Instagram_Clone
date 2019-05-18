from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    title='Home'
    return render(request,"index.html",{"title":title})

@login_required(login_url="/accounts/login/")
def stories(request):
    return render(request,'feeds.html')

@login_required(login_url="/accounts/login/")
def profile(request):
    return render(request,"profile.html")

@login_required(login_url='/accounts/login/')
def uploads(request):
    title='Upload'
    return render(request,"upload.html",{"title":title})
