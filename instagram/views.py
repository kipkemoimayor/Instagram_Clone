from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import PostImage,EditProfile
from .models import Image,Profile

# Create your views here.

def index(request):
    title='Home'
    return render(request,"index.html",{"title":title})

@login_required(login_url="/accounts/login/")
def stories(request):
    try:
        images=Image.objects.all()
    except Exception as e:
        raise Http404()
    return render(request,'feeds.html',{"images":images})

@login_required(login_url="/accounts/login/")
def profile(request):
    try:
        current_user=request.user.id
        profile_photos=Image.objects.filter(userId=current_user)
    except Exception as e:
        raise Http404()

    return render(request,"profile.html",{'profile':profile_photos})

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
        return redirect("profile")
    else:
        form=PostImage()
    return render(request,"upload.html",{"title":title,"form":form})
@login_required(login_url='/accounts/login/')
def edit(request):
    if request.method=='POST':
        form=EditProfile(request.POST,request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.save()
        return redirect("profile")
    else:
        form=EditProfile()
    return render(request,"edit.html",{"form":form})
