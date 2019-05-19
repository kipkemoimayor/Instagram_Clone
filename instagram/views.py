from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import PostImage,EditProfile,UpdateProfile,CommentForm,Likes
from .models import Image,Profile,Comments
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    title='Home'
    return render(request,"index.html",{"title":title})

@login_required(login_url="/accounts/login/")
def stories(request):
    try:
        current_user=request.user.id
        images=Image.objects.all()
        profile_image=Profile.objects.all()
        profile=profile_image.reverse()[0:1]
        users=User.objects.all()
        comments=Comments.objects.all()
        #comments
    except Exception as e:
        raise Http404()


    return render(request,'feeds.html',{"images":images,"profile":profile,"users":users,"comments":comments})

@login_required(login_url="/accounts/login/")
def profile(request):
    try:
        current_user=request.user.id
        profile_photos=Image.objects.filter(userId=current_user)
        profile_image=Profile.objects.filter(userId=current_user).all()
        profile=profile_image.reverse()[0:1]

    except Exception as e:
        raise Http404()

    return render(request,"profile.html",{'profile':profile_photos,"pic":profile})

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
    current_user_id=request.user.id
    profile=Profile.objects.filter(userId=current_user_id)
    if len(profile)<1:

        if request.method=='POST':
            form=EditProfile(request.POST,request.FILES)
            if form.is_valid():
                profile=form.save(commit=False)
                profile.userId=current_user_id
                profile.save()
            return redirect("profile")
        else:
            form=EditProfile()
            return render(request,"edit.html",{"form":form})
    else:
        if request.method=='POST':
            form=EditProfile(request.POST,request.FILES )
            if form.is_valid():
                profile=form.save(commit=False)
                bio=form.cleaned_data['bio']
                pic=form.cleaned_data['pic']
                update=Profile.objects.filter(userId=current_user_id).update(bio=bio,pic=pic)
                profile.userId=current_user_id
                profile.save(update)
            return redirect("profile")
        else:

            form=EditProfile()

            return render(request,"edit.html",{"form":form})

def comments(request,image_id):
    try:
        image=Image.objects.filter(id=image_id).all()
        comment=Comments.objects.filter(images=image_id).all()
    except Exception as e:
        raise  Http404()

    imag=Image.objects.filter(id=image_id).all()
    # a=imag[4]
    count=0
    for i in imag:
        count+=i.likes

    if request.method=='POST':
        form=Likes(request.POST)
        k=request.POST.get("like","")
        if k:

            like=int(k)
            if form.is_valid:
                likes=form.save(commit=False)
                all=count+like
                Image.objects.filter(id=image_id).update(likes=all)
                return redirect('comment',image_id)
    else:
        forms=Likes()
    if request.method=='POST':
        current_user=request.user
        i=request.POST.get("id","")
        form=CommentForm(request.POST)
        if form.is_valid:
            comments=form.save(commit=False)
            comments.user=current_user
            comments.images=i
            comments.save()
            return redirect('comment',image_id)
    else:
        form=CommentForm()
    return render(request,"comment.html",{"images":image,'form':form,"comments":comment,"count":count,"forms":forms})

def other_users(request,user_id):
    
    return render(request,"other.html")
