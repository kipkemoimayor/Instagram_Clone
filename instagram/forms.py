from . models import Image,Profile,Comments
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
