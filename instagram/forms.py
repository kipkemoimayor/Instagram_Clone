from . models import Image,Profile,Comments,Followers
from django import forms

class PostImage(forms.ModelForm):
    class Meta:
        model=Image
        exclude=['likes','comments','date','user','userId','profile']
class EditProfile(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['userId']

class UpdateProfile(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['userId']

class CommentForm(forms.ModelForm):
    # comment=models.CharField(max_length=30)
    class Meta:
        model=Comments
        exclude=['user','images']

class Likes(forms.ModelForm):
    class Meta:
        model=Image
        exclude=['likes','comments','date','user','userId','profile','image','name','caption']

class FormFollow(forms.ModelForm):
    class Meta:
        model=Followers
        exclude=['user','insta','user_id']
