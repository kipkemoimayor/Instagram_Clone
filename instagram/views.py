from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import PostImage
from .models import Image,Profile

# Create your views here.

def index(request):
    title='Home'
    return render(request,"index.html",{"title":title})

@login_required(login_url="/accounts/login/")
def stories(request):
    return render(request,'feeds.html')

@login_required(login_url="/accounts/login/")
def profile(request):
    profile_photos=Image.objects.filter()
    return render(request,"profile.html")

@login_required(login_url='/accounts/login/')
def uploads(request):
    title='Upload'
    current_user=request.user
    current_user_id=request.user.id
    if request.method=='POST':
        form=PostImage(request.POST,request.FILES)
        if form.is_valid():
            image=form.save(commit=False)
            image.user=current_user
            image.userId=current_user_id
            image.profile=current_user_id
            image.save()
        return redirect("uploads")
    else:
        form=PostImage()
    return render(request,"upload.html",{"title":title,"form":form})
